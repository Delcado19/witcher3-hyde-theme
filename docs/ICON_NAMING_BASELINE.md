# Witcher3 Icon Naming Baseline

**Baseline date:** 2026-09-14

This document defines how canonical icon names and aliases are validated for the Witcher 3 HyDE Theme.

The goal is not merely to make every name unique. A canonical icon name should come from a real Linux desktop namespace whenever one exists, and every non-standard extension should have a traceable reason for existing.

## Source hierarchy

Icon names are validated in the following order.

### 1. Freedesktop Icon Naming Specification

Primary source:

- https://specifications.freedesktop.org/icon-naming/latest/

The current `latest` page still identifies itself as **Icon Naming Specification 0.8.90**, but it is treated as the authoritative current Freedesktop reference for this project.

A fixed `/0.8.90/` page also exists:

- https://specifications.freedesktop.org/icon-naming/0.8.90/

The two pages are not assumed to be byte-identical. For example, the current `latest` page contains `find-location` in the Actions context while the fixed `0.8.90` page does not. Therefore the project records the baseline date in addition to the displayed specification version.

Freedesktop names have the highest priority when the intended semantic concept matches a standardized icon.

Examples:

```text
address-book-new
appointment-new
call-start
call-stop
document-open
edit-copy
media-playback-start
folder
network-server
audio-volume-high
```

The specification also defines the intended icon context. A standardized icon should not be assigned to a contradictory context merely because the same filename happens to be usable elsewhere.

For example:

```text
audio-volume-high
```

is a **Status** icon in the Freedesktop specification. It therefore belongs to the Witcher3 Status / Panel / Waybar family rather than consuming a separate Actions/UI design slot.

### 2. Freedesktop shared-mime-info

Primary sources:

- https://gitlab.freedesktop.org/xdg/shared-mime-info
- https://specifications.freedesktop.org/shared-mime-info-spec/latest/

`shared-mime-info` is the authoritative source for MIME-type identities used by the Linux desktop. It is distinct from the Icon Naming Specification: the latter defines generic semantic icon names, while `shared-mime-info` determines the specific icon name associated with a MIME type.

Unless a user override supplies an explicit icon name, the shared MIME specification derives the specific icon name from the MIME type by replacing `/` with `-`.

Examples:

```text
image/png      -> image-png
image/webp     -> image-webp
image/svg+xml  -> image-svg+xml
```

The MIME database may additionally specify a generic icon such as `image-x-generic`. A generic fallback does not replace the specific MIME-derived icon name; both serve different lookup roles.

A valid `shared-mime-info`-derived name therefore does not become a Witcher3 project extension merely because the pinned Breeze theme lacks dedicated artwork for it.

### 3. KDE Breeze icon namespace

Repository:

- https://github.com/KDE/breeze-icons

Pinned project reference:

```text
repository: KDE/breeze-icons
branch:     master
commit:     235730e69d90949621e4fee77fcc459772b7a8f0
```

Breeze is used as the primary source for widely deployed KDE/Qt icon names that extend beyond the minimal Freedesktop standard set.

A name being present in Breeze does **not** automatically make it preferable to a Freedesktop-standard or shared-mime-info-derived name. The upstream standard-derived name remains canonical when it describes the intended concept.

Breeze is particularly useful for validating:

- KDE actions not covered by the Freedesktop minimum set
- additional places and folder states
- device variants
- status and panel icons
- MIME/file-type coverage used by Dolphin and other KDE applications

### 4. Upstream application identity

Application icons are handled differently from generic semantic icons.

The Freedesktop specification explicitly permits applications to install an icon named after the executable when they do not use one of the generic desktop application names.

For branded applications, acceptable evidence includes, in order of preference:

1. the application's current upstream `.desktop` file `Icon=` value;
2. the current Flatpak application ID / exported desktop ID when that is the deployed desktop identity;
3. an upstream-documented executable/icon name used by the Linux package;
4. a well-established packaging alias when required for cross-distribution coverage.

Examples of distinct names that may all point to one canonical artwork include:

```text
firefox
firefox-bin
firefox-esr
org.mozilla.firefox
```

Aliases remain aliases. They do not create additional visual designs.

A branded application should not be renamed to an unrelated generic Freedesktop icon merely to make the name look standardized.

### 5. Current HyDE namespace

HyDE-specific names are validated against the current HyDE implementation and maintained HyDE resources rather than against historical theme repositories.

Project HyDE technical baseline:

```text
HyDE-Project/HyDE
commit: 51b6cbf55b0bf982b2ea88af00a0cdbae0c787c7
```

HyDE evidence is appropriate for names that are consumed specifically by:

- Waybar modules
- HyDE scripts
- HyDE launchers
- HyDE status indicators
- other HyDE-owned desktop integration

A HyDE-specific name should not replace an existing Freedesktop standard name when the standard name already covers the same concept.

## Canonical-name classes

Each matrix entry will eventually be classified into one of these provenance classes:

| Class | Meaning |
| --- | --- |
| `freedesktop` | Exact standardized name from the current Freedesktop Icon Naming Specification |
| `shared-mime` | Specific icon name derived from a MIME type defined by upstream shared-mime-info |
| `breeze` | Exact deployed KDE/Breeze extension not superseded by a matching Freedesktop or shared-mime-info name |
| `application` | Exact upstream application identity, desktop icon name, executable identity, or application ID |
| `hyde` | Name required by current HyDE integration |
| `project-extension` | Deliberate Witcher3 extension for a concept not covered by the sources above |

`project-extension` is a last resort, not a default bucket for unverified names.

## Alias rules

Aliases are generated or packaged separately from canonical artwork.

An alias must:

- resolve to exactly one canonical design;
- never duplicate its own canonical name;
- never collide with another canonical design;
- represent the same application or semantic concept;
- preserve case only when an upstream application identifier genuinely requires it;
- have an upstream, shared-mime-info, packaging, desktop-ID, KDE, HyDE, or compatibility reason.

Aliases are not counted toward the 645 unique-design budget.

## Context mapping

The Witcher3 matrix groups map to standard desktop contexts as follows:

| Witcher3 group | Primary external context |
| --- | --- |
| Applications | Applications plus upstream branded application identities |
| Actions/UI | Actions |
| Places/Folders | Places, with selected folder-state extensions where required |
| Status/Panel/Waybar | Status plus current HyDE/Waybar status extensions |
| Devices | Devices |
| MIME/Filetypes | MimeTypes plus specific names derived from shared-mime-info MIME identities |
| Categories/Misc | Categories plus explicitly documented misc extensions |

Some real icon themes expose the same artwork in more than one directory or through symlinks. That does not justify duplicating the design in the Witcher3 matrix. One canonical design should own the artwork and compatibility names should be aliases or generated links.

## Validation stages

Canonical-name validation is intentionally split into stages.

### Stage A — structural integrity

Already automated by:

```text
tools/validate-icon-matrix.py
tools/normalize-icon-matrix.py
.github/workflows/icon-matrix.yml
```

This stage validates:

- exactly 645 designs;
- sequential design IDs;
- fixed group counts;
- valid class and priority values;
- unique canonical names;
- non-redundant aliases;
- no alias-to-canonical namespace collisions;
- synchronized CSV and Markdown representations.

Passing Stage A does **not** prove that a name exists in Freedesktop, shared-mime-info, Breeze, an application, or HyDE.

### Stage B — Freedesktop classification

Every matrix canonical name that exactly matches a Freedesktop standard name is classified and checked against the standard context.

Context mismatches are errors unless a documented compatibility reason exists.

### Stage B-MIME — shared-mime-info classification

MIME/Filetypes entries not resolved by the generic Freedesktop Icon Naming Specification are checked against upstream `shared-mime-info`.

For a MIME type without an explicit user icon override, its specific icon name is derived by replacing `/` with `-`. This stage verifies both the MIME identity and the resulting exact icon name. A separate `generic-icon` entry is recorded as fallback evidence, not substituted for the specific name.

Names validated here receive `shared-mime` provenance even when the pinned Breeze theme does not provide dedicated artwork under that name.

### Stage C — KDE/Breeze classification

Remaining generic desktop names are checked against the pinned Breeze source tree.

The validator should record the exact Breeze path/context in which the name exists.

A basename's presence in Breeze establishes deployed KDE namespace evidence whether the path contains primary artwork or is a symlink/compatibility alias. Presence alone does **not** establish that the name is the best semantic canonical for the Witcher3 concept. Stage C must therefore distinguish namespace evidence from semantic evidence and inspect link targets or KDE usage when that distinction can change the meaning.

### Stage D — application identity validation

Branded application entries and their aliases are checked against upstream desktop files, application IDs, executable names, or maintained Linux packaging metadata.

### Stage E — HyDE and project extensions

Remaining names are validated against current HyDE or explicitly documented as Witcher3 project extensions.

No name should be considered fully validated while its provenance remains unknown.

## Current correction established by this baseline

The original matrix contained two separate design families using the same four standardized status names:

```text
audio-volume-high
audio-volume-medium
audio-volume-low
audio-volume-muted
```

The Status / Panel / Waybar designs retain those canonical names because Freedesktop defines them in the Status context.

The duplicated Actions/UI slots were reassigned to four standardized Action names that were previously missing from the matrix:

```text
W3-281  address-book-new
W3-282  appointment-new
W3-283  call-start
W3-284  call-stop
```

This preserves the 645-design budget while removing the namespace collision and increasing actual standards coverage.

## Review resolution — W3-576 encrypted MIME canonical

**Recorded:** 2026-09-17

The temporary review stop for W3-576 is cleared. The matrix retains:

```text
W3-576  encrypted
concept: Locked parchment with Quen shield
provenance class: breeze
```

The earlier review note correctly identified that basename presence alone was insufficient, but it described the Breeze link relationship too broadly. The re-review separates MIME-standard evidence from KDE theme-namespace evidence.

### MIME-standard evidence

The Freedesktop Icon Naming snapshot used by this project defines neither `application-encrypted` nor `encrypted`.

The upstream shared-mime-info specification derives a specific icon name from a MIME type by replacing `/` with `-` unless an explicit icon is supplied. The shared MIME database contains `application/pgp-encrypted`, so its specific MIME icon name is `application-pgp-encrypted`. It does not establish `encrypted` as a generic Freedesktop/shared-mime-info MIME canonical.

Therefore W3-576 is **not** classified as `freedesktop` and `encrypted` must not be presented as a shared-mime-info MIME standard name.

### KDE/Breeze namespace evidence

The pinned Breeze tree deploys an `encrypted` name in its MIME-type namespace. Breeze also contains the specific `application-pgp-encrypted` artwork. At the inspected 64 px MIME size, `encrypted.svg` is a Git symlink while `application-pgp-encrypted.svg` is primary artwork.

That symlink relationship alone would not justify choosing the broader-looking name. Separate KDE application evidence does: KDE Basket requests the theme icon name `encrypted` for a generic locked basket state rather than for a PGP MIME object. This demonstrates that `encrypted` is consumed in the KDE ecosystem with generic lock/encryption semantics.

### Decision

Retain `encrypted` for W3-576 as a KDE/Breeze namespace extension. It matches the intentionally generic Witcher3 concept better than the PGP-specific `application-pgp-encrypted`, while avoiding the unsupported project-invented name `application-encrypted`.

The Stage C exact-name audit should be interpreted as **Breeze namespace coverage**, not as automatic semantic proof. Symlink targets, upstream consumers, and MIME semantics must still be checked when a candidate name could broaden or narrow the intended concept.

Sequential MIME canonical review may continue with W3-577.
