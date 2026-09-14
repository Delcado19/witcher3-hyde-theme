#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"

UPSTREAM_URL="https://github.com/vinceliuice/Colloid-gtk-theme.git"
UPSTREAM_COMMIT="fe11342f37f124f1b29d44cf33e9a06053f4bba2"
PATCH_FILE="${PROJECT_ROOT}/design/gtk/patches/0001-witcher3-palette.patch"

BUILD_ROOT="${PROJECT_ROOT}/build/gtk"
SOURCE_DIR="${BUILD_ROOT}/colloid-src"
RAW_DIR="${BUILD_ROOT}/raw"
STAGE_ROOT="${BUILD_ROOT}/stage"
THEME_DIR="${STAGE_ROOT}/Witcher3"
ARCHIVE_DIR="${PROJECT_ROOT}/Source/arcs"
ARCHIVE_PATH="${ARCHIVE_DIR}/Gtk_Witcher3.tar.xz"

PACKAGE=0

usage() {
  cat <<'USAGE'
Usage: tools/build-gtk.sh [--package]

Build the Witcher3 GTK theme from the pinned Colloid upstream revision.

Options:
  --package   Also create Source/arcs/Gtk_Witcher3.tar.xz after validation.
  -h, --help  Show this help.

The default build only creates the ignored local staging directory:
  build/gtk/stage/Witcher3/
USAGE
}

while (($#)); do
  case "$1" in
    --package)
      PACKAGE=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'error: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

require_command() {
  local command_name="$1"
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'error: required command not found: %s\n' "$command_name" >&2
    exit 1
  fi
}

for command_name in git sassc sed grep find tar; do
  require_command "$command_name"
done

if [[ ! -f "$PATCH_FILE" ]]; then
  printf 'error: palette patch not found: %s\n' "$PATCH_FILE" >&2
  exit 1
fi

printf '==> Cleaning local GTK build directory\n'
rm -rf "$BUILD_ROOT"
mkdir -p "$BUILD_ROOT" "$RAW_DIR" "$STAGE_ROOT"

printf '==> Cloning pinned Colloid source\n'
git clone --quiet "$UPSTREAM_URL" "$SOURCE_DIR"
git -C "$SOURCE_DIR" checkout --quiet --detach "$UPSTREAM_COMMIT"

actual_commit="$(git -C "$SOURCE_DIR" rev-parse HEAD)"
if [[ "$actual_commit" != "$UPSTREAM_COMMIT" ]]; then
  printf 'error: checked-out Colloid commit mismatch\n' >&2
  printf 'expected: %s\n' "$UPSTREAM_COMMIT" >&2
  printf 'actual:   %s\n' "$actual_commit" >&2
  exit 1
fi

printf '==> Verifying and applying Witcher3 palette patch\n'
git -C "$SOURCE_DIR" apply --check "$PATCH_FILE"
git -C "$SOURCE_DIR" apply "$PATCH_FILE"

printf '==> Building upstream dark theme\n'
(
  cd "$SOURCE_DIR"
  ./install.sh -n Witcher3 -c dark -d "$RAW_DIR"
)

GENERATED_DIR="${RAW_DIR}/Witcher3-Dark"
if [[ ! -d "$GENERATED_DIR" ]]; then
  printf 'error: expected generated theme not found: %s\n' "$GENERATED_DIR" >&2
  exit 1
fi

printf '==> Normalizing runtime theme to Witcher3\n'
mv "$GENERATED_DIR" "$THEME_DIR"
rm -rf \
  "${RAW_DIR}/Witcher3-Dark-hdpi" \
  "${RAW_DIR}/Witcher3-Dark-xhdpi"

# HyDE only needs the GTK runtime directories from this derivative.
rm -rf \
  "${THEME_DIR}/gnome-shell" \
  "${THEME_DIR}/cinnamon" \
  "${THEME_DIR}/metacity-1" \
  "${THEME_DIR}/xfwm4" \
  "${THEME_DIR}/labwc" \
  "${THEME_DIR}/plank"

cat > "${THEME_DIR}/index.theme" <<'INDEX'
[Desktop Entry]
Type=X-GNOME-Metatheme
Name=Witcher3
Comment=Witcher3 GTK theme for the Witcher 3 HyDE Theme
Encoding=UTF-8

[X-GNOME-Metatheme]
GtkTheme=Witcher3
IconTheme=Witcher3-HyDE
ButtonLayout=close,minimize,maximize:menu
INDEX

cp "${SOURCE_DIR}/LICENSE" "${THEME_DIR}/LICENSE.Colloid-GPL-3.0"

cat > "${THEME_DIR}/WITCHER3-GTK-SOURCE.txt" <<SOURCE
Witcher3 GTK Theme

Structural upstream: vinceliuice/Colloid-gtk-theme
Upstream URL: ${UPSTREAM_URL}
Pinned commit: ${UPSTREAM_COMMIT}
Witcher3 patch: design/gtk/patches/0001-witcher3-palette.patch
License: GNU GPL v3.0 for the Colloid-derived GTK work

Project documentation:
- docs/GTK_BASELINE.md
- design/gtk/upstream/COLLOID_SOURCE.md
SOURCE

printf '==> Validating staged GTK theme\n'
for required_path in \
  "${THEME_DIR}/index.theme" \
  "${THEME_DIR}/gtk-2.0" \
  "${THEME_DIR}/gtk-3.0" \
  "${THEME_DIR}/gtk-4.0" \
  "${THEME_DIR}/LICENSE.Colloid-GPL-3.0" \
  "${THEME_DIR}/WITCHER3-GTK-SOURCE.txt"; do
  if [[ ! -e "$required_path" ]]; then
    printf 'error: required staged path missing: %s\n' "$required_path" >&2
    exit 1
  fi
done

if ! grep -q '^Name=Witcher3$' "${THEME_DIR}/index.theme"; then
  printf 'error: index.theme does not declare Name=Witcher3\n' >&2
  exit 1
fi

if ! grep -q '^GtkTheme=Witcher3$' "${THEME_DIR}/index.theme"; then
  printf 'error: index.theme does not declare GtkTheme=Witcher3\n' >&2
  exit 1
fi

if ! grep -q '^IconTheme=Witcher3-HyDE$' "${THEME_DIR}/index.theme"; then
  printf 'error: index.theme does not declare IconTheme=Witcher3-HyDE\n' >&2
  exit 1
fi

if ! grep -Rqi '#B72A18' "${THEME_DIR}/gtk-2.0" "${THEME_DIR}/gtk-3.0" "${THEME_DIR}/gtk-4.0"; then
  printf 'error: Witcher3 primary red was not found in generated GTK output\n' >&2
  exit 1
fi

if grep -RqiE '#(5b9bf8|3c84f7)' "${THEME_DIR}/gtk-2.0" "${THEME_DIR}/gtk-3.0" "${THEME_DIR}/gtk-4.0"; then
  printf 'error: stock Colloid blue remains in generated GTK output\n' >&2
  exit 1
fi

broken_links="$(find "$THEME_DIR" -xtype l -print)"
if [[ -n "$broken_links" ]]; then
  printf 'error: broken symlinks found in staged GTK theme:\n%s\n' "$broken_links" >&2
  exit 1
fi

printf '==> GTK staging validation passed\n'
printf 'stage: %s\n' "$THEME_DIR"

if ((PACKAGE)); then
  printf '==> Packaging reproducible HyDE GTK archive\n'
  mkdir -p "$ARCHIVE_DIR"
  rm -f "$ARCHIVE_PATH"
  tar \
    --sort=name \
    --mtime='@0' \
    --owner=0 \
    --group=0 \
    --numeric-owner \
    -C "$STAGE_ROOT" \
    -cJf "$ARCHIVE_PATH" \
    Witcher3

  top_entries="$(tar -tJf "$ARCHIVE_PATH" | sed 's#^\./##' | cut -d/ -f1 | sort -u)"
  if [[ "$top_entries" != 'Witcher3' ]]; then
    printf 'error: archive contains unexpected top-level entries:\n%s\n' "$top_entries" >&2
    exit 1
  fi

  printf 'archive: %s\n' "$ARCHIVE_PATH"
fi
