<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# MODULE — hybrid-local-search Spec — 2026-05-07

> Claim label: candidate ≥95% for local architecture, ranking design, and ScoutFlow boundary fit; external 2026 tool currency requires live-web refresh.  
> Scope: SQLite FTS5 + local sentence embeddings + hybrid reranking over PR, memory, handoff, dispatch transcript, decision log, wiki/candidate/source docs.  
> Budget target: ≤500 LOC Python for first working sidecar.  
> Authority posture: derived, rebuildable, read-mostly local projection; no cloud embedding.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Why Hybrid Search Is Required

ScoutFlow now has too many truth surfaces for `grep` alone: PR chain, PRD/SRD, current, task-index, decision log, dispatch127-176, memory files, handoff packets, research reports, and code refs. The daily failure mode is not “no document exists”; it is “the relevant decision exists but is split across task ID, PR number, phase name, and user override wording.”

A pure FTS search finds exact tokens like `supersession`, `T-P1A-104`, or `audio_transcript`. It fails when the user asks semantic questions like “Codex 在 May 4 关于 supersession 的决定” and the document uses `superseded_by` or “PR #93 不得原样合并”. A pure embedding search finds paraphrases but can under-rank exact identifiers. Therefore U6 should use a **hybrid retrieval** pipeline: FTS5/BM25 for exact lexical anchors, local dense embeddings for semantic recall, then a small reranker that explains why each result appeared.

## 2. Scope and Non-goals

### 2.1 In scope

- Index Markdown docs, PR summaries/diffs when locally available, handoff files, dispatch transcript files, memory files, decision logs, wiki pages, candidate specs, and selected source code.
- Chunk documents into citeable spans with file path, line range, source kind, date, phase, cluster, PR/task IDs, and supersession markers.
- Use SQLite FTS5 for lexical search.
- Use local embeddings from `sentence-transformers`, `ollama`, Apple-local models, or another local provider. No OpenAI/Anthropic/cloud embedding API.
- Support both exact ID queries and loose bilingual Chinese/English queries.
- Return results with enough metadata for Replay/U5 to reconstruct lineage.

### 2.2 Out of scope

- No enterprise ElasticSearch, OpenSearch, pgvector, hosted vector DB, SaaS RAG platform, or team sharing.
- No authoritative writeback into ScoutFlow DB.
- No automatic PR creation, no issue updates, no GitHub comments.
- No document generation by the search service itself.
- No cloud embedding or telemetry.

## 3. Corpus Kinds

The `kind` enum should stay close to the U6 prompt:

```text
PR | memory | handoff | dispatch_transcript | decision_log | wiki | candidate | source_code | report | contract | current
```

A source adapter maps files into normalized documents. Examples:

| Source | kind | Key metadata |
|---|---|---|
| `docs/PRD-v2-2026-05-04.md` | contract | phase, authority_level, created_at |
| `docs/SRD-v2-2026-05-04.md` | contract | phase, authority_level, created_at |
| `docs/current.md` | current | active phase, blocked lanes, handoff |
| `docs/task-index.md` | decision_log | task IDs, PR numbers, merge commits |
| `dispatches/Dispatch*.md` | dispatch_transcript | dispatch number, task ID, wave, candidate/runtime flag |
| external reports | report | report title, review domain, candidate status |
| code refs | source_code | module path, API route, symbol names |
| memory files | memory | source session, timestamp, cluster |
| handoff trail | handoff | handoff ID, from/to agent, continuation |

## 4. SQLite Data Model

The first release can use one SQLite DB: `data/derived/search/search.sqlite`. It is not the ScoutFlow authority database. It can be deleted and rebuilt.

```sql
-- ============================================================
-- CANDIDATE DDL — derived hybrid search projection
-- NOT A SCOUTFLOW AUTHORITY MIGRATION
-- ============================================================
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS search_documents (
    doc_id TEXT PRIMARY KEY,
    kind TEXT NOT NULL CHECK(kind IN (
        'PR','memory','handoff','dispatch_transcript','decision_log','wiki',
        'candidate','source_code','report','contract','current'
    )),
    title TEXT NOT NULL,
    file_path TEXT NOT NULL,
    source_uri TEXT,
    created_at TEXT,
    modified_at TEXT,
    phase TEXT,
    cluster TEXT,
    task_id TEXT,
    pr_number TEXT,
    authority_level TEXT NOT NULL DEFAULT 'candidate',
    sha256 TEXT NOT NULL,
    indexed_at TEXT NOT NULL,
    metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS search_chunks (
    chunk_id TEXT PRIMARY KEY,
    doc_id TEXT NOT NULL,
    chunk_index INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    body_normalized TEXT NOT NULL,
    start_line INTEGER,
    end_line INTEGER,
    token_count_est INTEGER NOT NULL,
    created_at TEXT,
    phase TEXT,
    cluster TEXT,
    task_id TEXT,
    pr_number TEXT,
    metadata_json TEXT NOT NULL DEFAULT '{}',
    FOREIGN KEY(doc_id) REFERENCES search_documents(doc_id) ON DELETE CASCADE,
    UNIQUE(doc_id, chunk_index)
);

CREATE VIRTUAL TABLE IF NOT EXISTS search_chunks_fts USING fts5(
    title,
    body_normalized,
    kind UNINDEXED,
    phase UNINDEXED,
    cluster UNINDEXED,
    task_id UNINDEXED,
    pr_number UNINDEXED,
    content='search_chunks',
    content_rowid='rowid',
    tokenize='unicode61 remove_diacritics 2'
);

-- Optional CJK fallback. If the local SQLite build supports trigram, use it
-- for Chinese substring recall. If not, generate char-bigram terms into
-- body_normalized and skip this table.
CREATE VIRTUAL TABLE IF NOT EXISTS search_chunks_tri USING fts5(
    title,
    body_normalized,
    content='search_chunks',
    content_rowid='rowid',
    tokenize='trigram'
);

CREATE TABLE IF NOT EXISTS search_embeddings (
    chunk_id TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    model_name TEXT NOT NULL,
    dimensions INTEGER NOT NULL CHECK(dimensions > 0),
    embedding_blob BLOB NOT NULL,
    embedding_norm REAL NOT NULL,
    embedded_at TEXT NOT NULL,
    FOREIGN KEY(chunk_id) REFERENCES search_chunks(chunk_id) ON DELETE CASCADE
);
```

SQLite `rowid` handling with external-content FTS can be annoying. In implementation, either add an integer surrogate key to `search_chunks`, or use a contentless FTS table and insert explicit `chunk_id` in an unindexed column. The spec favors citeability over cleverness: the service must always return `doc_id`, `chunk_id`, `file_path`, `start_line`, and `end_line`.

## 5. Chunking Rules

Chunking is the heart of retrieval quality. Recommended defaults:

- Markdown heading-aware chunks: keep `#`, `##`, `###` hierarchy in metadata.
- Target 600-900 tokens or 2200-3500 characters per chunk.
- Overlap 80-120 tokens for long prose sections.
- Never split a table row group if it contains task IDs or PR numbers.
- For code, chunk by file and function/class boundary when possible; otherwise 120 lines with 20-line overlap.
- Keep line ranges. For generated Markdown, line-range citations are more valuable than abstract snippets.
- Normalize identifiers into extra lexical text: `PR #139`, `PR139`, `pull request 139`; `T-P1A-104`, `TP1A104`; `audio_transcript`, `audio transcript`.

Chinese/English mixed queries need explicit normalization. The normalizer should:

1. Lowercase ASCII but preserve original body for display.
2. Insert spaces around task IDs, PR IDs, dates, slashes, underscores, and camelCase boundaries.
3. Add a CJK bigram shadow string when trigram FTS is unavailable.
4. Expand known ScoutFlow aliases: `PRD`, `product requirements`, `产品基线`; `SRD`, `software requirements`, `工程基线`; `supersession`, `superseded_by`, `不得原样合并`; `runtime blocked`, `blocked lane`, `禁止`.

## 6. Embedding Storage Options

Three storage modes are acceptable for first release:

| Mode | Fit | Tradeoff |
|---|---|---|
| SQLite BLOB + Python brute-force/top-N | simplest for ≤20k chunks | enough for single-user; no extension install |
| sqlite-vec/sqlite-vss extension | faster vector query in SQLite | needs local extension install and live version check |
| FAISS sidecar index + SQLite metadata | fast and mature for many vectors | extra index file, rebuild discipline needed |

Because the prompt asks for single-user ≤500 LOC, the first release should not block on sqlite-vss. Use SQLite BLOB embeddings plus a NumPy cosine scan for the filtered candidate set. A later optimization can swap to sqlite-vec/vss/FAISS without changing `search_chunks` identity.

For 5k-25k chunks, brute-force cosine over normalized float32 embeddings is acceptable on an M-series Mac if batched and memory-mapped. Example size: 20k chunks × 1024 dimensions × 4 bytes = about 80 MB before SQLite overhead. The DB budget remains plausible if chunk count and model dimensions are controlled.

## 7. Hybrid Query Algorithm

The query pipeline:

```text
user query
  -> normalize query + extract filters/IDs/dates
  -> FTS5 lexical search top K_lex=80
  -> embedding encode query locally
  -> dense cosine search top K_dense=80
  -> merge candidates by chunk_id
  -> feature scoring and rerank top 30
  -> group by doc_id if requested
  -> return explainable snippets + line ranges
```

Recommended weighted sum:

```text
score = 0.45 * lexical_score_norm
      + 0.40 * dense_score_norm
      + 0.10 * metadata_boost
      + 0.05 * recency_or_authority_boost
```

Where:

- `lexical_score_norm`: normalize BM25 so best lexical result is 1.0. SQLite FTS5 `bm25()` returns lower is better, so convert carefully.
- `dense_score_norm`: cosine similarity after L2-normalizing embeddings; clamp to [0,1] for display.
- `metadata_boost`: exact task ID, PR number, dispatch number, phase, or kind match.
- `authority_boost`: `current`/contract docs outrank external reports when answering “what is allowed now”; candidate docs remain visible but labeled.

For ID-heavy queries, lexical and metadata should dominate. For vague conceptual queries, dense should dominate. Implement a simple query classifier:

```text
if query contains PR number/task ID/date/exact state word -> lexical_weight=0.55, dense_weight=0.30
else if query length < 4 tokens -> lexical_weight=0.50, dense_weight=0.35
else -> lexical_weight=0.40, dense_weight=0.45
```

Reciprocal Rank Fusion (RRF) is a robust alternative:

```text
rrf_score = 1/(60 + lexical_rank) + 1/(60 + dense_rank)
```

The first release can expose both modes behind config, but default to weighted sum because it provides easier explanations and lets authority boosts be explicit.

## 8. Query Examples

The service should answer:

- “Codex 在 May 4 关于 supersession 的决定是什么？”
- “为什么 audio_transcript 仍然 blocked？”
- “PR #93 和 T-P1A-103 的关系？”
- “哪个 dispatch 讨论 Wave5 visual reporting？”
- “找出所有说 frontend implementation 不批准的上下文。”
- “Replay Dispatch127-176 lineage，给我 task -> PR -> artifact 的链。”
- “DB vNext evidence_ledger 和 artifact_assets 的关系是什么？”
- “Bridge/VaultWriter 现在是否可以 true write？”
- “哪些 external reports 说 search/index 是 daily loop 风险？”

Each result must include source labels: `authority`, `promoted_addendum`, `candidate`, `external_report`, `dispatch`, or `code_ref`. This prevents a candidate report from outranking current authority in a way that misleads an operator.

## 9. Incremental Indexing

A file watcher is useful but not mandatory for the first release. The simpler path:

```bash
python -m local_search index --config local.search.yaml
python -m local_search query "audio_transcript blocked"
python -m local_search serve --host 127.0.0.1
```

Incremental indexing checks `file_path`, `mtime`, `size`, and `sha256`. If unchanged, skip chunking and embedding. If changed, delete old chunks and embeddings for that doc inside a transaction, insert new chunks, update FTS, then queue embeddings. Embeddings can lag lexical indexing; query results should display `embedding_status=missing` rather than failing.

## 10. Replay/U5 Integration

U5 replay needs lineage, not just snippets. Add metadata extraction for:

- dispatch number: `Dispatch176`
- task ID: `T-P1A-155`
- PR number: `PR #139`
- merge commit when present
- file domain matrix entries
- state words: blocked, candidate, landed, promoted, superseded, not authority
- run IDs and checkpoint paths

A replay query should return ordered segments:

```json
{
  "query": "Dispatch127-176 supersession lineage",
  "results": [
    {
      "chunk_id": "...",
      "kind": "dispatch_transcript",
      "file_path": ".../Dispatch176...md",
      "line_range": [1, 80],
      "task_id": "T-P1A-155",
      "score_breakdown": {"lexical": 0.88, "dense": 0.74, "metadata": 1.0},
      "authority_label": "candidate"
    }
  ]
}
```

## 11. Privacy and Safety

Embedding is a privacy boundary. The corpus includes handoffs, memory, dispatch transcripts, and possibly private project paths. Therefore:

- No cloud embedding API.
- No remote vector DB.
- No automatic telemetry.
- No indexing of credentials, cookies, QR images, auth sidecars, browser profiles, `data/`, `referencerepo/`, `.env`, or raw stdout/stderr unless a future safe adapter explicitly redacts them.
- Redaction patterns should run before chunking.
- Config must require explicit source roots.
- Query server binds to `127.0.0.1` only.

## 12. LOC Budget

A ≤500 LOC MVP is credible if kept ruthless:

| Component | LOC |
|---|---:|
| config + source globbing | 45 |
| metadata extraction | 70 |
| Markdown/code chunking | 85 |
| SQLite DDL/repository/FTS maintenance | 110 |
| embedding provider wrapper | 70 |
| hybrid query/rerank | 80 |
| CLI | 45 |
| tiny local API optional | defer or 70 extra |

The first implementation should be CLI-first. A UI can reuse the grid browser pattern later, but U6’s core value is retrieval quality and lineage correctness, not a dashboard.


## 13. Authority-Aware Reranking Appendix

ScoutFlow search must not behave like a generic RAG demo. Many documents are intentionally `candidate`, `not-authority`, or historical. The reranker should include an explicit authority model:

```text
authority_weight(query, result):
  if query asks "allowed now", "current", "can we", "是否批准":
      current/contract/base docs get +0.20
      promoted addenda get +0.10 with boundary label
      candidate reports get -0.10 unless exact match
      archive/historical gets -0.20 unless query asks history
  elif query asks "who discussed", "which dispatch", "history", "why":
      dispatch and reports can rank normally
  else:
      keep mild +0.05 for current/contract
```

This is not bureaucracy; it prevents dangerous answers. A visual report can say a screenshot harness exists, while current can say browser automation is still blocked. The search service should surface both, but the answer to “is it approved?” must privilege current/contract.

## 14. Known-Answer Benchmark Appendix

Before enabling semantic rerank by default, create a local benchmark file:

```yaml
queries:
  - id: q_audio_blocked
    query: 为什么 audio_transcript runtime 仍 blocked？
    must_include_any:
      - docs/PRD-v2-2026-05-04.md
      - docs/SRD-v2-2026-05-04.md
      - docs/current.md
    forbidden_top1_if:
      - external report only
  - id: q_supersession
    query: PR #93 T-P1A-103 supersede
    must_include_any:
      - docs/current.md
      - docs/task-index.md
  - id: q_vault_write
    query: VaultWriter true write approved?
    must_include_any:
      - services/api/scoutflow_api/vault/commit.py
      - docs/current.md
```

Run the same query set against each embedding provider. Record `top1`, `recall@5`, `authority_correct`, and latency. The best model is not the one with the nicest vendor page; it is the one that retrieves the right ScoutFlow chunk with the right authority label.

## 15. CLI Contract

The search sidecar can be useful without a server:

```bash
u6-search index --config local.search.yaml
u6-search query "audio_transcript blocked" --top 8
u6-search query "PR #93 superseded" --kind current,decision_log
u6-search benchmark --queries local.known-answer.yaml
u6-search rebuild --atomic
```

Suggested stdout:

```yaml
query: audio_transcript blocked
mode: hybrid
embedding_provider: sentence_transformers
model: BAAI/bge-m3
cloud_calls: 0
results:
  - rank: 1
    file_path: docs/SRD-v2-2026-05-04.md
    line_range: [110, 130]
    authority_label: authority
    score: 0.93
    why: exact phrase + authority boost + dense match
```

Line ranges are not optional. They are the difference between a search result the user can audit and a black-box answer.

## 16. Source Adapter Detail

PR and git data can be indexed in layers. First, index local Markdown task-index and dispatches. Second, if the local git repo is present, index `git log --oneline --decorate`, merge commit messages, and changed file lists. Third, if PR metadata has been exported from GitHub, index PR title/body/comments as `PR` kind. U6 does not need GitHub live calls to function. It should prefer local exported facts to network calls.

Memory and handoff files need special care. They may contain private reasoning summaries or operator notes. Index only files explicitly included by config. Add a redaction pass before embeddings so a secret-like value cannot be sent even to a local model endpoint that the user misconfigured to non-loopback. The provider wrapper should reject non-loopback endpoints, but defense in depth is appropriate.

## 17. Failure Mode Examples

| Failure | Bad behavior | Correct behavior |
|---|---|---|
| model not installed | crash on every query | run lexical-only and print provider unavailable |
| FTS tokenizer poor for Chinese | user thinks no result exists | trigram/bigram fallback, alias expansion |
| candidate report exact phrase | candidate outranks current for approval question | candidate shown with warning, current boosted |
| old archive result | stale rule appears current | archive label and time-aware rerank |
| huge code file | chunk too large, embedding truncates | function/line chunking |
| changed model dimensions | cosine scan crashes | embedding_version invalidates old rows |
| corrupted FTS table | empty results | rebuild FTS from chunks |

Hybrid search is valuable only if it remains trustworthy under these mundane failures.


## 18. FTS Maintenance Detail

SQLite FTS5 external-content tables are efficient but require disciplined updates. A low-risk implementation can avoid triggers and update FTS rows explicitly inside the same transaction that writes `search_chunks`:

```text
reindex_doc(doc):
  begin transaction
  delete from search_chunks_fts where rowid in old rowids
  delete from search_chunks where doc_id = doc.doc_id
  upsert search_documents
  for chunk in new_chunks:
      insert search_chunks
      insert search_chunks_fts(rowid, title, body_normalized, kind, phase, cluster, task_id, pr_number)
  commit
```

If rowids are unstable or awkward, use a contentless table with explicit `chunk_id` stored as an unindexed column. The implementation should choose the simpler route after testing against the local SQLite build. Correctness beats theoretical elegance.

## 19. Dense Scan Pseudocode

For ≤20k chunks, vector extension is not mandatory:

```text
encode query -> q float32 normalized
load embeddings where provider/model active
if filters exist:
  restrict to chunk_ids from lexical/date/kind filter first
matrix = np.vstack(candidate_vectors)
scores = matrix @ q
select top K dense
merge with lexical top K
rerank with metadata/authority features
```

This is fast enough for a first single-user corpus and avoids extension install risk. If the corpus grows to hundreds of thousands of chunks, FAISS or sqlite-vec can be adopted behind the same provider abstraction.

## 20. Date and Phase Handling

Dates in user queries should be extracted but not over-trusted. “May 4” in this project likely means 2026-05-04 because the source pack centers around May 2026. The query parser can infer year from corpus context only when safe, then display the assumption:

```yaml
date_interpretation:
  input: May 4
  interpreted_as: 2026-05-04
  reason: corpus window 2026-05-04 to 2026-05-05
```

Phase labels (`Phase 1A`, `Wave 4`, `Wave5`, `STEP3`) should be extracted into metadata so the user can filter. Search should also preserve contradictory timing: a candidate can discuss future Phase 2 while current says Phase 2 runtime is not approved.


## 21. Answer Assembly Boundary

The search module should retrieve evidence, not invent final authority. A caller may use results to draft an answer, but `hybrid-local-search` itself returns ranked chunks and score explanations. This separation matters because ScoutFlow often asks “what is true now?” A search result can include conflicting chunks: current says blocked, a candidate says future plan, code says dry-run. The service should expose conflict rather than collapse it.

Suggested response fields:

```json
{
  "query": "frontend 是否批准",
  "assumptions": ["interpreted frontend as H5/frontend implementation"],
  "results": [],
  "conflicts_detected": [
    {
      "topic": "frontend runtime approval",
      "authority_result": "current blocks implementation",
      "candidate_result": "visual specs discuss future UI"
    }
  ]
}
```

This makes U6 a dependable operator tool rather than a black-box chatbot.

## 22. Source Freshness and Tombstones

When a document disappears, do not immediately erase it from search if it was part of a known handoff trail. Mark `missing_at` and lower its rank. For files under generated temporary folders, deletion can remove rows on rebuild. For authority docs, disappearance is itself notable and should be reported in status. Tombstones help explain why an old query result changed after a rebuild.


## 23. Minimum Search Non-negotiables

The minimum viable search tool passes only if it can answer exact-ID questions, authority-boundary questions, and broad semantic questions without hiding source labels. Exact-ID means PR numbers, task IDs, dispatch IDs, and filenames are preserved. Authority-boundary means current/PRD/SRD outrank candidate reports when the query asks whether something is approved. Broad semantic means Chinese/English paraphrases can find related docs when lexical terms differ. If embeddings are unavailable, the tool still returns lexical results and says `mode=lexical_only`; it does not fake dense recall. If line ranges cannot be produced for a source, the result should say `line_range_unavailable` rather than inventing citations.


## 24. Minimal API Shape If a Server Is Added

A server is optional, but if added it should stay read-only and loopback-only:

```text
GET /api/search?q=&kind=&phase=&top=
GET /api/docs/{doc_id}
GET /api/chunks/{chunk_id}
GET /api/status
```

No endpoint writes ScoutFlow authority, no endpoint downloads models, and no endpoint changes config. Configuration remains a local file and CLI concern. This prevents a convenience UI from becoming an unreviewed control plane. The API should return raw ranked results and score breakdowns, not final prose answers. A separate assistant or user can synthesize an answer from evidence.


## 25. Final Search Acceptance Sentence

The MVP is acceptable only when a skeptical reviewer can run one command, ask a blocked-runtime question, get current authority first, see candidate material second, and inspect file path plus line range without trusting hidden model reasoning.


## 26. Extra Acceptance Guard

A final guardrail: any result generated from archive, external report, or candidate dispatch must carry that label in the first screen of output. Hidden labels are a failure because the user may otherwise mistake historical or speculative material for current permission.


## 27. Final Label Guard

Search is accepted only when labels, scores, and source paths are visible together.
