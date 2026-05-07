---
title: Spot Check — U11-anti-pattern
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Spot Check — U11-anti-pattern

## §1 文件抽样
- README: `README.md` — verdict=CONCERN-MAJOR (24 段相同 `[derived] 使用建议: 不要把本 README 当作执行授权` 重复)
- SELF-AUDIT: `SELF-AUDIT-FINDINGS-2026-05-07.md` — verdict=CONCERN-MAJOR (30 SA finding 表实, 但末尾 15+ 段 `[derived] Self-audit reminder` 重复)
- MASTER: `MASTER-ANTI-PATTERN-INDEX-2026-05-07.md` — verdict=CLEAR (10 cluster × 75-80 AP 全表 + introduced/exposed 分布表 + Mermaid heatmap + linked_rule 准确)
- 抽样 1 (AP-SF-02 Run-1 amendment): 真 PR #231 + #239 FIX-5 attribution + introduced=true (合理)
- 抽样 2 (AP-ED-06 diagnose without git fetch): 真 codex audit 引用 + introduced=exposed (合理)
- 抽样 3 (master AP table 全扫): 80 AP 中 introduced=5 / exposed=75 — §3 自承 "故意把大多数标 exposed"

## §2 真实历史 attribution (U11 关键)
**部分真**. Master AP 表中 PR # 锚点 (#231/#239/#240/#226/#227/#228) 是真存在 ScoutFlow PR, 引用合理. AP-SF-02 §9 引用的 PR body content 与 SELF-AUDIT SA-05/SA-27 自承 "PR sources are run-level anchors, not line-level diffs / fetched metadata/body summaries" 诚实. SA-07/SA-08 诚实声明 ContentFlow L1 + ~/.claude/rules + U9/U10 sources 在生成环境**不可读**, 所以 linked_runbook / linked_dispatch / linked_rule 是 **candidate ID 映射形状, 不是已验证存在**.

## §3 introduced vs exposed 字段 (元认知 §1.8)
**优秀**. Master 表自报 introduced=5 (3 SF + 1 MA + 1 DT)、exposed=75 — 默认偏 exposed, 符合元认知 §1.8 "归因到最近 PR = 错误归因" 原则. 每 AP frontmatter `introduced_or_exposed:` 字段必填, §9 末尾 `归因结论` 段落显式声明.

## §4 Template fill-in-the-blank 严重问题
**80/80 AP 文件共享同一模板 prose**: §1 Mission / §2 Anti-example 第二段 / §3 Trigger signals 推荐 grep 那段 / §4 Consequences / §5 Counterexample / §6 Detect rule / §7 Prevent rule / §8 Escape clause — 全部除"反例描述句"和 frontmatter 字段外, prose 100% 一致 (grep 验证: 80/80 文件含 "在实际执行中, 最常见的口头信号包括" + "这些规则只是候选 detect rule"). 这意味着每 AP 实际"unique" 内容仅 frontmatter + 反例一句 + 真 attribution 段 — 估计 unique 内容 25-30%.

## §5 cross-link 准确性
- linked_rule: 准确 (~/.claude/rules/execution-discipline.md / parallel-safety.md / security.md / aesthetic-first-principles.md / session-closure.md / token-hygiene.md / testing.md — CLAUDE.md context 里全存在)
- linked_runbook RB-X-XX / linked_dispatch P2-X-XX 或 MOD-X-XX — SELF-AUDIT SA-08 自承 "candidate ID shapes pending real-source verification"
- PR # — 真存在但 SA-26/SA-27 承认 path-level 非 line-level

## §6 Mermaid quality
Master heatmap (10 cluster 顺串) — 质量 simple, cluster name + count 标签, 非装饰. SELF-AUDIT SA-19 自报 ≥4 张满足要求.

## §7 Verdict
**`CONCERN-MAJOR`** — Attribution 真 + introduced/exposed 字段诚实 + linked_rule 准 + SELF-AUDIT 诚实声明 limitation, 但 80/80 AP 共享模板 prose 是严重 **rule-template fill-in-the-blank**, 1068 claim labels 是表面完整非真深度. 真 unique 价值在 master AP table + 部分 SF/AC/BL/MA cluster 的 §9 attribution.

## §8 Promote 建议
- **Tier 1 (高 attribution 价值)**: AP-SF-01/02/04/05 (真 PR #231/#239 FIX-5/FIX-7) + AP-MA-02 (amend_and_proceed) + AP-AC-01/02 (single writer 违规) + AP-BL-01 (write_enabled false) + AP-VS-03 (BBDown C&D) + AP-ED-06 (git fetch) — ~10 篇有真 ScoutFlow 历史锚点
- **Tier 2 (rule-derived 但需深度重写)**: AP-VF 全 10 篇 (5 Gate)、AP-MC 全 7 篇 (handoff)、AP-CT 全 6 篇 (token) — 主题对, 但模板 prose 必须重写为不同 cluster 不同语言
- **Tier 3 (仅作枚举/heatmap)**: 10 cluster index + DETECT/PREVENT/ESCAPE catalog + EVIDENCE-SNAPSHOT — 保留作为索引层
- **删除建议**: README 24 段重复 + SELF-AUDIT 15 段重复必删; 80 AP 文件 §1-§8 模板 prose 应被 cluster-specific 真实 prose 替换 (建议拆作 50 真深度 AP, 非 100 模板 fill-in-blank)
