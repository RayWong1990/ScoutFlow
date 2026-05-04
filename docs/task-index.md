# ScoutFlow Task Index

> 共享薄账本。当前只服务 Step0 与 Phase 0 / 1A 开工安全，不承担重治理职能。
> 当前限制：Active product lane max=`3` + Authority writer max=`1`；当前 Active count=`0/3`，Review count=`0`。

## 规则

- 当前只维护 Step0 / Phase 0 / Phase 1A 开工安全相关任务
- 任务状态变化时先写本文件，再更新 `docs/current.md`
- Review / audit / research lanes 不计入 product lane 上限，除非写 authority
- 外部研究统一落 `docs/research/`，不在项目根建立重治理目录
- 任何活动任务都必须写明 owner、scope、allowed paths、validation
- research note 不直接升级为 authority；draft spec 必须显式标记 `draft / not final authority / not runtime approval`

## 当前 Phase

`Phase 1A — metadata_only manual_url quick_capture contract`

## Active

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Review

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Backlog / Research

| 任务 ID | 标题 | 状态 | Owner Tool | 范围 | Allowed Paths | Forbidden Paths | 关联 PRD / SRD / Contract | Validation | Stop-the-line | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` | `—` |

## Wave 2 Conflict Domain (T-P1A-018/019/020)

> Registered 2026-05-04 by T-P1A-017 ledger-open. 18/19/20 must not collide on the domains below.
> Wave 2 closed 2026-05-04 by T-P1A-027. Table retained as historical reference only — Wave 2 lanes (T-P1A-018/019/020) all merged and frozen. Future waves register their own conflict domains.

| Conflict Domain | Owner Lane | Other lanes |
|---|---|---|
| `services/api/scoutflow_api/storage.py` | T-P1A-018 | 19/20 read-only |
| `services/api/scoutflow_api/captures.py` + `jobs.py` + `main.py` | T-P1A-018 | 19/20 read-only |
| `services/api/scoutflow_api/external_tools/**` | T-P1A-019 | 18 不动 |
| `services/api/scoutflow_api/metadata_probe_receipt_bridge.py` | T-P1A-019 | 18 不动 |
| `services/api/scoutflow_api/orchestration/**` (新建) | T-P1A-019 | 18/20 不动 |
| `tests/api/test_capture_trust_trace.py` | T-P1A-020 | 18/19 不动 |
| `tests/api/test_jobs_complete.py` + `test_captures_discover.py` | T-P1A-018 | 19/20 read-only |
| `tests/contracts/test_*_contract.py` | 各 lane 可加自己的新 contract test 文件，但同一文件单写者 | — |
| `docs/research/t-p1a-02X-*.md` | 各对应 task；别人不动 | — |
| `services/api/migrations/**` | FORBIDDEN | 任何 lane 不得动 |

**Authority writer slot [L4]**: T-P1A-017 / T-P1A-026 各自占用 Authority writer slot 1/1，跑期间禁止任何其他 authority writer 同时改 `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md`。

## Blocked

| 任务 ID | 标题 | 阻塞原因 | 需要动作 | 时间 |
|---|---|---|---|---|
| `—` | `—` | `—` | `—` | `—` |

## Done

| 任务 ID | 标题 | 完成时间 | 备注 |
|---|---|---|---|
| `T-P1A-028` | SRD-v3 candidate + DB design audit-fix | `2026-05-04` | branch=`task/T-P1A-028-srd-v3-candidate-audit-fix`; PR=#53; merge commit=c1c2565; scope=docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md + docs/specs/db-vnext-design-2026-05-04.md; result=SRD-v3 candidate audit-fix covering trigger contract, composite FK, PlatformResult CHECK, cross-capture identity, reachability vocabulary, and F-012 hard gate; status=candidate / not SRD-v3 promoted authority / not migration approval / not runtime approval; post-S0/S1 wording + evidence identity immutability fix=T-P1A-029 |
| `T-P1A-027` | Wave 2 authority ledger reconciliation | `2026-05-04` | branch=`task/T-P1A-027-wave2-authority-reconciliation`; PR=#52; merge commit=c2bcac0; scope=docs/current.md + AGENTS.md + docs/task-index.md + docs/decision-log.md + docs/specs/contracts-index.md; result=Wave 2 authority surfaces closed, Active count=0/3, T-P1A-020/T-P1A-026 moved to Done, stale T-P1A-021 Backlog/Research row removed, contracts-index PR #51 state refreshed; no product code / schema / migration / runtime |
| `T-P1A-026` | SRD-v3 candidate amendment for DB vNext | `2026-05-04` | branch=`task/T-P1A-026-srd-v3-db-vnext-candidate`; PR=#51; merge commit=fdf0673; scope=docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md (473 lines) + contracts-index.md (+1); ID-reuse=user-authorized substitution from original Wave 2 close scope; result=Stage 2 SRD-v3 candidate authored covering 5-table evidence-chain DDL + supersession boundary + purge defaults + lineage_variant vocabulary; status=candidate / not SRD-v3 promoted authority / not migration approval / not runtime approval; audit-fix=T-P1A-028 completed via PR #53; post-S0/S1 wording guard=T-P1A-029 |
| `T-P1A-020` | Trust Trace / Explore contract hardening | `2026-05-04` | branch=`task/T-P1A-020-trust-trace-explore-contract-hardening`; main PR=#43; follow-up invariants PR=#49 (PR #48 stacked-base superseded by #49, no semantic delta); merge commits=6d959ab + 8694c06; scope=tests/api/test_capture_trust_trace.py (+45) + new tests/contracts/test_trust_trace_dto_snapshot_contract.py (327 lines) + new docs/research/t-p1a-020-trust-trace-explore-state-map-2026-05-04.md (90+47 lines); 5-state snapshot frozen=created/queued/running/failed/metadata_fetched; UI naming invariants + retry policy + open-question on metadata_fetched staleness TTL added in #49; no storage.py / captures.py / jobs.py changes (18-owned read-only honored); no PlatformResult / WorkerReceipt / Trust Trace DTO change; no audio_transcript runtime |
| `T-P1A-019` | metadata probe dry-run orchestrator | `2026-05-04` | branch=`task/T-P1A-019-metadata-probe-dry-run-orchestrator`; PR=`#44`; merge commit=`44e87a147ba6ba962731757c9d99baf40fcf0dd3`; audit-fix commit=`6dead72`; scope=`new services/api/scoutflow_api/orchestration/ package + dry_run_metadata_probe + bridge build_metadata_fetch_failure_receipt extension`; result=`135 tests passed (15 contract + 4 e2e new); provenance gate (URL-derived BV vs probe.platform_item_id); failure receipt path for non-ok platform_result; success evidence still gated on T-P1A-011C auth-present source`; conflict-domain-owner=`external_tools/**`, `metadata_probe_receipt_bridge.py`, `orchestration/**`; T-P1A-018 owned files (storage/jobs/captures/main) untouched; no subprocess.run; no live BBDown; no migration; no PlatformResult / WorkerReceipt schema / Trust Trace DTO change; no audio_transcript runtime |
| `T-P1A-018` | metadata_fetch job enqueue API + OpenAPI UX audit-fix | `2026-05-04` | branch=`task/T-P1A-018-metadata-fetch-job-enqueue-api`; PR=`#39`; merge commit=`a1f965bdf22d027f173683ae324d2b2acd0a9f19`; scope=`POST /captures/{capture_id}/metadata-fetch/jobs enqueue endpoint + idempotency hardening + 5-Gate OpenAPI UX polish (P0/P1/P2)`; result=`116 tests passed; tags=captures/jobs/ops; Literal types + dedupe_key pattern; full responses contract; app description + openapi_tags`; conflict-domain-owner=`storage.py/captures.py/jobs.py/main.py`; no migration; PlatformResult enum unchanged; Trust Trace data shape unchanged; no BBDown / ffmpeg / ASR / audio_transcript runtime |
| `T-P1A-017` | Wave 2 ledger open | `2026-05-04` | branch=`task/T-P1A-017-wave2-ledger-open`; PR=`#36`; merge commit=`ca300659ba74392eb50b210f76d340f0855f706f`; scope=`docs-only authority ledger registration of T-P1A-018/019/020 active lanes + T-P1A-021/022/023/024/025 research lanes + Wave 2 conflict domain table + [L4] authority writer slot`; opened Wave 2 with sequencing 018→019→020; user-approved lane plan recorded; no runtime / worker / frontend / ASR / audio_transcript approval |
| `T-P1A-021` | BBDown runtime gate matrix research | `2026-05-04` | branch=`task/T-P1A-021-bbdown-runtime-gate-matrix`; PR=`#37`; merge commit=`1e283457ff55d4e552b317bdfeb4b5a454a098d9`; scope=`docs/research/t-p1a-021-bbdown-runtime-gate-matrix-2026-05-04.md only`; status=`research / candidate — not authority; not runtime approval`; covers ToolPreflightResult / PlatformResult states + safe execution preconditions + evidence routing rules + future T-P1A-021A bounded probe proposal; no BBDown execution |
| `T-P1A-025` | DB / evidence ledger vNext proposal | `2026-05-04` | branch=`task/T-P1A-025-db-evidence-ledger-vnext-proposal`; PR=`#42`; merge commit=`7a120f22efbf4e5455ad96a0c5cffb796c433c31`; scope=`docs/research/t-p1a-025-db-ledger-vnext.md only`; status=`research / frozen — not authority; not migration approval; not runtime approval`; result=`frozen research input for Stage 2 SRD-v3 DB vNext amendment writing`; no services/tests/migrations/authority docs/runtime |
| `T-P1A-024` | Explore wireframe + state table | `2026-05-04` | branch=`task/T-P1A-024-explore-wireframe-state-table`; PR=`#40`; merge commit=`05c545a6c17d8006d113f7c39a5179d9c057540c`; scope=`docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md only`; status=`research / frozen — not authority; not frontend approval`; result=`frozen research input for Explore / state-table decisions`; no services/migrations/frontend runtime |
| `T-P1A-023` | LLM normalization schema | `2026-05-04` | branch=`task/T-P1A-023-post-merge-wording-fix`; PR=`#45` + follow-up PR=`#46`; final merge commit=`d23abee7fc2daac234f2bad69689309ad855bf67`; scope=`docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md only`; status=`research / frozen — not authority; not schema approval`; result=`merged research note plus wording hardening on main`; no services/migrations/runtime |
| `T-P1A-022` | ASR pipeline prestudy | `2026-05-04` | branch=`task/T-P1A-022-asr-pipeline-prestudy`; PR=`#38`; merge commit=`ed81b3a066e78dae25f8e4a7ca8dd69c0d08c0d9`; scope=`docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md only`; status=`research / frozen — not authority; not runtime approval`; result=`frozen research input; audio_transcript remains blocked`; no services/migrations/audio_transcript runtime |
| `T-P1A-016` | Dispatch template extract | `2026-05-04` | scope=`docs-only meta-template extraction`; result=`docs/dispatch-template.md + dispatch authoring guide + retro added`; self_audit=`7-8 segments compressed to 5`; boundary=`no product code, no PRD/SRD/LP/spec contract changes`; no runtime |
| `T-P1A-015` | PRD/SRD promote to v2 | `2026-05-04` | scope=`promote PRD/SRD base docs to v2 + archive v1/amendment chain + update forward references`; result=`PRD-v2/SRD-v2 created, 7 historical files archived, forward authority references switched to v2`; audit=`rebased after PR #34 merge + T-P1A-016 ledger absorbed`; no product/runtime/schema change |
| `T-P1A-014` | Lean constraints cleanup v2 | `2026-05-04` | scope=`docs-only governance slimming`; result=`README/AGENTS/CLAUDE slimmed, SRD §6/§7 lean cleanup, 8 contract groups, 4 hard LP, lane=3+writer=1`; audit=`GPT Pro PASS WITH NOTES`; unlock_condition=`PR #33 merged; T-P1A-015 unlocked`; no product/runtime/schema change |
| `T-P1A-013B` | Authority sync + docs-check suffix task hardening | `2026-05-04` | scope=`authority drift fix + docs-check suffix task parsing hardening`; fixes=`remove stale T-P1A-013A active line from docs/current.md + parse suffix task ids exactly + current-doc self-check`; result=`authority state and docs-check now agree on 011D/E/F/G, 012R, 013A/B`; no product/runtime change |
| `T-P1A-013A` | Receipt / Trust Trace audit hardening | `2026-05-04` | scope=`small code/test hardening after merged 012/012R/013`; fixes=`path containment before metadata bridge writes + current-phase success evidence validator on generic receipt API`; result=`blocked T-P1A-011 and no-auth success evidence no longer accepted through generic metadata_fetch receipts`; trust_trace=`layering unchanged`; no runtime |
| `T-P1A-013` | Explore Trust Trace minimal surface | `2026-05-04` | mode=`API/CLI`; implementation=`GET /captures/{capture_id}/trust-trace`; layering=`capture + capture_state + metadata_job + probe_evidence + receipt_ledger + media_audio + audit`; result=`receipt only appears after receipt ledger exists; auth-present evidence labeled correctly; media/audio stays not approved`; no frontend / no BBDown runtime |
| `T-P1A-012R` | Receipt-wiring single-point retro | `2026-05-04` | scope=`post-08 docs-only retro`; result=`012 proves safe evidence-to-receipt mapping in tests only`; ceremony_tax=`yes`; readiness=`Dispatch 09 can proceed`; no product-code change |
| `T-P1A-012` | Metadata probe receipt / artifact ledger wiring | `2026-05-04` | scope=`consume existing T-P1A-011C auth-present metadata evidence into POST /jobs/{job_id}/complete baseline`; implementation=`metadata_probe_receipt_bridge helper + metadata_fetch artifact-kind gate + evidence-source metadata writeback`; artifact_kinds=`safe_metadata_evidence + metadata_probe_summary`; result=`011C auth-present evidence maps into artifact_assets/job_events without new BBDown runtime`; no media / ffmpeg / ASR / manual auth / audio_transcript / frontend / workers |
| `T-P1A-011G` | Sidecar review for `07.x` + patched `08/09` | `2026-05-04` | verdict=`PASS_WITH_FIXES`; scope=`read-only review criteria + repo authority-doc sync repair`; fix=`remove stale 011C-only focus from AGENTS/current/task-index/decision-log/README`; readiness=`Dispatch 08 ready; Dispatch 09 ready`; no runtime |
| `T-P1A-011F` | Dispatch 08/09 prompt patch | `2026-05-04` | scope=`repo-side patch report + external patched prompt verification`; corrected=`08 depends on 011C evidence, not blocked 011`; preserved=`T-P1A-012/013 numbering`; external patched files stayed outside GitHub PR; no runtime |
| `T-P1A-011E` | Minimal retro skeleton | `2026-05-04` | scope=`docs/retro/README.md + three templates + 2026-05-04 week-1 retro`; boundary=`not authority, not PRD/SRD amendment, not product scope`; no runtime |
| `T-P1A-011D` | Second retro / remediation triage | `2026-05-04` | scope=`GitHub truth + Opus claim triage + numbering repair + pre-08 dispatch plan`; locked=`T-P1A-012 remains Dispatch 08, T-P1A-013 remains Dispatch 09`; no runtime |
| `T-P1A-011C` | Auth-present BBDown metadata probe | `2026-05-04` | scope=`repo-external executable/auth store + repo-external temp cwd + single sample URL`; result=`platform_result=ok`; parsed=`aid/title/duration/page_count/selected_page`; fix=`minimal bbdown_info_parser repair + regression test for real BBDown 1.6.3 output`; no media / ffmpeg / ASR / receipt / capture state |
| `T-P1A-011B` | Manual-auth QR local-only gate | `2026-05-04` | scope=`repo-external executable/auth store + repo-external temp cwd`; result=`QR displayed locally, user scan completed, auth completed from safe tool output`; evidence=`temp QR cwd cleaned, auth sidecar stayed outside Git`; no `-info`, no media, no `PlatformResult`, no receipt/capture state |
| `T-P1A-011` | BBDown tool preflight compatibility repair | `2026-05-04` | scope=`bbdown_preflight.py + test_bbdown_tool_preflight_contract.py`; fix=`when BBDown 1.6.3 treats --version as missing root url, preflight may retry with --help and still parse version`; live verification=`ContentFlow local BBDown -> executable_found version=1.6.3`; no `-info`, no `PlatformResult`, no auth/media/receipt/capture state |
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
| `T-P1A-010` | Wave 1 ledger open | `2026-05-04` | branch=`task/T-P1A-010-wave1-ledger-open`; scope=`ledger-only registration of T-P1A-010A / 010B / 010C`; opened three Wave 1 active slots; no BBDown execution, no media download, no ffmpeg, no ASR, no credentials, no browser automation |
| `T-P1A-010A` | BBDown executable discovery / tool preflight package | `2026-05-04` | PR=`#23`; head=`155e0b8a2910e81fc26625dd3be4391ab792e289`; merge commit=`0b5d4350c4dad3ebae3d594245ddfcfb65a22f91`; workflow run=`25284770283`; docs-smoke=`success`; api-contract-tests=`success`; scope=`ToolPreflightResult code and contract tests only`; not live BBDown / URL / `-info` / media / ffmpeg / ASR / receipt / artifact / capture state approval |
| `T-P1A-010B` | BBDown no-auth `-info` adapter shell with injected runner and parser integration | `2026-05-04` | PR=`#22`; head=`73bc85443241c336d03bf74c5cef5a676a9a4957`; merge commit=`b6a23a9d46c94e07974404d7eec19ba2dffe7092`; workflow run=`25284816246`; docs-smoke=`success`; api-contract-tests=`success`; scope=`injected-runner adapter shell and parser integration only`; no live BBDown / real `BBDown -info` / QR or manual auth / media / ffmpeg / ASR / receipt / artifact / capture state approval |
| `T-P1A-010C` | PRD/SRD amendment repair pack + next dispatch plan + red-team checklist | `2026-05-04` | PR=`#24`; head=`02ab26ebf8e966b7af30abc90d8a56733f1c636e`; merge commit=`297d286a13b8d60d9627db80925289fb85674a8a`; workflow run=`25284792684`; docs-smoke=`success`; api-contract-tests=`success`; scope=`candidate amendment docs and contracts-index registration only`; PRD/SRD v1.2 remains `candidate / draft / not final authority / not runtime approval`; `audio_transcript` remains blocked |

## Stop-the-line

- 发现 schema / state words / FS layout / LP 冲突
- 发现 raw response、日志或报账结构带出凭据
- 发现任务开始落 Phase 2-4 真实逻辑
- 发现有人尝试让 `recommendation / keyword / RAW gap` 直接创建 capture
- 发现 research note 或 draft spec 被写成 final authority
