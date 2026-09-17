#!/usr/bin/env python3
"""Audit Witcher3 MIME/Filetypes canonicals against pinned shared-mime-info.

This is Stage B-MIME of the icon naming validation pipeline. It runs after the
Freedesktop Icon Naming audit and before KDE/Breeze. Exact names already covered
by the Freedesktop Icon Naming Specification keep Freedesktop provenance and
are not reclassified here.

For each primary MIME identity in shared-mime-info, the specific icon name is:

* the explicit <icon name="..."> override, when present; otherwise
* the MIME type with '/' replaced by '-'.

<generic-icon> is fallback evidence only and is never promoted to a specific
MIME canonical by this audit. MIME aliases are also reported separately rather
than treated as primary identities.
"""

from __future__ import annotations

import argparse
import csv
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
FREEDESKTOP_PATH = (
    ROOT / "design/icons/standards/freedesktop-icon-naming-latest-2026-09-14.csv"
)
MIME_NAMESPACE = "http://www.freedesktop.org/standards/shared-mime-info"
EXPECTED_MATRIX_ROWS = 645
EXPECTED_MIME_ROWS = 85
EXPECTED_FREEDESKTOP_NAMES = 288


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def parse_shared_mime(
    path: Path,
) -> tuple[
    dict[str, list[tuple[str, str]]],
    dict[str, set[str]],
    dict[str, set[str]],
    Counter[str],
]:
    """Return specific icons, generic icons, alias-derived names and counters."""

    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        raise SystemExit(f"Unable to parse shared-mime-info XML {path}: {exc}")

    if root.tag != f"{{{MIME_NAMESPACE}}}mime-info":
        raise SystemExit(f"Unexpected shared-mime-info root element: {root.tag!r}")

    specific_to_types: dict[str, list[tuple[str, str]]] = defaultdict(list)
    generic_to_types: dict[str, set[str]] = defaultdict(set)
    alias_derived_to_primary: dict[str, set[str]] = defaultdict(set)
    counts: Counter[str] = Counter()
    seen_primary_types: set[str] = set()

    ns = {"m": MIME_NAMESPACE}
    for element in root.findall("m:mime-type", ns):
        mime_type = element.attrib.get("type", "").strip()
        if not mime_type or "/" not in mime_type:
            raise SystemExit(f"Invalid primary MIME identity: {mime_type!r}")
        if mime_type in seen_primary_types:
            raise SystemExit(f"Duplicate primary MIME identity: {mime_type}")
        seen_primary_types.add(mime_type)
        counts["primary_types"] += 1

        explicit_icons = [
            icon.attrib.get("name", "").strip()
            for icon in element.findall("m:icon", ns)
        ]
        explicit_icons = [name for name in explicit_icons if name]
        if len(explicit_icons) > 1:
            raise SystemExit(
                f"MIME type {mime_type} has multiple explicit icon overrides: "
                f"{explicit_icons!r}"
            )

        if explicit_icons:
            specific_name = explicit_icons[0]
            source_kind = "explicit-icon"
            counts["explicit_specific_icons"] += 1
        else:
            specific_name = mime_type.replace("/", "-", 1)
            source_kind = "derived"
            counts["derived_specific_icons"] += 1

        specific_to_types[specific_name].append((mime_type, source_kind))

        for generic in element.findall("m:generic-icon", ns):
            generic_name = generic.attrib.get("name", "").strip()
            if generic_name:
                generic_to_types[generic_name].add(mime_type)
                counts["generic_icon_assignments"] += 1

        for alias in element.findall("m:alias", ns):
            alias_type = alias.attrib.get("type", "").strip()
            if alias_type and "/" in alias_type:
                alias_derived_to_primary[alias_type.replace("/", "-", 1)].add(
                    mime_type
                )
                counts["aliases"] += 1

    if counts["primary_types"] < 800:
        raise SystemExit(
            "Unexpectedly small shared-mime-info database: "
            f"{counts['primary_types']} primary MIME identities"
        )

    return (
        dict(specific_to_types),
        dict(generic_to_types),
        dict(alias_derived_to_primary),
        counts,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-xml",
        type=Path,
        required=True,
        help="Pinned shared-mime-info data/freedesktop.org.xml.in",
    )
    parser.add_argument(
        "--resolved-output",
        type=Path,
        help="Optional newline-delimited output of Stage-B-MIME-resolved canonicals",
    )
    args = parser.parse_args()

    if not args.source_xml.is_file():
        raise SystemExit(f"shared-mime-info source XML not found: {args.source_xml}")

    matrix_rows = read_csv(MATRIX_PATH)
    if len(matrix_rows) != EXPECTED_MATRIX_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_MATRIX_ROWS} matrix rows, found {len(matrix_rows)}"
        )

    mime_rows = [row for row in matrix_rows if row["group"].strip() == "MIME/Filetypes"]
    if len(mime_rows) != EXPECTED_MIME_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_MIME_ROWS} MIME/Filetypes rows, found {len(mime_rows)}"
        )

    freedesktop_rows = read_csv(FREEDESKTOP_PATH)
    freedesktop_names = {row["name"].strip() for row in freedesktop_rows}
    if len(freedesktop_names) != EXPECTED_FREEDESKTOP_NAMES:
        raise SystemExit(
            f"Expected {EXPECTED_FREEDESKTOP_NAMES} Freedesktop names, "
            f"found {len(freedesktop_names)}"
        )

    (
        specific_to_types,
        generic_to_types,
        alias_derived_to_primary,
        source_counts,
    ) = parse_shared_mime(args.source_xml)

    freedesktop_preempted: list[tuple[str, str]] = []
    shared_matches: list[tuple[str, str, tuple[tuple[str, str], ...]]] = []
    unresolved: list[tuple[str, str]] = []
    generic_only: list[tuple[str, str, tuple[str, ...]]] = []
    alias_only: list[tuple[str, str, tuple[str, ...]]] = []

    for row in mime_rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()

        if canonical in freedesktop_names:
            freedesktop_preempted.append((row_id, canonical))
            continue

        specific_matches = specific_to_types.get(canonical)
        if specific_matches:
            shared_matches.append(
                (row_id, canonical, tuple(sorted(specific_matches)))
            )
            continue

        unresolved.append((row_id, canonical))

        generic_types = generic_to_types.get(canonical)
        if generic_types:
            generic_only.append((row_id, canonical, tuple(sorted(generic_types))))

        alias_primary_types = alias_derived_to_primary.get(canonical)
        if alias_primary_types:
            alias_only.append(
                (row_id, canonical, tuple(sorted(alias_primary_types)))
            )

    accounted = len(freedesktop_preempted) + len(shared_matches) + len(unresolved)
    if accounted != len(mime_rows):
        raise SystemExit(
            f"Internal Stage B-MIME accounting error: {accounted} != {len(mime_rows)}"
        )

    print(
        "Parsed shared-mime-info source: "
        f"{source_counts['primary_types']} primary MIME identities; "
        f"{source_counts['explicit_specific_icons']} explicit specific-icon overrides; "
        f"{source_counts['generic_icon_assignments']} generic-icon assignments; "
        f"{source_counts['aliases']} aliases."
    )
    print(
        "MIME/Filetypes Stage B-MIME coverage: "
        f"{len(freedesktop_preempted)} Freedesktop-preempted / "
        f"{len(shared_matches)} shared-mime / {len(unresolved)} unresolved."
    )

    print()
    print("Exact shared-mime specific-icon matches:")
    for row_id, canonical, matches in shared_matches:
        evidence = ", ".join(
            f"{mime_type} ({source_kind})" for mime_type, source_kind in matches
        )
        print(f"- {row_id}: {canonical!r} -> {evidence}")

    if generic_only:
        print()
        print("Generic-icon fallback matches among unresolved names (not resolved here):")
        for row_id, canonical, mime_types in generic_only:
            print(f"- {row_id}: {canonical!r} <- {', '.join(mime_types)}")

    if alias_only:
        print()
        print("Alias-derived name matches among unresolved names (review only):")
        for row_id, canonical, primary_types in alias_only:
            print(f"- {row_id}: {canonical!r} <- alias of {', '.join(primary_types)}")

    print()
    print("Names still unresolved after Freedesktop + shared-mime-info:")
    for row_id, canonical in unresolved:
        print(f"- {row_id}: {canonical!r}")

    if args.resolved_output is not None:
        resolved_names = sorted({canonical for _, canonical, _ in shared_matches})
        args.resolved_output.parent.mkdir(parents=True, exist_ok=True)
        args.resolved_output.write_text(
            "".join(f"{name}\n" for name in resolved_names),
            encoding="utf-8",
        )
        print()
        print(
            f"Wrote {len(resolved_names)} Stage-B-MIME resolved names to "
            f"{args.resolved_output}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
