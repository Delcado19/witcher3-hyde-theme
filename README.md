# Witcher 3 HyDE Theme

A complete **The Witcher 3-inspired desktop theme for HyDE / Hyprland**, designed as a cohesive desktop environment rather than a wallpaper-and-color preset.

The project aims to cover the full desktop experience with a consistent Witcher visual language across Hyprland, Waybar, Rofi, Kitty, Kvantum, wallpapers, cursors, GTK styling, and a dedicated icon theme.

> This is an unofficial fan project. It is not affiliated with, endorsed by, or sponsored by CD PROJEKT RED.

---

## Project Goals

Most HyDE themes focus primarily on colors, wallpapers, and a reused icon pack. This project goes further.

The target is a desktop theme that still looks intentionally Witcher-themed after leaving the launcher or wallpaper behind.

The current scope includes:

- Hyprland appearance and window styling
- Waybar colors and visual integration
- Rofi theme colors
- Kitty terminal colors
- Kvantum / Qt styling
- GTK theme integration
- Witcher-themed wallpapers
- Witcher-themed cursor package
- A dedicated Witcher icon theme
- Theme validation and build tooling

Hyprlock-specific theming, animation overrides, or other optional HyDE components are **not baseline requirements**. They should only be added when the current HyDE implementation provides a clear integration path and the component improves the Witcher3 theme without introducing brittle or obsolete configuration.

---

## Technical Baseline

The current HyDE implementation is the technical source of truth for this project. Historical theme layouts or older community conventions are used only when they still match current HyDE behavior.

Project references:

- [`docs/HYDE_REFERENCE_MATRIX.md`](docs/HYDE_REFERENCE_MATRIX.md) — current HyDE theme structure, archive conventions, and implementation decisions
- [`design/palette/witcher3-color-system.md`](design/palette/witcher3-color-system.md) — measured and normalized Witcher3 UI palette
- [`design/icons/matrix/witcher-icon-matrix-v1.md`](design/icons/matrix/witcher-icon-matrix-v1.md) — 645-design icon specification

---

## Repository Structure

The first complete HyDE target is:

```text
witcher3-hyde-theme/
│
├── README.md
├── LICENSE
│
├── Configs/
│   └── .config/
│       └── hyde/
│           └── themes/
│               └── Witcher3/
│                   ├── hypr.theme
│                   ├── kitty.theme
│                   ├── rofi.theme
│                   ├── waybar.theme
│                   ├── theme.dcol
│                   ├── wall.set
│                   ├── kvantum/
│                   │   ├── kvantum.theme
│                   │   └── kvconfig.theme
│                   └── wallpapers/
│                       └── ...
│
├── Source/
│   └── arcs/
│       ├── Gtk_<final-name>.tar.*
│       ├── Icon_Witcher3-HyDE.tar.*
│       └── Cursor_<optional-name>.tar.*
│
├── screenshots/
│   ├── overview.jpg
│   ├── desktop.jpg
│   ├── launcher.jpg
│   └── dolphin.jpg
│
├── design/
│   ├── palette/
│   │   └── witcher3-color-system.md
│   └── icons/
│       ├── matrix/
│       │   ├── witcher-icon-matrix-v1.md
│       │   └── witcher-icon-matrix-v1.csv
│       ├── sources/
│       │   ├── hero/
│       │   ├── glyph/
│       │   └── emblem/
│       └── aliases/
│
├── docs/
│   ├── ASSET_POLICY.md
│   └── HYDE_REFERENCE_MATRIX.md
│
└── tools/
    ├── build-icons.py
    ├── validate-icons.py
    ├── build-theme.sh
    └── validate-theme.sh
```

`wall.set` is shown because the finished theme should have a deterministic default wallpaper, but current HyDE can create it automatically when a valid wallpaper exists.

Optional components are intentionally absent from this baseline until their integration has been validated against current HyDE.

### Runtime vs. development files

The repository intentionally separates the installable HyDE theme from its development sources.

**Installable theme content**

```text
Configs/
Source/
```

These directories follow the structure expected by HyDE theme repositories.

**Development content**

```text
design/
docs/
tools/
screenshots/
```

These files are used to design, generate, validate, document, and package the theme, but are not required as runtime dependencies after installation.

---

## Color System

The Witcher3 UI palette is derived from an equal-weight analysis of 17 official CD PROJEKT RED press-kit screenshots used only as local reference material.

The core hierarchy is:

```text
cold blackened iron
    ↓
warm charcoal / aged leather
    ↓
weathered steel
    ↓
silver / frost
    ↓
Witcher red as the primary active accent
```

Primary production tokens include:

| Role | Hex |
| --- | --- |
| Canvas | `#0A151E` |
| Surface | `#171A1C` |
| Warm surface | `#1C1813` |
| Elevated surface | `#262729` |
| Border / steel | `#3D3A39` |
| Primary text | `#DEE6F0` |
| Secondary text / silver | `#B0B6C2` |
| Primary active red | `#B72A18` |
| Amber | `#D58E4D` |
| Cyan | `#3188A6` |
| Alchemy green | `#3DB479` |

Red is deliberately used as a controlled interaction color rather than as a large-area background. Silver and dark steel carry most normal interface hierarchy.

See [`design/palette/witcher3-color-system.md`](design/palette/witcher3-color-system.md) for the complete measured palette, contrast checks, and component mapping.

---

## Icon Theme

One of the main goals of this project is to avoid falling back to a generic third-party icon theme during normal desktop use.

The Witcher icon system is therefore being designed as a real standalone icon theme rather than a small collection of renamed files.

### Current design target

| Category | Unique designs |
|---|---:|
| Applications | 220 |
| Actions / UI | 100 |
| Places / Folders | 65 |
| Status / Panel / Waybar | 95 |
| Devices | 45 |
| MIME / Filetypes | 85 |
| Categories / Misc | 35 |
| **Total** | **645** |

Aliases do **not** count as unique designs.

Multiple icon names may point to the same canonical artwork where they represent the same application or semantic action.

Example:

```text
firefox
firefox-bin
firefox-esr
org.mozilla.firefox
```

These may resolve to one canonical Firefox design.

Different applications such as Firefox, Chromium, Brave, Thunderbird, Discord, and Steam are expected to use genuinely different artwork.

### Visual classes

The icon system is divided into three visual families:

- **Hero** — detailed application icons
- **Glyph** — reduced UI, status, action, and Waybar icons
- **Emblem** — folders, devices, MIME types, and category icons

The master artwork is created at high resolution, while very small sizes may receive simplified variants instead of being reduced mechanically.

---

## Theme Resource Packages

HyDE theme resources are stored under:

```text
Source/arcs/
```

Planned packages:

```text
Gtk_<final-name>.tar.*
Icon_Witcher3-HyDE.tar.*
Cursor_<optional-name>.tar.*
```

The GTK archive is required for a complete HyDE theme import. The final `$GTK_THEME` value in `hypr.theme` must match the top-level theme directory contained in that archive.

The icon archive is a core project deliverable even though HyDE itself can operate without one. Its top-level directory must match:

```text
$ICON_THEME = Witcher3-HyDE
```

The final icon archive should therefore contain a complete icon-theme directory similar to:

```text
Witcher3-HyDE/
├── index.theme
├── scalable/
├── 16x16/
├── 22x22/
├── 24x24/
├── 32x32/
├── 48x48/
├── 64x64/
├── 128x128/
├── 256x256/
└── ...
```

The exact size layout may change during implementation and validation.

The cursor package remains optional until a Witcher-specific cursor design is judged to improve the complete desktop experience enough to justify overriding the user's normal cursor theme.

---

## Development Workflow

The project follows a specification-first, test-before-next-change workflow.

For the HyDE runtime theme:

1. Keep the Witcher3 color system stable and documented.
2. Select or build a redistributable GTK base and determine the exact `$GTK_THEME` name.
3. Add at least one project-owned or redistributable wallpaper.
4. Implement and test a modern `hypr.theme` without legacy theme-local `exec` side effects.
5. Implement and test Waybar, Rofi, and Kitty theme files.
6. Generate or derive the Kvantum files from a known-good HyDE installation.
7. Add `theme.dcol` to keep the deliberate Witcher3 palette stable across wallpapers.
8. Set the deterministic default `wall.set` once the default wallpaper is selected.
9. Add validation/build tooling and test clean installation.

For the icon theme:

1. Define the complete icon matrix.
2. Validate canonical Linux / Freedesktop / KDE / HyDE icon names.
3. Define aliases separately from unique artwork.
4. Create and review the visual assets.
5. Test small-size readability.
6. Build the icon-theme directory.
7. Validate theme structure and aliases.
8. Package the installable archive.

Release archives should only be created after the corresponding validation steps pass.

---

## Installation

The theme is intended to be compatible with HyDE's normal theme repository workflow.

During development, installation instructions may change while the final package layout is being validated.

Until the first stable release exists, this repository should be treated as a development project rather than a finished theme package.

---

## Status

**Current phase:** palette baseline and first HyDE runtime integration.

- [x] Define the project as a full HyDE theme
- [x] Establish a current-HyDE-compatible repository baseline
- [x] Document the current HyDE reference/theme matrix
- [x] Define the initial 645-design icon budget
- [x] Define the initial Witcher3 production color system
- [x] Create and refine the initial Waybar theme
- [ ] Validate canonical icon names
- [ ] Expand alias coverage
- [ ] Select/build the GTK resource package and final `$GTK_THEME`
- [ ] Add the first redistributable wallpaper
- [ ] Create and test Hyprland theme
- [ ] Create and test Rofi theme
- [ ] Create and test Kitty theme
- [ ] Create and test Kvantum theme
- [ ] Create and validate `theme.dcol`
- [ ] Select the default wallpaper and add `wall.set`
- [ ] Decide whether a custom cursor package is justified
- [ ] Produce Witcher icon artwork
- [ ] Build `Icon_Witcher3-HyDE.tar.*`
- [ ] Add screenshots
- [ ] Add validation tooling
- [ ] Test clean installation
- [ ] Create first release

Hyprlock theming, animation overrides, and other optional components remain deferred until current HyDE behavior or a concrete design requirement justifies them.

---

## Contributing

The project is currently being developed as a controlled design system.

Before adding new icon artwork, first check whether the required concept already exists in the icon matrix or should be represented as an alias.

New artwork should preserve the established Witcher visual language and must remain readable at its intended desktop size.

Avoid:

- unnecessary duplicate artwork
- aliases disguised as new designs
- unrelated icon styles
- low-resolution source images
- assets with unclear licensing
- direct copies of commercial artwork

---

## Credits and Trademark Notice

**The Witcher**, **The Witcher 3: Wild Hunt**, related names, characters, symbols, locations, and other intellectual property belong to their respective rights holders, including CD PROJEKT S.A. where applicable.

This repository is an **unofficial, non-commercial fan-made desktop theme**.

No affiliation, endorsement, sponsorship, or official relationship with CD PROJEKT RED is claimed or implied.

Third-party assets remain subject to their original licenses and copyright terms.

See [LICENSE](LICENSE) for repository licensing details.
