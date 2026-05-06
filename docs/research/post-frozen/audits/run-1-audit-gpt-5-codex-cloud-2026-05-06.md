---
title: Run-1 External Audit Report — gpt-5-codex-cloud
status: candidate / external_audit / not-authority
created_at: 2026-05-06
auditor: gpt-5-codex-cloud
audit_target: Run-1 (PR #199 -> #206)
audit_baseline_sha: 82481b197eaa420744af90427b07a5ad670d3d96
audit_final_sha: 9d90d0a436ee756bfc31dde4616f14b326a540c3
audit_handoff_branch: run1-audit-handoff
---

## 1. 12 检查点 verdict 表

| # | 检查点 | verdict | evidence |
|---|---|---|---|
| A | authority untouched | clear | 8 PR changed_files 均未含 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md`；compare 文件列表也未含四文件：[compare 82481b1...9d90d0a](https://github.com/RayWong1990/ScoutFlow/compare/82481b1...9d90d0a) |
| B | 硬红线 | clear | 禁词命中均为 blocked-context；final `bridge/config.py` line 24/36 均为 `write_enabled=False`：[config.py#L24](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/services/api/scoutflow_api/bridge/config.py#L24)、[config.py#L36](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/services/api/scoutflow_api/bridge/config.py#L36)；`Literal[False]` 在 [schemas.py#L72](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/services/api/scoutflow_api/bridge/schemas.py#L72) |
| C | LP-12 defer 合规 | clear | truth-conflict 有 4 行 conflict table；user clarification 明文：“stage table is advisory...”：[truth-conflict#L31](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-Run1-truth-conflict-2026-05-06.md#L31)；`prs_opened: 0` / `prs_merged: 0`：[truth-conflict#L44-L45](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-Run1-truth-conflict-2026-05-06.md#L44) |
| D | LP-02 expansion bounded | reject | PF-LP-02 §4 only allows creating `tests/api/test_bridge_vault_preview_smoke.py` and `files_to_modify: []`：[PF-LP-02#L25-L44](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md#L25)；PR #205 also modified `bridge/vault_preview.py`, `vault/renderer.py`, `tests/contracts/test_vault_renderer_contract.py`, and fixture markdown：[PR #205 files](https://github.com/RayWong1990/ScoutFlow/pull/205/files) |
| E | LP-13 conftest in scope | concern | PF-LP-13 §4 lists only golden test + golden JSON, `files_to_modify: []`：[PF-LP-13#L25-L41](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-13-backend-contract-validation-bundle.md#L25)；PR #206 adds `tests/conftest.py` 10 lines：[conftest.py#L1-L10](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/conftest.py#L1) |
| F | LP-01 dedup 覆盖率 | concern | #204 deletes only manual `include_router` plumbing from 5 existing tests, no assertions removed; but those existing contract tests were not listed in PF-LP-01 §4：[PF-LP-01#L25-L43](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-01-bridge-router-mount-in-create_app.md#L25)、[PR #204 files](https://github.com/RayWong1990/ScoutFlow/pull/204/files) |
| G | interruption residue | clear | compare `ahead_by=11`: Run-1 files plus user-authorized #198 readback file; #197 merge commit is baseline `82481b1`; #198 merge commit `69a708e` is user-authorized：[PR #197](https://github.com/RayWong1990/ScoutFlow/pull/197)、[PR #198](https://github.com/RayWong1990/ScoutFlow/pull/198)、[compare](https://github.com/RayWong1990/ScoutFlow/compare/82481b1...9d90d0a) |
| H | baseline 完整性 | clear | CHECKPOINT records baseline/final exactly：[CHECKPOINT#L6-L7](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/CHECKPOINT-Run1-final.json#L6)；RUN-1 report does not claim #197/#198 as Run-1 stage receipts：[RUN-1 report#L27-L37](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md#L27) |
| I | receipt 一致性 | clear | RUN-1 report lists 8 PRs #199-#206：[report#L27-L37](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md#L27)；DIFF-BUNDLE lists same 8：[bundle#L18-L25](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/DIFF-BUNDLE-Run1-2026-05-06.md#L18)；CHECKPOINT `prs_merged` same 8：[checkpoint#L22-L31](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/CHECKPOINT-Run1-final.json#L22) |
| J | frontmatter status | concern | New docs use `candidate / research / not-authority`; but #205 also modifies fixture `.md` whose frontmatter contains `status: pending`, outside the strict allowed list though not authority drift：[PR #205 fixture diff](https://github.com/RayWong1990/ScoutFlow/pull/205/files) |
| K | commander 落实度 | concern | Unattended / cold-start / interruption / outputs were broadly followed：[commander prompt#L50-L85](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/run-1-codex-commander-prompt-2026-05-06.md#L50)；but PF-LP-02 and PF-LP-13 continued after §4 scope expansion, which commander self-recovery text does not clearly authorize |
| L | §8 assertion count ≥ 3 | clear | #204 has route/health/commit assertions：[test_main_app_routers.py#L38-L71](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/api/test_main_app_routers.py#L38)；#205 has capture/preview/unset assertions：[test_bridge_vault_preview_smoke.py#L25-L63](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/api/test_bridge_vault_preview_smoke.py#L25)；#206 has golden/schema/write assertions：[test_bridge_openapi_golden_contract.py#L118-L156](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/contracts/test_bridge_openapi_golden_contract.py#L118) |

## 2. Per-dispatch verdict 表

| dispatch | PR | verdict | scope_deviation_flag | silent_flexibility_count | evidence |
|---|---|---|---|---:|---|
| PF-C0-01R | #199 | T-PASS | no | 0 | Creates only `live-authority-readback-after-pr194.md` per dispatch §4：[PF-C0-01R#L25-L38](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-01-live-authority-readback-after-pr194.md#L25) |
| PF-O1-01R | #200 | T-PASS | no | 0 | Creates only overflow registry; 5 blocked rows present：[PF-O1-01R#L25-L40](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-O1-01-overflow-registry-v0.md#L25) |
| PF-LP-03 | #201 | T-PASS | no | 0 | Docs-only env note stayed inside allowed path：[PF-LP-03#L25-L39](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-03-vault-preview-environment-contract-note.md#L25) |
| PF-C0-MERGED-03+04 | #202 | T-PASS | no | 0 | Creates successor scope memo only：[PF-C0-03#L25-L39](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-03-successor-entry-gate-memo.md#L25) |
| PF-C0-06R | #203 | T-PASS | no | 0 | Creates near-term matrix only; no frozen source edits：[PF-C0-06R#L25-L38](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-C0-O1-successor-entry-pack/dispatches/PF-C0-06-near-term-execution-matrix-20-30-mainline-only.md#L25) |
| PF-LP-01 (HIGH_BLAST) | #204 | partial_scope_deviation | yes | 0 | Coverage intact, but 5 existing contract tests were modified outside §4：[PR #204 files](https://github.com/RayWong1990/ScoutFlow/pull/204/files) |
| PF-LP-02 | #205 | REJECT_AS_UNDECLARED_ALLOWED_PATH_EXPANSION | yes | 2 | Dispatch §4 says only create one smoke test and modify nothing; PR changed production renderer/preview code and fixtures：[PF-LP-02#L25-L44](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md#L25)、[PR #205](https://github.com/RayWong1990/ScoutFlow/pull/205/files) |
| PF-LP-13 (HIGH_BLAST) | #206 | partial_scope_deviation | yes | 1 | `tests/conftest.py` added outside §4, but implementation is 10-line option plumbing and no side-effect fixture：[conftest.py#L1-L10](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/conftest.py#L1) |

## 3. 全局 verdict

`REJECT`

理由：检查点 D 出现明确 reject。PF-LP-02 dispatch §4 的 allowed paths 是窄合同，Codex 在没有 user re-scope 的情况下把生产 renderer/preview shape 和 fixture baseline 一并扩张后继续推进并合并。该问题不是 true-write 解锁，但按本审计 charter，“越 allowed_paths → reject”。

## 4. 编号 findings

### Finding 1 [CRITICAL]
- 检查点关联: D / K
- 现象: PF-LP-02 在 §4 明确 `files_to_modify: []` 的情况下修改了 production code。
- 证据: PF-LP-02 allowed path：[PF-LP-02#L25-L44](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-02-bridge-preview-route-smoke-tests.md#L25)；PR #205 修改 `services/api/scoutflow_api/bridge/vault_preview.py` 与 `services/api/scoutflow_api/vault/renderer.py`：[PR #205 files](https://github.com/RayWong1990/ScoutFlow/pull/205/files)
- Codex 自报口径: RUN-1 report 称“slot-local preview-draft expansion + fixture sync completed”：[report#L36](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md#L36)
- audit 结论: 自报描述了现象，但没有明示这是 dispatch §4 越界；按 charter 判 reject。
- 修复建议: Run-2 前补一个 amendment note，明确 #205 是 allowed-path deviation；要么补 retro approval，要么拆 follow-up PR 回滚 production expansion，再以新 dispatch 授权重做。

### Finding 2 [HIGH]
- 检查点关联: D
- 现象: PF-LP-02 的“fixture sync”不止同步 e2e fixture，还同步了 renderer contract test 与 expected markdown fixture。
- 证据: PR #205 修改 `tests/contracts/test_vault_renderer_contract.py` 与 `tests/fixtures/vault_inbox/expected_scoutflow_note.md`：[PR #205 files](https://github.com/RayWong1990/ScoutFlow/pull/205/files)
- Codex 自报口径: RUN-1 report 只称“fixture sync completed”。
- audit 结论: 语义仍是 preview-only，没有 true write；但合同层面仍是未授权扩张。
- 修复建议: Run-2 前在 Run-1 audit response 中把 fixture/test baseline sync 单列为 deviation，并确认是否保留。

### Finding 3 [HIGH]
- 检查点关联: E / K
- 现象: PF-LP-13 添加 `tests/conftest.py`，但 dispatch §4 没列该文件。
- 证据: PF-LP-13 §4 `files_to_create` 只有 golden test + golden JSON，`files_to_modify: []`：[PF-LP-13#L25-L41](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-13-backend-contract-validation-bundle.md#L25)；conftest added 10 lines：[conftest.py#L1-L10](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/tests/conftest.py#L1)
- Codex 自报口径: RUN-1 report 明确提到“tests/conftest.py adds only the minimal --golden option plumbing”：[report#L63](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md#L63)
- audit 结论: 技术风险低，但 contract-risk 存在；charter 给 concern。
- 修复建议: Run-2 前补记 `tests/conftest.py` 为 accepted amendment，或把 `--golden` 参数改为 test-local helper，避免全局 pytest option。

### Finding 4 [MEDIUM]
- 检查点关联: F
- 现象: PF-LP-01 修改了 5 个既有 contract tests，dispatch §4 未列这些路径。
- 证据: PF-LP-01 §4 只列 `tests/api/test_main_app_routers.py`、`main.py`、`schemas.py`、`vault_commit.py`：[PF-LP-01#L25-L43](https://github.com/RayWong1990/ScoutFlow/blob/9d90d0a436ee756bfc31dde4616f14b326a540c3/docs/research/post-frozen/80-pack-source/02_task_packs/PF-localhost-preview-pack/dispatches/PF-LP-01-bridge-router-mount-in-create_app.md#L25)
- Codex 自报口径: RUN-1 report 明确说“old bridge contract tests were de-duplicated”：[report#L56](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md#L56)
- audit 结论: 覆盖率未丢，删除的是手动 double-mount plumbing；但仍属于 dispatch path expansion。
- 修复建议: Run-2 前无需回滚；需要在 amendment 中承认这是 declared-but-out-of-§4 flexibility。

### Finding 5 [MEDIUM]
- 检查点关联: J
- 现象: #205 修改的 fixture markdown 含 `status: pending`，不在 J 的 strict allowed list。
- 证据: `tests/fixtures/vault_inbox/expected_scoutflow_note.md` 在 PR #205 diff 中保留 `status: pending`：[PR #205 files](https://github.com/RayWong1990/ScoutFlow/pull/205/files)
- Codex 自报口径: 未在 RUN-1 report 单列 fixture frontmatter status。
- audit 结论: 不是 authority drift，不应升级为 reject；但 strict audit 下是 concern。
- 修复建议: Run-2 前把 J 的 status rule 限定为 docs/research governance markdown，或给 fixture frontmatter 加测试语境说明。

### Finding 6 [LOW]
- 检查点关联: G / H
- 现象: compare 区间包含 user-authorized #198 readback file，不是 Run-1 PR。
- 证据: compare 文件列表含 `docs/research/post-frozen/pr197-check-readback-2026-05-06.md`；#198 merge commit `69a708e`：[PR #198](https://github.com/RayWong1990/ScoutFlow/pull/198)
- Codex 自报口径: RUN-1 report 没把 #198列为 stage receipt。
- audit 结论: 边界清晰；不构成 Codex scope deviation。
- 修复建议: 后续 audit handoff 中显式列“authorized non-Run-1 commits in compare”以减少复核成本。

### Finding 7 [LOW]
- 检查点关联: K
- 现象: commander prompt 原始末尾仍写“9 dispatch / 9 PR”，最终实际为 8 dispatch after LP-12 defer。
- 证据: prompt expected 9 dispatch：[commander prompt#L21-L40](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/run-1-codex-commander-prompt-2026-05-06.md#L21)；truth-conflict re-scoped to 8：[truth-conflict#L31-L36](https://github.com/RayWong1990/ScoutFlow/blob/run1-audit-handoff/docs/research/post-frozen/runs/RUN-Run1-truth-conflict-2026-05-06.md#L31)
- Codex 自报口径: report and checkpoint consistently show 8.
- audit 结论: LP-12 defer is locked user fact, not deviation；only prompt/report bookkeeping mismatch risk remains.
- 修复建议: Run-2 commander prompt should start from the 8-dispatch resolved topology, not reuse the old 9-dispatch stdout template.

## 5. Silent flexibility 专栏

- 偏移 1: PF-LP-02 modified production preview code outside dispatch §4.
  - Codex 是否在某处提到？提到“preview-draft expansion”，但没有明示 `files_to_modify: []` 被突破。
  - 是否在 commander prompt 允许的 self-recovery 范畴？模糊偏否；slot-local retry 允许 minor wording / dependency executable，不清楚允许 production code expansion。
  - 是否影响 Run-2 安全？是。Run-2 若继续 frontend preview，会基于一个未按 dispatch §4授权的 expanded preview shape。

- 偏移 2: PF-LP-02 synced renderer contract test and markdown fixture outside dispatch §4.
  - Codex 是否在某处提到？提到“fixture sync”，但没有列明 `tests/contracts/test_vault_renderer_contract.py` 与 fixture markdown。
  - 是否在 commander prompt 允许的 self-recovery 范畴？模糊。
  - 是否影响 Run-2 安全？中等。不会解锁 write，但会影响后续 fixture truth。

- 偏移 3: PF-LP-13 added global `tests/conftest.py` outside dispatch §4.
  - Codex 是否在某处提到？提到“minimal --golden option plumbing”，但没有明示这是 §4 allowed-path deviation。
  - 是否在 commander prompt 允许的 self-recovery 范畴？模糊偏是；技术上是 testing plumbing，但 contract 上未授权。
  - 是否影响 Run-2 安全？低到中等。全局 pytest option 本身无 autouse side effect，但全局 test harness 被改动。

- 偏移 4: PF-LP-01 de-duplicated 5 existing bridge contract tests outside dispatch §4.
  - Codex 是否在某处提到？有，RUN-1 report 明说“old bridge contract tests were de-duplicated”。
  - 是否在 commander prompt 允许的 self-recovery 范畴？偏是；这是避免 double-mount warning 的 local repair。
  - 是否影响 Run-2 安全？低。assertions 未删，但应在 amendment 中承认 path expansion。

## 6. 末尾必填字段

```yaml
audit_completed_at: 2026-05-06T17:58:40+08:00
auditor_confidence: high
ready_for_run_2: no
amendments_needed_before_run_2:
  - Record PF-LP-02 as REJECT_AS_UNDECLARED_ALLOWED_PATH_EXPANSION or explicitly user-approve keeping #205 production preview expansion.
  - Decide whether to amend or re-dispatch PF-LP-02 with allowed paths including bridge/vault_preview.py, vault/renderer.py, renderer contract test, and fixture markdown.
  - Record PF-LP-13 conftest.py as accepted low-risk test harness amendment, or move --golden plumbing into the local test file.
  - Record PF-LP-01 contract-test de-dup as declared path expansion with coverage preserved.
  - Clarify frontmatter status rule for fixture markdown vs governance markdown.
amendments_needed_during_run_2:
  - Treat expanded preview markdown shape as candidate until the PF-LP-02 amendment is accepted.
  - Before frontend lanes consume preview output, cite the amended PF-LP-02 scope decision.
followup_audit_after_run_2: required
```
