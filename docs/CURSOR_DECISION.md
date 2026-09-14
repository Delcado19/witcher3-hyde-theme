# Cursor Decision

**Project:** Witcher 3 HyDE Theme  
**Decision date:** 2026-09-14  
**HyDE baseline:** `51b6cbf55b0bf982b2ea88af00a0cdbae0c787c7`

## Decision

The first Witcher3 HyDE release will **not** ship, select, or force a theme-specific cursor.

`Configs/.config/hyde/themes/Witcher3/hypr.theme` therefore intentionally does not declare:

```text
$CURSOR_THEME
$CURSOR_SIZE
```

and the first release does not include a `Cursor_*.tar.*` archive.

Witcher3 leaves cursor ownership to HyDE and the user's existing HyDE configuration instead of replacing a desktop-wide interaction setting merely for visual completeness.

## Current HyDE behavior

The decision is based on the current HyDE implementation rather than on older theme conventions.

At the pinned HyDE baseline, the default theme environment provides:

```text
CURSOR_THEME="Bibata-Modern-Ice"
CURSOR_SIZE=24
```

`theme.switch.sh` treats `$CURSOR_THEME` and `$CURSOR_SIZE` as parsed theme variables, but falls back to the already loaded HyDE values when a theme does not define them. The parsable user Hyprland state is loaded after the theme file and can override the theme values.

When a cursor theme is selected, HyDE propagates it broadly. Current code updates XDG cursor inheritance, GTK cursor settings, xsettings, Xresources/Xdefaults, and applies the cursor to the running Hyprland session through `hyprctl setcursor` in the current color/config path. A theme-specific cursor is therefore a desktop-wide behavior choice, not an isolated decorative asset.

## Archive contract

Current `theme.patch.sh` recognizes:

```text
Cursor_*.tar.* -> $CURSOR_THEME -> ~/.local/share/icons
```

but `Cursor_` is an **optional** package. Unlike the GTK package, absence of a cursor variable/archive does not invalidate a HyDE theme import.

If Witcher3 later ships a custom cursor, the archive must follow the same HyDE contract as other resources:

1. `hypr.theme` declares the exact `$CURSOR_THEME` name.
2. `Source/` contains exactly one matching `Cursor_*.tar.*` package.
3. The archive top-level directory matches `$CURSOR_THEME` exactly.
4. The cursor theme is complete enough for normal desktop use rather than containing only a themed pointer.

## Official-theme precedent

The current official `Graphite-Mono` branch in `HyDE-Project/hyde-themes` does not declare `$CURSOR_THEME` in `hypr.theme` and ships no `Cursor_` archive. Its resource set contains GTK and icon packages only.

This confirms that leaving cursor selection outside an individual theme is a supported current-HyDE configuration, not a workaround.

## Why Witcher3 v1 does not force a cursor

A cursor is continuously visible during interaction and has usability/accessibility consequences. A weak or incomplete themed cursor would reduce the quality of the complete desktop more than keeping the user's established cursor.

For v1 the project therefore avoids:

- bundling an unrelated third-party cursor merely to make the theme appear more complete;
- replacing the user's cursor without a strong Witcher-specific design benefit;
- shipping a partial cursor set with only a pointer, hand, or a few decorative states;
- adding another redistributed visual dependency and its provenance/license burden without need.

The current HyDE/Bibata default already provides a mature fallback, while users remain free to choose another cursor through their normal HyDE configuration.

## Future custom Witcher cursor

A custom cursor remains a possible post-v1 enhancement, but only as a deliberate original-artwork subproject.

Before enabling `$CURSOR_THEME`, the project should have a coherent and tested set covering normal Xcursor/desktop interaction states, including at minimum the common pointer, link, text, precision, move/drag, resize, wait/progress, prohibited, and related aliases expected by modern applications.

The set should also be tested at practical cursor sizes and across Hyprland, GTK, Qt/XWayland applications, and HiDPI scaling where applicable.

Until those requirements are met, the intentional Witcher3 cursor configuration is:

```text
Theme-owned cursor: none
Theme-owned cursor size: none
Cursor archive: none
Runtime cursor source: HyDE / user configuration
```

## Revisit trigger

Revisit this decision only when one of the following is true:

- a complete original Witcher3 cursor family has been designed and tested;
- current HyDE changes its cursor/theme resource contract;
- a concrete integration problem proves that inheriting the HyDE/user cursor is insufficient.

Do not revisit it simply because a release checklist contains an optional cursor slot.
