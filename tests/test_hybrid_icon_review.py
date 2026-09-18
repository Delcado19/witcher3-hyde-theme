#!/usr/bin/env python3
"""Tests for the Witcher3-HyDE hybrid crossover review generator."""

from __future__ import annotations

import binascii
import importlib.util
from pathlib import Path
import struct
import tempfile
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools/build-hybrid-icon-review.py"

spec = importlib.util.spec_from_file_location("witcher3_hybrid_review", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
hybrid_review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hybrid_review)

MINIMAL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <path d="M8 8h48v48H8z"/>
</svg>
"""


def png_chunk(kind: bytes, payload: bytes) -> bytes:
    crc = binascii.crc32(kind)
    crc = binascii.crc32(payload, crc) & 0xFFFFFFFF
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", crc)


def write_png(path: Path, size: int) -> None:
    signature = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    row = b"\x00" + (b"\x20\x40\x60\xff" * size)
    raw = row * size
    data = signature + png_chunk(b"IHDR", ihdr)
    data += png_chunk(b"IDAT", zlib.compress(raw, level=9))
    data += png_chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


class HybridIconReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (ROOT / "build").mkdir(exist_ok=True)

    def test_png_dimensions(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hybrid-review-", dir=ROOT / "build") as tmp:
            path = Path(tmp) / "master.png"
            write_png(path, 512)
            self.assertEqual(hybrid_review.png_dimensions(path), (512, 512))

    def test_complete_master_covers_all_review_sizes(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hybrid-review-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            svg = base / "sample.svg"
            master = base / "master.png"
            output = base / "review.html"
            svg.write_text(MINIMAL_SVG, encoding="utf-8")
            write_png(master, 512)
            available, missing = hybrid_review.generate_review(svg, master, None, output)
            self.assertEqual(available, len(hybrid_review.SIZES))
            self.assertEqual(missing, [])
            document = output.read_text(encoding="utf-8")
            self.assertIn("master downscale (512px)", document)
            self.assertIn("32px", document)
            self.assertIn("96px", document)
            self.assertIn("512px", document)
            self.assertIn("#0A151E", document)
            self.assertIn("#F2F0EA", document)

    def test_optimized_png_overrides_master(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hybrid-review-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            svg = base / "sample.svg"
            master = base / "master.png"
            optimized = base / "optimized"
            output = base / "review.html"
            svg.write_text(MINIMAL_SVG, encoding="utf-8")
            write_png(master, 512)
            write_png(optimized / "64.png", 64)
            hybrid_review.generate_review(svg, master, optimized, output)
            self.assertIn("optimized 64.png", output.read_text(encoding="utf-8"))

    def test_wrong_optimized_dimensions_fail(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hybrid-review-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            svg = base / "sample.svg"
            master = base / "master.png"
            optimized = base / "optimized"
            output = base / "review.html"
            svg.write_text(MINIMAL_SVG, encoding="utf-8")
            write_png(master, 512)
            write_png(optimized / "64.png", 48)
            with self.assertRaises(ValueError):
                hybrid_review.generate_review(svg, master, optimized, output)

    def test_missing_raster_is_reported_incrementally(self) -> None:
        with tempfile.TemporaryDirectory(prefix="hybrid-review-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            svg = base / "sample.svg"
            output = base / "review.html"
            svg.write_text(MINIMAL_SVG, encoding="utf-8")
            available, missing = hybrid_review.generate_review(svg, None, None, output)
            self.assertEqual(available, 0)
            self.assertEqual(missing, list(hybrid_review.SIZES))
            self.assertIn("missing PNG", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
