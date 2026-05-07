---
name: direct-merge-ok-not-cross-boundary
description: amend_and_proceed + 单 PR direct merge + admin override OK; 但不许越界
type: feedback
source_atlas_node: F-DIRECT-MERGE-OK
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
status: current authority
---

# Direct merge OK, but not cross-boundary

战友接受: amend_and_proceed pattern (≤2 amend / single PR squash / admin override fail CI 不阻 docs-only PR). 但 "direct merge OK" **不等于**"可越 authority / runtime / migration / overflow lane 边界". 边界在内, merge 模式可松.

**Why:** 历史 PR #122 / #240 / #243 / #244 都用 admin override + amend_and_proceed 模式. ScoutFlow 单人 prosumer + 多 agent 协作场景, ceremony 重 = 损耗大. 但 5 overflow lane / authority files / 历史 ledger immutable 等硬红线无任何 merge 模式可绕.

**How to apply:** PR 启动时分清 "merge ceremony" 和 "boundary discipline". docs-only PR / surface 静态壳 / receipt closure 等 merge 模式可松. 任何涉及 authority / runtime / migration / overflow lane 解禁的 PR 必走完整 dispatch + 外审 + user 拍板. 见到 "既然 admin merge OK 我就 ..." 立刻反问 "改的是 ceremony 还是 boundary?".
