---
title: Run-2 Amendment Ledger (3-Window Audit Synthesis)
status: candidate / amendment-ledger / not-authority
created_at: 2026-05-06
audit_inputs:
  - codex-cloud-independent: REJECT (8 findings)
  - gpt-pro-web-independent: REJECT_AS_RECEIPT_TRACEABILITY_DRIFT (8 findings)
  - hermes: V-PASS_WITH_AMENDMENTS (2 findings)
synthesis_verdict: REJECT_AS_RECEIPT_TRACEABILITY_DRIFT (2/3 REJECT, 1/3 V-PASS_WITH_AMENDMENTS)
synthesis_decision: amend_and_proceed (no code rollback; receipt/traceability fixes only)
user_authorization: pre-authorized direct-merge; no further external audit required
---

# Run-2 Amendment Ledger

## 9 + 1 项 FIX 映射

| FIX | 严重度 | 关联 finding | 文件 / 改动 | status |
|---|---|---|---|---|
| FIX-1 | CRITICAL | codex F1, gpt-pro F4 | `CHECKPOINT-Run2-final.json` LP-06/07 schema 加 `coverage_prs[]` | applied |
| FIX-2 | HIGH | codex F3, gpt-pro F2, hermes F1 | UAT-1 evidence verdict `works -> partial` + sub-field | applied |
| FIX-3 | HIGH | codex F2, gpt-pro F1, hermes F2 | RUN-2 + CHECKPOINT 加 `ready_for_run_3_reasons` | applied |
| FIX-4 | HIGH | codex F7, gpt-pro F4 | CHECKPOINT 加 SHA 分层字段 | applied |
| FIX-5 | MEDIUM | codex F5, gpt-pro F5 | `CHECKPOINT-Amendment-final.json` Step8 gate resolution | applied |
| FIX-6 | MEDIUM | codex F6, gpt-pro F3 | 原 Run-2 commander prompt 推到 `run2-audit-handoff` | applied |
| FIX-7 | MEDIUM | codex F4, gpt-pro F6 | 新增 `PR226-PR228-topology-note` | applied |
| FIX-8 | LOW | codex F8, gpt-pro F7 | W2 stale `#216 unrelated` 措辞修正 | applied |
| FIX-9 | LOW | gpt-pro F8 | RUN-2 summary allowed-surface 句精确化 | applied |
| FIX-LEDGER | — | 本文件 | 本 amendment ledger 写入 | applied |

## 边界硬保证

- 全部修改在 `docs/research/post-frozen/**`
- 未触: `docs/current.md` / `docs/task-index.md` / `docs/decision-log.md` / `AGENTS.md`
- 未触: `services/**` / `apps/**` / `workers/**` / `packages/**` / `data/**`
- `write_enabled=False` / 硬红线全保留
- 单 PR / 直接 merge / user 预授权（基于 3 窗口外审 synthesis）

## 与 Run-1 amendment 模式的一致性

本次 amendment 沿用 Run-1 PR `#231` amendment 模式：

- 多 auditor `REJECT` -> user 看 synthesis -> 授权 `amend_and_proceed`
- 仅 receipt/traceability 修复，不触 code
- 单 PR 直 merge，不再外审循环
- 未来 Run-3 如再触发 `>=2/3 REJECT` 应仍走此路径

## post-amendment readiness

- ready_for_run_3: no
- blocking_reasons:
  - LP-18 closeout intentionally stopped short of authority writeback
  - real_browser_visual_uat_not_run (user-authorized partial-evidence mode)
  - human_decision_pending: 是否要求真浏览器 UAT + authority writeback 才启 Run-3
- 这些 blocker 已在 RUN-2 report `## ready_for_run_3` 段显式记录
