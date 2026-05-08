---
name: overflow-not-blocker
description: overflow registry 收纳 blocked options 不阻塞 product main; 5 lane Hold ≠ wave 卡死
type: project
source_atlas_node: P-OVERFLOW-NOT-BLOCKER
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
memory_role: cross-vendor instinct source
status: reference storage
---

# Overflow registry — not a blocker

5 overflow lane (true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench) 全 Hold **不阻塞** product main wave. lane 是 captured options, 等 user 拍板 + dispatch + 外审解禁. 主线推进可绕过 overflow, 用 stub / preview / candidate.

**Why:** master spec §13 wave routing 设计就是 W2C / W2D / W3E / W6K 等可在 overflow lane Hold 期间推进 (用 mock data / preview / static shell). overflow lane 解禁 (W4F / W4G / W5H / W6J) 是后续 wave, 不是阻塞前置.

**How to apply:** 见到 "5 lane 全 Hold, 我们没法做" = 错. 反问 "这个 wave 真依赖哪条 lane 解禁?". 大部分 product wave 用 stub / mock / preview 推进. lane 解禁走单独 PR (类似 PR #244 doc 整治 / write_enabled flag flip), 不夹带在普通 wave.
