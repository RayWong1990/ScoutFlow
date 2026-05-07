---
title: LINKED RULES INDEX — U10
status: candidate
authority: not-authority
created_at: 2026-05-07
runbook_id: LINKED-RULES-INDEX
cluster: Supporting
trigger_keywords:
  - linked rules
  - claude rules
  - canonical rules
risk_level: medium
single_user_applicable: true
multi_agent_applicable: true
linked_dispatch:
  - MOD-LINKED-RULES
linked_rule:
  - ~/.claude/rules/aesthetic-first-principles.md
  - ~/.claude/rules/agents.md
  - ~/.claude/rules/development-workflow.md
  - ~/.claude/rules/testing.md
  - ~/.claude/rules/security.md
  - ~/.claude/rules/parallel-safety.md
  - ~/.claude/rules/session-closure.md
  - ~/.claude/rules/token-hygiene.md
  - ~/.claude/rules/execution-discipline.md
  - ~/.claude/rules/codex-metacognition-learnings.md
boundary_statement: prompt-provided rule mapping; current container validation failed for local paths.
---

# LINKED RULES INDEX

[environment limitation] 当前运行环境没有可读的 `~/.claude/rules/*.md`；因此本索引不声称已经读取或验证这些规则正文。它只按 U10 prompt 给出的 canonical path 建立 runbook mapping。

| Rule path | Exists in current container | Mapped clusters | Expected use |
|---|---:|---|---|
| `~/.claude/rules/aesthetic-first-principles.md` | `false` | Visual | referenced, not rewritten |
| `~/.claude/rules/agents.md` | `false` | Dispatch | referenced, not rewritten |
| `~/.claude/rules/development-workflow.md` | `false` | Boundary, Tooling | referenced, not rewritten |
| `~/.claude/rules/testing.md` | `false` | Boundary, Visual, Tooling | referenced, not rewritten |
| `~/.claude/rules/security.md` | `false` | Capture, Boundary, Egress, Tooling, Recovery | referenced, not rewritten |
| `~/.claude/rules/parallel-safety.md` | `false` | Capture, Dispatch | referenced, not rewritten |
| `~/.claude/rules/session-closure.md` | `false` | Dispatch, Memory, Egress, Recovery | referenced, not rewritten |
| `~/.claude/rules/token-hygiene.md` | `false` | Memory | referenced, not rewritten |
| `~/.claude/rules/execution-discipline.md` | `false` | Capture, Dispatch, Boundary, Visual, Memory, Egress, Recovery | referenced, not rewritten |
| `~/.claude/rules/codex-metacognition-learnings.md` | `false` | supporting only | referenced, not rewritten |

[mapping note] aesthetic-first-principles 映射 Visual；agents/parallel-safety 映射 Dispatch；development-workflow/testing 映射 Boundary 与 Tooling；security 映射 Capture/Boundary/Egress/Tooling/Recovery；session-closure/token-hygiene 映射 Memory；execution-discipline 全局适用。

[non-rewrite rule] 本库不复制或重写全局规则正文。runbook 只链接规则名并把必要操作写成候选 checklist；真正执行前，用户应在自己的环境读取规则正文。

## Rules validation appendix

[rule map] 本索引按提示提供的 `~/.claude/rules/*.md` 名称建立映射，但当前容器未能读取这些本地文件，因此不声称已验证原文。用户审计时应逐项打开 canonical rule，确认文件名、原则、阈值和例外是否仍然有效。

[rule usage] runbook 引用 rule 的目的不是重写全局规则，而是告诉操作者在该场景下最容易违反哪一条。若 global rule 与 candidate runbook 冲突，优先 global rule，并把 runbook 标为 needs_update。

[rule drift] 当安全、token、parallel、session closure 或 aesthetic gate 规则更新时，先修 LINKED-RULES-INDEX，再批量扫描 runbook frontmatter，避免旧 SOP 用新规则无法支持的语言。
