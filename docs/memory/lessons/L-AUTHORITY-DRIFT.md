---
name: authority-drift
description: research note / draft spec / chat summary 被错写成 final authority — 内容性质判断错位
type: project
source_atlas_node: L-AUTHORITY-DRIFT
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
memory_role: cross-vendor instinct source
risk_if_forgotten: critical
cross_session_count: 16
status: reference storage
---

# Authority drift

research note / draft spec / chat summary / candidate doc / external report / brainstorm output 任何**未经 PR merge + decision-log entry**的内容都不能被引用成 authority. 任何"已批准 / 已 promoted / 已锁定"声明必须有显式 **PR merge SHA + decision-log D-XXX entry** 双轨支撑. 当前被锁成 `current authority` 的 surface 只有 `current.md` / `task-index.md` / `decision-log.md` / `00-START-HERE.md`; `AGENTS.md` / 根 `CLAUDE.md` 属于 routing / instruction surface，不等同于 current-authority ledger.

**Why:** 跟 `L-CANDIDATE-PROMOTION` 是 `AP-authority-drift` 同一 anti-pattern 的**两个侧面** — promotion-discipline (语言纪律 4 处声明 candidate) vs **authority-drift (内容性质判断错位)**. ScoutFlow 跨 16 session 多次出现"chat 总结被引成 spec / research note 被当 promoted base / brainstorm 期 candidate 被引为 framework 决策" — 这类失误后果是路线漂移 + runtime/migration 偷渡 + 5 overflow lane 隐性解禁. ATLAS `LINKED-DECISION-AND-RUNBOOK.md` 把 `L-AUTHORITY-DRIFT` + `L-CANDIDATE-PROMOTION` + `T-CANDIDATE-NOT-AUTHORITY` 三者并列为 same anti-pattern 的独立 lesson, 不是同义.

**How to apply:** 任何"X 已批准 / X 已 promoted / 按 X 实施"类声明立刻反问 "PR merge SHA? decision-log entry 哪条?". 见到无法 trace 到 PR/decision-log 的 authority 引用, 默认当 candidate. authority 文件 single writer 锁不松动 — sidecar role (Claude / Codex / GPT Pro / Hermes) 默认不直接写 authority, 必须走 **dispatch 注册 (task-index Active row) + 单写权 (decision-log D-XXX) + docs-check 三层**. PR review 见到 brainstorm/chat/research 内容被合并到 authority file 立刻 reject. 跟 `L-CANDIDATE-PROMOTION` 配套使用 — 该条管语言纪律, 本条管内容性质判断.
