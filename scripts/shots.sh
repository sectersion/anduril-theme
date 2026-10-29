#!/usr/bin/env bash
# Capture screenshots of all deployed pages into screenshots/
# Requires: npx playwright + chromium (npx playwright install chromium), or sets PAGE env.
set -euo pipefail
BASE="${1:-https://anduril.vaultless.dev}"
OUT="${2:-screenshots}"
mkdir -p "$OUT"
for p in index.html systems.html reliability.html specs.html 404.html; do
  name="${p%.html}"
  echo "→ $BASE/$p → $OUT/${name}.png"
  npx -y playwright screenshot \
    --viewport-size=1440,900 --full-page --wait-for-timeout=2500 \
    "$BASE/$p" "$OUT/${name}.png" || echo "failed: $p"
done
echo "Done. Compare across commits with any image-diff tool."
