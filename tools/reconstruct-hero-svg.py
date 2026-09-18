#!/usr/bin/env python3
"""Perceptually reconstruct a detailed Hero PNG as a real SVG candidate.

The source composition is not redrawn. The tool uses perceptual superpixel
segmentation, palette clustering and contour tracing, then optionally Scour.
No raster image is embedded in the SVG.

Runtime reconstruction dependencies:
  Pillow numpy opencv-python scikit-image scikit-learn
Optional comparison dependency:
  cairosvg
Optional final optimizer:
  scour (python-scour)

Imports are lazy so repository CI can compile/import dependency-free helpers
without installing the optional reconstruction stack.
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
) -> dict[str, int | float | str]:
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

    parts = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {analysis_size} {analysis_size}">'
        ),
        (
            '<g shape-rendering="geometricPrecision" '
            'stroke-linejoin="round" '
            f'stroke-width="{seam_stroke:g}">'
        ),
    ]
    order = sorted(
        range(color_count), key=lambda idx: float(palette[idx].mean())
    )
    emitted_colors = 0
    for palette_index in order:
        paths = grouped[palette_index]
        if not paths:
            continue
        red, green, blue = (
            int(value) for value in palette[palette_index]
        )
        color = f"#{red:02x}{green:02x}{blue:02x}"
        parts.append(
            f'<path fill="{color}" stroke="{color}" '
            f'd="{"".join(paths)}"/>'
        )
        emitted_colors += 1
    parts.append("</g></svg>\n")

    output_svg.parent.mkdir(parents=True, exist_ok=True)
    output_svg.write_text("".join(parts), encoding="utf-8")
    return {
        "analysis_size": analysis_size,
        "requested_segments": segments,
        "actual_segments": int(len(segment_ids)),
        "palette_colors": emitted_colors,
        "polygons": polygon_count,
        "input_bytes": input_png.stat().st_size,
        "svg_bytes_before_optimizer": output_svg.stat().st_size,
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


def render_comparison(
    input_png: Path, svg_path: Path, output_dir: Path
) -> dict[str, object]:
    """Render 256/512 diagnostics; metrics are not acceptance gates."""
    try:
        import io
        import cairosvg  # type: ignore
        import numpy as np  # type: ignore
        from PIL import Image  # type: ignore
        from skimage.metrics import structural_similarity as ssim  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "comparison rendering additionally requires cairosvg, "
            "Pillow, numpy, and scikit-image"
        ) from exc

    output_dir.mkdir(parents=True, exist_ok=True)
    source = Image.open(input_png).convert("RGBA")
    svg_bytes = svg_path.read_bytes()
    background = np.asarray([23, 26, 28], dtype=np.float32)
    results: dict[str, object] = {}

    def composite(array):
        alpha = array[:, :, 3:4].astype(np.float32) / 255.0
        return (
            array[:, :, :3].astype(np.float32) * alpha
            + background * (1.0 - alpha)
        ).astype(np.uint8)

    for size in (256, 512):
        rendered_png = cairosvg.svg2png(
            bytestring=svg_bytes,
            output_width=size,
            output_height=size,
        )
        vector_render = Image.open(
            io.BytesIO(rendered_png)
        ).convert("RGBA")
        target = source.resize(
            (size, size), Image.Resampling.LANCZOS
        )
        a = composite(np.asarray(vector_render))
        b = composite(np.asarray(target))
        score = float(
            ssim(a, b, channel_axis=2, data_range=255)
        )
        mae = float(
            np.abs(
                a.astype(np.float32) - b.astype(np.float32)
            ).mean()
        )
        results[str(size)] = {"ssim": score, "mae": mae}

        board = Image.new(
            "RGB", (size * 2, size), (23, 26, 28)
        )
        board.paste(target, (0, 0), target)
        board.paste(vector_render, (size, 0), vector_render)
        board.save(
            output_dir / f"compare-{size}.png", optimize=True
        )
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
    parser.add_argument("--seam-stroke", type=float, default=0.55)
    parser.add_argument("--no-scour", action="store_true")
    parser.add_argument("--compare-dir", type=Path)
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
            args.input_png, args.output_svg, args.compare_dir
        )

    encoded = json.dumps(report, indent=2, sort_keys=True)
    print(encoded)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(encoded + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
