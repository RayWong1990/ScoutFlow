---
title: Wave 5 Scope and Template Extraction
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
created_at: 2026-05-05
scope: STEP2 item 2A-9 bounded structural extraction for Dispatch127-176 backbone preparation
related_files:
  - docs/PRD-v2-2026-05-04.md
  - docs/SRD-v2-2026-05-04.md
  - docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md
  - docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
  - docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md
  - /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md
---

# Wave 5 Scope and Template Extraction

> State: candidate / not authority / not execution approval / not runtime approval / not migration approval.
> This file handles STEP2 item `2A-9` only.
> It is bounded structural extraction, not slot-finalization, not runtime approval, and not Phase 2A migration approval.

## 0. Purpose and Method

This document produces four bounded outputs:

1. Wave 5 PRD/SRD section index candidates for later `BACKBONE-TAXONOMY.md`.
2. batch1 worklist structural template extraction from the `Dispatch 76-125` b2v4 pack.
3. implemented-vs-unimplemented continuation mapping for `Dispatch127-176`.
4. the suggested candidate output path for this extraction artifact.

Extraction rules used here:

- `canonical` means promoted base authority in `docs/PRD-v2-2026-05-04.md` or `docs/SRD-v2-2026-05-04.md`.
- `promoted_addendum` means the file is not the base authority doc, but current repo truth says it is promoted for B2 planning/contract baseline.
- `candidate_context` means the file is useful context but is not promoted as baseline and must not be treated as default enforced contract.
- `inference` is allowed only when no direct section anchor exists; any such case must later carry `inference_from` and `risk_flag: tentative`.

Current repo truth that constrains this extraction:

- `Wave 4` is open and current next gate is `T-P1A-073 / slot-label PR #98`; therefore `Dispatch 98+` is not free theme space and should be treated as in-flight or reserved, not regenerated. See [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:3) and [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:29).
- `PRD-v2.1 + SRD-v3 H5/Bridge` are promoted addenda for B2 planning/contract baseline, but runtime/frontend/migration remain gated. See [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:6), [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:14), [contracts-index.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/contracts-index.md:53), and [contracts-index.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/contracts-index.md:54).
- `DB vNext` remains candidate-only and must not become the default backbone for `Dispatch127-176`. See [contracts-index.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/contracts-index.md:53).

## 1. Wave 5 PRD/SRD Section Index Candidates

### 1.1 Primary anchors for `Dispatch127-176`

These are the strongest candidates for later `contract_source` fields.

| Tier | Anchor | Why it belongs in the Wave 5 candidate pool | Carry-forward rule |
|---|---|---|---|
| `canonical` | [PRD v2 §4.3 Phase 2 entity outline](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md:128) | Defines the future product entities `signals / hypotheses / capture_plans / topic_cards`; these are not yet implemented in `Dispatch 76-125` and are the cleanest base for post-Wave-4 product-structure work. | Candidate docs/spec only; do not treat as runtime approval. |
| `canonical` | [PRD v2 §5.2 当前 capture 主链路](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md:149) | Preserves the full lifecycle chain and explicitly says Phase 1A currently lands only on `metadata_fetched` + receipt + trust trace. | Later Wave 5 candidates may project or prepare later states, but must not imply they are already unlocked. |
| `canonical` | [PRD v2 §7.2 Thin API 边界](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md:243) | Defines what API may and may not do; this is the base anchor for any continuation touching Bridge/H5/vault projection. | Use as a negative boundary, not as direct feature detail. |
| `canonical` | [PRD v2 §9.1-§9.2 Phase 路线](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md:286) | Declares `Phase 2` as `Signal Workbench / Capture Plan / Topic Card` and separately marks higher phases as not auto-approved. | Use to separate Wave 5 candidate docs/spec work from runtime unlock claims. |
| `canonical` | [SRD v2 §2.7 Phase 2 entity outline](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:132) | Engineering counterpart for the same future entities; useful when a future dispatch is docs/spec and not H5/Bridge/Vault execution work. | Candidate-only bridge into future FR/DR, not code approval. |
| `canonical` | [SRD v2 §3.2-§3.4 数据与状态约束](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:148) | Locks state semantics, `audio_transcript` blocked wording, and local-only path boundaries. | Use as negative guardrail for all Wave 5 candidate work. |
| `canonical` | [SRD v2 §4.1-§4.3 接口边界](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:171) | Defines API/Worker/Console boundaries and keeps frontend non-authority. | Required whenever a later dispatch touches H5/Bridge or prompt/handoff tooling. |
| `canonical` | [SRD v2 §6.3 并行执行约束](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:237) | Establishes enforced baseline `product_lane_max=3`, `authority_writer_max=1`, same-file writer max 1. | Any later surge model must stay candidate-only unless separately overridden. |
| `canonical` | [SRD v2 §7.3 明确不等于批准](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:260) | Clean reminder that frontend mode, BBDown runtime, ffmpeg, ASR, `audio_transcript`, and Phase 2-4 runtime are still not approved. | Use as stop-line language in later worklist/backbone entries. |
| `promoted_addendum` | [PRD v2.1 §X.1 Strong Visual Capture H5](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md:34) | Supplies the four-panel product intent and state-machine framing that batch1 `Dispatch 98-104` began to implement. | Valid backbone for continuation/hardening; not standalone frontend approval. |
| `promoted_addendum` | [PRD v2.1 §X.2 Existing PARA / Claudian Vault Integration](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md:77) | Gives product-level vault boundary and `00-Inbox` discipline without making runtime promises. | Good anchor for post-125 hardening and write-boundary docs; not commit approval. |
| `promoted_addendum` | [PRD v2.1 §X.4 PR Factory Product Operating Mode](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md:117) | Introduces candidate surge mode, including possible `product lane max = 5`. | Use as candidate-only support for later commander/pool docs, never as current enforced baseline. |
| `promoted_addendum` | [PRD v2.1 §X.6 Promotion basis and future evidence gates](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md:164) | Defines future walking skeleton / visual / runtime gates. | Strong source for later `manual_gates_required` or `risk_flag: tentative`. |
| `promoted_addendum` | [SRD v3 H5/Bridge §17.1 H5 Capture Station](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md:67) | Engineering shape for the four-panel H5 surface and panel responsibilities. | Use for continuation of `Dispatch 98-104` and visual hardening after mid-checkpoint. |
| `promoted_addendum` | [SRD v3 H5/Bridge §17.2 Bridge / Thin API Route Group](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md:136) | Defines candidate route list, preview/commit semantics, and `BridgeErrorCode` split. | Use for post-`Dispatch 110` hardening; do not imply runtime unlock. |
| `promoted_addendum` | [SRD v3 H5/Bridge §17.3 VaultWriter Contract](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md:218) | Defines path policy, frontmatter contract, four-section body, and preview vs commit rules. | Use for post-`Dispatch 115` contract verification or preview/hardening only. |
| `promoted_addendum` | [SRD v3 H5/Bridge §17.4 PR Factory Protocol Dependency](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md:288) | Connects H5/Bridge/Vault continuation to future PR factory surge rules while keeping current baseline unchanged. | Good source for later pool/lock/handoff docs. |
| `promoted_addendum` | [SRD v3 H5/Bridge §17.6 Promotion basis and future evidence gates](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md:336) | Explicitly states no walking skeleton, no runtime, no migration approval yet. | Use as stop-line copy for any optimistic continuation draft. |

### 1.2 Context-only anchors

These are useful, but they should not become the default first-wave backbone for `Dispatch127-176`.

| Tier | Anchor | Why it is context-only | Safe use |
|---|---|---|---|
| `promoted_addendum` | [PRD v2.1 §X.3 Fixed Product Shoulders](/Users/wanglei/workspace/ScoutFlow/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md:96) | Useful for naming directions such as `BBDown`, `Whisper family`, `Obsidian PARA vault`, and `OpenDesign`, but not detailed enough to drive a 50-slot backbone alone. | Use as supporting product-direction context. |
| `candidate_context` | [DB vNext §1.4-§1.5 identity/FK enforcement](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md:180) | Strong migration-prep and invariant material, but contracts index still marks DB vNext candidate-only and not migration approval. | Reserve for overflow or separate docs/spec lanes; do not anchor default early slots. |
| `candidate_context` | [DB vNext §4 Candidate DDL](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md:484) | Too close to Phase 2A migration target shape for a default Wave 5 continuation pack. | Use only when a slot is explicitly docs-only DB-prep or overflow candidate. |
| `candidate_context` | [DB vNext §5 Deferred To Phase 2A First Implementation Task](/Users/wanglei/workspace/ScoutFlow/docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md:868) | Explicitly says Phase 2A first implementation task, not current enforced work. | Keep as deferred reference, not primary backbone. |

### 1.3 Exclude from default backbone

The following are not good default anchors for `Dispatch127-176`:

- `BBDown live runtime`: batch1 worklist explicitly says it remains blocked until Wave 5 candidate, but current authority still keeps live runtime gated. See [worklist §53 Wave 5 candidate](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4434) and [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:20).
- `audio_transcript`: still blocked until later phase / Wave 6. See [PRD v2 §4.2](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md:121), [SRD v2 §2.1](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md:65), and [worklist §53 Wave 5 candidate](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4434).
- `migrations/**`: still forbidden and separately gated. See [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:17) and [worklist §53 Wave 5 candidate](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4434).

## 2. batch1 Worklist Structural Template Extraction

### 2.1 Verified structure in the `Dispatch 76-125` worklist

The batch1 worklist is not just a title list. It already contains a reusable multi-layer structure:

| Section | Evidence | Reuse verdict | Notes |
|---|---|---|---|
| file frontmatter | [worklist lines 1-17](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:1) | `reuse_with_adapt` | Keep metadata concept, but remove legacy `PRxx` naming from cloud-facing packaging. |
| `§0` overview | [worklist §0](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:24) | `reuse_exact_shape` | Includes 50-slot quick lookup, lane occupancy, file conflict matrix, and dependency graph. |
| per-dispatch packet `§1-§50` | [worklist Dispatch 98 example](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:1953) and [worklist Dispatch 111 example](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:3090) | `reuse_exact_shape` | Heading + YAML packet + execution notes/handoff is the most reusable unit. |
| `§51` file-domain conflict matrix | [worklist §51](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4395) | `reuse_exact_shape` | Keep as a required operational section in the next pack. |
| `§52` parallel scheduling advice | [worklist §52](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4406) | `reuse_with_adapt` | Keep concept, but adapt to V3 staged pool and `product_lane_max=5 run-only override`. |
| `§53` wave entry/exit | [worklist §53](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4410) | `reuse_exact_shape` | Strong template for gate assumptions and blocked items. |
| `§54` relay header | [worklist §54](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4440) | `reuse_with_adapt` | Keep `backbone_source` and forward-anchor idea, but move live head / PR / hash facts to commander-injected layer. |
| `§55` one-line summary and appendices | [worklist §55 + appendices](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4444) | `reuse_exact_shape` | Useful closeout block for future packs. |

### 2.2 Reusable per-dispatch schema from batch1

The per-dispatch packet already has a stable field family:

- `task_id`
- `title`
- `type`
- `lane`
- `wave`
- `phase`
- `sequence`
- `目标`
- `allowed_paths`
- `forbidden_paths`
- `输入素材`
- `输出物`
- `验收标准`
- `validation`
- `依赖前置`
- `预期_diff`
- `预期时长`
- `PR标题模板`
- `Execution notes`
- `Backbone source`
- `Specific errata`
- `Handoff next`
- `Boundary`

This is the correct starting skeleton for `Dispatch127-176`, but it should not be copied unchanged.

### 2.3 Required adaptations for `Dispatch127-176`

| Batch1 pattern | Keep | Adaptation needed for 127-176 |
|---|---|---|
| `Dispatch N — T-P1A-XXX` heading | yes | Keep exact `Dispatch` naming; do not reintroduce `PRxx` as canonical pack identity. |
| YAML first, prose notes second | yes | Still the cleanest layout for both human audit and machine extraction. |
| `wave: '4'` | no | Replace or extend with `wave_hint` semantics from V3, such as `4-final`, `5-frozen`, `5-tentative`, `6-overflow-reference`. |
| `sequence` field | yes | Continue using prior dispatch + required artifact existence, but make it slot-based rather than live-PR-based. |
| `Backbone source` | yes | Keep mandatory, but point to the new batch2 extraction / new worklist amendment rather than doc3 frozen sections. |
| `预期_diff` | partial | Keep as optional planning hint only; actual diff stat belongs to commander/runtime log. |
| `current_main_head_at_drafting_time` idea from §54 | concept only | Move live baseline, branch, PR number, and hash to commander-injected fields, not human-authored backbone prose. |
| `Specific errata` | yes | Keep because batch1 shows it is the easiest place to pin anti-drift rules. |
| `validation` command list | yes | Preserve command-based verification discipline. |
| `Handoff next` | yes | Keep slot-based handoff chain for 127-176 and possible `overflow_candidate` path. |

### 2.4 Structural draft that should carry forward

For the next pack, the reusable skeleton is:

1. frontmatter for the whole worklist file
2. `§0` global overview with 50-slot quick lookup
3. conflict/domain matrix
4. dependency graph
5. one packet per dispatch
6. operational conflict matrix
7. scheduling guidance
8. wave entry/exit and blocked-state table
9. relay header rules
10. appendices

Batch1 already proves that this shape is deep enough for a 50-slot pack and still grep-friendly. It should be reused as a structural template, not rewritten from scratch.

## 3. Implemented-vs-Unimplemented Continuation Mapping for `Dispatch127-176`

### 3.1 What is already covered by the existing `Dispatch 76-125` pack

| Domain | Evidence | Status for 127-176 planning |
|---|---|---|
| `Dispatch 76-90` Wave 3B probes / clone mirrors / prototype references / policy notes | [worklist §0.1 lines 30-44](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:30) and [worklist §55](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4446) | Treat as closed background. Do not regenerate these themes in 127-176. |
| `Dispatch 91-97` Bridge/Vault SPEC v2, H5 design tokens, H5 mock, 5 Gate audit, Wave 3B closeout, Wave 4 entry | [worklist lines 45-51](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:45) and [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:6) | Treat as landed preconditions, not open design space. |
| `Dispatch 98-104` H5 app scaffold + four-panel shell + URL/metadata/scope/trust-trace panels + API client boundary | [worklist lines 52-58](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:52) and [current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:29) | Treat as in-flight or reserved in the existing pack. Do not duplicate titles or file domains in 127-176. |
| `Dispatch 105-110` Bridge route group scaffold / health / config / preview / dry-run / OpenAPI hardening | [worklist lines 59-64](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:59) | Treat as reserved continuation inside the current pack; 127-176 should assume these are the bridge-first pass, not recreate them. |
| `Dispatch 111-120` Vault writer scaffold / path policy / frontmatter renderer / preview renderer / dry-run ledger / placeholder walking skeleton / H5-Bridge integration / fixture E2E | [worklist lines 65-74](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:65) | Treat as existing pack reservation; 127-176 may only continue after these themes, not overlap them. |
| `Dispatch 121-125` 5 Gate CI harness / frontend lint / Playwright smoke / visual reporting / Wave 4 mid checkpoint | [worklist lines 75-80](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:75) and [worklist lines 4308-4389](/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md:4308) | Treat as the handoff base for `Dispatch127-176`. `Dispatch125` is explicitly a mid-checkpoint, not a closeout. |

### 3.2 What remains unimplemented and should drive `Dispatch127-176`

| Continuation area | Why it is still open | Recommended source tier |
|---|---|---|
| post-`Dispatch125` Wave 4 continuation and closeout work | batch1 stops at `Wave 4 mid checkpoint`, not final Wave 4 closeout; handoff explicitly points to `Dispatch127 continuation` after consumed `Dispatch126` slot | `worklist §50` + `current authority` + `promoted addenda` |
| H5/Bridge/Vault hardening after first-pass implementation | source amendments define target shape and future evidence gates, but current authority still says no walking skeleton or runtime approval | `promoted_addendum` |
| visual-touchpoint and localhost review roster hardening | batch1 has 5 Gate audit + CI smoke/report, but not the full later cloud-pack/operator-facing review packaging | `promoted_addendum` + `candidate_context` |
| candidate product-structure docs/spec for `signals / hypotheses / capture_plans / topic_cards` | base PRD/SRD keep these as outline only; batch1 does not consume them | `canonical` |
| PR factory / surge / pool / handoff packaging | PRD v2.1 and SRD v3 H5/Bridge both mention candidate surge/protocol dependency, but batch1 does not convert that into a 127-176 backbone yet | `promoted_addendum` + `candidate_context` |

### 3.3 What should remain blocked or overflow-only

| Area | Why it should not become default Wave 5 backbone |
|---|---|
| `BBDown live runtime` | batch1 marks it blocked until Wave 5 candidate, but current authority still forbids live runtime approval; it needs explicit later dispatches, not silent inclusion. |
| `audio_transcript` | base PRD/SRD still keep it blocked and batch1 pushes it to Wave 6. |
| `migrations/**` | current authority still treats migrations as hard redline requiring separate dispatch + explicit authorization. |
| `DB vNext` as first-wave default | contracts index still marks it candidate-only and not migration approval; use only as overflow or explicitly docs-only prep lane. |

### 3.4 Safe continuation rules for `Dispatch127-176`

The safest continuation interpretation is:

1. `Dispatch127-176` should start from the `Dispatch125` handoff and not reopen `Dispatch76-125` topic selection.
2. The default backbone should be `PRD v2 base + SRD v2 base + PRD v2.1 promoted addendum + SRD v3 H5/Bridge promoted addendum`.
3. `DB vNext` should be attached only when a slot is explicitly marked docs/spec/candidate-context or overflow.
4. Any slot that implies `BBDown live`, `audio_transcript`, `vault true commit`, or `migrations/**` must be marked `risk_flag: tentative` or be deferred out of the default 50-slot body.
5. Any slot overlapping file domains already reserved in `Dispatch98-125` should be treated as duplicate until the `Dispatch125` readback proves that a post-mid-checkpoint continuation is needed.

## 4. Suggested Output Path

The suggested candidate output path is:

`docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md`

This file is already using that path.

## 5. Later `BACKBONE-TAXONOMY.md` Construction Rules

When this extraction is later converted into `BACKBONE-TAXONOMY.md`, use these rules:

- every backbone row must cite `contract_source`
- `contract_source` must prefer:
  1. `canonical`
  2. `promoted_addendum`
  3. `batch1 worklist §M or §53/§54 structural references`
  4. `inference`
- if `inference` is used:
  - add `inference_from`
  - add `risk_flag: tentative`
- if a topic does not fit into the first 50 slots cleanly, record it as `overflow_candidate` rather than forcing it into `Dispatch127-176`

## 6. Grep Verification Appendix

The following command set is sufficient to re-check the main anchors used here:

```bash
rg -n "^### 4\\.3 Phase 2 entity outline|^### 5\\.2 当前 capture 主链路|^### 7\\.2 Thin API 边界|^### 9\\.1 当前 Phase 切分" docs/PRD-v2-2026-05-04.md
rg -n "^### 2\\.7 Phase 2 entity outline|^### 3\\.2 当前必须保持的状态语义|^### 4\\.1 API 层职责|^### 4\\.3 Console ↔ API 边界|^### 6\\.3 并行执行约束|^### 7\\.3 明确不等于批准的内容" docs/SRD-v2-2026-05-04.md
rg -n "^## §X\\.1|^## §X\\.2|^## §X\\.3|^## §X\\.4|^## §X\\.6|product lane max = 5|future walking skeleton" docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md
rg -n "^### §17\\.1|^### §17\\.2|^### §17\\.3|^### §17\\.4|^### §17\\.6|vault-preview|vault-commit|BridgeErrorCode" docs/SRD-amendments/h5-bridge-para-vault-srd-v3-candidate-2026-05-04.md
rg -n "^### 1\\.4|^### 1\\.5|^## 4\\. Candidate DDL|^## 5\\. Deferred To Phase 2A First Implementation Task" docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
rg -n "^## 0\\.|^### 0\\.|^## 51\\.|^## 52\\.|^## 53\\.|^## 54\\.|^## 55\\.|Handoff next: Dispatch 127|Wave 5 candidate" /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-PR76-PR125-dispatch-pack-2026-05-05-b2v4/scoutflow-doc3-amend-pr76-pr125-worklist-2026-05-05.md
```

## 7. Extraction Verdict

`verdict=ready_for_backbone_drafting`

Meaning:

- the PRD/SRD anchor pool is explicit enough to draft `BACKBONE-TAXONOMY.md`
- the batch1 structural template is explicit enough to reuse
- the continuation boundary between `Dispatch76-125` and `Dispatch127-176` is explicit enough to avoid duplicate theme generation
- this does not imply slot titles are finalized, runtime is approved, or Wave 5 scope is fully promoted
