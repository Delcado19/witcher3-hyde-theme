#!/usr/bin/env python3
"""Audit Witcher3 application aliases against the pinned Flathub ID snapshot.

Stage D validates application identity independently of icon-name coverage.
The artwork canonical may remain a conventional desktop icon name such as
`firefox`; exact Flathub application IDs are expected to live in `aliases` and
will later become compatibility symlinks in the generated icon theme.

Missing Flathub coverage does not make an application invalid because many
applications are distributed outside Flathub. The pinned counts below make the
validated 2026-09-14 coverage reproducible and prevent silent regressions.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
FLATHUB_PATH = ROOT / "design/icons/standards/flathub-app-ids-2026-09-14.csv"

EXPECTED_APPLICATION_ROWS = 220
EXPECTED_FLATHUB_IDS = 3352
EXPECTED_ROWS_WITH_FLATHUB_ALIAS = 126
EXPECTED_EXACT_FLATHUB_ALIASES = 126
EXPECTED_CANONICAL_FLATHUB_IDS = 0
EXPECTED_ROWS_WITHOUT_FLATHUB = 94
EXPECTED_SHAPED_NON_FLATHUB_ALIASES = 21

# Flatpak application IDs are reverse-DNS-like. Requiring at least three
# components intentionally avoids classifying desktop filenames such as
# `mpv.desktop` or `nemo.desktop` as app-ID candidates.
APP_ID_SHAPED_RE = re.compile(
    r"^[A-Za-z0-9_][A-Za-z0-9_-]*"
    r"(?:\.[A-Za-z0-9_][A-Za-z0-9_-]*){2,}$"
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def parse_aliases(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(";") if item.strip()]


def main() -> int:
    flathub_rows = read_csv(FLATHUB_PATH)
    if not flathub_rows or list(flathub_rows[0].keys()) != ["app_id"]:
        raise SystemExit("Unexpected Flathub snapshot columns")

    flathub_ids = [row["app_id"].strip() for row in flathub_rows]
    if len(flathub_ids) != EXPECTED_FLATHUB_IDS:
        raise SystemExit(
            f"Expected {EXPECTED_FLATHUB_IDS} Flathub IDs, found {len(flathub_ids)}"
        )
    if any(not app_id for app_id in flathub_ids):
        raise SystemExit("Flathub snapshot contains an empty application ID")
    if flathub_ids != sorted(set(flathub_ids)):
        raise SystemExit("Flathub snapshot IDs must be sorted and unique")

    flathub_set = set(flathub_ids)
    matrix_rows = read_csv(MATRIX_PATH)
    application_rows = [row for row in matrix_rows if row["group"].strip() == "Applications"]
    if len(application_rows) != EXPECTED_APPLICATION_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_APPLICATION_ROWS} application rows, "
            f"found {len(application_rows)}"
        )

    canonical_matches: list[tuple[str, str]] = []
    rows_with_flathub_alias: list[tuple[str, str, tuple[str, ...]]] = []
    rows_without_flathub: list[tuple[str, str]] = []
    shaped_non_flathub_aliases: list[tuple[str, str, str]] = []
    flathub_id_owners: dict[str, list[tuple[str, str]]] = defaultdict(list)
    exact_alias_count = 0

    for row in application_rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        aliases = parse_aliases(row["aliases"])

        if canonical in flathub_set:
            canonical_matches.append((row_id, canonical))
            flathub_id_owners[canonical].append((row_id, canonical))

        exact_aliases = tuple(sorted(alias for alias in aliases if alias in flathub_set))
        exact_alias_count += len(exact_aliases)
        for app_id in exact_aliases:
            flathub_id_owners[app_id].append((row_id, canonical))

        if exact_aliases:
            rows_with_flathub_alias.append((row_id, canonical, exact_aliases))
        elif canonical not in flathub_set:
            rows_without_flathub.append((row_id, canonical))

        for alias in aliases:
            if APP_ID_SHAPED_RE.fullmatch(alias) and alias not in flathub_set:
                shaped_non_flathub_aliases.append((row_id, canonical, alias))

    conflicting_ids = {
        app_id: owners
        for app_id, owners in flathub_id_owners.items()
        if len({owner[0] for owner in owners}) > 1
    }
    if conflicting_ids:
        print("Flathub IDs assigned to multiple Witcher3 designs:")
        for app_id, owners in sorted(conflicting_ids.items()):
            rendered = ", ".join(f"{row_id} ({canonical})" for row_id, canonical in owners)
            print(f"- {app_id}: {rendered}")
        return 1

    measured = {
        "rows_with_alias": len(rows_with_flathub_alias),
        "exact_aliases": exact_alias_count,
        "canonical_ids": len(canonical_matches),
        "rows_without": len(rows_without_flathub),
        "shaped_non_flathub": len(shaped_non_flathub_aliases),
    }
    expected = {
        "rows_with_alias": EXPECTED_ROWS_WITH_FLATHUB_ALIAS,
        "exact_aliases": EXPECTED_EXACT_FLATHUB_ALIASES,
        "canonical_ids": EXPECTED_CANONICAL_FLATHUB_IDS,
        "rows_without": EXPECTED_ROWS_WITHOUT_FLATHUB,
        "shaped_non_flathub": EXPECTED_SHAPED_NON_FLATHUB_ALIASES,
    }
    if measured != expected:
        raise SystemExit(
            f"Unexpected Stage D coverage: {measured!r}; expected {expected!r}"
        )

    print(f"Flathub snapshot: {len(flathub_set)} application IDs.")
    print(f"Witcher3 application designs: {len(application_rows)}.")
    print(
        "Application rows with >=1 exact Flathub alias: "
        f"{len(rows_with_flathub_alias)} / {len(application_rows)}"
    )
    print(f"Exact Flathub alias entries matched: {exact_alias_count}")
    print(f"Canonical names that are themselves Flathub IDs: {len(canonical_matches)}")
    print(
        "Application rows without an exact Flathub canonical/alias: "
        f"{len(rows_without_flathub)} / {len(application_rows)}"
    )
    print(
        "App-ID-shaped aliases absent from the pinned Flathub snapshot: "
        f"{len(shaped_non_flathub_aliases)}"
    )

    if canonical_matches:
        print()
        print("Canonical names that directly equal a Flathub application ID:")
        for row_id, canonical in canonical_matches:
            print(f"- {row_id}: {canonical}")

    print()
    print("Exact Flathub aliases by Witcher3 application design:")
    for row_id, canonical, app_ids in rows_with_flathub_alias:
        print(f"- {row_id}: {canonical!r} -> {', '.join(app_ids)}")

    if shaped_non_flathub_aliases:
        print()
        print("App-ID-shaped aliases not present on Flathub (review, not failure):")
        for row_id, canonical, alias in shaped_non_flathub_aliases:
            print(f"- {row_id}: {canonical!r} -> {alias}")

    print()
    print("Application designs with no exact Flathub identity match:")
    for row_id, canonical in rows_without_flathub:
        print(f"- {row_id}: {canonical!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
