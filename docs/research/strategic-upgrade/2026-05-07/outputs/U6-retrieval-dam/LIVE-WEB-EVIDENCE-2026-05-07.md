<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# LIVE WEB EVIDENCE — 2026-05-07

> Claim label: **blocked / not live-verified**.  
> Reason: this execution environment has web browsing disabled. I cannot truthfully claim ≥18 live searches, vendor access dates, or 2026 freshness checks.  
> This file provides the evidence-refresh checklist, vendor/topic inventory, and decision impact. It must be refreshed in a browsing-enabled window before final authority promotion.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Truth Statement

Live web browsing was requested by U6, including ≥18 searches across SQLite FTS5, sqlite-vss/sqlite-vec, Chroma, LanceDB, DuckDB vector, embedding models, Ollama, Apple Foundation Models, pHash/dHash/aHash, macOS Spotlight, and prosumer DAM tools. In this environment, the `web` tool is disabled. Therefore:

```yaml
live_web_browsing_used: false
live_verified_count: 0
vendor_access_dates: none
external_2026_currency: not_verified
```

No URL in this file should be treated as freshly visited. The module specs are still useful as local architecture candidates, but external tool selection must be refreshed before implementation.

## 2. Evidence Refresh Checklist

When browsing is enabled, run at least these searches and record access date, exact URL, version/release status, license, install friction, and relevance to U6.

| # | Topic/vendor | What to verify | Decision impact | Current status |
|---:|---|---|---|---|
| 1 | SQLite FTS5 official docs | tokenizer options, external content tables, bm25 behavior | FTS schema/query correctness | not live-verified |
| 2 | SQLite trigram tokenizer | availability in user SQLite build and syntax | CJK substring search strategy | not live-verified |
| 3 | sqlite-vec | install method, binary availability, current maintenance | vector-in-SQLite option | not live-verified |
| 4 | sqlite-vss | maintenance status, FAISS dependency, platform support | vector extension option | not live-verified |
| 5 | FAISS on macOS/Apple Silicon | pip wheels, CPU/MPS status, install pain | fallback vector index | not live-verified |
| 6 | Chroma local | embedded/local mode, disk layout, telemetry controls | alternative local vector DB | not live-verified |
| 7 | LanceDB | local file-backed vector table, Python API, disk behavior | alternative vector DB | not live-verified |
| 8 | DuckDB vector/search | vector similarity extension/status | alternative analytic store | not live-verified |
| 9 | sentence-transformers | current Apple Silicon/MPS support, bge-m3 usage | primary embedding path | not live-verified |
| 10 | BAAI/bge-m3 | model card, dimensions, license, multilingual claims | primary model decision | not live-verified |
| 11 | intfloat multilingual-e5 | model card, query/passsage prefix requirement | fallback model | not live-verified |
| 12 | nomic-embed-text | current local embedding model status | Ollama fallback | not live-verified |
| 13 | mxbai-embed-large | current embedding dimensions/license/local availability | Ollama fallback | not live-verified |
| 14 | Ollama embeddings API | local endpoint behavior, model list, privacy | fallback provider | not live-verified |
| 15 | Apple Foundation Models | embedding API availability and local-only guarantee | future Apple-native option | not live-verified |
| 16 | Apple MLX | embedding model support/conversions | Apple Silicon optimization | not live-verified |
| 17 | PyTorch MPS | current stability/limitations for sentence-transformers | primary acceleration | not live-verified |
| 18 | Core ML tools | conversion path for embedding models | later optimization | not live-verified |
| 19 | Pillow image processing | format support, security notes | thumbnail pipeline | not live-verified |
| 20 | ImageHash / pHash/dHash/aHash libraries | implementation quality and dependencies | DAM hash pipeline | not live-verified |
| 21 | OpenCV pHash alternatives | whether worth dependency | likely defer | not live-verified |
| 22 | macOS `mdls` / Spotlight metadata | read-only metadata fields and behavior | Finder/Spotlight read-only integration | not live-verified |
| 23 | macOS xattr/Finder tags | read vs write semantics | enforce no-write boundary | not live-verified |
| 24 | Eagle DAM | prosumer workflow patterns | UI inspiration only | not live-verified |
| 25 | Mylio DAM | prosumer local DAM organization patterns | UI inspiration only | not live-verified |
| 26 | Reciprocal Rank Fusion papers/posts/docs | RRF formula and tuning | hybrid rerank option | not live-verified |
| 27 | BM25 + dense hybrid retrieval current practice | weighting/normalization patterns | ranking design | not live-verified |
| 28 | CLIP/SigLIP local image embeddings | semantic visual search feasibility | future DAM extension | not live-verified |

## 3. Vendor Evidence Template

Each live evidence row should be captured like this:

```markdown
### <Vendor / project>
- URL:
- Accessed at:
- Version/release observed:
- License observed:
- Local-only? yes/no/unclear
- Apple Silicon notes:
- Install friction:
- U6 relevance:
- Decision: adopt / benchmark / defer / reject
- Evidence quote:
```

Do not write “accessed” unless a real page was opened in that browsing-enabled session.

## 4. Decision Impact of Missing Live Web

The missing live refresh affects tool choice, not the core architecture. The following are safe architectural decisions even without live web:

- local-first, single-user, derived SQLite projection;
- FTS5 lexical retrieval as a base;
- local embeddings only;
- no cloud embeddings;
- pHash/dHash/sha256 for visual dedup;
- thumbnails in derived storage;
- no Spotlight write;
- no original file mutation;
- authority labels and candidate/not-authority separation.

The following must wait for live verification:

- whether sqlite-vec or sqlite-vss is the better SQLite vector extension in 2026;
- whether bge-m3 remains the best first model versus newer local bilingual models;
- whether Apple Foundation Models offers an embedding API suitable for this local Python workflow;
- whether Ollama’s current model list includes the desired embedding models on the user’s machine;
- whether Chroma/LanceDB/DuckDB vector have changed enough to beat the simple SQLite BLOB + NumPy MVP;
- current best practices around pHash libraries and imagehash dependencies;
- current macOS Spotlight/xattr behavior on the user’s OS version.

## 5. Interim Recommendations Without Live Web

The implementation-safe interim posture is:

1. Build search MVP with SQLite FTS5 and optional SQLite BLOB embeddings, not with a hard dependency on a vector extension.
2. Choose embedding provider by local install state: sentence-transformers if available, Ollama if available, lexical-only otherwise.
3. Do not install a heavy vector DB until a benchmark proves SQLite BLOB + NumPy is insufficient.
4. Build visual-DAM with Pillow + pHash/dHash/aHash + hash bands; defer CLIP/SigLIP semantic visual search.
5. Treat all vendor choices as `candidate_pending_live_refresh`.

## 6. Local Probe Results

Execution sandbox probe:

```yaml
which_whisper: not_found
which_ollama: not_found
python_import_sentence_transformers: not_found
python_import_PIL: installed
python_import_faiss: not_found
python_import_chromadb: not_found
python_import_lancedb: not_found
python_import_duckdb: not_found
sqlite_fts5: available
```

This is not the user’s Mac. It only tells us what was available where this package was generated. The final implementation should run the same probe on the user’s machine and write the result into a local-only readiness report.

## 7. Stop Conditions

Do not promote U6 to authority if any of these remain unresolved:

- live web evidence count is zero;
- chosen embedding model has no local-only proof;
- vector extension requires unsafe install or cloud service;
- pHash thresholds are untested on PF-V assets;
- Spotlight integration writes metadata;
- model cache exceeds budget without user approval;
- search ranks candidate reports above current authority for “what is allowed now?” queries.

This file is intentionally conservative. It preserves trust by refusing to manufacture evidence.


## 8. Minimum Live Search Log Target

A browsing-enabled refresh should produce at least 18 concrete evidence entries. A strong refresh would include 28 entries from the table above, but the hard minimum can be:

```text
1 SQLite FTS5 docs
2 SQLite trigram tokenizer docs
3 sqlite-vec project/release
4 sqlite-vss project/release
5 FAISS macOS install/current notes
6 sentence-transformers install/MPS/current docs
7 BAAI/bge-m3 model card
8 multilingual-e5 model card
9 nomic-embed-text model card/provider page
10 mxbai-embed-large model card/provider page
11 Ollama embeddings API docs
12 Apple Foundation Models docs
13 MLX docs/model support
14 PyTorch MPS docs
15 Core ML conversion docs
16 Pillow docs/security notes
17 ImageHash/pHash/dHash/aHash docs or benchmark
18 macOS mdls/xattr/Spotlight metadata reference
```

For each, record whether it changes U6. If a source is stale, archived, or installation-hostile, mark `defer` or `reject` rather than forcing it into the architecture.

## 9. Claims That Must Not Be Made Yet

Because no live browsing occurred, the following claims would be unsafe:

- “sqlite-vec is definitely better than sqlite-vss in 2026.”
- “Apple Foundation Models provides a production-ready embedding API for this workflow.”
- “Ollama currently supports the exact chosen embedding model on the user’s machine.”
- “bge-m3 is the latest best bilingual model.”
- “Eagle/Mylio current feature sets support a particular workflow.”
- “macOS Spotlight metadata fields behave the same on the user’s OS version.”

The generated specs avoid those claims. They name candidates and define verification gates.

## 10. Evidence Refresh Output Contract

After live refresh, update this file with:

```yaml
live_web_browsing_used: true
live_verified_count: <count>
access_window_started: <timestamp>
access_window_finished: <timestamp>
adopted_tools:
  vector_storage: sqlite_blob_numpy | sqlite_vec | sqlite_vss | faiss
  embedding_primary: <model>
  embedding_fallback: <model/provider>
  dam_hash_library: <library or local implementation>
rejected_tools:
  - name: <tool>
    reason: <privacy/install/overkill/stale>
```

Only then should README stdout move from `multi_pass_completed: 9/10` to `10/10`.


## 11. Suggested Search Queries for Refresh

Use concrete searches, not vague browsing:

```text
SQLite FTS5 bm25 external content table tokenizer trigram 2026
sqlite-vec SQLite vector extension macOS install 2026
sqlite-vss FAISS SQLite extension maintenance 2026
sentence-transformers Apple Silicon MPS embeddings bge-m3
BAAI bge-m3 model card dimensions license multilingual
Ollama embeddings API nomic-embed-text mxbai bge-m3 local
Apple Foundation Models embeddings local API documentation 2026
MLX embedding models Apple Silicon sentence transformers alternative
PyTorch MPS sentence-transformers known limitations embeddings
Pillow image thumbnail EXIF security decompression bomb
ImageHash pHash dHash aHash Python perceptual hash benchmark
macOS mdls Spotlight metadata read kMDItemPixelWidth
macOS xattr Finder tags read write safety
Eagle DAM local digital asset management thumbnails tags 2026
Mylio DAM local photo management metadata 2026
hybrid search BM25 dense retrieval reciprocal rank fusion 2026
LanceDB local vector database Python file backed 2026
Chroma local persistent client telemetry disable 2026
DuckDB vector similarity extension 2026
FAISS Apple Silicon pip install macOS arm64 2026
```

Record the exact query, URL clicked, and access timestamp. Search result snippets alone are not enough.

## 12. Adoption Criteria Per Tool Class

| Tool class | Adopt only if | Reject/defer if |
|---|---|---|
| vector extension | local install simple, maintained, works on Apple Silicon | build from source fragile, stale, DB locks unclear |
| embedding model | local-only, bilingual benchmark good, ≤2GB target or approved exception | cloud-only, unclear license, poor Chinese recall |
| DAM library | small dependency, safe image handling, deterministic hash | heavy dependency for no measured gain |
| local vector DB | materially beats SQLite MVP | adds daemon/state/telemetry/backup complexity |
| Apple-native API | local-only proof and quality benchmark | API unclear or tied to cloud/account state |
| prosumer DAM reference | gives UI/workflow ideas | tempts migration into separate app |

## 13. Refresh Failure Handling

If live refresh finds a tool is stale or unsuitable, do not rewrite the whole architecture. The architecture is intentionally adapter-based:

- vector extension fails → use SQLite BLOB + NumPy;
- bge-m3 unsuitable → benchmark E5/MiniLM/Ollama local options;
- Ollama absent → sentence-transformers or lexical-only;
- Apple Foundation Models unavailable → no change;
- ImageHash library unsuitable → implement small pHash/dHash with Pillow/NumPy;
- Chroma/LanceDB too heavy → no change.

A robust spec should survive vendor drift.


## 14. How to Use This File After Refresh

After live browsing, this file should become a decision ledger, not a link dump. Each evidence entry should end with one of four decisions:

- `adopt`: safe and useful for MVP;
- `benchmark`: promising but must be tested on ScoutFlow corpus;
- `defer`: useful later but expands scope or budget;
- `reject`: violates privacy, overbuilds, stale, or install-hostile.

A refreshed evidence file that lists 30 links but makes no decisions is not enough. The point is to protect the single-user implementation from accidental infrastructure drift.

## 15. Refresh Questions That Matter Most

The top five questions are:

1. Which local bilingual embedding model gives best recall under the ≤2GB cache target?
2. Is sqlite-vec/vss easy enough on the user’s Apple Silicon Mac to justify replacing SQLite BLOB + NumPy?
3. Does Ollama have a suitable embedding model already installed locally?
4. Does Apple provide a local embedding API that is actually usable from this workflow?
5. Which pHash/dHash implementation is safe, small, and deterministic enough?

Answer these before debating secondary UI references.

## 16. Evidence Freshness Policy

For fast-moving tooling, evidence older than 90 days should be treated as stale unless it is official stable documentation. For stable concepts like BM25, pHash, and SQLite basics, older documentation may still be useful, but install/version details still need current verification. This distinction lets U6 use established algorithms without pretending every vendor detail is timeless.


## 17. Promotion Rule

This evidence file is the gatekeeper for external currency. A future implementation spec may cite tool choices only after this file has real access timestamps and decision rows. If live refresh cannot be performed, the safe implementation remains dependency-light: SQLite FTS5, SQLite BLOB embeddings if a local model is available, Pillow thumbnails, and deterministic perceptual hashes. Do not convert a candidate vendor list into authority.

## 18. Evidence Versus Inspiration

Prosumer DAM tools such as Eagle or Mylio can inspire grid layout, filtering, and metadata affordances, but they should not drive architecture. ScoutFlow needs a rebuildable local projection tied to U4/PF-V provenance. A polished external DAM app may be better for general photo libraries, but U6’s value is ScoutFlow-specific lineage, hash grouping, and search integration.


## 19. Live Refresh Acceptance Checklist

A completed refresh should answer all of the following in writing:

```yaml
sqlite_fts5_current_docs_checked: true
vector_extension_choice_explained: true
embedding_primary_license_checked: true
embedding_primary_dimensions_recorded: true
ollama_local_status_checked_on_user_mac: true
apple_foundation_models_status_checked: true
pHash_library_or_local_impl_chosen: true
spotlight_read_write_boundary_verified: true
prosumer_dam_references_labeled_inspiration_only: true
```

If any item remains false, keep the package as candidate and do not promote tool choices into authority.


## 20. Final Evidence Acceptance Sentence

The live-web pass is acceptable only when every adopted vendor choice has a current source, access date, local-only/privacy assessment, and explicit adopt/benchmark/defer/reject decision. Until then, the dependency-light architecture remains the safe candidate.


## 21. Extra Evidence Guard

When refresh is done, quote only primary or high-quality sources for adoption decisions. Blog posts and forum notes can explain risks, but official docs or model cards should anchor install, license, and API claims. Any unsupported claim must stay as `needs_verification`.


## 22. Final Freshness Guard

Fresh evidence must include access dates, observed versions, and a clear statement of whether the item changes the U6 recommendation.


## 23. Extra Verification Guard

A refreshed vendor row should distinguish official documentation, model card, release note, benchmark, and community commentary. Only official documentation or model cards should anchor adoption. Community commentary can highlight risks but cannot certify privacy or version facts.


Final note: unverifiable freshness remains a blocker.
