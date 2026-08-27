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
# Files go at the ZIP ROOT, not inside a folder. Mod installers create Mods/<Name>/ themselves
# and extract into it, so a wrapper folder would nest the DLL one level too deep and stop the
# Modding API finding it. Every mod in modlinks packages this way.
rm -rf "$DIST"
mkdir -p "$DIST/staging"

dotnet build "$SRC/$NAME.csproj" -c Release -v minimal

cp "$SRC/bin/Release/$NAME.dll" "$DIST/staging/"
cp "$SRC/reword-config.json"    "$DIST/staging/"
cp "$ROOT/README.md"            "$DIST/staging/"
cp "$ROOT/REWORDS.md"           "$DIST/staging/"

ZIP="$DIST/$NAME-$VERSION.zip"
( cd "$DIST/staging" && zip -qr "../$(basename "$ZIP")" . )
rm -rf "$DIST/staging"

echo
echo "  $ZIP"
unzip -Z1 "$ZIP" | sed 's/^/  /'
echo
echo "Next:"
echo "  gh release create v$VERSION \"$ZIP\" --title \"$NAME $VERSION\" --notes \"...\""
