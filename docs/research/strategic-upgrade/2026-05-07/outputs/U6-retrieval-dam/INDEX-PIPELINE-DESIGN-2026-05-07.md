<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# INDEX PIPELINE DESIGN — 2026-05-07

> Claim label: candidate ≥95% for local indexing architecture, incremental rebuild, and error recovery.  
> Scope: file watcher + incremental index + full rebuild + recovery for both visual-DAM and hybrid-local-search.  
> Boundary: no production deployment, no ScoutFlow authority write, no cloud calls.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Design Principle

Both U6 modules are derived indexes. That single decision simplifies recovery: when the projection is corrupt, stale, or wrong, delete and rebuild. The pipeline should be boring and auditable, with explicit manifests and no silent authority mutation.

```text
source roots / CSV / repo docs / handoff files / images
  -> source manifest
  -> normalization/chunking or image metadata
  -> derived rows in staging DB
  -> validation and integrity checks
  -> atomic publish
```

The same pattern applies to `visual_dam.sqlite` and `search.sqlite`, but the adapters differ.

## 2. Source Adapters

### 2.1 Search adapters

| Adapter | Inputs | Output |
|---|---|---|
| repo docs | `docs/**/*.md`, contracts, PRD/SRD, current, task-index | normalized documents with authority labels |
| dispatch trail | `dispatches/Dispatch*.md`, run reports, checkpoint summaries | dispatch documents with task IDs and wave metadata |
| PR summaries | local PR export, git log summaries, merged PR metadata | PR documents with PR number, merge commit, changed files |
| memory/handoff | memory files and handoff packets | timestamped memory/handoff docs |
| source code | selected `services/api/**`, specs, schemas | code chunks with symbols/path |
| external reports | candidate/external review Markdown | report docs labeled not-authority/candidate |

### 2.2 visual-DAM adapters

| Adapter | Inputs | Output |
|---|---|---|
| PF-V CSV | 19-column `INDEX.csv` once available | asset rows with PF-V metadata JSON |
| U4 visual_asset | future/approved U4 source | stable asset IDs and generation metadata |
| artifact_assets | approved artifact file rows if present | asset candidates from existing ledger |
| manual local folder | explicitly configured image roots | manual asset rows, local-only |

Every adapter emits a `SourceRecord` with `source_id`, `kind`, `path`, `mtime`, `size`, `sha256`, `metadata`, and `discovered_at`. No adapter should open arbitrary paths outside configured roots.

## 3. Manifest Tables

Use manifest tables in each projection DB. They make incremental updates and audit easier.

```sql
CREATE TABLE IF NOT EXISTS index_runs (
    run_id TEXT PRIMARY KEY,
    module TEXT NOT NULL CHECK(module IN ('visual_dam','hybrid_search')),
    mode TEXT NOT NULL CHECK(mode IN ('incremental','full_rebuild','repair')),
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL CHECK(status IN ('running','ok','failed','aborted')),
    source_count INTEGER NOT NULL DEFAULT 0,
    changed_count INTEGER NOT NULL DEFAULT 0,
    error_count INTEGER NOT NULL DEFAULT 0,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS source_files (
    source_id TEXT PRIMARY KEY,
    adapter TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_path_sha256 TEXT NOT NULL,
    mtime_ns INTEGER,
    size_bytes INTEGER,
    sha256 TEXT,
    first_seen TEXT NOT NULL,
    last_seen TEXT NOT NULL,
    missing_at TEXT,
    last_indexed_run_id TEXT,
    metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS index_errors (
    error_id TEXT PRIMARY KEY,
    run_id TEXT NOT NULL,
    source_id TEXT,
    file_path TEXT,
    stage TEXT NOT NULL,
    error_code TEXT NOT NULL,
    message TEXT NOT NULL,
    created_at TEXT NOT NULL,
    resolved_at TEXT,
    metadata_json TEXT NOT NULL DEFAULT '{}'
);
```

For search, `source_files` links to `search_documents`. For DAM, it links to `visual_dam_index`. A source can disappear without deleting derived rows immediately; mark `missing_at` and let the UI show “missing original”.

## 4. Incremental Index Algorithm

```text
for each configured source root:
  enumerate files matching include/exclude policy
  stat file path, mtime, size
  compare with source_files
  if new or mtime/size changed:
      compute sha256
      if sha changed:
          queue reindex
      else:
          update last_seen only
  mark sources not observed in this run as missing
process queue in transactions
```

Search reindex transaction:

1. Parse metadata and body.
2. Chunk content.
3. Delete old chunks and embeddings for `doc_id`.
4. Insert new `search_documents` row.
5. Insert new `search_chunks` rows.
6. Rebuild FTS rows for the doc.
7. Queue embeddings for chunks.
8. Commit.

Visual reindex transaction:

1. Resolve path and validate containment.
2. Compute original sha256.
3. Open image safely.
4. Generate thumbnails to temp files under derived root.
5. Compute thumbnail sha and hashes.
6. Move thumbnails into final derived path atomically.
7. Upsert `visual_dam_index`, thumbnail variants, hash bands.
8. Commit.

If embedding generation fails, lexical chunks remain indexed. If thumbnail generation fails, the asset should appear in an error view but not break the whole scan.

## 5. Full Rebuild Algorithm

Full rebuild is safer as an atomic staging operation:

```text
create staging directory
create staging DB
scan all sources into staging DB
write thumbnails into staging thumb directory
run validation:
  PRAGMA integrity_check
  foreign key check if applicable
  row count sanity
  sample query sanity
  path containment sanity
if validation ok:
  rename current DB -> backup
  rename staging DB -> current
  rename staging thumbs -> current thumbs or merge by sha
else:
  keep current DB, retain failed staging logs
```

SQLite atomic rename is dependable on local filesystems when source and destination are on the same volume. Keep one or two backups:

```text
search.sqlite
search.sqlite.prev
visual_dam.sqlite
visual_dam.sqlite.prev
```

Do not delete old thumbnails aggressively. Thumbnails are cheap and useful for missing-original history. A separate `gc-thumbs --dry-run` can list unreferenced thumbnails, but deletion should be explicit.

## 6. File Watcher

A watcher is optional. Polling every few minutes is enough for single-user local-first. If implemented, use Python `watchdog` only after dependency approval. Watcher behavior:

- Debounce changes for 2-5 seconds.
- Coalesce multiple writes to the same file.
- Never index partial files still being written; wait until size/mtime is stable across two polls.
- Queue work; one writer thread/process at a time.
- If watcher crashes, the next manual incremental run catches up.

For U6, a simple command is better:

```bash
python -m u6_index incremental --since last_run
python -m u6_index rebuild --module search --atomic
python -m u6_index rebuild --module visual_dam --atomic
```

## 7. Exclude Policy

Default excludes are non-negotiable:

```yaml
exclude_globs:
  - "**/.git/**"
  - "**/.env*"
  - "**/BBDown.data"
  - "**/BBDownTV.data"
  - "**/qrcode.png"
  - "**/*cookie*"
  - "**/*token*"
  - "**/browser-profile/**"
  - "**/data/secrets/**"
  - "**/referencerepo/**"
  - "**/node_modules/**"
  - "**/__pycache__/**"
```

Search may index `referencerepo` only if a future local-only reference scan explicitly opts in, because reference repos can explode disk and pull in irrelevant code. DAM may index image folders only if their root is explicitly configured.

## 8. Error Recovery

Common failures and recovery:

| Failure | Detection | Recovery |
|---|---|---|
| corrupt SQLite DB | `PRAGMA integrity_check` fails | restore `.prev` or rebuild |
| embedding model changed | `embedding_version` mismatch | keep chunks, rebuild embeddings |
| source file moved | previous source not seen | mark missing; do not delete row immediately |
| original image corrupt | Pillow open fails | `index_errors`; no thumbnail update |
| thumbnail write interrupted | temp file remains | cleanup temp dir on next run |
| FTS row drift | FTS count mismatch | rebuild FTS from `search_chunks` |
| vector extension unavailable | import/load failure | fallback to BLOB + NumPy scan |
| Ollama unavailable | health check fails | lexical-only mode; mark embedding provider unavailable |
| path traversal request | containment check | deny request; log local error |
| web evidence stale | live_verified_at null or old | block “verified” label; keep candidate |

## 9. Observability

Local stdout should be truthful and compact:

```yaml
module: hybrid_search
run_id: 2026-05-07T101500Z
mode: incremental
source_seen: 92
changed: 14
chunks_written: 188
embeddings_written: 188
errors: 1
cloud_calls: 0
status: ok
```

For visual-DAM:

```yaml
module: visual_dam
run_id: 2026-05-07T101800Z
mode: incremental
assets_seen: 1048
assets_changed: 27
thumbnails_written: 27
near_duplicate_groups_changed: 9
errors: 2
original_files_modified: 0
spotlight_writes: 0
cloud_calls: 0
status: ok
```

The stdout contract should always include `cloud_calls: 0`, `original_files_modified: 0` for DAM, and `authority_writes: 0` for both modules.

## 10. Implementation Order

1. Search lexical-only index with FTS5 and chunking.
2. Search local embeddings provider wrapper and hybrid rerank.
3. Search replay metadata extraction.
4. visual-DAM scanner with sha/dimensions/thumbnail.
5. visual-DAM pHash/dHash/aHash and similarity query.
6. visual grid browser.
7. Atomic rebuild and recovery polish.
8. Benchmarks and self-audit.

This order gives value early: lexical search alone helps immediately; pHash grid helps visual browsing even before semantic image models.


## 11. Atomicity and Locking Detail

Single-user does not mean zero concurrency. The user can run a query while an index is rebuilding. The simplest safe pattern:

- Readers open the current DB read-only.
- Incremental writer uses one process lock file: `search.index.lock` or `visual_dam.index.lock`.
- Full rebuild writes a staging DB and never mutates the current DB until validation passes.
- Publish step is a rename/swap while no writer lock is held by another process.
- Query server should reopen DB connection when it detects DB inode/version changed.

Do not hold long write transactions while embedding hundreds of chunks. Insert chunks first, commit, then embed in batches and commit per batch. If embedding is interrupted, the lexical index remains valid and missing embeddings are visible.

## 12. Index Versioning

Both modules should carry an `index_version` and a `schema_version`.

```sql
CREATE TABLE IF NOT EXISTS projection_meta (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
```

Required keys:

```text
schema_version
index_algorithm_version
created_at
last_full_rebuild_at
active_embedding_model_key
visual_hash_algorithm_version
source_config_sha256
```

When `visual_hash_algorithm_version` changes, recompute hashes. When `source_config_sha256` changes, run a full source reconciliation because files may enter or leave scope. When only query weighting changes, no rebuild is needed.

## 13. Dry-run Mode

Every destructive-looking operation should have dry-run:

```bash
u6-search rebuild --dry-run
u6-dam gc-thumbs --dry-run
u6-dam scan --dry-run
```

Dry-run outputs counts and planned actions, not vague prose:

```yaml
would_index_new: 14
would_reindex_changed: 3
would_mark_missing: 2
would_write_thumbnails: 3
would_delete: 0
cloud_calls: 0
authority_writes: 0
```

The `would_delete` value should be zero for first release except explicit garbage-collection dry-runs. Even then, actual deletion should require a separate command.

## 14. Redaction Before Embedding

The search pipeline should run a redaction pre-pass before embedding text. Redaction does not need to destroy the displayed source document; it only changes `body_for_embedding` and `body_normalized`.

Patterns:

- cookie/token/password-like key-value pairs;
- QR/auth sidecar filenames;
- long bearer-like strings;
- local browser profile paths;
- signed URLs;
- `.env`-style secrets.

If a chunk is heavily redacted, add `metadata_json.redaction_density`. High density chunks can be excluded from embedding and retrieved lexically only. This aligns with ScoutFlow’s redaction discipline.

## 15. Pipeline Health Dashboard Without a Dashboard

A small `status` CLI is enough:

```bash
u6-status
```

Output:

```yaml
search:
  docs: 92
  chunks: 1260
  embeddings: 1260
  last_full_rebuild: 2026-05-07T10:00:00Z
  errors_open: 1
visual_dam:
  assets: 1048
  thumbnails: 1048
  duplicate_groups: 83
  missing_originals: 4
  errors_open: 2
privacy:
  cloud_calls_observed: 0
  authority_writes: 0
```

This gives the user operational confidence without building another console surface.


## 16. Deterministic IDs

Stable IDs make rebuilds comparable. Suggested formulas:

```text
search doc_id = sha256(kind + normalized_file_path + source_uri_or_empty)
search chunk_id = sha256(doc_id + chunk_index + start_line + end_line + chunk_body_sha256)
visual source_id = sha256(adapter + normalized_original_path)
visual asset_id = U4 asset_id if present else pfv row asset_id else sha256(csv_path + row_number + original_path)
```

Do not use random UUIDs for derived rows unless there is no other option. Random IDs make duplicate detection, benchmark comparison, and replay lineage harder.

## 17. Queue Table

If embeddings or thumbnails are asynchronous, use a small queue table rather than in-memory lists:

```sql
CREATE TABLE IF NOT EXISTS index_queue (
    queue_id TEXT PRIMARY KEY,
    module TEXT NOT NULL,
    work_kind TEXT NOT NULL,
    target_id TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('queued','running','ok','failed')),
    attempts INTEGER NOT NULL DEFAULT 0,
    not_before TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    error_code TEXT,
    error_message TEXT
);
```

This keeps recovery simple: after a crash, reset stale `running` rows to `queued` or `failed` based on age. For the first release, the queue can live in the projection DB and be processed by the CLI command that created it.

## 18. Integrity Checks

Validation before publish should include:

```text
PRAGMA integrity_check == ok
no thumbnail_path outside derived root
no source file path outside allowed roots
search_chunks count equals expected FTS count or FTS rebuild succeeds
all active embeddings have same dimensions/model_key
no unresolved high-severity redaction errors
no open path_policy errors for accepted rows
```

A rebuild that fails validation must not replace the current DB. The user should get a concise failure report and the old index should keep working.


## 19. Source Priority Ordering

When the same fact appears in multiple sources, the indexer should not deduplicate it away. Instead, it records all sources and lets ranking apply authority labels. Priority for “current truth” queries:

```text
user latest explicit instruction
> docs/current.md / task-index / decision-log
> PRD/SRD v2
> promoted addenda
> specs/contracts
> dispatch/handoff
> external reports
> archive/historical notes
```

This mirrors ScoutFlow’s authority-first posture. For historical questions, the query classifier can relax the priority and surface older dispatches.

## 20. Rebuild Frequency

Recommended cadence for a single user:

- manual incremental after a work session;
- full rebuild after schema/index algorithm change;
- full rebuild after adding a large new corpus root;
- embedding rebuild only when model/version/text format changes;
- thumbnail rebuild only when thumbnail size/hash algorithm changes.

Do not run heavy rebuilds automatically at startup. Startup should be fast and safe.


## 21. Manual Recovery Playbook

A user-facing recovery playbook should be short:

```bash
u6-status
u6-search rebuild --atomic
u6-dam rebuild --atomic
u6-search rebuild-fts
u6-search rebuild-embeddings --model active
```

If all else fails, delete the derived DB and rebuild from sources. Because U6 never writes authority or originals, destructive recovery is safe as long as it targets only the derived directory. The CLI should print the exact derived path before any cleanup command.


## 22. Config Snapshot

Each index run should store a redacted config snapshot hash and a small safe summary:

```yaml
source_roots_count: 4
exclude_globs_count: 12
embedding_provider: sentence_transformers
visual_thumbnail_sizes: [256, 1024]
config_sha256: <hash>
```

Do not store raw secrets or entire private paths when a hashed/summarized value is enough. The goal is reproducibility without creating another sensitive artifact.


## 23. Final Pipeline Acceptance Sentence

The pipeline is acceptable when interruption, corruption, missing files, model changes, and config changes all lead to visible recovery paths rather than silent stale search results.


## 24. Extra Recovery Guard

Every rebuild command should finish with a status line that states whether the previous index is still intact. This reassures the user that failed rebuilds do not destroy working search.


## 25. Final Queue Guard

Queued work must be restartable, inspectable, and safe to abandon.
