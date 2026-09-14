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
- Hyprlock theming
- Optional animation overrides
- Witcher-themed wallpapers
- Witcher-themed cursor package
- A dedicated Witcher icon theme
- Theme validation and build tooling

---

## Repository Structure

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
│                   ├── hyprlock.theme
│                   ├── animations.theme
│                   ├── wall.set
│                   ├── kvantum/
│                   │   ├── kvantum.theme
│                   │   └── kvconfig.theme
│                   ├── logo/
│                   │   └── witcher3.png
│                   └── wallpapers/
│                       ├── witcher-01.jpg
│                       ├── witcher-02.jpg
│                       └── ...
│
├── Source/
│   └── arcs/
│       ├── Gtk_Witcher3.tar.gz
│       ├── Icon_Witcher3-HyDE.tar.gz
│       └── Cursor_Witcher3.tar.gz
│
├── screenshots/
│   ├── overview.jpg
│   ├── desktop.jpg
│   ├── launcher.jpg
│   └── dolphin.jpg
│
├── design/
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
└── tools/
    ├── build-icons.py
    ├── validate-icons.py
    ├── build-theme.sh
    └── validate-theme.sh
```

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
tools/
screenshots/
```

These files are used to design, generate, validate, document, and package the theme, but are not required as runtime dependencies after installation.

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
Gtk_Witcher3.tar.gz
Icon_Witcher3-HyDE.tar.gz
Cursor_Witcher3.tar.gz
```

The icon archive is expected to contain a complete icon-theme directory whose name matches the icon theme selected in `hypr.theme`.

Example:

```text
$ICON_THEME = Witcher3-HyDE
```

The final archive should therefore contain a top-level directory similar to:

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

---

## Development Workflow

The project follows a specification-first workflow.

1. Define the complete icon matrix.
2. Validate canonical Linux / Freedesktop / KDE / HyDE icon names.
3. Define aliases separately from unique artwork.
4. Create and review the visual assets.
5. Test small-size readability.
6. Build the icon-theme directory.
7. Validate theme structure and aliases.
8. Package the installable archives.
9. Test the complete theme in HyDE.
10. Create release archives only after validation succeeds.

The project deliberately avoids inflating icon counts by duplicating a small number of images under hundreds of filenames.

---

## Installation

The theme is intended to be compatible with HyDE's normal theme repository workflow.

During development, installation instructions may change while the final package layout is being validated.

Until the first stable release exists, this repository should be treated as a development project rather than a finished theme package.

---

## Status

**Current phase:** theme structure and icon specification.

- [x] Define the project as a full HyDE theme
- [x] Establish a HyDE-compatible repository layout
- [x] Define the initial 645-design icon budget
- [ ] Validate canonical icon names
- [ ] Expand alias coverage
- [ ] Finalize the Witcher color system
- [ ] Create Hyprland theme
- [ ] Create Waybar theme
- [ ] Create Rofi theme
- [ ] Create Kitty theme
- [ ] Create Kvantum theme
- [ ] Create Hyprlock theme
- [ ] Build GTK resource package
- [ ] Build cursor resource package
- [ ] Produce Witcher icon artwork
- [ ] Build `Icon_Witcher3-HyDE.tar.gz`
- [ ] Add wallpapers
- [ ] Add screenshots
- [ ] Add validation tooling
- [ ] Test clean installation
- [ ] Create first release

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
