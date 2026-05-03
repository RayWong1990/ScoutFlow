# Locked Principles

> Step0 / Phase 0 的 LP 入口文档。当前状态统一为 `candidate baseline`。

## LP-001 — Capture Scope Gate

- Principle: `recommendation / keyword / RAW gap` 不得直接创建 capture。
- Phase: `1A`
- Enforcement path: `services/api/scoutflow_api/captures.py`
- Test / lint path: `tests/contracts/test_lp001_capture_gate.py`
- Current status: `candidate baseline`

## LP-002 — Plan estimate → approve → run

- Principle: Capture Plan 必须先 estimate，再 approve，再 run。
- Phase: `2`
- Enforcement path: `services/api/services/state_guard.py`
- Test / lint path: `tests/api/test_lp002_plan_state.py`
- Current status: `candidate baseline`

## LP-003 — merger-of-record

- Principle: 代码 / schema / migration 与 PRD / IA / 产品叙事有明确合并仲裁边界。
- Phase: `0`
- Enforcement path: `AGENTS.md`、`.github/pull_request_template.md`
- Test / lint path: PR 模板人工审查
- Current status: `candidate baseline`

## LP-004 — Evidence Browser 不真嵌

- Principle: 当前不承诺 iframe / WebView 真内嵌平台页。
- Phase: `1`
- Enforcement path: `tools/check-ui-redlines`
- Test / lint path: UI redline lint
- Current status: `candidate baseline`

## LP-005 — 命名禁区

- Principle: 禁止使用 `crawl / spider / scrape_all / auto_capture / harvest` 等误导性命名。
- Phase: `0`
- Enforcement path: `tools/check-banned-words`
- Test / lint path: 禁用词扫描
- Current status: `candidate baseline`

## LP-006 — Single Writer / Multi Reviewer

- Principle: 同一任务只能有一个主写入窗口；其他工具只做 read-only review / research / patch suggestion。
- Phase: `0`
- Enforcement path: `AGENTS.md`, `docs/specs/parallel-execution-protocol.md`, `.github/pull_request_template.md`
- Test / lint path: PR 模板人工审查 + docs redline lint
- Current status: `candidate baseline`

## LP-007 — GitHub Audit Source

- Principle: 跨工具审计以 GitHub commit / PR diff / workflow run 为事实源，不以聊天摘要替代仓库事实。
- Phase: `0`
- Enforcement path: `AGENTS.md`, `README.md`, `docs/specs/parallel-execution-protocol.md`
- Test / lint path: PR 模板人工审查
- Current status: `candidate baseline`
