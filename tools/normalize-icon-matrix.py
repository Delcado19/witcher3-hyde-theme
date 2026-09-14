#!/usr/bin/env python3
"""Normalize the Witcher3 icon matrix and regenerate its Markdown mirror.

The CSV file is the source of truth. This tool performs deterministic data
hygiene only; it does not invent aliases or broadly rename applications.
"""

from __future__ import annotations

import argparse
import csv
import io
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
MD_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.md"

FIELDNAMES = [
    "id",
    "group",
    "canonical_name",
    "witcher_concept",
    "style_class",
    "priority",
    "aliases",
    "notes",
]

# The Freedesktop Icon Naming Specification defines audio-volume-* as Status
# icons, not Actions. Keep W3-409..W3-412 as the canonical status designs and
# use these four previously duplicated Action slots for missing standard Action
# icons instead.
ACTION_REPLACEMENTS = {
    "W3-281": {
        "canonical_name": "address-book-new",
        "witcher_concept": "Fresh contact ledger with a silver clasp and small plus rune",
    },
    "W3-282": {
        "canonical_name": "appointment-new",
        "witcher_concept": "New calendar parchment stamped with a red wax date seal",
    },
    "W3-283": {
        "canonical_name": "call-start",
        "witcher_concept": "Raised communication horn with an alchemy-green start rune",
    },
    "W3-284": {
        "canonical_name": "call-stop",
        "witcher_concept": "Lowered communication horn cut by a Witcher-red stop slash",
    },
}

MD_HEADER = """# Witcher 3 HyDE Icon Matrix v1

**Target: 645 genuinely distinct visual designs before alias expansion.**

## Design classes

- **Hero** — detailed application icons, master at 1024×1024.
- **Glyph** — reduced, high-contrast symbols for Actions, Status, Waybar and small UI sizes.
- **Emblem** — medium-detail family for folders, devices, MIME and categories.

## Priority

- **P0** — first usable HyDE desktop build.
- **P1** — high-value daily-use coverage.
- **P2** — broad coverage.
- **P3** — specialist/lower-priority coverage.

## Counts

| Group | Unique designs |
|---|---:|
| Applications | 220 |
| Actions/UI | 100 |
| Places/Folders | 65 |
| Status/Panel/Waybar | 95 |
| Devices | 45 |
| MIME/Filetypes | 85 |
| Categories/Misc | 35 |
| **Total** | **645** |

## Alias policy

Aliases do **not** count as designs. `canonical_name` owns the artwork; `aliases` become symlinks or generated aliases during the build. Alias coverage in v1 is a seed and will be expanded in a separate validation pass.

## Matrix

| ID | Group | Canonical name | Witcher concept | Class | Priority | Alias seed | Notes |
|---|---|---|---|---|---|---|---|
"""


def read_rows() -> list[dict[str, str]]:
    with CSV_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDNAMES:
            raise SystemExit(
                f"Unexpected CSV columns: {reader.fieldnames!r}; expected {FIELDNAMES!r}"
            )
        return [dict(row) for row in reader]


def normalize_aliases(raw: str, canonical: str) -> str:
    aliases: list[str] = []
    seen: set[str] = set()
    for item in raw.split(";"):
        alias = item.strip()
        if not alias or alias == canonical or alias in seen:
            continue
        seen.add(alias)
        aliases.append(alias)
    return "; ".join(aliases)


def normalize_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    normalized: list[dict[str, str]] = []

    for original in rows:
        row = {field: original.get(field, "").strip() for field in FIELDNAMES}

        replacement = ACTION_REPLACEMENTS.get(row["id"])
        if replacement:
            row.update(replacement)
            row["aliases"] = ""

        row["aliases"] = normalize_aliases(
            row["aliases"], row["canonical_name"]
        )
        normalized.append(row)

    return normalized


def render_csv(rows: list[dict[str, str]]) -> str:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=FIELDNAMES,
        lineterminator="\n",
        extrasaction="raise",
    )
    writer.writeheader()
    writer.writerows(rows)
    return "\ufeff" + buffer.getvalue()


def md_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_markdown(rows: list[dict[str, str]]) -> str:
    lines = [MD_HEADER.rstrip("\n")]
    for row in rows:
        values = [
            row["id"],
            row["group"],
            row["canonical_name"],
            row["witcher_concept"],
            row["style_class"],
            row["priority"],
            row["aliases"],
            row["notes"],
        ]
        lines.append("| " + " | ".join(md_cell(value) for value in values) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="write normalized CSV and regenerated Markdown instead of checking",
    )
    args = parser.parse_args()

    rows = normalize_rows(read_rows())
    expected_csv = render_csv(rows)
    expected_md = render_markdown(rows)

    current_csv = CSV_PATH.read_text(encoding="utf-8")
    current_md = MD_PATH.read_text(encoding="utf-8")

    changed: list[str] = []
    if current_csv != expected_csv:
        changed.append(str(CSV_PATH.relative_to(ROOT)))
    if current_md != expected_md:
        changed.append(str(MD_PATH.relative_to(ROOT)))

    if args.write:
        CSV_PATH.write_text(expected_csv, encoding="utf-8", newline="")
        MD_PATH.write_text(expected_md, encoding="utf-8", newline="")
        if changed:
            print("Normalized:")
            for path in changed:
                print(f"  {path}")
        else:
            print("Icon matrix already normalized.")
        return 0

    if changed:
        print("Icon matrix normalization required:")
        for path in changed:
            print(f"  {path}")
        print("Run tools/normalize-icon-matrix.py --write")
        return 1

    print("Icon matrix CSV and Markdown mirror are normalized and synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
