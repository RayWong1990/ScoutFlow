# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-002 review-candidate / T-P1A-003 / T-P1A-004`
- 主任务：`T-P1A-002`
- 工作模式：`T-P1A-002` authority writer 本地候选实现；`T-P1A-003` / `T-P1A-004` 仍保持各自边界
- 当前任务状态：`review`（`T-P1A-002` 本地候选）；`T-P1A-003=active`; `T-P1A-004=active`
- 当前结论：`T-P1A-002` 已在分支 `task/T-P1A-002-api-jobs-receipt-ledger` 和 PR `#9` 落地 API-side `POST /jobs/{job_id}/complete`、`jobs` / `job_events` 最小 migration、receipt validation models 与 `artifact_assets` ledger mapping；本地 full validation 为 `verdict=clear`，GitHub run `25277830562` 中 `docs-smoke=pass` / `api-contract-tests=pass`。该候选仍不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR，不启用 `audio_transcript` runtime，不进入 Phase 2-4。

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
- `T-P1A-002` = `API-side receipt ingestion and artifact ledger mapping review-candidate`
- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `POST /jobs/{job_id}/complete` = `worker receipt API-side validation and ledger entrypoint`; 当前只接收已存在 job 的 receipt，不创建 worker queue runtime
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 项目根不建立重治理目录

> `T-P1A-001` 合并只表示最小 `metadata_only` API-side baseline 进入 `main`，不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；状态 `review-candidate`；只做 API-side receipt ingestion 与 artifact ledger mapping；不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR
- `T-P1A-003`：BBDown tool-surface research / adapter contract proposal；只做 public-source research note / draft spec，不实现或调用 runtime capture
- `T-P1A-004`：Redaction / secret scan / CI hardening；只做未来 tool stdout/stderr/log 的安全 tooling、CI 与 contract tests，不调用外部 capture tools
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract 已通过 PR `#7` 合并入 `main`；merge commit `d826ce191d71f9ab21d4a45543b980da1d282293`；`artifact_assets` 的 `capture_manifest` API-side ledger stub 作为 `T-P1A-002` receipt mapping 的前置基线
- `T-P0-002`：入口文档深化 + 并行执行协议固化，已在 PR `#1` 合并后闭合为 `done`
- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，已闭合为 `done`
- `T-P0-004`：通信测试 artifacts 清理与主线恢复，已闭合为 `done`
- `T-P0-005` / `T-P0-006`：按 user 决定视为通信测试，不作为活动产品任务或 Phase 1A approval
- `T-P0-007`：Phase 1A Bilibili `manual_url` quick_capture readiness pack，已合并入 `main`
- GitHub queue / Web GPT sync smoke / Codex adapter / MCP communication harness 当前暂停或关闭，不是 ScoutFlow 产品方向

## 下一步候选

- 对 `T-P1A-002` 做外部审计与 merge 决策
- `T-P1A-002` 是 API authority writer review-candidate；本地与 GitHub Actions 已清，仍需人审
- `T-P1A-003` 是 research / draft contract proposal，不能直接升级为 authority
- `T-P1A-004` 是安全 tooling / CI hardening
- 当前不自动扩展到 `audio_transcript`

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
