# Current

## 当前状态

- Phase：`0`
- Step：`Step0`
- 主任务：`T-P0-007`
- 工作模式：Phase 1A readiness planning；Bilibili `manual_url` quick_capture 开工门准备
- 当前任务状态：`review candidate`
- 当前结论：正在准备后续 `T-P1A-001` 的 implementation gate；不等于产品代码 approval，不进入 Phase 1A 实现

## 当前允许

- `docs/`
- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `.github/pull_request_template.md`
- `tools/check-docs-redlines.py` 仅如需
- `.github/workflows/docs-check.yml` 仅如需

## 当前禁止

- `apps/`
- `services/`
- `workers/`
- `packages/`
- `data/`
- `referencerepo/`
- `candidates/`
- `dispatches/`
- `audits/`
- 真实采集实现
- 浏览器自动化
- Phase 2-4 真实逻辑

## 当前候选基准

- `POST /captures/discover` = `capture 创建入口（capture creation entrypoint）`
- `recommendation / keyword / RAW gap` 不直接创建 capture
- 活动任务上限 `3`
- 项目根不建立重治理目录

> 上述候选基准已获 user 批准，可作为 `Phase 0 / Phase 1A` 的候选实现基线；这不等于批准开始产品代码实现。

## 当前任务

- `T-P0-002`：入口文档深化 + 并行执行协议固化，已在 PR `#1` 合并后闭合为 `done`
- `T-P0-003`：目录骨架 + 文档 lint stub + 入口文档同步，已闭合为 `done`
- `T-P0-004`：通信测试 artifacts 清理与主线恢复，已闭合为 `done`
- `T-P0-005` / `T-P0-006`：按 user 决定视为通信测试，不作为活动产品任务或 Phase 1A approval
- `T-P0-007`：Phase 1A Bilibili `manual_url` quick_capture readiness pack，当前为 docs-only review candidate
- GitHub queue / Web GPT sync smoke / Codex adapter / MCP communication harness 当前暂停或关闭，不是 ScoutFlow 产品方向

## 下一步候选

- user review `docs/plans/phase1a-manual-url-quick-capture-readiness-2026-05-03.md`
- user 后续可选择是否批准 `T-P1A-001` 作为第一项 code-bearing Phase 1A 任务
- 当前不自动进入 `Phase 1A` 产品代码

## 阻塞

- 未获 user 明确批准前，不启动 `T-P1A-001`
