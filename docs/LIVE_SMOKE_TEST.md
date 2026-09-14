# Witcher3 HyDE Live Smoke Test

**Project:** Witcher 3 HyDE Theme  
**Purpose:** Development-only live validation before the custom `Witcher3-HyDE` icon package is complete  
**Status:** Supported development workflow; not a release/import package

## Why this workflow exists

The repository's real `hypr.theme` declares:

```text
$GTK_THEME = Witcher3
$ICON_THEME = Witcher3-HyDE
$COLOR_SCHEME = prefer-dark
```

Current HyDE validates every explicitly declared resource theme against a matching archive during `theme.patch.sh`.

For Witcher3 this means:

- `Gtk_Witcher3.tar.xz` is required because `$GTK_THEME = Witcher3` is declared.
- `Icon_Witcher3-HyDE.tar.xz` is required because `$ICON_THEME = Witcher3-HyDE` is declared.
- no cursor archive is required because Witcher3 v1 intentionally declares no cursor override.
- at least one wallpaper is required.

The GTK package can already be built and validated reproducibly. The custom icon package cannot be produced honestly until the original icon artwork is complete.

A normal clean import of the repository is therefore intentionally **not release-ready yet**.

The smoke-test workflow exists so the real HyDE runtime integration can still be tested now without shipping placeholder icons or weakening the repository's final icon contract.

## Safety model

`tools/prepare-hyde-live-smoke.sh` does **not** install or switch the live desktop theme.

It creates an ignored staging tree under:

```text
build/hyde-live-smoke/
```

The staging tree contains:

- the real Witcher3 `Configs/` runtime files
- the real Kaer Morhen wallpaper
- a freshly built and validated `Gtk_Witcher3.tar.xz`
- the normal v1 no-cursor policy

It has exactly one intentional development-only difference:

```text
$ICON_THEME = Witcher3-HyDE
```

is removed from the **staged copy** of `hypr.theme` only.

The repository file is never modified by the stager. No fallback or placeholder `Icon_*.tar.*` archive is created.

## 1. Update the repository

From the local clone:

```bash
git pull --ff-only
```

The working tree should be clean before preparing the smoke test:

```bash
git status --short
```

Expected output: no lines.

## 2. Prepare the smoke-test tree

Run:

```bash
./tools/prepare-hyde-live-smoke.sh
```

The script will:

1. build the pinned Colloid-derived Witcher3 GTK package;
2. validate the GTK2, GTK3 and GTK4 runtime tree;
3. validate the GTK archive top-level directory;
4. calculate the archive SHA-256;
5. copy the real Witcher3 runtime files into `build/hyde-live-smoke/`;
6. remove only the unfinished `$ICON_THEME` declaration from the staged `hypr.theme`;
7. confirm that no icon or cursor archive is present;
8. write `build/hyde-live-smoke/DEV_SMOKE_TEST.txt`;
9. remove the generated repository-level GTK archive again after copying it into the ignored staging tree, unless it existed before the invocation.

The repository should therefore remain clean apart from ignored `build/` content.

Verify:

```bash
git status --short
```

Expected output: no lines.

## 3. Review the staging manifest

Before touching the live HyDE installation:

```bash
cat build/hyde-live-smoke/DEV_SMOKE_TEST.txt
```

Also verify the development-only icon omission:

```bash
grep -E '^\$([A-Z_]+_)?THEME' \
  build/hyde-live-smoke/Configs/.config/hyde/themes/Witcher3/hypr.theme
```

The staged file must contain the Witcher3 GTK and color declarations but no `$ICON_THEME` declaration.

The repository file must still contain:

```bash
grep -F '$ICON_THEME = Witcher3-HyDE' \
  Configs/.config/hyde/themes/Witcher3/hypr.theme
```

## 4. Record the currently active HyDE theme

Before importing the smoke tree, record the current theme so it can be restored after testing:

```bash
eval "$(hyde-shell init)"
printf '%s\n' "$HYDE_THEME" | tee build/hyde-live-smoke/PREVIOUS_THEME.txt
```

Do not continue if this produces an empty theme name.

If an existing live Witcher3 development theme already exists at:

```text
~/.config/hyde/themes/Witcher3
```

back it up or remove it deliberately before continuing. Do not overwrite an unknown existing installation blindly.

## 5. Import and apply the development smoke tree

Use the current HyDE installation's own patcher:

```bash
~/.local/lib/hyde/theme.patch.sh \
  Witcher3 \
  "$(pwd)/build/hyde-live-smoke"
```

This is the first step in this runbook that modifies the live HyDE environment.

The patcher should accept the GTK archive, skip the intentionally undeclared icon package, import the runtime files and wallpaper, and use HyDE's normal theme-switch path.

## 6. Live validation checklist

The icon system is explicitly **out of scope** for this smoke test. Do not judge icon appearance yet.

Validate the following:

- Kaer Morhen becomes the Witcher3 wallpaper.
- HyDE creates runtime `wall.set` itself.
- the fixed Witcher3 `theme.dcol` palette is used rather than allowing the wallpaper to redefine the entire interface palette.
- Hyprland borders, gaps, rounding, shadow and blur match the Witcher3 theme.
- Waybar uses the intended dark steel / silver / Witcher-red hierarchy.
- Rofi opens correctly and selection/hover states remain readable.
- Kitty reloads with the Witcher3 palette.
- GTK3 applications render with the `Witcher3` GTK theme.
- GTK4 applications use `Witcher3/gtk-4.0` rather than falling back unexpectedly.
- Dolphin / Qt remains controlled by the Witcher3 Kvantum configuration.
- text, menus, entries, buttons, selected states and disabled states remain readable.
- no obvious missing GTK image/assets warnings occur.
- switching away from Witcher3 and back does not leave stale colors or broken application styling.

Record any component-specific failures before changing files. Fix and retest one component at a time.

## 7. Restore the previous theme

Read the recorded theme:

```bash
cat build/hyde-live-smoke/PREVIOUS_THEME.txt
```

Then restore it through HyDE's current theme switcher:

```bash
eval "$(hyde-shell init)"
~/.local/lib/hyde/theme.switch.sh \
  -s "$(cat build/hyde-live-smoke/PREVIOUS_THEME.txt)"
```

Confirm visually that the previous theme is active again before deleting any development files.

## 8. Optional cleanup after restoring the previous theme

Only after confirming that Witcher3 is no longer active, the development installation may be removed:

```bash
rm -rf "$HOME/.config/hyde/themes/Witcher3"
rm -rf "$HOME/.local/share/themes/Witcher3"
rm -rf build/hyde-live-smoke
```

Do not run this cleanup if those paths contained pre-existing data that was not created by this smoke-test cycle.

## GTK reproducibility baseline

The CI build currently produces byte-identical `Gtk_Witcher3.tar.xz` archives across two complete builds in the same clean runner.

Validated archive contract:

```text
archive: Source/arcs/Gtk_Witcher3.tar.xz
top-level directory: Witcher3/
```

The archive is intentionally not committed as a release/runtime repository asset until the live validation gate in `docs/GTK_BASELINE.md` has passed.

## What this test does not prove

A successful smoke test does **not** mean the full repository is ready for normal clean import or release.

The final clean import still requires the real:

```text
Source/arcs/Icon_Witcher3-HyDE.tar.xz
```

built from accepted original icon artwork.

Do not solve that blocker with an empty icon theme, copied vendor pack, renamed fallback pack or placeholder artwork.

## Exit criterion

After the live smoke test passes:

1. record the GTK3 / GTK4 / Qt / Rofi / Waybar / Kitty results;
2. treat the GTK runtime package as live-validated rather than CI-only;
3. update GTK documentation/provenance as appropriate;
4. continue the original icon artwork pipeline;
5. perform a true clean HyDE repository import only after the real `Witcher3-HyDE` icon archive exists.
