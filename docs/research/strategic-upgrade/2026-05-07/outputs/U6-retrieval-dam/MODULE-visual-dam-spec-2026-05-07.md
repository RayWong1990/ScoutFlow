<!--
U6 Retrieval & DAM Layer candidate package.
Status: candidate / not-authority.
Boundary: spec only; no service deployment; no production code write; no ScoutFlow authority write.
Live web note: this execution environment had web browsing disabled. External 2026 freshness is therefore marked as not live-verified.
-->

# MODULE — visual-DAM Spec — 2026-05-07

> Claim label: candidate ≥95% for ScoutFlow-local architecture and DAM algorithm shape; external library/version currency requires live-web refresh.  
> Scope: thumbnail + perceptual hash dedup + grid browser + EXIF-equivalent metadata.  
> Budget target: ≤800 LOC total, with Python core around 500 LOC and grid/browser around 300 LOC.  
> Authority posture: derived index only; does not mutate original images, ScoutFlow authority DB, PF-V CSV, Finder tags, Spotlight metadata, or xattrs.

## Source Basis / 读取依据

- U6 cloud prompt: visual-DAM + hybrid-local-search, single-user local SQLite, output ZIP with 9 files, candidate / not-authority, no production deployment, no cloud embedding, no Spotlight write. 引用标记：fileciteturn0file0
- PRD v2: ScoutFlow 是 single-user、local-first 的内容采集与证据整理系统；authority 由 SQLite + FS + state words 构成；不做 SaaS、多用户、浏览器自动化、平台互动、runtime 越权。引用标记：fileciteturn1file0
- SRD v2: 默认本机 127.0.0.1、SQLite + FS 双事实源；API 负责 validation/idempotency/state transition/receipt/trust trace；Worker 不直连 authority SQLite；当前不批准 BBDown/ffmpeg/ASR/frontend/runtime 扩张。引用标记：fileciteturn2file0
- Local audit pack: `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip`，已解包读取 repo docs、current、contracts、dispatch127-176、external reports、code refs。
- Execution-environment probe, not user's physical Mac: SQLite FTS5 available; Pillow installed; `sentence-transformers` not installed; `ollama` not found; `whisper` not found; FAISS/Chroma/LanceDB/DuckDB Python imports not found in this sandbox.


## 1. Mission

`visual-DAM` exists because PF-V / GPT-Image-2 image volume has crossed the point where Finder preview, `git log`, and ad-hoc filename memory no longer work. The service should answer three practical questions quickly:

1. **Where is this asset?** Show a durable local thumbnail, the source path, the PF-V/U4 metadata, and a safe detail view without moving the original.
2. **Have I already made something like this?** Use perceptual hashes to surface near duplicates, prompt reruns, resizes, and variants.
3. **Can I browse the batch visually?** Provide a local grid browser with filters by date, model, prompt cluster, campaign, status, format, dimensions, source run, and similarity bucket.

This is not an enterprise DAM, not a multi-user SaaS, not a replacement for `visual_asset`, and not an image generation workflow. It is a **rebuildable local projection** over assets already created by U4/PF-V or existing filesystem evidence. The design intentionally favors SQLite + thumbnails + pHash/dHash over ElasticSearch, S3, object stores, or remote vector APIs.

## 2. Boundary Contract

### 2.1 What the module may do

- Read the PF-V `INDEX.csv` and/or a future U4 `visual_asset` table through an explicitly approved read path.
- Read image bytes only to compute `sha256`, dimensions, format, EXIF-equivalent technical metadata, thumbnails, and perceptual hashes.
- Create derived files under a dedicated derived directory, for example `data/derived/visual-dam/thumbs/` or another local-only path approved later.
- Create and rebuild a separate projection DB, for example `data/derived/visual-dam/visual_dam.sqlite`.
- Serve a local read-only grid at `127.0.0.1:<port>` when explicitly run by the user.

### 2.2 What the module must never do

- Never move, rename, rewrite, optimize, compress, re-encode, or delete the original image.
- Never write macOS Spotlight metadata, Finder tags, xattrs, comments, or irreversible file metadata.
- Never upload image bytes, captions, prompts, metadata, embeddings, or hashes to a cloud service.
- Never treat `visual_dam_index` as authority. It is cache/projection; if deleted, it can be rebuilt from `visual_asset` + file bytes + PF-V CSV.
- Never bypass ScoutFlow authority rules. If future integration needs to register durable rows in ScoutFlow DB, it must go through an approved API/migration gate; this spec itself does not approve that gate.

## 3. Data Model

The primary table requested by U6 is `visual_dam_index`. Because this is a candidate derived DB, the FK to `visual_asset(asset_id)` is expressed as a **logical FK** unless U4 has already created that table in the same SQLite database. If U4 lives elsewhere, `asset_id` remains a stable join key and the rebuild process validates referential coverage separately.

```sql
-- ============================================================
-- CANDIDATE DDL — derived visual-DAM projection
-- NOT A MIGRATION. NOT EXECUTABLE AGAINST SCOUTFLOW AUTHORITY
-- unless a future dispatch approves integration.
-- ============================================================
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS visual_dam_index (
    asset_id TEXT PRIMARY KEY,
    source_kind TEXT NOT NULL CHECK (
        source_kind IN ('u4_visual_asset', 'pfv_index_csv', 'manual_import', 'artifact_asset')
    ),
    source_row_id TEXT,
    original_path TEXT NOT NULL,
    original_path_sha256 TEXT NOT NULL,
    original_sha256 TEXT NOT NULL,
    thumbnail_path TEXT NOT NULL,
    thumbnail_sha256 TEXT NOT NULL,
    phash_64 TEXT NOT NULL CHECK(length(phash_64) = 16),
    dhash_64 TEXT NOT NULL CHECK(length(dhash_64) = 16),
    ahash_64 TEXT NOT NULL CHECK(length(ahash_64) = 16),
    dimensions_width INTEGER NOT NULL CHECK(dimensions_width > 0),
    dimensions_height INTEGER NOT NULL CHECK(dimensions_height > 0),
    file_size_bytes INTEGER NOT NULL CHECK(file_size_bytes >= 0),
    format TEXT NOT NULL,
    color_mode TEXT,
    icc_profile_sha256 TEXT,
    exif_equivalent_json TEXT NOT NULL DEFAULT '{}',
    pfv_metadata_json TEXT NOT NULL DEFAULT '{}',
    model_name TEXT,
    prompt_cluster TEXT,
    run_id TEXT,
    created_at TEXT,
    indexed_at TEXT NOT NULL,
    last_seen TEXT NOT NULL,
    missing_at TEXT,
    index_version INTEGER NOT NULL DEFAULT 1,
    CHECK (missing_at IS NULL OR missing_at >= last_seen)
);

CREATE INDEX IF NOT EXISTS idx_visual_dam_created_at
    ON visual_dam_index(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_visual_dam_model_cluster
    ON visual_dam_index(model_name, prompt_cluster, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_visual_dam_sha
    ON visual_dam_index(original_sha256);

CREATE INDEX IF NOT EXISTS idx_visual_dam_phash_prefix
    ON visual_dam_index(substr(phash_64, 1, 4));

CREATE INDEX IF NOT EXISTS idx_visual_dam_last_seen
    ON visual_dam_index(last_seen DESC);
```

A second table records derived thumbnail variants. The core budget can skip it initially, but the spec includes it because retina thumbnails and detail thumbnails often need different sizes.

```sql
CREATE TABLE IF NOT EXISTS visual_dam_thumbnail_variant (
    asset_id TEXT NOT NULL,
    variant TEXT NOT NULL CHECK(variant IN ('grid_256', 'detail_1024', 'tiny_64')),
    thumbnail_path TEXT NOT NULL,
    width INTEGER NOT NULL,
    height INTEGER NOT NULL,
    sha256 TEXT NOT NULL,
    bytes INTEGER NOT NULL CHECK(bytes >= 0),
    created_at TEXT NOT NULL,
    PRIMARY KEY(asset_id, variant),
    FOREIGN KEY(asset_id) REFERENCES visual_dam_index(asset_id) ON DELETE CASCADE
);
```

For fast hamming-distance prefiltering without a vector extension, keep compact buckets. Each 64-bit hash is split into four 16-bit bands. Candidate lookup can retrieve rows sharing at least one band, then compute exact hamming distance in Python.

```sql
CREATE TABLE IF NOT EXISTS visual_dam_hash_band (
    hash_name TEXT NOT NULL CHECK(hash_name IN ('phash_64', 'dhash_64', 'ahash_64')),
    band INTEGER NOT NULL CHECK(band BETWEEN 0 AND 3),
    band_value TEXT NOT NULL CHECK(length(band_value) = 4),
    asset_id TEXT NOT NULL,
    PRIMARY KEY(hash_name, band, band_value, asset_id),
    FOREIGN KEY(asset_id) REFERENCES visual_dam_index(asset_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_visual_dam_hash_band_lookup
    ON visual_dam_hash_band(hash_name, band, band_value);
```

## 4. Ingestion Pipeline

The pipeline is intentionally small and deterministic:

```text
PF-V INDEX.csv / U4 visual_asset rows
  -> normalize metadata row
  -> resolve path with containment policy
  -> stat original file, compute sha256
  -> open with Pillow in safe mode
  -> read dimensions / mode / EXIF-equivalent technical facts
  -> generate thumbnails under derived root
  -> compute aHash/dHash/pHash 64-bit
  -> upsert visual_dam_index + thumbnail_variant + hash_band
  -> mark missing rows if previously indexed file disappeared
```

### 4.1 Path and containment policy

The scanner should accept configured roots, not arbitrary paths. A config file can define:

```yaml
visual_dam:
  source_roots:
    - /Users/wanglei/workspace/ScoutFlow/data/visual-assets
    - /Users/wanglei/workspace/raw/05-Projects/ScoutFlow/visual
  derived_root: /Users/wanglei/workspace/ScoutFlow/data/derived/visual-dam
  csv_sources:
    - /Users/wanglei/workspace/ScoutFlow/local/PF-V-INDEX.csv
  follow_symlinks: false
```

For each file, resolve `Path(path).expanduser().resolve(strict=True)` and reject any resolved path outside `source_roots`. Reject symlinks by default. This matters because a DAM indexer has broad read capability; it must not become a credential-file scanner.

### 4.2 Thumbnail generation

Use Pillow in the first implementation because it is already present in the execution sandbox and is enough for PNG/JPEG/WebP thumbnails. Sharp/WASM is not needed for ≤800 LOC. Suggested rules:

- `grid_256`: max 256px on the long edge, JPEG or WebP, neutral background for alpha images, output quality around 82.
- `detail_1024`: max 1024px long edge, only generate lazily when detail view opens or when the asset is selected.
- `tiny_64`: optional for fast placeholders.
- Preserve aspect ratio; never crop by default.
- Strip EXIF from thumbnails; thumbnails are derived display artifacts, not provenance evidence.
- Thumbnail path = `<derived_root>/thumbs/<sha256[0:2]>/<asset_id>-grid_256.jpg` to avoid one giant directory.

Failure handling should be boring: if Pillow cannot open an asset, insert or update a row in an `index_errors` table, leave the original untouched, and continue scanning.

### 4.3 EXIF-equivalent metadata

The prompt requests EXIF-equivalent metadata, not necessarily a full EXIF writer/reader. For generated images, useful metadata is often absent. Store a normalized JSON object with fields that are stable and safe:

```json
{
  "width": 1536,
  "height": 1024,
  "format": "PNG",
  "mode": "RGBA",
  "mtime": "2026-05-05T12:34:56Z",
  "file_size_bytes": 2382931,
  "icc_profile_sha256": "...",
  "has_alpha": true,
  "exif_present": false,
  "reader": "Pillow",
  "reader_version": "local"
}
```

Do not store raw EXIF blobs if they might contain device serials, GPS, usernames, or private filesystem paths. For PF-V generated assets, metadata from `INDEX.csv` is usually more valuable than EXIF. Keep the full PF-V row as `pfv_metadata_json` after redacting secrets and normalizing columns, and project common filters to scalar columns.

## 5. Perceptual Hash Strategy

The first release should compute three 64-bit hashes because each catches a different failure mode:

| Hash | Why keep it | Main use |
|---|---|---|
| `sha256` | exact bytes | exact duplicate and cache identity |
| `aHash_64` | simple average luminance | crude guard and sanity check |
| `dHash_64` | adjacent gradient | resize/quality variants; often robust for UI screenshots |
| `pHash_64` | DCT low-frequency structure | visual near-duplicate search; primary ranking signal |

The core similarity query should use pHash first, dHash second, and sha256 as a hard exact-match override. Hamming thresholds should be conservative at first:

| pHash distance | Label | Action |
|---:|---|---|
| 0 | exact perceptual duplicate | show as same-looking asset |
| 1-4 | near duplicate | group automatically but keep separate rows |
| 5-8 | strong visual sibling | show high in similar panel |
| 9-12 | possible sibling | show only when user asks for broad search |
| >12 | likely different | hide by default |

The displayed similarity score can be an explainable approximation:

```text
similarity = 100 * (1 - min(phash_distance, 16) / 16)
secondary_adjustment = -0.5 * dhash_distance if dhash_distance > phash_distance + 4
```

Avoid claiming “85% visual similarity” as a scientifically calibrated metric. In UI copy, say “hash similarity bucket” unless a future visual embedding model is approved.

### 5.1 Candidate SQL + Python query

```sql
-- Step 1: get candidate rows that share at least one 16-bit pHash band.
SELECT DISTINCT i.asset_id, i.thumbnail_path, i.phash_64, i.dhash_64, i.created_at,
       i.model_name, i.prompt_cluster
FROM visual_dam_hash_band AS b
JOIN visual_dam_index AS i ON i.asset_id = b.asset_id
WHERE b.hash_name = 'phash_64'
  AND (
      (b.band = 0 AND b.band_value = :band0) OR
      (b.band = 1 AND b.band_value = :band1) OR
      (b.band = 2 AND b.band_value = :band2) OR
      (b.band = 3 AND b.band_value = :band3)
  )
  AND i.asset_id != :asset_id
LIMIT 500;
```

Then Python computes exact hamming distance:

```python
def hamming_hex64(a: str, b: str) -> int:
    return (int(a, 16) ^ int(b, 16)).bit_count()
```

This avoids requiring sqlite-vss/FAISS for visual hash dedup. A future vector index is useful for CLIP-like semantic image search, but U6’s stated minimum is thumbnail + pHash/dedup/grid, so hash bands keep the first release simple.

## 6. Grid Browser

The grid browser should be a tiny local app, not a frontend project. Recommended implementation:

- Python `http.server` or FastAPI if ScoutFlow already has FastAPI in active environment.
- One static `index.html` with vanilla JS and CSS, ≤300 LOC.
- Endpoints are read-only:
  - `GET /api/assets?query=&model=&cluster=&from=&to=&missing=false&limit=100&offset=0`
  - `GET /api/assets/{asset_id}`
  - `GET /api/assets/{asset_id}/similar?max_distance=8`
  - `GET /thumbs/<relative_path>` with strict path containment.
- No drag/drop import in first release. Import is handled by indexer CLI over configured paths.
- No delete, rename, tag write, Finder metadata write, or original-file mutation.

The UI should optimize for “scan and decide”:

1. Left rail: filters for date, model, run, prompt cluster, format, dimensions, duplicate bucket, missing state.
2. Main grid: thumbnails with compact badges: model, date, pHash group count, dimensions.
3. Detail drawer: original path, safe metadata JSON, hash values, similar assets, copy-path buttons.
4. Similar strip: nearest 12 visual siblings with distance and source run.
5. Evidence warning: “derived index; original untouched; no cloud upload.”

Keyboard shortcuts matter more than polish: `/` focus search, arrow keys move, `s` open similar, `c` copy original path, `t` copy thumbnail path, `Esc` close drawer.

## 7. U4 visual_asset Integration

U4 is expected to own the conceptual asset identity. U6 should attach only derived DAM facts. The ideal join shape:

```sql
SELECT
  va.asset_id,
  va.prompt_id,
  va.generation_model,
  va.created_at AS generated_at,
  va.campaign,
  va.status,
  dam.thumbnail_path,
  dam.phash_64,
  dam.dhash_64,
  dam.dimensions_width,
  dam.dimensions_height,
  dam.file_size_bytes,
  dam.format
FROM visual_asset AS va
JOIN visual_dam_index AS dam ON dam.asset_id = va.asset_id
WHERE va.created_at >= datetime('now', '-30 days')
  AND va.generation_model LIKE '%GPT-Image-2%';
```

If U4 table is not yet present, the DAM indexer can generate stable `asset_id` from PF-V row identity, such as `pfv:<run_id>:<row_number>` or `sha256:<original_sha256>`. The safer long-term route is U4-controlled IDs; hash-derived IDs collapse distinct generated assets with identical bytes, which is convenient for dedup but not ideal for provenance.

## 8. Spotlight / Finder / macOS Metadata

The only approved behavior here is read-only inspection. The module may shell out to `mdls` or read existing xattrs if the user explicitly wants to see existing Finder/Spotlight facts, but it must not write tags, comments, or custom metadata. Candidate read-only fields:

- `kMDItemContentCreationDate`
- `kMDItemContentModificationDate`
- `kMDItemPixelWidth`
- `kMDItemPixelHeight`
- `kMDItemColorSpace`
- existing Finder tags, if available and safe

Implementation rule: Spotlight read failures are non-fatal. The DAM must work with pure filesystem + Pillow metadata, because generated assets may live in folders not indexed by Spotlight.

## 9. Error Recovery and Rebuild

The projection DB should be disposable. Recommended commands:

```bash
python -m visual_dam scan --config local.visual-dam.yaml
python -m visual_dam rebuild --config local.visual-dam.yaml --atomic
python -m visual_dam serve --db data/derived/visual-dam/visual_dam.sqlite --host 127.0.0.1
```

`rebuild --atomic` writes to `visual_dam.sqlite.tmp`, runs `PRAGMA integrity_check`, verifies thumbnail path containment, then swaps the DB file. If a rebuild fails, keep the old DB. For incremental scan, rows missing from the latest source scan are marked `missing_at` rather than deleted. This preserves dedup history while making missing originals visible.

## 10. Test Matrix

| Test | Expected |
|---|---|
| exact duplicate PNG | same sha256, same or near same pHash, grouped |
| resized JPEG variant | different sha256, pHash ≤8 in most normal cases |
| alpha PNG thumbnail | thumbnail has visible background, no crash |
| corrupt file | index_errors row; no pipeline abort |
| source path outside root | rejected before open |
| symlink to private path | rejected when `follow_symlinks=false` |
| missing previously indexed file | `missing_at` set, thumbnail retained |
| grid thumbnail route path traversal | 403/404, never reads outside derived root |
| Spotlight missing | no failure; field omitted |
| pHash query with 1000 assets | returns within interactive time on local SQLite |

## 11. LOC Budget

A realistic ≤800 LOC implementation:

| Component | LOC |
|---|---:|
| config + path policy | 60 |
| SQLite DDL + repository | 90 |
| PF-V/U4 source adapter | 70 |
| image metadata + thumbnail + hashes | 150 |
| scan/rebuild CLI | 80 |
| similarity query | 55 |
| local HTTP API | 80 |
| `index.html` + CSS + JS | 240 |
| tests/smoke helpers | outside core or 80 additional |

The module should ship as a spec-first sidecar. A later dispatch can approve code, migrations, or integration. This U6 package does not.


## 12. Implementation Pseudocode Appendix

The following pseudocode is included to remove ambiguity while still honoring the “spec only, no production code” boundary. It describes the intended shape, not an approved implementation.

```text
scan_visual_sources(config):
  run = start_index_run(module='visual_dam', mode='incremental')
  for source in configured_sources:
    for record in source.enumerate():
      try:
        resolved = resolve_within_roots(record.path, config.source_roots)
        stat = safe_stat(resolved)
        if source_file_unchanged(record.source_id, stat):
          mark_seen(record.source_id)
          continue
        original_sha = sha256_file(resolved)
        image = pillow_open(resolved)
        metadata = read_safe_image_metadata(image, stat)
        hashes = compute_hashes(image)
        thumb_tmp = render_thumbnail_tmp(image, size=256)
        thumb_final = move_thumbnail_by_asset_id(thumb_tmp, record.asset_id)
        upsert_visual_dam_row(record, metadata, hashes, thumb_final)
        upsert_hash_bands(record.asset_id, hashes)
      except PathRejected as e:
        record_index_error(run, record, 'path_policy', e)
      except ImageOpenError as e:
        record_index_error(run, record, 'image_decode', e)
      except Exception as e:
        record_index_error(run, record, 'unknown', e)
  mark_missing_sources_not_seen(run)
  finish_run(run)
```

The important part is transaction shape. Thumbnail temp writes happen before the SQLite commit, but the final row should not point to a thumbnail until the file is fully written and hash-verified. If the DB commit fails after thumbnail creation, the next cleanup pass can delete unreferenced temp files. If thumbnail creation fails, the DB should not pretend the asset is browseable.

## 13. PF-V INDEX.csv Handling

The prompt says PF-V `INDEX.csv` has 19 columns, but the actual schema was not present in the supplied files. The adapter should therefore be schema-tolerant:

- Require only one stable identity column or derive a temporary row key from `(csv_path, row_number, original_path)`.
- Require one file path column; if multiple candidate columns exist, use explicit config.
- Treat prompt/model/run/date/status/campaign columns as optional projections.
- Store the entire redacted row in `pfv_metadata_json` so no information is lost.
- Emit a schema report on first run:

```yaml
pfv_index_schema_detected:
  columns_count: 19
  path_column: image_path
  id_column: asset_id
  optional_columns_detected: [model, prompt, run_id, created_at, status]
  unmapped_columns: [...]
  rows_seen: 1048
```

This avoids overfitting the spec to an unknown CSV shape. If the user later provides the real PF-V CSV, U6 can lock a stricter adapter.

## 14. Visual Dedup Product Semantics

Dedup should not erase provenance. Two assets may be visually identical but still meaningful as separate generations: different prompt versions, different run IDs, different downstream decisions, or different campaign contexts. Therefore the UI should group duplicates but never merge rows by default.

Recommended group labels:

| Label | Definition | UI behavior |
|---|---|---|
| exact bytes | same `original_sha256` | show collapsed group with exact badge |
| same-looking | pHash distance 0 and dHash close | show as likely same visual |
| near duplicate | pHash 1-4 | show together; keep run metadata visible |
| visual sibling | pHash 5-8 | show under “similar” but do not collapse |
| possible sibling | pHash 9-12 | hidden unless broad search is selected |

The grouping algorithm can be union-find over pairwise near-duplicate links. The group ID should be derived, not authority: `group:<min_asset_id>:<hash_version>`. If thresholds change, groups can change. That is acceptable because groups are a view, not truth.

## 15. Grid Browser Acceptance Walkthrough

A useful manual test session:

1. Start server bound to `127.0.0.1` and open the grid.
2. Filter to last 30 days and `model_name contains GPT-Image-2`.
3. Select a known mockup asset.
4. Press `s` to show similar images.
5. Confirm pHash/dHash distances are visible, not hidden behind a vague “AI similarity” label.
6. Copy original path and thumbnail path.
7. Open a missing-original row and verify warning copy is clear.
8. Try a path traversal thumbnail URL and verify it does not read outside derived root.
9. Quit server and verify no original file mtime changed.
10. Run incremental scan again and verify unchanged assets are skipped.

A pass means the user can answer “where is it?” and “have I made something like this?” in minutes instead of rummaging through Finder.


## 16. Threat Model

The DAM scanner is a privileged local reader. Even though it does not write originals, it can accidentally expose private files if path policy is weak. Threats and mitigations:

| Threat | Example | Mitigation |
|---|---|---|
| path escape | CSV path points to `~/.ssh/id_rsa` | configured source roots + extension/type checks + image decode requirement |
| symlink escape | image folder contains symlink to secrets | reject symlinks by default, resolve paths before open |
| thumbnail route traversal | `/thumbs/../../private` | serve only DB-known thumbnail relative paths under derived root |
| metadata leakage | EXIF GPS/user paths in JSON | store safe normalized metadata, not raw EXIF blobs |
| accidental mutation | thumbnail writer overwrites original | derived root separate from source roots; temp files only under derived root |
| duplicate merge loss | exact-looking images merged | group only, never delete/merge provenance rows |
| stale hash algorithm | thresholds change silently | `visual_hash_algorithm_version` stored in meta table |

A later semantic-image embedding extension would expand the threat model because prompts/images might be embedded by a larger local model. That is explicitly deferred.

## 17. Future Extension: Semantic Visual Search

The MVP deliberately stops at pHash/dHash/aHash. A future U6.2 could add local CLIP/SigLIP-style image-text embeddings to answer “show images with dense dashboard feel” or “find mockups with left rail and timeline.” That extension should use a separate table:

```sql
CREATE TABLE IF NOT EXISTS visual_semantic_embeddings (
    asset_id TEXT PRIMARY KEY,
    provider TEXT NOT NULL,
    model_name TEXT NOT NULL,
    dimensions INTEGER NOT NULL,
    embedding_blob BLOB NOT NULL,
    embedded_at TEXT NOT NULL,
    FOREIGN KEY(asset_id) REFERENCES visual_dam_index(asset_id) ON DELETE CASCADE
);
```

It should not replace pHash. pHash answers duplicate/variant questions with deterministic, explainable distances. Semantic image embeddings answer conceptual visual queries, which are useful but less auditable and more expensive. Keeping them separate lets U6 remain small and trusted.


## 18. Minimum Configuration Contract

A future implementation should refuse to run without an explicit config. Defaults can suggest paths, but the user must decide source roots and derived root. Required keys: `source_roots`, `derived_root`, `db_path`, `thumbnail_sizes`, `allowed_extensions`, and `follow_symlinks=false`. This prevents the DAM from becoming a whole-home-folder crawler. The config hash should be stored in `projection_meta` so a later reviewer can tell which roots produced the index.


## 19. Final DAM Non-negotiables

The minimum viable DAM passes only if all non-negotiables remain true: original files unchanged, thumbnails derived, hashes explainable, paths contained, metadata redacted, grid local-only, and duplicate grouping reversible.
