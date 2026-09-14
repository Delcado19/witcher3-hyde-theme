#!/usr/bin/env python3
"""Audit Witcher3 canonical icon names against the pinned Freedesktop snapshot.

This is Stage B of the icon naming validation pipeline. A name that is absent
from the Freedesktop list is not considered invalid here; it must be validated
later against Breeze, application metadata, HyDE, or documented as a project
extension.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
STANDARD_PATH = (
    ROOT
    / "design/icons/standards/freedesktop-icon-naming-latest-2026-09-14.csv"
)

EXPECTED_STANDARD_COUNTS = {
    "Actions": 103,
    "Animations": 1,
    "Applications": 20,
    "Categories": 19,
    "Devices": 27,
    "Emblems": 13,
    "Emotes": 21,
    "International": 1,
    "MimeTypes": 15,
    "Places": 9,
    "Status": 59,
}

# The matrix groups are design/coverage families, but an exact Freedesktop
# standard name should normally live in the corresponding semantic family.
# Categories/Misc intentionally owns the standard contexts for which the
# Witcher3 design budget has no dedicated top-level group.
ALLOWED_CONTEXTS = {
    "Applications": {"Applications"},
    "Actions/UI": {"Actions"},
    "Places/Folders": {"Places"},
    "Status/Panel/Waybar": {"Status"},
    "Devices": {"Devices"},
    "MIME/Filetypes": {"MimeTypes"},
    "Categories/Misc": {
        "Categories",
        "Emblems",
        "Emotes",
        "International",
        "Animations",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def main() -> int:
    standard_rows = read_csv(STANDARD_PATH)
    if list(standard_rows[0].keys()) != ["context", "name"]:
        raise SystemExit("Unexpected Freedesktop snapshot columns")

    standard_counts = Counter(row["context"].strip() for row in standard_rows)
    if dict(standard_counts) != EXPECTED_STANDARD_COUNTS:
        raise SystemExit(
            f"Unexpected Freedesktop snapshot counts: {dict(standard_counts)!r}"
        )

    standard_by_name: dict[str, str] = {}
    for row in standard_rows:
        context = row["context"].strip()
        name = row["name"].strip()
        previous = standard_by_name.setdefault(name, context)
        if previous != context:
            raise SystemExit(
                f"Freedesktop name {name!r} appears in multiple contexts: "
                f"{previous}, {context}"
            )

    if len(standard_by_name) != 288:
        raise SystemExit(
            f"Expected 288 unique Freedesktop names, found {len(standard_by_name)}"
        )

    matrix_rows = read_csv(MATRIX_PATH)
    exact_matches: list[tuple[str, str, str, str]] = []
    context_mismatches: list[str] = []
    matrix_match_counts: Counter[str] = Counter()
    matched_by_group: Counter[str] = Counter()
    unmatched_by_group: Counter[str] = Counter()
    standard_aliases_to_nonstandard_canonical: list[str] = []

    for row in matrix_rows:
        row_id = row["id"].strip()
        group = row["group"].strip()
        canonical = row["canonical_name"].strip()
        context = standard_by_name.get(canonical)

        if context is None:
            unmatched_by_group[group] += 1
        else:
            exact_matches.append((row_id, canonical, group, context))
            matrix_match_counts[context] += 1
            matched_by_group[group] += 1

            allowed = ALLOWED_CONTEXTS.get(group, set())
            if context not in allowed:
                context_mismatches.append(
                    f"{row_id}: {canonical!r} is Freedesktop {context}, "
                    f"but matrix group is {group!r}"
                )

        aliases = [
            item.strip()
            for item in row["aliases"].split(";")
            if item.strip()
        ]
        if canonical not in standard_by_name:
            standard_aliases = [
                alias for alias in aliases if alias in standard_by_name
            ]
            for alias in standard_aliases:
                standard_aliases_to_nonstandard_canonical.append(
                    f"{row_id}: non-standard canonical {canonical!r} has "
                    f"Freedesktop alias {alias!r} ({standard_by_name[alias]})"
                )

    print(f"Freedesktop snapshot: {len(standard_by_name)} standard names.")
    print(
        f"Matrix exact Freedesktop canonical matches: {len(exact_matches)} / "
        f"{len(matrix_rows)} designs."
    )
    print()
    print("Exact matches by Freedesktop context:")
    for context in EXPECTED_STANDARD_COUNTS:
        print(
            f"  {context}: {matrix_match_counts[context]} / "
            f"{EXPECTED_STANDARD_COUNTS[context]} standard names"
        )

    print()
    print("Matrix coverage by Witcher3 group:")
    for group in ALLOWED_CONTEXTS:
        matched = matched_by_group[group]
        unmatched = unmatched_by_group[group]
        print(f"  {group}: {matched} Freedesktop / {unmatched} unresolved")

    if standard_aliases_to_nonstandard_canonical:
        print()
        print(
            "Freedesktop names currently used only as aliases of a non-standard "
            "canonical (review required):"
        )
        for item in standard_aliases_to_nonstandard_canonical:
            print(f"- {item}")

    if context_mismatches:
        print()
        print(f"Found {len(context_mismatches)} Freedesktop context mismatch(es):")
        for mismatch in context_mismatches:
            print(f"- {mismatch}")
        return 1

    print()
    print("All exact Freedesktop canonical matches use compatible matrix groups.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
