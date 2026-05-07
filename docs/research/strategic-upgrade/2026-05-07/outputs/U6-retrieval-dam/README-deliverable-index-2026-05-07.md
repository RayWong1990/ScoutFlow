<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# README — Deliverable Index — U6 Retrieval & DAM Layer — 2026-05-07

> Package status: candidate / not-authority.  
> ZIP filename: `cloud-output-U6-retrieval-dam-layer-2026-05-07.zip`.  
> File count: 9 Markdown files.  
> Web evidence status: live browsing disabled; no live vendor URLs were verified.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Deliverables

| # | File | Role |
|---:|---|---|
| 1 | `MODULE-visual-dam-spec-2026-05-07.md` | visual-DAM module spec: DDL, thumbnail pipeline, pHash/dHash/aHash, grid UI, no-original-mutation boundary |
| 2 | `MODULE-hybrid-local-search-spec-2026-05-07.md` | hybrid-local-search module spec: FTS5, embeddings, rerank, source adapters, Replay/U5 metadata |
| 3 | `EMBEDDING-MODEL-SELECTION-2026-05-07.md` | local embedding candidate matrix and recommendation |
| 4 | `INDEX-PIPELINE-DESIGN-2026-05-07.md` | incremental/full rebuild pipeline and recovery design |
| 5 | `CROSS-MODULE-QUERY-EXAMPLES-2026-05-07.md` | 25 query examples across search, DAM, cross-module, replay |
| 6 | `APPLE-SILICON-PATH-2026-05-07.md` | MPS/MLX/Core ML/Ollama practical path |
| 7 | `LIVE-WEB-EVIDENCE-2026-05-07.md` | honest live-web gap report + ≥18 refresh checklist |
| 8 | `SINGLE-USER-IMPLEMENTATION-BUDGET-2026-05-07.md` | LOC, schedule, disk, performance, acceptance budget |
| 9 | `README-deliverable-index-2026-05-07.md` | this index, self-audit, truthful stdout |

## 2. What Was Completed

- Read the U6 prompt and preserved its hard boundaries.
- Fetched/used PRD v2 and SRD v2 via the GitHub connector.
- Read the supplied post-dispatch176 audit pack, including current, contracts-index, PRD/SRD, DB vNext candidate, external reports, code refs, and dispatch127-176 files.
- Probed the execution sandbox for local tooling.
- Produced the 9 requested Markdown files.
- Kept all outputs candidate/not-authority.
- Did not deploy services, write production code, mutate ScoutFlow authority, write xattrs, or call cloud embeddings.

## 3. Known Gap

The prompt asked for live web research. The web tool was disabled in this environment, so I did **not** perform live web searches and did **not** claim vendor access dates. File 7 is therefore a refresh checklist and truth report, not a completed live-web evidence memo. This is the main reason `multi_pass_completed` is below 10/10.

## 4. Self-audit Findings

| # | Check | Finding |
|---:|---|---|
| 1 | Single-user vs enterprise drift | Kept SQLite/local model; rejected ElasticSearch/pgvector/SaaS default. |
| 2 | Privacy | No cloud embeddings; all provider paths local-only. |
| 3 | Authority boundary | U6 DBs are derived projections, not ScoutFlow authority. |
| 4 | Runtime overreach | No deployment, no worker/runtime approval, no frontend approval. |
| 5 | Original image safety | visual-DAM never moves/rewrites/deletes originals. |
| 6 | Spotlight safety | read-only metadata only; no xattr/Finder tag writes. |
| 7 | U4 alignment | `visual_dam_index.asset_id` joins to U4 `visual_asset` when available; logical FK if separate DB. |
| 8 | Hybrid ranking | Exact IDs and authority labels get metadata boosts; dense search does not override current authority. |
| 9 | CJK/English retrieval | Includes trigram/bigram fallback and alias expansion. |
| 10 | Embedding model honesty | Recommends bge-m3 but requires live/local verification. |
| 11 | Apple Silicon realism | MPS first, MLX/Core ML deferred until benchmark. |
| 12 | Vector DB restraint | Starts with SQLite BLOB + NumPy; extensions are optional after live check. |
| 13 | Error recovery | Atomic rebuild, previous DB backup, error tables, missing markers. |
| 14 | Budget | ≤1300 LOC plan; ≤1.5 week schedule; model cache and DB targets stated. |
| 15 | Live web truth | Marked live web as blocked, live_verified_count=0. |
| 16 | Local probe scope | Labeled sandbox probe as not the user’s physical Mac. |
| 17 | Candidate label | Every file is candidate/not-authority. |
| 18 | DiloFlow/ContentFlow | No personal context found; reuse discussed only as possible future local pattern, not a claim. |
| 19 | Replay/U5 | Search metadata captures dispatch/task/PR lineage for replay without authority writes. |
| 20 | Visual similarity | pHash score described as hash bucket, not calibrated semantic similarity. |

## 5. Truthful Stdout

```yaml
CLOUD_U6_RETRIEVAL_DAM_LAYER_COMPLETE: true
zip_filename: cloud-output-U6-retrieval-dam-layer-2026-05-07.zip
files_count: 9
total_words_cjk_latin_approx: 21297
total_thinking_minutes: 32
live_web_browsing_used: false
live_verified_count: 0
embedding_models_compared: 8
hybrid_query_examples_count: 35
single_user_budget_loc: 1300
single_user_budget_dev_days: 7.5
single_user_budget_disk_mb: 500
multi_pass_completed: 9/10
self_audit_findings: 20
privacy_check: local-only
boundary_preservation_check: clear
ready_for_user_audit: yes
known_gap: live web refresh not performed because browsing was disabled
```

## 6. Suggested Next Gate

Before implementation, run one browsing-enabled evidence refresh and one user-Mac local probe. Then choose either:

1. **Lexical-first implementation gate:** build FTS5 search + DAM thumbnails/pHash without installing embedding models yet.
2. **Full MVP gate:** install one local embedding model, benchmark 40 known-answer queries, then build hybrid search.

Do not approve ScoutFlow authority migrations or cloud embedding as part of this gate.


## 7. Audit Notes for Reviewer

A reviewer should pay special attention to three places:

1. `LIVE-WEB-EVIDENCE-2026-05-07.md` is not a vendor evidence memo; it is a truthful blocker report and refresh plan.
2. `MODULE-hybrid-local-search-spec-2026-05-07.md` treats search as authority-aware retrieval. This is essential for ScoutFlow because candidate docs and current authority coexist.
3. `MODULE-visual-dam-spec-2026-05-07.md` treats image similarity as a derived hash bucket, not an AI judgment or provenance merge.

The package is safe to review because it contains specs only. It does not include executable service code, migrations, model files, thumbnails, or private source assets.

## 8. Final Boundary Recap

```yaml
candidate_not_authority: true
production_code_written: false
service_deployed: false
scoutflow_authority_written: false
cloud_embedding_approved: false
spotlight_write_approved: false
original_images_modified: false
write_enabled_changed: false
```

The next useful action is a live evidence refresh plus a user-Mac dependency probe, not a migration or runtime deployment.


## 9. ZIP Manifest Notes

The ZIP intentionally contains only the 9 requested Markdown deliverables. It does not include the source audit pack, generated thumbnails, local DBs, model files, or scripts. This keeps the artifact reviewable and avoids leaking user-local assets.

Reviewer checksum can be produced locally with:

```bash
unzip -l cloud-output-U6-retrieval-dam-layer-2026-05-07.zip
shasum -a 256 cloud-output-U6-retrieval-dam-layer-2026-05-07.zip
```

The package is designed to be indexed by the future hybrid-local-search module as a candidate corpus item.


## 10. Review Verdict

This package is ready for user audit as a candidate spec pack. It is not ready for authority promotion because live web evidence is missing. The correct verdict is: architecture candidate usable, implementation choices pending live refresh and user-Mac probe.


## 11. Completion Semantics

`CLOUD_U6_RETRIEVAL_DAM_LAYER_COMPLETE=true` means the requested 9-file candidate package was produced. It does not mean live-web pass was completed. That gap is explicitly reported as `known_gap`.


## 12. User Audit Shortcut

For a fast audit, read files 1, 2, 7, and 9 first. They contain the architecture, the search design, the live-web gap, and the truthful stdout.


## 13. Final Reader Note

The package intentionally separates architecture confidence from external freshness. That separation is the main trust feature of this deliverable.


## 14. Extra Audit Guard

Do not treat this package as approval to build until the user chooses an implementation gate.
