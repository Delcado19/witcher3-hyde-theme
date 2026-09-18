# Witcher3-HyDE Icon Build Contract

This document defines the packaging contract for the project-owned `Witcher3-HyDE` icon theme.

The icon matrix remains the source of truth for design coverage and naming:

- `design/icons/matrix/witcher-icon-matrix-v1.csv`
- 645 genuinely distinct canonical designs before alias expansion
- aliases never count as additional artwork

The build system must consume this matrix; it must not maintain a second handwritten list of icon names.

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

Each canonical matrix row owns exactly one project source SVG:

```text
design/icons/src/<context>/<canonical_name>.svg
```

Examples:

```text
design/icons/src/apps/firefox.svg
design/icons/src/actions/edit-copy.svg
design/icons/src/status/audio-volume-high.svg
design/icons/src/mimetypes/application-pdf.svg
```

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

- **Hero** — detailed application artwork. Design master canvas: 1024×1024.
- **Glyph** — reduced high-contrast artwork for Actions, Status, Waybar, and small UI surfaces.
- **Emblem** — medium-detail artwork for Places, Devices, MIME types, and Categories.

All release artwork is true vector SVG. The build must not rasterize the canonical artwork into a large set of generated PNG sizes.

No placeholder artwork is allowed in a release package.

## 5. Package layout

The first complete release uses one scalable directory per functional context:

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

The build copies canonical SVGs into the corresponding `scalable/<context>/` directory.

The initial `index.theme` contract is:

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

1. `canonical_name` owns the SVG artwork.
2. Every semicolon-separated entry in `aliases` becomes a relative symlink in the same package directory.
3. Alias files never duplicate SVG data.
4. The build fails if an alias collides with another canonical or alias.
5. The build fails if an alias symlink would be dangling.
6. A canonical name must never also be emitted as its own alias.

Example:

```text
scalable/apps/tauonmb.svg
scalable/apps/com.github.taiko2k.tauonmb.svg -> tauonmb.svg
```

The existing matrix validator remains responsible for global canonical/alias namespace integrity before packaging begins.

## 7. SVG validation

A release build must fail if any of the 645 canonical source SVGs is missing or invalid.

At minimum, every canonical SVG must:

- parse as XML;
- have an `<svg>` root element;
- define a `viewBox`;
- contain non-empty vector content;
- not be a symlink to unrelated external artwork;
- not embed an external network resource.

The build may add stricter SVG checks later, but it must not silently rewrite artwork in ways that alter the visual design.

## 8. Completeness policy

The default release build is **fail-closed**:

```text
645 matrix rows
645 canonical source SVGs
0 missing canonical SVGs
0 unexpected canonical SVGs
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

The implementation following this contract must perform the following sequence:

1. read and validate the 645-row CSV matrix;
2. resolve each matrix group to its package directory;
3. validate all 645 canonical source SVGs;
4. reject unexpected/colliding source names;
5. generate `index.theme` from a fixed template owned by the project;
6. copy canonical SVGs into staging;
7. create matrix aliases as relative symlinks;
8. validate the staged icon theme and symlink graph;
9. optionally run an installed icon-cache validator without retaining its cache;
10. when explicitly requested, create the reproducible `.tar.xz` release archive;
11. verify that the archive contains only the `Witcher3-HyDE/` top-level directory.

The builder must validate by default and package only through an explicit packaging option. This mirrors the project's GTK build policy and prevents accidental release artifacts during normal development checks.

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
