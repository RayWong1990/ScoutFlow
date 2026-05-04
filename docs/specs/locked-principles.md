# Locked Principles

> 当前状态：`Phase 1A hard baseline`。Hard LPs=`LP-001 / LP-006 / LP-007 / LP-SEC-001`；触碰这些或 `AGENTS.md` §4 红线即 stop-the-line。降级项见 `docs/retro/2026-05-04-lean-cleanup.md`。

## LP-001 — Capture Scope Gate

- Principle: `recommendation / keyword / RAW gap` 不得直接创建 capture。
- Phase: `1A`
- Enforcement path: `services/api/scoutflow_api/captures.py`
- Test / lint path: `tests/contracts/test_lp001_capture_gate.py`
- Current status: `hard baseline`
- Note: 命名禁区由 `tools/check-docs-redlines.py` lint enforce，不再作为独立 LP。

## LP-006 — Single Writer / Multi Reviewer

- Principle: 同一 authority conflict domain 只能有一个主写入窗口；其他工具只做 read-only review / research / patch suggestion。
- Phase: `0/1A`
- Enforcement path: `AGENTS.md`, `CLAUDE.md`, `docs/specs/parallel-execution-protocol.md`, `.github/pull_request_template.md`
- Current status: `hard baseline`
- Absorbs: former `LP-003 merger-of-record` is now treated as part of Single Writer authority ownership.

## LP-007 — GitHub Audit Source

- Principle: 高风险或 material task 的跨工具审计以 GitHub commit / PR diff / workflow run 为事实源，不以聊天摘要替代仓库事实。
- Phase: `0/1A`
- Applies to: schema, security, receipt, runtime gate, authority files, and any user-marked high-risk task.
- Current status: `hard baseline for high-risk/material tasks`; small docs-only tasks may use lighter local review when user allows.

## LP-SEC-001 — Credential Material Is Never Evidence

- Principle: cookie / token / auth sidecar / raw credential material cannot be used as tracked evidence and must not enter Git, PR, CI, logs, DB artifacts, or tracked docs.
- Phase: `1A+`
- Enforcement path: `docs/specs/raw-response-redaction.md`, `tools/check-secrets-redlines.py`, `.gitignore`, code review
- Current status: `hard baseline`

## 降级 / 吸收记录

| Former LP | New status |
|---|---|
| `LP-002` Plan estimate -> approve -> run | `[Phase 2 reference; not enforced in current Phase 1A]` |
| `LP-003` merger-of-record | absorbed into `LP-006` |
| `LP-004` Evidence Browser 不真嵌 | `[Phase 1B+ UI reference]` |
| `LP-005` 命名禁区 | independent LP removed; lint remains in `tools/check-docs-redlines.py` |
