# Witcher3 GTK Build

The Witcher3 GTK theme is built reproducibly from the pinned Colloid upstream revision documented in:

```text
design/gtk/upstream/COLLOID_SOURCE.md
```

The architectural and licensing decision is documented in:

```text
docs/GTK_BASELINE.md
```

## Build

Requirements:

- `git`
- `sassc`
- `sed`
- `grep`
- `find`
- `tar`

Build the local staging tree:

```bash
bash tools/build-gtk.sh
```

Create the HyDE archive only after the staging validation succeeds:

```bash
bash tools/build-gtk.sh --package
```

Generated local staging output is ignored by Git:

```text
build/gtk/stage/Witcher3/
```

The optional distributable archive is:

```text
Source/arcs/Gtk_Witcher3.tar.xz
```

## Runtime contract

```text
$GTK_THEME = Witcher3
```

The archive must contain exactly one top-level theme directory:

```text
Witcher3/
```

At minimum it must contain:

```text
Witcher3/
├── index.theme
├── gtk-2.0/
├── gtk-3.0/
└── gtk-4.0/
```

The build script also records the Colloid GPL-3.0 license and source provenance inside the staged theme.

## Modification strategy

The first Witcher3 derivative intentionally keeps the change set small. The palette patch modifies only the central Colloid color generation paths needed for GTK output:

```text
src/sass/_color-palette-default.scss
gtkrc.sh
assets.sh
```

Do not combine the initial palette work with a Sass toolchain migration, large widget-style rewrite, or unrelated upstream cleanup. Those changes should be evaluated separately after the first Witcher3 GTK package passes runtime validation.
