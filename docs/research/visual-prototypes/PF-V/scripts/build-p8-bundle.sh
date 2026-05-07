#!/usr/bin/env bash
# PF-V P8 Bundle Builder
# Packs P7 output + PF-V reference docs + P8 prompt into one small ZIP for GPT Pro.

set -euo pipefail

PFV_ROOT="/Users/wanglei/workspace/ScoutFlow/docs/research/visual-prototypes/PF-V"
PROJECT_ROOT="/Users/wanglei/workspace/ScoutFlow"
P7_OUTPUT_SRC="/Users/wanglei/Downloads/PF-V-P7-output"
STAGE="/tmp/pfv-p8-bundle"
OUT_ZIP="${PFV_ROOT}/pfv-p8-bundle.zip"

echo "[1/4] Cleaning stage..."
rm -rf "$STAGE" "$OUT_ZIP"
mkdir -p "$STAGE/p7-output"

echo "[2/4] Copying P7 output (76 files) + PF-V reference docs..."

# P7 output (gold, GPT Pro just produced 25 min ago)
cp -R "${P7_OUTPUT_SRC}/." "${STAGE}/p7-output/"

# PF-V context refs (renamed for unambiguous referencing in prompt)
cp "${PFV_ROOT}/README.md"                                    "${STAGE}/PF-V-README.md"
cp "${PFV_ROOT}/04-INDEX.csv"                                 "${STAGE}/PF-V-INDEX.csv"
cp "${PFV_ROOT}/LESSONS-LEARNED.md"                           "${STAGE}/PF-V-LESSONS-LEARNED.md"
cp "${PFV_ROOT}/MAINTENANCE-PROTOCOL.md"                      "${STAGE}/PF-V-MAINTENANCE-PROTOCOL.md"
cp "${PFV_ROOT}/03-P7-batch-prompt-v2.md"                     "${STAGE}/PF-V-03-P7-batch-prompt-v2.md"
cp "${PFV_ROOT}/05-HANDOFF-to-PF-C4-protocol.md"              "${STAGE}/PF-V-05-HANDOFF-protocol-v0-candidate.md"
cp "${PFV_ROOT}/00-master-context.md"                         "${STAGE}/PF-V-00-master-context.md"
cp "${PROJECT_ROOT}/CLAUDE.md"                                "${STAGE}/PROJECT-CLAUDE.md"

# P8 prompt (the actual task)
cp "${PFV_ROOT}/04-P8-handoff-prompt.md"                      "${STAGE}/P8-PROMPT.md"

echo "  Stage contents:"
ls -lh "${STAGE}/"

echo "[3/4] Creating ZIP..."
cd "$STAGE"
zip -qr "$OUT_ZIP" .
cd - > /dev/null

ZIP_KB=$(du -k "$OUT_ZIP" | cut -f1)
FILE_COUNT=$(unzip -l "$OUT_ZIP" | tail -1 | awk '{print $2}')

echo ""
echo "═══════════════════════════════════════════════"
echo "  P8 Bundle Built ✓"
echo "═══════════════════════════════════════════════"
echo "  Output: $OUT_ZIP"
echo "  Size:   ${ZIP_KB}KB"
echo "  Files:  $FILE_COUNT"
echo "═══════════════════════════════════════════════"
