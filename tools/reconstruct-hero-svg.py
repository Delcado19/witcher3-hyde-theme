#!/usr/bin/env python3
"""Perceptually reconstruct a detailed Hero PNG as a real SVG candidate.

The source composition is not redrawn. The tool uses perceptual superpixel
segmentation, palette clustering and contour tracing, then optionally Scour.
No raster image is embedded in the SVG.

An optional edge-aware surface-smoothing mode keeps the reconstructed vector
geometry but softens low-frequency faceting while restoring strong source
edges through a separately vectorized detail mask.

Runtime reconstruction dependencies:
  Pillow numpy opencv-python scikit-image scikit-learn
Optional comparison dependencies:
  cairosvg or Inkscape
Optional final optimizer:
  scour (python-scour)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
from typing import Sequence

PRESETS = {
    "draft": {
        "segments": 2000, "palette": 80, "compactness": 8.0,
        "sigma": 0.6, "epsilon": 0.50,
    },
    "balanced": {
        "segments": 4000, "palette": 128, "compactness": 7.0,
        "sigma": 0.6, "epsilon": 0.38,
    },
    "fidelity": {
        "segments": 8000, "palette": 192, "compactness": 6.0,
        "sigma": 0.6, "epsilon": 0.28,
    },
}

BRILLIANCE_PRESETS = {
    "off": {"contrast": 1.00, "chroma": 1.00, "highlight": 0.0},
    "mild": {"contrast": 1.07, "chroma": 1.05, "highlight": 1.5},
    "balanced": {"contrast": 1.10, "chroma": 1.07, "highlight": 2.5},
    "punchy": {"contrast": 1.13, "chroma": 1.10, "highlight": 3.5},
}


def relative_polygon_path(points: Sequence[Sequence[int]]) -> str:
    """Serialize one closed polygon using compact relative line segments."""
    if len(points) < 3:
        raise ValueError("a polygon requires at least three points")
    x0, y0 = int(points[0][0]), int(points[0][1])
    parts = [f"M{x0} {y0}"]
    px, py = x0, y0
    deltas: list[str] = []
    for point in points[1:]:
        x, y = int(point[0]), int(point[1])
        deltas.append(f"{x - px} {y - py}")
        px, py = x, y
    if deltas:
        parts.append("l" + " ".join(deltas))
    parts.append("z")
    return "".join(parts)


def preset_config(name: str) -> dict[str, float | int]:
    try:
        return dict(PRESETS[name])
    except KeyError as exc:
        raise ValueError(f"unknown preset: {name}") from exc


def brilliance_config(name: str) -> dict[str, float]:
    try:
        return dict(BRILLIANCE_PRESETS[name])
    except KeyError as exc:
        raise ValueError(f"unknown brilliance preset: {name}") from exc


def _apply_palette_brilliance(
    palette,
    source_rgb,
    source_mask,
    *,
    contrast: float,
    chroma: float,
    highlight: float,
):
    """Restore contrast/chroma compressed by region averaging and clustering.

    The transform operates only on the vector palette. Geometry is unchanged.
    L* contrast is expanded around the source image's visible-pixel mean,
    chroma is scaled in Lab, and only the brightest palette colors receive
    a small highlight lift.
    """
    if (
        abs(contrast - 1.0) < 1e-9
        and abs(chroma - 1.0) < 1e-9
        and abs(highlight) < 1e-9
    ):
        return palette, {
            "lstar_pivot": None,
            "highlight_threshold": None,
        }

    try:
        import numpy as np  # type: ignore
        from skimage.color import lab2rgb, rgb2lab  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "brilliance compensation requires numpy and scikit-image"
        ) from exc

    visible = source_rgb[source_mask].astype(np.float32) / 255.0
    visible_lab = rgb2lab(visible.reshape(-1, 1, 3)).reshape(-1, 3)
    pivot = float(visible_lab[:, 0].mean())

    palette_rgb = palette.astype(np.float32) / 255.0
    palette_lab = rgb2lab(
        palette_rgb.reshape(-1, 1, 3)
    ).reshape(-1, 3)

    original_l = palette_lab[:, 0].copy()
    palette_lab[:, 0] = pivot + contrast * (original_l - pivot)

    highlight_threshold = pivot + 0.42 * (100.0 - pivot)
    ramp = np.clip(
        (original_l - highlight_threshold)
        / max(1.0, 100.0 - highlight_threshold),
        0.0,
        1.0,
    )
    palette_lab[:, 0] += highlight * ramp
    palette_lab[:, 0] = np.clip(palette_lab[:, 0], 0.0, 100.0)
    palette_lab[:, 1] *= chroma
    palette_lab[:, 2] *= chroma

    corrected = lab2rgb(
        palette_lab.reshape(-1, 1, 3)
    ).reshape(-1, 3)
    corrected = np.clip(
        np.rint(corrected * 255.0), 0, 255
    ).astype(np.uint8)
    return corrected, {
        "lstar_pivot": pivot,
        "highlight_threshold": float(highlight_threshold),
    }


def _runtime_modules():
    try:
        import cv2  # type: ignore
        import numpy as np  # type: ignore
        from PIL import Image  # type: ignore
        from skimage.segmentation import slic  # type: ignore
        from sklearn.cluster import KMeans  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "reconstruction requires Pillow, numpy, opencv-python, "
            "scikit-image, and scikit-learn"
        ) from exc
    return cv2, np, Image, slic, KMeans


def _edge_mask_path(
    rgb,
    alpha,
    *,
    threshold: float,
    dilate_iterations: int,
    contour_epsilon: float,
):
    """Return a vectorized mask for strong source-image edges."""
    cv2, np, *_ = _runtime_modules()
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(np.float32)
    grad_x = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
    magnitude = np.sqrt(grad_x * grad_x + grad_y * grad_y) / 4.0
    visible = alpha > 20
    edge_mask = ((magnitude > threshold) & visible).astype(np.uint8) * 255
    if dilate_iterations > 0:
        edge_mask = cv2.dilate(
            edge_mask,
            np.ones((3, 3), dtype=np.uint8),
            iterations=dilate_iterations,
        )
    coverage = float((edge_mask > 0).sum() / max(1, int(visible.sum())))
    contours, _ = cv2.findContours(
        edge_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    paths: list[str] = []
    for contour in contours:
        if cv2.contourArea(contour) < 1.0:
            continue
        approx = cv2.approxPolyDP(contour, contour_epsilon, True)
        points = approx[:, 0, :]
        if len(points) < 3:
            continue
        paths.append(relative_polygon_path(points))
    return "".join(paths), coverage, len(paths)


def _alpha_underlay(
    rgb,
    alpha,
    *,
    alpha_threshold: int,
    contour_epsilon: float = 1.0,
):
    """Build an opaque dark vector underpainting for the visible silhouette.

    Facet paths are individually anti-aliased by SVG renderers. Thousands of
    adjacent paths can therefore expose the desktop background through tiny
    partially transparent seams. A silhouette underpainting keeps those seams
    inside the artwork instead of letting the external background leak through.

    The underlay follows the source alpha topology (including real holes) and
    derives its dark forged-material color from the source image itself.
    """
    cv2, np, *_ = _runtime_modules()
    visible = alpha > alpha_threshold
    binary = visible.astype(np.uint8) * 255
    contours, _ = cv2.findContours(
        binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE
    )
    paths: list[str] = []
    for contour in contours:
        if cv2.contourArea(contour) < 1.0:
            continue
        approx = cv2.approxPolyDP(contour, contour_epsilon, True)
        points = approx[:, 0, :]
        if len(points) < 3:
            continue
        paths.append(relative_polygon_path(points))

    pixels = rgb[visible].astype(np.float32)
    if len(pixels) == 0:
        color = "#000000"
    else:
        luma = (
            0.2126 * pixels[:, 0]
            + 0.7152 * pixels[:, 1]
            + 0.0722 * pixels[:, 2]
        )
        threshold = float(np.percentile(luma, 25.0))
        dark = pixels[luma <= threshold]
        median = np.rint(np.median(dark, axis=0)).astype(np.uint8)
        color = "#{:02x}{:02x}{:02x}".format(
            int(median[0]), int(median[1]), int(median[2])
        )

    return "".join(paths), color, len(paths)


def _emit_svg(
    *,
    analysis_size: int,
    art_paths: str,
    seam_stroke: float,
    smoothing: bool,
    edge_path: str,
    smooth_blur: float,
    smooth_detail_opacity: float,
    underlay_path: str = "",
    underlay_color: str = "#000000",
) -> str:
    underlay = (
        f'<path fill="{underlay_color}" fill-rule="evenodd" '
        f'd="{underlay_path}"/>'
        if underlay_path
        else ""
    )
    facets = (
        '<g shape-rendering="geometricPrecision" '
        'stroke-linejoin="round" '
        f'stroke-width="{seam_stroke:g}">{art_paths}</g>'
    )
    group = underlay + facets
    if not smoothing:
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {analysis_size} {analysis_size}">'
            f'{group}</svg>\n'
        )

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 {analysis_size} {analysis_size}">'
        '<defs>'
        '<filter id="surfaceSoft" x="-5%" y="-5%" width="110%" height="110%">'
        f'<feGaussianBlur stdDeviation="{smooth_blur:g}"/>'
        '</filter>'
        f'<g id="heroArt">{group}</g>'
        f'<mask id="strongEdges" maskUnits="userSpaceOnUse" x="0" y="0" '
        f'width="{analysis_size}" height="{analysis_size}">'
        f'<rect width="{analysis_size}" height="{analysis_size}" fill="#000"/>'
        f'<path d="{edge_path}" fill="#fff"/>'
        '</mask>'
        '</defs>'
        '<use xlink:href="#heroArt" filter="url(#surfaceSoft)"/>'
        '<use xlink:href="#heroArt" mask="url(#strongEdges)"/>'
        f'<use xlink:href="#heroArt" opacity="{smooth_detail_opacity:g}"/>'
        '</svg>\n'
    )


def reconstruct(
    input_png: Path,
    output_svg: Path,
    *,
    analysis_size: int,
    segments: int,
    palette_size: int,
    compactness: float,
    sigma: float,
    epsilon: float,
    alpha_threshold: int,
    min_area: float,
    seam_stroke: float,
    surface_smoothing: bool,
    smooth_blur: float,
    edge_threshold: float,
    edge_dilate: int,
    edge_epsilon: float,
    smooth_detail_opacity: float,
    brilliance: str,
    opaque_underlay: bool,
) -> dict[str, int | float | str | bool | None]:
    cv2, np, Image, slic, KMeans = _runtime_modules()

    source = Image.open(input_png).convert("RGBA")
    resized = source.resize(
        (analysis_size, analysis_size), Image.Resampling.LANCZOS
    )
    rgba = np.asarray(resized)
    rgb = rgba[:, :, :3]
    alpha = rgba[:, :, 3]
    mask = alpha > alpha_threshold
    if not bool(mask.any()):
        raise ValueError("input has no visible pixels above alpha threshold")

    work = rgb.copy()
    work[~mask] = 0
    labels = slic(
        work,
        n_segments=segments,
        compactness=compactness,
        sigma=sigma,
        start_label=0,
        mask=mask,
        channel_axis=-1,
        convert2lab=True,
    )

    segment_ids = np.unique(labels[mask])
    means = []
    weights: list[int] = []
    for sid in segment_ids:
        region = labels == sid
        a = alpha[region].astype(np.float32) / 255.0
        denominator = max(float(a.sum()), 1.0)
        mean = (
            rgb[region].astype(np.float32) * a[:, None]
        ).sum(axis=0) / denominator
        means.append(mean)
        weights.append(int(region.sum()))

    means_array = np.asarray(means)
    color_count = min(palette_size, len(segment_ids))
    kmeans = KMeans(
        n_clusters=color_count, random_state=0, n_init=6, max_iter=200
    )
    kmeans.fit(means_array, sample_weight=np.asarray(weights))
    palette = np.clip(
        np.rint(kmeans.cluster_centers_), 0, 255
    ).astype(np.uint8)
    assignments = kmeans.predict(means_array)

    brilliance_values = brilliance_config(brilliance)
    palette, brilliance_report = _apply_palette_brilliance(
        palette,
        rgb,
        mask,
        contrast=brilliance_values["contrast"],
        chroma=brilliance_values["chroma"],
        highlight=brilliance_values["highlight"],
    )

    grouped: dict[int, list[str]] = {
        idx: [] for idx in range(color_count)
    }
    polygon_count = 0
    for sid, palette_index in zip(segment_ids, assignments):
        region = (labels == sid).astype(np.uint8) * 255
        contours, _ = cv2.findContours(
            region, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        for contour in contours:
            if cv2.contourArea(contour) < min_area:
                continue
            approx = cv2.approxPolyDP(contour, epsilon, True)
            points = approx[:, 0, :]
            if len(points) < 3:
                continue
            grouped[int(palette_index)].append(
                relative_polygon_path(points)
            )
            polygon_count += 1

    order = sorted(
        range(color_count), key=lambda idx: float(palette[idx].mean())
    )
    art_parts: list[str] = []
    emitted_colors = 0
    for palette_index in order:
        paths = grouped[palette_index]
        if not paths:
            continue
        red, green, blue = (
            int(value) for value in palette[palette_index]
        )
        color = f"#{red:02x}{green:02x}{blue:02x}"
        art_parts.append(
            f'<path fill="{color}" stroke="{color}" '
            f'd="{"".join(paths)}"/>'
        )
        emitted_colors += 1

    underlay_path = ""
    underlay_color = "#000000"
    underlay_shapes = 0
    if opaque_underlay:
        underlay_path, underlay_color, underlay_shapes = _alpha_underlay(
            rgb,
            alpha,
            alpha_threshold=alpha_threshold,
        )

    edge_path = ""
    edge_coverage = 0.0
    edge_shapes = 0
    if surface_smoothing:
        edge_path, edge_coverage, edge_shapes = _edge_mask_path(
            rgb,
            alpha,
            threshold=edge_threshold,
            dilate_iterations=edge_dilate,
            contour_epsilon=edge_epsilon,
        )

    svg = _emit_svg(
        analysis_size=analysis_size,
        art_paths="".join(art_parts),
        seam_stroke=seam_stroke,
        smoothing=surface_smoothing,
        edge_path=edge_path,
        smooth_blur=smooth_blur,
        smooth_detail_opacity=smooth_detail_opacity,
        underlay_path=underlay_path,
        underlay_color=underlay_color,
    )

    output_svg.parent.mkdir(parents=True, exist_ok=True)
    output_svg.write_text(svg, encoding="utf-8")
    return {
        "analysis_size": analysis_size,
        "requested_segments": segments,
        "actual_segments": int(len(segment_ids)),
        "palette_colors": emitted_colors,
        "polygons": polygon_count,
        "input_bytes": input_png.stat().st_size,
        "svg_bytes_before_optimizer": output_svg.stat().st_size,
        "seam_stroke": seam_stroke,
        "surface_smoothing": surface_smoothing,
        "edge_mask_coverage": edge_coverage,
        "edge_mask_shapes": edge_shapes,
        "brilliance_preset": brilliance,
        "brilliance_contrast": brilliance_values["contrast"],
        "brilliance_chroma": brilliance_values["chroma"],
        "brilliance_highlight": brilliance_values["highlight"],
        "brilliance_lstar_pivot": brilliance_report["lstar_pivot"],
        "brilliance_highlight_threshold": brilliance_report[
            "highlight_threshold"
        ],
        "opaque_underlay": opaque_underlay,
        "underlay_color": underlay_color if opaque_underlay else None,
        "underlay_shapes": underlay_shapes,
    }


def optimize_with_scour(svg_path: Path) -> bool:
    """Run Scour when installed; absence is non-fatal."""
    executable = shutil.which("scour")
    if not executable:
        return False
    with tempfile.NamedTemporaryFile(
        suffix=".svg", delete=False
    ) as handle:
        temp_path = Path(handle.name)
    try:
        subprocess.run(
            [
                executable,
                "-i", str(svg_path),
                "-o", str(temp_path),
                "--enable-viewboxing",
                "--enable-id-stripping",
                "--enable-comment-stripping",
                "--shorten-ids",
                "--indent=none",
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        temp_path.replace(svg_path)
        return True
    finally:
        temp_path.unlink(missing_ok=True)


def _render_with_inkscape(svg_path: Path, output_png: Path, size: int) -> None:
    executable = shutil.which("inkscape")
    if not executable:
        raise SystemExit("Inkscape renderer requested but inkscape is unavailable")
    subprocess.run(
        [
            executable,
            str(svg_path),
            f"--export-filename={output_png}",
            f"--export-width={size}",
            f"--export-height={size}",
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )


def _render_with_cairosvg(svg_path: Path, output_png: Path, size: int) -> None:
    try:
        import cairosvg  # type: ignore
    except ImportError as exc:
        raise SystemExit("CairoSVG renderer requested but cairosvg is unavailable") from exc
    output_png.write_bytes(
        cairosvg.svg2png(
            bytestring=svg_path.read_bytes(),
            output_width=size,
            output_height=size,
        )
    )


def render_comparison(
    input_png: Path,
    svg_path: Path,
    output_dir: Path,
    *,
    renderer: str,
) -> dict[str, object]:
    """Render 256/512 diagnostics; metrics are not acceptance gates."""
    try:
        import numpy as np  # type: ignore
        from PIL import Image  # type: ignore
        from skimage.metrics import structural_similarity as ssim  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "comparison rendering requires Pillow, numpy, and scikit-image"
        ) from exc

    if renderer == "auto":
        renderer = "inkscape" if shutil.which("inkscape") else "cairosvg"

    output_dir.mkdir(parents=True, exist_ok=True)
    source = Image.open(input_png).convert("RGBA")
    background = np.asarray([23, 26, 28], dtype=np.float32)
    results: dict[str, object] = {"renderer": renderer}

    def composite(array):
        a = array[:, :, 3:4].astype(np.float32) / 255.0
        return (
            array[:, :, :3].astype(np.float32) * a
            + background * (1.0 - a)
        ).astype(np.uint8)

    for size in (256, 512):
        rendered_path = output_dir / f"svg-{size}.png"
        if renderer == "inkscape":
            _render_with_inkscape(svg_path, rendered_path, size)
        elif renderer == "cairosvg":
            _render_with_cairosvg(svg_path, rendered_path, size)
        else:
            raise ValueError(f"unknown comparison renderer: {renderer}")

        vector_render = Image.open(rendered_path).convert("RGBA")
        target = source.resize((size, size), Image.Resampling.LANCZOS)
        a = composite(np.asarray(vector_render))
        b = composite(np.asarray(target))
        score = float(ssim(a, b, channel_axis=2, data_range=255))
        mae = float(
            np.abs(
                a.astype(np.float32) - b.astype(np.float32)
            ).mean()
        )
        results[str(size)] = {"ssim": score, "mae": mae}

        board = Image.new("RGB", (size * 2, size), (23, 26, 28))
        board.paste(target, (0, 0), target)
        board.paste(vector_render, (size, 0), vector_render)
        board.save(output_dir / f"compare-{size}.png", optimize=True)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Perceptually reconstruct a detailed Hero PNG "
            "as a real vector SVG candidate."
        )
    )
    parser.add_argument("input_png", type=Path)
    parser.add_argument("output_svg", type=Path)
    parser.add_argument(
        "--preset", choices=tuple(PRESETS), default="fidelity"
    )
    parser.add_argument("--analysis-size", type=int, default=512)
    parser.add_argument("--segments", type=int)
    parser.add_argument("--palette", type=int)
    parser.add_argument("--compactness", type=float)
    parser.add_argument("--sigma", type=float)
    parser.add_argument("--epsilon", type=float)
    parser.add_argument("--alpha-threshold", type=int, default=20)
    parser.add_argument("--min-area", type=float, default=1.0)
    parser.add_argument("--seam-stroke", type=float, default=1.25)
    parser.add_argument(
        "--no-underlay",
        action="store_true",
        help=(
            "disable the source-alpha silhouette underpainting that prevents "
            "desktop background leakage through anti-aliased facet seams"
        ),
    )
    parser.add_argument("--surface-smoothing", action="store_true")
    parser.add_argument("--smooth-blur", type=float, default=1.1)
    parser.add_argument("--edge-threshold", type=float, default=105.0)
    parser.add_argument("--edge-dilate", type=int, default=1)
    parser.add_argument("--edge-epsilon", type=float, default=0.5)
    parser.add_argument("--smooth-detail-opacity", type=float, default=0.04)
    parser.add_argument(
        "--brilliance",
        choices=tuple(BRILLIANCE_PRESETS),
        default="off",
        help=(
            "optional Lab palette compensation; preserves vector geometry "
            "while restoring contrast, chroma, and bright highlights"
        ),
    )
    parser.add_argument("--no-scour", action="store_true")
    parser.add_argument("--compare-dir", type=Path)
    parser.add_argument(
        "--comparison-renderer",
        choices=("auto", "inkscape", "cairosvg"),
        default="auto",
    )
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = preset_config(args.preset)
    for name in (
        "segments", "palette", "compactness", "sigma", "epsilon"
    ):
        override = getattr(args, name)
        if override is not None:
            config[name] = override

    report = reconstruct(
        args.input_png,
        args.output_svg,
        analysis_size=args.analysis_size,
        segments=int(config["segments"]),
        palette_size=int(config["palette"]),
        compactness=float(config["compactness"]),
        sigma=float(config["sigma"]),
        epsilon=float(config["epsilon"]),
        alpha_threshold=args.alpha_threshold,
        min_area=args.min_area,
        seam_stroke=args.seam_stroke,
        surface_smoothing=args.surface_smoothing,
        smooth_blur=args.smooth_blur,
        edge_threshold=args.edge_threshold,
        edge_dilate=args.edge_dilate,
        edge_epsilon=args.edge_epsilon,
        smooth_detail_opacity=args.smooth_detail_opacity,
        brilliance=args.brilliance,
        opaque_underlay=not args.no_underlay,
    )

    optimized = (
        False
        if args.no_scour
        else optimize_with_scour(args.output_svg)
    )
    report["scour_optimized"] = optimized
    report["svg_bytes_final"] = args.output_svg.stat().st_size
    report["size_ratio_svg_to_png"] = (
        report["svg_bytes_final"] / report["input_bytes"]
    )
    report["preset"] = args.preset

    if args.compare_dir:
        report["comparison"] = render_comparison(
            args.input_png,
            args.output_svg,
            args.compare_dir,
            renderer=args.comparison_renderer,
        )

    encoded = json.dumps(report, indent=2, sort_keys=True)
    print(encoded)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
