#!/usr/bin/env python3
"""Build a self-contained visual review sheet for the 14-icon pilot.

The review sheet embeds existing source SVGs as data URIs, renders them at the
mandatory review sizes for their artwork class, and shows them on the Witcher3
dark surfaces plus a generic light edge-case surface.

The tool accepts an incomplete pilot by default so artwork can be reviewed
incrementally. Use --require-all for the final pilot gate.
"""

from __future__ import annotations

import argparse
import base64
import html
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "tools/build-icons.py"
DEFAULT_OUTPUT = ROOT / "build/icons/pilot-review.html"

spec = importlib.util.spec_from_file_location("witcher3_build_icons", BUILDER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {BUILDER_PATH}")
build_icons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_icons)

PILOT = (
    ("W3-409", "audio-volume-high"),
    ("W3-398", "network-wireless-100"),
    ("W3-386", "battery-full"),
    ("W3-221", "document-new"),
    ("W3-228", "edit-copy"),
    ("W3-236", "go-home"),
    ("W3-321", "folder"),
    ("W3-322", "folder-home"),
    ("W3-482", "computer-laptop"),
    ("W3-543", "application-pdf"),
    ("W3-621", "applications-system"),
    ("W3-070", "dolphin"),
    ("W3-082", "konsole"),
    ("W3-083", "kitty"),
)

SIZES = {
    "Glyph": (16, 22, 24, 32, 48),
    "Emblem": (22, 32, 48, 64, 128),
    "Hero": (32, 48, 64, 128, 256, 512),
}

SURFACES = (
    ("w3-canvas", "#0A151E"),
    ("w3-surface", "#171A1C"),
    ("w3-surface-warm", "#1C1813"),
    ("w3-elevated", "#262729"),
    ("light edge-case", "#F2F0EA"),
)


def pilot_rows() -> list[dict[str, str]]:
    rows = build_icons.read_matrix()
    by_id = {row["id"]: row for row in rows}
    selected: list[dict[str, str]] = []

    for row_id, expected_canonical in PILOT:
        row = by_id.get(row_id)
        if row is None:
            raise ValueError(f"Pilot matrix ID missing: {row_id}")
        actual = row["canonical_name"]
        if actual != expected_canonical:
            raise ValueError(
                f"Pilot matrix drift for {row_id}: expected {expected_canonical!r}, "
                f"found {actual!r}"
            )
        if row["style_class"] not in SIZES:
            raise ValueError(
                f"Pilot row {row_id} has unsupported style class "
                f"{row['style_class']!r}"
            )
        selected.append(row)

    return selected


def svg_data_uri(path: Path) -> str:
    build_icons.validate_svg(path)
    payload = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/svg+xml;base64,{payload}"


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def icon_card(row: dict[str, str], source_root: Path) -> tuple[str, bool]:
    path = build_icons.expected_source_path(row, source_root)
    row_id = html.escape(row["id"])
    canonical = html.escape(row["canonical_name"])
    style_class = html.escape(row["style_class"])
    group = html.escape(row["group"])
    concept = html.escape(row["witcher_concept"])

    if not path.is_file():
        return (
            f"""
<section class="icon-card missing">
  <header>
    <div><strong>{row_id}</strong> · <code>{canonical}</code></div>
    <div class="meta">{style_class} · {group}</div>
  </header>
  <p>{concept}</p>
  <div class="missing-box">MISSING SOURCE SVG<br><code>{html.escape(display_path(path))}</code></div>
</section>
""",
            False,
        )

    uri = svg_data_uri(path)
    size_cells = []
    for size in SIZES[row["style_class"]]:
        size_cells.append(
            f'<div class="size-cell"><img src="{uri}" width="{size}" height="{size}" '
            f'alt="{canonical} at {size}px"><span>{size}px</span></div>'
        )
    sizes_html = "".join(size_cells)

    surfaces_html = []
    for label, color in SURFACES:
        surfaces_html.append(
            f"""
<div class="surface" style="--surface:{color}">
  <div class="surface-label">{html.escape(label)} <code>{color}</code></div>
  <div class="sizes">{sizes_html}</div>
</div>
"""
        )

    return (
        f"""
<section class="icon-card">
  <header>
    <div><strong>{row_id}</strong> · <code>{canonical}</code></div>
    <div class="meta">{style_class} · {group}</div>
  </header>
  <p>{concept}</p>
  {''.join(surfaces_html)}
</section>
""",
        True,
    )


def review_html(source_root: Path) -> tuple[str, int, list[str]]:
    rows = pilot_rows()
    cards: list[str] = []
    present = 0
    missing: list[str] = []

    for row in rows:
        card, exists = icon_card(row, source_root)
        cards.append(card)
        if exists:
            present += 1
        else:
            missing.append(f"{row['id']} {row['canonical_name']}")

    document = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Witcher3-HyDE Icon Pilot Review</title>
<style>
:root {{
  color-scheme: dark;
  font-family: Inter, ui-sans-serif, system-ui, sans-serif;
  background: #0A151E;
  color: #DEE6F0;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 32px; background: #0A151E; }}
main {{ max-width: 1500px; margin: 0 auto; }}
h1 {{ margin: 0 0 8px; font-size: 28px; }}
.summary {{ margin: 0 0 28px; color: #B0B6C2; }}
.icon-card {{
  border: 1px solid #3D3A39;
  background: #171A1C;
  margin: 0 0 24px;
  padding: 18px;
}}
.icon-card header {{
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: baseline;
}}
.icon-card p {{ color: #B0B6C2; margin: 8px 0 16px; }}
.meta {{ color: #D58E4D; font-size: 13px; }}
.surface {{
  background: var(--surface);
  border: 1px solid #3D3A39;
  margin-top: 10px;
  min-height: 92px;
  padding: 10px 12px 14px;
}}
.surface-label {{
  color: #DEE6F0;
  font-size: 12px;
  margin-bottom: 10px;
}}
.sizes {{
  display: flex;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 18px;
}}
.size-cell {{
  min-width: 56px;
  min-height: 64px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  gap: 6px;
}}
.size-cell img {{ display: block; object-fit: contain; }}
.size-cell span {{
  color: #B0B6C2;
  background: #0A151ECC;
  padding: 2px 5px;
  font-size: 11px;
}}
.missing {{ border-color: #B72A18; }}
.missing-box {{
  border: 1px dashed #B72A18;
  color: #DEE6F0;
  padding: 24px;
  text-align: center;
  background: #1C1813;
}}
code {{ color: inherit; }}
@media (max-width: 700px) {{
  body {{ padding: 14px; }}
  .icon-card header {{ display: block; }}
}}
</style>
</head>
<body>
<main>
  <h1>Witcher3-HyDE · 14-icon pilot review</h1>
  <p class="summary">{present} / {len(rows)} pilot SVGs present · generated from repository sources · no raster review assets committed</p>
  {''.join(cards)}
</main>
</body>
</html>
"""
    return document, present, missing


def generate_review(source_root: Path, output: Path) -> tuple[int, list[str]]:
    document, present, missing = review_html(source_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(document, encoding="utf-8")
    return present, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-root",
        type=Path,
        default=build_icons.SOURCE_ROOT,
        help="Canonical SVG source root (default: design/icons/src)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Review HTML output path (default: build/icons/pilot-review.html)",
    )
    parser.add_argument(
        "--require-all",
        action="store_true",
        help="Return failure when any of the 14 pilot SVGs is missing",
    )
    args = parser.parse_args()

    try:
        present, missing = generate_review(args.source_root, args.output)
    except ValueError as exc:
        print(f"Pilot review generation failed:\n{exc}", file=sys.stderr)
        return 1

    print(f"Wrote pilot review: {args.output}")
    print(f"Pilot SVGs present: {present} / {len(PILOT)}")
    if missing:
        print("Missing pilot SVGs:")
        for item in missing:
            print(f"- {item}")
        if args.require_all:
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
