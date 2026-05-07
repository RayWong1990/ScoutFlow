---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "Cluster VF Index — Visual / 5-Gate Failure"
kind: "cluster-index"
no_actual_rule_deployment_implied: true
---

# Cluster VF — Visual / 5-Gate Failure

[evidence-backed] 本 index 汇总 `Visual / 5-Gate Failure` 的候选 anti-pattern。风险画像：强视觉不是审美口号，而是可判定的 5 Gate；技术渲染成功不能替代视觉通过。 本 index 不把任何 candidate spec 提升为 authority；它只提供审计导航、detect/prevent/escape 的快速入口。

## Anti-pattern 清单

| ID | title | risk | introduced/exposed | detect | prevent | linked |
|---|---|---|---|---|---|---|
| AP-VF-01 | Primary title loses hierarchy to subtitle | high | exposed | human | template | RB-VF-01 / P3-VF-01 |
| AP-VF-02 | Subtitle or toast occludes critical content | high | exposed | human | contract | RB-VF-02 / P3-VF-02 |
| AP-VF-03 | Random spacing and alignment | medium | exposed | human | template | RB-VF-03 / P3-VF-03 |
| AP-VF-04 | Contrast below durable review threshold | high | exposed | human | template | RB-VF-04 / P3-VF-04 |
| AP-VF-05 | Decoration heavier than evidence | high | exposed | human | contract | RB-VF-05 / P3-VF-05 |
| AP-VF-06 | Saturation hijacks attention | medium | exposed | human | template | RB-VF-06 / P3-VF-06 |
| AP-VF-07 | CJK/Latin baseline mismatch | medium | exposed | human | template | RB-VF-07 / P3-VF-07 |
| AP-VF-08 | Good-enough visual pass | high | exposed | audit | contract | RB-VF-08 / P3-VF-08 |
| AP-VF-09 | Retrofitted visual after code | high | exposed | audit | template | RB-VF-09 / P3-VF-09 |
| AP-VF-10 | Mobile safe-area occlusion | high | exposed | human | contract | RB-VF-10 / P3-VF-10 |

## Cluster detect matrix

[evidence-backed] 本 cluster 的 detect 入口不是单条正则，而是授权、路径、证据、边界四列一起看。任何一列从 candidate/partial/blocked/not-authority 转为 works/pass/approved/authority，都必须写出来源或回退措辞。

```mermaid
flowchart TD
    A[VF signal] --> B{evidence label present?}
    B -- no --> C[flag needs-amendment]
    B -- yes --> D{authorization ref present?}
    D -- no --> E[mark partial / candidate]
    D -- yes --> F[allow review, not auto-approve]
```

## Prevent placement

[candidate] 最适合落位的是 template/schema/contract，而不是在当前 U11 直接部署 hook。建议每个未来 dispatch row 都包含 `authority_surface_touched`、`user_authorization_ref`、`introduced_or_exposed`、`evidence_label`、`escape_clause` 五个最小字段。

## Escape overview

[candidate] cluster 级逃逸路径：暂停新写入 → 生成 delta table → 重标 claim label → 区分 introduced/exposed → 决策 keep/rollback/defer/amend_and_proceed。对于已 merge 的 PR，优先写 amendment ledger，而不是口头解释。

## Cross-links

- [candidate] `AP-VF-01` ↔ `RB-VF-01` ↔ `P3-VF-01` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-02` ↔ `RB-VF-02` ↔ `P3-VF-02` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-03` ↔ `RB-VF-03` ↔ `P3-VF-03` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-04` ↔ `RB-VF-04` ↔ `P3-VF-04` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-05` ↔ `RB-VF-05` ↔ `P3-VF-05` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-06` ↔ `RB-VF-06` ↔ `P3-VF-06` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-07` ↔ `RB-VF-07` ↔ `P3-VF-07` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-08` ↔ `RB-VF-08` ↔ `P3-VF-08` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-09` ↔ `RB-VF-09` ↔ `P3-VF-09` ↔ `~/.claude/rules/aesthetic-first-principles.md`
- [candidate] `AP-VF-10` ↔ `RB-VF-10` ↔ `P3-VF-10` ↔ `~/.claude/rules/aesthetic-first-principles.md`

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VF 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。
