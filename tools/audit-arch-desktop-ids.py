#!/usr/bin/env python3
"""Audit Witcher3 application identities against official Arch desktop IDs.

Stage E complements the Flathub application-ID audit with the native desktop
entries shipped by the stable Arch Linux core, extra, and multilib repositories.
This is especially relevant to HyDE/CachyOS because many KDE, GNOME, terminal,
and system applications are installed as native packages rather than Flatpaks.

The 2026-09-14 coverage counts are pinned below so matrix or snapshot changes
cannot silently reduce native application identity coverage.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
ARCH_PATH = ROOT / "design/icons/standards/arch-desktop-ids-2026-09-14.csv"
FLATHUB_PATH = ROOT / "design/icons/standards/flathub-app-ids-2026-09-14.csv"

EXPECTED_APPLICATION_ROWS = 220
EXPECTED_ARCH_DESKTOP_IDS = 2436
EXPECTED_ARCH_REPO_MEMBERSHIPS = {"core": 2, "extra": 2433, "multilib": 1}
EXPECTED_FLATHUB_IDS = 3352
EXPECTED_CANONICAL_ARCH_ROWS = 59
EXPECTED_ALIAS_ARCH_ROWS = 68
EXPECTED_ANY_ARCH_ROWS = 125
EXPECTED_ARCH_ONLY_ROWS = 48
EXPECTED_COMBINED_ROWS = 174
EXPECTED_UNRESOLVED_ROWS = 46
ALLOWED_ARCH_REPOS = {"core", "extra", "multilib"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def parse_aliases(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(";") if item.strip()]


def main() -> int:
    arch_rows = read_csv(ARCH_PATH)
    if not arch_rows or list(arch_rows[0].keys()) != ["desktop_id", "repos"]:
        raise SystemExit("Unexpected Arch desktop-ID snapshot columns")

    arch_ids: dict[str, tuple[str, ...]] = {}
    for row in arch_rows:
        desktop_id = row["desktop_id"].strip()
        repos = tuple(sorted(item for item in row["repos"].split(";") if item))
        if not desktop_id or "/" in desktop_id:
            raise SystemExit(f"Malformed Arch desktop ID: {desktop_id!r}")
        if not repos or not set(repos) <= ALLOWED_ARCH_REPOS:
            raise SystemExit(f"Invalid Arch repository membership: {row!r}")
        if desktop_id in arch_ids:
            raise SystemExit(f"Duplicate Arch desktop ID: {desktop_id!r}")
        arch_ids[desktop_id] = repos

    if len(arch_ids) != EXPECTED_ARCH_DESKTOP_IDS:
        raise SystemExit(
            f"Expected {EXPECTED_ARCH_DESKTOP_IDS} Arch desktop IDs, "
            f"found {len(arch_ids)}"
        )

    repo_memberships = {
        repo: sum(repo in repos for repos in arch_ids.values())
        for repo in ("core", "extra", "multilib")
    }
    if repo_memberships != EXPECTED_ARCH_REPO_MEMBERSHIPS:
        raise SystemExit(
            f"Unexpected Arch repository memberships: {repo_memberships!r}; "
            f"expected {EXPECTED_ARCH_REPO_MEMBERSHIPS!r}"
        )

    flathub_rows = read_csv(FLATHUB_PATH)
    if not flathub_rows or list(flathub_rows[0].keys()) != ["app_id"]:
        raise SystemExit("Unexpected Flathub snapshot columns")
    flathub_ids = {row["app_id"].strip() for row in flathub_rows}
    if len(flathub_ids) != EXPECTED_FLATHUB_IDS:
        raise SystemExit(
            f"Expected {EXPECTED_FLATHUB_IDS} Flathub IDs, found {len(flathub_ids)}"
        )

    matrix_rows = read_csv(MATRIX_PATH)
    application_rows = [
        row for row in matrix_rows if row["group"].strip() == "Applications"
    ]
    if len(application_rows) != EXPECTED_APPLICATION_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_APPLICATION_ROWS} application rows, "
            f"found {len(application_rows)}"
        )

    arch_id_owners: dict[str, list[tuple[str, str]]] = defaultdict(list)
    canonical_arch_matches: list[tuple[str, str, tuple[str, ...]]] = []
    alias_arch_matches: list[tuple[str, str, tuple[str, ...]]] = []
    rows_with_arch: list[tuple[str, str, tuple[str, ...]]] = []
    arch_only_rows: list[tuple[str, str, tuple[str, ...]]] = []
    combined_rows: list[tuple[str, str]] = []
    unresolved_rows: list[tuple[str, str]] = []

    for row in application_rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        aliases = parse_aliases(row["aliases"])
        names = [canonical, *aliases]

        canonical_match = canonical in arch_ids
        alias_matches = tuple(sorted(alias for alias in aliases if alias in arch_ids))
        arch_matches = tuple(sorted({name for name in names if name in arch_ids}))
        flathub_match = any(name in flathub_ids for name in names)

        if canonical_match:
            canonical_arch_matches.append((row_id, canonical, arch_ids[canonical]))
        if alias_matches:
            alias_arch_matches.append((row_id, canonical, alias_matches))
        if arch_matches:
            rows_with_arch.append((row_id, canonical, arch_matches))
            for desktop_id in arch_matches:
                arch_id_owners[desktop_id].append((row_id, canonical))

        if arch_matches and not flathub_match:
            arch_only_rows.append((row_id, canonical, arch_matches))
        if arch_matches or flathub_match:
            combined_rows.append((row_id, canonical))
        else:
            unresolved_rows.append((row_id, canonical))

    conflicting_ids = {
        desktop_id: owners
        for desktop_id, owners in arch_id_owners.items()
        if len({owner[0] for owner in owners}) > 1
    }
    if conflicting_ids:
        print("Arch desktop IDs assigned to multiple Witcher3 designs:")
        for desktop_id, owners in sorted(conflicting_ids.items()):
            rendered = ", ".join(
                f"{row_id} ({canonical})" for row_id, canonical in owners
            )
            print(f"- {desktop_id}: {rendered}")
        return 1

    measured = {
        "canonical_arch_rows": len(canonical_arch_matches),
        "alias_arch_rows": len(alias_arch_matches),
        "any_arch_rows": len(rows_with_arch),
        "arch_only_rows": len(arch_only_rows),
        "combined_rows": len(combined_rows),
        "unresolved_rows": len(unresolved_rows),
    }
    expected = {
        "canonical_arch_rows": EXPECTED_CANONICAL_ARCH_ROWS,
        "alias_arch_rows": EXPECTED_ALIAS_ARCH_ROWS,
        "any_arch_rows": EXPECTED_ANY_ARCH_ROWS,
        "arch_only_rows": EXPECTED_ARCH_ONLY_ROWS,
        "combined_rows": EXPECTED_COMBINED_ROWS,
        "unresolved_rows": EXPECTED_UNRESOLVED_ROWS,
    }
    if measured != expected:
        raise SystemExit(
            f"Unexpected Stage E coverage: {measured!r}; expected {expected!r}"
        )

    print(f"Arch snapshot: {len(arch_ids)} desktop IDs.")
    for repo in ("core", "extra", "multilib"):
        print(f"  {repo}: {repo_memberships[repo]} desktop-ID memberships")

    print(f"Witcher3 application designs: {len(application_rows)}.")
    print(f"Rows whose canonical is an exact Arch desktop ID: {len(canonical_arch_matches)}")
    print(f"Rows with >=1 exact Arch alias: {len(alias_arch_matches)}")
    print(f"Rows with any exact Arch canonical/alias: {len(rows_with_arch)} / 220")
    print(f"Rows newly covered by Arch beyond Flathub: {len(arch_only_rows)}")
    print(f"Combined Flathub or Arch identity coverage: {len(combined_rows)} / 220")
    print(f"Still unresolved after Flathub + Arch: {len(unresolved_rows)} / 220")

    print()
    print("Canonical names matching official Arch desktop IDs:")
    for row_id, canonical, repos in canonical_arch_matches:
        print(f"- {row_id}: {canonical!r} [{','.join(repos)}]")

    print()
    print("Alias names matching official Arch desktop IDs:")
    for row_id, canonical, aliases in alias_arch_matches:
        rendered = ", ".join(
            f"{alias} [{','.join(arch_ids[alias])}]" for alias in aliases
        )
        print(f"- {row_id}: {canonical!r} -> {rendered}")

    print()
    print("Application designs resolved by Arch but not Flathub:")
    for row_id, canonical, matches in arch_only_rows:
        rendered = ", ".join(
            f"{match} [{','.join(arch_ids[match])}]" for match in matches
        )
        print(f"- {row_id}: {canonical!r} -> {rendered}")

    print()
    print("Application designs still unresolved after Flathub + Arch:")
    for row_id, canonical in unresolved_rows:
        print(f"- {row_id}: {canonical!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
