# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-003 active`
- 主任务：`T-P1A-003`
- 工作模式：`T-P1A-002` 与 `T-P1A-004` 已 merged to `main`；`T-P1A-003` 仍保持 draft research note 边界
- 当前任务状态：`T-P1A-003=active`; `T-P1A-002=done`; `T-P1A-004=done`
- 当前结论：`main` 当前已合入 `T-P1A-001` metadata-only API-side baseline、`T-P1A-002` receipt / artifact ledger baseline、`T-P1A-004` text redaction / secret scan safety baseline。`T-P1A-002` 的 merge commit=`1449f0d753c2da1476178f99934cf66c3add372c`，GitHub run=`25278781456`，`docs-smoke=success` / `api-contract-tests=success`；`T-P1A-004` 的 merge commit=`4f6af1ce3d823c84fc8f38cefee0790ec1830c62`，GitHub run=`25279195327`，`docs-smoke=success` / `api-contract-tests=success`；`T-P1A-003` 仍停在 draft PR `#10`，head=`42baf4165d7bf9022a9e8742d989a7428ae3ee4b`，GitHub run=`25278481839`，但它仍只是 research note，不是 authority。当前 Active count=`1/3`；当前不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

## 当前允许

- `docs/`
- `services/api/`
- `tests/`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `.github/pull_request_template.md`
- `tools/check-docs-redlines.py` 仅如需
- `.github/workflows/docs-check.yml` 仅如需
- `pyproject.toml`

## 当前禁止

- `apps/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- `audio_transcript` runtime
- 真下载 / ASR / BBDown / yt-dlp / ffmpeg
- 浏览器自动化
- Phase 2-4 真实逻辑

## 当前候选基准

- `T-P1A-001` = `metadata_only API-side capture creation baseline merged`
- `T-P1A-002` = `API-side receipt ingestion and artifact ledger mapping merged baseline`
- `T-P1A-004` = `redaction / secret scan / CI hardening merged baseline`
- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `POST /jobs/{job_id}/complete` = `worker receipt API-side validation and ledger entrypoint`; 当前只接收已存在 job 的 receipt，不创建 worker queue runtime
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`；当前 Active count=`1/3`
- 项目根不建立重治理目录

> `T-P1A-001` / `T-P1A-002` / `T-P1A-004` 的合并只表示对应 API-side 和安全基线进入 `main`，不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-003`：BBDown tool-surface research / adapter contract proposal；状态 `active`；PR `#10` 只承载 public-source research note / draft proposal，不实现或调用 runtime capture，不自动升级为 authority
- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；状态 `done`；已通过 PR `#9` 合并入 `main`，建立 `POST /jobs/{job_id}/complete`、`jobs` / `job_events` 最小 schema、receipt validation、artifact ledger mapping 与 idempotency / DB guard baseline
- `T-P1A-004`：Redaction / secret scan / CI hardening；状态 `done`；已通过 PR `#8` 合并入 `main`，建立 `redact_sensitive_text`、`check-secrets-redlines.py`、secret scan contract tests 与相关 CI safety baseline
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract 已通过 PR `#7` 合并入 `main`；merge commit `d826ce191d71f9ab21d4a45543b980da1d282293`；`artifact_assets` 的 `capture_manifest` API-side ledger stub 作为 `T-P1A-002` 的前置基线
- `T-P0-002`：入口文档深化 + 并行执行协议固化，已在 PR `#1` 合并后闭合为 `done`
- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，已闭合为 `done`
- `T-P0-004`：通信测试 artifacts 清理与主线恢复，已闭合为 `done`
- `T-P0-005` / `T-P0-006`：按 user 决定视为通信测试，不作为活动产品任务或 Phase 1A approval
- `T-P0-007`：Phase 1A Bilibili `manual_url` quick_capture readiness pack，已合并入 `main`
- GitHub queue / Web GPT sync smoke / Codex adapter / MCP communication harness 当前暂停或关闭，不是 ScoutFlow 产品方向

## 下一步候选

- `T-P1A-003` 保持 research note / draft PR；只有 user 明确批准时，才允许从 note 提炼 draft spec
- 当前不自动开启 `T-P1A-005`，也不自动批准任何 runtime
- 若要继续 Phase 1A，下一步必须基于 merged `T-P1A-002` / `T-P1A-004` 基线重新开任务，而不是回滚到旧 review 分支
- 当前不自动扩展到 `audio_transcript`

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
