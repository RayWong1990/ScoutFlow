---
name: candidate-promotion-discipline
description: candidate 文档不许漂移成 authority；语言纪律必须显式写到 title / frontmatter / 正文 / closeout 4 处
type: project
source_atlas_node: L-CANDIDATE-PROMOTION
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
risk_if_forgotten: critical
cross_session_count: 18
status: current authority
---

# Candidate-promotion discipline

candidate / draft / outline / not-approved / not-authority **必须显式**写在文档 4 处: title 段 / frontmatter `status:` 字段 / 正文首段边界声明 / closeout 声明. 不允许"我以为大家都知道这是 candidate" 的隐性约定.

**Why:** ScoutFlow 跨 18+ session 多次出现 candidate 漂移成 authority 踩坑 — research note 被引用成 spec, draft contract 被当 promoted, 候选 PRD 被 implicit 升级. 单人 prosumer + 多 agent 协作场景 implicit 假设最容易破. forward-going 4 状态词锁 (current authority / promoted addendum / candidate north-star / reference storage) 就是这条规则的 contract 化 (PR #244).

**How to apply:** 写 candidate 文档时 4 处显式声明. PR review 硬检查 4 处是否齐全. 任何"已经批准 / 已经完成"的隐含语气立刻反问 "哪个 PR / 哪条 decision-log entry?". 见到没标 status 字段的文档默认当 candidate.
