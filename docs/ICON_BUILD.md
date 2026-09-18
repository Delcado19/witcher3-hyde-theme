# Witcher3-HyDE Icon Build Contract

This document defines the packaging contract for the project-owned `Witcher3-HyDE` icon theme.

The icon matrix remains the source of truth for design coverage and naming:

- `design/icons/matrix/witcher-icon-matrix-v1.csv`
- 645 genuinely distinct canonical designs before alias expansion
- aliases never count as additional artwork

The build system must consume this matrix; it must not maintain a second handwritten list of icon names.

The final release is intentionally **hybrid**. Output format is chosen by visible rendering benefit, not by a blanket "small PNG / large SVG" or "small SVG / large PNG" rule:

- small functional artwork that gains nothing from raster detail is delivered as SVG;
- detailed artwork is delivered as size-specific PNG where the raster version visibly preserves more material, lighting, texture, or painted detail than a reduced SVG;
- one canonical may therefore have a simplified SVG for small sizes and optimized PNG variants for larger sizes;
- the SVG→PNG crossover is **not frozen yet**. It must be established by visual A/B review before the final raster size set is written into the package contract.

The current SVG-only staging implementation is a development scaffold, not the final v1 delivery format.

## 1. Runtime identity

The runtime icon theme name is:

```text
Witcher3-HyDE
```

The HyDE theme declares:

```text
$ICON_THEME = Witcher3-HyDE
```

The release archive is:

```text
Source/arcs/Icon_Witcher3-HyDE.tar.xz
```

Its only top-level theme directory must be:

```text
Witcher3-HyDE/
```

This is required by the current HyDE theme patcher, which maps `Icon_*.tar.*` archives to `$ICON_THEME`, verifies the archive's top-level directory against that value, and extracts icon archives into `~/.local/share/icons`.

## 2. Standards baseline

The package follows the freedesktop.org Icon Theme Specification and uses KDE Breeze at the pinned project reference commit as a compatibility reference for real-world KDE/Plasma usage.

Primary references:

- freedesktop.org Icon Theme Specification: `https://specifications.freedesktop.org/icon-theme/latest/`
- pinned KDE Breeze Icons reference: `235730e69d90949621e4fee77fcc459772b7a8f0`
- pinned HyDE reference: `51b6cbf55b0bf982b2ea88af00a0cdbae0c787c7`

The theme must contain a valid `index.theme`. Theme and icon names are case-sensitive.

## 3. Source artwork layout

Artwork is stored by functional matrix group, not by style class. Style class remains matrix metadata that controls design language and review requirements.

```text
design/icons/src/
  apps/
  actions/
  places/
  status/
  devices/
  mimetypes/
  categories/
```

Each canonical matrix row owns exactly one **artwork identity**, but that identity is not required to ship in only one file format.

During the current family-expansion phase, vector-delivered artwork continues to live at:

```text
design/icons/src/<context>/<canonical_name>.svg
```

Examples:

```text
design/icons/src/actions/edit-copy.svg
design/icons/src/status/audio-volume-high.svg
design/icons/src/devices/gpu.svg
design/icons/src/mimetypes/application-pdf.svg
```

Detailed raster-capable artwork may later add a high-resolution master and reviewed, size-specific PNG derivatives. The raster-master directory layout is intentionally **not frozen before the crossover pilot**; freezing it now would encode an untested output policy. The matrix remains the semantic source of truth regardless of how many delivery files a canonical ultimately emits.

The matrix group maps to the source/package context as follows:

| Matrix group | Directory | Icon-theme context |
|---|---|---|
| Applications | `apps` | `Applications` |
| Actions/UI | `actions` | `Actions` |
| Places/Folders | `places` | `Places` |
| Status/Panel/Waybar | `status` | `Status` |
| Devices | `devices` | `Devices` |
| MIME/Filetypes | `mimetypes` | `MimeTypes` |
| Categories/Misc | `categories` | `Categories` |

These are project packaging buckets. A matrix row may intentionally differ from the formal freedesktop naming-spec context; those differences are validated separately by the project's naming audits and explicit context-exception data. The package must not rename a canonical merely to make its design bucket match a specification context.

## 4. Artwork classes

The existing matrix style classes remain authoritative:

- **Hero** — detailed application artwork. Initial detailed-master target: 1024×1024 or larger.
- **Glyph** — reduced high-contrast artwork for Actions, Status, Waybar, and small UI surfaces.
- **Emblem** — medium-detail artwork for Places, Devices, MIME types, and Categories.

Style class defines **visual language and review requirements**, not a mandatory delivery format.

Hybrid delivery rules:

1. **Use SVG where raster detail has no visible advantage.** This is expected to cover Waybar/status/action Glyphs and many compact Emblems.
2. **Use PNG where detail is visibly better.** Detailed Hero artwork is expected to benefit most from raster masters and size-specific PNG exports.
3. **Allow both for one canonical.** A simplified small-size SVG may coexist with detailed PNGs for larger icon sizes.
4. **Optimize raster sizes individually.** PNG variants are not accepted as a blind resize ladder; each selected size must be reviewed and may need contrast, edge, silhouette, texture, or detail adjustments.
5. **Do not freeze the crossover by assumption.** The first PNG size is determined by visual A/B testing of the simplified SVG against the detailed raster artwork at representative desktop sizes.
6. **Do not use an SVG wrapper containing an embedded PNG as the default workaround.** That merely hides a raster image inside SVG and does not provide the size-specific art direction the hybrid system is intended to preserve.

No placeholder artwork is allowed in a release package.

## 5. Package layout

The **current validation scaffold** uses one scalable directory per functional context:

```text
Witcher3-HyDE/
  index.theme
  scalable/
    apps/
    actions/
    places/
    status/
    devices/
    mimetypes/
    categories/
```

The current builder copies canonical SVGs into the corresponding `scalable/<context>/` directory.

This is **not the frozen final hybrid layout**. The final v1 package may additionally contain fixed-size raster directories such as `<size>x<size>/<context>/` for approved PNG sizes. The exact raster size set and the SVG/PNG crossover remain pending visual review.

The current SVG-only validation `index.theme` scaffold is:

```ini
[Icon Theme]
Name=Witcher3-HyDE
Comment=Witcher 3 inspired icon theme for HyDE
Inherits=hicolor
Directories=scalable/apps,scalable/actions,scalable/places,scalable/status,scalable/devices,scalable/mimetypes,scalable/categories

[scalable/apps]
Size=48
Context=Applications
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/actions]
Size=48
Context=Actions
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/places]
Size=48
Context=Places
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/status]
Size=48
Context=Status
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/devices]
Size=48
Context=Devices
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/mimetypes]
Size=48
Context=MimeTypes
Type=Scalable
MinSize=8
MaxSize=1024

[scalable/categories]
Size=48
Context=Categories
Type=Scalable
MinSize=8
MaxSize=1024
```

`hicolor` is the only inherited theme. The Witcher3 package must not silently depend on Tela, Breeze, Papirus, or another optional third-party icon theme being installed.

## 6. Alias contract

For every matrix row:

1. `canonical_name` owns the artwork identity.
2. Every semicolon-separated entry in `aliases` becomes a relative symlink to the canonical file in every emitted delivery directory where that canonical exists.
3. Alias files never duplicate SVG or PNG data.
4. The build fails if an alias collides with another canonical or alias.
5. The build fails if an alias symlink would be dangling.
6. A canonical name must never also be emitted as its own alias.

Example:

```text
scalable/apps/tauonmb.svg
scalable/apps/com.github.taiko2k.tauonmb.svg -> tauonmb.svg
```

The existing matrix validator remains responsible for global canonical/alias namespace integrity before packaging begins.

## 7. Artwork validation

The current incremental pipeline validates SVG artwork because the already-produced Glyph/Emblem families are vector sources. The final hybrid pipeline must validate both vector and raster delivery assets.

At minimum, every emitted SVG must:

- parse as XML;
- have an `<svg>` root element;
- define a `viewBox`;
- contain non-empty vector content;
- not be a symlink to unrelated external artwork;
- not embed an external network resource.

The build may add stricter SVG checks later, but it must not silently rewrite artwork in ways that alter the visual design.

For raster-delivered canonicals, the final pipeline must additionally validate the approved master/derivative relationship, exact target dimensions, alpha handling, absence of accidental upscaling, and the expected per-size file set. Those rules will be frozen after the visual crossover pilot.

## 8. Completeness policy

The default release build is **fail-closed**:

```text
645 matrix rows
645 canonical artwork identities
0 missing required delivery assets under the approved hybrid policy
0 unexpected canonical delivery assets
0 namespace collisions
0 dangling aliases
```

A future developer-only incomplete-build option may be introduced for local layout testing, but it must never be the default and must never produce the release archive path without an explicit development marker.

The project does not generate substitute icons from text, initials, generic shapes, or another icon theme to fill missing artwork.

## 9. Reproducible archive

The release builder must stage the theme under a temporary build directory and produce:

```text
Source/arcs/Icon_Witcher3-HyDE.tar.xz
```

The archive must preserve relative alias symlinks and contain exactly one top-level directory:

```text
Witcher3-HyDE/
```

The packaging step should normalize archive metadata so identical source artwork and matrix data produce byte-for-byte reproducible output where the local GNU tar/xz toolchain permits it. At minimum this means stable path ordering, stable timestamps, numeric owner/group metadata, and no host-specific absolute paths.

Generated icon caches are not source artifacts and must not be committed into the release archive. A cache tool such as `gtk-update-icon-cache` may be used as an additional validation step against the staged directory, but any generated cache must be removed before packaging.

## 10. Build outputs versus repository sources

Repository-owned source data:

```text
design/icons/matrix/
design/icons/src/
tools/
```

Generated staging data belongs below `build/` and is disposable.

Release output belongs only at:

```text
Source/arcs/Icon_Witcher3-HyDE.tar.xz
```

The installed desktop must never depend on the repository checkout. HyDE installs the archive into the user's icon data directory and selects it through `$ICON_THEME`.

## 11. Required builder behavior

The final implementation following this contract must perform the following sequence:

1. read and validate the 645-row CSV matrix;
2. resolve each matrix group and approved delivery mode;
3. validate each canonical artwork identity and all required SVG/PNG delivery assets;
4. reject unexpected/colliding source or delivery names;
5. generate `index.theme` from a fixed project-owned template that declares both scalable and approved fixed-size directories;
6. stage SVGs only where vector delivery has passed the applicable visual/fidelity policy (Hero SVGs must satisfy `design/icons/HERO_STYLE_LOCK.md`);
7. stage reviewed size-specific PNGs where raster delivery is selected, including PNG-only Hero canonicals;
8. create matrix aliases as relative symlinks in every emitted delivery directory;
9. validate the staged icon theme and complete symlink graph;
10. optionally run an installed icon-cache validator without retaining its cache;
11. when explicitly requested, create the reproducible `.tar.xz` release archive;
12. verify that the archive contains only the `Witcher3-HyDE/` top-level directory.

The builder must validate by default and package only through an explicit packaging option.

**Implementation status:** `tools/build-icons.py` currently implements the older SVG-only staging scaffold. It remains useful for validating the existing vector artwork and aliases, but it must be revised to the approved hybrid layout before v1 release packaging. The repository must not treat the present scalable-only package graph as the final release contract.

## 12. Pilot visual review sheet

The 14-icon pilot has a repository-owned visual review helper:

```text
python3 tools/build-icon-review.py
```

It writes a disposable, self-contained HTML review page to:

```text
build/icons/pilot-review.html
```

The page embeds the existing canonical SVG sources directly and renders every pilot icon at the mandatory sizes for its artwork class on:

```text
#0A151E  w3-canvas
#171A1C  w3-surface
#1C1813  w3-surface-warm
#262729  w3-elevated
#F2F0EA  generic light edge-case
```

The command is intentionally incremental: missing pilot icons are shown as missing cards so partial batches can still be reviewed.

The final pilot gate is fail-closed:

```text
python3 tools/build-icon-review.py --require-all
```

That command must fail until all 14 pilot SVGs exist and every present SVG passes the same source-level SVG validator used by the icon builder.

The generated HTML belongs under `build/` and must not be committed as source or packaged into the icon theme.

## 13. Hero fidelity and hybrid crossover pilot — required before raster layout freeze

Before the final PNG size ladder or per-class delivery defaults are committed, Hero artwork must follow the authoritative policy in `design/icons/HERO_STYLE_LOCK.md`.

For Hero/Application canonicals, **SVG is optional**. Do not compare an intentionally different flat/cartoon vector against a detailed PNG and call the result a format crossover.

The required order is:

1. approve a production-quality high-resolution raster master;
2. attempt a visually faithful vector reconstruction only when worthwhile;
3. compare SVG vs PNG first at 256 and 512 px for subject, silhouette, composition, color hierarchy, depth, lighting and material language;
4. reject the SVG if it is visibly a different artwork or requires unacceptable style compromise;
5. allow PNG-only delivery when the fidelity gate fails;
6. only after the SVG passes fidelity, compare the approved forms at 32, 48, 64, 96, 128, 256 and 512 px;
7. judge native-size display quality and record SVG byte size/complexity;
8. encode central family rules only when repeated valid prototypes support them; otherwise use explicit per-canonical delivery metadata.

The PNG→SVG experiment may use visual segmentation, curve fitting, layered gradients/masks, restrained filters and path/structure optimization. One-click tracing and SVG files that merely embed the raster master do not count as successful Hero vector delivery.

Procedural fixtures, placeholder renderers, synthetic detail demos and visually unfaithful simplified vectors may validate tooling but **must never be treated as crossover evidence**.

Glyph / Waybar / status artwork may remain SVG at all practical sizes, and many Emblems may also remain SVG. Hero artwork must not be forced into SVG merely for consistency with those classes.

## 14. Hybrid crossover review helper

The visual crossover pilot uses:

```text
python3 tools/build-hybrid-icon-review.py
```

The helper compares an **approved, fidelity-passing SVG candidate** with a detailed raster master at the current test sizes 32, 48, 64, 96, 128, 256, and 512 px on the standard review surfaces. It must not be used to legitimize a Hero SVG that already fails the large-size fidelity gate.

It is intentionally neutral about the final threshold. When `--optimized-dir` contains `<size>.png`, that exact-size derivative replaces the master downscale for the corresponding comparison. This supports size-specific optimization without assuming which sizes will ultimately ship.

The helper writes only disposable HTML below `build/`; it does not generate artwork and does not define the release layout.
