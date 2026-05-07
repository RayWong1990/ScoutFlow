---
title: Cloud GPT Pro Prompt — U3 Entity v0 Contracts (Signal/Hypothesis/CapturePlan/TopicCard)
status: candidate / cloud-prompt / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
target_writer: Cloud ChatGPT Pro single window (deep thinking mode, ≥1.5h)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow (public during the 4h cloud window)
target_output: ZIP bundle, 10 markdown files, total ~12K Chinese+English words
deliverable_kind: download_link
expected_thinking_time: 100-150 minutes
relates_to:
  - SRD §1.3 outline: signals / hypotheses / capture_plans / topic_cards (future)
  - C1-02 topic-card-lite v0 (6 字段 landed in PR #240)
  - C1-03 historical asset extraction from T-P1A-124/125 (landed in PR #240)
  - past wave5 candidates: docs/research/wave5/topic-card-entity-surface-candidate-2026-05-05.md
---

# Cloud GPT Pro Prompt — U3 Entity v0 Contracts (4 Entity)

> Paste this entire document into Cloud ChatGPT Pro deep-thinking window (separate from U1, U2).
> Output deliverable = a single download link to a ZIP file containing 10 markdown files.
> Expected total deep-thinking duration: 100-150 minutes minimum.

---

## §0 Pre-flight

- repo PUBLIC during 4h cloud window (per master pre-flight)
- baseline_origin_main: `ea509022eb05a552777373394a6fc2a5077f27f6`
- 3 cloud window 同时跑（U1 / U2 / U3）

---

```
<<<CLOUD U3 BEGIN>>>

You are Cloud ChatGPT Pro acting as a senior knowledge graph + ontology architect for the ScoutFlow project. Your single mission is to author 4 entity v0 contracts (Signal / Hypothesis / CapturePlan / TopicCard v1) plus IR shapes, candidate DB schema, lifecycle state machines, SoR matrix update, 8 corner cases, and a transition guide. Output is a downloadable ZIP bundle with 10 markdown files.

This is candidate research authoring only. It is NOT DB schema migration approval, NOT runtime approval, NOT entity-as-authority promotion. The user will audit the ZIP locally before any promotion decision.

You must take at least 75 minutes of deep thinking BEFORE producing the final output.

## §1 Project Identity

- repo: https://github.com/RayWong1990/ScoutFlow (PUBLIC during 4h work)
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline: `ea509022eb05a552777373394a6fc2a5077f27f6`
- Single-user, local-first, evidence-anchored capture system

## §2 Entity Definition (sourced from SRD-v2 §1.3 outline + 4 run 实证)

### 2.1 Signal
- 当前: SRD §1.3 outline，无 schema，无 lifecycle
- v0 含义: 用户 capture 的可观察信号源（一段 metadata / 一段 transcript / 一个评论 trend / 一个数据点）
- 在 ScoutFlow 角色: capture 的 observation primitive (≠ capture itself; capture 是 record，signal 是 observation derived from records)
- 来源: T-P1A-024 capture-scope-state-table 探索过

### 2.2 Hypothesis
- 当前: SRD §1.3 outline，无 schema，无 lifecycle
- v0 含义: 用户基于多 signal 形成的 testable claim ("这个 creator 在涨粉" / "这个话题 q1 有上升")
- 在 ScoutFlow 角色: signal 间的关系图节点，用户后续 follow / park / reject
- 来源: post-dispatch176 strategy candidate 提到 hypothesis 这一层

### 2.3 CapturePlan
- 当前: SRD §1.3 outline，无 schema，无 lifecycle
- v0 含义: 用户对一组 signal/hypothesis 的"未来 capture 编排"（哪些 URL / 哪些 frequency / 哪些 enrichment level）
- 在 ScoutFlow 角色: 把"过去观察"升级为"未来主动 capture"
- 来源: T-P1A-024 capture-scope-state-table + 145/146 历史 asset

### 2.4 TopicCard v1 (extends C1-02 lite v0)
- 当前: C1-02 lite v0 已 land (6 字段: title / platform_item_id / canonical_url / capture_id / export_posture / target_path)
- v1 扩展: 含 enrichment metadata + signal 引用 + hypothesis 引用 + capture_plan 引用 + lifecycle state
- 在 ScoutFlow 角色: 对外 export 的 portable knowledge unit
- 来源: C1-02 contract 已 landed; C1-04 transformer 已实现

## §3 Required Inputs

### §3.1 Base authority + SRD-v2 §1.3

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md (focus §1.3, §2.7)
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md (focus §1)

### §3.2 C1-02 / C1-03 / C1-04 / C1-05 landed material

- C1-02 contract: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/specs/post-frozen/topic-card-lite-contract-v0.md
- C1-03 historical extract: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c1-historical-asset-extraction-145-146.md
- C1-04 transformer code: https://github.com/RayWong1990/ScoutFlow/blob/main/apps/capture-station/src/features/topic-card-preview/topicCardLite.ts
- C1-05 markdown companion: https://github.com/RayWong1990/ScoutFlow/blob/main/apps/capture-station/src/features/topic-card-vault/

### §3.3 Wave 5 candidate research (frozen but evidence-only reference)

- topic card entity: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/wave5/topic-card-entity-surface-candidate-2026-05-05.md
- hypothesis comparison UX: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/wave5/hypothesis-comparison-ux-candidate-2026-05-05.md (if exists)
- signal ingestion audit: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/wave5/signal-ingestion-audit-lane-candidate-2026-05-05.md (if exists)
- capture plan IA: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/wave5/capture-plan-frontend-ia-candidate-2026-05-05.md (if exists)
- T-P1A-024 capture-scope: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md

### §3.4 ScoutFlow ↔ RAW SoR matrix (current source)

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-scoutflow-raw-bridge-candidate-2026-05-05.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/scoutflow-raw-sor-handoff-matrix.md

### §3.5 Run-3+4 PF-C1 results

- Run-3+4 report: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md
- C1-08 user verdict: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/evidence/PF-C1-08-human-verdict-2026-05-06.md
- C1-09 false-positive log: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/c1-false-positive-edit-cost-log.md

### §3.6 DB Schema candidate (for Phase 2 reference)

- T-P1A-025 DB ledger vNext: https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-025-db-ledger-vnext.md

## §4 Required Output Structure — ZIP Bundle Schema (STRICT)

ZIP `cloud-output-U3-entity-v0-contracts-2026-05-07.zip` 含 **10 markdown 文件**:

### §4.1 Files 1-4: 4 Entity v0 Contracts (≥1500 字 each)

For each entity, file `ENTITY-<Name>-v0-contract-2026-05-07.md`. Required sections:

1. **frontmatter**: status: candidate / entity_v0_contract / not-authority
2. **§1 Identity**: name / role / IR layer (preview-only candidate IR; not DB authority object)
3. **§2 Field Schema** (≥7 字段，含):
   - id (ULID generation)
   - canonical_url (if applicable)
   - source_capture_id (link to existing capture)
   - core typed fields per entity
   - lifecycle state field (enum)
   - claim label per field (canonical / candidate / tentative)
4. **§3 IR Shape** (JSON schema candidate, with required vs optional)
5. **§4 Lifecycle State Machine** (Mermaid stateDiagram-v2; ≥4 states + transition gates)
6. **§5 Relations to Other Entities** (e.g. Signal → Hypothesis many-to-many, Hypothesis → CapturePlan one-to-many)
7. **§6 Allowed Operations** (create / read / project / archive — NOT delete; per single-writer single-owner model)
8. **§7 SoR (Source of Record)** (ScoutFlow SQLite vs RAW vs DiloFlow — entity 归属哪个)
9. **§8 IR vs DB authority gap** (当前 v0 只是 IR shape; Phase 2 DB schema 升级前不上库)
10. **§9 v0 vs v1 vs v2 Roadmap** (3 个 future iteration 概念)
11. **§10 Sample Instance** (1-2 个 fully populated example with all fields)
12. **§11 Risks + Open Questions** (≥3 risks + ≥3 open questions)

#### TopicCard v1 special section
- §1.5 "Extends C1-02 lite v0": 列哪些字段 carry-over，哪些新加，哪些 reshape
- §1.6 "Migration from lite v0 to v1" 步骤

### §4.2 File 5: `IR-SHAPES-CROSS-ENTITY-2026-05-07.md` (≥1200 字)

- 4 entity 之间的关系图（Mermaid ER diagram）
- IR carry-forward 与 promote 路径
- type alignment (TypeScript type alias candidates)
- JSON shape 跨 entity 一致性规则
- "anti-second-inbox" 规则: signal/hypothesis 不重 emit 同一 capture 的 derived state

### §4.3 File 6: `DB-CANDIDATE-SCHEMA-PHASE-2-2026-05-07.md` (≥1500 字)

- Phase 2 SQLite candidate schema (4 entity 各自 table + relation tables)
- frontmatter 必标 `migration_approval: not-approved`，每段 reminder "this is candidate; no migration without lane-4 unlock per U2"
- 含: CREATE TABLE statements (candidate only) / FOREIGN KEY relations / index recommendations / state words extension
- 必引 t-p1a-025 DB vNext 已 explore 的字段
- "NOT in this schema" 段: 列举 v0 不上库的字段（preview_only / synthetic_partial / candidate-only）
- 含 mermaid ER diagram

### §4.4 File 7: `LIFECYCLE-STATE-MACHINES-2026-05-07.md` (≥1200 字)

- 4 entity 各自 state machine 整合到 1 张图
- 跨 entity 转移规则 (e.g. Signal → Hypothesis 必须经 user verdict gate)
- "rollback" 路径 (Hypothesis can be archived but not deleted)
- "second-inbox failure" 状态触发 / 检测 / 修复
- 含 4 个独立 mermaid stateDiagram-v2 + 1 张总图

### §4.5 File 8: `SOR-MATRIX-V2-2026-05-07.md` (≥1000 字)

- 扩展 post-dispatch176 SoR matrix 至 4 entity + RAW + DiloFlow
- 每 entity / 每 surface 的 owner / writer / reader / projection target
- 必含: ScoutFlow → DiloFlow handoff for compiled topic_card
- 必含: ScoutFlow → RAW handoff for raw note candidate (扩展 PF-C2-10)
- 含: dual-SoR 风险 + 防御措施
- 含: matrix 在 v2 vs v3 的演化对比表

### §4.6 File 9: `CORNER-CASES-AND-ANTI-PATTERNS-2026-05-07.md` (≥1500 字)

8+ corner cases，每 case 有:
- ID
- 触发条件
- 当前 IR / SoR 行为
- 预期 v0 行为
- 异常 fallback
- 测试方法

必含 corner cases:
1. Signal 引用同一 capture 多次（duplicate dedup）
2. Hypothesis 引用 conflict signal（A 说 up, B 说 down）
3. CapturePlan 触发后 capture 失败（plan rollback）
4. TopicCard v1 升级时 lite v0 字段被 reshape（migration error）
5. ScoutFlow 修改 entity 同时 RAW 已 intake（dual-write conflict）
6. user reject hypothesis 但已生成下游 capture_plan（cascade revert）
7. Signal 来源 capture 被 user 删除（broken reference）
8. 同一 capture 被多个 user 工作流引用（sharing）
9. Cross-platform Signal (e.g. Bilibili capture cross-reference XHS post)
10. AI-generated Signal vs human-validated Signal 边界

### §4.7 File 10: `README-deliverable-index-2026-05-07.md` (≥500 字)

- 列全 10 文件 + 字数 + claim label 占比
- 多 pass 工作流摘要
- audit checklist (user 收到 ZIP 后 5+ 项)
- 与 U1 / U2 输出的协作锚点（U3 输出是 U1 SRD-v3 §4 entity outline + U2 Lane-4/5 unlock 的 design input）

---

## §5 Multi-Pass Work Plan (10 Pass, ≥75 min cumulative)

### Pass 1: SRD-v2 §1.3 + outline read (10 min)
Extract every word about signals / hypotheses / capture_plans / topic_cards. Map current state.

### Pass 2: C1-02 / C1-03 / C1-04 / C1-05 landed material read (15 min)
Read TopicCard lite v0 contract + transformer + markdown companion. Identify which lite v0 fields are stable, which need v1 extension.

### Pass 3: Wave 5 candidate research read (10 min)
Read topic-card-entity-surface + hypothesis-comparison-ux + signal-ingestion + capture-plan-IA. Extract candidate vocabulary.

### Pass 4: 2-month web evidence integration (15 min)
Integrate following findings:
- 2026 ontology renaissance year (Gartner D&A Summit, semantic layers + knowledge graphs as agent infrastructure)
- Agentic PKM Patterns gist (MarkBruns, GitHub): auto-classification + capture pipeline + voice/multimodal + bridge/hypothesis notes + self-evolving systems
- Eric J. Ma March 2026 blog: Obsidian + structured note types + AI agent skills reduced KM time 30-40% → <10%
- Capacities / Tana supertag patterns: object-like tags as schema model
- Local-first 2026 stack: plain text + SQLite FTS + local embeddings + MCP server
- Knowledge graph vs ontology distinction: ontology defines meaning + rules; KG contains instance data
- Obsidian YAML frontmatter as schema enforcement vehicle
- SwarmVault local-first RAG knowledge vault example (markdown on disk + SQLite FTS + local embeddings + MCP)
- Atomic notes / Evergreen notes / MOCs (Maps of Content) PKM frameworks
- PARA / Zettelkasten / Johnny Decimal taxonomies

### Pass 5: 4 entity v0 contract authoring (25 min, ~6 min each)
For each entity (Signal / Hypothesis / CapturePlan / TopicCard v1), author full v0 contract per §4.1 schema. Include sample instance with realistic data.

### Pass 6: Cross-entity IR shape + DB schema authoring (15 min)
Author Files 5 (IR cross-entity) + 6 (DB candidate schema). Mermaid ER diagram. CREATE TABLE statements with `[candidate]` label.

### Pass 7: Lifecycle + SoR + corner cases (15 min)
Author Files 7 (lifecycle state machines) + 8 (SoR matrix v2) + 9 (corner cases ≥8 with 10 included).

### Pass 8: Adversarial self-audit (10 min)
Find ≥8 issues:
- entity 字段是否存在 ambiguity (e.g. Signal vs capture observation 边界模糊)
- DB schema 是否暗推 lane-4 migration unlock
- SoR matrix 是否引入 dual-write
- corner case 是否覆盖 cross-platform / multi-user / sharing 场景
- lifecycle 状态机是否有 deadlock / unreachable state
- claim label 是否 drift
- v0 vs v1 vs v2 roadmap 是否过度 commit
- 是否引用 PF-V 视觉 lane 之外的视觉决策（不应推 visual gate）

### Pass 9: Format guard + frontmatter scan (5 min)
### Pass 10: README index + ZIP package (5 min)

---

## §6 Self-Audit Checklist (15 items)

1. ZIP contains exactly 10 files
2. Each entity contract ≥1500 字
3. Each entity has 4-state lifecycle (≥create/active/archived/deprecated)
4. DB candidate schema includes `migration_approval: not-approved`
5. SoR matrix v2 covers ScoutFlow + RAW + DiloFlow
6. ≥8 corner cases, each with fallback
7. TopicCard v1 special section: extends C1-02 lite v0 + migration steps
8. No entity claims to be DB authority (all v0 IR layer)
9. Mermaid diagrams syntactically valid (≥4 stateDiagram-v2 + 2 ER)
10. Web 2-month evidence ≥4 of 10 cited
11. Each entity has Sample Instance with realistic data
12. Anti-second-inbox rule explicit (in IR-SHAPES file)
13. Risks + Open Questions ≥3 each per entity
14. Cross-entity relations defined (Signal-Hypothesis-CapturePlan chain)
15. README index lists all files + word count + claim label ratio

---

## §7 Hard Boundaries (违反任一即整 ZIP reject)

1. 不声明任何 entity 已 promoted 为 DB authority
2. 不声明 lane-4 dbvnext_migration 已 unlock
3. 不写 services/api/migrations/** 任何路径暗示
4. 不声明 lite v0 已可 promote 为 v1 (v1 提议是 candidate; 实际 promote 须经 amendment + audit)
5. 不修任何 production code path
6. 不破 single-writer single-owner SoR 假设
7. 不暗推 multi-user / collab / SaaS 场景 (single-user local-first 必须保持)
8. 不引入 ScoutFlow 已禁的 vendor (BBDown / yt-dlp / ffmpeg as enriched signal source 不许暗用)
9. 不 skip claim label
10. 不 deliver < 10 files / < 10K cumulative words

---

## §8 Quality Criteria

| 维度 | 权重 | 评分细节 |
|---|---:|---|
| Entity field completeness | 25% | 每 entity ≥7 字段 + sample instance |
| Lifecycle clarity | 20% | mermaid + 4-state + transition gates |
| Cross-entity relations | 15% | ER diagram + JSON shape alignment |
| SoR matrix v2 coverage | 15% | ScoutFlow + RAW + DiloFlow |
| Corner case robustness | 10% | ≥8 cases + fallback |
| Web evidence integration | 10% | ≥4 of 10 web 2-month findings |
| Boundary preservation | 5% | no migration / authority leak |

---

## §9 Format Guard

- frontmatter scanner: 10 文件全 `candidate / not-authority`
- claim label scanner: 80%+ paragraphs labeled
- mermaid scanner: stateDiagram-v2 / erDiagram / 各 ≥4
- migration redline scanner: no "migration is approved" outside `[tentative candidate]` future-conditional
- entity DB-authority redline scanner: no "Signal is in DB" without `[tentative candidate]` Phase 2 conditional
- word count scanner: each file meets §4 word target

---

## §10 Stdout Output Contract

```
CLOUD U3 ENTITY-V0-CONTRACTS COMPLETE
deliverable_url: <download link>
zip_filename: cloud-output-U3-entity-v0-contracts-2026-05-07.zip
files_count: 10
total_words: <number ≥10000>
total_thinking_minutes: <number, ≥75>
multi_pass_completed: 10/10
self_audit_findings: <count ≥8>
critical_issues_fixed_inline: <count>
critical_issues_remaining: <count, should be 0>
entity_coverage:
  signal_v0: <wordcount>
  hypothesis_v0: <wordcount>
  capture_plan_v0: <wordcount>
  topic_card_v1: <wordcount>
mermaid_diagrams_count: <number, ≥6>
corner_cases_count: <number, ≥8>
sample_instances_count: <number, ≥4>
web_evidence_findings_used: <number out of 10>
boundary_preservation_check: clear / concern / reject
ready_for_user_audit: yes / no
```

---

## §11 Web Evidence (paste-time evidence layer, 必引)

### §11.1 2026 Ontology Renaissance

- Gartner D&A Summit 2026 positioned semantic layers + knowledge graphs as foundational infrastructure for agentic AI.
- Ontology defines meaning + rules; knowledge graph contains instance data.
- A knowledge graph platform models business entities, their relationships, and their meaning across systems, then makes that structured context available to both human analysts and AI systems.
- Netflix incident knowledge case study: ontology captures, structures, preserves machine-readable triple data structure.

### §11.2 Agentic PKM Patterns (MarkBruns gist)

- Auto-classification schema: agents classify raw captures into structured schemas (PARA folders or atomic Zettel notes), apply tags/metadata, enforce templates.
- Capture pipelines: Obsidian Web Clipper + AI Interpreter (Gemini/Claude) auto-summarizes, extracts YAML frontmatter, files to /raw-inbox.
- Voice/multimodal: SpeakNote / Note Companion → Whisper/Deepgram transcription + entity tagging.
- Bridge/hypothesis notes: custom MCP agents using vector search + LLM propose bridge notes between domains.
- Self-evolving systems: progressive AKM loops auto-fine-tune RAG embeddings.

### §11.3 Eric J. Ma March 2026 blog

- Obsidian + AI coding agents + structured note types reduced KM overhead from 30-40% → <10%.
- Plain text + structured note types + agent skills.
- Plain text turned out to be the right format for 2025 and 2026 KM.

### §11.4 Capacities / Tana supertag patterns

- Supertags (Tana) apply template power to each note, adding reusable metadata that simplifies search.
- Capacities object-like tags reuse certain types of notes for powerful resurfacing.
- Useful reference model for typed-note schemas (signal, hypothesis, claim, evergreen) inside Obsidian via YAML frontmatter.

### §11.5 Local-first 2026 canonical stack

- plain text + SQLite FTS + local embeddings + MCP server is emerging canonical pattern.
- SwarmVault: local-first RAG knowledge vault (compiles raw sources into durable markdown wiki with knowledge graph + hybrid SQLite FTS + embeddings; MCP server for LLM access).
- All data on disk; no data leaves laptop.

### §11.6 Obsidian PKM evergreen / atomic / MOC frameworks

- Evergreen notes: stand-alone insights remaining relevant over time; backlinks + unlinked mentions create idea network.
- MOCs: manually curated index pages linking related notes, similar to Wikipedia category pages.
- Atomic notes / PARA / Zettelkasten / Johnny Decimal / FILE / LIFT taxonomies.

### §11.7 Knowledge Graph vs Ontology

- Ontology = formal explicit specification of shared conceptualization; defines types, relationships, constraints, rules; semantic blueprint for consistency.
- Knowledge graph = instance data (entities + edges); follows ontology rules.
- Conceptual pivot: ontology defines meaning + rules; KG contains instance data.

### §11.8 Obsidian YAML frontmatter as schema enforcement

- Dataview / Templater / Tasks plugins enforce schema via YAML.
- Template-bound note types simplify resurfacing, search, agentic queries.

### §11.9 RedShop e-commerce data new frontier (April 2026)

- Xiaohongshu launched RedShop for US users in April 2026.
- Product listings live in /goods-detail/ separate from social /explore/ posts.
- Implication for ScoutFlow Lane-2: future product-data signal lane separate from creator-content signal lane.

### §11.10 AI agent fleet patterns

- Orchestrator-worker pattern accounts for ~70% of production multi-agent.
- Pass complete context to each sub-agent (sub-agents can't see orchestrator's history).
- Output schema defined before build avoids merge complexity.
- Per-entity scope owner (single-writer) prevents infinite handoff loops.

---

## §12 Sibling Project Cross-Reference

- **DiloFlow**: channel 看见看不见, downstream consumer of TopicCard v1 + capture_plan output. SoR matrix v2 must include DiloFlow as `compiled topic_card consumer + script_seed origin`.
- **ContentFlow legacy**: ingest-pipeline + topic-engine had earlier signal taxonomy. Reference for inspiration only; do not directly couple v0 to legacy.
- **hermes-agent**: orchestration sidecar with openai venv. Phase 2 LLM normalization (signal-to-hypothesis bridge note generation) could host here.

## §13 If Repo is Private (Inline Fallback Mode)

If fetch returns 404, ask user to flip public OR paste inline content of: SRD-v2 + C1-02 contract + 4 wave5 candidate files + Run-3+4 report + ScoutFlow-RAW SoR matrix. Do NOT proceed without inputs.

---

## §14 Final Mission Statement

Deliver a download link to a 10-file ZIP that gives the user 4 v0 entity contracts + cross-entity IR shapes + DB candidate schema + lifecycle state machines + SoR matrix v2 + corner cases + transition guide. The ZIP must be saturating enough that a 30-minute user audit can decide whether to (a) fold into PRD-v3/SRD-v3, (b) defer to Phase 2 dispatch, or (c) reject + restart.

Take 75+ minutes. Use 10 passes. Adversarially audit yourself. Then deliver.

Begin Pass 1 now.

<<<CLOUD U3 END>>>
```

---

## Use guide

- 复制 `<<<CLOUD U3 BEGIN>>> ... <<<CLOUD U3 END>>>` 整段
- 粘到 cloud GPT Pro 深度思考窗口 3 (与 U1, U2 并行)
- 等 1.5-2.5h
- 收 download link → 下载到 `/tmp/strategic-upgrade-cloud-out/u3/`

## Acceptance criteria

- 10 个文件全在
- 总字数 ≥ 10000
- 4 个 entity v0 contract 各 ≥1500 字
- DB candidate schema 含 mermaid ER + CREATE TABLE
- 4 个 lifecycle state machine + 1 总图
- ≥8 corner cases
- ≥4 web 2-month 引用
- 无 migration / DB authority / lite v0 promote 偷写

任一不达 → 重 paste 同段 prompt。
