# Witcher3 Color System

**Project:** Witcher 3 HyDE Theme  
**Technical theme name:** `Witcher3`  
**Status:** Initial palette baseline  
**Reference analysis date:** 2026-09-14

This document defines the first production color system for the Witcher 3 HyDE Theme.

The palette is derived from a local reference set of 17 official CD PROJEKT RED press-kit screenshots supplied for analysis. The screenshots themselves are intentionally **not stored in this repository**. Only measured color data, normalized design tokens, and implementation guidance are committed.

The goal is not to reproduce a single screenshot. The goal is to preserve the recurring visual language shared across dark combat scenes, forests, settlements, Skellige-like cold environments, warm firelight, Blood and Wine scenery, and Witcher sign effects while keeping the desktop usable.

## Design direction

The palette should read as **The Witcher 3 first, generic dark fantasy second**.

The core visual hierarchy is:

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

Brighter world colors are deliberately subordinate:

- amber / firelight for warnings and warm emphasis
- cold cyan-blue for magical or informational states
- alchemy green for success / toxicity / potion-related states
- moss and leather browns for decorative secondary surfaces
- violet only as a rare optional semantic color, never as a base theme accent

This prevents the theme from becoming a multicolor "sign palette" or a generic RGB gaming theme.

## Reference set

The local analysis set contains 17 official press-kit screenshots:

- 7 `W3SoP_*` images
- 1 `TW3NG_DLCs_*` image
- 9 `TW3RE_*` images

The set includes dark/night combat scenes, magical effects, forest scenes, settlements, city views, open nature, warm sunset light, cold maritime scenery, and Blood and Wine environments.

The image files remain local reference material and are not tracked by Git.

## Analysis method

To avoid one large image dominating the result, every screenshot contributed an equal pixel sample.

Method used for the initial baseline:

1. Downsample each source image for analysis only.
2. Sample up to 8,000 pixels per image.
3. Combine all 17 equal-weighted samples.
4. Convert sampled RGB values to CIELAB.
5. Run an 18-cluster MiniBatch K-Means pass to find recurring global color anchors.
6. Run separate HSV-filtered analyses for red, amber, green, cyan/blue, violet/magenta, and low-saturation neutral pixels.
7. Normalize the measured anchors into a smaller UI palette.
8. Check important foreground/background pairs using WCAG relative-luminance contrast ratios.

The percentages below are approximate shares of the balanced analysis sample. They are not intended as exact full-image pixel statistics.

## Measured global anchors

These are recurring color clusters found across the complete reference set.

| Approx. share | Hex | Character | Role in the reference material |
| ---: | --- | --- | --- |
| 16.65% | `#1C1813` | warm near-black | shadow, earth, wood, leather, warm darkness |
| 11.60% | `#0A151E` | cold blue-black | night, forest shade, cold atmospheric darkness |
| 8.30% | `#122D3D` | deep slate blue | fog, water, cold ambient light |
| 7.81% | `#3D3A39` | neutral weathered steel | stone, metal, neutral mid-dark surfaces |
| 7.20% | `#3D2813` | dark umber | wood, dirt, warm environmental shadow |
| 5.80% | `#102C2E` | dark teal charcoal | forest/water shadow |
| 5.42% | `#2D5161` | muted steel blue | mist, sky reflection, cold metal |
| 4.75% | `#7D572C` | worn leather brown | wood, leather, dry vegetation |
| 4.56% | `#B0B6C2` | cool silver | steel, sky highlights, pale material |
| 4.41% | `#644741` | muted reddish brown | skin, wood, warm stone, aged material |
| 4.02% | `#787281` | ash / mauve-gray | muted atmospheric midtone |
| 3.85% | `#505A26` | moss olive | vegetation and subdued natural accents |
| 3.60% | `#632B10` | burnt brown-red | firelit surfaces and rust-like warmth |
| 3.28% | `#DEE6F0` | frost white | sky, snow-like highlights, strong light |
| 3.08% | `#628FA6` | muted sky steel | cold daylight and water |
| 2.63% | `#A28E77` | parchment taupe | stone, cloth, dry/warm neutral light |
| 1.67% | `#BB5B1D` | burnt orange | fire, sunset, hot effects |
| 1.36% | `#D7A466` | warm amber | firelight and sunlit highlights |

### What the global anchors tell us

The reference set is not dominated by pure black. Its darkness is split primarily between a **warm black-brown** and a **cold blue-black**.

That duality is important for Witcher3. A single neutral grayscale palette would lose much of the game's atmosphere.

Likewise, bright color occupies relatively little of the image area. The theme should therefore keep saturated colors as controlled accents rather than turning every component into a colored surface.

## Measured accent anchors

The following values come from color-specific analysis rather than from the global dominant-color pass.

### Red

Bright/high-saturation red pixels clustered around:

| Hex | Interpretation |
| --- | --- |
| `#801D0C` | deep ember red |
| `#7F3626` | muted rust red |
| `#C52D13` | bright sign/combat ember |

A wider red sample also contained `#AD3417`, `#621B0E`, and muted brown-red tones.

### Amber / firelight

| Hex | Interpretation |
| --- | --- |
| `#865625` | dark warm gold-brown |
| `#C25F10` | hot orange |
| `#D58E4D` | bright amber |

### Green

| Hex | Interpretation |
| --- | --- |
| `#4A6823` | moss / vegetation |
| `#106B3C` | dark alchemy green |
| `#3DB479` | bright magical / alchemical green |

### Cyan / blue

| Hex | Interpretation |
| --- | --- |
| `#1D5D6A` | dark cyan |
| `#1C496B` | cold steel blue |
| `#3188A6` | bright magical / informational cyan |

### Violet / magenta

Violet-magenta pixels account for only about **0.5%** of the balanced sample. The strongest useful anchor is approximately `#743874`, but this color is too rare to justify a permanent primary role.

Decision: violet may be used for a specific semantic state later, but it is **not part of the core Witcher3 identity palette**.

## Production UI tokens

The production palette is intentionally smaller than the measured source palette. Some tokens are exact measured anchors; others are normalized between nearby measured values for better UI consistency and contrast.

### Core surfaces

| Token | Hex | Purpose |
| --- | --- | --- |
| `w3-canvas` | `#0A151E` | primary desktop/UI background |
| `w3-surface` | `#171A1C` | primary panel/menu surface |
| `w3-surface-warm` | `#1C1813` | warm alternate surface |
| `w3-elevated` | `#262729` | elevated controls/cards/popovers |
| `w3-border` | `#3D3A39` | inactive borders and separators |

`w3-canvas` and `w3-surface-warm` preserve the cold/warm darkness split measured in the screenshots.

### Text and metal

| Token | Hex | Purpose |
| --- | --- | --- |
| `w3-text-primary` | `#DEE6F0` | primary text and high-priority icons |
| `w3-text-secondary` | `#B0B6C2` | secondary text, steel/silver iconography |
| `w3-text-muted` | `#8E8B8D` | subdued labels and metadata |
| `w3-steel` | `#3D3A39` | weathered-metal structural color |
| `w3-silver` | `#B0B6C2` | bright metallic accent |

Pure `#FFFFFF` should be avoided for normal UI text. `#DEE6F0` keeps the light end slightly cold and metallic.

### Primary active accent

| Token | Hex | Purpose |
| --- | --- | --- |
| `w3-red` | `#B72A18` | primary active/selected accent |
| `w3-red-deep` | `#621B0E` | pressed/deep red, dark gradients |

`#B72A18` is a normalized UI red derived from the measured bright red anchors around `#AD3417` and `#C52D13`.

It is intentionally darker than the brightest sampled ember red so that `w3-text-primary` remains readable when red is used as a selection background.

### Secondary semantic accents

| Token | Hex | Purpose |
| --- | --- | --- |
| `w3-amber` | `#D58E4D` | warning, firelight, warm highlight |
| `w3-cyan` | `#3188A6` | informational/magical cool state |
| `w3-alchemy` | `#3DB479` | success, alchemy, toxicity/potion state |
| `w3-moss` | `#505A26` | decorative natural accent |
| `w3-leather` | `#7D572C` | decorative warm material accent |

`w3-moss` and `w3-leather` are primarily decorative. They should not be used as normal text colors on the primary canvas.

### Optional rare accent

| Token | Hex | Purpose |
| --- | --- | --- |
| `w3-violet` | `#743874` | optional special/arcane state only |

Do not use `w3-violet` in the default Waybar/Rofi/Kitty palette unless a concrete semantic need appears.

## Contrast checks

Important contrast pairs against `w3-canvas` (`#0A151E`):

| Foreground | Ratio | Guidance |
| --- | ---: | --- |
| `w3-text-primary` `#DEE6F0` | 14.65:1 | excellent for text |
| `w3-text-secondary` `#B0B6C2` | 9.06:1 | excellent for text |
| `w3-text-muted` `#8E8B8D` | 5.47:1 | suitable for normal text |
| `w3-amber` `#D58E4D` | 6.85:1 | suitable for text/icons |
| `w3-alchemy` `#3DB479` | 7.03:1 | suitable for text/icons |
| `w3-cyan` `#3188A6` | 4.57:1 | usable for normal text; prefer icons/active states |
| `w3-red` `#B72A18` | 2.95:1 | **not for normal red text on canvas** |
| `w3-moss` `#505A26` | 2.49:1 | decorative only |
| `w3-leather` `#7D572C` | 2.87:1 | decorative only |
| `w3-violet` `#743874` | 2.25:1 | decorative/special state only |

Important selection pair:

```text
w3-text-primary #DEE6F0
on
w3-red          #B72A18
= 4.97:1
```

Therefore the primary red works well as an active/selected **background** with light foreground text, but should not be used for small red text directly on the dark canvas.

## Usage rules

### 1. Red is the primary interaction color

Use `w3-red` for:

- active workspace indicators
- selected Rofi entries
- active Hyprland border accents
- important toggles
- focused states
- limited emphasis

Do not flood entire panels with red.

### 2. Silver carries normal interface hierarchy

Most icons, labels, borders and inactive states should remain in the steel/silver family.

This keeps the red meaningful.

### 3. Warm and cold darkness may coexist

Use cold `w3-canvas` for the global background and warm `w3-surface-warm` selectively for secondary surfaces or details.

This reproduces the recurring warm/cold tension found in the reference screenshots without requiring visible gradients everywhere.

### 4. Amber, cyan and green are semantic

They should communicate state, not decorate arbitrary components.

Recommended meanings:

- amber: warning / heat / attention
- cyan: information / cold magic / special status
- green: success / alchemy / healthy-positive state

### 5. Moss and leather are material colors

Use them sparingly in illustrations, folder emblems, custom icons, separators, or decorative details.

Do not let them become competing primary UI accents.

### 6. Avoid pure white and pure black

The reference material contains rich near-black and cool pale tones rather than relying only on `#000000` and `#FFFFFF`.

The UI should preserve that character.

### 7. Avoid a literal Witcher-sign rainbow

Aard/Igni/Quen/Yrden/Axii should not automatically map to five persistent desktop colors.

The source material does not support such equal visual weight, and doing so would weaken the coherent Witcher3 identity.

## Initial component mapping

This is the intended starting point for later runtime files. It is guidance only; no runtime theme files should be created solely from this table without testing.

### Waybar

| Waybar role | Witcher3 token |
| --- | --- |
| `bar-bg` | transparent or `w3-canvas` with controlled alpha |
| `main-bg` | `w3-surface` |
| `main-fg` | `w3-text-primary` |
| `wb-act-bg` | `w3-red` |
| `wb-act-fg` | `w3-text-primary` |
| `wb-hvr-bg` | `w3-border` or `w3-elevated` |
| `wb-hvr-fg` | `w3-text-primary` |

### Rofi

| Rofi role | Witcher3 token |
| --- | --- |
| `main-bg` | `w3-canvas` with opacity |
| `main-fg` | `w3-text-primary` |
| `main-br` | `w3-silver` or `w3-border` depending on visual weight |
| `main-ex` | `w3-red` |
| `select-bg` | `w3-red` |
| `select-fg` | `w3-text-primary` |
| `separatorcolor` | transparent or `w3-border` |
| `border-color` | transparent initially |

### Hyprland

Suggested direction:

- inactive borders: `w3-border`
- active border: primarily `w3-red`, optionally paired with a restrained steel/silver endpoint
- shadows: very dark cold blue-black
- no bright rainbow gradient

### Kitty

The Kitty palette should retain conventional terminal color distinctions for usability, but its background, foreground, cursor, selection and tab colors should be built around the Witcher3 core surfaces and silver/red hierarchy.

Do not force opacity or font settings as part of the initial color implementation.

## Relationship to wallpapers and Wallbash

The final `theme.dcol` should preserve this deliberate palette instead of allowing every wallpaper to redefine the desktop identity.

Wallpapers may contain much brighter or warmer scenes, especially Blood and Wine or sunset imagery. Those scenes should enrich the desktop without changing the base UI into a yellow, orange, green or pastel theme.

The fixed UI palette therefore acts as the common visual bridge across all planned Witcher3 wallpapers.

## Asset and provenance rule

The 17 CD PROJEKT RED screenshots used to establish this palette remain outside the public repository.

This file stores only:

- measured color values
- statistical summaries
- normalized project-owned design tokens
- implementation guidance

No screenshot pixels, thumbnails, crops, extracted textures, logos, or other proprietary visual assets are committed as part of this color-system document.

## Baseline decision

The initial Witcher3 UI identity is:

```text
CANVAS        #0A151E  cold blackened iron
SURFACE       #171A1C  neutral charcoal
SURFACE WARM  #1C1813  warm shadow / leather-black
BORDER        #3D3A39  weathered steel
TEXT          #DEE6F0  frost silver
SECONDARY     #B0B6C2  cool silver
MUTED         #8E8B8D  ash
ACTIVE RED    #B72A18  Witcher active accent
DEEP RED      #621B0E  ember shadow
AMBER         #D58E4D  fire / warning
CYAN          #3188A6  cold magic / information
ALCHEMY       #3DB479  success / potion / toxicity
MOSS          #505A26  natural decorative accent
LEATHER       #7D572C  warm material accent
VIOLET        #743874  rare optional special state
```

This palette is the baseline to test first. Runtime component files should be implemented one at a time and visually validated before the palette is considered final.