# Witcher3 GTK Baseline

**Project:** Witcher 3 HyDE Theme  
**Technical theme name:** `Witcher3`  
**Decision date:** 2026-09-14  
**Status:** GTK base selected; Witcher3 package not built yet

## Decision

Use **Colloid GTK Theme** by `vinceliuice` as the structural upstream base for the Witcher3 GTK package.

The finished HyDE package will not expose an upstream variant name such as `Colloid-Red-Dark`. It will be built as a dedicated Witcher3 derivative with this runtime identity:

```text
$GTK_THEME = Witcher3
```

Planned HyDE archive:

```text
Source/arcs/Gtk_Witcher3.tar.xz
```

Required top-level archive directory:

```text
Witcher3/
```

The archive name, top-level directory, and `$GTK_THEME` value must remain consistent.

## Why Colloid

Colloid is a suitable structural base because it provides:

- GTK 2, GTK 3 and GTK 4 theme sources
- a current dark-theme path suitable for a dark HyDE desktop
- configurable color variants
- an existing build/install pipeline rather than a binary-only package
- a relatively neutral, modern visual structure that can be recolored without forcing a macOS-like identity
- GPL-3.0 source licensing that permits modification and redistribution when the GPL obligations are preserved

The Witcher3 package will use Colloid for layout, widget styling, assets and GTK compatibility structure, while replacing the upstream visual identity with the Witcher3 production palette.

Upstream:

```text
https://github.com/vinceliuice/Colloid-gtk-theme
```

Upstream license:

```text
GNU General Public License v3.0
```

## Why not ship an unmodified upstream variant

A direct package such as:

```text
Colloid-Red-Dark
```

would technically provide a dark red GTK theme, but it would create three problems:

1. The runtime GTK identity would remain Colloid rather than Witcher3.
2. The stock Colloid red does not match the measured Witcher3 palette.
3. Future Witcher3 changes would depend on upstream variant naming instead of a stable project-owned GTK contract.

The Witcher3 GTK package should therefore be a reproducible derivative rather than a renamed prebuilt directory.

## Why Graphite was not selected

Graphite was considered because its dark neutral appearance is visually close to the project direction.

It was rejected as the first production base because current upstream reports include unresolved 2026 GTK4/Libadwaita problems and a reported GTK3 performance regression. Those issues may not affect every Hyprland installation, but they add unnecessary risk to a theme whose GTK package is intended to be a stable HyDE dependency.

Graphite can remain a visual reference, but it is not the selected implementation base.

## HyDE GTK behavior

Current HyDE applies `$GTK_THEME` to GTK configuration during theme switching.

For GTK 4, HyDE checks whether the selected installed GTK theme contains:

```text
<theme-directory>/gtk-4.0/
```

If that directory exists, HyDE links it as the active GTK 4 configuration. If it does not exist, HyDE falls back to:

```text
Wallbash-Gtk
```

Because the Witcher3 derivative is intended to contain a real `gtk-4.0/` directory, that GTK4 implementation must be tested as part of the package. It must not be treated as an unused upstream extra.

The Witcher3 build must not depend on Colloid's optional `--libadwaita` installer behavior at runtime. HyDE owns the GTK4 switch/link operation.

## Witcher3 visual mapping

The source of truth for colors remains:

```text
design/palette/witcher3-color-system.md
```

Initial GTK mapping:

| GTK role | Witcher3 token | Hex |
| --- | --- | --- |
| Primary background | `w3-canvas` | `#0A151E` |
| Main surface | `w3-surface` | `#171A1C` |
| Warm alternate surface | `w3-surface-warm` | `#1C1813` |
| Elevated controls | `w3-elevated` | `#262729` |
| Borders / separators | `w3-border` | `#3D3A39` |
| Primary text | `w3-text-primary` | `#DEE6F0` |
| Secondary text | `w3-text-secondary` | `#B0B6C2` |
| Muted text | `w3-text-muted` | `#8E8B8D` |
| Selection / active accent | `w3-red` | `#B72A18` |
| Pressed / deep accent | `w3-red-deep` | `#621B0E` |
| Warning | `w3-amber` | `#D58E4D` |
| Information | `w3-cyan` | `#3188A6` |
| Success / positive | `w3-alchemy` | `#3DB479` |

### GTK-specific rules

- `w3-red` is the primary selection and active-control color.
- Normal text remains silver/frost rather than red.
- Red text on the primary canvas should be avoided because its measured contrast is insufficient for normal body text.
- Amber, cyan and alchemy green are semantic state colors, not permanent decorative accents.
- Pure `#000000` and pure `#FFFFFF` should not become normal surface/text colors.
- The GTK theme should remain dark-only for the first release. A light Witcher3 GTK variant is outside the initial scope.

## Build-source policy

The distributable `Gtk_Witcher3.tar.xz` is a modified derivative of GPL-3.0 material.

Therefore the repository must retain the information and source material needed to satisfy the upstream license when the archive is distributed.

The implementation phase should include a dedicated GTK source/build area rather than committing only an opaque generated archive.

Planned development layout:

```text
design/gtk/
├── README.md
├── upstream/
│   └── COLLOID_SOURCE.md
├── patches/
│   └── ...
└── build/
    └── ...
```

The exact source-vendoring strategy is intentionally not fixed by this document. Before the first public GTK archive is committed, choose one reproducible GPL-compliant approach:

1. keep the required modified source in this repository, or
2. keep a pinned upstream source reference plus all complete Witcher3 modifications and a reproducible build path, provided this is sufficient for the distributed form and license obligations.

`THIRD_PARTY_NOTICES.md` must identify Colloid, its upstream author/source, its GPL-3.0 license, and the fact that Witcher3 modifies it.

## Build-tool note

Colloid currently builds through `sassc`/LibSass. SassC is now an archived upstream project, so it should be treated as a build-time compatibility dependency rather than a desirable new project dependency.

For the first reproducible build, preserving the upstream build path is acceptable if it works on the target HyDE/Arch environment. A migration to Dart Sass should only be attempted separately and only if output compatibility can be verified.

Do not combine a Sass toolchain migration with the initial Witcher3 recolor.

## Required first build contents

The first generated `Witcher3/` directory should contain at least:

```text
Witcher3/
├── index.theme
├── gtk-2.0/
├── gtk-3.0/
└── gtk-4.0/
```

Other upstream desktop-environment directories should only be included when they are useful to the HyDE target or required by the selected build process. The archive should not be inflated with GNOME Shell, Cinnamon, XFWM, Plank or unrelated desktop assets merely because upstream can generate them.

## Runtime contract

Once the first GTK package passes validation, `hypr.theme` should use:

```text
$GTK_THEME = Witcher3
$ICON_THEME = Witcher3-HyDE
$COLOR_SCHEME = prefer-dark
```

Do not add theme-local `exec = gsettings ...` commands. Current HyDE centrally applies the GTK, icon, cursor, Qt and color-scheme settings during theme switching.

## Validation gate

The GTK package is not considered complete until all of the following pass on the target HyDE installation:

- archive extracts to exactly one top-level `Witcher3/` directory
- `$GTK_THEME = Witcher3` resolves correctly
- GTK3 applications use the Witcher3 theme
- GTK4 applications use `Witcher3/gtk-4.0` through HyDE's normal switch mechanism
- Dolphin/Qt remains controlled by Kvantum rather than being accidentally affected by GTK work
- Flatpak GTK behavior is checked using HyDE's current theme-switch overrides
- text, menu, entry, button, selection and disabled-state contrast is readable
- destructive/selected controls do not become indistinguishable from normal controls
- no missing image/assets warnings appear in GTK application logs
- no broken or recursive symlinks exist inside the archive
- theme switching away from Witcher3 and back again works cleanly

Only after this validation gate passes should `Gtk_Witcher3.tar.xz` be treated as a release asset.

## Next implementation step

Create the reproducible GTK source/build area and produce a **local first-pass `Witcher3` GTK directory** from the selected Colloid base.

Do not commit a generated GTK archive before the source/provenance path and validation procedure exist.
