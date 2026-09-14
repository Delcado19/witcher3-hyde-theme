#!/usr/bin/env python3
"""Audit remaining Witcher3 application identities against Arch commands.

Stage F starts only with application designs that were not resolved by either
Flathub application IDs or official Arch Desktop Entry IDs. It then checks
whether the design's canonical name or an existing alias exactly matches a
real /usr/bin command shipped by the official Arch core, extra, or multilib
repositories.

This is appropriate for CLI/session/system components such as tmux, Waybar, or
Hyprland-related tools that may have no Desktop Entry at all. The validated
2026-09-14 coverage is pinned below to prevent silent regressions.
"""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
FLATHUB_PATH = ROOT / "design/icons/standards/flathub-app-ids-2026-09-14.csv"
ARCH_DESKTOP_PATH = ROOT / "design/icons/standards/arch-desktop-ids-2026-09-14.csv"
ARCH_COMMAND_PATH = ROOT / "design/icons/standards/arch-command-names-2026-09-14.csv"

EXPECTED_APPLICATION_ROWS = 220
EXPECTED_FLATHUB_IDS = 3352
EXPECTED_ARCH_DESKTOP_IDS = 2436
EXPECTED_ARCH_COMMANDS = 22691
EXPECTED_STAGE_E_UNRESOLVED = 46
EXPECTED_COMMAND_REPO_MEMBERSHIPS = {"core": 1567, "extra": 20802, "multilib": 331}
EXPECTED_CANONICAL_COMMAND_ROWS = 15
EXPECTED_ALIAS_COMMAND_ROWS = 1
EXPECTED_RESOLVED_ROWS = 15
EXPECTED_UNRESOLVED_ROWS = 31
EXPECTED_COMBINED_ROWS = 189
EXPECTED_RESOLVED_IDS = {
    "W3-035",
    "W3-036",
    "W3-050",
    "W3-090",
    "W3-108",
    "W3-112",
    "W3-186",
    "W3-202",
    "W3-203",
    "W3-205",
    "W3-206",
    "W3-207",
    "W3-208",
    "W3-209",
    "W3-219",
}
ALLOWED_ARCH_REPOS = {"core", "extra", "multilib"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def parse_aliases(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(";") if item.strip()]


def read_single_column(path: Path, column: str, expected_count: int) -> set[str]:
    rows = read_csv(path)
    if not rows or list(rows[0].keys()) != [column]:
        raise SystemExit(f"Unexpected columns in {path.name}")
    values = [row[column].strip() for row in rows]
    if len(values) != expected_count or len(set(values)) != expected_count:
        raise SystemExit(
            f"Expected {expected_count} unique {column} values in {path.name}, "
            f"found {len(values)} rows / {len(set(values))} unique"
        )
    return set(values)


def read_arch_map(path: Path, key: str, expected_count: int) -> dict[str, tuple[str, ...]]:
    rows = read_csv(path)
    if not rows or list(rows[0].keys()) != [key, "repos"]:
        raise SystemExit(f"Unexpected columns in {path.name}")

    result: dict[str, tuple[str, ...]] = {}
    for row in rows:
        value = row[key].strip()
        repos = tuple(sorted(item for item in row["repos"].split(";") if item))
        if not value or "/" in value:
            raise SystemExit(f"Malformed {key}: {value!r}")
        if not repos or not set(repos) <= ALLOWED_ARCH_REPOS:
            raise SystemExit(f"Invalid repository membership: {row!r}")
        if value in result:
            raise SystemExit(f"Duplicate {key}: {value!r}")
        result[value] = repos

    if len(result) != expected_count:
        raise SystemExit(
            f"Expected {expected_count} {key} entries in {path.name}, "
            f"found {len(result)}"
        )
    return result


def main() -> int:
    flathub_ids = read_single_column(FLATHUB_PATH, "app_id", EXPECTED_FLATHUB_IDS)
    arch_desktop_ids = read_arch_map(
        ARCH_DESKTOP_PATH, "desktop_id", EXPECTED_ARCH_DESKTOP_IDS
    )
    arch_commands = read_arch_map(ARCH_COMMAND_PATH, "command", EXPECTED_ARCH_COMMANDS)

    command_memberships = {
        repo: sum(repo in repos for repos in arch_commands.values())
        for repo in ("core", "extra", "multilib")
    }
    if command_memberships != EXPECTED_COMMAND_REPO_MEMBERSHIPS:
        raise SystemExit(
            f"Unexpected Arch command memberships: {command_memberships!r}; "
            f"expected {EXPECTED_COMMAND_REPO_MEMBERSHIPS!r}"
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

    stage_e_unresolved: list[dict[str, str]] = []
    for row in application_rows:
        canonical = row["canonical_name"].strip()
        aliases = parse_aliases(row["aliases"])
        names = [canonical, *aliases]
        if any(name in flathub_ids for name in names):
            continue
        if any(name in arch_desktop_ids for name in names):
            continue
        stage_e_unresolved.append(row)

    if len(stage_e_unresolved) != EXPECTED_STAGE_E_UNRESOLVED:
        raise SystemExit(
            f"Expected {EXPECTED_STAGE_E_UNRESOLVED} Stage-E unresolved rows, "
            f"found {len(stage_e_unresolved)}"
        )

    command_owners: dict[str, list[tuple[str, str]]] = defaultdict(list)
    canonical_matches: list[tuple[str, str, tuple[str, ...]]] = []
    alias_matches: list[tuple[str, str, tuple[str, ...]]] = []
    resolved_rows: list[tuple[str, str, tuple[str, ...]]] = []
    unresolved_rows: list[tuple[str, str]] = []

    for row in stage_e_unresolved:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        aliases = parse_aliases(row["aliases"])

        if canonical in arch_commands:
            canonical_matches.append((row_id, canonical, arch_commands[canonical]))

        exact_aliases = tuple(sorted(alias for alias in aliases if alias in arch_commands))
        if exact_aliases:
            alias_matches.append((row_id, canonical, exact_aliases))

        exact_commands = tuple(
            sorted({name for name in [canonical, *aliases] if name in arch_commands})
        )
        if exact_commands:
            resolved_rows.append((row_id, canonical, exact_commands))
            for command in exact_commands:
                command_owners[command].append((row_id, canonical))
        else:
            unresolved_rows.append((row_id, canonical))

    conflicts = {
        command: owners
        for command, owners in command_owners.items()
        if len({owner[0] for owner in owners}) > 1
    }
    if conflicts:
        print("Arch commands assigned to multiple Witcher3 designs:")
        for command, owners in sorted(conflicts.items()):
            rendered = ", ".join(
                f"{row_id} ({canonical})" for row_id, canonical in owners
            )
            print(f"- {command}: {rendered}")
        return 1

    resolved_ids = {row_id for row_id, _, _ in resolved_rows}
    measured = {
        "canonical_command_rows": len(canonical_matches),
        "alias_command_rows": len(alias_matches),
        "resolved_rows": len(resolved_rows),
        "unresolved_rows": len(unresolved_rows),
        "combined_rows": EXPECTED_APPLICATION_ROWS - len(unresolved_rows),
    }
    expected = {
        "canonical_command_rows": EXPECTED_CANONICAL_COMMAND_ROWS,
        "alias_command_rows": EXPECTED_ALIAS_COMMAND_ROWS,
        "resolved_rows": EXPECTED_RESOLVED_ROWS,
        "unresolved_rows": EXPECTED_UNRESOLVED_ROWS,
        "combined_rows": EXPECTED_COMBINED_ROWS,
    }
    if measured != expected:
        raise SystemExit(
            f"Unexpected Stage F coverage: {measured!r}; expected {expected!r}"
        )
    if resolved_ids != EXPECTED_RESOLVED_IDS:
        raise SystemExit(
            f"Unexpected Stage F resolved IDs: {sorted(resolved_ids)!r}; "
            f"expected {sorted(EXPECTED_RESOLVED_IDS)!r}"
        )

    print(f"Arch command snapshot: {len(arch_commands)} command names.")
    for repo in ("core", "extra", "multilib"):
        print(f"  {repo}: {command_memberships[repo]} command memberships")
    print(f"Stage-E unresolved application designs: {len(stage_e_unresolved)}.")
    print(f"Rows whose canonical is an exact Arch command: {len(canonical_matches)}")
    print(f"Rows with >=1 exact Arch command alias: {len(alias_matches)}")
    print(f"Rows newly resolved by exact Arch commands: {len(resolved_rows)}")
    print(f"Still unresolved after Stage F: {len(unresolved_rows)}")
    print(
        "Combined Flathub / Arch Desktop Entry / Arch command coverage: "
        f"{EXPECTED_APPLICATION_ROWS - len(unresolved_rows)} / {EXPECTED_APPLICATION_ROWS}"
    )

    print()
    print("Stage-F exact command matches:")
    for row_id, canonical, commands in resolved_rows:
        rendered = ", ".join(
            f"{command} [{','.join(arch_commands[command])}]" for command in commands
        )
        print(f"- {row_id}: {canonical!r} -> {rendered}")

    print()
    print("Application designs still unresolved after Stage F:")
    for row_id, canonical in unresolved_rows:
        print(f"- {row_id}: {canonical!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
