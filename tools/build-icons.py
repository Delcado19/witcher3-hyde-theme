#!/usr/bin/env python3
"""Validate, stage, and optionally package the Witcher3-HyDE icon theme.

The 645-row CSV matrix is the source of truth. Canonical SVG artwork must exist
under design/icons/src/<context>/<canonical>.svg. Aliases are emitted as
relative symlinks and never duplicate artwork.

Normal invocation validates and stages only:

    python3 tools/build-icons.py

Release packaging is explicit:

    python3 tools/build-icons.py --package
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import os
from pathlib import Path
import re
import shutil
import sys
import tarfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "design/icons/matrix/witcher-icon-matrix-v1.csv"
SOURCE_ROOT = ROOT / "design/icons/src"
BUILD_ROOT = ROOT / "build/icons"
STAGE_ROOT = BUILD_ROOT / "stage"
THEME_NAME = "Witcher3-HyDE"
THEME_STAGE = STAGE_ROOT / THEME_NAME
ARCHIVE_PATH = ROOT / "Source/arcs/Icon_Witcher3-HyDE.tar.xz"
EXPECTED_DESIGNS = 645

FIELDNAMES = [
    "id",
    "group",
    "canonical_name",
    "witcher_concept",
    "style_class",
    "priority",
    "aliases",
    "notes",
]

GROUP_MAP = {
    "Applications": ("apps", "Applications"),
    "Actions/UI": ("actions", "Actions"),
    "Places/Folders": ("places", "Places"),
    "Status/Panel/Waybar": ("status", "Status"),
    "Devices": ("devices", "Devices"),
    "MIME/Filetypes": ("mimetypes", "MimeTypes"),
    "Categories/Misc": ("categories", "Categories"),
}

STYLE_CLASS_BY_GROUP = {
    "Applications": "Hero",
    "Actions/UI": "Glyph",
    "Places/Folders": "Emblem",
    "Status/Panel/Waybar": "Glyph",
    "Devices": "Emblem",
    "MIME/Filetypes": "Emblem",
    "Categories/Misc": "Emblem",
}

GRAPHIC_ELEMENTS = {
    "circle",
    "ellipse",
    "image",
    "line",
    "path",
    "polygon",
    "polyline",
    "rect",
    "text",
    "use",
}

UNSAFE_NAME_RE = re.compile(r"(?:^\.|/|\\|\x00)")
NETWORK_RE = re.compile(r"(?:https?:)?//", re.IGNORECASE)


def index_theme_text() -> str:
    directories = ",".join(
        f"scalable/{directory}" for directory, _context in GROUP_MAP.values()
    )
    lines = [
        "[Icon Theme]",
        f"Name={THEME_NAME}",
        "Comment=Witcher 3 inspired icon theme for HyDE",
        "Inherits=hicolor",
        f"Directories={directories}",
        "",
    ]
    for directory, context in GROUP_MAP.values():
        lines.extend(
            [
                f"[scalable/{directory}]",
                "Size=48",
                f"Context={context}",
                "Type=Scalable",
                "MinSize=8",
                "MaxSize=1024",
                "",
            ]
        )
    return "\n".join(lines)


def parse_aliases(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(";") if item.strip()]


def safe_icon_name(name: str, *, label: str) -> None:
    if not name:
        raise ValueError(f"{label} is empty")
    if name in {".", ".."} or UNSAFE_NAME_RE.search(name):
        raise ValueError(f"Unsafe {label}: {name!r}")


def read_matrix(path: Path = MATRIX_PATH) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError(f"Matrix not found: {path}")

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != FIELDNAMES:
            raise ValueError(
                f"Unexpected matrix columns: {reader.fieldnames!r}; "
                f"expected {FIELDNAMES!r}"
            )
        rows = [{key: value.strip() for key, value in row.items()} for row in reader]

    if len(rows) != EXPECTED_DESIGNS:
        raise ValueError(
            f"Expected {EXPECTED_DESIGNS} matrix rows, found {len(rows)}"
        )

    canonicals: dict[str, str] = {}
    aliases: dict[str, str] = {}
    ids: set[str] = set()

    for row in rows:
        row_id = row["id"]
        group = row["group"]
        canonical = row["canonical_name"]
        style_class = row["style_class"]

        if not row_id or row_id in ids:
            raise ValueError(f"Duplicate or empty matrix ID: {row_id!r}")
        ids.add(row_id)

        if group not in GROUP_MAP:
            raise ValueError(f"{row_id}: unknown matrix group {group!r}")
        expected_style = STYLE_CLASS_BY_GROUP[group]
        if style_class != expected_style:
            raise ValueError(
                f"{row_id}: style class {style_class!r} does not match "
                f"{group!r} ({expected_style!r})"
            )

        safe_icon_name(canonical, label=f"canonical name for {row_id}")
        owner = canonicals.get(canonical)
        if owner is not None:
            raise ValueError(
                f"Canonical collision: {canonical!r} is owned by {owner} and {row_id}"
            )
        if canonical in aliases:
            raise ValueError(
                f"Canonical {canonical!r} for {row_id} collides with alias of "
                f"{aliases[canonical]}"
            )
        canonicals[canonical] = row_id

        seen_row_aliases: set[str] = set()
        for alias in parse_aliases(row["aliases"]):
            safe_icon_name(alias, label=f"alias for {row_id}")
            if alias == canonical:
                raise ValueError(f"{row_id}: canonical repeated as alias: {alias!r}")
            if alias in seen_row_aliases:
                raise ValueError(f"{row_id}: duplicate alias: {alias!r}")
            seen_row_aliases.add(alias)
            if alias in canonicals:
                raise ValueError(
                    f"Alias {alias!r} for {row_id} collides with canonical of "
                    f"{canonicals[alias]}"
                )
            owner = aliases.get(alias)
            if owner is not None:
                raise ValueError(
                    f"Alias collision: {alias!r} is owned by {owner} and {row_id}"
                )
            aliases[alias] = row_id

    # A canonical can occur after an earlier alias, so verify the complete sets once more.
    overlap = set(canonicals) & set(aliases)
    if overlap:
        sample = ", ".join(sorted(overlap)[:10])
        raise ValueError(f"Canonical/alias namespace overlap: {sample}")

    return rows


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def validate_svg(path: Path) -> None:
    if path.is_symlink():
        raise ValueError(f"Canonical source SVG must not be a symlink: {path}")
    if not path.is_file():
        raise ValueError(f"Missing canonical SVG: {path}")

    try:
        tree = ET.parse(path)
    except (ET.ParseError, OSError) as exc:
        raise ValueError(f"Invalid SVG XML {path}: {exc}") from exc

    root = tree.getroot()
    if local_name(root.tag) != "svg":
        raise ValueError(f"SVG root element is not <svg>: {path}")
    if not root.attrib.get("viewBox", "").strip():
        raise ValueError(f"SVG has no viewBox: {path}")

    has_graphics = False
    for element in root.iter():
        if local_name(element.tag) in GRAPHIC_ELEMENTS:
            has_graphics = True
        for value in element.attrib.values():
            if NETWORK_RE.search(value):
                raise ValueError(
                    f"SVG contains an external network reference in an attribute: {path}"
                )
        if element.text and NETWORK_RE.search(element.text):
            raise ValueError(
                f"SVG contains an external network reference in text/style data: {path}"
            )

    if not has_graphics:
        raise ValueError(f"SVG contains no drawable vector element: {path}")


def expected_source_path(row: dict[str, str], source_root: Path) -> Path:
    directory, _context = GROUP_MAP[row["group"]]
    return source_root / directory / f"{row['canonical_name']}.svg"


def validate_sources(rows: list[dict[str, str]], source_root: Path = SOURCE_ROOT) -> None:
    expected: set[Path] = set()
    errors: list[str] = []

    for row in rows:
        path = expected_source_path(row, source_root)
        expected.add(path)
        try:
            validate_svg(path)
        except ValueError as exc:
            errors.append(str(exc))

    actual: set[Path] = set()
    if source_root.is_dir():
        for path in source_root.rglob("*.svg"):
            actual.add(path)

    unexpected = sorted(actual - expected)
    missing = sorted(expected - actual)

    # Missing paths are already reported by validate_svg. Unexpected artwork gets a
    # dedicated summary because it usually means the matrix and source tree diverged.
    if unexpected:
        errors.append(
            "Unexpected source SVGs not owned by the matrix: "
            + ", ".join(str(path.relative_to(source_root)) for path in unexpected)
        )

    if len(actual & expected) != EXPECTED_DESIGNS:
        errors.append(
            "Canonical source coverage is incomplete: "
            f"{len(actual & expected)} / {EXPECTED_DESIGNS} present"
        )

    if missing and not errors:
        # Defensive fallback; normally every missing path has already been reported.
        errors.append(f"Missing {len(missing)} canonical source SVG(s)")

    if errors:
        preview_limit = 40
        preview = errors[:preview_limit]
        suffix = "" if len(errors) <= preview_limit else (
            f"\n... {len(errors) - preview_limit} additional error(s) omitted"
        )
        raise ValueError("\n".join(preview) + suffix)


def stage_theme(
    rows: list[dict[str, str]],
    source_root: Path = SOURCE_ROOT,
    theme_stage: Path = THEME_STAGE,
) -> None:
    if theme_stage.parent.exists():
        shutil.rmtree(theme_stage.parent)
    theme_stage.mkdir(parents=True, exist_ok=True)

    (theme_stage / "index.theme").write_text(index_theme_text(), encoding="utf-8")

    for directory, _context in GROUP_MAP.values():
        (theme_stage / "scalable" / directory).mkdir(parents=True, exist_ok=True)

    for row in rows:
        directory, _context = GROUP_MAP[row["group"]]
        destination_dir = theme_stage / "scalable" / directory
        canonical = row["canonical_name"]
        source = expected_source_path(row, source_root)
        target = destination_dir / f"{canonical}.svg"
        shutil.copyfile(source, target)
        os.chmod(target, 0o644)

        for alias in parse_aliases(row["aliases"]):
            alias_path = destination_dir / f"{alias}.svg"
            if alias_path.exists() or alias_path.is_symlink():
                raise ValueError(f"Staging collision at alias path: {alias_path}")
            alias_path.symlink_to(f"{canonical}.svg")


def validate_stage(
    rows: list[dict[str, str]], theme_stage: Path = THEME_STAGE
) -> None:
    index_path = theme_stage / "index.theme"
    if index_path.read_text(encoding="utf-8") != index_theme_text():
        raise ValueError("Staged index.theme differs from the fixed build contract")

    expected_paths: set[Path] = {Path("index.theme")}
    canonical_count = 0
    alias_count = 0

    for row in rows:
        directory, _context = GROUP_MAP[row["group"]]
        base = Path("scalable") / directory
        canonical_rel = base / f"{row['canonical_name']}.svg"
        canonical_path = theme_stage / canonical_rel
        expected_paths.add(canonical_rel)
        canonical_count += 1
        if not canonical_path.is_file() or canonical_path.is_symlink():
            raise ValueError(f"Missing staged canonical file: {canonical_rel}")
        validate_svg(canonical_path)

        for alias in parse_aliases(row["aliases"]):
            alias_rel = base / f"{alias}.svg"
            alias_path = theme_stage / alias_rel
            expected_paths.add(alias_rel)
            alias_count += 1
            if not alias_path.is_symlink():
                raise ValueError(f"Alias is not a symlink: {alias_rel}")
            if os.readlink(alias_path) != f"{row['canonical_name']}.svg":
                raise ValueError(
                    f"Alias target mismatch: {alias_rel} -> {os.readlink(alias_path)!r}"
                )
            resolved = alias_path.resolve(strict=False)
            if not resolved.is_file():
                raise ValueError(f"Dangling alias: {alias_rel}")
            if resolved.parent != alias_path.parent.resolve():
                raise ValueError(f"Alias escapes its package directory: {alias_rel}")

    actual_files: set[Path] = set()
    for path in theme_stage.rglob("*"):
        if path.is_file() or path.is_symlink():
            actual_files.add(path.relative_to(theme_stage))

    extras = sorted(actual_files - expected_paths)
    missing = sorted(expected_paths - actual_files)
    if extras or missing:
        raise ValueError(
            f"Staged file graph mismatch; extras={extras!r}, missing={missing!r}"
        )

    if canonical_count != EXPECTED_DESIGNS:
        raise ValueError(
            f"Expected {EXPECTED_DESIGNS} staged canonicals, found {canonical_count}"
        )

    print(f"Staged {canonical_count} canonical SVGs and {alias_count} alias symlinks.")


def add_tar_entry(archive: tarfile.TarFile, path: Path, arcname: str) -> None:
    info = tarfile.TarInfo(arcname)
    info.mtime = 0
    info.uid = 0
    info.gid = 0
    info.uname = ""
    info.gname = ""

    if path.is_symlink():
        info.type = tarfile.SYMTYPE
        info.mode = 0o777
        info.linkname = os.readlink(path)
        info.size = 0
        archive.addfile(info)
    elif path.is_dir():
        info.type = tarfile.DIRTYPE
        info.mode = 0o755
        info.size = 0
        archive.addfile(info)
    elif path.is_file():
        info.type = tarfile.REGTYPE
        info.mode = 0o644
        data = path.read_bytes()
        info.size = len(data)
        archive.addfile(info, io.BytesIO(data))
    else:
        raise ValueError(f"Unsupported staged filesystem entry: {path}")


def package_theme(
    theme_stage: Path = THEME_STAGE, archive_path: Path = ARCHIVE_PATH
) -> str:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = archive_path.with_suffix(archive_path.suffix + ".tmp")
    if temporary.exists():
        temporary.unlink()

    entries = [theme_stage, *sorted(theme_stage.rglob("*"), key=lambda p: p.as_posix())]
    try:
        with tarfile.open(temporary, mode="w:xz", preset=9) as archive:
            for path in entries:
                relative = path.relative_to(theme_stage)
                arcname = THEME_NAME if relative == Path(".") else (
                    f"{THEME_NAME}/{relative.as_posix()}"
                )
                add_tar_entry(archive, path, arcname)
        temporary.replace(archive_path)
    finally:
        if temporary.exists():
            temporary.unlink()

    validate_archive(archive_path)
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    print(f"Packaged {archive_path.relative_to(ROOT)}")
    print(f"SHA-256: {digest}")
    return digest


def validate_archive(archive_path: Path = ARCHIVE_PATH) -> None:
    if not archive_path.is_file():
        raise ValueError(f"Archive not found: {archive_path}")

    with tarfile.open(archive_path, mode="r:xz") as archive:
        members = archive.getmembers()
        if not members:
            raise ValueError("Icon archive is empty")
        top_levels = {member.name.split("/", 1)[0] for member in members}
        if top_levels != {THEME_NAME}:
            raise ValueError(
                f"Archive top-level entries {sorted(top_levels)!r} do not match {THEME_NAME!r}"
            )
        for member in members:
            parts = Path(member.name).parts
            if member.name.startswith("/") or ".." in parts:
                raise ValueError(f"Unsafe archive member path: {member.name!r}")
            if member.issym():
                if Path(member.linkname).is_absolute() or ".." in Path(member.linkname).parts:
                    raise ValueError(
                        f"Unsafe archive symlink target: {member.name!r} -> {member.linkname!r}"
                    )


def run(*, package: bool) -> None:
    rows = read_matrix()
    print(f"Validated matrix contract for {len(rows)} canonical designs.")

    validate_sources(rows)
    print(f"Validated {EXPECTED_DESIGNS} canonical source SVGs.")

    stage_theme(rows)
    validate_stage(rows)

    if package:
        package_theme()
    else:
        print("Staging validation passed. Use --package to create the release archive.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate and build the Witcher3-HyDE icon theme."
    )
    parser.add_argument(
        "--package",
        action="store_true",
        help="create Source/arcs/Icon_Witcher3-HyDE.tar.xz after validation",
    )
    args = parser.parse_args()

    try:
        run(package=args.package)
    except ValueError as exc:
        print(f"Icon build failed:\n{exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
