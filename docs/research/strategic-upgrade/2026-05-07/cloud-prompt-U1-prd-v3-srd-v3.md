---
title: Cloud GPT Pro Prompt — U1 PRD-v3 / SRD-v3 Candidate (multi-pass deep authoring)
status: candidate / cloud-prompt / not-authority
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-07
target_writer: Cloud ChatGPT Pro single window (deep thinking mode, ≥2h)
project_root: /Users/wanglei/workspace/ScoutFlow
github_repo: https://github.com/RayWong1990/ScoutFlow (public during the 4h cloud window only)
target_output: ZIP bundle, 7 markdown files, total ~10K Chinese+English words
deliverable_kind: download_link
expected_thinking_time: 120-150 minutes
relates_to:
  - past cloud prompt: plan/archive/2026-05-05-wave5-gpt-pro-prompts/gpt-pro-prompt-prd-v3-srd-v4-wave5-outline-2026-05-05.md
  - past 50-pack: raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05/
---

# Cloud GPT Pro Prompt — U1 PRD-v3 / SRD-v3 Candidate Authoring

> Paste this entire document（含 `<<<CLOUD U1 BEGIN>>>` 到 `<<<CLOUD U1 END>>>` 段）into Cloud ChatGPT Pro deep-thinking window。
> Output deliverable = a single download link (ZIP bundle / shareable file) containing 7 markdown files following the exact schema in §3.
> Expected total deep-thinking duration: 120-150 minutes minimum. Quality strictly outranks latency.

---

## §0 Pre-flight (user 必跑一次)

```bash
cd /Users/wanglei/workspace/ScoutFlow
git fetch origin --prune
git rev-parse origin/main  # 期望: ea509022eb05a552777373394a6fc2a5077f27f6
gh repo edit RayWong1990/ScoutFlow --visibility public --accept-visibility-change-consequences
# (4h 后 flip private)
```

---

```
<<<CLOUD U1 BEGIN>>>

You are Cloud ChatGPT Pro acting as a senior product/system requirements architect for the ScoutFlow project. Your single mission is to author a PRD-v3 candidate plus an SRD-v3 candidate that fold all post-v2 evidence (8 amendments + 4 run receipts + 1 visual lane) into a coherent next-base-document pair, and to package the output as a downloadable ZIP bundle.

This is candidate research authoring only. It is NOT authority promotion, NOT runtime approval, NOT migration approval, NOT vault true-write approval, NOT browser-automation approval, NOT BBDown / yt-dlp / ffmpeg / ASR unlock, NOT frontend implementation approval. The user will audit the ZIP output locally before any promotion decision.

You must take at least 90 minutes of deep thinking BEFORE producing the final output. Quality is more important than latency. If your environment supports long reasoning, spend 120-150 minutes.

## §1 Project Identity

- repo: https://github.com/RayWong1990/ScoutFlow (PUBLIC during your 4h work window; will flip back to private after)
- live status: WAVE_6_CANDIDATE_OPEN / NOT_EXECUTION_APPROVED
- baseline_origin_main: `ea509022eb05a552777373394a6fc2a5077f27f6` (Run-3+4 receipt amendment merged)
- ScoutFlow's role: single-user, local-first, evidence-ledger-anchored content capture system (Bilibili + XHS + YouTube outlook)
- Sibling projects:
  - DiloFlow (channel 看见看不见, downstream consumer of ScoutFlow's compiled material)
  - ContentFlow (legacy ingest-pipeline / topic-engine / data-platform — historical inspiration only)
  - hermes-agent (orchestration sidecar, currently has openai venv installed)
  - AtlasFlow / blowflow / openclaw / ABU-SD-Agent (orthogonal projects)

## §2 Required Inputs

If the repo is reachable (PUBLIC), fetch each file directly. If it returns 404, ask the user to paste the inline content. Do NOT invent repo facts.

### §2.1 Base authority (canonical fact source)

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/current.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/task-index.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/decision-log.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/AGENTS.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/specs/contracts-index.md

### §2.2 PRD-v2 / SRD-v2 base + amendments

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-v2-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-v2-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md

### §2.3 8 amendment trail (post-v2 promote/amend events)

| PR | Description | URL |
|---|---|---|
| #197/#198 | pre-Run-1 readback | https://github.com/RayWong1990/ScoutFlow/pull/197 + /pull/198 |
| #231 | Run-1 amendment ledger + 3 audit reports | https://github.com/RayWong1990/ScoutFlow/pull/231/files |
| #239 | Run-2 receipt traceability amendment (10-FIX bundle) | https://github.com/RayWong1990/ScoutFlow/pull/239/files |
| #240 | Run-3+4 PF-C1 + PF-C2 single-PR closeout (24 dispatch) | https://github.com/RayWong1990/ScoutFlow/pull/240/files |
| Run-1 audits | 3 cloud audit reports | https://github.com/RayWong1990/ScoutFlow/tree/main/docs/research/post-frozen/audits |
| Run-2 amendment ledger | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-AMENDMENT-LEDGER-2026-05-06.md |
| Run-1 amendment ledger | https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-1-AMENDMENT-LEDGER-2026-05-06.md |

### §2.4 4 run receipts (Run-1 / Run-2 / Window-2 / Run-3+4)

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-1-CODEX0-REPORT-2026-05-06.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Run1-final.json
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-2-CODEX0-REPORT-2026-05-06.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Run2-final.json
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-W2-CODEX0-DOCS-REPORT-2026-05-06.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-W2-final.json
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/RUN-3-4-CODEX0-REPORT-2026-05-06.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/runs/CHECKPOINT-Run3-4-final.json

### §2.5 Wave 5 / Dispatch127-176 candidate chain (frozen, evidence-only reference)

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/80-pack-source/02_task_packs/_PACK-DEFAULTS.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/80-pack-source/02_task_packs/_SHARED-STOP-LINES.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-roadmap-candidate-2026-05-05.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-wave-strategy-candidate-2026-05-05.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-dispatch176-scoutflow-raw-bridge-candidate-2026-05-05.md

### §2.6 Phase 2 future / overflow context

- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/post-frozen/overflow-registry-v0.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-021-bbdown-runtime-gate-matrix-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md
- https://github.com/RayWong1990/ScoutFlow/blob/main/docs/research/t-p1a-025-db-ledger-vnext.md

### §2.7 Past cloud prompt (PRD-v3/SRD-v4 outline, 2026-05-05) — schema reference only

- The past cloud prompt that authored an outline candidate but was never promoted: `plan/archive/2026-05-05-wave5-gpt-pro-prompts/gpt-pro-prompt-prd-v3-srd-v4-wave5-outline-2026-05-05.md` — use as schema/methodology reference, not as authoritative content. The current task supersedes that prompt's scope: now we have 4 run receipts as evidence, so the outline can become a real candidate, not just an outline.

### §2.8 Past 50-pack delivery schema reference

- ZIP delivery example: `raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05/` — folder of 50 dispatch.md files + manifest.jsonl + execution-plan.md + CHECKPOINT.json. Your output ZIP for U1 follows the same packaging discipline (see §3 below).

## §3 Required Output Structure — ZIP Bundle Schema (STRICT)

Output **a single download link** to a ZIP file or equivalent shareable bundle named `cloud-output-U1-prd-v3-srd-v3-2026-05-07.zip`, containing exactly **7 markdown files** with the following STRICT schema:

### §3.1 File 1: `PRD-v3-candidate-2026-05-07.md`

- Word target: 2800-3500 Chinese characters with embedded English technical terms
- Frontmatter:
  ```yaml
  ---
  title: ScoutFlow PRD v3 (Candidate)
  status: candidate / prd_v3_candidate / not-authority
  authority: not-authority
  execution_approval: not-approved
  promote_decision_pending: yes
  supersedes: docs/PRD-v2-2026-05-04.md (not yet, candidate only)
  promoted-from: PRD-v2 base + 8 amendment events (PR #197/198/231/239/240) + 4 run receipts + 1 visual lane PF-V parallel
  base_origin_main_sha: ea509022eb05a552777373394a6fc2a5077f27f6
  created_at: 2026-05-07
  ---
  ```
- Required sections (each with claim labels):
  1. 0. 元信息（项目身份 / 阅读顺序 / 文档角色 / candidate 状态强声明）
  2. 1. Mission / 范围 / 非目标（incorporate 4 run 实证）
  3. 2. 当前功能基线（FR）— 折叠 v2 + 8 amendment 后的 effective FR
  4. 3. 数据 / 状态（DR）— SQLite + FS + state words 仍为 base
  5. 4. 红线 + 边界（incorporate Run-2/3+4 amendment 立住的 amendment 模式）
  6. 5. Phase 2 outline upgrade — 把 5 overflow lane 升格成"Phase 2 unlock conditions"（不是已 unlock，是 conditions enumerated）
  7. 6. ScoutFlow → DiloFlow / RAW 接口契约（fold 自 post-dispatch176-scoutflow-raw-bridge-candidate）
  8. 7. PF-V 视觉 lane 接入策略（PF-C4-01 frontend bootstrap input）
  9. 8. v3 Promote Gate Map（v3 何时可 promote = 何种证据 / 何种用户 verdict）
  10. 9. 追溯 / archive 规则
- Claim label distribution target: 50% canonical fact + 25% promoted_addendum-aware inference + 15% candidate carry-forward + 10% tentative candidate

### §3.2 File 2: `SRD-v3-candidate-2026-05-07.md`

- Word target: 2800-3500 字
- Frontmatter:
  ```yaml
  ---
  title: ScoutFlow SRD v3 (Candidate)
  status: candidate / srd_v3_candidate / not-authority
  authority: not-authority
  runtime_approval: not-approved
  migration_approval: not-approved
  supersedes: docs/SRD-v2-2026-05-04.md (not yet, candidate only)
  upstream: PRD-v3-candidate-2026-05-07.md
  base_origin_main_sha: ea509022eb05a552777373394a6fc2a5077f27f6
  created_at: 2026-05-07
  ---
  ```
- Required sections:
  1. 0. 元信息 + 仲裁链
  2. 1. 系统总览 — 当前生效 vs 仍是 outline 的部分（incorporate 4 run 实证：bridge router mounted + write_enabled=False 双分支 + topic-card-lite v0 + RAW handoff staging）
  3. 2. API 当前 effective contract（POST /captures/discover + GET /captures/{id}/vault-preview + 新增 bridge router routes）
  4. 3. Bridge 与 Vault 边界（vault_preview / vault_commit / write_enabled=False 不变）
  5. 4. Phase 2 entity 工程 outline upgrade — `signals / hypotheses / capture_plans / topic_cards` 从 future outline 升级为"Phase 2 candidate IR shape"（依赖 U3 输出，但 v3 内自含 hook）
  6. 5. ASR / runtime / browser automation / migration 边界 + Phase 2 unlock conditions（依赖 U2 输出，v3 内含 anchor）
  7. 6. 多 Agent 协作工程契约（沿用 4 run 实证：Codex0 single writer / 3-window cloud audit / amend_and_proceed pattern）
  8. 7. PF-V handoff 工程接管点（image→HTML5→React TSX 路径）
  9. 8. DR / 单 user / local-first 假设（incorporate 2026 local-first canonical stack: plain text + SQLite FTS + local embeddings + MCP）
  10. 9. 追溯 / archive
- Claim label distribution: 同 §3.1

### §3.3 File 3: `AMENDMENT-FOLD-TABLE-2026-05-07.md`

- Word target: 1000-1500 字
- 表格内容（必含）:
  - 8 amendment 事件（PR #197 起到 PR #240）
  - 每事件: 触发原因 / amendment 内容 / fold 入 v3 哪一节 / claim label
  - 4 run 实证: 每 run 关键事实 → fold 路径
  - 5 overflow lane 状态变化（v2 静态描述 → v3 unlock conditions enumerated）
- 必含 mermaid timeline diagram (5 月 2 日 → 5 月 7 日)
- frontmatter status: candidate / amendment_fold_table / not-authority

### §3.4 File 4: `TRANSITION-GUIDE-V2-TO-V3-2026-05-07.md`

- Word target: 800-1200 字
- 必含:
  - v2 → v3 deprecation 列表（哪些 v2 段被 supersede / 哪些保留 / 哪些 archive）
  - migration steps for downstream consumers (其它 doc / dispatch / spec 怎么 update reference)
  - rollback plan（若 v3 promote 后发现重大问题）
  - promote gate（什么时候能从 candidate → promoted base = 满足 N 个 evidence + user verdict）
- frontmatter status: candidate / transition_guide / not-authority

### §3.5 File 5: `TRACEABILITY-MATRIX-2026-05-07.md`

- Word target: 1500-2000 字
- 表格内容: v3 每节 → source（v2 / amendment / run receipt / 新增 tentative）
- 至少 50 行（PRD-v3 + SRD-v3 总段数 ≥50）
- 每行 4 列: v3 段名 / 来源 / claim label / evidence URL
- frontmatter status: candidate / traceability / not-authority

### §3.6 File 6: `SELF-AUDIT-PRD-V3-2026-05-07.md`

- Word target: 600-900 字
- GPT Pro 自找的 5+ 缺陷 / inconsistency / unverified claim / over-promotion risk
- 每条: 现象 / 严重度 / 修复建议
- 必含: "若用户拒绝某 amendment，v3 哪几节需 rewind" 分析
- frontmatter status: candidate / self_audit / not-authority

### §3.7 File 7: `README-deliverable-index.md`

- Word target: 400-600 字
- 列全 7 文件 + 字数 + claim label 占比 + 多 pass 工作流摘要
- 末尾含 "post-cloud audit checklist"（user 收到 ZIP 后该做的 5 件事）
- frontmatter status: candidate / readme_index / not-authority

---

## §4 Multi-Pass Work Plan (10 Pass, ≥90 min cumulative)

You MUST execute these passes in order BEFORE producing final output:

### Pass 1: Base v2 read (10-15 min)
Read PRD-v2 + SRD-v2 fully. Extract every canonical fact. Build a mental model of the v2 baseline.

### Pass 2: Amendment trail read (15 min)
Read 8 amendment events in chronological order (PR #197 → #240). For each, identify: (a) what was added/changed, (b) what claim label level it had, (c) whether it was promoted or stayed candidate.

### Pass 3: 4 run receipt deep read (20 min)
Read Run-1 / Run-2 / Window-2 / Run-3+4 receipts including DIFF-BUNDLE + CHECKPOINT. Extract: dispatch list / verdict distribution / silent flexibility instances / boundary preserved / partial cascades.

### Pass 4: Overflow + Phase 2 candidate read (10 min)
Read overflow registry + BBDown gate matrix + ASR prestudy + DB vNext + LLM normalization. Identify which Phase 2 entry conditions are now closer / further from being met based on 4 run實证.

### Pass 5: 2-month web evidence integration (10 min)
Integrate the following 2-month web findings into v3 design (cite as evidence in §3 sections):
- 2026-01-28 Bilibili cease-and-desist letter to bilibili-API-collect → vendor diversification mandatory
- yt-dlp metadata-only `skip_download:True` legal in US/EU/most jurisdictions
- Whisper large-v3-turbo / Parakeet v3 / Voxtral 三选 (all run on Apple Silicon, single user PKM viable)
- Local-first 2026 canonical stack: plain text + SQLite FTS + local embeddings + MCP server
- 2026 ontology renaissance year (knowledge graph + entity ontology re-emerged as agent enabler)
- AI agent fleet: GitHub /fleet 80% production = orchestrator-worker pattern
- XHS no official API, requires residential proxy + reverse-engineered libs
Cite each in v3 with [tentative candidate] or [candidate carry-forward] label.

### Pass 6: Sibling project context (5 min)
Integrate DiloFlow (channel 看见看不见, downstream consumer) + ContentFlow (legacy ingest-pipeline / topic-engine) + hermes-agent (orchestration sidecar w/ openai venv). Define the SoR boundary for ScoutFlow→DiloFlow handoff (extends past post-dispatch176-scoutflow-raw-bridge-candidate matrix).

### Pass 7: PRD-v3 outline draft (15 min)
Draft PRD-v3 section map. Each section: name + 1 sentence purpose + claim labels expected + evidence sources. Use the §3.1 required sections list.

### Pass 8: SRD-v3 outline draft (15 min)
Draft SRD-v3 section map. Same discipline as Pass 7. Use §3.2 required sections list.

### Pass 9: Full content authoring (30-45 min)
Write all 7 files following the schema. Maintain claim label discipline. Write Chinese with embedded English technical terms (no double translation).

### Pass 10: Adversarial self-audit (10-15 min)
Find ≥5 issues in your own output. Categories to check:
- claim label drift (claim something is canonical when it's tentative)
- over-promotion (treating amendment as base authority)
- silent flexibility (changing scope without declaration)
- boundary leak (implying runtime / migration / true-write enabled)
- PRD/SRD inconsistency (PRD says X, SRD says Y conflicting)
- evidence gap (claim N has no source URL)
Document all issues in SELF-AUDIT-PRD-V3-2026-05-07.md with severity + fix recommendation. If any issue is CRITICAL, fix before producing final output.

---

## §5 Self-Audit Checklist (15 items, embed in SELF-AUDIT file)

For each item, mark `clear` / `concern` / `reject`:

1. PRD-v3 frontmatter status = `candidate / not-authority` (not `promoted` / `base`)
2. SRD-v3 frontmatter same
3. No section asserts Phase 2 is unlocked
4. No section asserts BBDown / yt-dlp / ffmpeg / ASR / browser automation / migration is enabled
5. write_enabled=False invariant maintained throughout SRD
6. Authority files (current.md / task-index.md / decision-log.md / AGENTS.md) NOT redrafted
7. Each section has ≥1 source URL or evidence anchor
8. Claim label coverage ≥ 80% of substantive paragraphs
9. Promote gate map (PRD-v3 §8) has measurable conditions, not vague "when ready"
10. Transition guide includes rollback plan
11. Traceability matrix has ≥50 rows
12. AMENDMENT-FOLD-TABLE covers all 8 events (no skip)
13. v3 design references at least 4 of the 7 web 2-month findings (Bilibili cease-and-desist, Whisper/Parakeet, local-first 2026, ontology renaissance, agent fleet, XHS scraper, yt-dlp legal)
14. SoR matrix update includes DiloFlow as downstream
15. README-deliverable-index lists every file with word count and claim label ratio

---

## §6 Hard Boundaries (违反任一即整 ZIP reject)

1. 不写 final authority 文本（不替代 docs/current.md / task-index.md / decision-log.md / AGENTS.md）
2. 不声明 PRD-v3 / SRD-v3 已 promote
3. 不 enable BBDown live / yt-dlp / ffmpeg / ASR / browser automation / migration / true vault write
4. 不修 production code paths（services/ apps/ workers/ packages/ data/）
5. 不 break write_enabled=False invariant
6. 不 silent-upgrade candidate to base
7. 不 fabricate facts not in source documents
8. 措辞用 T-PASS / V-PASS / partial / FAIL_ENV / REJECT_AS_X / clear / concern / reject — 禁裸 PASS / DONE / OK
9. 不 skip claim label
10. 不 deliver < 7 files / < 9000 cumulative words

---

## §7 Quality Criteria (per-file rubric)

Each output file judged on:

| 维度 | 权重 | 评分细节 |
|---|---:|---|
| Claim label discipline | 25% | 80%+ paragraphs labeled / no drift |
| Evidence linkage | 20% | every section has ≥1 source URL |
| Boundary preservation | 20% | no Phase 2 / runtime / migration leak |
| Coherence | 15% | PRD-v3 ↔ SRD-v3 internally consistent |
| Web evidence integration | 10% | ≥4 of 7 web 2-month findings used |
| Promote gate clarity | 10% | conditions measurable, not vague |

Target overall: ≥85% on every file. Below 70% on any file = full ZIP reject.

---

## §8 Source References (paste-time evidence layer)

When the user audits your ZIP, they will check sources. Include source URLs explicitly in your file content, not just at end. Don't hide sources in footnotes only.

### §8.1 Web 2-month findings (cite when integrating)

- Bilibili cease-and-desist 2026-01-28: SocialSisterYi/bilibili-API-collect maintainer received warning letter. Implication: third-party API doc projects under legal pressure; vendor diversification mandatory.
- yt-dlp 2026 legal status: tool itself legal in US/EU; metadata-only via `skip_download:True` is the safest path. CVE-2026-26331 patched in core.
- Whisper / Parakeet / Voxtral 2026 benchmark: Whisper large-v3-turbo (809M params, 6x faster than large-v3, MIT) / Parakeet v3 (NVIDIA, 600M, 80ms on Apple Silicon, FluidAudio Swift SDK) / Voxtral Mini 4B Realtime (Mistral, 2026-02 release, Apache-2.0).
- Local-first 2026: canonical stack = plain text + SQLite FTS + local embeddings + MCP server (SwarmVault as RAG knowledge vault example). CRDT-based sync for multi-device.
- Ontology renaissance 2026: Gartner D&A Summit 2026 positioned semantic layers + knowledge graphs as foundational infrastructure for agentic AI. Ontology defines meaning and rules; knowledge graph contains instance data.
- AI agent fleet: GitHub /fleet (Copilot CLI) + 80% production multi-agent = orchestrator-worker pattern. Sub-agents stateless, isolated context windows, shared filesystem. Pass complete context to each sub-agent. Start centralized; decentralize only when bottlenecks found.
- XHS 2026 scraper: no official API for international devs. Apify / Bright Data / MediaCrawler with residential proxy required. RedShop e-commerce data new frontier.

### §8.2 Local sibling project cross-reference

- DiloFlow at `/Users/wanglei/workspace/DiloFlow` — channel 看见看不见, EP01-script-v1.md exists, AGENTS.md + CLAUDE.md present, control/ + episodes/ + channel/ subdirs. ScoutFlow → DiloFlow handoff: ScoutFlow produces evidence + topic_card; DiloFlow consumes for episode script.
- ContentFlow at `/Users/wanglei/workspace/contentflow` — has ingest-pipeline + topic-engine + creator-research subdirs. Legacy reference for topic engine concepts. Do not directly couple — historical only.
- hermes-agent at `/Users/wanglei/workspace/hermes-agent` — orchestration sidecar with openai Python lib already in venv. Could be Phase 2 LLM normalization runtime host (per t-p1a-023 design).

### §8.3 Past cloud prompt schema reference

The past PRD-v3/SRD-v4 outline cloud prompt (2026-05-05) used 9-section section-map plus mermaid state diagram. Your task supersedes that scope: now you author the **content**, not just **outline**. Re-use the schema discipline (claim labels, multi-pass, hard boundaries) but produce real candidate prose, not merely section names.

---

## §9 Format Guard (final check before download link)

Before finalizing ZIP:

1. Run a frontmatter scanner: every .md file has `status: candidate / [type] / not-authority` first line in frontmatter.
2. Run a claim label scanner: every substantive paragraph has at least one of `[canonical fact] / [promoted_addendum-aware inference] / [candidate carry-forward] / [tentative candidate]` marker.
3. Run a hard-redline scanner: no occurrence of "BBDown is enabled" / "true write is unlocked" / "migration is approved" / "Phase 2 is live" outside `[tentative candidate]` future-conditional context.
4. Run a word-count scanner: each file meets §3 word target.
5. Run a section completeness scanner: PRD-v3 / SRD-v3 each have all 10 required sections from §3.1 / §3.2.

If any check fails, fix and re-run. Do not deliver a non-conforming ZIP.

---

## §10 Stdout Output Contract

Once ZIP is ready, output the following structured response in your chat:

```
CLOUD U1 PRD-V3-SRD-V3 COMPLETE
deliverable_url: <download link or shareable file URL>
zip_filename: cloud-output-U1-prd-v3-srd-v3-2026-05-07.zip
files_count: 7
total_words: <number>
total_thinking_minutes: <number, ≥90>
multi_pass_completed: 10/10
self_audit_findings: <count of issues found by Pass 10>
critical_issues_fixed_inline: <count>
critical_issues_remaining: <count, should be 0>
claim_label_distribution:
  canonical_fact: <%>
  promoted_addendum_aware: <%>
  candidate_carry_forward: <%>
  tentative_candidate: <%>
boundary_preservation_check: clear / concern / reject
ready_for_user_audit: yes / no
```

If `ready_for_user_audit: no`, you MUST list the unresolved blocking reasons and offer to fix.

---

## §11 If Repo is Private (Inline Fallback Mode)

If your fetch attempts return 404 (repo private during your run), do NOT proceed. Instead, respond to user with:

```
GITHUB FETCH FAILED — REPO PRIVATE
Required: please flip repo to public for the duration of this run, or paste the inline content of the following 30 files:
[list]
After paste, I will resume.
```

Do NOT attempt to author from memory or general knowledge. The deliverable must be grounded in the actual repo facts.

---

## §12 Final Mission Statement

Your mission, restated: deliver a single download link to a 7-file ZIP that lets the user perform a 30-minute audit and decide whether PRD-v3 + SRD-v3 candidate is ready for promotion. Your output, if accepted, replaces PRD-v2 + SRD-v2 as the next base after one human review cycle. The stakes are high — a bad ZIP wastes 2-2.5h of cloud GPT Pro time and forces a re-run.

Take 90+ minutes. Use 10 passes. Adversarially audit yourself. Then deliver.

Begin Pass 1 now. Do not skip to authoring.

<<<CLOUD U1 END>>>
```

---

## Use guide

```bash
# 1. user 跑 §0 pre-flight
# 2. 复制 <<<CLOUD U1 BEGIN>>> ... <<<CLOUD U1 END>>> 整段
# 3. 粘到 cloud GPT Pro 深度思考窗口 1
# 4. 等 2-2.5h
# 5. 收 download link → 下载到本地 /tmp/strategic-upgrade-cloud-out/u1/
# 6. 解压 + audit (用 README-deliverable-index.md 作 entry)
```

## Acceptance criteria (user 后续审 ZIP 时用)

- 7 个文件全在
- 总字数 ≥ 9000
- 每文件 frontmatter status 含 `candidate / not-authority`
- 每段内容含 claim label
- 无 Phase 2 unlock / runtime / migration / true-write 偷写
- self-audit 自找 ≥5 issues + 标 severity
- traceability matrix ≥ 50 rows
- web 2-month 至少 4 项被 cite

任一不达 → 重 paste 整段 prompt 给同窗或新窗。
