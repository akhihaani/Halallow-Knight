#!/usr/bin/env bash
# Build a release zip ready to drop into the game's Mods folder, or to attach to a GitHub release.
#
# Usage:  ./tools/package.sh [version]
#
# The zip contains one folder, so a user unzips it straight into Mods/ - which is also exactly
# what Lumafly's manual-install button expects.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="HalallowKnight"
SRC="$ROOT/src/$NAME"
DIST="$ROOT/dist"

# The version lives in the config, so a wording-only change still ships a new number.
VERSION="${1:-$(python3 -c "import json;print(json.load(open('$SRC/reword-config.json'))['version'])")}"

echo "Packaging $NAME $VERSION"
rm -rf "$DIST"
mkdir -p "$DIST/$NAME"

dotnet build "$SRC/$NAME.csproj" -c Release -v minimal

cp "$SRC/bin/Release/$NAME.dll" "$DIST/$NAME/"
cp "$SRC/reword-config.json"    "$DIST/$NAME/"
cp "$ROOT/README.md"            "$DIST/$NAME/"
cp "$ROOT/REWORDS.md"           "$DIST/$NAME/"

ZIP="$DIST/$NAME-$VERSION.zip"
( cd "$DIST" && zip -qr "$(basename "$ZIP")" "$NAME" )

echo
echo "  $ZIP"
unzip -Z1 "$ZIP" | sed 's/^/  /'
echo
echo "Next:"
echo "  gh release create v$VERSION \"$ZIP\" --title \"$NAME $VERSION\" --notes \"...\""
