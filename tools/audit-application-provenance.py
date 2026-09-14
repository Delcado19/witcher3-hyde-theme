#!/usr/bin/env python3
"""Validate the explicit provenance queue for Stage-F unresolved applications.

Stage G does not pretend that every remaining application has one universal
Linux identity source. It recomputes the rows unresolved by Flathub, official
Arch Desktop Entries, and official Arch commands, then requires exactly one
review record for each of them.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
FLATHUB_PATH = ROOT / "design/icons/standards/flathub-app-ids-2026-09-14.csv"
ARCH_DESKTOP_PATH = ROOT / "design/icons/standards/arch-desktop-ids-2026-09-14.csv"
ARCH_COMMAND_PATH = ROOT / "design/icons/standards/arch-command-names-2026-09-14.csv"
PROVENANCE_PATH = ROOT / "design/icons/standards/application-provenance-review.csv"

EXPECTED_APPLICATION_ROWS = 220
EXPECTED_FLATHUB_IDS = 3352
EXPECTED_ARCH_DESKTOP_IDS = 2436
EXPECTED_ARCH_COMMANDS = 22691
EXPECTED_PROVENANCE_ROWS = 31

ALLOWED_CLASSES = {
    "retired-product",
    "unofficial-wrapper",
    "upstream-appimage",
    "archived-project",
    "vendor-linux",
    "official-arch-package",
    "upstream-desktop",
    "aur-package",
    "framework-command",
    "renamed-successor",
    "unknown",
}
ALLOWED_STATUSES = {
    "validated-current",
    "validated-historical",
    "needs-alias-fix",
    "needs-canonical-review",
    "needs-source",
}
EXPECTED_COLUMNS = [
    "id",
    "canonical_name",
    "provenance_class",
    "status",
    "evidence",
    "notes",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [dict(row) for row in reader]
        if reader.fieldnames is None:
            raise SystemExit(f"Missing header in {path.name}")
        return rows


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


def read_two_column_ids(path: Path, key: str, expected_count: int) -> set[str]:
    rows = read_csv(path)
    if not rows or list(rows[0].keys()) != [key, "repos"]:
        raise SystemExit(f"Unexpected columns in {path.name}")
    values = [row[key].strip() for row in rows]
    if len(values) != expected_count or len(set(values)) != expected_count:
        raise SystemExit(
            f"Expected {expected_count} unique {key} values in {path.name}, "
            f"found {len(values)} rows / {len(set(values))} unique"
        )
    return set(values)


def main() -> int:
    flathub_ids = read_single_column(FLATHUB_PATH, "app_id", EXPECTED_FLATHUB_IDS)
    arch_desktop_ids = read_two_column_ids(
        ARCH_DESKTOP_PATH, "desktop_id", EXPECTED_ARCH_DESKTOP_IDS
    )
    arch_commands = read_two_column_ids(
        ARCH_COMMAND_PATH, "command", EXPECTED_ARCH_COMMANDS
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

    unresolved: dict[str, str] = {}
    for row in application_rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        names = [canonical, *parse_aliases(row["aliases"])]
        if any(name in flathub_ids for name in names):
            continue
        if any(name in arch_desktop_ids for name in names):
            continue
        if any(name in arch_commands for name in names):
            continue
        unresolved[row_id] = canonical

    if len(unresolved) != EXPECTED_PROVENANCE_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_PROVENANCE_ROWS} Stage-F unresolved rows, "
            f"found {len(unresolved)}"
        )

    provenance_rows = read_csv(PROVENANCE_PATH)
    if provenance_rows and list(provenance_rows[0].keys()) != EXPECTED_COLUMNS:
        raise SystemExit(
            f"Unexpected provenance columns: {list(provenance_rows[0].keys())!r}; "
            f"expected {EXPECTED_COLUMNS!r}"
        )
    if len(provenance_rows) != EXPECTED_PROVENANCE_ROWS:
        raise SystemExit(
            f"Expected {EXPECTED_PROVENANCE_ROWS} provenance rows, "
            f"found {len(provenance_rows)}"
        )

    seen_ids: set[str] = set()
    errors: list[str] = []
    status_counts: Counter[str] = Counter()
    class_counts: Counter[str] = Counter()

    for row in provenance_rows:
        row_id = row["id"].strip()
        canonical = row["canonical_name"].strip()
        provenance_class = row["provenance_class"].strip()
        status = row["status"].strip()
        evidence = row["evidence"].strip()
        notes = row["notes"].strip()

        if row_id in seen_ids:
            errors.append(f"duplicate provenance row for {row_id}")
        seen_ids.add(row_id)

        expected_canonical = unresolved.get(row_id)
        if expected_canonical is None:
            errors.append(f"{row_id}: stale provenance row; design is no longer unresolved")
        elif canonical != expected_canonical:
            errors.append(
                f"{row_id}: canonical mismatch {canonical!r} != {expected_canonical!r}"
            )

        if provenance_class not in ALLOWED_CLASSES:
            errors.append(f"{row_id}: invalid provenance_class {provenance_class!r}")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{row_id}: invalid status {status!r}")

        if status == "needs-source":
            if provenance_class != "unknown":
                errors.append(
                    f"{row_id}: needs-source must use provenance_class 'unknown'"
                )
            if evidence:
                errors.append(f"{row_id}: needs-source row must not claim evidence")
        else:
            if not evidence:
                errors.append(f"{row_id}: status {status!r} requires evidence")

        if status == "validated-current" and provenance_class in {
            "retired-product",
            "archived-project",
        }:
            errors.append(
                f"{row_id}: archived/retired provenance cannot be validated-current"
            )
        if status == "validated-historical" and provenance_class not in {
            "retired-product",
            "archived-project",
        }:
            errors.append(
                f"{row_id}: validated-historical requires retired/archive provenance"
            )
        if status == "needs-alias-fix" and provenance_class not in {
            "official-arch-package",
            "framework-command",
        }:
            errors.append(
                f"{row_id}: needs-alias-fix must identify a package/framework source"
            )
        if status == "needs-canonical-review" and provenance_class != "renamed-successor":
            errors.append(
                f"{row_id}: needs-canonical-review must use renamed-successor provenance"
            )
        if not notes:
            errors.append(f"{row_id}: notes must explain the provenance decision")

        status_counts[status] += 1
        class_counts[provenance_class] += 1

    missing = sorted(set(unresolved) - seen_ids)
    if missing:
        errors.append("missing provenance rows: " + ", ".join(missing))

    if errors:
        print(f"Found {len(errors)} application-provenance error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(provenance_rows)} Stage-G provenance review rows.")
    print("Status counts:")
    for status in sorted(status_counts):
        print(f"  {status}: {status_counts[status]}")
    print("Provenance class counts:")
    for provenance_class in sorted(class_counts):
        print(f"  {provenance_class}: {class_counts[provenance_class]}")

    actionable = [
        row for row in provenance_rows
        if row["status"].strip().startswith("needs-")
    ]
    print()
    print(f"Actionable review rows: {len(actionable)}")
    for row in actionable:
        print(
            f"- {row['id'].strip()}: {row['canonical_name'].strip()!r} "
            f"[{row['status'].strip()}]"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
