# Colloid GTK Upstream Source

**Witcher3 GTK structural base:** `vinceliuice/Colloid-gtk-theme`  
**Pinned upstream commit:** `fe11342f37f124f1b29d44cf33e9a06053f4bba2`  
**Upstream commit date:** 2026-08-22  
**Pinned by Witcher3 project:** 2026-09-14

## Source

Repository:

```text
https://github.com/vinceliuice/Colloid-gtk-theme
```

Pinned revision:

```text
https://github.com/vinceliuice/Colloid-gtk-theme/commit/fe11342f37f124f1b29d44cf33e9a06053f4bba2
```

Clone/reproduce the exact upstream state with:

```bash
git clone https://github.com/vinceliuice/Colloid-gtk-theme.git
cd Colloid-gtk-theme
git checkout fe11342f37f124f1b29d44cf33e9a06053f4bba2
```

Do not build Witcher3 directly from an unpinned moving `main` branch.

## License

Colloid GTK Theme is distributed under:

```text
GNU General Public License v3.0
```

Upstream license file:

```text
https://github.com/vinceliuice/Colloid-gtk-theme/blob/fe11342f37f124f1b29d44cf33e9a06053f4bba2/LICENSE
```

The Witcher3 GTK derivative must preserve the applicable GPL-3.0 terms and attribution. The generated GTK package must not be presented as MIT-licensed merely because the surrounding Witcher3 repository uses MIT for its original code and documentation.

## Relationship to Witcher3

Colloid is used as a **structural GTK source base**, not as the final runtime identity.

The intended Witcher3 runtime contract is:

```text
GTK theme name: Witcher3
HyDE variable:  $GTK_THEME = Witcher3
Archive:        Source/arcs/Gtk_Witcher3.tar.xz
Top directory:  Witcher3/
```

The Witcher3 derivative will replace the stock Colloid color identity with the palette defined in:

```text
design/palette/witcher3-color-system.md
```

The architectural and licensing decision is documented in:

```text
docs/GTK_BASELINE.md
```

## Upstream build characteristics at the pinned revision

The pinned Colloid source provides GTK 2, GTK 3 and GTK 4 theme generation and uses the upstream SassC/LibSass build path.

Witcher3 should initially preserve that upstream build mechanism so that the first change is limited to creating and validating the Witcher3 visual derivative. A SassC-to-Dart-Sass migration, if required later, must be handled as a separate change with output comparison.

The upstream `--libadwaita` installation option is **not** part of the Witcher3 runtime mechanism. Current HyDE itself switches GTK4 by linking the active theme's `gtk-4.0/` directory.

## Update policy

This pin is intentionally stable.

Do not advance it merely because upstream `main` receives a new commit. Before changing the pin:

1. review upstream changes since this revision;
2. identify GTK2/GTK3/GTK4, asset or build-system changes relevant to Witcher3;
3. build the Witcher3 derivative against the candidate revision;
4. compare visual output and GTK warnings;
5. test the candidate through HyDE theme switching;
6. update this file and the corresponding third-party notice in the same planned upstream-update change.

The selected source revision should remain unchanged while the initial Witcher3 GTK recolor and packaging path are being established.
