# ScoutFlow Task Index

> 共享薄账本。当前只服务 Step0 与 Phase 0 / 1A 开工安全，不承担重治理职能。
> 当前限制：活动任务仅允许 `1-3` 条；当前 Active count=`3/3`，Review count=`0`。

## 规则

- 当前只维护 Step0 / Phase 0 / Phase 1A 开工安全相关任务
- 任务状态变化时先写本文件，再更新 `docs/current.md`
- 外部研究统一落 `docs/research/`，不在项目根建立重治理目录
- 任何活动任务都必须写明 owner、scope、allowed paths、validation
- research note 不直接升级为 authority；draft spec 必须显式标记 `draft / not final authority / not runtime approval`

## 当前 Phase

`Phase 1A — metadata_only manual_url quick_capture contract`

## Active

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `T-P1A-010A` | BBDown executable discovery / tool preflight package | `active` | `Codex Desktop window A` | Tool path discovery, preflight result modeling, `BBDown --version` wrapper with mockable subprocess | `services/api/scoutflow_api/external_tools/**`, `tests/contracts/**`, `docs/research/**` status note if needed | `workers/**`, `apps/**`, `packages/**`, `data/**`, `referencerepo/**`, `dispatches/**`, `audits/**`; no URL, no `-info`, no auth, no media, no ffmpeg, no ASR, no receipt, no capture state | `C-BBD-001`, `C-PLT-001`, `C-SEC-001`, `C-OPS-001`, `C-OPS-003` | `python tools/check-docs-redlines.py`; `python tools/check-secrets-redlines.py`; `python -m pytest tests/contracts -q`; `git diff --check` | Any real BBDown execution, credential material, raw stdout/stderr persistence, or `executable_not_found` promoted to `PlatformResult` | Coding PR must not edit `docs/current.md` or `docs/task-index.md`; provide ledger status text in PR body |
| `T-P1A-010B` | BBDown no-auth `-info` adapter shell with injected runner and parser integration | `active` | `Codex Desktop window B` | Command builder and injected runner for no-auth `BBDown -info`; sanitized fixture and existing parser integration only | `services/api/scoutflow_api/external_tools/**`, `tests/contracts/**`, `tests/fixtures/bbdown/**`, `docs/research/**` status note if needed | `workers/**`, `apps/**`, `packages/**`, `data/**`, `referencerepo/**`, `dispatches/**`, `audits/**`; no real BBDown execution, no auth, no media, no receipt, no capture state | `C-BBD-001`, `C-PLT-001`, `C-SEC-001`, `C-OPS-001`, `C-OPS-003` | `python tools/check-docs-redlines.py`; `python tools/check-secrets-redlines.py`; `python -m pytest tests/contracts -q`; `python -m pytest tests/api tests/contracts -q`; `git diff --check` | Any real subprocess call, credential material, unredacted URL, raw response persistence, or parser output treated as runtime approval | Coding PR must not edit `docs/current.md` or `docs/task-index.md`; no `PlatformResult` emission from tool preflight |
| `T-P1A-010C` | PRD/SRD amendment repair pack + next dispatch plan + red-team checklist | `active` | `Opus / GPT / OpenClaw sidecar`; one docs writer only if user authorizes | PRD/SRD amendment repair pack, QR-auth separation rules, next dispatch plan, red-team checklist | `docs/PRD-v1.1-amendment-2026-05-02.md`, `docs/SRD-v1.1-amendment-2026-05-03.md`, `docs/specs/contracts-index.md`, `docs/research/**`, `docs/plans/**` only when explicitly authorized | Product code, runtime, `workers/**`, `apps/**`, `packages/**`, `data/**`, `referencerepo/**`, root `dispatches/**`, root `audits/**`; no authority override beyond draft amendments | `C-AUTH-001`, `C-SCOPE-001`, `C-PROC-001`, `C-BBD-001`, `C-OPS-001`, `C-OPS-003` | `python tools/check-docs-redlines.py`; `python tools/check-secrets-redlines.py`; `git diff --check` | Any draft amendment written as final authority, QR/auth material in tracked files, or Phase 2-4 runtime pulled into Phase 1A | Default sidecar is read-only; if one docs writer is authorized, it still must leave `docs/current.md` and `docs/task-index.md` to ledger owner |

## Review

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Backlog

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Blocked

| 任务 ID | 标题 | 阻塞原因 | 需要动作 | 时间 |
|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` |

## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P0-000` | Step0 Execution Plan + SRD 开工安全补丁（含 audit-fix） | `2026-05-03` | user 已批准作为后续实现候选基准 |
| `T-P0-001` | GitHub Bootstrap + Initial Repository Baseline | `2026-05-03` | initial=`22c2c2014b9d10f48a6a8fe11fc73f38ba1b0045`; second=`d1c12326450f5a92d8b0b6f32c0cac51f5f5ee5a`; remote=`https://github.com/RayWong1990/ScoutFlow.git`; private repo；无产品代码 |
| `T-P0-002` | 入口文档深化 + 并行执行协议固化 | `2026-05-03` | branch=`task/T-P0-002-parallel-execution-protocol`; commit=`ee1f4cfd34282e39be74afc20310ef7801ac4b25`; PR=`#1`; merge commit=`bafeb56c79c69a43f2806aaec88ea7014db36815`; workflow run=`25271451489`; docs-check=`success`; GPT Pro external audit=`COMMENT review, no blocking issue`; 无产品代码；未批准 Phase 1A 产品实现 |
| `T-P0-003` | 目录骨架 + 文档 lint stub + 入口文档同步 | `2026-05-03` | commit=`b32ae22edd7e60becc39d5d5d0bca8381b948254`; final close commit=`efe607dbafe3c398d582aaf0a0d5e9521ff2a814`; docs-check run=`25270586304`; 创建 docs redline lint stub；接入 GitHub Actions docs-check；同步 README / AGENTS / CLAUDE 入口口径；无产品代码 |
| `T-P0-004` | 通信测试清理与 ScoutFlow 主线恢复 | `2026-05-03` | GitHub queue / sync smoke / Codex adapter 探索按 user 决定暂停或关闭；`example/` 与 smoke-only `examples/` 移除；PR `#2` 与 Issue `#3/#4/#5` 关闭；无产品代码；未批准 Phase 1A 产品实现 |
| `T-P0-007` | Phase 1A Bilibili `manual_url` quick_capture readiness pack | `2026-05-03` | branch=`task/T-P0-007-phase1a-readiness`; reviewed commit=`40aa2f325bf5defe9fad9427fd0c8a006bf84436`; PR=`#6`; merge commit=`cc649030437dfab1ea52f062d454c1da789703c5`; workflow run=`25276308045`; docs-smoke=`success`; GPT Pro external audit=`PASS`; docs-only readiness planning；merged to `main`；`T-P1A-001` 已获 user 显式批准 |
| `T-P1A-001` | Bilibili `manual_url` quick_capture metadata contract | `2026-05-03` | branch=`task/T-P1A-001-manual-url-quick-capture`; reviewed head=`fda2203e54c014845b88fe332dea93471f501f89`; PR=`#7`; merge commit=`d826ce191d71f9ab21d4a45543b980da1d282293`; workflow run=`25277184277`; docs-smoke=`success`; api-contract-tests=`success`; merged to `main`; meaning=`metadata_only API-side capture creation baseline merged`; no workers / frontend / `audio_transcript` runtime |
| `T-P1A-002` | API jobs / receipt / artifact ledger foundation | `2026-05-03` | branch=`task/T-P1A-002-api-jobs-receipt-ledger`; reviewed head=`7e54ec0d0b1a8aae5fcd041b02a6f1f56ac28e97`; PR=`#9`; merge commit=`1449f0d753c2da1476178f99934cf66c3add372c`; workflow run=`25278781456`; docs-smoke=`success`; api-contract-tests=`success`; local audit-fix validation=`42 passed`; API-side only；no workers / ASR / frontend / `audio_transcript` runtime |
| `T-P1A-004` | Redaction / secret scan / CI hardening | `2026-05-03` | branch=`task/T-P1A-004-redaction-secret-scan-ci`; rebased head=`7c74233095c3c297d4634a7e342547830d77bf32`; PR=`#8`; merge commit=`4f6af1ce3d823c84fc8f38cefee0790ec1830c62`; workflow run=`25279195327`; docs-smoke=`success`; api-contract-tests=`success`; local validation=`25 passed` contracts / `50 passed` api+contracts；no workers / frontend / runtime capture |
| `T-P1A-003` | BBDown tool-surface research note | `2026-05-03` | PR=`#10`; head=`42baf4165d7bf9022a9e8742d989a7428ae3ee4b`; merge commit=`8328c567e26db118ad456b29f8616066174b3568`; GitHub run=`25280084928`; `docs-smoke=success`; `api-contract-tests=success`; scope=`docs/research/**` research note only；not authority；not implementation approval；no runtime |
| `T-P1A-005` | Human gate sync and PR #10 research merge | `2026-05-03` | branch=`task/T-P1A-005-human-gate-sync`; head=`e10c9fc3808668fd34b6dc2150db151186640743`; PR=`#12`; merge commit=`419546de000f4a163d4158f2ced9784ba263c09c`; workflow run=`25280435814`; docs-smoke=`success`; api-contract-tests=`success`; scope=`AGENTS.md`, `README.md`, `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `docs/specs/contracts-index.md`; no runtime approval |
| `T-P1A-006` | BBDown adapter contract draft | `2026-05-03` | PR=`#14`; head=`ef5deba11f12d359bec61564a5bef1c9962037c8`; merge commit=`014e37a11427922c52d35b56c3962110d3711d17`; workflow run=`25280751608`; docs-smoke=`success`; api-contract-tests=`success`; merged draft on `main` only；not final authority；not runtime approval |
| `T-P1A-007` | Explore URL UX / risk / receipt status brainstorm | `2026-05-03` | PR=`#15`; head=`8271a43e88765f8214a303d98df863e1d7ea7f94`; merge commit=`e9b4d1bb5bae0d79ead0b9bb6f60304f3a560abe`; workflow run=`25282020291`; docs-smoke=`success`; api-contract-tests=`success`; merged research note / decision pack only；no frontend / API / runtime approval |
| `T-P1A-008` | BBDown sanitized fixture parser | `2026-05-03` | PR=`#17`; head=`4e1aa6f13efc9f67f29964aa16da967cd553d84d`; merge commit=`0cfcef58533bba1902eec6ed19a3f7fbed308a64`; workflow run=`25282572121`; docs-smoke=`success`; api-contract-tests=`success`; fixture-only parser / classifier baseline merged；no live BBDown / real Bilibili URL / download / ffmpeg / ASR / workers |
| `T-P1A-009` | BBDown local runtime spike | `2026-05-03` | PR=`#19`; head=`8d702979009ee49216f871c0fe4cd55fd131e065`; merge commit=`af1cbcedf92409e187e77217cc0b39449738d1ba`; workflow run=`25283202028`; docs-smoke=`success`; api-contract-tests=`success`; report-only spike merged；`BBDown` executable not found in PATH；no `-info`；no `PlatformResult` emitted；`tool_preflight_result=executable_not_found`；not adapter runtime approval；not `audio_transcript` approval |
| `T-P1A-010` | Wave 1 ledger open | `2026-05-04` | branch=`task/T-P1A-010-wave1-ledger-open`; scope=`ledger-only registration of T-P1A-010A / 010B / 010C`; Active count=`3/3`; Review count=`0`; no BBDown execution, no media download, no ffmpeg, no ASR, no credentials, no browser automation |

## Stop-the-line

- 发现 schema / state words / FS layout / LP 冲突
- 发现 raw response、日志或报账结构带出凭据
- 发现任务开始落 Phase 2-4 真实逻辑
- 发现有人尝试让 `recommendation / keyword / RAW gap` 直接创建 capture
- 发现 research note 或 draft spec 被写成 final authority
