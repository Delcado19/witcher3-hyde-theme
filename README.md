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
- HyDE/user cursor inheritance for v1; a complete original Witcher cursor family may be considered later
- A dedicated Witcher icon theme
- Theme validation and build tooling

Hyprlock-specific theming, animation overrides, or other optional HyDE components are **not baseline requirements**. They should only be added when the current HyDE implementation provides a clear integration path and the component improves the Witcher3 theme without introducing brittle or obsolete configuration.

---

## Technical Baseline

The current HyDE implementation is the technical source of truth for this project. Historical theme layouts or older community conventions are used only when they still match current HyDE behavior.

Project references:

- [`docs/HYDE_REFERENCE_MATRIX.md`](docs/HYDE_REFERENCE_MATRIX.md) — current HyDE theme structure, archive conventions, and implementation decisions
- [`docs/CURSOR_DECISION.md`](docs/CURSOR_DECISION.md) — v1 cursor inheritance decision and post-v1 revisit criteria
- [`docs/GTK_BASELINE.md`](docs/GTK_BASELINE.md) — selected GTK base, runtime contract, source pin, and validation requirements
- [`docs/ICON_BUILD.md`](docs/ICON_BUILD.md) — standalone icon-theme build, staging, alias, and archive contract
- [`design/palette/witcher3-color-system.md`](design/palette/witcher3-color-system.md) — measured and normalized Witcher3 UI palette
- [`design/icons/matrix/witcher-icon-matrix-v1.md`](design/icons/matrix/witcher-icon-matrix-v1.md) — 645-design icon specification
- [`design/icons/ART_DIRECTION.md`](design/icons/ART_DIRECTION.md) — Hero/Glyph/Emblem visual system and acceptance rules
- [`design/icons/PILOT_BATCH.md`](design/icons/PILOT_BATCH.md) — first 14-icon artwork validation batch
- [`design/icons/HYBRID_CROSSOVER_PILOT.md`](design/icons/HYBRID_CROSSOVER_PILOT.md) — Hero SVG↔PNG visual crossover experiment

Current integration is tested against pinned upstream states where practical instead of silently following moving targets.

---

## Repository Structure

The first complete HyDE target is:

```text
witcher3-hyde-theme/
│
├── .github/
│   └── workflows/
│       ├── gtk-build.yml
│       ├── hypr-theme.yml
│       ├── icon-build.yml
│       ├── icon-matrix.yml
│       ├── kitty-theme.yml
│       ├── kvantum-theme.yml
│       ├── rofi-theme.yml
│       ├── theme-dcol.yml
│       ├── wallpaper-theme.yml
│       └── waybar-theme.yml
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
│                   ├── kvantum/
│                   │   └── kvconfig.theme
│                   └── wallpapers/
│                       └── witcher3_kaer_morhen.png
│
├── Source/
│   └── arcs/
│       ├── Gtk_Witcher3.tar.xz
│       └── Icon_Witcher3-HyDE.tar.xz
│
├── screenshots/
│   ├── overview.jpg
│   ├── desktop.jpg
│   ├── launcher.jpg
│   └── dolphin.jpg
│
├── design/
│   ├── gtk/
│   │   ├── patches/
│   │   └── upstream/
│   ├── palette/
│   │   └── witcher3-color-system.md
│   └── icons/
│       ├── ART_DIRECTION.md
│       ├── PILOT_BATCH.md
│       ├── matrix/
│       │   ├── witcher-icon-matrix-v1.md
│       │   └── witcher-icon-matrix-v1.csv
│       ├── standards/
│       │   └── ...
│       └── src/
│           ├── apps/
│           ├── actions/
│           ├── places/
│           ├── status/
│           ├── devices/
│           ├── mimetypes/
│           └── categories/
│
├── docs/
│   ├── ASSET_POLICY.md
│   ├── CURSOR_DECISION.md
│   ├── GTK_BASELINE.md
│   ├── HYDE_REFERENCE_MATRIX.md
│   └── ICON_BUILD.md
│
└── tools/
    ├── build-gtk.sh
    ├── build-icons.py
    ├── build-icon-review.py
    ├── import-witcher-wallpaper.py
    ├── validate-icon-matrix.py
    ├── validate-icon-sources.py
    └── validate-wallpaper-theme.py
```

The Kaer Morhen default wallpaper is bundled as a validated 2560×1440 16-bit RGB PNG. With exactly one bundled wallpaper, current HyDE's fallback selection is deterministic and creates `wall.set` as runtime state when the theme is first applied; `wall.set` is intentionally not stored in the repository. The reviewed 14-icon artwork pilot is now present; broad icon coverage and screenshots remain development targets. Witcher3 v1 intentionally does not ship or force a cursor package and inherits the normal HyDE/user cursor configuration instead. Icon and wallpaper build/validation tooling is CI-tested independently of unfinished visual assets.

### Kvantum integration

Witcher3 intentionally does **not** vendor a theme-local `kvantum.theme` SVG at this stage.

Current HyDE already ships and renders its maintained Wallbash Kvantum SVG template. Witcher3 provides:

```text
Configs/.config/hyde/themes/Witcher3/theme.dcol
Configs/.config/hyde/themes/Witcher3/kvantum/kvconfig.theme
```

`theme.dcol` supplies the fixed Witcher palette. `kvconfig.theme` contains only the Witcher-specific Kvantum color and text-state overrides required for the red selection scheme. Missing Kvantum settings continue to inherit from Kvantum defaults, while HyDE supplies the current SVG structure.

This avoids carrying a large copied SVG that would otherwise need to be kept in sync with HyDE.

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
.github/
design/
docs/
tests/
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

The fixed HyDE / Wallbash mapping is stored in:

```text
Configs/.config/hyde/themes/Witcher3/theme.dcol
```

Its primary roles are:

```text
pry1 = #0A151E  canvas / background
pry2 = #171A1C  surface
pry3 = #262729  elevated surface
pry4 = #B72A18  Witcher red selection / accent
```

See [`design/palette/witcher3-color-system.md`](design/palette/witcher3-color-system.md) for the complete measured palette, contrast checks, and component mapping.

---

## GTK Theme

The GTK runtime identity is:

```text
$GTK_THEME = Witcher3
```

The selected structural base is the GPL-3.0 licensed **Colloid GTK Theme**, pinned to an explicit upstream commit and modified through a small project-owned palette patch rather than a copied source tree.

The reproducible builder is:

```text
tools/build-gtk.sh
```

The intended package is:

```text
Source/arcs/Gtk_Witcher3.tar.xz
```

with exactly one archive top-level directory:

```text
Witcher3/
```

The CI build currently validates the GTK2, GTK3, and GTK4 staging tree and the packaged archive. Live visual validation on the target HyDE desktop is still required before release.

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

The current matrix contains 645 unique canonical names and 206 validated aliases without namespace collisions. Application identity is checked against pinned Flathub, official Arch Desktop Entry, and official Arch command snapshots; remaining vendor/AUR/historical cases are recorded explicitly in the provenance review data rather than treated as guessed names.

For the 220 application designs, 193 are machine-resolved by the pinned identity snapshots and the remaining 27 have explicit validated current or historical provenance. There are currently no actionable `needs-*` application identity rows.

Different applications such as Firefox, Chromium, Brave, Thunderbird, Discord, and Steam are expected to use genuinely different artwork. Multiple runtime names may resolve to one canonical design through generated relative symlinks.

### Visual classes

The icon system is divided into three visual families:

- **Hero** — detailed application icons
- **Glyph** — reduced UI, status, action, and Waybar icons
- **Emblem** — folders, devices, MIME types, and category icons

The final release may use **hybrid SVG/PNG**, but format policy is class-sensitive. Small functional Glyph/Emblem artwork may use simplified vector delivery where that improves clarity. Hero/Application artwork is different: its approved high-detail Witcher artwork is the visual source of truth, SVG is optional, and a Hero SVG is accepted only when it remains visually faithful to the PNG identity, composition, palette, depth, lighting and material language. If a practical faithful SVG cannot be produced, PNG-only Hero delivery is explicitly allowed. There is no rule that small Hero sizes must use SVG. See [`design/icons/HERO_STYLE_LOCK.md`](design/icons/HERO_STYLE_LOCK.md).

The visual rules are defined in [`design/icons/ART_DIRECTION.md`](design/icons/ART_DIRECTION.md). The first cross-context review set is defined in [`design/icons/PILOT_BATCH.md`](design/icons/PILOT_BATCH.md). The 14-icon Hero/Glyph/Emblem pilot is complete, visually reviewed at its mandatory sizes and project surfaces, and protected by a fail-closed CI completeness gate.

The Hero pilot has reached its first production-quality raster milestone: corrected Dolphin and Kitty high-detail forged-metal treatments were visually accepted as quality anchors. The subsequent flat/simplified Dolphin SVG comparison was rejected because it did not resemble the accepted PNG closely enough in subject/silhouette, color hierarchy or material finish; that experimental SVG is no longer a valid delivery candidate.

A first PNG→SVG fidelity reconstruction tool is now tracked as `tools/reconstruct-hero-svg.py`. It uses perceptual image segmentation and true vector path reconstruction rather than a stylistic redraw. The current Dolphin fidelity prototype is compact relative to its raster master and already close at 256 px, but remains visibly faceted at 512 px; it is therefore still an experiment, not accepted Hero artwork.

The reconstruction tool also includes an experimental edge-aware smoothing pass, but Dolphin review preferred the sharper original facet geometry: smoothing lost too much material detail. For the current Dolphin candidate, the project owner selected the `punchy` Lab-space brilliance preset and accepted the residual faceted/mosaic character as an intentional vector-specific style. That decision is Dolphin-specific until other Hero reconstructions are reviewed.

Dolphin and Kitty have now been regenerated after a light-background alpha defect was found in the faceted reconstruction pipeline. The reconstructor uses a dark source-alpha-derived vector underpainting beneath the facets, and Kitty's working master alpha was corrected after near-black background removal had accidentally erased interior forged regions. Earlier per-size crossover conclusions are superseded until the corrected seven-size/five-surface sheets receive a fresh visual review.

Hero development is now PNG-fidelity-first. The next experiment is a visually guided PNG→SVG reconstruction/optimization pipeline. Only a vector result that still looks like the same Hero artwork may proceed to crossover testing; otherwise PNG-only is the correct result. The earlier folder/file-cabinet Dolphin composition remains retired as final identity. Reference binaries are not committed automatically without provenance/redistribution clearance.

### Build contract

The standalone icon builder is:

```text
python3 tools/build-icons.py
```

Normal invocation validates and stages only. Release packaging is explicit:

```text
python3 tools/build-icons.py --package
```

The current builder remains fail-closed for the existing SVG source tree, but its scalable-only package graph is a development scaffold. Before the real v1 archive is produced, the builder must be upgraded to the approved hybrid layout and validate all required SVG/PNG delivery assets for 645 canonical artwork identities.

Artwork may still be added incrementally. Existing source SVGs are checked with:

```text
python3 tools/validate-icon-sources.py
```

The incremental validator accepts an incomplete artwork set during development but applies the final SVG/path rules to every file that already exists. At 645/645 it automatically exercises the strict staging path.

The builder itself is already CI-tested using a synthetic 645-SVG fixture, including alias-symlink validation and byte-reproducible archive generation. No synthetic fixture artwork is committed to the project or shipped as release content.

---

## Theme Resource Packages

HyDE theme resources are stored under:

```text
Source/arcs/
```

Planned v1 packages:

```text
Gtk_Witcher3.tar.xz
Icon_Witcher3-HyDE.tar.xz
```

The GTK archive is required for a complete HyDE theme import. The `$GTK_THEME` value in `hypr.theme` must match the top-level `Witcher3/` directory contained in that archive.

The icon archive is a core project deliverable even though HyDE itself can operate without one. Its top-level directory must match:

```text
$ICON_THEME = Witcher3-HyDE
```

The current SVG validation scaffold stages:

```text
Witcher3-HyDE/
├── index.theme
└── scalable/
    ├── apps/
    ├── actions/
    ├── places/
    ├── status/
    ├── devices/
    ├── mimetypes/
    └── categories/
```

The final v1 archive will retain scalable directories where SVG is the approved delivery mode and add fixed-size raster directories for PNG sizes that pass the crossover review. The exact raster ladder is intentionally not frozen yet. `index.theme` inherits only `hicolor`; aliases remain relative symlinks to the canonical asset in each emitted directory rather than duplicate artwork.

See [`docs/ICON_BUILD.md`](docs/ICON_BUILD.md) for the complete archive and validation contract.

Witcher3 v1 intentionally ships no cursor package and does not declare `$CURSOR_THEME` or `$CURSOR_SIZE`. Cursor selection remains owned by the user's HyDE configuration. A complete original Witcher cursor family may be reconsidered after v1; see [`docs/CURSOR_DECISION.md`](docs/CURSOR_DECISION.md).

---

## Validation

Runtime components are validated independently so one broken integration does not hide behind a broad theme-level test.

Current CI coverage includes:

| Component | Validation |
| --- | --- |
| GTK | Reproducible pinned-source build, staging checks, archive layout |
| Hyprland | Current HyDE `hyq` parser path and Lua export |
| Waybar | HyDE target line, required color roles, expected Witcher values |
| Rofi | HyDE target line, required roles, Rasi syntax validation |
| Kitty | Official pinned Kitty binary and Kitty's internal config parser |
| `theme.dcol` | Shell syntax, complete variable matrix, Hex/RGBA consistency |
| Kvantum | Rendered Kvconfig, pinned HyDE SVG, XML validity, color roles, selection contrast |
| Wallpaper | Strict 2560×1440 16-bit RGB PNG structure/data validation, exact approved filename, single-wallpaper baseline, and repository-level `wall.set` rejection |
| Icon matrix | 645-design structure, canonical/alias namespace, Freedesktop/Breeze naming and application identity provenance |
| Icon builder | Incremental source validation, permanent 14-icon pilot completeness review gate, plus synthetic 645-SVG staging, symlink, archive, and reproducibility tests |

Static CI validation does **not** replace final visual testing on a real HyDE installation.

---

## Development Workflow

The project follows a specification-first, test-before-next-change workflow.

For the HyDE runtime theme:

1. Keep the Witcher3 color system stable and documented.
2. Build the redistributable GTK package and keep the exact `$GTK_THEME` contract stable.
3. Implement and statically validate Hyprland, Waybar, Rofi, and Kitty integrations.
4. Define `theme.dcol` as the fixed Wallbash palette.
5. Add the minimal Kvantum override while reusing current HyDE's maintained Wallbash SVG template.
6. Bundle and validate at least one permitted redistributable wallpaper. **Done.** Current HyDE creates `wall.set` as runtime state when the theme is applied.
7. Produce and package the dedicated icon artwork through the validated builder.
8. Keep cursor ownership with HyDE/user configuration for v1. **Done.** Revisit only for a complete original Witcher cursor family.
9. Test the complete theme on a clean/current HyDE installation before release.

For the icon theme:

1. Define and structurally validate the complete 645-design matrix. **Done.**
2. Validate canonical Linux / Freedesktop / KDE names and application identities. **Done.**
3. Validate aliases separately from unique artwork. **Done for the current matrix baseline.**
4. Freeze the semantic build contract. **Done.** Hybrid SVG/PNG delivery is now the target; the exact crossover and final raster size ladder remain pending visual A/B review.
5. Define Hero/Glyph/Emblem art direction and the first cross-context pilot. **Done.**
6. Produce and review the 14-icon pilot artwork. **Done.**
7. Expand accepted artwork family-by-family while incremental CI validates each batch. **In progress: `main` now has 428/645 canonical artwork sources. Actions/UI, Places/Folders, Status/Panel/Waybar, Devices, MIME/Filetypes, and Categories/Misc are complete; Applications/Hero is the only incomplete group.**
8. Reach 645/645 canonical artwork identities, validate the hybrid delivery policy, and run the strict full staging path. **Pending remaining artwork and hybrid-builder upgrade.**
9. Package `Source/arcs/Icon_Witcher3-HyDE.tar.xz`. **Pending complete artwork.**

Release archives should only be created after the corresponding validation steps pass.

---

## Installation

The theme is intended to be compatible with HyDE's normal theme repository workflow.

During development, installation instructions may change while the final package layout is being validated.

Until the first stable release exists, this repository should be treated as a development project rather than a finished theme package.

---

## Status

**Current phase:** runtime styling and icon infrastructure are validated. Icon artwork expansion is well underway: Actions/UI is 100/100, Places/Folders is 65/65, Status/Panel/Waybar is 95/95, and Devices is 45/45, all merged to `main`. `main` contains 428/645 canonical artwork sources. Categories/Misc is complete at 35/35; Applications has 3/220 accepted pilot icons and is the only remaining incomplete group. The final icon delivery is hybrid SVG/PNG; the visual crossover size and final raster ladder remain intentionally pending visual A/B review.

- [x] Define the project as a full HyDE theme
- [x] Establish a current-HyDE-compatible repository baseline
- [x] Document the current HyDE reference/theme matrix
- [x] Define the 645-design icon budget and matrix
- [x] Define the Witcher3 production color system
- [x] Select and pin the Colloid GTK structural base
- [x] Build and CI-validate the initial `Gtk_Witcher3.tar.xz` package
- [x] Create and validate the Hyprland theme
- [x] Create and validate the Waybar theme
- [x] Create and validate the Rofi theme
- [x] Create and validate the Kitty theme
- [x] Create and validate the fixed `theme.dcol` palette
- [x] Create and validate the Kvantum / Qt color integration
- [x] Add component-level validation workflows
- [x] Validate icon canonical names and application identities
- [x] Establish and validate the current icon alias namespace
- [x] Define the standalone icon build/archive contract
- [x] Implement and CI-validate the strict icon builder
- [x] Add incremental SVG artwork validation
- [x] Define icon art direction and the 14-icon pilot batch
- [x] Add and CI-validate the Kaer Morhen default wallpaper
- [x] Document `wall.set` as HyDE-managed runtime state rather than a repository asset
- [x] Decide v1 cursor policy: inherit HyDE/user cursor; no cursor package
- [x] Produce and review the 14-icon Witcher artwork pilot
- [ ] Expand original icon artwork to 645/645 canonicals
- [ ] Build the real `Icon_Witcher3-HyDE.tar.xz` from accepted artwork
- [ ] Add screenshots
- [ ] Perform live visual validation of GTK3 / GTK4 / Qt / Rofi / Waybar / Kitty
- [ ] Test clean HyDE theme import and switching
- [ ] Create first release

Hyprlock theming, animation overrides, a custom Witcher cursor family, and other optional components remain deferred until current HyDE behavior or a concrete design requirement justifies them.

---

## Contributing

The project is currently being developed as a controlled design system.

Before adding new icon artwork, first check whether the required concept already exists in the icon matrix or should be represented as an alias.

New artwork should preserve [`design/icons/ART_DIRECTION.md`](design/icons/ART_DIRECTION.md), remain readable at its intended desktop size, and pass the incremental icon source validator before the next artwork batch begins.

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