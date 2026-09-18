import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "reconstruct-hero-svg.py"
SPEC = importlib.util.spec_from_file_location("hero_reconstruct", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class HeroSvgReconstructionHelpersTest(unittest.TestCase):
    def test_relative_polygon_path(self):
        self.assertEqual(
            MODULE.relative_polygon_path(
                [(10, 10), (15, 10), (15, 18), (10, 18)]
            ),
            "M10 10l5 0 0 8 -5 0z",
        )

    def test_fidelity_preset_is_denser_than_balanced(self):
        fidelity = MODULE.preset_config("fidelity")
        balanced = MODULE.preset_config("balanced")
        self.assertGreater(fidelity["segments"], balanced["segments"])
        self.assertGreater(fidelity["palette"], balanced["palette"])
        self.assertLess(fidelity["epsilon"], balanced["epsilon"])

    def test_unknown_preset_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.preset_config("nope")

    def test_brilliance_presets_are_ordered(self):
        off = MODULE.brilliance_config("off")
        balanced = MODULE.brilliance_config("balanced")
        punchy = MODULE.brilliance_config("punchy")
        self.assertEqual(off["contrast"], 1.0)
        self.assertGreater(balanced["contrast"], off["contrast"])
        self.assertGreater(punchy["chroma"], balanced["chroma"])
        self.assertGreater(punchy["highlight"], balanced["highlight"])

    def test_unknown_brilliance_preset_rejected(self):
        with self.assertRaises(ValueError):
            MODULE.brilliance_config("nope")

    def test_surface_smoothing_keeps_real_vector_art_once(self):
        svg = MODULE._emit_svg(
            analysis_size=512,
            art_paths='<path d="M0 0h10v10z" fill="#fff"/>',
            seam_stroke=0.55,
            smoothing=True,
            edge_path="M0 0h4v4z",
            smooth_blur=1.1,
            smooth_detail_opacity=0.04,
        )
        self.assertIn("feGaussianBlur", svg)
        self.assertIn('mask id="strongEdges"', svg)
        self.assertIn('xlink:href="#heroArt"', svg)
        self.assertNotIn("<image", svg)
        self.assertEqual(svg.count('<path d="M0 0h10v10z"'), 1)


if __name__ == "__main__":
    unittest.main()
