#!/usr/bin/env python3
"""Tests for the strict Witcher3 wallpaper importer."""

from __future__ import annotations

import binascii
import importlib.util
import struct
import sys
import tempfile
import unittest
import zipfile
import zlib
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
IMPORTER_PATH = ROOT / "tools/import-witcher-wallpaper.py"


def load_importer():
    spec = importlib.util.spec_from_file_location("test_witcher_wallpaper_importer", IMPORTER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {IMPORTER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


IMPORTER = load_importer()


def png_chunk(chunk_type: bytes, payload: bytes) -> bytes:
    crc = binascii.crc32(chunk_type)
    crc = binascii.crc32(payload, crc) & 0xFFFFFFFF
    return struct.pack(">I", len(payload)) + chunk_type + payload + struct.pack(">I", crc)


def make_png(
    *,
    width: int = 2560,
    height: int = 1440,
    bit_depth: int = 16,
    color_type: int = 2,
) -> bytes:
    ihdr = struct.pack(">IIBBBBB", width, height, bit_depth, color_type, 0, 0, 0)

    channels = 3 if color_type == 2 else 1
    bytes_per_sample = 2 if bit_depth == 16 else 1
    row = b"\x00" + bytes(width * channels * bytes_per_sample)
    raw = row * height
    idat = zlib.compress(raw, level=9)

    return (
        IMPORTER.PNG_SIGNATURE
        + png_chunk(b"IHDR", ihdr)
        + png_chunk(b"IDAT", idat)
        + png_chunk(b"IEND", b"")
    )


def make_zip(path: Path, members: list[tuple[str, bytes]]) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for name, data in members:
            zf.writestr(name, data)


class WallpaperImporterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.valid_png = make_png()

    def test_valid_png_contract(self) -> None:
        fields = IMPORTER.parse_png(self.valid_png)
        self.assertEqual(fields["width"], 2560)
        self.assertEqual(fields["height"], 1440)
        self.assertEqual(fields["bit_depth"], 16)
        self.assertEqual(fields["color_type"], 2)

    def test_wrong_resolution_is_rejected(self) -> None:
        with self.assertRaisesRegex(IMPORTER.WallpaperError, "unexpected PNG IHDR"):
            IMPORTER.parse_png(make_png(width=1920, height=1080))

    def test_wrong_bit_depth_is_rejected(self) -> None:
        with self.assertRaisesRegex(IMPORTER.WallpaperError, "unexpected PNG IHDR"):
            IMPORTER.parse_png(make_png(bit_depth=8))

    def test_corrupt_crc_is_rejected(self) -> None:
        corrupted = bytearray(self.valid_png)
        # Flip one IHDR payload byte without updating its CRC.
        corrupted[16] ^= 0x01
        with self.assertRaisesRegex(IMPORTER.WallpaperError, "invalid CRC"):
            IMPORTER.parse_png(bytes(corrupted))

    def test_corrupt_idat_stream_is_rejected_even_with_valid_crc(self) -> None:
        ihdr = struct.pack(">IIBBBBB", 2560, 1440, 16, 2, 0, 0, 0)
        broken = (
            IMPORTER.PNG_SIGNATURE
            + png_chunk(b"IHDR", ihdr)
            + png_chunk(b"IDAT", b"not-a-zlib-stream")
            + png_chunk(b"IEND", b"")
        )
        with self.assertRaisesRegex(IMPORTER.WallpaperError, "not valid zlib data"):
            IMPORTER.parse_png(broken)

    def test_duplicate_approved_basename_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            archive = Path(temp_dir) / "wallpapers.zip"
            make_zip(
                archive,
                [
                    (IMPORTER.WALLPAPER_NAME, self.valid_png),
                    (f"nested/{IMPORTER.WALLPAPER_NAME}", self.valid_png),
                ],
            )
            with self.assertRaisesRegex(IMPORTER.WallpaperError, "found 2"):
                IMPORTER.read_approved_wallpaper(archive)

    def test_unsafe_approved_entry_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            archive = Path(temp_dir) / "wallpapers.zip"
            make_zip(archive, [(f"../{IMPORTER.WALLPAPER_NAME}", self.valid_png)])
            with self.assertRaisesRegex(IMPORTER.WallpaperError, "unsafe ZIP entry path"):
                IMPORTER.read_approved_wallpaper(archive)

    def test_import_is_atomic_idempotent_and_does_not_create_wall_set(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            archive = root / "witcher3_.zip"
            make_zip(
                archive,
                [
                    ("other.png", b"not-used"),
                    (IMPORTER.WALLPAPER_NAME, self.valid_png),
                ],
            )

            wallpaper_dir = root / "theme/wallpapers"
            wallpaper_path = wallpaper_dir / IMPORTER.WALLPAPER_NAME
            wall_set_path = root / "theme/wall.set"

            with (
                mock.patch.object(IMPORTER, "WALLPAPER_DIR", wallpaper_dir),
                mock.patch.object(IMPORTER, "WALLPAPER_PATH", wallpaper_path),
                mock.patch.object(IMPORTER, "WALL_SET_PATH", wall_set_path),
            ):
                first_path, first_hash, first_changed = IMPORTER.import_wallpaper(archive)
                second_path, second_hash, second_changed = IMPORTER.import_wallpaper(archive)

            self.assertTrue(first_changed)
            self.assertFalse(second_changed)
            self.assertEqual(first_path, wallpaper_path)
            self.assertEqual(second_path, wallpaper_path)
            self.assertEqual(first_hash, second_hash)
            self.assertEqual(wallpaper_path.read_bytes(), self.valid_png)
            self.assertFalse(wall_set_path.exists())
            self.assertFalse(wall_set_path.is_symlink())

    def test_existing_wall_set_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            archive = root / "witcher3_.zip"
            make_zip(archive, [(IMPORTER.WALLPAPER_NAME, self.valid_png)])

            wallpaper_dir = root / "theme/wallpapers"
            wallpaper_path = wallpaper_dir / IMPORTER.WALLPAPER_NAME
            wall_set_path = root / "theme/wall.set"
            wall_set_path.parent.mkdir(parents=True)
            wall_set_path.write_text("runtime-state-must-not-be-committed", encoding="utf-8")

            with (
                mock.patch.object(IMPORTER, "WALLPAPER_DIR", wallpaper_dir),
                mock.patch.object(IMPORTER, "WALLPAPER_PATH", wallpaper_path),
                mock.patch.object(IMPORTER, "WALL_SET_PATH", wall_set_path),
            ):
                with self.assertRaisesRegex(IMPORTER.WallpaperError, "wall.set"):
                    IMPORTER.import_wallpaper(archive)

            self.assertFalse(wallpaper_path.exists())


if __name__ == "__main__":
    unittest.main()
