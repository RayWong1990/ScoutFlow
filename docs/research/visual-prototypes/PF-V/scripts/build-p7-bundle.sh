#!/usr/bin/env bash
# PF-V P7 Bundle Builder
# Curates 65 V-PASS images per task mapping, optimizes PNG, packs ZIP for GPT Pro upload.
# Idempotent: re-running cleans stage + rebuilds.

set -euo pipefail

PFV_ROOT="/Users/wanglei/workspace/ScoutFlow/docs/research/visual-prototypes/PF-V"
STAGE="/tmp/pfv-p7-bundle"
OUT_ZIP="${PFV_ROOT}/pfv-p7-bundle.zip"
PROMPT_DOC="${PFV_ROOT}/03-P7-batch-prompt-v2.md"

echo "[1/5] Cleaning stage dir..."
rm -rf "$STAGE" "$OUT_ZIP"
mkdir -p "$STAGE"

echo "[2/5] Copying + renaming 65 source images..."

# Surface group dirs
for d in 00_app-shell 01_url-bar 02_live-metadata 03_capture-scope 04_trust-trace \
         05_vault-preview 06_vault-commit 07_topic-card-lite 08_topic-card-vault \
         09_signal-hypothesis-ia 10_capture-plan-ia 11_density-spec 12_type-spec \
         13_icons-system 14_icons-state; do
  mkdir -p "${STAGE}/${d}"
done

# Mapping: source_path → stage_path
declare -A MAP=(
  # 00 App Shell (1)
  ["${PFV_ROOT}/images-P0/pfv-SUPER-ANCHOR-FINAL-cn.png"]="00_app-shell/task-00_master.png"

  # 01 URL Bar (5) — empty/focus/validating/error/history-dropdown
  ["${PFV_ROOT}/images-P2-url-bar/pfv-S04-V1-cn-empty.png"]="01_url-bar/task-01_state-empty.png"
  ["${PFV_ROOT}/images-P2-url-bar/pfv-S04-V2-cn-focus.png"]="01_url-bar/task-02_state-focus.png"
  ["${PFV_ROOT}/images-P2-url-bar/pfv-S04-V5-cn-validating.png"]="01_url-bar/task-03_state-validating.png"
  ["${PFV_ROOT}/images-P2-url-bar/pfv-S04-V6-cn-error-TOP3.png"]="01_url-bar/task-04_state-error.png"
  ["${PFV_ROOT}/images-P2-url-bar/pfv-S04-V9-cn-history-dropdown-TOP1.png"]="01_url-bar/task-05_state-history-dropdown.png"

  # 02 Live Metadata (5)
  ["${PFV_ROOT}/images-P2-live-metadata/pfv-S05-V1-cn-long-cn-title.png"]="02_live-metadata/task-06_long-cn-title.png"
  ["${PFV_ROOT}/images-P2-live-metadata/pfv-S05-V4-cn-numbers-heavy-TOP3.png"]="02_live-metadata/task-07_numbers-heavy.png"
  ["${PFV_ROOT}/images-P2-live-metadata/pfv-S05-V6-cn-tags-overflow-TOP2.png"]="02_live-metadata/task-08_tags-overflow.png"
  ["${PFV_ROOT}/images-P2-live-metadata/pfv-S05-V7-cn-live-counter-TOP1.png"]="02_live-metadata/task-09_live-counter.png"
  ["${PFV_ROOT}/images-P2-live-metadata/pfv-S05-V10-cn-thumbnail-field.png"]="02_live-metadata/task-10_thumbnail-field.png"

  # 03 Capture Scope (3)
  ["${PFV_ROOT}/images-P2-capture-scope/pfv-S06-V1-cn-lifecycle-start.png"]="03_capture-scope/task-11_lifecycle-start.png"
  ["${PFV_ROOT}/images-P2-capture-scope/pfv-S06-V3-cn-lifecycle-complete-TOP3.png"]="03_capture-scope/task-12_lifecycle-complete.png"
  ["${PFV_ROOT}/images-P2-capture-scope/pfv-S06-V5-cn-blocked-layer-tooltip-TOP1.png"]="03_capture-scope/task-13_blocked-layer-tooltip.png"

  # 04 Trust Trace (3)
  ["${PFV_ROOT}/images-P2-trust-trace/pfv-S07-V1-cn-filter-dom-only.png"]="04_trust-trace/task-14_filter-dom-only.png"
  ["${PFV_ROOT}/images-P2-trust-trace/pfv-S07-V3-cn-time-axis-TOP1.png"]="04_trust-trace/task-15_time-axis.png"
  ["${PFV_ROOT}/images-P2-trust-trace/pfv-S07-V4-cn-error-path-TOP2.png"]="04_trust-trace/task-16_error-path.png"

  # 05 Vault Preview (5)
  ["${PFV_ROOT}/images-P2-vault-preview/pfv-S08-V1-cn-idle.png"]="05_vault-preview/task-17_idle.png"
  ["${PFV_ROOT}/images-P2-vault-preview/pfv-S08-V3-cn-ready-TOP1.png"]="05_vault-preview/task-18_ready.png"
  ["${PFV_ROOT}/images-P2-vault-preview/pfv-S08-V5-cn-blocked-overflow-registry-TOP2.png"]="05_vault-preview/task-19_blocked-overflow-registry.png"
  ["${PFV_ROOT}/images-P2-vault-preview/pfv-S08-V7-cn-frontmatter-expanded.png"]="05_vault-preview/task-20_frontmatter-expanded.png"
  ["${PFV_ROOT}/images-P2-vault-preview/pfv-S08-V8-cn-copy-action-TOP3.png"]="05_vault-preview/task-21_copy-action.png"

  # 06 Vault Commit (5)
  ["${PFV_ROOT}/images-P2-vault-commit/pfv-S09-V1-cn-standard.png"]="06_vault-commit/task-22_standard.png"
  ["${PFV_ROOT}/images-P2-vault-commit/pfv-S09-V2-cn-tooltip-knowledge-flywheel-TOP1.png"]="06_vault-commit/task-23_tooltip-knowledge-flywheel.png"
  ["${PFV_ROOT}/images-P2-vault-commit/pfv-S09-V4-cn-modal-pass-TOP3.png"]="06_vault-commit/task-24_modal-pass.png"
  ["${PFV_ROOT}/images-P2-vault-commit/pfv-S09-V5-cn-modal-fail.png"]="06_vault-commit/task-25_modal-fail.png"
  ["${PFV_ROOT}/images-P2-vault-commit/pfv-S09-V9-cn-batch-dry-run-TOP2.png"]="06_vault-commit/task-26_batch-dry-run.png"

  # 07 Topic Card Lite (5)
  ["${PFV_ROOT}/images-P3-topic-card-lite/pfv-S10-V1-cn-news-article.png"]="07_topic-card-lite/task-27_news-article.png"
  ["${PFV_ROOT}/images-P3-topic-card-lite/pfv-S10-V2-cn-bilibili-video-TOP1.png"]="07_topic-card-lite/task-28_bilibili-video.png"
  ["${PFV_ROOT}/images-P3-topic-card-lite/pfv-S10-V5-cn-multi-signal.png"]="07_topic-card-lite/task-29_multi-signal.png"
  ["${PFV_ROOT}/images-P3-topic-card-lite/pfv-S10-V7-cn-evidence-pointers-TOP2.png"]="07_topic-card-lite/task-30_evidence-pointers.png"
  ["${PFV_ROOT}/images-P3-topic-card-lite/pfv-S10-V10-cn-dual-card-compare-TOP3.png"]="07_topic-card-lite/task-31_dual-card-compare.png"

  # 08 Topic Card Vault (5)
  ["${PFV_ROOT}/images-P3-topic-card-vault/pfv-S11-V1-cn-default.png"]="08_topic-card-vault/task-32_default.png"
  ["${PFV_ROOT}/images-P3-topic-card-vault/pfv-S11-V5-cn-source-url-aggregate-TOP3.png"]="08_topic-card-vault/task-33_source-url-aggregate.png"
  ["${PFV_ROOT}/images-P3-topic-card-vault/pfv-S11-V7-cn-promote-readiness-TOP1.png"]="08_topic-card-vault/task-34_promote-readiness.png"
  ["${PFV_ROOT}/images-P3-topic-card-vault/pfv-S11-V8-cn-promote-diloflow-modal.png"]="08_topic-card-vault/task-35_promote-diloflow-modal.png"
  ["${PFV_ROOT}/images-P3-topic-card-vault/pfv-S11-V10-cn-obsidian-sync-status-TOP2.png"]="08_topic-card-vault/task-36_obsidian-sync-status.png"

  # 09 Signal/Hypothesis IA (3)
  ["${PFV_ROOT}/images-P3-signal-hypothesis-ia/pfv-S12-V2-cn-signal-expanded-with-hypotheses.png"]="09_signal-hypothesis-ia/task-37_signal-expanded-with-hypotheses.png"
  ["${PFV_ROOT}/images-P3-signal-hypothesis-ia/pfv-S12-V3-cn-hypothesis-compare-TOP2.png"]="09_signal-hypothesis-ia/task-38_hypothesis-compare.png"
  ["${PFV_ROOT}/images-P3-signal-hypothesis-ia/pfv-S12-V4-cn-signal-lifecycle-stepper-TOP3.png"]="09_signal-hypothesis-ia/task-39_signal-lifecycle-stepper.png"

  # 10 Capture Plan IA (3)
  ["${PFV_ROOT}/images-P3-capture-plan-ia/pfv-S12-V7-cn-plan-io-contract.png"]="10_capture-plan-ia/task-40_plan-io-contract.png"
  ["${PFV_ROOT}/images-P3-capture-plan-ia/pfv-S12-V8-cn-plan-dry-run-TOP1.png"]="10_capture-plan-ia/task-41_plan-dry-run.png"
  ["${PFV_ROOT}/images-P3-capture-plan-ia/pfv-S12-V9-cn-plan-execution-log.png"]="10_capture-plan-ia/task-42_plan-execution-log.png"

  # 11 Density Spec (1)
  ["${PFV_ROOT}/images-P6-density-refinement/pfv-S17-V3-cn-density-compact-TOP1.png"]="11_density-spec/task-43_density-compact-baseline.png"

  # 12 Type Spec (1)
  ["${PFV_ROOT}/images-P6-typography-refinement/pfv-S18-V4-cn-type-weight-heavy-TOP2.png"]="12_type-spec/task-44_type-weight-heavy.png"

  # 13 Icons system (10)
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V1-cn-icon-capture.png"]="13_icons-system/task-45_icon-capture.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V2-cn-icon-preview.png"]="13_icons-system/task-46_icon-preview.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V3-cn-icon-commit.png"]="13_icons-system/task-47_icon-commit.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V4-cn-icon-dry-run.png"]="13_icons-system/task-48_icon-dry-run.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V5-cn-icon-blocked-TOP2.png"]="13_icons-system/task-49_icon-blocked.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V6-cn-icon-signal-TOP3.png"]="13_icons-system/task-50_icon-signal.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V7-cn-icon-hypothesis.png"]="13_icons-system/task-51_icon-hypothesis.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V8-cn-icon-plan.png"]="13_icons-system/task-52_icon-plan.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V9-cn-icon-trace-TOP1.png"]="13_icons-system/task-53_icon-trace.png"
  ["${PFV_ROOT}/images-P5-icons-system/pfv-S15-V10-cn-icon-evidence.png"]="13_icons-system/task-54_icon-evidence.png"

  # 14 Icons state (10)
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V1-cn-icon-live-TOP2.png"]="14_icons-state/task-55_icon-state-live.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V2-cn-icon-success.png"]="14_icons-state/task-56_icon-state-success.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V3-cn-icon-warning.png"]="14_icons-state/task-57_icon-state-warning.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V4-cn-icon-error.png"]="14_icons-state/task-58_icon-state-error.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V5-cn-icon-blocked.png"]="14_icons-state/task-59_icon-state-blocked.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V6-cn-icon-locked.png"]="14_icons-state/task-60_icon-state-locked.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V7-cn-icon-focus-TOP1.png"]="14_icons-state/task-61_icon-state-focus.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V8-cn-icon-loading-TOP3.png"]="14_icons-state/task-62_icon-state-loading.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V9-cn-icon-empty.png"]="14_icons-state/task-63_icon-state-empty.png"
  ["${PFV_ROOT}/images-P5-icons-state/pfv-S16-V10-cn-icon-ready.png"]="14_icons-state/task-64_icon-state-ready.png"
)

MISSING=0
for src in "${!MAP[@]}"; do
  dst="${STAGE}/${MAP[$src]}"
  if [[ ! -f "$src" ]]; then
    echo "  MISSING: $src"
    MISSING=$((MISSING+1))
    continue
  fi
  cp "$src" "$dst"
done

if [[ $MISSING -gt 0 ]]; then
  echo "ERROR: $MISSING source images missing. Aborting."
  exit 1
fi

echo "  Copied 65 images to stage."

echo "[3/5] Optimizing PNGs via PIL (resize + lossless compress)..."
python3 <<'PYEOF'
import os
from PIL import Image
stage = "/tmp/pfv-p7-bundle"
# Resize policy:
# - Surface mockups (16:9 desktop @ 2K = 2048×1152) → max 1536px wide (still HD, text readable)
# - Icons (1024×1024) → keep 1024 (small files already)
MAX_WIDE = 1152
total_before = 0
total_after = 0
count = 0
for root, _, files in os.walk(stage):
    for f in files:
        if not f.endswith('.png'):
            continue
        path = os.path.join(root, f)
        before = os.path.getsize(path)
        img = Image.open(path)
        # Drop alpha if no transparency
        if img.mode == 'RGBA':
            extrema = img.getextrema()
            if len(extrema) == 4 and extrema[3] == (255, 255):
                img = img.convert('RGB')
        # Resize if wider than MAX_WIDE (preserves aspect)
        w, h = img.size
        if w > MAX_WIDE:
            new_h = int(h * MAX_WIDE / w)
            img = img.resize((MAX_WIDE, new_h), Image.LANCZOS)
        img.save(path, optimize=True, compress_level=9)
        after = os.path.getsize(path)
        total_before += before
        total_after += after
        count += 1
mb_before = total_before / (1024*1024)
mb_after = total_after / (1024*1024)
saved_pct = (1 - total_after/total_before) * 100 if total_before else 0
print(f"  {count} PNGs: {mb_before:.1f}MB -> {mb_after:.1f}MB ({saved_pct:.0f}% saved)")
PYEOF

echo "[4/5] Copying PROMPT.md to stage root..."
cp "$PROMPT_DOC" "${STAGE}/PROMPT.md"

echo "[5/5] Creating ZIP..."
cd "$STAGE"
zip -qr "$OUT_ZIP" .
cd - > /dev/null

ZIP_MB=$(du -m "$OUT_ZIP" | cut -f1)
FILE_COUNT=$(unzip -l "$OUT_ZIP" | tail -1 | awk '{print $2}')

echo ""
echo "═══════════════════════════════════════════════"
echo "  P7 Bundle Built ✓"
echo "═══════════════════════════════════════════════"
echo "  Output: $OUT_ZIP"
echo "  Size:   ${ZIP_MB}MB"
echo "  Files:  $FILE_COUNT (65 PNG + 1 PROMPT.md)"
echo "═══════════════════════════════════════════════"
echo ""
echo "Stage dir kept at $STAGE for inspection (auto-cleaned next run)."
