#!/usr/bin/env python3
"""Validate structure and namespace integrity of the Witcher3 icon matrix."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"

EXPECTED_COLUMNS = [
    "id",
    "group",
    "canonical_name",
    "witcher_concept",
    "style_class",
    "priority",
    "aliases",
    "notes",
]
EXPECTED_GROUPS = {
    "Applications": 220,
    "Actions/UI": 100,
    "Places/Folders": 65,
    "Status/Panel/Waybar": 95,
    "Devices": 45,
    "MIME/Filetypes": 85,
    "Categories/Misc": 35,
}
EXPECTED_STYLES = {"Hero", "Glyph", "Emblem"}
EXPECTED_PRIORITIES = {"P0", "P1", "P2", "P3"}
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+@:-]*$")


def main() -> int:
    with MATRIX_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise SystemExit(
                f"Unexpected columns: {reader.fieldnames!r}; "
                f"expected {EXPECTED_COLUMNS!r}"
            )
        rows = list(reader)

    if len(rows) != 645:
        raise SystemExit(f"Expected 645 matrix rows, found {len(rows)}")

    ids = [row["id"].strip() for row in rows]
    expected_ids = [f"W3-{index:03d}" for index in range(1, 646)]
    if ids != expected_ids:
        mismatches = [
            f"row {index + 1}: {actual!r} != {expected!r}"
            for index, (actual, expected) in enumerate(zip(ids, expected_ids))
            if actual != expected
        ]
        raise SystemExit("Non-sequential IDs:\n" + "\n".join(mismatches[:20]))

    group_counts = Counter(row["group"].strip() for row in rows)
    if dict(group_counts) != EXPECTED_GROUPS:
        raise SystemExit(
            f"Unexpected group counts: {dict(group_counts)!r}; "
            f"expected {EXPECTED_GROUPS!r}"
        )

    canonical_to_id: dict[str, str] = {}
    alias_to_ids: defaultdict[str, list[str]] = defaultdict(list)
    errors: list[str] = []

    for row in rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        concept = row["witcher_concept"].strip()
        style = row["style_class"].strip()
        priority = row["priority"].strip()
        aliases = [
            item.strip()
            for item in row["aliases"].split(";")
            if item.strip()
        ]

        if not canonical:
            errors.append(f"{row_id}: missing canonical_name")
        elif not NAME_RE.fullmatch(canonical):
            errors.append(f"{row_id}: invalid canonical_name {canonical!r}")

        if not concept:
            errors.append(f"{row_id}: missing witcher_concept")
        if style not in EXPECTED_STYLES:
            errors.append(f"{row_id}: invalid style_class {style!r}")
        if priority not in EXPECTED_PRIORITIES:
            errors.append(f"{row_id}: invalid priority {priority!r}")

        if canonical in canonical_to_id:
            errors.append(
                f"{row_id}: canonical_name {canonical!r} already used by "
                f"{canonical_to_id[canonical]}"
            )
        else:
            canonical_to_id[canonical] = row_id

        if len(aliases) != len(set(aliases)):
            duplicates = sorted(
                name for name, count in Counter(aliases).items() if count > 1
            )
            errors.append(
                f"{row_id}: duplicate aliases within row: {', '.join(duplicates)}"
            )

        for alias in aliases:
            if alias == canonical:
                errors.append(f"{row_id}: alias duplicates canonical_name {alias!r}")
            if not NAME_RE.fullmatch(alias):
                errors.append(f"{row_id}: invalid alias {alias!r}")
            alias_to_ids[alias].append(row_id)

    for alias, owner_ids in sorted(alias_to_ids.items()):
        unique_owners = sorted(set(owner_ids))
        if len(unique_owners) > 1:
            errors.append(
                f"Alias {alias!r} is shared by multiple designs: "
                + ", ".join(unique_owners)
            )

        canonical_owner = canonical_to_id.get(alias)
        if canonical_owner and canonical_owner not in unique_owners:
            errors.append(
                f"Alias {alias!r} collides with canonical_name of {canonical_owner}; "
                f"alias owner(s): {', '.join(unique_owners)}"
            )

    if errors:
        print(f"Found {len(errors)} icon-matrix error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    alias_count = sum(
        1
        for row in rows
        for item in row["aliases"].split(";")
        if item.strip()
    )

    print(f"Validated {len(rows)} unique designs.")
    print(f"Validated {len(canonical_to_id)} canonical names.")
    print(f"Validated {alias_count} alias entries without namespace collisions.")
    print("Group counts:")
    for group, expected in EXPECTED_GROUPS.items():
        print(f"  {group}: {group_counts[group]} / {expected}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
