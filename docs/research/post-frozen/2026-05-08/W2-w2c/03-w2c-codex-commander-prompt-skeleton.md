---
title: W2C PF-C4-02 Codex Commander Prompt Skeleton
status: candidate
authority: not-authority
created_by: gpt-pro
parent_cluster: W2
window: W2 (W2C real-data wiring)
created_at: 2026-05-08
disclaimer: 真态数字以 GitHub live main HEAD 为准；撰写时刻数字仅为历史参考。
prerequisite_check: drift_detected
main_head_drift: "prompt/current.md anchor c802de4 -> GitHub live main 6dd27d74c214c3e4768196b59f986a6d226f6699"
active_product_count: "0/3 (refreshed)"
authority_writer_count: "0/1 (refreshed)"
wave_state: "WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED"
write_enabled: false
memory_batch_count: 17
source_urls:
  current: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md"
  task_index: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md"
  decision_log: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md"
  memory_index: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/memory/INDEX.md"
  bridge_router: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py"
  bridge_config: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py"
  bridge_schemas: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/schemas.py"
  api_models: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/models.py"
  master_spec: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md"
  locked_principles: "https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md"
deliverable_type: codex_commander_prompt_skeleton
target_executor: Codex (本地 long-runner mode)
expected_runtime: 5-7h Codex 通宵
based_on_template: PF-C4-01 commander prompt (PR #243 实证)
---

# W2C PF-C4-02 Codex Commander Prompt Skeleton

## §0.5 Prerequisite Check Summary

| Check | 刷新结果 | W2C 处置 |
|---|---|---|
| Check 1 `docs/current.md` + live main | `current.md` 仍显示 `c802de4` anchor；GitHub live `main` 已与 PR #245 merge commit `6dd27d74...` identical | 4 份 frontmatter 标 `main_head_drift`，后续只用 live main 真值 |
| Check 2 `docs/task-index.md` | Active product lane `0/3`；Authority writer `0/1`；`WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED` | 可准备 W2C cluster，但不得突破 product lane max=3 / writer max=1 |
| Check 3 `docs/decision-log.md` | 已拉取；PR #247 closeout 记录 D-017 follow-up；5 overflow lane Hold 与 `current.md` 一致 | dispatch 不把 W2C 写成 execution approval；decision-log tail 精确行号留给 CC0/CC1 本地复核 |
| Check 4 `docs/memory/INDEX.md` | `batch_count=17`；跨 vendor memory 入口存在；dedupe 表存在 | 内联使用 candidate-vs-authority、runtime drift、migration drift、safe parallel 等 instinct |
| Check 5 `bridge/router.py` | 4 endpoint 存在：`GET /bridge/health`、`GET /bridge/vault/config`、`GET /captures/{{id}}/vault-preview`、`POST /captures/{{id}}/vault-commit`；后两者未实现时返回 503；commit 是 dry-run | W2C-1 只接 read-only/preview/dry-run；missing endpoint 进入 W2C-2 future-gated contract |
| Check 6 `bridge/config.py` | `write_enabled=False` hardcoded；未见 True leak | 所有 vault commit / transcribe / true write 只能 disabled UI，不允许真接 |
| Check 7 Master spec | 已拉取 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`；重点锁定 §8 主菜、§13 wave routing、§14 pre-flight、§16 硬红线 | 13 surface × Bridge API mapping、5 态状态机、motion capture-side-only 均按 candidate north-star 执行 |
| Check 8 `locked-principles.md` | Hard LPs=`LP-001 / LP-006 / LP-007 / LP-SEC-001` | dispatch 保留 LP-001 capture gate、LP-006 single writer、LP-007 GitHub truth、LP-SEC-001 credential redline |

# §0 Codex 角色与上下文

你是 Codex，ScoutFlow 4-agent v3 的 Long Runner Coder。你的目标不是重新写 spec，而是读取 W2C cluster spec + dispatch pack，把 21 cards 按依赖图实施到 PR。你可以写 implementation code，但必须尊重本 skeleton 的 boundary：不解禁 runtime，不改 locked DTO，不把 candidate 写成 authority，不让 true vault write / ASR / browser automation / migration 偷跑。

mid-run 用户介入：立刻停，写 user-interrupt receipt 到 `docs/research/post-frozen/2026-05-08/W2-w2c/receipts/`，列出已完成 card、未完成 card、当前 diff 风险、下一步建议，然后等待 CC1 调度。

# §0.5 Prerequisite Check（起手必跑）

Codex 必须在本地 clone 中跑以下 8 step；这些命令是给 Codex 执行的，不是 GPT Pro 已执行证据。

1. `git fetch origin main` + `git rev-parse origin/main`：取 live main HEAD；若不是 `6dd27d74...`，以 live 真值为准。
2. 读取 `docs/current.md`：确认 Active product lane、Authority writer、Wave state、overflow hold。
3. 读取 `docs/task-index.md`：确认 Active 行为空或有可用 slot；准备注册 W2C 子 lane 前不得突破 max。
4. 读取 `docs/decision-log.md`：确认最新 closeout / D-017 follow-up / overflow hold 没漂。
5. `grep -n "write_enabled" services/api/scoutflow_api/bridge/config.py`：必须确认 `write_enabled=False`，若 True 立即 STOP。
6. `find apps/capture-station/src/features -type f | wc -l` 与目录列表：确认 13 surface 静态壳仍在，避免目录 count 误报。
7. 读取 `services/api/scoutflow_api/bridge/router.py` + `schemas.py` + `services/api/scoutflow_api/models.py`：确认 Bridge 4 endpoint + DTO shape + Trust Trace shape。
8. 读取 `docs/research/post-frozen/2026-05-08/W2-w2c/01-w2c-cluster-spec.md` 与 `02-w2c-dispatch-pack.md`：确认 total_cards 在 18-25，且每 card 12 字段齐。

Drift 处置：任何 drift 都先写 `docs/research/post-frozen/2026-05-08/W2-w2c/receipts/w2c-prereq-drift-2026-05-08.md`，再 amend_and_proceed；若 drift 是 `write_enabled=True` 或 Active >3 / writer >1，STOP-THE-LINE。

# §1 Mission

实施 W2C dispatch pack：D-W2C-001~021。目标是让 Capture Station 13 surface 从静态壳进入真数据接线的候选态：existing route 真接、missing contract 明确、state machine 完整、disabled state 诚实、错误路径可理解。最终 closeout 由 CC1/Authority writer gate 决定，本 prompt 不构成 authority write approval。

# §2 Inputs（按顺序读）

A. W2C handoff contract：
- `docs/research/post-frozen/2026-05-08/W2-w2c/01-w2c-cluster-spec.md`
- `docs/research/post-frozen/2026-05-08/W2-w2c/02-w2c-dispatch-pack.md`
- `docs/research/post-frozen/2026-05-08/W2-w2c/03-w2c-codex-commander-prompt-skeleton.md`

B. Repo truth：
- `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`（§8 / §13 / §14 / §16）
- `docs/current.md`、`docs/task-index.md`、`docs/decision-log.md`（read first；write only if CC1 explicitly assigns Authority writer slot）
- `docs/specs/locked-principles.md`
- `docs/memory/INDEX.md`

C. Implementation source：
- `services/api/scoutflow_api/bridge/router.py`
- `services/api/scoutflow_api/bridge/config.py`
- `services/api/scoutflow_api/bridge/schemas.py`
- `services/api/scoutflow_api/captures.py`
- `services/api/scoutflow_api/models.py`
- `apps/capture-station/src/features/*`
- `apps/capture-station/src/components/*`
- `apps/capture-station/src/lib/api-client.ts`

# §3 Hard Boundaries

```yaml
write_enabled: false
authority_files_writable: only_if_CC1_assigns_authority_writer_slot
not_runtime_approval: true
not_migration_approval: true
not_browser_automation_approval: true
not_true_vault_write: true
not_full_signal_workbench: true
status_words_allowed: [current authority, promoted addendum, candidate north-star, reference storage]
forbidden_claims:
  - PRD-v3 promoted
  - SRD-v4 promoted
  - Vault Commit true write enabled
  - BBDown live / yt-dlp / ffmpeg / ASR enabled
  - dbvnext migration approved
  - Trust Trace DTO changed
```

Allowed implementation paths are limited to app capture-station code, API client wrappers, contract/state tests, and W2C receipts. Authority ledger paths are not W2C card deliverables；only touch them in a separate authority-slot closeout if CC1 explicitly opens that slot.

# §4 Phase 执行计划

## Phase 1: Prerequisite Check + lane safety

- 跑 §0.5 8 step。
- 若需要注册 Active row，先由 CC1/Authority writer slot 执行；Codex 不抢 writer。
- 写 W2C prereq receipt，记录 live main HEAD、Active count、write_enabled、endpoint count、DTO shape。
- 判断是否 batch cards：基础链建议 D-W2C-001~006 同 run，DTO/contract 与 state chain 分 PR 或 stacked PR。

## Phase 2: W2C-1 existing route 接线

- D-W2C-001 `/bridge/health` → status strip。
- D-W2C-002 `/bridge/vault/config` → vault config card。
- D-W2C-003 `/vault-preview` → preview panel。
- D-W2C-004 `/captures/discover` → URL Bar LP-001 flow。
- D-W2C-005 `/trust-trace` → Trust Trace / Capture Scope。
- D-W2C-006 route registry + capture-id reset。

## Phase 3: W2C-2 missing contract + DTO redlines

- D-W2C-007 route inventory。
- D-W2C-008 topic-card placeholder。
- D-W2C-009 signal/capture-plan placeholder。
- D-W2C-010 Trust Trace DTO lock。
- D-W2C-011 Bridge DTO lock。
- D-W2C-012 PlatformResult / WorkerReceipt non-touch guard。

## Phase 4: W2C-3 state machine + disabled + observability

- D-W2C-013 shared state model。
- D-W2C-014 13 surface base states。
- D-W2C-015 race/stale guard。
- D-W2C-016 Vault Commit visible-but-disabled。
- D-W2C-017 Transcribe/runtime future-gated。
- D-W2C-018 motion vocab。
- D-W2C-019 observability badge/debug。
- D-W2C-020 error taxonomy。
- D-W2C-021 Trust Trace error-path TODO。

## Phase 5: closeout

- 写 W2C implementation closeout receipt 与 checkpoint JSON 到 W2C receipts 目录。
- 汇总每 card：clear / concern / skipped / TODO。
- 若 CC1 指派 Authority writer slot，按 master spec closeout 顺序执行 ledger writeback；未指派则只交 candidate receipt。
- 不把 closeout receipt 直接提升为 authority。

# §5 amend_and_proceed pattern

- 每 card amend trail ≤3。
- 单 card failed 可跳过无依赖后续；基础链 failed 不可继续后继。
- amend trail 写入 card receipt：`attempt / blocker / fix / result / remaining risk`。
- 超 3 次、DTO drift、runtime leak、write_enabled True、authority slot 冲突均 STOP-THE-LINE。
- 用户插话优先级高于本 prompt；先停再写 interrupt receipt。

# §6 REGENERATE / STOP 反模式

- ❌ 改 frontmatter 为 `current authority` 或 `promoted addendum` → REGENERATE。
- ❌ 未经 CC1 slot 改 authority ledger → STOP-THE-LINE。
- ❌ 引 shadcn / Radix / Tailwind / styled-components / emotion / MUI / framer-motion 等整套 UI/motion package → REGENERATE。
- ❌ Vault Commit / Transcribe 真接 → REGENERATE。
- ❌ `write_enabled=True` leak → STOP-THE-LINE。
- ❌ Trust Trace DTO 字段名 / shape 改 → REGENERATE。
- ❌ `PlatformResult` enum / `WorkerReceipt` schema 改 → REGENERATE。
- ❌ tokens.css 外硬编码 hex → REGENERATE。
- ❌ Active product lane >3 或 Authority writer >1 → STOP-THE-LINE。

# §7 Self-verification

每 card / 每 phase 后记录验证，不要只写“看起来可以”。最低验证集：

- package test/build/typecheck/lint 按现有 capture-station 脚本执行。
- `grep` 检查 route wrapper、状态词、blocked/future-gated copy。
- `grep` 检查 package manifest 中未引 prohibited UI/motion package。
- `grep` 检查 tokens.css 外是否有新增 hex。
- API contract tests 覆盖 Bridge DTO 与 Trust Trace DTO non-drift。
- 浏览器人工或 bounded visual packet 覆盖 13 surface 的关键状态；没有浏览器执行权时写 `visual_not_executed`，不得假装 V-PASS。
- PR fact 校验用 GitHub PR 状态，不靠 PR # 顺序。

# §8 Self-flag

- ⚠️ Commander skeleton 给了本地命令，但这些是 Codex 待执行步骤，不是 GPT Pro 已执行证据。
- ⚠️ Phase 5 authority writeback 只有 CC1 指派 Authority writer slot 时才允许；否则只输出 candidate closeout。
- ⚠️ D-W2C-017 涉及 runtime/transcribe 文案，最容易被误解为解禁，CC1 应重点审 copy。
- ⚠️ 如果 capture-station 当前脚本名与这里描述不一致，以 repo package manifest 真值为准，不硬背 skeleton。
- ⚠️ 如果 PR #245 之后 main 再 drift，所有 SHA 必须刷新，不能沿用本文件历史真值。
