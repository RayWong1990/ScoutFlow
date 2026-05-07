---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "Cluster ED Index — Engineering-Discipline"
kind: "cluster-index"
no_actual_rule_deployment_implied: true
---

# Cluster ED — Engineering-Discipline

[evidence-backed] 本 index 汇总 `Engineering-Discipline` 的候选 anti-pattern。风险画像：工程纪律失守会把 candidate 变成脆弱实现，尤其在测试、hooks、git truth 与破坏性命令上。 本 index 不把任何 candidate spec 提升为 authority；它只提供审计导航、detect/prevent/escape 的快速入口。

## Anti-pattern 清单

| ID | title | risk | introduced/exposed | detect | prevent | linked |
|---|---|---|---|---|---|---|
| AP-ED-01 | No TDD before implementation | high | exposed | audit | template | RB-ED-01 / MOD-ED-01 |
| AP-ED-02 | Coverage threshold below 80 without waiver | medium | exposed | static | hook | RB-ED-02 / MOD-ED-02 |
| AP-ED-03 | Code-review agent skipped | medium | exposed | audit | contract | RB-ED-03 / MOD-ED-03 |
| AP-ED-04 | No verification loop | high | exposed | grep | template | RB-ED-04 / MOD-ED-04 |
| AP-ED-05 | Import path assumption | medium | exposed | static | hook | RB-ED-05 / MOD-ED-05 |
| AP-ED-06 | Diagnose without git fetch | high | exposed | grep | hook | RB-ED-06 / MOD-ED-06 |
| AP-ED-07 | Destructive git misuse | critical | exposed | human | contract | RB-ED-07 / MOD-ED-07 |
| AP-ED-08 | Hooks skipped for speed | high | exposed | grep | hook | RB-ED-08 / MOD-ED-08 |

## Cluster detect matrix

[evidence-backed] 本 cluster 的 detect 入口不是单条正则，而是授权、路径、证据、边界四列一起看。任何一列从 candidate/partial/blocked/not-authority 转为 works/pass/approved/authority，都必须写出来源或回退措辞。


## Prevent placement

[candidate] 最适合落位的是 template/schema/contract，而不是在当前 U11 直接部署 hook。建议每个未来 dispatch row 都包含 `authority_surface_touched`、`user_authorization_ref`、`introduced_or_exposed`、`evidence_label`、`escape_clause` 五个最小字段。

## Escape overview

[candidate] cluster 级逃逸路径：暂停新写入 → 生成 delta table → 重标 claim label → 区分 introduced/exposed → 决策 keep/rollback/defer/amend_and_proceed。对于已 merge 的 PR，优先写 amendment ledger，而不是口头解释。

## Cross-links

- [candidate] `AP-ED-01` ↔ `RB-ED-01` ↔ `MOD-ED-01` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-02` ↔ `RB-ED-02` ↔ `MOD-ED-02` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-03` ↔ `RB-ED-03` ↔ `MOD-ED-03` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-04` ↔ `RB-ED-04` ↔ `MOD-ED-04` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-05` ↔ `RB-ED-05` ↔ `MOD-ED-05` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-06` ↔ `RB-ED-06` ↔ `MOD-ED-06` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-07` ↔ `RB-ED-07` ↔ `MOD-ED-07` ↔ `~/.claude/rules/testing.md`
- [candidate] `AP-ED-08` ↔ `RB-ED-08` ↔ `MOD-ED-08` ↔ `~/.claude/rules/testing.md`

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster ED 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。
