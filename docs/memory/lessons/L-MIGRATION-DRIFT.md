---
name: migration-drift
description: DB schema / migration 不允许跟 candidate spec 一起偷渡; 必须独立 dispatch + 外审 + dbvnext_migration lane
type: project
source_atlas_node: L-MIGRATION-DRIFT
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
memory_role: cross-vendor instinct source
risk_if_forgotten: critical
status: reference storage
---

# Migration drift

DB schema 改动 / migration script / entity v0→v1 / vault schema upgrade 等任何持久化层变化, 必须走独立 dispatch + 外审 + `dbvnext_migration` overflow lane 解禁 PR. 不允许在 candidate spec 或 frontend PR 里 implicit 携带 migration.

**Why:** 5 overflow lane 之一 `dbvnext_migration` 设计初衷就是隔离 schema 变更. SRD-v3 db-vnext candidate 仍在 candidate north-star 状态, 任何 promoted 化必须走 amend PR + user 拍板. 历史多次出现 "PRD-v3 supplement 提到新字段 → 被理解为 schema 已批" 的滑坡.

**How to apply:** PR review 时 grep `migration` / `schema` / `ALTER` / `CREATE TABLE` / `entity_v` 等关键词, 任一命中立刻反问 "走 dbvnext_migration lane 了吗?". commander prompt 写明 "本 PR 不含 schema change". CI 加 schema-diff guard (post-merge follow-up).
