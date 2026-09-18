#!/usr/bin/env python3
"""Build a self-contained SVG-vs-PNG crossover review sheet.

The helper compares one SVG treatment with a detailed raster master.
When <size>.png exists in an optimized directory, that exact-size PNG overrides
master downscaling for the corresponding review size.

It does not create artwork and does not define a final delivery threshold.
"""

from __future__ import annotations

import argparse
import base64
import html
import importlib.util
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "tools/build-icons.py"
DEFAULT_OUTPUT = ROOT / "build/icons/hybrid-crossover-review.html"
SIZES = (32, 48, 64, 96, 128, 256, 512, 1024)
SURFACES = (
    ("w3-canvas", "#0A151E"),
    ("w3-surface", "#171A1C"),
    ("w3-surface-warm", "#1C1813"),
    ("w3-elevated", "#262729"),
    ("light edge-case", "#F2F0EA"),
)
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

spec = importlib.util.spec_from_file_location("witcher3_build_icons", BUILDER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {BUILDER_PATH}")
build_icons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_icons)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 24 or not data.startswith(PNG_SIGNATURE):
        raise ValueError(f"Not a PNG file: {path}")
    if data[12:16] != b"IHDR":
        raise ValueError(f"PNG has no leading IHDR chunk: {path}")
    width, height = struct.unpack(">II", data[16:24])
    if width < 1 or height < 1:
        raise ValueError(f"PNG has invalid dimensions {width}x{height}: {path}")
    return width, height


def data_uri(path: Path, mime: str) -> str:
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{payload}"


def raster_for_size(
    size: int, master: Path | None, optimized_dir: Path | None
) -> tuple[Path | None, str]:
    if optimized_dir is not None:
        optimized = optimized_dir / f"{size}.png"
        if optimized.is_file():
            width, height = png_dimensions(optimized)
            if (width, height) != (size, size):
                raise ValueError(
                    f"Optimized raster must be exactly {size}x{size}: "
                    f"{optimized} is {width}x{height}"
                )
            return optimized, f"optimized {size}.png"

    if master is not None and master.is_file():
        width, height = png_dimensions(master)
        if width != height:
            raise ValueError(f"Raster master must be square: {master} is {width}x{height}")
        if width < size:
            raise ValueError(
                f"Raster master would be upscaled at {size}px: {master} is {width}x{height}"
            )
        return master, f"master downscale ({width}px)"

    return None, "missing raster"


def review_html(
    svg_path: Path,
    raster_master: Path | None,
    optimized_dir: Path | None,
) -> tuple[str, int, list[int]]:
    build_icons.validate_svg(svg_path)
    svg_uri = data_uri(svg_path, "image/svg+xml")
    canonical = html.escape(svg_path.stem)
    rows: list[str] = []
    available = 0
    missing: list[int] = []

    for size in SIZES:
        raster_path, raster_label = raster_for_size(size, raster_master, optimized_dir)
        if raster_path is None:
            missing.append(size)
            raster_uri = ""
        else:
            available += 1
            raster_uri = data_uri(raster_path, "image/png")

        surfaces: list[str] = []
        for surface_name, surface_color in SURFACES:
            raster_markup = (
                f'<img src="{raster_uri}" width="{size}" height="{size}" '
                f'alt="{canonical} raster at {size}px">'
                if raster_uri
                else '<div class="missing">missing PNG</div>'
            )
            surfaces.append(
                f"""
<div class="surface" style="--surface:{surface_color};--review-size:{size}px">
  <div class="surface-name">{html.escape(surface_name)} <code>{surface_color}</code></div>
  <div class="pair">
    <div class="variant">
      <div class="variant-label">SVG</div>
      <img src="{svg_uri}" width="{size}" height="{size}" alt="{canonical} SVG at {size}px">
    </div>
    <div class="variant">
      <div class="variant-label">PNG · {html.escape(raster_label)}</div>
      {raster_markup}
    </div>
  </div>
</div>
"""
            )

        rows.append(
            f"""
<section class="size-row">
  <h2>{size}px</h2>
  <div class="surfaces">{''.join(surfaces)}</div>
</section>
"""
        )

    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Witcher3-HyDE Hybrid Crossover Review · {canonical}</title>
<style>
:root {{ color-scheme: dark; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 28px; background: #0A151E; color: #DEE6F0; }}
main {{ max-width: 1600px; margin: 0 auto; }}
.summary {{ color: #B0B6C2; margin-bottom: 28px; }}
.size-row {{ border: 1px solid #3D3A39; background: #171A1C; padding: 16px; margin: 18px 0; }}
.surfaces {{ display: flex; gap: 12px; overflow-x: auto; align-items: flex-start; padding-bottom: 8px; }}
.surface {{ background: var(--surface); min-height: 150px; border: 1px solid #3D3A39; padding: 10px; flex: 0 0 auto; min-width: max(240px, calc(var(--review-size) * 2 + 56px)); }}
.surface-name {{ font-size: 12px; margin-bottom: 10px; }}
.pair {{ display: grid; grid-template-columns: repeat(2, var(--review-size)); gap: 12px; align-items: end; justify-content: center; }}
.variant {{ min-height: 100px; display: flex; flex-direction: column; gap: 8px; align-items: center; justify-content: flex-end; }}
.variant-label {{ font-size: 11px; color: #B0B6C2; text-align: center; }}
.variant img {{ display: block; object-fit: contain; }}
.missing {{ color: #B72A18; border: 1px dashed #B72A18; padding: 10px; font-size: 12px; }}
code {{ color: inherit; }}
</style>
</head>
<body>
<main>
<h1>Hybrid crossover review · <code>{canonical}</code></h1>
<p class="summary">SVG vs detailed raster · {available}/{len(SIZES)} raster sizes available · test sizes only, not a frozen delivery ladder</p>
{''.join(rows)}
</main>
</body>
</html>
"""
    return document, available, missing


def generate_review(
    svg_path: Path,
    raster_master: Path | None,
    optimized_dir: Path | None,
    output: Path,
) -> tuple[int, list[int]]:
    document, available, missing = review_html(svg_path, raster_master, optimized_dir)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    return available, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--svg", type=Path, required=True)
    parser.add_argument("--raster-master", type=Path)
    parser.add_argument("--optimized-dir", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--require-raster",
        action="store_true",
        help="fail when any comparison size has no raster source",
    )
    args = parser.parse_args()

    try:
        available, missing = generate_review(
            args.svg, args.raster_master, args.optimized_dir, args.output
        )
    except (OSError, ValueError) as exc:
        print(f"Hybrid review generation failed:\n{exc}", file=sys.stderr)
        return 1

    print(f"Wrote hybrid review: {args.output}")
    print(f"Raster comparison sizes available: {available} / {len(SIZES)}")
    if missing:
        print("Missing raster comparison sizes: " + ", ".join(f"{s}px" for s in missing))
        if args.require_raster:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
