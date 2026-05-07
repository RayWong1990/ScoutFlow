---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "Cluster BL Index — Boundary-Leak / Overflow Slip"
kind: "cluster-index"
no_actual_rule_deployment_implied: true
---

# Cluster BL — Boundary-Leak / Overflow Slip

[evidence-backed] 本 index 汇总 `Boundary-Leak / Overflow Slip` 的候选 anti-pattern。风险画像：候选态、预览态、runtime gate 与 true write 被混淆，导致 blocked lane 偷跑。 本 index 不把任何 candidate spec 提升为 authority；它只提供审计导航、detect/prevent/escape 的快速入口。

## Anti-pattern 清单

| ID | title | risk | introduced/exposed | detect | prevent | linked |
|---|---|---|---|---|---|---|
| AP-BL-01 | write_enabled=False implies future unlock | critical | exposed | grep | contract | RB-BL-01 / P3-BL-01 |
| AP-BL-02 | BBDown live runtime implied approval | critical | exposed | grep | schema | RB-BL-02 / P3-BL-02 |
| AP-BL-03 | ASR runtime implied approval | critical | exposed | grep | schema | RB-BL-03 / P3-BL-03 |
| AP-BL-04 | Browser automation implied approval | critical | exposed | grep | contract | RB-BL-04 / P3-BL-04 |
| AP-BL-05 | Migration implied approval | critical | exposed | grep | hook | RB-BL-05 / P3-BL-05 |
| AP-BL-06 | Five overflow lanes unlocked in one PR | critical | exposed | audit | contract | RB-BL-06 / P3-BL-06 |
| AP-BL-07 | Dispatch schema lacks can_open flags | high | exposed | static | schema | RB-BL-07 / P3-BL-07 |
| AP-BL-08 | Vendor candidate silently accepted | high | exposed | grep | contract | RB-BL-08 / P3-BL-08 |
| AP-BL-09 | Preview-only drifts into production write | critical | exposed | grep | hook | RB-BL-09 / P3-BL-09 |
| AP-BL-10 | Candidate file silently becomes authority | critical | exposed | grep | template | RB-BL-10 / P3-BL-10 |

## Cluster detect matrix

[evidence-backed] 本 cluster 的 detect 入口不是单条正则，而是授权、路径、证据、边界四列一起看。任何一列从 candidate/partial/blocked/not-authority 转为 works/pass/approved/authority，都必须写出来源或回退措辞。

```mermaid
flowchart TD
    A[BL signal] --> B{evidence label present?}
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

- [candidate] `AP-BL-01` ↔ `RB-BL-01` ↔ `P3-BL-01` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-02` ↔ `RB-BL-02` ↔ `P3-BL-02` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-03` ↔ `RB-BL-03` ↔ `P3-BL-03` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-04` ↔ `RB-BL-04` ↔ `P3-BL-04` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-05` ↔ `RB-BL-05` ↔ `P3-BL-05` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-06` ↔ `RB-BL-06` ↔ `P3-BL-06` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-07` ↔ `RB-BL-07` ↔ `P3-BL-07` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-08` ↔ `RB-BL-08` ↔ `P3-BL-08` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-09` ↔ `RB-BL-09` ↔ `P3-BL-09` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-BL-10` ↔ `RB-BL-10` ↔ `P3-BL-10` ↔ `~/.claude/rules/security.md`

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster BL 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。
