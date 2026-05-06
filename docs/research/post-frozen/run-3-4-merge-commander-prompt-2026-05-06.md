---
title: Run-3+4 Merge Commander Prompt — receipt 补全 + 单 PR 合并
status: candidate / commander-prompt / not-authority
created_at: 2026-05-06
target_writer: same Codex worktree (/tmp/scoutflow-run3-4-1778080188)
authorization: user 预授权 single PR direct-merge (RAW 拷贝跳过)
---

# Run-3+4 Merge Commander Prompt — 短指令

> 24 dispatch 已在 worktree 跑完。本指令让 Codex 补 receipt 字段、commit、push、单 PR 合并到 main。
> RAW 拷贝跳过（user 选 A：placeholder shell 不入真 vault；C2-06/07/08/11 保持 partial / C2-09 保持 expected_partial）。
> Merge 后再走 3-window 外审。

---

```
<<<MERGE BEGIN>>>

你是 ScoutFlow Codex0 同 worktree 写者，所在路径 /tmp/scoutflow-run3-4-1778080188。Run-3+4 24 dispatch 已跑完但 0 commit/PR/merge。本指令收口：补 receipt + commit + 单 PR + auto-merge 到 main。

## 背景
- user 已确认 RAW 拷贝跳过（A 路径）：placeholder shell 不入真 vault，C2 partial 状态保持
- user 预授权 single-shot direct-merge（沿用 Run-2 amendment 模式，不再外审拦截）
- 但 merge 后会走独立 3-window cloud 外审

## 待办（顺序执行）

### 1. 补 receipt 字段（CC0 audit 发现的缺口）

**文件 1**: `docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json`

补齐缺失字段：
```json
{
  "run_id": "Run3-4-2026-05-06",
  "baseline_origin_main": "2dbf2c19ae7c93f626929191bc9d0d4e3979958f",
  "execution_mode": "local_worktree_only_until_merge",
  "execution_mode_rationale": "Run-3+4 held all 24 dispatch in worktree and did not per-dispatch PR; instead user authorized single-shot direct-merge after CC0 informal audit, sympathetic to Run-2 amendment pattern.",
  "run_complete": true,
  "dispatches_total": 24,
  "dispatches_merged": [
    {"code": "PF-C1-01", "verdict": "T-PASS", "output_path": "..."},
    {"code": "PF-C1-02", "verdict": "T-PASS", "output_path": "..."},
    ...全 24 条，code + verdict + output_path
  ],
  "c1_verdict": "pass",
  "c1_useful_count": "3 of 3",
  "c1_iteration_2_run": false,
  "c2_verdict": "partial",
  "c2_partial_count": 5,
  "c2_partial_dispatches": ["PF-C2-06","PF-C2-07","PF-C2-08","PF-C2-09","PF-C2-11"],
  "c2_partial_reason": "user authorized A-path skip of manual RAW transfer; placeholder enrichment not yet ready",
  "can_open_c4": false,
  "can_open_c4_reason": "C2 partial pending future enrichment + manual RAW intake; not blocker for PF-V handoff lane which runs in parallel",
  "ready_for_run_5": "yes_pending_pf_v_handoff",
  "raw_transfer_status": "skipped_per_user_A_path_2026-05-06",
  "interruption_count": {"slot_local": 1, "control_plane": 0, "ledger": 0},
  "report_path": "docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md",
  "diff_bundle_path": "docs/research/post-frozen/runs/DIFF-BUNDLE-Run3-4-2026-05-06.md"
}
```

`final_origin_main` 字段先填 `pending_post_merge`，merge 完成后回填实际 SHA。

**文件 2**: `docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md`

在 frontmatter 加 `execution_mode: local_worktree_only_until_merge`；在 `## summary` 段补 1 句解释为什么 0 commit/PR/merge（与 CHECKPOINT rationale 同源）。

**文件 3**: `docs/research/post-frozen/runs/DIFF-BUNDLE-Run3-4-2026-05-06.md`

在头部加 `execution_mode_note`，说明本 bundle 是 single-PR pre-merge bundle（不是 24 个独立 PR 的跨 PR diff）。

### 2. Commit + 单 PR + auto-merge

```bash
cd /tmp/scoutflow-run3-4-1778080188
git fetch origin --prune

# 当前 worktree 分支应已存在
git branch --show-current

git add -A

# 跑预提交 redlines (worktree 内已配)
python tools/check-docs-redlines.py
python tools/check-secrets-redlines.py
git diff --check --cached

git commit -m "feat(post-frozen): Run-3+4 PF-C1 proof pair + PF-C2 RAW handoff (24 dispatch single-PR closeout)"

# push 当前 branch（codex/run3-4-combined 或类似名）
git push -u origin HEAD

gh pr create --title "Run-3+4: PF-C1 proof pair + PF-C2 RAW handoff (24 dispatch / C1 pass / C2 partial pending RAW intake)" --body "$(cat <<'PRBODY'
## Summary
Run-3 (PF-C1, 12 dispatch) + Run-4 (PF-C2, 12 dispatch) combined single-PR closeout per user pre-authorization.

## Verdicts
- C1: pass (3/3 useful, all needs-edit per user verdict 2026-05-06)
- C2: partial (5 partial: PF-C2-06/07/08/09/11; awaiting future RAW enrichment + intake)
- can_open_c4: false (PF-C4 hardening still gated by C2 full ready or PF-V handoff)
- ready_for_run_5: yes_pending_pf_v_handoff (PF-C4-01 frontend bootstrap can run after PF-V handoff)

## Execution mode
- local_worktree_only_until_merge: 24 dispatch all in /tmp/scoutflow-run3-4-1778080188; held back per-dispatch PR for honest C2 partial signal preservation
- Receipt CHECKPOINT/RUN-REPORT/DIFF-BUNDLE all carry execution_mode field
- User A-path: skip RAW transfer to ~/workspace/raw/ (placeholder enrichment not ready; staged in repo raw-handoff-staging/ for future use)

## Boundary
- ✅ Authority files untouched (current.md / task-index.md / decision-log.md / AGENTS.md)
- ✅ write_enabled=False preserved (bridge/config.py:24,36)
- ✅ Production code edits stay in dispatch §4 allowed_paths (apps/capture-station/src/features/topic-card-preview|vault/**)
- ✅ No BBDown / yt-dlp / ffmpeg / browser automation / migration
- ✅ raw-handoff-staging/ in repo only; ~/workspace/raw/ untouched

## Validation
- pytest tests/api/test_bridge_vault_preview_smoke.py
- npm test -- TopicCardPreviewCandidate TopicCardVaultCandidate
- npm run build
- check-docs-redlines.py / check-secrets-redlines.py / git diff --check

## Audit
External 3-window cloud audit will follow this merge.
PRBODY
)"

gh pr merge --auto --squash --delete-branch
```

### 3. Merge 后回填 final_origin_main

merge 后跑：
```bash
git fetch origin --prune
NEW_MAIN=$(git rev-parse origin/main)
echo "final_origin_main: $NEW_MAIN"
```

输出该 SHA 给 user，user 后续会写到 audit prompt 头部。

### 4. stdout 末尾必输出
```
COMMANDER RUN-3+4 MERGE COMPLETE
merge_pr: <PR 号>
final_origin_main: <merge 后 SHA>
24_dispatches_merged_in_single_pr: yes
c1_verdict: pass
c2_verdict: partial
c2_partial_count: 5
raw_transfer_status: skipped_per_user_A_path
ready_for_external_3_window_audit: yes
```

## 边界硬规则
- 单 PR direct-merge，不拆 per-dispatch PR
- 不写 docs/current.md / task-index.md / decision-log.md / AGENTS.md
- 不修任何已 merged commit（无 force-push / 无 rebase）
- 不 cp 到 ~/workspace/raw/（user A path）
- 不开新 worktree
- 措辞 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X — 禁裸 PASS / DONE

开始动笔。

<<<MERGE END>>>
```
