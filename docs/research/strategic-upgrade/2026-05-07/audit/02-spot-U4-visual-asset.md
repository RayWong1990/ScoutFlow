---
title: Spot Check — U4-visual-asset
status: candidate / audit_report / not-authority
created_at: 2026-05-07
---

# Spot Check — U4-visual-asset

## §1 文件抽样
- README-deliverable-index (truthful stdout 含 13 节 + 自检 20 条)
- SELF-AUDIT 内嵌于 README §3 (无独立文件, sniff 报 NOT FOUND 是误判)
- MASTER 内嵌于 README §12 audit-ready summary
- Random 3: MODULE-visual-asset-spec / MODULE-prompt-template-spec / SINGLE-USER-IMPLEMENTATION-BUDGET / CROSS-MODULE-CONTRACT (4 抽)

## §2 SQLite DDL + Python CRUD 真完整?
**真**. visual_asset DDL 含 3 表 (`visual_assets` / `visual_asset_events` / `visual_asset_phase_use`) + 4 索引 + 1 trigger + FK on/off + CHECK 约束 (kind/state/use_kind enum). Python CRUD `add_asset` / `transition` / `list_reuse` 含 sha256 / PIL dims / uuid / state-guard `cannot lock asset before 5-Gate pass`. prompt_template DDL 同样真 (3 表 + 3 索引 + lineage `parent_prompt_id` / `superseded_by`). thumbnail/pHash 6 步算法 (Pillow + dHash inline + integrity_mismatch 触发条件). **非占位文字**.

## §3 prosumer ≤300 行边界
LOC 预算: visual_assets ~240 / prompt_templates ~220 / design_tokens ~180 / pattern_library ~210 / gate_audit ~240 / contract_audit ~160 + schema 120 = **~1,250 LOC**, 单模块均 <300 行硬上限. development day 估 4.75-5.5 days. 无 Tailwind / shadcn / Panda / RBAC / cloud sync — 边界严守 prosumer 而非 enterprise DAM.

## §4 cross-link
CROSS-MODULE-CONTRACT 提供 6 条 link (visual_assets.prompt_id → prompt_templates / pattern_tag → pattern_entries / token_visual asset → token extraction prompt 等), 含 hard-FK (co-located) vs soft-FK (modular) 双层 posture + 跨模块 SQL 5.1 (asset+prompt+pattern join). lock 前需跑 contract audit query.

## §5 Boundary 守
**严守**. 全 10 文件 frontmatter `write_enabled: false / claim_scope: spec-only`. 每个 module 都有 "Source Register / 证据边界" 段, 明示 `~/workspace/ScoutFlow / aesthetic-first-principles.md / PF-V INDEX.csv` **未读**, 全标 `needs_local_refresh / live_web_not_used`. `locked` state 显式定义为 "visual asset lock only, not product authority". S00-S18 / Pattern A-J **绝不 fabricate bodies**, 留 placeholder. 无 secret hit / 无 5 overflow / 无 unlock 暗示.

## §6 Verdict
**`CLEAR`** — schema/CRUD/budget/边界四层都过得硬, 是 spec 而非 boilerplate.

## §7 Promote 建议
- **Tier 1 promote**: `MODULE-visual-asset-spec` (DDL + state machine 5 态 + CRUD + dedupe pHash 阈值) → 可作为 `tools/u4_visual_assets.py` 实现 contract
- **Tier 1 promote**: `5-GATE-AUTOMATION-HOOKS` lock guard → 进 prevent rule contract
- **instrument**: `PF-V-INTEGRATION-MAP` header-driven importer → 等 user 提供 INDEX.csv 后升级 verified mapping
- 不要 Tier 1 promote: `LIVE-WEB-EVIDENCE` (28 URL seeds 全未验)
- README §3 self-audit 20 条已是优质 ledger, 可拆出独立 SELF-AUDIT 文件供 sniff-test 自动识别
