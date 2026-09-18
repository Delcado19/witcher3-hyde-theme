# Witcher3-HyDE Icon Pilot Batch

**Purpose:** validate the visual system before large-scale artwork production.  
**Pilot size:** 14 canonical icons.  
**Release coverage represented:** all seven package contexts and all three artwork classes.

This batch is intentionally small. It should expose problems in silhouette, material treatment, small-size readability, family consistency, and package validation before the project commits to hundreds of finished SVGs.

## Pilot result — PASS — 2026-09-18

The 14-icon pilot is accepted as the visual baseline for family expansion.

Review result:

- **14 / 14** canonical pilot SVGs are present and pass `python3 tools/validate-icon-sources.py`;
- Glyphs were reviewed at 16, 22, 24, 32, and 48 px;
- Emblems were reviewed at 22, 32, 48, 64, and 128 px;
- Heroes were reviewed at 32, 48, 64, 128, 256, and 512 px;
- all three artwork classes were checked on `#0A151E`, `#171A1C`, `#1C1813`, `#262729`, and a generic light edge-case surface;
- the only systemic review issue found was weak light-surface contrast on `audio-volume-high` and `network-wireless-100`; both were corrected with restrained weathered-steel under-strokes;
- `folder` / `folder-home` share one base construction while remaining distinct;
- Dolphin, Konsole, and Kitty remain distinct by silhouette and do not establish a repeated Hero container rule;
- Witcher red remains a controlled accent rather than a default large-area fill;
- the permanent CI gate `python3 tools/build-icon-review.py --require-all` passes.

**Expansion is authorized.** Continue by coherent families, beginning with core Actions/UI around the existing pilot anchors.

## 1. Pilot set

| Order | Matrix ID | Canonical | Context | Class | Priority | Pilot purpose |
|---:|---|---|---|---|---|---|
| 1 | `W3-409` | `audio-volume-high` | Status | Glyph | P0 | establish tiny silver/steel audio glyph weight |
| 2 | `W3-398` | `network-wireless-100` | Status | Glyph | P0 | test repeated arcs and negative space at 16–24 px |
| 3 | `W3-386` | `battery-full` | Status | Glyph | P0 | test state-family container and restrained alchemy accent |
| 4 | `W3-221` | `document-new` | Actions | Glyph | P0 | test parchment semantics reduced to toolbar scale |
| 5 | `W3-228` | `edit-copy` | Actions | Glyph | P0 | test overlapping geometry and separation at 16 px |
| 6 | `W3-236` | `go-home` | Actions | Glyph | P0 | test Witcher-specific silhouette without losing standard navigation meaning |
| 7 | `W3-321` | `folder` | Places | Emblem | P0 | establish the base folder/folio family silhouette |
| 8 | `W3-322` | `folder-home` | Places | Emblem | P0 | prove that folder emblems remain distinct without rebuilding the base object |
| 9 | `W3-482` | `computer-laptop` | Devices | Emblem | P1 | establish device metal construction and screen treatment |
| 10 | `W3-543` | `application-pdf` | MimeTypes | Emblem | P1 | establish the document/MIME family and red contract seal |
| 11 | `W3-621` | `applications-system` | Categories | Emblem | P1 | establish category/preference emblem complexity |
| 12 | `W3-070` | `dolphin` | Applications | Hero | P0 | test transformation of recognizable app identity into an original Witcher object |
| 13 | `W3-082` | `konsole` | Applications | Hero | P0 | test a dark app icon where silhouette/metal separation must survive the theme background |
| 14 | `W3-083` | `kitty` | Applications | Hero | P0 | test a character/medallion concept without turning the whole app family into repeated medallions |

## 2. Exact matrix concepts

### W3-409 — `audio-volume-high`

```text
Silver horn with three waves
```

Keep the horn body simple enough that later `medium`, `low`, and `muted` variants can reuse the same core silhouette without becoming duplicate canonical designs.

### W3-398 — `network-wireless-100`

```text
Four radio arcs over tower
```

The tower and arc rhythm must remain clear at 16 px. Do not use a detailed landscape or antenna environment.

### W3-386 — `battery-full`

```text
Charged green mutagen vial battery
```

The vial is the state-family container. The green alchemy cue is allowed, but the outer shape must still read when rendered with little or no color information.

### W3-221 — `document-new`

```text
Blank parchment with a glowing plus rune
```

The plus sign is the primary action cue. Parchment construction is secondary.

### W3-228 — `edit-copy`

```text
Two overlapping contract sheets
```

The overlap must remain obvious at 16 px without thin internal text lines.

### W3-236 — `go-home`

```text
Kaer Morhen keep silhouette
```

This is the strongest Witcher-specific semantic experiment in the Glyph subset. It must still read immediately as Home rather than as a generic castle/application icon.

### W3-321 — `folder`

```text
Default black leather folio with wolf clasp
```

This establishes the common Places/Folder base geometry. The clasp should be original project artwork and must not reproduce an official Witcher medallion asset.

### W3-322 — `folder-home`

```text
Kaer Morhen home crest on folder
```

Reuse the established folder construction. The Home variation should come primarily from the emblem, not from a completely different folder silhouette.

### W3-482 — `computer-laptop`

```text
Folded travel workstation with glowing screen
```

The object should remain recognizably a laptop before the fantasy material treatment is noticed.

### W3-543 — `application-pdf`

```text
Red PDF contract seal
```

Use the document family structure and a strong red seal cue. Avoid depending on tiny `PDF` text for recognition.

### W3-621 — `applications-system`

```text
Heavy system gear with wolf rune
```

The gear is the category semantic anchor. The rune is secondary identity detail.

### W3-070 — `dolphin`

```text
Blue sea-dolphin sigil on a steel file-cabinet shield
```

The dolphin/file-management relationship must remain recognizable while avoiding a direct trace of KDE's vendor artwork.

### W3-082 — `konsole`

```text
Black rune-terminal slab with a luminous command chevron
```

This icon deliberately tests dark-on-dark separation. It needs enough steel/silver edge definition to remain readable on `w3-canvas` and `w3-surface` without a sticker outline.

### W3-083 — `kitty`

```text
Cat-school medallion with a terminal prompt etched below
```

This is allowed to use a medallion-like construction because the concept calls for it. It must not establish a rule that every Hero icon receives the same container.

## 3. Pilot source paths

Accepted artwork will enter the repository only at these paths:

```text
design/icons/src/status/audio-volume-high.svg
design/icons/src/status/network-wireless-100.svg
design/icons/src/status/battery-full.svg

design/icons/src/actions/document-new.svg
design/icons/src/actions/edit-copy.svg
design/icons/src/actions/go-home.svg

design/icons/src/places/folder.svg
design/icons/src/places/folder-home.svg

design/icons/src/devices/computer-laptop.svg

design/icons/src/mimetypes/application-pdf.svg

design/icons/src/categories/applications-system.svg

design/icons/src/apps/dolphin.svg
design/icons/src/apps/konsole.svg
design/icons/src/apps/kitty.svg
```

No alias SVGs are authored manually. The builder creates aliases as symlinks later.

## 4. Pilot review matrix

Each icon is reviewed at the sizes relevant to its class.

| Class | Mandatory pilot sizes | Primary question |
|---|---|---|
| Glyph | 16, 22, 24, 32, 48 px | Does the state/action remain obvious without decorative detail? |
| Emblem | 22, 32, 48, 64, 128 px | Does the family remain coherent while the emblem stays distinct? |
| Hero | 32, 48, 64, 128, 256, 512 px | Is app identity strong at small sizes and craftsmanship clean at large sizes? |

All 14 should additionally be checked against these project surfaces:

```text
#0A151E
#171A1C
#1C1813
#262729
```

The repository also provides a generated visual review sheet:

```text
python3 tools/build-icon-review.py
```

Open `build/icons/pilot-review.html` to inspect the current pilot sources at all mandatory class sizes on the four Witcher3 dark surfaces plus a generic light edge-case surface. For the final pilot gate, use:

```text
python3 tools/build-icon-review.py --require-all
```

## 5. Acceptance gates

The pilot is successful only if all of the following are true:

1. all 14 SVGs pass `python3 tools/validate-icon-sources.py`;
2. no icon depends on external raster/network content;
3. the three Glyph state/action prototypes remain readable at 16 px;
4. `folder` and `folder-home` visibly belong to one family without looking identical;
5. the Device, MIME, and Category emblems feel related without sharing one generic badge;
6. Dolphin, Konsole, and Kitty remain distinguishable by silhouette before decorative details are inspected;
7. Witcher red remains an accent rather than becoming the fill color of every icon;
8. no copied Witcher UI art or extracted game asset is used;
9. no vendor logo is merely pasted unchanged onto a generic Witcher background;
10. the set looks coherent on the actual HyDE dark surfaces.

## 6. Expansion decision

Do not begin broad 645-icon production merely because individual pilot icons look attractive.

First review the pilot as one set. If the set exposes a systemic problem, fix the art direction before expanding.

After the pilot passes, expand by **families**, not arbitrary individual names. Recommended early expansion order:

1. complete core Actions/UI families;
2. complete battery/network/audio and other Waybar/Status state families;
3. complete the common Folder family;
4. complete P0/P1 desktop Applications;
5. complete Devices;
6. complete MIME families;
7. complete Categories/Preferences;
8. finish lower-priority Applications and specialist coverage.

This order gives the live desktop coherent functional coverage early while preserving the 645-design final target.
