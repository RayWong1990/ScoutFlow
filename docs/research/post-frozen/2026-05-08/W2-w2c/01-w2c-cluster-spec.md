---
title: W2C PF-C4-02 真数据接线 Cluster Spec
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
deliverable_type: cluster_spec
sub_lanes: [W2C-1, W2C-2, W2C-3]
parent_master_spec_section: §8 (Capture Station UX 第二波 PF-C4-02 主菜)
---

# W2C PF-C4-02 真数据接线 Cluster Spec

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

# §0 Cluster Mission

W2C cluster 是 ScoutFlow Capture Station 第二波主菜：在 PR #243 已 land 的 13 surface 静态壳上，把 `captures.py` 与 `bridge/router.py` 的现有 route 接进 UI，补齐缺失 contract 的候选边界，并实施 13 surface × 5 态状态机 + capture-side 微交互 vocab。它不是 PRD-v3，不是 SRD-v3，不是 runtime approval，不是 migration approval，也不是 authority writeback；它只是一组 `candidate / not-authority` spec + dispatch pack，供 CC0/CC1 audit 后再派给 Codex Long Runner。

W2C 不跨窗吞掉 W2D memory graph、W2E overflow registry 或后续 W3/W6 runtime 解禁。它只处理 PF-C4-02：Stage 2-6 read-only / preview / disabled-state wiring，把“能看见、能理解、不能误点越界”作为本窗核心质量线。

# §1 Sub-lane 拆解

## §1.1 W2C-1: 接现有 route，不扩 route

目标是把现有 `captures.py` + `bridge/router.py` route 接进 13 surface：`/bridge/health` 进入全局 backend 状态条，`/bridge/vault/config` 进入 vault config card，`/captures/{id}/vault-preview` 进入 Vault Preview，`/captures/{id}/vault-commit` 只进入 dry-run / disabled UI，`/captures/discover` 与 `/captures/{id}/trust-trace` 进入 URL Bar / Trust Trace / Capture Scope 的数据链。边界是：不新增 backend runtime，不调用 BBDown live / yt-dlp / ffmpeg / ASR，不让 vault commit 成为 true write。

输入包以 GitHub raw 为准：`bridge/router.py`、`bridge/config.py`、`bridge/schemas.py`、`captures.py`、`models.py`、`apps/capture-station/src/features/*` 13 surface 静态壳、`apps/capture-station/src/lib/api-client.ts`。W2C-1 的验收重点是“route wrapper 存在 + UI 诚实表达 route 状态 + response shape 不漂”。

## §1.2 W2C-2: 补缺失 contract，只补候选，不偷开

目标是把 master spec §8.1 的 13 surface 与现有 endpoint 逐格对齐，明确哪些 surface 只有静态壳、哪些能真接 existing route、哪些必须 future-gated。重点缺口集中在 Topic Card Preview、Topic Card Vault 的 topic-card DTO、Signal Hypothesis 的 hypothesis DTO、Capture Plan 的 plan DTO、Live Metadata 的 metadata readback DTO 以及 Trust Trace error-path 的 graph 算法依赖。

边界是：缺失 endpoint 不在 W2C 中硬造 runtime；可以写 contract draft、TODO placeholder、disabled badge copy、fixture shape 与 negative tests，但不得改 Trust Trace DTO 字段名 / shape，不得改 `PlatformResult` enum，不得改 `WorkerReceipt` schema，不得打开 dbvnext migration lane。

## §1.3 W2C-3: 状态机 + 微交互 vocab

目标是把 `loading / loaded / empty / error / disabled` 五态落实到 13 surface，并把 motion 约束为 capture-side-only 的 6 类 CSS Variables vocab：loading pulse、route badge fade、surface focus ring、disabled hover tooltip、error shake-lite、success settle。这里的“CSS Variables”是 contract 表述，不是本文件写真 CSS。

边界是：motion 不渗透 wiki / reading surface；tokens.css 外不硬编码 hex；不引 shadcn / Radix / TanStack / React Flow / Zustand / framer-motion 等整套 vendored UI；状态机仅描述 UI 行为与验收，不在本 spec 写真实 .tsx / .css 实现。

# §2 状态机 spec

## §2.1 13 surface × 5 态矩阵

| Surface | loading | loaded | empty | error | disabled |
|---|---|---|---|---|---|
| App Shell | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| URL Bar | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Live Metadata | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Capture Scope | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Trust Trace | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Vault Preview | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Vault Commit | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | 按钮可见但不可点击；blocked badge 指向 write_enabled=False + 5 overflow Hold |
| Topic Card Preview | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | future-gated badge；解释缺失 contract，显示下一波入口但不执行 |
| Topic Card Vault | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | route unavailable 或 governance gate 时展示 disabled copy，不隐藏 surface |
| Signal Hypothesis | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | future-gated badge；解释缺失 contract，显示下一波入口但不执行 |
| Capture Plan | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | future-gated badge；解释缺失 contract，显示下一波入口但不执行 |
| Density Spec | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | 静态规格保持可见；无数据 route 时标 reference-only |
| Type Spec | skeleton shimmer + route badge | 主数据/配置/状态完整显示 | 无 capture 或无结果时显示 honest empty | route 4xx/5xx/network 显示可读错误，不吞掉 | 静态规格保持可见；无数据 route 时标 reference-only |

## §2.2 5 态 transition 触发条件

| 触发 | 目标态 | 适用范围 | 说明 |
|---|---|---|---|
| route in-flight | `loading` | 所有有 route 的 surface | capture-id 切换时全 13 surface 先进入统一 reset/loading，避免旧 capture 数据残留 |
| 200 OK + 有业务数据 | `loaded` | read-only / preview / trust trace | response shape 必须匹配 Pydantic schema；DTO drift 进 error 而不是静默显示 |
| 200 OK + 空结果 | `empty` | topic-card / metadata / plan 等候选数据 | empty copy 必须说清“无结果”与“未实现”不是一回事 |
| 4xx / 5xx / network | `error` | route surface | 4xx 偏 user/action/capture-state，5xx 偏 backend/contract，network 偏连接；copy 分层 |
| `write_enabled=False` | `disabled` | vault-commit / true write / transcribe | disabled ≠ hidden；必须可见、不可点击、hover 给治理原因 |
| future-gated route | `disabled` | signal / plan / topic-card / transcribe | 显示 future-gated badge 与 TODO 指针；不自动发请求 |
| capture-id changed | reset → loading | 全 13 surface | 统一清旧数据；可保留非数据型 layout chrome |
| route wrapper missing | disabled / TODO | 对应 surface | 标 `<!-- TODO: contract gap, CC0 后续补 -->` |

## §2.3 disabled state 设计

1. `write_enabled=False` 时，所有写入动作都保持 visible-but-disabled：按钮变灰、`blocked` badge、governance tooltip 解释 5 overflow lane Hold：`true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench`。
2. Vault Commit 只能显示 dry-run contract 与 target preview；`committed` 必须为 false，`write_enabled` 必须是 false，UI 不允许出现“已写入 vault”的成功文案。
3. Transcribe / ASR / media download / browser automation 一律 disabled；可以显示“未来 route 需要单独 dispatch + user approval + audit”，但不能出现可点击执行按钮。
4. disabled 不等于 hidden。用户应能理解系统为什么不能点，而不是误以为功能消失或坏了。
5. 对 missing endpoint，copy 使用 `future-gated`，对 governance block，copy 使用 `blocked`，对网络失败，copy 使用 `retryable error`，三者不得混用。

<!-- TODO: Trust Trace error-path highlight 依赖 W1B PF-C4-EXT graph 算法，W2C 只保留 error-path placeholder，不强转图算法。 -->

# §3 DTO redlines

## §3.1 Trust Trace DTO 锁定

Trust Trace DTO 当前由 `services/api/scoutflow_api/models.py` 锁定为分层结构，不得 flatten。W2C dispatch 只能消费，不得改字段名 / shape。

| DTO 层 | 锁定字段 |
|---|---|
| `TrustTraceResponse` | `label / capture / capture_state / metadata_job / probe_evidence / receipt_ledger / media_audio / audit` |
| `TrustTraceCapture` | `capture_id / platform / platform_item_id / source_kind / capture_mode / created_by_path` |
| `TrustTraceCaptureState` | `capture_created / status` |
| `TrustTraceMetadataJob` | `present / job_id / job_type / status / platform_result` |
| `TrustTraceProbeEvidence` | `present / probe_mode / source_task_id / source_report_path / platform_result` |
| `TrustTraceReceiptLedger` | `present / artifact_count / artifact_kinds / redaction` |
| `TrustTraceMediaAudio` | `status / audio_transcript` |
| `TrustTraceAuditBlock` | `platform_result / evidence_file_path / artifact_count / redaction_policy / safe_parsed_fields` |

红线：不得把 `media_audio.audio_transcript` 从 blocked/not-approved 文案改成 runtime success；不得把 `probe_evidence` 当成 media/audio readiness；不得把 receipt ledger 与 capture state 合并成一个“成功”灯。

## §3.2 Bridge endpoint DTO 现状

| DTO | freeze 字段 | W2C 用法 | forbidden |
|---|---|---|---|
| `BridgeHealthResponse` | `bridge_available / spec_version / write_enabled / blocked_by` | backend 状态条 + route availability | UI 不得把 `write_enabled=False` 展示成 true |
| `BridgeVaultConfigResponse` | `vault_root_resolved / vault_root / preview_enabled / write_enabled / frontmatter_mode / error` | Vault Preview / Vault Commit config card | 不得暴露 credential / local secret；`frontmatter_mode` 仍是 `raw_4_field` |
| `BridgeFrontmatter` | `title / date / tags / status` | preview frontmatter block | 不扩成 PRD-v3 frontmatter |
| `BridgeVaultPreviewResponse` | `capture_id / target_path / frontmatter / body_markdown / warnings` | Vault Preview 主数据 | `target_path` 仅显示，不写入 |
| `BridgeVaultCommitResponse` | `capture_id / committed / dry_run / write_enabled / target_path / error` | Vault Commit disabled/dry-run | `write_enabled` literal false，不得出现 true leak |

## §3.3 缺失 contract 占位

| Surface | 缺口 | W2C 处理 | 后续路线 |
|---|---|---|---|
| Live Metadata | metadata readback route 不完整；现有 metadata-fetch job 是 enqueue，不等同 readback | 使用 Trust Trace / discover response 回填；缺口 TODO | 后续补 `GET /captures/{id}/metadata` 或 equivalent readback |
| Topic Card Preview | topic-card DTO 未锁 | 只写候选 DTO contract + fixture shape | 后续 topic-card API lane |
| Topic Card Vault | vault preview 与 topic-card vault copy 关系未锁 | 复用 vault-preview response，不改 Bridge DTO | 后续 topic-card-vault DTO |
| Signal Hypothesis | hypothesis route 缺失 | disabled placeholder + TODO | 后续 signal workbench lane，仍不解禁 full_signal_workbench |
| Capture Plan | plan route 缺失 | disabled placeholder + TODO | 后续 plan API lane |
| Trust Trace error-path | graph/path 算法缺 | 保留 TODO 与 error copy | W1B/PF-C4-EXT graph lane |
| Transcribe | ASR/runtime route blocked | 永远 disabled | 5 overflow 解禁后另立 dispatch |

# §4 Route contract

## §4.1 13 surface × Bridge/API mapping

| Surface | Route | Method | 撰写时刻状态 | §0.5 Check verify | UX 行为 |
|---|---|---|---|---|---|
| App Shell | `GET /bridge/health` | GET | ✅ existing | §0.5 refreshed | 真接线 |
| URL Bar | `POST /captures/discover` | POST | ✅ existing | §0.5 refreshed | 真接线 |
| Live Metadata | `POST /captures/{id}/metadata-fetch/jobs + Trust Trace readback` | POST | ⚠️ existing enqueue + readback gap | §0.5 refreshed | disabled / placeholder / TODO，不强转 runtime |
| Capture Scope | `GET /captures/{id}/trust-trace` | GET | ✅ existing | §0.5 refreshed | 真接线 |
| Trust Trace | `GET /captures/{id}/trust-trace` | GET | ✅ existing | §0.5 refreshed | 真接线 |
| Vault Preview | `GET /captures/{id}/vault-preview` | GET | ✅ existing | §0.5 refreshed | 真接线 |
| Vault Commit | `POST /captures/{id}/vault-commit dry-run only` | POST | ✅ existing | §0.5 refreshed | 真接线 |
| Topic Card Preview | `future-gated topic-card DTO placeholder` | N/A | ⚠️ partial/future-gated | §0.5 refreshed | disabled / placeholder / TODO，不强转 runtime |
| Topic Card Vault | `GET /captures/{id}/vault-preview + future topic-card DTO` | GET | ⚠️ partial/future-gated | §0.5 refreshed | disabled / placeholder / TODO，不强转 runtime |
| Signal Hypothesis | `future-gated signal contract placeholder` | N/A | ⚠️ partial/future-gated | §0.5 refreshed | disabled / placeholder / TODO，不强转 runtime |
| Capture Plan | `future-gated plan contract placeholder` | N/A | ⚠️ partial/future-gated | §0.5 refreshed | disabled / placeholder / TODO，不强转 runtime |
| Density Spec | `static token/readiness surface` | N/A | ✅ static spec surface | §0.5 refreshed | 真接线 |
| Type Spec | `static token/readiness surface` | N/A | ✅ static spec surface | §0.5 refreshed | 真接线 |

## §4.2 现有 4 Bridge endpoint 真接策略

- `/bridge/health`：全局 backend 状态条，反映 bridge availability、spec_version、blocked_by；不带 capture-id。
- `/bridge/vault/config`：Vault Preview / Vault Commit 共享 config card；`write_enabled=False` 时 Commit surface 自动 disabled。
- `/captures/{id}/vault-preview`：Vault Preview 主数据；503 时进入 error，而不是显示 fake markdown。
- `/captures/{id}/vault-commit`：只作为 dry-run contract；UI 默认 disabled，若 route 可返回，也只能展示 `dry_run=true` 与 `write_enabled=false`。

## §4.3 `captures.py` existing route 接线策略

- `/captures/discover`：URL Bar 的 LP-001 entrypoint。它是既有 bounded create path，不是 W2C 新增 runtime；W2C 只负责表单、错误态、capture-id handoff。
- `/captures/{id}/metadata-fetch/jobs`：只允许表达 queued/running/succeeded/failed 的 job state；不得执行 BBDown live，不得暗示 media/audio ready。
- `/captures/{id}/trust-trace`：Trust Trace / Capture Scope 的核心 readback；DTO 分层显示，绝不 flatten。

## §4.4 缺失 contract 占位策略

所有 missing endpoint 均使用同一个候选规则：UI 可见、route badge 写 `future-gated`、按钮 disabled、tooltip 写“需要后续 dispatch + audit + user gate”，并在 spec 中保留 `<!-- TODO: contract gap, CC0 后续补 -->`。W2C 不用 “temporary mock success” 盖住 contract gap。

# §5 5 维验收

## §5.1 T-PASS 技术存在

- 13 surface 都能从统一 state adapter 读到 `loading / loaded / empty / error / disabled`。
- Bridge 4 endpoint wrapper 存在，response shape 与 `BridgeXXXResponse` Pydantic schema 对齐。
- `TrustTraceResponse` 分层字段未改，UI 只消费。
- `write_enabled=False` 在 config + commit surface 双重生效。
- tokens.css 外不硬编码 hex，不引整套 vendored UI。

## §5.2 V-PASS 视觉接受

- 战友实际打开 Capture Station，逐个审 13 surface × 5 态。
- 重点审视觉层级、空间对齐、遮挡安全、字体可读、视觉重量。
- disabled tooltip 不能像错误，也不能像功能消失；error copy 不能像 governance block。
- motion 只出现在 capture-side workstation surface，不渗透 reading/wiki surface。

## §5.3 S-PASS 听感接受

W2C 无音频输出，S-PASS 标 `not_applicable`。任何 ASR / transcribe 声称都属于越界。

## §5.4 U-PASS 用户接受

- 用户从 URL Bar 创建 capture 后，能理解 capture-id 如何驱动 metadata / trust trace / vault preview。
- 用户能清楚知道为什么 Vault Commit 与 Transcribe 不能点。
- 用户能从 error/empty/disabled 三类文案区分“没数据”“接口坏”“治理禁止”。

## §5.5 verdict

| Verdict | 条件 |
|---|---|
| clear | T-PASS + V-PASS + U-PASS 均通过；无 DTO drift；无 overflow unlock |
| concern | 1-3 个非 critical 漏洞；可 amend_and_proceed |
| reject | 出现写入解禁、Trust Trace DTO 改、authority 文件误入 deliverable 写入清单、runtime/migration 越界 |


## §5.6 Acceptance packet 结构

W2C 交付给 CC0/CC1 的验收包建议分 5 类，不把任何一类单独当作终判：

| Packet | 内容 | 不构成 |
|---|---|---|
| route wiring evidence | wrapper 清单、route badge 截图、response shape 对照 | 不构成 backend runtime approval |
| state-machine evidence | 13 surface × 5 态 checklist、empty/error/disabled copy 截图 | 不构成 V-PASS 终判，仍需战友看 |
| DTO guard evidence | Trust Trace / Bridge DTO non-drift 检查、negative checklist | 不构成 schema migration approval |
| disabled evidence | Vault Commit / Transcribe / runtime buttons visible-but-disabled 截图 | 不构成 5 overflow lane 解禁 |
| closeout receipt | card result、amend trail、TODO、self-flag | 不构成 authority current truth |

验收顺序建议：先 T-PASS，再 V-PASS，再 U-PASS；S-PASS 固定 not_applicable。若 V-PASS 未跑，verdict 只能是 `concern` 或 `not_yet_verified`，不能写 `clear`。

## §5.7 W2C 不可用 “mock success” 兜底

W2C 的 UI 可以使用 fixture 展示 layout，但不能让 fixture 被误认为真实 route success。凡是 missing endpoint / future-gated route，必须带 `future-gated` 或 `TODO` badge；凡是 503 / not implemented，必须走 error 或 disabled copy；凡是 `write_enabled=False`，必须走 disabled copy。

允许的 placeholder：

| Placeholder | 允许条件 | 必须显示 |
|---|---|---|
| layout placeholder | 仅用于视觉骨架 | `placeholder` / `static shell` |
| future-gated placeholder | 缺 endpoint / 缺 DTO | `future-gated` + TODO |
| dry-run preview | Bridge commit route 返回 dry-run | `dry_run=true` + `write_enabled=false` |
| error placeholder | route 4xx/5xx/network | error code / human reason |

禁止的 placeholder：

| Placeholder | 禁止原因 |
|---|---|
| fake committed success | 会误导 true vault write 已解禁 |
| fake transcript success | 会误导 ASR/runtime 已解禁 |
| fake trust graph success | 会掩盖 W1B graph/path 依赖 |
| fake topic-card API success | 会掩盖 missing contract |


# §6 Cross-cutting boundaries

- 不把本 spec 写成 `current authority` 或 `promoted addendum`。
- 不把 PRD canonical 改成 PRD-v3，不把 SRD canonical 改成 SRD-v4 或错误的 promoted claim。
- 不解禁 `true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench`。
- 不改 `PlatformResult` enum、`WorkerReceipt` schema、Trust Trace DTO shape。
- 不把 Vault Commit / Transcribe 真接；必须 future-gated / disabled。
- 不引 shadcn / Radix / TanStack / React Flow / Zustand 等整套 vendored UI。
- 不在 tokens.css 外硬编码 hex。
- 不把 motion 扩散到 wiki / reading surface。
- 不把 research note / candidate docs 当 authority。


## §6.1 Hard redline matrix

| 红线 | W2C 允许 | W2C 禁止 | Audit 观察点 |
|---|---|---|---|
| Candidate vs authority | frontmatter 写 `status: candidate` | 写成 `current authority` / `promoted addendum` | grep frontmatter |
| Main HEAD | 标 live drift | 背 `c802de4` 当最新 | prereq receipt |
| Active slot | ≤3 product lanes | 提议 >3 | task-index readback |
| Authority writer | ≤1 writer | 多 writer 同改 ledger | LP-006 |
| Vault write | dry-run / disabled | true write / committed success | BridgeCommitResponse |
| Runtime tools | blocked copy | BBDown live / yt-dlp / ffmpeg / ASR | overflow hold |
| Migration | none | services/api/migrations 或 SQL runtime | dbvnext hold |
| Browser automation | none | Playwright/browser automation claim | runtime gate |
| DTO | consume only | Trust Trace / PlatformResult / WorkerReceipt 改 shape | schema diff |
| UI dependency | self-rolled + tokens | vendored UI/motion package | package manifest |
| Motion | capture-side only | wiki/reading surface motion | visual review |
| Color | token vars | tokens.css 外硬编码 hex | grep |
| Evidence | receipt + tests + screenshots | chat summary 替代 GitHub facts | LP-007 |
| Credential | none | cookie/token/auth sidecar tracked | LP-SEC-001 |

## §6.2 合法升级路径

W2C 遇到缺口时不要把“需要升级”误读为“永远禁止”。合法路径是：写 candidate gap → CC0/CC1 audit → user gate → 新 dispatch → 单独 PR → evidence → closeout。对 true vault write、runtime tools、browser automation、dbvnext migration、full signal workbench，必须另立 lane，不能借 W2C 的 UI 接线顺手开。

## §6.3 文案守则

- `blocked`：治理上禁止，通常对应 write_enabled=False / overflow hold。
- `future-gated`：contract 或 dispatch 尚未启动，未来可设计但现在不可点。
- `empty`：route 成功但没有业务数据。
- `error`：route 或网络失败，需要 retry / inspect。
- `static`：规格 surface，不承诺有 runtime data。

以上 5 类 copy 必须可被用户一眼区分；尤其 `blocked` 不要写成 `error`，否则用户会误以为重试即可突破治理 gate。


# §7 dispatch 拆分原则

- baseline 21 cards；上限 25，下限 18，再多就是 over-engineering。
- 每 card 目标 ≤ 1 PR diff；跨 feature dir 时必须解释为什么仍是单 feature。
- 每 card 必含 12 字段：`id / status / cluster / dependency / TL;DR / 输入包 / 输出 deliverable / 验收 / anti-patterns_REGENERATE / pre-flight check / self-verification / post-merge follow-up`。
- W2C-1 先跑 route wrapper，再跑 W2C-2 contract gap，最后跑 W2C-3 state/motion；可并行只限无共享写冲突的 docs/test card。
- amend_and_proceed：单 card amend trail ≤3；超过 3 或跨链依赖失败即 STOP-THE-LINE。
- dispatch pack 不包含 authority file deliverable 写入清单；authority writeback 只能由 CC1/Authority writer slot 单独开。

# §8 Self-flag

- ⚠️ `decision-log.md` 已拉取但云端 connector 展示被截断，D-017 follow-up 通过 PR #247 body 交叉确认；最新 decision-log tail 的精确行号留给 CC0/CC1 本地复核。
- ⚠️ W2C-2 缺失 endpoint 列表是从 master spec §8.1 + 当前 route 反推，可能漏掉已在其他 app lib 中定义但未暴露的 typed wrapper。
- ⚠️ `Live Metadata` 是否应由 `/captures/{id}/metadata` 还是 Trust Trace readback 承接，需要 CC0/CC1 对 `storage.py` 与 UI expectation 做二次审。
- ⚠️ Trust Trace error-path 高亮依赖 graph/path 算法，W2C 仅保留 placeholder，不能保证视觉细节最终足够。
- ⚠️ 21 cards 对 5-7h Codex 通宵是合理 baseline，但如果 CC1 判定共享组件太集中，建议拆成 2 run，而不是塞同一 PR。
