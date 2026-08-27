#!/usr/bin/env bash
# Print the ModLinks manifest for the CURRENT release, ready to paste.
#
# ModLinks does not track this repository. It pins a URL and a checksum, so every release needs a
# pull request against hk-modding/modlinks updating <Version> and SHA256, or Lumafly keeps serving
# the old version forever.
#
# Usage:  ./tools/modlinks.sh            # checksum from the PUBLISHED release (what CI verifies)
#         ./tools/modlinks.sh --local    # checksum from ./dist, before publishing
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NAME="HalallowKnight"
REPO="akhihaani/Halallow-Knight"
CFG="$ROOT/src/$NAME/reword-config.json"

VERSION="$(python3 -c "import json;print(json.load(open('$CFG'))['version'])")"
ZIP="$NAME-$VERSION.zip"
URL="https://github.com/$REPO/releases/download/v$VERSION/$ZIP"

if [ "${1:-}" = "--local" ]; then
    [ -f "$ROOT/dist/$ZIP" ] || { echo "No $ROOT/dist/$ZIP - run ./tools/package.sh first." >&2; exit 1; }
    SHA=$(shasum -a 256 "$ROOT/dist/$ZIP" | awk '{print toupper($1)}')
    SRC="local dist/ (NOT yet published - CI verifies the published asset)"
else
    # gh, not curl: a release download URL can serve a stale CDN copy.
    TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
    gh release download "v$VERSION" --repo "$REPO" -p "$ZIP" -D "$TMP" --clobber 2>/dev/null \
        || { echo "No published release v$VERSION on $REPO. Publish it, or use --local." >&2; exit 1; }
    SHA=$(shasum -a 256 "$TMP/$ZIP" | awk '{print toupper($1)}')
    SRC="published release v$VERSION"

    if unzip -Z1 "$TMP/$ZIP" | grep -q '/'; then
        echo "WARNING: the published zip wraps its files in a folder." >&2
        echo "Installers create Mods/$NAME/ themselves, so this installs one level too deep." >&2
    fi
fi

echo "# checksum from: $SRC" >&2
echo >&2

sed -e "s|@VERSION@|$VERSION.0|" -e "s|@SHA@|$SHA|" -e "s|@URL@|$URL|" "$ROOT/docs/modlinks-template.xml"

cat >&2 <<MSG

Paste at the END of https://github.com/hk-modding/modlinks/blob/main/ModLinks.xml
(just before </ModLinks>), replacing the existing <Manifest> for $NAME.

Never re-upload an asset for a version already listed there - their CI re-verifies every
checksum nightly, so a changed asset breaks the build. Cut a new version instead.
MSG
