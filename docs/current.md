# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-002 / T-P1A-003 / T-P1A-004`
- 主任务：`T-P1A-002 / T-P1A-003 / T-P1A-004`
- 工作模式：PR `#7` merged 后的三任务登记；本轮不执行三个 prompt
- 当前任务状态：`active`
- 当前结论：`T-P1A-001` metadata-only API-side capture creation baseline 已合并入 `main`（merge commit `d826ce191d71f9ab21d4a45543b980da1d282293`）。当前只登记 `T-P1A-002` / `T-P1A-003` / `T-P1A-004` 三个 active tasks；产品代码仍仅允许出现在对应任务批准路径；禁止 `audio_transcript` runtime、禁止 worker runtime、禁止浏览器自动化。

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
- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 项目根不建立重治理目录

> `T-P1A-001` 合并只表示最小 `metadata_only` API-side baseline 进入 `main`，不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-002`：API jobs / receipt / artifact ledger foundation；只做 API-side receipt ingestion 与 artifact ledger mapping；不创建 workers，不调用 BBDown / yt-dlp / ffmpeg / ASR
- `T-P1A-003`：BBDown tool-surface research / adapter contract proposal；只做 public-source research note / draft spec，不实现或调用 runtime capture
- `T-P1A-004`：Redaction / secret scan / CI hardening；只做未来 tool stdout/stderr/log 的安全 tooling、CI 与 contract tests，不调用外部 capture tools
- `T-P1A-001`：Bilibili `manual_url` quick_capture metadata contract 已通过 PR `#7` 合并入 `main`；merge commit `d826ce191d71f9ab21d4a45543b980da1d282293`；`artifact_assets` 当前仅为 `capture_manifest` API-side ledger stub，worker receipt endpoint 仍属后续任务
- `T-P0-002`：入口文档深化 + 并行执行协议固化，已在 PR `#1` 合并后闭合为 `done`
- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，已闭合为 `done`
- `T-P0-004`：通信测试 artifacts 清理与主线恢复，已闭合为 `done`
- `T-P0-005` / `T-P0-006`：按 user 决定视为通信测试，不作为活动产品任务或 Phase 1A approval
- `T-P0-007`：Phase 1A Bilibili `manual_url` quick_capture readiness pack，已合并入 `main`
- GitHub queue / Web GPT sync smoke / Codex adapter / MCP communication harness 当前暂停或关闭，不是 ScoutFlow 产品方向

## 下一步候选

- 按 user 指定从三个 active tasks 中选择执行路线；当前登记不代表三个 prompt 已执行
- `T-P1A-002` 是 API authority writer 大任务
- `T-P1A-003` 是 research / draft contract proposal，不能直接升级为 authority
- `T-P1A-004` 是安全 tooling / CI hardening
- 当前不自动扩展到 `audio_transcript`

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
