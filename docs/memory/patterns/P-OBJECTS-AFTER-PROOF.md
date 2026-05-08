---
name: objects-after-proof
description: 先 proof loop, 再对象化扩张; entity v0 → v1 必须等 proof 跑通
type: project
source_atlas_node: P-OBJECTS-AFTER-PROOF
cross_vendor_readers: [cc0, cc1, codex, gpt-pro, hermes]
memory_role: cross-vendor instinct source
status: reference storage
---

# Objects-after-proof

entity / Workbench / schema 抽象的扩张顺序: **proof loop 跑通 → 真用户使用反馈 → 抽象哪些是真重复 → 对象化**. 倒过来 (先抽象 schema 再做 proof) = `L-OVEROBJECTIFICATION` 踩坑.

**Why:** Wave 4 Phase 2 大量 entity 拆 slot 已 frozen, 但发现 "对象化先于 proof" 是路线 bias. master spec §10 `P-OBJECTS-AFTER-PROOF` pattern + `T-PRODUCT-PROOF-NOT-BREADTH` theme 已锁后续顺序.

**How to apply:** entity v0 → v1 任何升级 PR 必先答 "哪个 proof loop 验证了这个升级是真需要?". 没 proof 数据支持的对象化推迟. C3 lightweight expansion (master spec §13) 只补 proof 真需要的对象化, 不全套.
