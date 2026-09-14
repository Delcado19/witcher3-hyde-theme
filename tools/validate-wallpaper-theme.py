#!/usr/bin/env python3
"""Validate the Witcher3 theme wallpaper repository state.

During development the repository may contain no wallpaper yet. Once artwork is
present, the initial baseline deliberately permits exactly one canonical
wallpaper: `witcher3_kaer_morhen.png`. Keeping a single file makes current
HyDE's first-run wallpaper selection deterministic without committing the
runtime `wall.set` symlink.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMPORTER_PATH = ROOT / "tools/import-witcher-wallpaper.py"
WALLPAPER_DIR = ROOT / "Configs/.config/hyde/themes/Witcher3/wallpapers"
WALL_SET_PATH = ROOT / "Configs/.config/hyde/themes/Witcher3/wall.set"
NOTICES_PATH = ROOT / "THIRD_PARTY_NOTICES.md"


def load_importer():
    spec = importlib.util.spec_from_file_location("witcher_wallpaper_importer", IMPORTER_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit(f"Unable to load {IMPORTER_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    importer = load_importer()
    errors: list[str] = []

    if os.path.lexists(WALL_SET_PATH):
        errors.append(
            "wall.set must not be committed; current HyDE creates that symlink at runtime"
        )

    if not WALLPAPER_DIR.exists():
        print("Wallpaper artwork: 0 / 1 (development state; wallpaper pending).")
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        return 0

    if not WALLPAPER_DIR.is_dir():
        errors.append(f"wallpaper path is not a directory: {WALLPAPER_DIR}")
        files: list[Path] = []
    else:
        entries = sorted(WALLPAPER_DIR.iterdir(), key=lambda path: path.name)
        unexpected_nonfiles = [path for path in entries if path.is_symlink() or not path.is_file()]
        for path in unexpected_nonfiles:
            errors.append(f"unexpected non-regular wallpaper entry: {path.relative_to(ROOT)}")
        files = [path for path in entries if path.is_file() and not path.is_symlink()]

    expected_names = [importer.WALLPAPER_NAME]
    names = [path.name for path in files]
    if names != expected_names:
        errors.append(
            f"initial wallpaper baseline must contain exactly {expected_names!r}; found {names!r}"
        )

    if files and files[0].name == importer.WALLPAPER_NAME:
        try:
            importer.parse_png(files[0].read_bytes())
        except importer.WallpaperError as exc:
            errors.append(f"{files[0].name}: {exc}")

    if NOTICES_PATH.is_file():
        notices = NOTICES_PATH.read_text(encoding="utf-8")
        required_markers = (
            "CD PROJEKT RED Fan Content Guidelines",
            "Configs/.config/hyde/themes/Witcher3/wallpapers/",
        )
        for marker in required_markers:
            if marker not in notices:
                errors.append(f"THIRD_PARTY_NOTICES.md is missing provenance marker {marker!r}")
    else:
        errors.append("THIRD_PARTY_NOTICES.md is missing")

    if errors:
        print(f"Found {len(errors)} wallpaper validation error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Wallpaper artwork: 1 / 1.")
    print(f"Validated: {WALLPAPER_DIR.relative_to(ROOT) / importer.WALLPAPER_NAME}")
    print("wall.set: absent from repository (correct; HyDE-managed runtime state).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
