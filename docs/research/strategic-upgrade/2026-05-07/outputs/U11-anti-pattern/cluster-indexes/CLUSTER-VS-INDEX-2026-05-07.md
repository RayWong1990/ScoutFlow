---
status: "candidate / cloud_prompt / not-authority"
authority: "not-authority"
created_at: "2026-05-07"
title: "Cluster VS Index — Vendor-SupplyChain"
kind: "cluster-index"
no_actual_rule_deployment_implied: true
---

# Cluster VS — Vendor-SupplyChain

[evidence-backed] 本 index 汇总 `Vendor-SupplyChain` 的候选 anti-pattern。风险画像：把 vendor 或开源工具当作永久可用默认能力，会制造法律、安装、成本和替代性风险。 本 index 不把任何 candidate spec 提升为 authority；它只提供审计导航、detect/prevent/escape 的快速入口。

## Anti-pattern 清单

| ID | title | risk | introduced/exposed | detect | prevent | linked |
|---|---|---|---|---|---|---|
| AP-VS-01 | Single vendor lane lock-in | high | exposed | audit | contract | RB-VS-01 / P4-VS-01 |
| AP-VS-02 | Vendor selection without spike audit | high | exposed | audit | template | RB-VS-02 / P4-VS-02 |
| AP-VS-03 | BBDown cease-and-desist not rechecked | critical | exposed | human | contract | RB-VS-03 / P4-VS-03 |
| AP-VS-04 | yt-dlp legal refresh skipped | critical | exposed | human | contract | RB-VS-04 / P4-VS-04 |
| AP-VS-05 | ASR vendor not benchmarked | high | exposed | audit | template | RB-VS-05 / P4-VS-05 |
| AP-VS-06 | Whisper local install not verified | medium | exposed | grep | hook | RB-VS-06 / P4-VS-06 |
| AP-VS-07 | Cloud API treated as free | high | exposed | audit | template | RB-VS-07 / P4-VS-07 |

## Cluster detect matrix

[evidence-backed] 本 cluster 的 detect 入口不是单条正则，而是授权、路径、证据、边界四列一起看。任何一列从 candidate/partial/blocked/not-authority 转为 works/pass/approved/authority，都必须写出来源或回退措辞。


## Prevent placement

[candidate] 最适合落位的是 template/schema/contract，而不是在当前 U11 直接部署 hook。建议每个未来 dispatch row 都包含 `authority_surface_touched`、`user_authorization_ref`、`introduced_or_exposed`、`evidence_label`、`escape_clause` 五个最小字段。

## Escape overview

[candidate] cluster 级逃逸路径：暂停新写入 → 生成 delta table → 重标 claim label → 区分 introduced/exposed → 决策 keep/rollback/defer/amend_and_proceed。对于已 merge 的 PR，优先写 amendment ledger，而不是口头解释。

## Cross-links

- [candidate] `AP-VS-01` ↔ `RB-VS-01` ↔ `P4-VS-01` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-02` ↔ `RB-VS-02` ↔ `P4-VS-02` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-03` ↔ `RB-VS-03` ↔ `P4-VS-03` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-04` ↔ `RB-VS-04` ↔ `P4-VS-04` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-05` ↔ `RB-VS-05` ↔ `P4-VS-05` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-06` ↔ `RB-VS-06` ↔ `P4-VS-06` ↔ `~/.claude/rules/security.md`
- [candidate] `AP-VS-07` ↔ `RB-VS-07` ↔ `P4-VS-07` ↔ `~/.claude/rules/security.md`

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。

[derived] 复核提醒：Cluster VS 的每个条目都要避免把 prompt 中的期望写成已执行事实。若 U9/U10 实源缺失，cross-link 只能保持候选映射；若 PR 或 local pack 证据无法证明具体历史实例，应在 self-audit 中降级 attribution confidence。
