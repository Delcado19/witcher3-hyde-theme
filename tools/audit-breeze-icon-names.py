#!/usr/bin/env python3
"""Audit unresolved Witcher3 canonical icon names against a pinned Breeze tree.

Stage C intentionally follows the Freedesktop audit. Canonical names already
covered by the pinned Freedesktop snapshot are excluded here. An unresolved
name that is also absent from Breeze is not automatically invalid: application
IDs, desktop IDs, HyDE-specific names, and project extensions are validated in
later stages.

The tool consumes a plain `git ls-tree -r --name-only` listing instead of a
checked-out Breeze repository. This keeps CI fast and makes the exact upstream
commit independently verifiable by the workflow.
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
FREEDESKTOP_PATH = (
    ROOT / "design/icons/standards/freedesktop-icon-naming-latest-2026-09-14.csv"
)

ICON_SUFFIXES = {".svg", ".png", ".xpm"}
EXPECTED_FREEDESKTOP_MATCHES = 135
EXPECTED_BREEZE_UNIQUE_NAMES = 4382
EXPECTED_BREEZE_MATCHES = 106
EXPECTED_UNRESOLVED = 404
EXPECTED_GROUP_COVERAGE = {
    "Applications": (19, 201),
    "Actions/UI": (19, 1),
    "Places/Folders": (19, 36),
    "Status/Panel/Waybar": (16, 58),
    "Devices": (10, 29),
    "MIME/Filetypes": (21, 63),
    "Categories/Misc": (2, 16),
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def parse_breeze_tree(path: Path) -> dict[str, set[str]]:
    names_to_contexts: dict[str, set[str]] = defaultdict(set)

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        raw_path = raw_line.strip()
        if not raw_path.startswith("icons/"):
            continue

        parts = PurePosixPath(raw_path).parts
        if len(parts) < 4:
            continue

        context = parts[1]
        filename = parts[-1]
        file_path = PurePosixPath(filename)
        if file_path.suffix.lower() not in ICON_SUFFIXES:
            continue

        name = file_path.stem
        if name.endswith("-symbolic"):
            name = name[: -len("-symbolic")]

        if name:
            names_to_contexts[name].add(context)

    return dict(names_to_contexts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tree-list",
        type=Path,
        required=True,
        help="Path to `git ls-tree -r --name-only` output for pinned Breeze",
    )
    args = parser.parse_args()

    if not args.tree_list.is_file():
        raise SystemExit(f"Breeze tree list not found: {args.tree_list}")

    freedesktop_rows = read_csv(FREEDESKTOP_PATH)
    freedesktop_names = {row["name"].strip() for row in freedesktop_rows}
    if len(freedesktop_names) != 288:
        raise SystemExit(
            f"Expected 288 Freedesktop names, found {len(freedesktop_names)}"
        )

    breeze_names = parse_breeze_tree(args.tree_list)
    if not breeze_names:
        raise SystemExit("No Breeze icon names were parsed from the supplied tree")
    if len(breeze_names) != EXPECTED_BREEZE_UNIQUE_NAMES:
        raise SystemExit(
            f"Expected {EXPECTED_BREEZE_UNIQUE_NAMES} unique Breeze names, "
            f"found {len(breeze_names)}"
        )

    breeze_context_counts = Counter(
        context
        for contexts in breeze_names.values()
        for context in contexts
    )

    matrix_rows = read_csv(MATRIX_PATH)
    if len(matrix_rows) != 645:
        raise SystemExit(f"Expected 645 matrix rows, found {len(matrix_rows)}")

    fdo_matches = 0
    breeze_matches: list[tuple[str, str, str, tuple[str, ...]]] = []
    unresolved: list[tuple[str, str, str]] = []
    matched_by_group: Counter[str] = Counter()
    unresolved_by_group: Counter[str] = Counter()
    breeze_alias_candidates: list[str] = []

    for row in matrix_rows:
        row_id = row["id"].strip()
        group = row["group"].strip()
        canonical = row["canonical_name"].strip()

        if canonical in freedesktop_names:
            fdo_matches += 1
            continue

        contexts = breeze_names.get(canonical)
        if contexts:
            ordered_contexts = tuple(sorted(contexts))
            breeze_matches.append((row_id, canonical, group, ordered_contexts))
            matched_by_group[group] += 1
            continue

        unresolved.append((row_id, canonical, group))
        unresolved_by_group[group] += 1

        aliases = [
            item.strip()
            for item in row["aliases"].split(";")
            if item.strip()
        ]
        for alias in aliases:
            alias_contexts = breeze_names.get(alias)
            if alias_contexts:
                breeze_alias_candidates.append(
                    f"{row_id}: unresolved canonical {canonical!r} has Breeze "
                    f"alias {alias!r} in {', '.join(sorted(alias_contexts))}"
                )

    if fdo_matches != EXPECTED_FREEDESKTOP_MATCHES:
        raise SystemExit(
            "Expected "
            f"{EXPECTED_FREEDESKTOP_MATCHES} Freedesktop-resolved matrix names, "
            f"found {fdo_matches}"
        )

    if len(breeze_matches) != EXPECTED_BREEZE_MATCHES:
        raise SystemExit(
            f"Expected {EXPECTED_BREEZE_MATCHES} additional Breeze matches, "
            f"found {len(breeze_matches)}"
        )

    if len(unresolved) != EXPECTED_UNRESOLVED:
        raise SystemExit(
            f"Expected {EXPECTED_UNRESOLVED} unresolved matrix names after Breeze, "
            f"found {len(unresolved)}"
        )

    actual_group_coverage = {
        group: (matched_by_group[group], unresolved_by_group[group])
        for group in EXPECTED_GROUP_COVERAGE
    }
    if actual_group_coverage != EXPECTED_GROUP_COVERAGE:
        raise SystemExit(
            "Unexpected Stage C group coverage: "
            f"{actual_group_coverage!r}; expected {EXPECTED_GROUP_COVERAGE!r}"
        )

    if fdo_matches + len(breeze_matches) + len(unresolved) != len(matrix_rows):
        raise SystemExit("Internal coverage accounting error")

    print(f"Parsed {len(breeze_names)} unique Breeze icon names.")
    print("Breeze source contexts:")
    for context, count in sorted(breeze_context_counts.items()):
        print(f"  {context}: {count} unique-name memberships")

    print()
    print(f"Freedesktop-resolved matrix names: {fdo_matches} / 645")
    print(
        "Additional exact Breeze canonical matches: "
        f"{len(breeze_matches)} / {645 - fdo_matches} unresolved after Stage B"
    )
    print(f"Still unresolved after Breeze: {len(unresolved)} / 645")

    print()
    print("Stage C coverage by Witcher3 group:")
    for group in EXPECTED_GROUP_COVERAGE:
        print(
            f"  {group}: {matched_by_group[group]} Breeze / "
            f"{unresolved_by_group[group]} still unresolved"
        )

    if breeze_alias_candidates:
        print()
        print(
            "Breeze names currently used only as aliases of an unresolved "
            "canonical (review required):"
        )
        for item in breeze_alias_candidates:
            print(f"- {item}")

    print()
    print("Exact Breeze matches among Stage-B-unresolved canonicals:")
    for row_id, canonical, group, contexts in breeze_matches:
        print(
            f"- {row_id}: {canonical!r} [{group}] -> "
            f"{', '.join(contexts)}"
        )

    print()
    print("Names still unresolved after Freedesktop + Breeze:")
    for row_id, canonical, group in unresolved:
        print(f"- {row_id}: {canonical!r} [{group}]")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
