# HyDE Reference Theme Matrix

**Project:** Witcher 3 HyDE Theme  
**Theme name:** `Witcher3`  
**Icon theme name:** `Witcher3-HyDE`  
**Audit date:** 2026-09-14

This document records the technical baseline for implementing the Witcher 3 HyDE theme. It is based on the current HyDE theme patch/switch implementation, the HyDE theme starter workflow, and five real-world HyDE themes maintained by `rishav12s`.

The goal is to separate current HyDE requirements from historical conventions and theme-specific choices before runtime files are added to this repository.

## Source hierarchy

Use sources in this order when implementation details disagree:

1. **Current HyDE implementation** — technical source of truth.
2. **Current theme-starter workflow** — preferred development and generation workflow.
3. **Maintained real-world themes by `rishav12s`** — practical implementation references.
4. **Older official/community themes** — visual or historical references only.

Primary references:

- https://github.com/HyDE-Project/HyDE/blob/master/Configs/.local/lib/hyde/theme.patch.sh
- https://github.com/HyDE-Project/HyDE/blob/master/Configs/.local/lib/hyde/theme.switch.sh
- https://github.com/richen604/hyde-theme-starter/blob/main/justfile
- https://github.com/rishav12s/Vanta-Black
- https://github.com/rishav12s/Cat-Latte
- https://github.com/rishav12s/Rain-Dark
- https://github.com/rishav12s/Solarized-Dark
- https://github.com/rishav12s/Monterey-Frost

## Reference-theme comparison

| Component | Vanta Black | Cat Latte | Rain Dark | Solarized Dark | Monterey Frost | Witcher3 decision |
| --- | --- | --- | --- | --- | --- | --- |
| `hypr.theme` | Yes | Yes | Yes | Yes | Yes | **Required** |
| `waybar.theme` | Yes | Yes | Yes | Yes | Yes | **Include** |
| `rofi.theme` | Yes | Yes | Yes | Yes | Yes | **Include** |
| `kitty.theme` | Yes | Yes | Yes | Yes | Yes | **Include** |
| `kvantum/kvantum.theme` | Yes | Yes | Yes | Yes | Yes | **Include** |
| `kvantum/kvconfig.theme` | Yes | Yes | Yes | Yes | Yes | **Include** |
| `theme.dcol` | Yes | Yes | No | Yes | No | **Recommended** |
| `wallpapers/` | Yes | Yes | Yes | Yes | Yes | **Required** |
| `wall.set` committed | No | No | No | No | No | **Do not commit; HyDE runtime state** |
| GTK archive | Yes | Yes | Yes | Yes | Yes | **Required by HyDE patcher** |
| Icon archive | Yes | Yes | Yes | Yes | Yes | **Required by this project** |
| Cursor archive | Yes | Yes | Yes | Yes | Yes | **No for v1; optional post-v1** |
| Font archive | No | No | No | No | Yes | Optional |
| `cava.theme` | Yes | No | No | No | No | Optional; not baseline |
| Active legacy `exec = gsettings ...` | Yes | Yes | Yes | Yes | No; commented | **Do not copy** |

## Current HyDE requirements

### Theme directory

The patcher expects the selected theme at:

```text
Configs/.config/hyde/themes/<Theme Name>/
```

For this project:

```text
Configs/.config/hyde/themes/Witcher3/
```

### Wallpapers

At least one supported wallpaper is required for a valid imported theme. Current HyDE accepts image files such as PNG, JPG/JPEG and GIF from the theme directory and treats the absence of wallpapers as an error.

The preferred layout is:

```text
Configs/.config/hyde/themes/Witcher3/
└── wallpapers/
    └── <project-owned-or-redistributable-wallpaper>.png
```

Do not add a placeholder copied from another theme merely to satisfy the patcher. The repository asset policy still applies.

### `wall.set`

`wall.set` is HyDE-managed runtime state and is intentionally not committed by Witcher3. Current HyDE checks it during theme switching. If it is missing or invalid, HyDE chooses the first available file in `wallpapers/` and creates the symlink automatically.

The v1 baseline bundles exactly one validated wallpaper, `witcher3_kaer_morhen.png`, so this fallback is deterministic without storing an install-local `wall.set` symlink in the repository.

### GTK package

The current theme patcher checks the GTK package as mandatory. The value declared by `$GTK_THEME` in `hypr.theme` must correspond to the top-level theme contained in a matching `Gtk_*.tar.*` archive.

Therefore a complete Witcher3 import cannot be considered finished until a redistributable GTK theme package has been selected or built and verified.

### Icon package

HyDE itself treats the icon archive as optional. This project does not: a custom desktop-wide Witcher icon theme is a core project deliverable.

Planned package:

```text
Source/arcs/Icon_Witcher3-HyDE.tar.xz
```

The archive's top-level directory must match the `$ICON_THEME` value used by `hypr.theme`.

## Archive conventions

Current HyDE recognizes archive prefixes including:

| Prefix | Hyprland variable | Target |
| --- | --- | --- |
| `Gtk_` | `$GTK_THEME` | `~/.local/share/themes` |
| `Icon_` | `$ICON_THEME` | `~/.local/share/icons` |
| `Cursor_` | `$CURSOR_THEME` | `~/.local/share/icons` |
| `Font_` | `$FONT` | `~/.local/share/fonts` |
| `Document-Font_` | `$DOCUMENT_FONT` | `~/.local/share/fonts` |
| `Monospace-Font_` | `$MONOSPACE_FONT` | `~/.local/share/fonts` |
| `Bar-Font_` | `$BAR_FONT` | `~/.local/share/fonts` |
| `Menu-Font_` | `$MENU_FONT` | `~/.local/share/fonts` |
| `Notification-Font_` | `$NOTIFICATION_FONT` | `~/.local/share/fonts` |
| `Sddm_` | `$SDDM_THEME` | `/usr/share/sddm/themes` |

The real-world reference themes consistently store these under:

```text
Source/arcs/
```

Both `.tar.gz` and `.tar.xz` occur in maintained themes. The important contract is the archive prefix, the declared variable, and the top-level directory inside the archive — not one specific compression format.

### Cursor archive status

`Cursor_*.tar.*` is recognized by current HyDE but is optional. The current HyDE default environment uses `Bibata-Modern-Ice` at size `24`, and `theme.switch.sh` falls back to the loaded HyDE/user cursor settings when a theme does not declare `$CURSOR_THEME` or `$CURSOR_SIZE`.

Witcher3 v1 intentionally does not declare either variable and ships no cursor archive. See [`CURSOR_DECISION.md`](CURSOR_DECISION.md) for the complete decision and revisit criteria.

## `hypr.theme` rules for Witcher3

All five audited themes use the HyDE destination header:

```text
$HOME/.config/hypr/themes/theme.conf|> $HOME/.config/hypr/themes/colors.conf
```

Older themes then commonly execute commands such as:

```text
exec = gsettings set ...
exec = Hyde cursor theme ...
exec = Hyde code theme ...
```

Do **not** copy that pattern into Witcher3 by default.

Current HyDE parses theme variables from `hypr.theme` and applies icon, GTK, cursor, Qt and font settings during `theme.switch.sh`. The modern Witcher3 file should therefore primarily declare variables and Hyprland visual settings rather than re-applying desktop settings through theme-local `exec` commands.

The v1 theme-owned variable set is:

```text
$GTK_THEME = Witcher3
$ICON_THEME = Witcher3-HyDE
$COLOR_SCHEME = prefer-dark
```

`$CURSOR_THEME` and `$CURSOR_SIZE` are intentionally absent in v1 so the existing HyDE/user cursor remains authoritative.

Fonts should only be declared if the theme intentionally owns the font choice. Do not hard-code a font into Rofi or Kitty merely because a reference theme does so.

`$CODE_THEME` is still understood by current HyDE, but current HyDE can fall back to Wallbash. It should be added only if Witcher3 deliberately ships or selects a compatible code theme.

## Waybar baseline

The five reference themes use the same small color interface:

```text
@define-color bar-bg ...;
@define-color main-bg ...;
@define-color main-fg ...;
@define-color wb-act-bg ...;
@define-color wb-act-fg ...;
@define-color wb-hvr-bg ...;
@define-color wb-hvr-fg ...;
```

They also use the same destination/generator header:

```text
$HOME/.config/waybar/theme.css|${scrDir}/wbarconfgen.sh
```

This makes `waybar.theme` a good first runtime file once the Witcher palette is frozen.

## Rofi baseline

The reference themes consistently define:

```text
main-bg
main-fg
main-br
main-ex
select-bg
select-fg
separatorcolor
border-color
```

with the destination header:

```text
$HOME/.config/rofi/theme.rasi
```

Monterey Frost additionally hard-codes a Rofi font. Witcher3 should avoid this initially and inherit the normal HyDE font configuration.

## Kitty baseline

`kitty.theme` is a normal Kitty palette with the destination/reload header:

```text
$HOME/.config/kitty/theme.conf|killall -SIGUSR1 kitty
```

The audited themes vary significantly in how much they override. Witcher3 should initially own colors only. Terminal font family, terminal opacity and unrelated user preferences should remain outside the theme unless later testing shows a strong reason to include them.

## Kvantum baseline

The maintained themes use two files:

```text
kvantum/
├── kvantum.theme
└── kvconfig.theme
```

The first is effectively the themed Wallbash/Kvantum SVG and the second is the matching Kvantum configuration. The starter workflow generates them from a working HyDE setup.

Do not hand-author these as the first implementation step. Generate or derive them from a known-good local HyDE state after the core palette is stable.

## `theme.dcol`

`theme.dcol` is optional in the current patcher. When present, HyDE explicitly uses it to override wallpaper-derived dominant colors.

This is useful for Witcher3 because the project wants a deliberate, consistent UI identity rather than allowing every wallpaper to redefine the full desktop palette.

Decision: **include `theme.dcol` after the palette is approved.**

## GTK 4

Do not add an independent `gtk-4.0/` directory merely because an older checklist suggests it.

Current HyDE first checks whether the selected GTK theme itself provides a `gtk-4.0` directory. If not, it falls back to `Wallbash-Gtk` for GTK 4. The Witcher3 decision therefore depends on the final GTK archive rather than on an empty repository stub.

## Components not in the baseline

Do not add these simply to make the repository look complete:

```text
hyprlock.theme
animations.theme
cava.theme
gtk-4.0/
logo/
```

They may be added later if there is a demonstrated HyDE integration or a deliberate Witcher3 design requirement.

`cava.theme` exists in Vanta Black, but it is not part of the starter's normal generated set and is not shared by the other audited reference themes.

## Recommended Witcher3 implementation order

1. Freeze the first Witcher3 UI palette and contrast rules.
2. Select or build the redistributable GTK base and determine the exact `$GTK_THEME` name.
3. Add one project-owned or redistributable test wallpaper.
4. Implement a modern `hypr.theme` without legacy `exec` side effects.
5. Implement and test `waybar.theme`.
6. Implement and test `rofi.theme`.
7. Implement and test `kitty.theme`.
8. Generate/derive Kvantum files from the working HyDE setup.
9. Generate and review `theme.dcol` so Wallbash keeps the intended Witcher palette.
10. Develop `Witcher3-HyDE` as an independent icon subproject and package it as `Icon_Witcher3-HyDE.tar.*`.
11. Keep cursor ownership with HyDE/user configuration for v1; revisit only for a complete original Witcher cursor family.

## Reference-specific lessons

### Vanta Black

Useful for deep-black contrast decisions and for seeing a theme that includes `theme.dcol` and an additional `cava.theme`. It also received later icon/symlink fixes, which reinforces the need to validate icon inheritance and symlinks rather than only checking appearance.

### Cat Latte

Most useful as an example of deliberately correcting inconsistencies in an existing official theme. It is a better process reference than a visual reference for Witcher3.

### Rain Dark

Useful as a clean example of the standard `Configs/` plus `Source/arcs/` package layout.

### Solarized Dark

Useful for deliberate color control through `theme.dcol` and for keeping application palettes coherent with the desktop palette.

### Monterey Frost

Useful because it was still receiving fixes in 2026. It also demonstrates the risks of forcing fonts in several places. Its old theme-local `exec` commands are commented out, which aligns better with current HyDE's centralized theme switching.

## Baseline decision

For Witcher3, the first complete target structure is:

```text
Configs/
└── .config/
    └── hyde/
        └── themes/
            └── Witcher3/
                ├── hypr.theme
                ├── kitty.theme
                ├── kvantum/
                │   ├── kvantum.theme
                │   └── kvconfig.theme
                ├── rofi.theme
                ├── theme.dcol
                ├── wallpapers/
                └── waybar.theme

Source/
└── arcs/
    ├── Gtk_<final-name>.tar.*
    └── Icon_Witcher3-HyDE.tar.*
```

`wall.set` is HyDE-managed runtime state and is not part of the repository target. A `Cursor_*.tar.*` package is also intentionally outside the v1 target; current HyDE supports themes without one, and Witcher3 inherits the user's existing HyDE cursor configuration.

No `hyprlock.theme` or `animations.theme` should be created until current HyDE behavior or a concrete design requirement justifies them.
