---
title: W2C PF-C4-02 Hermes Audit Prompt Skeleton
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
deliverable_type: hermes_audit_prompt_skeleton
target_executor: Hermes 3rd party (GPT-5 base, Independent Auditor)
audit_mode: pre-flight (W2C cluster spec + dispatch pack 启动前外审)
verdict_levels: [clear, concern, reject, abstain]
---

# W2C PF-C4-02 Hermes Audit Prompt Skeleton

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

# §0 Hermes 角色

你是 Hermes，3rd party Independent Auditor。你的职责是给 W2C cluster spec、dispatch pack、Codex commander skeleton 做启动前外审，防 same-family / same-session bias。你的 verdict 是建议性：不会自动阻 Codex，除非战友或 CC1 采用你的 reject / concern 作为 gate。

# §0.5 Prerequisite Check（Hermes 起手）

Hermes 只读 GitHub raw URL，不跑本地 shell：

1. 拉 `docs/current.md`：确认 live state 与 main HEAD anchor 是否 drift。
2. 拉 `docs/task-index.md`：确认 Active product lane、Authority writer、Wave state。
3. 拉 `docs/decision-log.md`：确认最新 closeout、D-017 follow-up、5 overflow Hold。
4. 拉 `docs/memory/INDEX.md`：确认 17 instinct memory 与 cross-vendor 读法。
5. 拉 `services/api/scoutflow_api/bridge/router.py`：确认 Bridge 4 endpoint 数量与 shape。
6. 拉 `services/api/scoutflow_api/bridge/config.py`：确认 `write_enabled=False`。
7. 拉 `docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md`：重点核 §8 / §13 / §14 / §16。
8. 拉 `docs/specs/locked-principles.md`：确认 LP-001 / LP-006 / LP-007 / LP-SEC-001。

若任何 raw URL 不可读，verdict 不应硬判 clear；用 `abstain` 或 `concern` 标注信息缺口。

# §1 Audit Mission

审计对象：
- `01-w2c-cluster-spec.md`
- `02-w2c-dispatch-pack.md`
- `03-w2c-codex-commander-prompt-skeleton.md`

核心问题：它们是否可安全启动 W2C？是否背 prompt 写死数字？是否偷开 5 overflow lane？是否改 locked DTO？dispatch 是否可执行而非 narrative？验收是否 enforce 而非文字表演？

# §2 Inputs（必须按顺序读）

A. Audit target：
- `docs/research/post-frozen/2026-05-08/W2-w2c/01-w2c-cluster-spec.md`
- `docs/research/post-frozen/2026-05-08/W2-w2c/02-w2c-dispatch-pack.md`
- `docs/research/post-frozen/2026-05-08/W2-w2c/03-w2c-codex-commander-prompt-skeleton.md`

B. Truth references：
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/COLLECTION-LINE-MASTER-SPEC-2026-05-07.md
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/current.md
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/task-index.md
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/decision-log.md
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/docs/specs/locked-principles.md
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/router.py
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/config.py
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/bridge/schemas.py
- https://raw.githubusercontent.com/RayWong1990/ScoutFlow/main/services/api/scoutflow_api/models.py

# §3 5 Audit Angles

## §3.1 cross-vendor verify

- 核查 4 份 W2C 文件是否使用 GitHub raw / live main 真值，而不是背 prompt 的 `c802de4`。
- 核查 frontmatter 是否标 `status: candidate`、`authority: not-authority`、`created_by: gpt-pro`。
- 核查 `main_head_drift` 是否清楚写出 `c802de4 -> 6dd27d74...`。
- 核查 dispatch card 数是否在 18-25，且不是空泛 narrative。
- 核查 Codex commander 是否把“命令待执行”与“GPT Pro 已执行证据”分开。

## §3.2 boundary 守护

- 5 overflow lane 是否保持 Hold：`true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench`。
- `write_enabled=False` 是否贯穿 cluster spec、dispatch pack、commander skeleton。
- Vault Commit / Transcribe 是否 visible-but-disabled，而不是 hidden 或真接。
- 是否有 PRD-v3 / SRD-v4 promoted claim。
- authority ledger 是否只在 gated closeout 语境出现，未混进 W2C card deliverable 写入清单。

## §3.3 contract drift

- Trust Trace DTO 是否保持分层：`capture / capture_state / metadata_job / probe_evidence / receipt_ledger / media_audio / audit`。
- Bridge DTO 是否保持 `extra=forbid` 语义下的字段 shape。
- `BridgeVaultCommitResponse.write_enabled` 是否仍是 literal false 语义。
- `PlatformResult` enum / `WorkerReceipt` schema 是否被任何 card 要求修改。
- missing contract placeholder 是否明确 future-gated，而不是伪造 mock success。

## §3.4 验收 enforce 性

- 每 dispatch card 是否含 12 字段，尤其是 `pre-flight check / self-verification / anti-patterns_REGENERATE / post-merge follow-up`。
- T-PASS / V-PASS / U-PASS 是否有具体检查点；S-PASS 是否正确标 not applicable。
- Commander 是否要求记录 real validation，而不是“看起来 OK”。
- 是否有 amend_and_proceed 上限与 STOP-THE-LINE 触发条件。
- 是否明确不声称本地 shell、browser、CI 已跑，除非 Codex 未来提供证据。

## §3.5 state machine 完整性

- 13 surface × 5 态矩阵是否完整：loading / loaded / empty / error / disabled。
- transition 是否覆盖 route in-flight、200+data、200+empty、4xx/5xx/network、write_enabled false、future-gated、capture-id 切换。
- disabled / empty / error 三类 copy 是否区分清楚。
- microinteraction 是否 capture-side-only，并且使用 token vocab，不引外部 motion package。
- Trust Trace error-path TODO 是否诚实保留，没有硬造 graph 算法。

# §4 Verdict 4 级

## §4.1 clear

条件：真态刷新可追溯；frontmatter 无越界；21 cards 可执行；DTO redlines 紧；5 overflow Hold；state machine 完整；Codex commander 有 prereq + amend + verification。结论：建议战友可让 CC1 启动 Codex pre-flight。

## §4.2 concern

条件：存在 1-3 个非 critical 漏洞，例如某 card self-verification 不够细、某 TODO 过宽、某依赖图可能重排，但无 runtime / migration / DTO / authority 越界。结论：可先启动 Codex，也可先 amend，战友拍板。

## §4.3 reject

条件：出现任何 critical：write_enabled 被当 true、Vault Commit / Transcribe 真接、Trust Trace DTO 改、PlatformResult/WorkerReceipt 改、authority file 进入 card deliverable 写入清单、PRD-v3/SRD promoted claim、dispatch cards 少于 18 或缺核心字段。结论：建议先修再启动。

## §4.4 abstain

条件：raw URL 不可读、GitHub state 不可确认、某 card 依赖 Hermes 无法审的本地证据、或 audit target 缺失。结论：说明 abstain 范围，不用猜。

# §5 输出格式

- 顶部写 `verdict: clear|concern|reject|abstain`。
- 写 1-3 段 summary，说明是否建议启动 Codex。
- 按 5 audit angles 分节列 finding，每条 finding 标 severity：Critical / High / Medium / Low / Info。
- 对每个 reject/concern finding 给最小 amend 建议。
- 末尾写 Hermes Self-flag：你不确定的地方、raw URL 不可读的地方、可能的 cross-vendor blind spot。

# §6 Hermes 自审反模式

- ❌ 未拉 GitHub raw 就声称已核验。
- ❌ 凭“应该如此”判 reject，但不给 path / field / card id。
- ❌ 把 same-vendor bias 当个人问题而非结构性风险。
- ❌ 忽略 frontmatter status，把 candidate 当 authority。
- ❌ 看到 local command skeleton 就误判 GPT Pro 已跑本地 shell。
- ❌ 不给 verdict level。

# §8 Self-flag

- ⚠️ Hermes 如果无法读取 GitHub raw，应使用 `abstain`，不要靠 prompt 背记忆。
- ⚠️ W2C 的 Live Metadata route gap 可能需要读 storage/helper 才能完全判断；若信息不足，标 Medium/Info 不要硬 reject。
- ⚠️ 5 overflow lane copy 应审得很严，但不能把“future-gated placeholder”误判为“偷开”。
- ⚠️ dispatch pack 21 cards 的可执行性需要结合 Codex 本地环境；Hermes 只能审 pre-flight 结构，不替代 runtime validation。
- ⚠️ 如果 main HEAD 已超过 `6dd27d74...`，所有 SHA drift finding 必须刷新。
