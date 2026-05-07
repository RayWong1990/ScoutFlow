---
name: safe-parallel-not-saturate
description: 最大马力 ≠ saturate slot; 安全前提下并行 = boundary 守住 + 主菜对齐
type: feedback
source_atlas_node: F-SAFE-PARALLEL
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
status: current authority
---

# Safe parallel, not saturate

战友"最大马力"原则 ≠ saturate slot 数. "最大马力"是手段, "最高质量"是目的. 跑 12 窗 GPT Pro 但 5 窗远期 spec 用不上 = 浪费战友 paste 带宽 + slot 干预 drift 风险. 真"最大马力" = P0 + 主菜 Codex + 关键 audit 跑到极致, 不是 saturate slot.

**Why:** 实战 (PR #244 / 16 ZIP / 80-pack 跑批) 多次确认: 4 active worker (CC0 + CC1 + GPT Pro + Codex) 协调好 ROI > 12 worker 失控. 5 overflow lane Hold 期间提前出 spec drift 风险 (3 个月后 stack / 红线 / vendor 状况都变了).

**How to apply:** 派单前算 ROI: (a) 真主菜对齐 (今晚必跑); (b) 暖手 (明天用); (c) 远期 (跑了也用不上). a + b 才上, c 砍. 见到 "12 窗都派满"提议, 反问 "哪些是 c 类 drift 风险?". boundary 守住前提下 saturate, 不在 boundary 模糊时 saturate.
