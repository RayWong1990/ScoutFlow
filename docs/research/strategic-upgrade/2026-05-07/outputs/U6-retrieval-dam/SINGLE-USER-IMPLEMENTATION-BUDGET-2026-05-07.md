<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# SINGLE-USER IMPLEMENTATION BUDGET — 2026-05-07

> Claim label: candidate ≥95% for budget arithmetic and implementation sequencing; exact model/disk numbers require local benchmark.  
> Scope: ≤1300 LOC, ≤1.5 weeks, model cache ≤2GB, SQLite DB ≤500MB, local-only privacy.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Budget Summary

U6 should be small enough that one person can build and maintain it. The target is not a platform; it is a local utility layer that makes ScoutFlow usable after hundreds of PRs and thousands of visual assets.

```yaml
single_user_budget_loc: 1300
visual_dam_loc_target: 800
hybrid_search_loc_target: 500
single_user_budget_dev_days: 7.5
model_cache_target_mb: 2048
sqlite_db_target_mb: 500
cloud_calls_allowed: 0
original_image_mutations_allowed: 0
authority_writes_allowed_by_this_spec: 0
```

## 2. LOC Breakdown

### 2.1 visual-DAM ≤800 LOC

| Area | LOC target | Notes |
|---|---:|---|
| config/path containment | 60 | roots, derived paths, symlink policy |
| SQLite repository/DDL | 90 | upserts, hash bands, error table |
| PF-V/U4 adapter | 70 | CSV and logical `visual_asset` source |
| image metadata + thumbnail | 120 | Pillow open, dimensions, thumbnails |
| pHash/dHash/aHash | 80 | can use small local implementation or dependency if approved |
| scanner/rebuild CLI | 90 | incremental and full rebuild |
| similarity query | 55 | band prefilter + hamming rerank |
| local HTTP API | 75 | assets/detail/similar/thumb routes |
| grid HTML/CSS/JS | 240 | vanilla single page |
| Total | 830 | trim by merging CLI/API helpers to hit 800 |

A strict 800 LOC cut can defer detail thumbnails or use CLI-only first. The highest-value MVP is thumbnails + hash + grid.

### 2.2 hybrid-local-search ≤500 LOC

| Area | LOC target | Notes |
|---|---:|---|
| config/source globbing | 45 | include/exclude roots |
| metadata extraction | 60 | task/PR/dispatch/date labels |
| Markdown/code chunking | 80 | heading-aware, line ranges |
| SQLite/FTS repository | 105 | DDL, content updates |
| embedding provider wrapper | 70 | ST/Ollama/local fallback |
| hybrid query/rerank | 80 | BM25 + cosine + metadata boost |
| CLI | 40 | index/query/rebuild |
| tests/smoke | outside target or 50 | can live separately |
| Total | 480 | leaves 20 LOC buffer |

The search MVP should be CLI-first. A UI is not required to make retrieval useful.

## 3. Schedule

A realistic 7.5 development-day plan:

| Day | Work |
|---:|---|
| 0.5 | live web refresh, local dependency probe, PF-V CSV schema confirmation |
| 1 | search lexical index: source adapters, chunking, FTS5, query CLI |
| 1 | search embeddings: provider wrapper, local model install/probe, hybrid rerank |
| 0.75 | search benchmark: 40 known-answer queries, authority ranking fixes |
| 1 | visual-DAM scanner: path policy, image metadata, thumbnails |
| 1 | visual hashes: pHash/dHash/aHash, band table, similar query |
| 1 | grid browser: assets API, thumbnail route, detail/similar panel |
| 0.75 | rebuild/recovery: atomic DB swap, error tables, stdout contracts |
| 0.5 | README, self-audit, local-only privacy check |

If live web or model install stalls, ship lexical-only search and thumbnail+pHash DAM first, then add embeddings after.

## 4. Disk Budget

Approximate disk use for first release:

| Item | Estimate |
|---|---:|
| search DB chunks + FTS | 50-150 MB |
| search embeddings | 50-250 MB depending on model/chunk count |
| visual DAM DB | 5-30 MB |
| thumbnails for 1000 images | 50-200 MB |
| model cache | 300-2048 MB |
| logs/backups | 50-200 MB |
| total target excluding original assets | ≤2.8 GB with model; ≤500 MB SQLite DB |

The prompt separately asks SQLite DB ≤500MB and model cache ≤2GB. That is plausible if chunk count is controlled and embeddings are not duplicated across models. Keep one active embedding model at a time; benchmark alternatives in short runs and delete unused cache only with user approval.

## 5. Performance Budget

| Operation | Target |
|---|---:|
| FTS query | <300ms on local corpus |
| hybrid query with brute-force 20k embeddings | <1-3s depending model/vector count |
| query embedding | interactive; provider-dependent |
| incremental reindex unchanged docs | seconds |
| full search rebuild | minutes, acceptable offline |
| thumbnail incremental for 100 changed images | minutes or less |
| pHash similar query | <500ms after band prefilter |
| grid first paint | <1s with pagination |

Latency should degrade gracefully. If embeddings are unavailable, lexical results still work. If thumbnails are missing, show metadata rows and error badges.

## 6. Maintenance Budget

The owner should not need to babysit a service. Design choices that reduce maintenance:

- derived DBs can be deleted and rebuilt;
- one config file per module;
- no daemon required for MVP;
- no cloud API keys;
- no schema migration in ScoutFlow authority DB;
- no original file write permissions;
- explicit stdout contracts;
- small benchmark set for regression checks;
- dependency-minimal implementation.

Avoid hidden complexity: Chroma/LanceDB/DuckDB may be excellent tools, but each adds state, upgrade, and backup semantics. U6 should not adopt them until the simple SQLite path fails a measured benchmark.

## 7. Acceptance Criteria

Search acceptance:

```text
- Indexes PRD/SRD/current/task-index/dispatch pack/external reports/code refs.
- Returns exact task/PR IDs in top results.
- Answers authority-boundary questions with current/contract above candidate docs.
- Embedding provider local-only or lexical-only fallback.
- No cloud request.
- Rebuildable from source files.
```

DAM acceptance:

```text
- Scans configured image roots or PF-V CSV.
- Generates thumbnails under derived root.
- Computes sha256 + pHash + dHash + aHash.
- Shows grid and detail view locally.
- Similar query returns expected near duplicates.
- Does not modify originals.
- Does not write Spotlight/xattr/Finder metadata.
```

Budget acceptance:

```text
- core LOC <= 1300 or explicit deferral list explains overage.
- model cache <= 2GB unless user approves exception.
- SQLite DB <= 500MB for initial corpus.
- dev time <= 1.5 weeks for MVP.
```

## 8. Defer List

To protect the budget, defer:

- semantic image embeddings / CLIP search;
- React app or elaborate frontend;
- vector DB beyond SQLite/FAISS fallback;
- macOS Spotlight writer/importer;
- automatic tagging;
- multi-user sharing;
- cloud embedding;
- background daemon with complex lifecycle;
- ScoutFlow authority migration.

The strongest U6 MVP is not the most feature-rich version. It is the one the user can run, rebuild, trust, and maintain alone.


## 9. Cost of Overbuilding

The main budget risk is not one hard function; it is adopting infrastructure that creates a second project. Examples:

| Temptation | Hidden cost | U6 answer |
|---|---|---|
| full React DAM app | frontend build, styling, state, tests | vanilla grid first |
| hosted vector DB | privacy and service lifecycle | local SQLite/NumPy first |
| multiple embedding models | duplicate DB/model cache | one active model |
| CLIP visual search | model cache and benchmark | defer; pHash first |
| Finder tag writer | irreversible local metadata writes | read-only only |
| daemon watcher | lifecycle/debug complexity | manual incremental first |
| ScoutFlow migration | authority risk and review cost | derived DB only |

A small tool that runs reliably beats a perfect system that the user hesitates to start.

## 10. First-Week Definition of Done

A credible first-week demo:

```text
Search:
  - index current, PRD/SRD, task-index, dispatch127-176, reports
  - answer 10 known queries with line/path evidence
  - local-only lexical or hybrid mode
DAM:
  - index at least one configured visual folder or PF-V CSV sample
  - show thumbnail grid
  - show similar assets by pHash
  - prove original mtimes unchanged
Ops:
  - rebuild command works
  - status command works
  - no cloud call, no authority write
```

This definition of done is intentionally modest and valuable. It directly addresses the user’s reported pain: grep/Finder collapse at scale.


## 11. Cut Lines If Budget Slips

Cut in this order:

1. Defer detail thumbnails; keep grid thumbnails.
2. Defer local HTTP API for search; keep CLI query.
3. Defer watcher; keep manual incremental scan.
4. Defer sqlite-vec/vss; keep SQLite BLOB + NumPy.
5. Defer semantic image embeddings; keep pHash/dHash.
6. Defer fancy grid filters; keep date/model/search/similar.
7. Defer multiple embedding candidates; benchmark one primary and one fallback only.

Do not cut privacy, authority labels, path containment, original-image no-write, or cloud-call prohibition. Those are not features; they are safety requirements.


## 12. Budget Red Flag

If the implementation requires Docker, a hosted service, a database server, a React build chain, more than one active embedding model, or a ScoutFlow authority migration, it has drifted beyond U6 MVP. Stop and re-scope before writing code.


## 13. Budget Pass Rule

If the MVP cannot be explained on one page, it is too large. The first release is search index, local embeddings optional, thumbnails, pHash similarity, grid, rebuild, status.


## 14. Final Budget Note

The MVP should be easy to stop, easy to rebuild, and easy to delete.
