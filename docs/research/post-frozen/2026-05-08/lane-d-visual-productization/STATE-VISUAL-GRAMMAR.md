---
title: State Visual Grammar
status: candidate / docs-only / not-authority
authority: not-authority
ingest_basis:
  - GPT Pro pack A `04-state-visual-grammar.md`
  - GPT Pro pack C `Lane-D-visual-productization-candidate-handoff.md`
---

# State Visual Grammar

## Nine-state Table

| State | Visible signal | Color / weight guidance | Copy tone | Evidence requirement | Common confusion |
|---|---|---|---|---|---|
| empty | Quiet container, explicit next step, no success ornament | Neutral, low emphasis but still readable | `等待输入` / `尚无预览` | None | Looking like disabled or error |
| loading | Pending indicator, skeleton/pulse, in-flight badge | Accent/focus only, never success green | `正在读取` / `正在生成` | Request/task indicator if available | Looking like source/runtime approval |
| disabled | Muted control with visible reason | Low saturation, clearly non-clickable | `当前未解禁` / `需要新 dispatch` | Gate ID or hold reason nearby | Looking like optional future enhancement |
| blocked | Strong boundary banner, stop-line icon, explicit block reason | Higher weight than disabled; warning/block palette | `已阻止：...` | Authority-backed hold or gate reason | Looking like loading or soft warning |
| preview | Reviewable panel with path/hash and explicit non-commit cue | Focus/preview palette, never success green | `预览已生成，尚未写入` | Preview payload/hash/path | Looking like committed |
| committed | Success state with receipt, path, and durable outcome cues | Success color allowed only here | `已写入` / `已提交收据` | Atomic write receipt | Appearing while `write_enabled=False` |
| failed | Error row with failing layer and next action | Error palette with clear attribution | `失败已记录：...` | Failure receipt or final-state row | Collapsing into generic unknown error |
| partial | Split-state summary that names what passed and what did not | Mixed neutral/warning; avoid celebratory headline | `部分完成：X 已完成，Y 未完成` | Per-part receipts | Being reported as clear pass |
| skipped | Intentional non-run state with explicit reason | Muted neutral, dashed or low-weight badge | `已跳过：原因` | Skip reason or duplicate relation | Being mistaken for failed execution |

## Copy Rules

- Chinese-first, operator-facing, short, direct.
- Keep code words verbatim when needed: `write_enabled=False`, `runtime_tools`, `true_vault_write`, `dbvnext_migration`.
- Avoid SaaS and growth-copy vocabulary such as `Upgrade`, `Magic`, `Premium`, `Try again later`.
- `blocked` is product truth, not apologetic helper text.

## Evidence Hierarchy

| State | Minimum evidence |
|---|---|
| committed | Write receipt, path, hash, and durable outcome confirmation |
| preview | Preview hash/path or equivalent review receipt |
| blocked | Hold/gate reason with explicit unlock path |
| failed | Layer attribution plus failure receipt or log summary |
| partial | Split receipts for the completed and incomplete parts |
| skipped | Intentional reason or duplicate relationship |
| empty/loading/disabled | UI truth plus next-action/gate cue |

## Visual Gate

Reject V-pass if any of the following happens:

1. `preview` and `committed` are visually too similar.
2. `disabled` controls still look clickable.
3. `blocked` reads like temporary loading.
4. `failed` lacks layer attribution.
5. Trust Trace shows decoration heavier than evidence.
6. A human cannot scan the state truth in roughly 10 seconds.

## State Vocabulary Note

GPT Pro C used a broader minimum vocabulary including `success`, `error`, `blocked_by_hold`, `preview_only`, `dry_run`, and `needs_human_gate`. This repo-side candidate doc keeps the dispatch-required nine-state grammar while preserving the same evidence-first semantics.
