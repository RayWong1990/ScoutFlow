---
name: handoff-overlong
description: handoff 长不等于可执行; 80 行内可执行 > 800 行不可执行
type: project
source_atlas_node: L-HANDOFF-OVERLONG
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
risk_if_forgotten: medium
status: current authority
---

# Handoff overlong anti-pattern

handoff / commander prompt / session closure 文档**长度 ≠ 价值**. 80 行内含明确"下次第一步"的 handoff > 800 行流水账 handoff. 8 段 boilerplate 模板 (Mission / What / Why / When / Where / How / Linked / Lessons) 对 instinct memory 是 noise, 真信息在"最短复述"1 句话.

**Why:** ContentFlow L 项目 21 swap 协作中 1749 行 handoff 实测被下个 session 跳读 / 漏读关键. ScoutFlow `~/.claude/rules/session-closure.md` 已锁 "Handoff 控制 80 行 重点写下次从哪继续". 长 narrative 是 Opus 习惯 (Codex 元认知 §2 反向洞察), 但跨 session 复利价值低.

**How to apply:** 写 handoff 时强制 80 行内. memory 写 instinct format (rule + Why + How, ≤200 字). 见到 GPT Pro / Opus 输出长 narrative 立刻问"最短复述是哪句?". 8 段 boilerplate 删掉, 留 essence.
