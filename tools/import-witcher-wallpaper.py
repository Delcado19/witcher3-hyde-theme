#!/usr/bin/env python3
"""Import the approved Witcher3 Kaer Morhen wallpaper from a local ZIP archive.

The importer is intentionally narrow. It accepts exactly the approved
`witcher3_kaer_morhen.png` screenshot, validates its PNG structure and expected
2560x1440 16-bit RGB format, and copies it into the HyDE theme's `wallpapers/`
directory. It never creates or modifies `wall.set`; current HyDE owns that
runtime symlink when the theme is applied.
"""

from __future__ import annotations

import argparse
import binascii
import hashlib
import os
import struct
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
WALLPAPER_NAME = "witcher3_kaer_morhen.png"
WALLPAPER_DIR = ROOT / "Configs/.config/hyde/themes/Witcher3/wallpapers"
WALLPAPER_PATH = WALLPAPER_DIR / WALLPAPER_NAME
WALL_SET_PATH = ROOT / "Configs/.config/hyde/themes/Witcher3/wall.set"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_WIDTH = 2560
EXPECTED_HEIGHT = 1440
EXPECTED_BIT_DEPTH = 16
EXPECTED_COLOR_TYPE = 2  # Truecolour RGB, no palette/alpha.
EXPECTED_COMPRESSION = 0
EXPECTED_FILTER = 0
EXPECTED_INTERLACE = 0


class WallpaperError(ValueError):
    """Raised when the source archive or wallpaper violates the import contract."""


def parse_png(data: bytes) -> dict[str, int]:
    """Validate basic PNG structure/chunk CRCs and return IHDR fields."""
    if not data.startswith(PNG_SIGNATURE):
        raise WallpaperError("wallpaper is not a PNG file")

    offset = len(PNG_SIGNATURE)
    ihdr: dict[str, int] | None = None
    seen_idat = False
    seen_iend = False

    while offset < len(data):
        if offset + 12 > len(data):
            raise WallpaperError("truncated PNG chunk header")

        length = struct.unpack(">I", data[offset : offset + 4])[0]
        chunk_type = data[offset + 4 : offset + 8]
        chunk_data_start = offset + 8
        chunk_data_end = chunk_data_start + length
        crc_end = chunk_data_end + 4
        if crc_end > len(data):
            raise WallpaperError("truncated PNG chunk payload")

        chunk_data = data[chunk_data_start:chunk_data_end]
        stored_crc = struct.unpack(">I", data[chunk_data_end:crc_end])[0]
        calculated_crc = binascii.crc32(chunk_type)
        calculated_crc = binascii.crc32(chunk_data, calculated_crc) & 0xFFFFFFFF
        if stored_crc != calculated_crc:
            name = chunk_type.decode("ascii", errors="replace")
            raise WallpaperError(f"PNG chunk {name!r} has an invalid CRC")

        if chunk_type == b"IHDR":
            if ihdr is not None:
                raise WallpaperError("PNG contains multiple IHDR chunks")
            if offset != len(PNG_SIGNATURE) or length != 13:
                raise WallpaperError("PNG IHDR must be the first chunk and 13 bytes long")
            (
                width,
                height,
                bit_depth,
                color_type,
                compression,
                filter_method,
                interlace,
            ) = struct.unpack(">IIBBBBB", chunk_data)
            ihdr = {
                "width": width,
                "height": height,
                "bit_depth": bit_depth,
                "color_type": color_type,
                "compression": compression,
                "filter": filter_method,
                "interlace": interlace,
            }
        elif chunk_type == b"IDAT":
            seen_idat = True
        elif chunk_type == b"IEND":
            if length != 0:
                raise WallpaperError("PNG IEND chunk must be empty")
            seen_iend = True
            offset = crc_end
            break

        offset = crc_end

    if ihdr is None:
        raise WallpaperError("PNG has no IHDR chunk")
    if not seen_idat:
        raise WallpaperError("PNG has no IDAT chunk")
    if not seen_iend:
        raise WallpaperError("PNG has no IEND chunk")
    if offset != len(data):
        raise WallpaperError("PNG contains trailing data after IEND")

    expected = {
        "width": EXPECTED_WIDTH,
        "height": EXPECTED_HEIGHT,
        "bit_depth": EXPECTED_BIT_DEPTH,
        "color_type": EXPECTED_COLOR_TYPE,
        "compression": EXPECTED_COMPRESSION,
        "filter": EXPECTED_FILTER,
        "interlace": EXPECTED_INTERLACE,
    }
    if ihdr != expected:
        raise WallpaperError(f"unexpected PNG IHDR: {ihdr!r}; expected {expected!r}")

    return ihdr


def safe_member_name(info: zipfile.ZipInfo) -> PurePosixPath:
    name = PurePosixPath(info.filename)
    if info.is_dir():
        raise WallpaperError(f"expected a file, found directory entry {info.filename!r}")
    if name.is_absolute() or ".." in name.parts:
        raise WallpaperError(f"unsafe ZIP entry path: {info.filename!r}")
    return name


def read_approved_wallpaper(archive: Path) -> bytes:
    if not archive.is_file():
        raise WallpaperError(f"archive does not exist: {archive}")

    try:
        with zipfile.ZipFile(archive, "r") as zf:
            matches: list[zipfile.ZipInfo] = []
            for info in zf.infolist():
                name = PurePosixPath(info.filename)
                if name.name == WALLPAPER_NAME:
                    safe_member_name(info)
                    matches.append(info)

            if len(matches) != 1:
                raise WallpaperError(
                    f"expected exactly one {WALLPAPER_NAME!r} in the archive, "
                    f"found {len(matches)}"
                )

            data = zf.read(matches[0])
    except zipfile.BadZipFile as exc:
        raise WallpaperError(f"invalid ZIP archive: {archive}") from exc

    parse_png(data)
    return data


def atomic_write(path: Path, data: bytes, *, force: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        if path.is_symlink() or not path.is_file():
            raise WallpaperError(f"destination is not a regular file: {path}")
        current = path.read_bytes()
        if current == data:
            return False
        if not force:
            raise WallpaperError(
                f"destination already exists with different content: {path}; "
                "use --force only if replacement is intentional"
            )

    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    finally:
        if tmp_path.exists():
            tmp_path.unlink()
    return True


def import_wallpaper(archive: Path, *, force: bool = False) -> tuple[Path, str, bool]:
    if WALL_SET_PATH.lexists() if hasattr(WALL_SET_PATH, "lexists") else False:
        # pathlib has no lexists on current supported Python versions; retained
        # only as a defensive no-op for alternate implementations.
        raise WallpaperError("wall.set must remain HyDE-managed runtime state")
    if os.path.lexists(WALL_SET_PATH):
        raise WallpaperError(
            f"repository already contains {WALL_SET_PATH}; remove it because current HyDE "
            "creates wall.set at runtime"
        )

    data = read_approved_wallpaper(archive)
    changed = atomic_write(WALLPAPER_PATH, data, force=force)
    digest = hashlib.sha256(data).hexdigest()
    return WALLPAPER_PATH, digest, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="path to the local witcher3_.zip archive")
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing different Kaer Morhen wallpaper after validation",
    )
    args = parser.parse_args()

    try:
        path, digest, changed = import_wallpaper(args.archive.resolve(), force=args.force)
    except WallpaperError as exc:
        parser.error(str(exc))

    action = "Imported" if changed else "Already current"
    print(f"{action}: {path.relative_to(ROOT)}")
    print(f"SHA-256: {digest}")
    print("wall.set: not created (managed by HyDE at runtime)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
