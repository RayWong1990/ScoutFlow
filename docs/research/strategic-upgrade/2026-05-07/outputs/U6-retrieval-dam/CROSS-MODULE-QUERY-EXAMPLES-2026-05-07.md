<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# CROSS-MODULE QUERY EXAMPLES — 2026-05-07

> Claim label: candidate ≥95% for query shape and integration logic; examples are realistic against the provided audit pack but not live-run against a production U6 index.  
> Scope: ≥15 query examples across PR retrieval, visual similarity, time dimension, U4 visual_asset join, and U5 replay lineage.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Query Contract

Every query result should include:

```json
{
  "result_id": "chunk-or-asset-id",
  "module": "hybrid_search | visual_dam | combined",
  "title": "...",
  "file_path": "...",
  "line_range": [10, 30],
  "authority_label": "authority | promoted_addendum | candidate | not_authority | derived",
  "score": 0.87,
  "score_breakdown": {},
  "warnings": []
}
```

For visual results, line range is replaced by thumbnail/original metadata. For combined results, the service should return two lists: `text_evidence` and `visual_evidence`, plus a joined narrative only if the caller asks.

## 2. Text Retrieval Examples

### Q1 — Supersession decision

**User query:** `Codex 在 May 4 关于 supersession 的决定`  
**Target:** task-index/current/dispatch docs around PR #93, T-P1A-103, supersede language.  
**Hybrid behavior:** lexical boost for `May 4`, `supersession`, `PR #93`, `T-P1A-103`; dense recall for Chinese paraphrase.

Pseudo-query:

```sql
SELECT * FROM hybrid_query(
  query => 'Codex 在 May 4 关于 supersession 的决定',
  kind_filter => ARRAY['decision_log','current','dispatch_transcript','contract'],
  date_hint => '2026-05-04'
);
```

Expected answer shape: cite the current authority statement that `PR #93` was superseded by `T-P1A-103` and must not be merged as-is, then show supporting task-index rows.

### Q2 — Why audio_transcript remains blocked

**User query:** `为什么 audio_transcript runtime 仍 blocked？`  
**Target:** PRD/SRD v2 and current.  
**Ranking rule:** authority docs outrank candidate reports.  
**Expected:** PRD/SRD boundary plus current prohibition; no dispatch candidate should override it.

### Q3 — Receipt/artifact ledger baseline

**User query:** `artifact_assets evidence_id 和 evidence_ledger 的关系`  
**Target:** DB vNext candidate section and contracts-index.  
**Expected:** show that `artifact_assets` is current authority naming, but `evidence_ledger` is DB vNext candidate, not migration approval.

### Q4 — Bridge true write gate

**User query:** `VaultWriter 现在可以 true write 吗？`  
**Target:** `vault/commit.py`, current, SRD.  
**Expected:** no; commit dry-run has `write_enabled=false`, true write remains unapproved.

### Q5 — H5 frontend approval

**User query:** `H5 frontend implementation 是否已经批准？`  
**Target:** current, external visual spec, contracts-index.  
**Expected:** design candidates/promoted addenda exist, but no frontend implementation/runtime approval.

### Q6 — Source code route boundary

**User query:** `healthz 是否检查 database？`  
**Target:** `services/api/scoutflow_api/main.py`.  
**Expected:** healthz is liveness only; does not check database or storage.

### Q7 — Product daily loop risk

**User query:** `哪个报告说 search/index 是 daily loop 风险？`  
**Target:** product mechanism premortem external report.  
**Expected:** external report labels old capture reuse time and search/index as product friction; label result as external candidate/not authority.

### Q8 — Dispatch visual reporting

**User query:** `Dispatch156 Wave5 visual reporting 讲了什么？`  
**Target:** `Dispatch156-T-P1A-135-wave5-visual-reporting-candidate.md`.  
**Expected:** show dispatch title, task ID, candidate status, visual reporting scope, no runtime overreach.

### Q9 — Five-gate CI vs human visual verdict

**User query:** `5 Gate CI 通过是否等于 human visual verdict？`  
**Target:** current/external report/visual dispatches.  
**Expected:** no; static readiness and CI are not human visual proof.

### Q10 — PlatformResult split

**User query:** `executable_not_found 是 PlatformResult 吗？`  
**Target:** PRD/SRD v2.  
**Expected:** no; it is ToolPreflightResult, not platform boundary result.

## 3. Visual-DAM Examples

### Q11 — Recent GPT-Image-2 similar assets

**User query:** `过去 30 天哪些 GPT-Image-2 输出与 mockup XX 视觉相似度 ≥85%？`  
**Module:** combined U4 + visual-DAM.  
**Pseudo-SQL:**

```sql
WITH target AS (
  SELECT phash_64, dhash_64 FROM visual_dam_index WHERE asset_id = :mockup_asset_id
), candidates AS (
  SELECT va.asset_id, va.prompt_id, va.generation_model, va.created_at,
         dam.thumbnail_path, dam.phash_64, dam.dhash_64
  FROM visual_asset va
  JOIN visual_dam_index dam ON dam.asset_id = va.asset_id
  WHERE va.created_at >= datetime('now', '-30 days')
    AND va.generation_model LIKE '%GPT-Image-2%'
)
SELECT * FROM candidates;
```

Python then computes hamming distance and maps pHash ≤8 to high visual similarity. UI should phrase it as `hash_similarity_bucket=strong_sibling`, not a calibrated CV score.

### Q12 — Exact duplicate generated twice

**User query:** `这张图是否重复生成过？`  
**Module:** visual-DAM.  
**Logic:** `original_sha256` exact match first; if none, pHash ≤4.  
**Expected:** show exact byte duplicates separately from perceptual duplicates.

### Q13 — Same prompt cluster, visually divergent

**User query:** `prompt_cluster=hero-card 的图里哪些不像其他？`  
**Module:** visual-DAM.  
**Logic:** within cluster, compute median pHash distance or nearest-neighbor distance; assets with large nearest distance are outliers.  
**Use:** find failed style runs or prompt drift.

### Q14 — Missing originals but thumbnails remain

**User query:** `哪些 asset 原图不见了但还有 thumbnail？`  
**Module:** visual-DAM.  
**SQL:**

```sql
SELECT asset_id, original_path, thumbnail_path, missing_at, last_seen
FROM visual_dam_index
WHERE missing_at IS NOT NULL
ORDER BY missing_at DESC;
```

**Expected:** show missing state without deleting thumbnail history.

### Q15 — Large PNG storage pressure

**User query:** `最近 60 天最大的 PNG 视觉资产`  
**Module:** visual-DAM.  
**SQL:**

```sql
SELECT asset_id, file_size_bytes, dimensions_width, dimensions_height,
       thumbnail_path, created_at, original_path
FROM visual_dam_index
WHERE format = 'PNG'
  AND created_at >= datetime('now', '-60 days')
ORDER BY file_size_bytes DESC
LIMIT 50;
```

**Use:** identify disk-heavy assets without touching originals.

### Q16 — Similarity group by run

**User query:** `run_id=PFV-2026-05-05 中每组近重复图`  
**Module:** visual-DAM.  
**Logic:** for each asset in run, query pHash band candidates within same run; union-find groups pHash ≤6.  
**Expected:** grid displays duplicate groups with group size badges.

## 4. Cross Text + Visual Examples

### Q17 — Visual asset linked to dispatch intent

**User query:** `Wave5 visual reporting 相关图片和 dispatch 一起给我`  
**Modules:** hybrid-search + visual-DAM.  
**Process:** text search finds Dispatch156/167 and visual reporting report; metadata extraction yields `wave5`, `visual_reporting`; visual-DAM filters `prompt_cluster` or PF-V metadata containing those tags.  
**Output:** left = dispatch/result snippets; right = thumbnails; no claim that images are evidence unless U4/PF-V metadata says so.

### Q18 — Find mockups near a contract phrase

**User query:** `和 Trust Trace graph spec 相关的 mockup 图`  
**Modules:** hybrid-search first, visual-DAM second.  
**Process:** search finds `trust_trace_graph_spec`, extracts keywords `trust_trace`, `graph`, `node chain`; visual-DAM filters PF-V metadata/prompt cluster, then sorts by recency and duplicate group.

### Q19 — Search source decision then browse assets

**User query:** `Strong visual H5 四面板相关的 prompt 输出`  
**Modules:** search over visual specs + visual-DAM PF-V metadata.  
**Expected:** text evidence says four panels: URL Bar, Live Metadata, Capture Scope, Trust Trace; visual results show candidate mockups tagged with those panels.

### Q20 — Find old evidence for new visual prompt

**User query:** `这个新 prompt 是否已经做过类似风格？`  
**Modules:** visual-DAM.  
**Process:** if the user supplies a new generated image path, compute temporary pHash without inserting; query nearest indexed assets; optionally search text prompt snippets if the prompt is known.

## 5. Replay/U5 Lineage Examples

### Q21 — Dispatch127-176 run lineage

**User query:** `Replay Dispatch127-176 overnight chain`  
**Target:** dispatch pack manifest, COMMANDER-RUN-PROMPT, CHECKPOINT, Dispatch127-176 files.  
**Expected:** ordered list by dispatch number, task ID, status, candidate/runtime label, and file path.

### Q22 — From task to PR to current

**User query:** `T-P1A-104 之后 current 怎么变化？`  
**Process:** exact task ID lexical hit; search current for mentions; search task-index for landed PRs; return chronological chain.

### Q23 — Blocked runtime lane check

**User query:** `哪些 dispatch 可能暗示 browser automation 解禁？`  
**Process:** search `browser automation`, `Playwright`, `screenshot`, `localhost`, `runtime`; rank current prohibitions high; label dispatches as candidate/not approval.

### Q24 — DB migration risk

**User query:** `services/api/migrations 为什么 forbidden？`  
**Target:** current and DB vNext candidate.  
**Expected:** current says migration dry-run/schema changes require new dispatch + user explicit authorization + PR + external audit.

### Q25 — Retrieve all “not authority” docs in a cluster

**User query:** `visual pipeline not-authority candidate docs`  
**Process:** filter `authority_level IN ('candidate','not_authority')` and cluster `visual`; return docs but with warning that they cannot override PRD/SRD/current.

## 6. Combined Ranking Guidance

For cross-module queries, do not merge visual hash score and text score into one opaque number. Use separate ranked panes:

```json
{
  "text_evidence": [{"score": 0.91, "authority_label": "current"}],
  "visual_evidence": [{"hash_distance": 4, "similarity_bucket": "near_duplicate"}],
  "join_explanation": "Text results define the concept; visual results are PF-V assets whose metadata or hash neighborhood matches that concept."
}
```

This prevents an attractive thumbnail from being mistaken for authority evidence. It also keeps the UI aligned with ScoutFlow’s evidence discipline.


## 7. Additional Query Examples for Acceptance

### Q26 — Find all mentions of `write_enabled=False`

**User query:** `write_enabled false 所有上下文`  
**Expected:** `vault/commit.py`, U6 prompt boundary, README truth sections. Use exact lexical match and underscore/space alias expansion.

### Q27 — Candidate docs that should not be promoted

**User query:** `哪些 DB vNext 文档明确不是 migration approval`  
**Expected:** DB vNext candidate and current prohibition; result warning: “not migration approval.”

### Q28 — Local tool readiness

**User query:** `本机 sentence-transformers ollama whisper 状态`  
**Expected:** local probe report from README/LIVE-WEB-EVIDENCE plus caveat that probe is execution sandbox, not the user Mac.

### Q29 — Visual outlier plus textual reason

**User query:** `找出 hero-card prompt cluster 中离群图，并显示相关 prompt notes`  
**Modules:** visual-DAM pHash nearest-neighbor outlier + hybrid-search over PF-V/prompt notes if indexed.  
**Expected:** thumbnails sorted by outlier distance; text snippets shown only if prompt metadata exists.

### Q30 — Authority versus external report conflict

**User query:** `外部报告建议 canary，但 current 是否允许 frontend?`  
**Expected:** show external recommendation and current prohibition together; answer should say recommendation exists but does not approve frontend implementation.

## 8. Query Evaluation Checklist

For every example query, evaluate:

| Check | Pass condition |
|---|---|
| exact identifiers | task/PR/dispatch IDs preserved in top results |
| authority label | current/contract/candidate clearly shown |
| no false approval | candidate docs do not imply runtime approval |
| line/path evidence | text results include file path and line range |
| visual safety | visual results show derived thumbnail, not original mutation |
| local privacy | no cloud lookup needed |
| bilingual recall | Chinese query can find English identifiers and vice versa |
| time filter | dates affect ranking when query contains time |

A query that returns the right file but hides candidate status is not a pass. ScoutFlow retrieval is evidence retrieval, not just document search.


## 9. More Combined Queries

### Q31 — “Show me all candidate specs that mention no cloud embedding”

Use hybrid search with lexical anchors `cloud embedding`, `local-only`, `privacy`, and authority labels. Expected result includes U6 files and SRD/PRD privacy boundaries. This checks that the package itself can be indexed later.

### Q32 — “Which visual assets are near duplicates of a missing original?”

Use `visual_dam_index WHERE missing_at IS NOT NULL`, then pHash query for each missing asset. This helps recover context when originals were moved but thumbnails/hash history remain.

### Q33 — “Find all tasks related to Wave5 visual proof gap”

Search terms: `Wave5`, `visual`, `screenshot`, `human visual verdict`, `5 Gate`. Expected results include current and external report rows that say static readiness is not proof.

### Q34 — “What did the code actually implement versus docs claim?”

Search both `source_code` and docs for a feature, then group results by kind. For `healthz`, code says liveness only; docs should not claim DB readiness.

### Q35 — “Which assets belong to prompt clusters mentioned in a dispatch?”

Text search extracts `prompt_cluster` or visual concept keywords from dispatch; DAM filters PF-V metadata and returns thumbnails. This is a practical bridge from planning docs to visual inventory.


## 10. Result Presentation Rule

Combined query UI should always keep evidence type visible. A thumbnail is not a textual decision; a dispatch is not current authority; a DB candidate is not a migration. Recommended badges: `current`, `PRD/SRD`, `contract`, `promoted_addendum`, `candidate`, `external_report`, `dispatch`, `source_code`, `derived_visual`. Badges should be visible in collapsed result cards so the user does not need to open every result to understand trust level.


## 11. Example Count

This file defines 35 examples, exceeding the requested 15. The extra examples are included to make future acceptance testing concrete rather than subjective.


## 12. Final Acceptance Note

The example suite should be converted into a regression fixture after implementation. Search quality should be measured, not judged by vibes.
