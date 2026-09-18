#!/usr/bin/env python3
"""Tests for the Witcher3-HyDE pilot review sheet generator."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools/build-icon-review.py"

spec = importlib.util.spec_from_file_location("witcher3_icon_review", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
icon_review = importlib.util.module_from_spec(spec)
spec.loader.exec_module(icon_review)

MINIMAL_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <path d="M8 8h48v48H8z"/>
</svg>
"""


class IconReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        (ROOT / "build").mkdir(exist_ok=True)
        cls.rows = icon_review.pilot_rows()

    def test_pilot_contract_matches_matrix(self) -> None:
        self.assertEqual(len(self.rows), 14)
        self.assertEqual(self.rows[0]["id"], "W3-409")
        self.assertEqual(self.rows[1]["id"], "W3-398")
        self.assertEqual(self.rows[4]["id"], "W3-228")
        self.assertEqual(self.rows[5]["id"], "W3-236")
        self.assertEqual(self.rows[-1]["canonical_name"], "kitty")

    def test_incomplete_review_marks_all_missing(self) -> None:
        with tempfile.TemporaryDirectory(prefix="icon-review-test-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            output = base / "review.html"
            present, missing = icon_review.generate_review(base / "src", output)

            self.assertEqual(present, 0)
            self.assertEqual(len(missing), 14)
            document = output.read_text(encoding="utf-8")
            self.assertIn("0 / 14 pilot SVGs present", document)
            self.assertIn("MISSING SOURCE SVG", document)
            self.assertIn("audio-volume-high", document)

    def test_complete_review_embeds_svg_and_required_surfaces(self) -> None:
        with tempfile.TemporaryDirectory(prefix="icon-review-test-", dir=ROOT / "build") as tmp:
            base = Path(tmp)
            source = base / "src"
            output = base / "review.html"

            for row in self.rows:
                path = icon_review.build_icons.expected_source_path(row, source)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(MINIMAL_SVG, encoding="utf-8")

            present, missing = icon_review.generate_review(source, output)
            self.assertEqual(present, 14)
            self.assertEqual(missing, [])

            document = output.read_text(encoding="utf-8")
            self.assertIn("14 / 14 pilot SVGs present", document)
            self.assertIn("data:image/svg+xml;base64,", document)
            for color in ("#0A151E", "#171A1C", "#1C1813", "#262729", "#F2F0EA"):
                self.assertIn(color, document)
            for label in ("16px", "22px", "24px", "32px", "48px", "64px", "128px", "256px", "512px"):
                self.assertIn(label, document)


if __name__ == "__main__":
    unittest.main()
