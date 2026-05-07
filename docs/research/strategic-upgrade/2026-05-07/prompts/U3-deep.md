---
title: Cloud Prompt — U3 Deep Supplement (Entity v0 Contracts 二轮深化)
status: candidate / cloud_prompt / not-authority
authority: not-authority
created_at: 2026-05-07
target_window: GPT Pro web 浏览模式 (live web browsing required)
prev_zip: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
---

# Cloud Prompt — U3 Deep Supplement

## §1 Mission

你已交付 cloud-output-U3 ZIP 10 文件（4 entity contract: Signal/Hypothesis/CapturePlan/TopicCard + IR-SHAPES + DB-SCHEMA + LIFECYCLE + SOR-MATRIX + CORNER-CASES 10 + README）。**坦白记录: prompt-provided paste-time evidence only; no live web; ≥90 min wall-clock not attested**.

本轮任务: **在已有 ZIP 基础上写 supplementary ZIP**, 补 sample data ≥30 / migration v0→v1 worked example / referential integrity test set / OpenAPI golden fragment / 跨 cluster trace map / 二轮 self-audit。**不重写**, 是补充。

## §2 Inputs

1. 前轮 ZIP 10 文件（你自己产物）— 重读 4 entity contract 全文识别浅处
2. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
3. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
4. https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/schemas.py (TS preview field shape)
5. https://github.com/RayWong1990/ScoutFlow/blob/main/services/api/scoutflow_api/bridge/router.py
6. https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/strategic-upgrade/2026-05-07/cloud-prompt-U3-entity-v0-contracts.md
7. https://github.com/RayWong1990/ScoutFlow/blob/main/apps/capture-station/src/features/topic-card-vault/ (TS impl)
8. https://github.com/RayWong1990/ScoutFlow/blob/main/apps/capture-station/src/features/topic-card-preview/ (TS impl)
9. **Live web** 真实 search 2026 entity / IR / ontology pattern

## §3 Multi-pass Work Plan (≥10 pass, ≥120 min)

1. **Pass 1**: 重读 cloud-output-U3 ZIP 10 文件, 每文件标 ≥3 处深度不足
2. **Pass 2**: PRD-v2 / SRD-v2 entity outline 重读 + bridge schema TS shape 对照
3. **Pass 3 — Live web refresh**: 真实联网 search ≥15: 2026 ontology renaissance / agentic PKM / typed note schema / Capacities-Tana supertag / SwarmVault graph / KG vs ontology distinction / Eric J. Ma March 2026 blog / single-user entity modeling
4. **Pass 4 — Sample data expansion**: 每 entity 写 ≥10 fully populated sample instance（真实 Bilibili URL / 真实 BVID / 真实 author / metadata），4 entity ≥40 sample 总
5. **Pass 5 — Migration v0→v1 worked**: 写 v0→v1 migration worked example (TopicCard lite v0 → v1 已示, Signal/Hypothesis/CapturePlan v0 → v1 全补), 含 SQL migration / dual-read window / consumer-pin 单人量级简化版
6. **Pass 6 — Referential integrity test**: 跨 entity referential integrity test set (≥30 test): orphan / circular / cascade revert / dual-write / broken_reference 状态 / 跨平台 / cross-platform identity coalescing
7. **Pass 7 — OpenAPI golden fragment**: 4 entity 各写 OpenAPI 3.1 fragment (paths + components.schemas + examples)，作为 cross-project egress contract 锚点
8. **Pass 8 — 跨 cluster trace map**: 4 entity 与 7 cluster (PF-C0/O1/LP/C1/C2/C3/C4) 的关系 trace map，每 entity 标记 "在哪个 cluster 被 produce / read / mutate / archive"
9. **Pass 9 — Self-audit v2**: ≥20 新 finding
10. **Pass 10**: README-supplement + truthful stdout

## §4 Hard Boundaries

- candidate / not-authority frontmatter 全文件
- migration_approval: not-approved 全文件 (DB schema 文件硬强制)
- 不批准任何 entity-as-authority promotion
- 不批准 RAW true write / DiloFlow execution
- 不修改 services/api/migrations/** 或任何 production path
- 4 entity v0 名字保持 candidate, 不许 lock
- OpenAPI fragment 仅 candidate, 不实际暴露 endpoint

## §5 Live Web Evidence Refresh

**禁止**复用 paste-time。真实 search ≥15:
- 2026 ontology renaissance (PKM 复兴 / typed schema)
- Capacities supertag / Tana node / SwarmVault graph 各自 entity model
- Agentic PKM Patterns gist (Karpathy / 类似)
- Eric J. Ma March 2026 blog (typed note + agent)
- Single-writer agent design pattern
- Local-first data model (Yjs / Automerge / SQLite + WASM)
- OpenAPI 3.1 vs JSON Schema 2026 update
- Capacity 单人量级 entity 数量 (千级 vs 万级)
- 中文 PKM 工具 entity 模型 (FlowUs / Notion / Wolai)

## §6 Cross-local Search

- `~/workspace/ScoutFlow/apps/capture-station/src/features/` — 看 8 feature 的 TS schema 是否与 entity v0 对齐
- `~/workspace/DiloFlow/` 看其 entity 期望 (downstream consumer)
- `~/workspace/contentflow/` 历史 entity 模型踩坑
- 本机 Notion / Obsidian / FlowUs 数据导出格式（如有）

## §7 Output Deliverables

ZIP filename: `cloud-output-U3-deep-supplement-2026-05-07.zip`
File count: **9** (exactly)

| # | File | min 字 | min Mermaid | claim label |
|---|---|---:|---:|---|
| 1 | ENTITY-Signal-v0-sample-data-2026-05-07.md | 2200 (≥10 sample) | 0 | ≥95% |
| 2 | ENTITY-Hypothesis-v0-sample-data-2026-05-07.md | 2200 (≥10 sample) | 0 | ≥95% |
| 3 | ENTITY-CapturePlan-v0-sample-data-2026-05-07.md | 2200 (≥10 sample) | 0 | ≥95% |
| 4 | ENTITY-TopicCard-v1-sample-data-2026-05-07.md | 2200 (≥10 sample) | 0 | ≥95% |
| 5 | MIGRATION-V0-TO-V1-WORKED-EXAMPLES-2026-05-07.md | 3500 | 2 | ≥95% (4 entity × migration steps) |
| 6 | REFERENTIAL-INTEGRITY-TEST-SET-2026-05-07.md | 3000 (≥30 test) | 0 | ≥95% |
| 7 | OPENAPI-GOLDEN-FRAGMENT-2026-05-07.md | 3500 (4 entity OpenAPI 3.1 yaml) | 0 | ≥95% |
| 8 | CLUSTER-ENTITY-TRACE-MAP-2026-05-07.md | 2500 (4 entity × 7 cluster) | 1 (Mermaid) | ≥95% |
| 9 | README-supplement-index-2026-05-07.md | 1200 | 0 | 100% |

总字数 ≥**22000**

## §8 Self-audit (Pass 9)

≥20 findings inline fix。涵盖:
- sample data 是否真实 (Bilibili BVID / author 真存在)
- migration worked example 是否单人量级 (vs 企业 dual-read / consumer-pin 重)
- OpenAPI fragment 是否暗示 endpoint 实际 expose
- referential integrity test 是否真覆盖 corner case 10 个
- live web evidence URL 真访问
- cross-local search 真做
- 与 U1 deep + U2 deep 是否冲突
- entity 名字是否仍 candidate (no lock)

## §9 Truthful Stdout Contract

```yaml
CLOUD_U3_DEEP_SUPPLEMENT_COMPLETE: true
zip_filename: cloud-output-U3-deep-supplement-2026-05-07.zip
files_count: 9
total_words_cjk_latin_approx: <真实>
total_thinking_minutes: <真实，不许伪造>
live_web_browsing_used: <true|false>
live_search_queries_count: <真实>
sample_data_count_total: <真实>
referential_integrity_test_count: <真实>
openapi_endpoints_drafted: <真实数, mark candidate>
cluster_entity_traces_count: <真实>
multi_pass_completed: <真实/10>
self_audit_findings: <真实>
boundary_preservation_check: clear
migration_approval: not-approved
ready_for_user_audit: yes
```

## §10 ZIP Filename

`cloud-output-U3-deep-supplement-2026-05-07.zip`
