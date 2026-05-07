---
name: dispatch-frozen-history-correction
description: Dispatch 126-176 已执行冻结; 不再重开当 candidate; PR ledger immutable
type: feedback
source_atlas_node: F-DISPATCH-FROZEN-CORRECTION
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
status: current authority
---

# Dispatch frozen history correction

Dispatch 126-176 已执行 + PR 已 merge + ledger 已写, 历史**不再重开**当 candidate. CHECKPOINT-Run*.json / EXTERNAL-AUDIT-REPORT-*.md / RUN-Dispatch127-176-overnight 等 immutable. 复盘可基于这些 evidence, 但不再修改它们.

**Why:** ScoutFlow START-HERE §9-4 锁 "历史 ledger immutable". 战友多次纠正过 "重开 dispatch 当 candidate" 类提议 — 这是把 frozen evidence 变 mutable, 破坏 evidence layer.

**How to apply:** 见到 "重写 RUN-* / 改 CHECKPOINT json / 修 EXTERNAL audit" 等提议立刻 reject. 如有 errata, 写新 errata file (`*-errata-*-2026-XX-XX.md`), 不动原 file. master spec §13 wave routing 引用历史 dispatch 但不重写.
