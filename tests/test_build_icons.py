#!/usr/bin/env python3
"""Tests for the strict Witcher3-HyDE icon builder.

The repository intentionally does not contain generated placeholder artwork.
These tests create a complete 645-SVG fixture in a temporary build directory,
derived from the real matrix, and exercise the same staging/package code used
for releases.
"""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools/build-icons.py"

spec = importlib.util.spec_from_file_location("witcher3_build_icons", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
build_icons = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_icons)

MINIMAL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <path d="M8 8h48v48H8z"/>
</svg>
"""

NETWORK_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <image href="https://example.invalid/icon.png" x="0" y="0" width="64" height="64"/>
</svg>
"""


class IconBuilderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = build_icons.read_matrix()
        (ROOT / "build").mkdir(exist_ok=True)

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="icon-builder-test-", dir=ROOT / "build")
        self.base = Path(self.tempdir.name)
        self.source = self.base / "src"
        self.stage = self.base / "stage" / build_icons.THEME_NAME
        self.archive = self.base / "Icon_Witcher3-HyDE.tar.xz"
        self._write_complete_fixture()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def _write_complete_fixture(self) -> None:
        for row in self.rows:
            path = build_icons.expected_source_path(row, self.source)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(MINIMAL_SVG, encoding="utf-8")

    def test_matrix_and_index_contract(self) -> None:
        self.assertEqual(len(self.rows), 645)
        index = build_icons.index_theme_text()
        self.assertIn("Name=Witcher3-HyDE", index)
        self.assertIn("Inherits=hicolor", index)
        self.assertIn("Context=Applications", index)
        self.assertIn("Context=MimeTypes", index)
        self.assertEqual(index.count("Type=Scalable"), 7)

    def test_complete_fixture_stages_and_packages_reproducibly(self) -> None:
        build_icons.validate_sources(self.rows, self.source)
        build_icons.stage_theme(self.rows, self.source, self.stage)
        build_icons.validate_stage(self.rows, self.stage)

        digest_one = build_icons.package_theme(self.stage, self.archive)
        bytes_one = self.archive.read_bytes()
        self.assertEqual(digest_one, hashlib.sha256(bytes_one).hexdigest())

        digest_two = build_icons.package_theme(self.stage, self.archive)
        bytes_two = self.archive.read_bytes()
        self.assertEqual(digest_one, digest_two)
        self.assertEqual(bytes_one, bytes_two)

        build_icons.validate_archive(self.archive)

    def test_missing_canonical_fails_closed(self) -> None:
        victim = build_icons.expected_source_path(self.rows[0], self.source)
        victim.unlink()
        with self.assertRaisesRegex(ValueError, "Missing canonical SVG"):
            build_icons.validate_sources(self.rows, self.source)

    def test_unexpected_svg_is_rejected(self) -> None:
        unexpected = self.source / "apps" / "not-in-matrix.svg"
        unexpected.write_text(MINIMAL_SVG, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Unexpected source SVGs"):
            build_icons.validate_sources(self.rows, self.source)

    def test_external_network_reference_is_rejected(self) -> None:
        victim = build_icons.expected_source_path(self.rows[0], self.source)
        victim.write_text(NETWORK_SVG, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "external network reference"):
            build_icons.validate_sources(self.rows, self.source)

    def test_canonical_source_symlink_is_rejected(self) -> None:
        first = build_icons.expected_source_path(self.rows[0], self.source)
        second = build_icons.expected_source_path(self.rows[1], self.source)
        first.unlink()
        first.symlink_to(second.relative_to(first.parent))
        with self.assertRaisesRegex(ValueError, "must not be a symlink"):
            build_icons.validate_sources(self.rows, self.source)


if __name__ == "__main__":
    unittest.main()
