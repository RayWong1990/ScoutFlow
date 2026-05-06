---
title: Run-3+4 External Audit Prompt — 3-Window Cloud Triangulation
status: candidate / audit-prompt / not-authority
created_at: 2026-05-07
target_writer: 3 independent cloud auditors (Hermes / GPT Pro web / Codex CLI fresh window)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow
audit_baseline_sha: 2dbf2c19ae7c93f626929191bc9d0d4e3979958f
audit_final_sha: ea509022eb05a552777373394a6fc2a5077f27f6
audited_pr: 240
audited_runs: [Run-3 PF-C1 proof pair, Run-4 PF-C2 RAW handoff]
known_limitations:
  - CHECKPOINT-Run3-4-final.json `final_origin_main` 字段写为 `pending_post_merge`（merge 后未补 commit）；真值 = `ea50902`
  - 24 dispatch single-PR direct-merge（非 per-dispatch PR）— 已在 receipt `execution_mode_rationale` 声明
  - 5 个 C2 partial 是 user A-path 跳过 RAW 拷贝的级联设计，非 silent flexibility
---

# Run-3 + Run-4 严格外审 Commander Prompt — 3 窗口云端三角验证

> 复制 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 整段，同时粘到 3 个独立云端窗口。
> 所有输入都是 GitHub URL（receipt 已 merged 到 main）。

---

## 派单前必跑（一次推 audit prompt 到 GitHub）

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git checkout -b run3-4-audit-handoff origin/main
git add docs/research/post-frozen/run-3-4-combined-codex-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/run-3-4-merge-commander-prompt-2026-05-06.md \
        docs/research/post-frozen/run-3-4-external-audit-prompt-2026-05-07.md
git commit -m "chore(post-frozen): snapshot Run-3+4 commander + merge + audit prompts for external audit"
git push -u origin run3-4-audit-handoff
```

---

## 已锁事实（审计员开工前 user 已确认）

- **baseline → final**: `2dbf2c1` → `ea50902`
- **single PR**: #240 merged 单发 24 dispatch — execution_mode = `local_worktree_only_until_merge`，已在 receipt 声明，**不质疑此架构**
- **C1 verdict**: pass / 3-of-3 useful / 全 needs-edit（user 显式判定，参 evidence file）
- **C2 verdict**: partial / 5 partial 是 user A-path 跳过 RAW 拷贝的设计内态，**不质疑**
- **CHECKPOINT 字段限制**: `final_origin_main: pending_post_merge` 是 single-PR 直 merge 受限留下的 receipt drift（user 已知；真值 = `ea50902`），**不要求修**

审计员任务：核 Codex 自报 + 找 silent flexibility，**不**重新质疑 4 项已锁事实。

---

```
<<<AUDIT BEGIN>>>

你是 ScoutFlow Run-3+4 独立外审员。3 独立云端窗口同时跑同段 prompt，user 三角对比 verdict。你不知道其它 2 个 auditor 是谁、不读对方报告。

## 角色
- 只读 audit。禁 git/gh/push/merge/任何文件修改/CI/pytest/pnpm
- 输出一份 markdown audit report 贴回对话
- 措辞 T-PASS / V-PASS / partial / FAIL_X / REJECT_AS_X / clear / concern / reject — 禁裸 PASS / DONE / OK / works
- 全云端：fetch GitHub URL，无本地

## 项目身份
- repo: https://github.com/RayWong1990/ScoutFlow
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline_origin_main: `2dbf2c19ae7c93f626929191bc9d0d4e3979958f`（Run-2 amendment 收口后）
- final_origin_main: `ea509022eb05a552777373394a6fc2a5077f27f6`（PR #240 merge 后）
- single PR: #240 (24 dispatch combined)

## 必读输入

### 1. Run-3+4 收尾产物（main 分支）
- RUN-3-4 报告: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md
- DIFF-BUNDLE: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/DIFF-BUNDLE-Run3-4-2026-05-06.md
- CHECKPOINT: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json
- C1-08 user verdict: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md
- C1 三 URL proof set: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c1-three-url-preview-proof-set.md
- C1 false-positive log: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c1-false-positive-edit-cost-log.md
- C1 readback: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c1-proof-readback.md
- C2 readback: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c2-proof-readback.md
- C2 second-inbox negative test: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c2-second-inbox-negative-test.md
- C2 RAW intake readback: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c2-raw-intake-readback-result.md
- ScoutFlow/RAW SoR matrix: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/scoutflow-raw-sor-handoff-matrix.md
- RAW handoff staging: https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/raw-handoff-staging
- C1 三 URL proof artifacts: https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/proof-artifacts/run-3-c1-07

### 2. Codex 收到的指令（run3-4-audit-handoff 分支）
- 原 commander prompt: https://github.com/RayWong1990/ScoutFlow/blob/run3-4-audit-handoff/docs/research/post-frozen/run-3-4-combined-codex-commander-prompt-2026-05-06.md
- merge commander prompt: https://github.com/RayWong1990/ScoutFlow/blob/run3-4-audit-handoff/docs/research/post-frozen/run-3-4-merge-commander-prompt-2026-05-06.md

### 3. PR #240
- https://github.com/RayWong1990/ScoutFlow/pull/240
- /files: https://github.com/RayWong1990/ScoutFlow/pull/240/files

### 4. Dispatch 源（验收基线）
- PF-C1 cluster: https://github.com/RayWong1990/ScoutFlow/tree/ea50902/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C1-proof-pair-pack
- PF-C2 cluster: https://github.com/RayWong1990/ScoutFlow/tree/ea50902/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C2-raw-handoff-pack

### 5. Live truth（关键代码 final-state）
- bridge/config.py: https://github.com/RayWong1990/ScoutFlow/blob/ea50902/services/api/scoutflow_api/bridge/config.py
- TopicCardPreviewCandidate.tsx: https://github.com/RayWong1990/ScoutFlow/blob/ea50902/apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.tsx
- TopicCardVaultCandidate.tsx: https://github.com/RayWong1990/ScoutFlow/blob/ea50902/apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx

### 6. Compare baseline → final
- https://github.com/RayWong1990/ScoutFlow/compare/2dbf2c1...ea50902

---

## 审计 Charter — 10 检查点

每点 verdict (clear / concern / reject) + evidence (URL + 引用).

### A. C1-04 / C1-05 production code 边界（HIGH）
- C1-04 应只触 `apps/capture-station/src/features/topic-card-preview/**` + `tests/**`
- C1-05 应只触 `apps/capture-station/src/features/topic-card-vault/**` + `tests/**`
- PR #240 /files 扫一遍，看是否有任何文件越出这 2 个 dispatch §4 allowed_paths
- 任何越界 → reject

### B. C1-08 user verdict → C1-10/12 verdict 链对齐（HIGH）
- user evidence 写: 3/3 useful / 全 `needs-edit` / overall=pass / c2_go_no_go=yes / allow_authority_writeback=no
- C1-10 readback 是否如实记录 pass + 3/3 needs-edit？
- C1-12 closeout 是否 stop authority writeback 严守 user `no`？grep `docs/current.md|task-index.md|decision-log.md|AGENTS.md` 在 #240 /files
- 不一致 → reject

### C. C2 5 partial cascade 诚实度（CRITICAL）
- Codex 自报 5 partial: PF-C2-06/07/08/09/11 + C2-09 标 `expected_partial`
- 每份 dispatch 文档应明文说"因为 user A-path 跳过 RAW 拷贝 / RAW intake 未发生"
- C2-09 second-inbox negative test 必须**不**写 pass — 因为 RAW intake 没发生就无法证伪
- 任一 dispatch 把 partial 偷升级为 pass → reject

### D. C2-10 SoR matrix `pass_with_pending_boundary` 语义（MEDIUM）
- 这措辞是 Codex 创造的复合 verdict
- 验：matrix 是否说清 ScoutFlow owns preview/evidence + RAW owns intake/compile/script + no dual SoR
- 验 `pending_boundary` 是指什么 boundary 待定（应是 RAW intake 这一段，与 C2 partial 同源）
- 措辞含糊或暗藏 dual-SoR 风险 → concern

### E. C2-12 future true-write gate 仍 overflow（HIGH）
- C2-12 dispatch pass_bar: "Drafts future true-write gate but keeps it in overflow unless human explicitly approves"
- 验 `future-true-write-gate-draft.md` 标 overflow / future_gate / not_in_mainline
- 验 main.py / bridge/config.py / 任何 production 代码无 `write_enabled=True` 路径或新 enable flag
- 任一暗示 `write_enabled` 解禁 → reject

### F. RAW handoff staging 边界（HIGH）
- staging 文件全在 `docs/research/post-frozen/raw-handoff-staging/` 内
- compare diff 不含 `~/workspace/raw/` 写操作（不可能 commit 这种 absolute path 但仍 grep）
- staged note 内容应是 placeholder enrichment（BVID + 占位 title + boundary flags），不是真 B 站 metadata（write_enabled=False 不真 fetch）
- 任一污染 → reject

### G. Authority untouched（HIGH）
- compare 2dbf2c1...ea50902 不含 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md`
- 任一命中 → reject

### H. 硬红线（HIGH）
- final-state `bridge/config.py` 仍 `write_enabled=False`（两 return 分支）
- compare diff 无: `BBDown` / `yt-dlp` / `ffmpeg` / `audio_transcript` / `subprocess.run` / `playwright` / `selenium` / `puppeteer` / 新 alembic migration

### I. Single-PR vs per-dispatch deviation 声明（MEDIUM）
- Run-3+4 原 commander prompt §"不停歇协议" 写: "per-dispatch one PR + auto-merge on mergeStateStatus=CLEAN"
- 实际：单 PR #240 合 24 dispatch
- 验 receipt 是否在 `execution_mode` / `execution_mode_rationale` 显式声明 deviation + 理由
- 未声明 → concern

### J. Receipt CHECKPOINT 内一致性（MEDIUM）
- CHECKPOINT.json `final_origin_main` 字段是 `pending_post_merge` 字面量（user 已知不修）
- 验 `dispatches_total: 24` 字段填齐
- 验 `dispatches_merged` 数组含 24 条目，code + verdict + output_path 全有
- 验 `c2_partial_dispatches` 数组含 5 个 (PF-C2-06/07/08/09/11)
- 验 `raw_transfer_status: skipped_per_user_A_path_2026-05-06`
- 任一缺 → concern

---

## 输出格式

完整 markdown report 贴回对话。

### Frontmatter
```yaml
---
title: Run-3+4 External Audit Report — <auditor_id>
status: candidate / external_audit / not-authority
created_at: 2026-05-07
auditor: <auditor_id>            # hermes / gpt-pro / codex-cloud / 其它
audit_target: Run-3+4 (PR #240, PF-C1 + PF-C2, 24 dispatch)
audit_baseline_sha: 2dbf2c19ae7c93f626929191bc9d0d4e3979958f
audit_final_sha: ea509022eb05a552777373394a6fc2a5077f27f6
---
```

### 1. 10 检查点 verdict 表
| # | 检查点 | verdict | evidence (URL + 引用) |
|---|---|---|---|
| A | C1-04/05 边界 | clear/concern/reject | ... |
| B | C1-08 → C1-10/12 verdict 链 | ... | ... |
| C | C2 5 partial cascade 诚实度 | ... | ... |
| D | C2-10 SoR pass_with_pending_boundary 语义 | ... | ... |
| E | C2-12 future true-write 仍 overflow | ... | ... |
| F | RAW handoff staging 边界 | ... | ... |
| G | authority untouched | ... | ... |
| H | 硬红线 | ... | ... |
| I | single-PR deviation 声明 | ... | ... |
| J | CHECKPOINT 一致性 | ... | ... |

### 2. Per-dispatch verdict 表（24 dispatch + 抽样 PR #240 部分文件）

C1: PF-C1-01..12 / verdict / scope_deviation_flag / silent_flexibility_count / evidence
C2: PF-C2-01..12 / 同上

### 3. 全局 verdict
- V-PASS / V-PASS_WITH_AMENDMENTS / V-PASS_WITH_HEAVY_EDIT_REQUIRED / REJECT

### 4. 编号 findings（5-10 条，按严重度）
模板:
```
### Finding N [CRITICAL/HIGH/MEDIUM/LOW]
- 检查点关联: <A-J>
- 现象: <一句话>
- 证据: <URL + 行号 + 引用>
- Codex 自报: <Codex 怎么说>
- audit 结论: <更严口径>
- 修复建议: <可执行动作>
```

### 5. Silent flexibility 专栏
列 Codex 执行了但没显式声明的偏移。

### 6. ready_for_run_5 重新判定
- ready_for_run_5: yes / yes_with_amendments / no
- amendments_needed_before_run_5: <列表>
- run_5_blockers: <列表>
- 与 Codex 自报 `ready_for_run_5: yes_pending_pf_v_handoff` 是否一致？为什么？

### 7. 末尾必填字段
```
audit_completed_at: <ISO 8601>
auditor_confidence: high / medium / low
ready_for_run_5: yes / yes_with_amendments / no
amendments_needed_before_run_5: <列表>
followup_audit_after_run_5: required / optional
```

---

## 边界硬规则
- 只读 + 输出 audit report
- 禁 git/gh/push/merge/任何文件修改
- 禁引用其它 auditor 产物
- 禁裸措辞 PASS/DONE/OK/works
- 禁把 4 项已锁事实当问题重新审

## 你的核心目标
找 Codex silent flexibility（Charter A/B/C/D/E/F/I 都聚焦此）。
不给 Codex 留情面，但也别 over-reach 把已锁设计当问题。

开始动笔，输出完整 audit report。

<<<AUDIT END>>>
```

---

## 派单顺序

1. 跑 pre-flight `git push -u origin run3-4-audit-handoff`
2. 复制 `<<<AUDIT BEGIN>>>` ... `<<<AUDIT END>>>` 整段
3. 同时粘到 3 个云端窗口：
   - **Hermes**（visual / boundary 守护）
   - **GPT Pro web**（cross-PR 一致性 / charter scope 较真）
   - **Codex CLI fresh window**（工程纪律 / state machine / 接口契约）
4. 收齐 3 份 audit report 后三角对比

## 三角验证决策

| 三角结果 | 决策 |
|---|---|
| 3 V-PASS | 直启 Run-5 (PF-C4) 或 PF-V handoff lane |
| 2 V-PASS + 1 V-PASS_WITH_AMENDMENTS | 看 amendment 同源否；若是 → 修补再启 Run-5 |
| 任一 REJECT | block + 走 amendment 路径（沿用 Run-1/Run-2 amendment 模式） |
| ready_for_run_5 多数 yes_pending_pf_v_handoff | 等 PF-V P7 (image→HTML5) 完成再启 Run-5 |
