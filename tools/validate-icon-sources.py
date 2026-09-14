#!/usr/bin/env python3
"""Validate incremental Witcher3-HyDE source artwork.

Unlike the release builder, this validator intentionally accepts an incomplete
source tree so artwork can be added in reviewed batches. Every SVG that does
exist must already obey the final matrix path and SVG contract. Once all 645
canonical SVGs exist, the validator automatically runs the full staging path.
"""

from __future__ import annotations

from collections import Counter
import importlib.util
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = ROOT / "tools/build-icons.py"

spec = importlib.util.spec_from_file_location("witcher3_build_icons", BUILDER_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {BUILDER_PATH}")
build_icons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_icons)


def main() -> int:
    try:
        rows = build_icons.read_matrix()
        expected_by_path: dict[Path, dict[str, str]] = {
            build_icons.expected_source_path(row, build_icons.SOURCE_ROOT): row
            for row in rows
        }

        actual = set()
        if build_icons.SOURCE_ROOT.is_dir():
            actual = set(build_icons.SOURCE_ROOT.rglob("*.svg"))

        unexpected = sorted(actual - set(expected_by_path))
        if unexpected:
            rendered = "\n".join(
                f"- {path.relative_to(build_icons.SOURCE_ROOT)}" for path in unexpected
            )
            raise ValueError(
                "Source SVGs exist at paths not owned by the icon matrix:\n" + rendered
            )

        counts: Counter[str] = Counter()
        errors: list[str] = []
        for path in sorted(actual):
            row = expected_by_path[path]
            try:
                build_icons.validate_svg(path)
            except ValueError as exc:
                errors.append(f"{row['id']} ({row['canonical_name']}): {exc}")
            else:
                counts[row["group"]] += 1

        if errors:
            raise ValueError("\n".join(errors))

        present = len(actual)
        missing = build_icons.EXPECTED_DESIGNS - present
        print(
            f"Validated {present} / {build_icons.EXPECTED_DESIGNS} canonical source SVGs; "
            f"{missing} remaining."
        )
        for group in build_icons.GROUP_MAP:
            total = sum(1 for row in rows if row["group"] == group)
            print(f"  {group}: {counts[group]} / {total}")

        if present == build_icons.EXPECTED_DESIGNS:
            print("Artwork set is complete; running the full staging validator.")
            build_icons.validate_sources(rows)
            build_icons.stage_theme(rows)
            build_icons.validate_stage(rows)
            print("Complete source set passed the strict release staging path.")
        else:
            print(
                "Partial artwork is valid. Release packaging remains unavailable "
                "until all 645 canonical SVGs exist."
            )

    except ValueError as exc:
        print(f"Icon source validation failed:\n{exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
