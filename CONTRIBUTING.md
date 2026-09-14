# Contributing

Thanks for helping improve the Witcher 3 HyDE Theme.

This repository is built as a complete HyDE theme rather than a loose collection of wallpapers and icons. Changes should therefore preserve compatibility with the HyDE theme layout and the project's visual system.

## Repository Areas

### Installable HyDE content

```text
Configs/
Source/
```

Files in these directories are part of the theme delivered to HyDE users.

### Development sources

```text
design/
tools/
screenshots/
```

These directories contain source artwork, specifications, build tooling, validation tools, and project documentation.

## General Rules

1. Keep each change focused.
2. Do not replace working assets or configuration without a clear reason.
3. Preserve HyDE-compatible paths and resource naming.
4. Do not commit generated build directories.
5. Do not commit secrets, tokens, local machine configuration, or personal paths.
6. Do not add assets whose origin or redistribution status is unknown.
7. Do not copy commercial Witcher artwork directly into newly created project artwork.

## Icon Contributions

The icon project is specification-first.

Before adding artwork:

1. Check `design/icons/matrix/`.
2. Determine whether the requested icon needs a genuinely new visual design.
3. If an existing canonical design already represents the same application or semantic action, add an alias instead.
4. Keep aliases separate from the unique-design count.

One matrix row is intended to represent one genuine visual design.

### Visual families

- **Hero** — detailed application artwork.
- **Glyph** — small, high-contrast UI, action, status, and Waybar symbols.
- **Emblem** — folders, devices, MIME types, and categories.

Small UI icons must remain readable at their real target size. A high-resolution master is not sufficient if the result becomes visually unclear at 16, 22, or 24 px.

## Asset Provenance

Every externally sourced asset must be recorded in `THIRD_PARTY_NOTICES.md` before it is included in a release.

Record at least:

- asset name
- author / project
- source
- license
- local path
- modifications made

If the license or redistribution permission cannot be determined, do not bundle the asset.

## Theme Packages

HyDE resource archives belong under:

```text
Source/arcs/
```

Expected naming follows HyDE's resource-prefix convention, for example:

```text
Gtk_Witcher3.tar.gz
Icon_Witcher3-HyDE.tar.gz
Cursor_Witcher3.tar.gz
```

Do not add these archive extensions to `.gitignore`.

## Formatting

The repository uses `.editorconfig` and `.gitattributes`.

Unix-facing configuration and scripts use LF line endings. PowerShell files use CRLF.

## Validation

Before a release, verify at minimum:

- expected HyDE theme files exist
- resource archive names match the names selected in `hypr.theme`
- archives contain the expected top-level theme directory
- icon aliases resolve to valid canonical icons
- `index.theme` references existing icon directories
- no unexpected fallback icon theme appears during normal desktop use
- wallpapers and bundled third-party assets are documented
- a clean installation works without depending on the repository working directory

## Licensing

Code, configuration, tooling, documentation, original artwork, Witcher-related intellectual property, and third-party resources are not necessarily governed by the same license terms.

Read `LICENSE` and `THIRD_PARTY_NOTICES.md` before redistributing project material.
