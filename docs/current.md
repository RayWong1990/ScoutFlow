# Current

## 当前状态

- Phase：`1A`
- Step：`T-P1A-001`
- 主任务：`T-P1A-001`
- 工作模式：首个 Phase 1A code-bearing task；`metadata_only only`
- 当前任务状态：`review`
- 当前结论：`T-P1A-001` metadata-only contract 已完成最小实现并进入 PR review candidate；产品代码仍仅允许出现在批准路径；禁止 `audio_transcript` runtime、禁止 worker runtime、禁止浏览器自动化。

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

- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 项目根不建立重治理目录

> 上述候选基准已获 user 批准；这只批准 `T-P1A-001` 的最小 `metadata_only` API-side baseline，不等于批准 broader Phase 1A runtime、workers、frontend、`audio_transcript` 或 Phase 2-4 产品代码。

## 当前任务

- `T-P1A-001`：Bilibili `manual_url` quick_capture，当前只做 `metadata_only only` 的 API-side contract 与 tests；`artifact_assets` 仅登记 `capture_manifest` 的 API-side ledger stub，worker receipt endpoint 仍属后续任务
- `T-P0-002`：入口文档深化 + 并行执行协议固化，已在 PR `#1` 合并后闭合为 `done`
- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，已闭合为 `done`
- `T-P0-004`：通信测试 artifacts 清理与主线恢复，已闭合为 `done`
- `T-P0-005` / `T-P0-006`：按 user 决定视为通信测试，不作为活动产品任务或 Phase 1A approval
- `T-P0-007`：Phase 1A Bilibili `manual_url` quick_capture readiness pack，已合并入 `main`
- GitHub queue / Web GPT sync smoke / Codex adapter / MCP communication harness 当前暂停或关闭，不是 ScoutFlow 产品方向

## 下一步候选

- 当前任务完成后，user review `T-P1A-001` tiny implementation PR
- 若 user 后续批准，可再开 `T-P1A-002` worker-side metadata fetch / artifact writing
- 当前不自动扩展到 `audio_transcript`

## 阻塞

- 不允许让 `recommendation / keyword / RAW gap` 直接创建 capture
- 不允许把 `/captures/discover` 语义写成 source discovery / search / recommendation discovery
