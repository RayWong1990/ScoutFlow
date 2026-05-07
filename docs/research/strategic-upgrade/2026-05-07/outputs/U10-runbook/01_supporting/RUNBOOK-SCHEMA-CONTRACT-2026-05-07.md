---
title: RUNBOOK SCHEMA CONTRACT — U10
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: RUNBOOK-SCHEMA-CONTRACT
cluster: Supporting
trigger_keywords:
  - schema
  - frontmatter
  - body contract
risk_level: medium
single_user_applicable: true
multi_agent_applicable: true
linked_dispatch:
  - MOD-RUNBOOK-SCHEMA
linked_rule:
  - ~/.claude/rules/execution-discipline.md
boundary_statement: candidate schema only; not authority.
---

# RUNBOOK SCHEMA CONTRACT

[schema contract] 每个 runbook 是一个 single-file SOP，不依赖读者重新推理。文件必须同时具备 frontmatter contract 与 9 段 body contract。

## Frontmatter required fields

- `title`
- `status: candidate`
- `authority: not-authority`
- `created_at`
- `runbook_id`
- `cluster`
- `trigger_keywords[]`
- `risk_level`
- `single_user_applicable`
- `multi_agent_applicable`
- `linked_dispatch[]`
- `linked_pr[]`
- `linked_tools[]`
- `linked_skill[]`
- `linked_rule[]`
- `source_basis[]`
- `boundary_statement`

## Body required sections

- `mission`: section heading must include this keyword; content must have claim labels.
- `trigger`: section heading must include this keyword; content must have claim labels.
- `preconditions`: section heading must include this keyword; content must have claim labels.
- `steps`: section heading must include this keyword; content must have claim labels.
- `verification`: section heading must include this keyword; content must have claim labels.
- `rollback`: section heading must include this keyword; content must have claim labels.
- `lessons`: section heading must include this keyword; content must have claim labels.
- `linked`: section heading must include this keyword; content must have claim labels.
- `footer`: section heading must include this keyword; content must have claim labels.
[frontmatter rule] status 必须是 candidate，authority 必须是 not-authority。risk_level 必须为 low/medium/high/critical 之一。trigger_keywords 必须具体，不允许只写 general、misc、ops。

[rollback rule] rollback 必须能操作：hold、defer、supersede、quarantine、revert、restore、readback、redaction repair、owner handoff。禁止把 rollback 写成“无需处理”或空泛人工判断。

[claim label rule] 正文段落建议使用 canonical fact、candidate procedure、operator step、verification item、rollback instruction、lesson、environment limitation 等标签。目标是让 90% 以上段落能被审计者判断事实层级。

[dispatch field rule] linked_dispatch 使用 P2-/P3-/P4-/MOD- 形式。由于当前没有 U9 catalog 文件，LINKED-DISPATCH-CATALOG 只给 candidate mapping，并在 stdout 标注 linked_dispatch_validated=false。

## Schema edge-case appendix

[schema edge] `trigger_keywords` 必须能帮助用户排除相邻场景。例如 `bilibili + metadata_only + manual_url` 与 `BBDown + legal posture` 不能混写成一个泛化 capture 触发器。`linked_dispatch` 必须像候选派发 ID，而不是自然语言说明。

[invalid example] 不合格写法包括：`risk_level: none`、`preconditions: no precondition`、`rollback: manual review`、`linked_rule: security`、`status: ready`。这些写法会把候选 SOP 变成隐性批准或不可审计文本。

[repair example] 合格修复是：保留 `status: candidate`，明确 `authority: not-authority`，把 rollback 写成具体动作，例如 quarantine、supersede、revert、hold、redaction repair、downstream notification，并标注 source limitation。
