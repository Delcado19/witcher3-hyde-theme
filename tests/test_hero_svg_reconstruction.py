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


if __name__ == "__main__":
    unittest.main()
