#!/usr/bin/env python3
"""Audit remaining Witcher3 canonical names against a pinned Breeze tree.

Stage C intentionally follows both Freedesktop audits: names covered by the
Icon Naming Specification (Stage B) or by shared-mime-info specific icon names
(Stage B-MIME) are excluded here. An unresolved name that is also absent from
Breeze is not automatically invalid: application IDs, desktop IDs,
HyDE-specific names, and project extensions are validated in later stages.

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
EXPECTED_FREEDESKTOP_MATCHES = 154
EXPECTED_BREEZE_UNIQUE_NAMES = 4382
GROUP_ORDER = (
    "Applications",
    "Actions/UI",
    "Places/Folders",
    "Status/Panel/Waybar",
    "Devices",
    "MIME/Filetypes",
    "Categories/Misc",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_resolved_names(path: Path) -> set[str]:
    if not path.is_file():
        raise SystemExit(f"Stage-B-MIME resolved-name file not found: {path}")

    names: list[str] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        name = raw_line.strip()
        if name:
            names.append(name)

    if len(names) != len(set(names)):
        raise SystemExit("Duplicate name in Stage-B-MIME resolved-name file")
    if not names:
        raise SystemExit("Stage-B-MIME resolved-name file is empty")
    return set(names)


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
    parser.add_argument(
        "--shared-mime-resolved",
        type=Path,
        required=True,
        help="Stage-B-MIME newline-delimited resolved canonical names",
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

    shared_mime_names = read_resolved_names(args.shared_mime_resolved)

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

    matrix_by_canonical = {
        row["canonical_name"].strip(): row
        for row in matrix_rows
    }
    unknown_shared = sorted(shared_mime_names - set(matrix_by_canonical))
    if unknown_shared:
        raise SystemExit(
            "Stage-B-MIME resolved file contains names absent from matrix: "
            + ", ".join(unknown_shared)
        )

    wrong_group = sorted(
        name
        for name in shared_mime_names
        if matrix_by_canonical[name]["group"].strip() != "MIME/Filetypes"
    )
    if wrong_group:
        raise SystemExit(
            "Stage-B-MIME resolved non-MIME matrix names: " + ", ".join(wrong_group)
        )

    overlap = sorted(shared_mime_names & freedesktop_names)
    if overlap:
        raise SystemExit(
            "Stage-B-MIME output overlaps Freedesktop Stage B: " + ", ".join(overlap)
        )

    fdo_matches = 0
    shared_mime_matches = 0
    breeze_matches: list[tuple[str, str, str, tuple[str, ...]]] = []
    unresolved: list[tuple[str, str, str]] = []
    shared_by_group: Counter[str] = Counter()
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

        if canonical in shared_mime_names:
            shared_mime_matches += 1
            shared_by_group[group] += 1
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

    if shared_mime_matches != len(shared_mime_names):
        raise SystemExit(
            "Stage-B-MIME handoff accounting error: "
            f"{shared_mime_matches} consumed / {len(shared_mime_names)} supplied"
        )

    if (
        fdo_matches
        + shared_mime_matches
        + len(breeze_matches)
        + len(unresolved)
        != len(matrix_rows)
    ):
        raise SystemExit("Internal Stage C coverage accounting error")

    print(f"Parsed {len(breeze_names)} unique Breeze icon names.")
    print("Breeze source contexts:")
    for context, count in sorted(breeze_context_counts.items()):
        print(f"  {context}: {count} unique-name memberships")

    print()
    print(f"Freedesktop-resolved matrix names: {fdo_matches} / 645")
    print(f"shared-mime-resolved matrix names: {shared_mime_matches} / 645")
    print(
        "Additional exact Breeze canonical matches: "
        f"{len(breeze_matches)} / {645 - fdo_matches - shared_mime_matches} "
        "remaining after Stage B + Stage B-MIME"
    )
    print(f"Still unresolved after Breeze: {len(unresolved)} / 645")

    print()
    print("Stage C coverage by Witcher3 group:")
    for group in GROUP_ORDER:
        print(
            f"  {group}: {shared_by_group[group]} shared-mime / "
            f"{matched_by_group[group]} Breeze / "
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
    print("Exact Breeze matches among names unresolved after Stage B-MIME:")
    for row_id, canonical, group, contexts in breeze_matches:
        print(
            f"- {row_id}: {canonical!r} [{group}] -> "
            f"{', '.join(contexts)}"
        )

    print()
    print("Names still unresolved after Freedesktop + shared-mime-info + Breeze:")
    for row_id, canonical, group in unresolved:
        print(f"- {row_id}: {canonical!r} [{group}]")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
