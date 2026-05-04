# SRD-v3 Candidate Amendment - DB VNext

---
status: amendment / candidate-for-SRD-v3-promote
task_id: T-P1A-026
authority_base: docs/SRD-v2-2026-05-04.md
based_on_main_commit: df2f0183c2302e23116379b74b882980dd8460ba
research_inputs:
  - docs/research/t-p1a-025-db-ledger-vnext.md
  - docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md
  - docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md
  - docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md
promote_target: SRD-v3
revalidate_before_promote: true
not_runtime_approval: true
not_migration_approval: true
---

> Status: **candidate / draft**. This amendment is a shape-only SRD-v3 candidate.
> It is not a migration script, not runtime approval, and not a promotion of
> `docs/SRD-v2-2026-05-04.md`.

## 0. Boundary

This amendment defines the DB vNext target shape for the ScoutFlow evidence
chain before Phase 2A migration work begins.

Allowed in this amendment:

- target schema shape
- identity-level invariants
- migration principles
- supersession semantics
- purge defaults
- explicit deferred decisions

Not allowed in this amendment:

- migration step order
- transaction choreography
- rollback scripts
- `INSERT`/backfill statements
- product code changes
- `services/api/migrations/**` edits
- runtime approval
- edits to frozen research inputs
- edits to `docs/SRD-v2-2026-05-04.md`

## 0.1 Diff Summary v2 -> v3

| Table | Status | Key change |
|---|---|---|
| `captures` | `carried over with a specific change` | downstream evidence-chain FKs must be explicit `ON DELETE RESTRICT`; state vocabulary remains phase-bounded |
| `receipt_ledger` | `NEW in v3` | separates durable receipt identity from `job_events` append log |
| `artifact_assets` | `carried over with a specific change` | adds nullable `evidence_id` to bind file artifacts to evidence claims; delete semantics tightened |
| `evidence_ledger` | `NEW in v3` | materializes evidence-claim identity with `lineage_variant`, `receipt_id`, and `superseded_by` |
| `job_events` | `carried over with a specific change` | becomes self-contained inside the evidence chain via `capture_id` and optional `receipt_id` |

## 1. Supersession Boundary

Supersession is split across identity and flow.

Identity-level truth must be enforced in SQL. Flow-level behavior remains in
the app layer.

Within this amendment, `superseded_by IS NULL` is the physical representation
of "current", and non-`NULL` is the physical representation of "superseded".
That is a design statement about how state is encoded in rows; the SQL-owned
enforcement lives in the partial unique lineage rule below.

### 1.1 Enforced In SQL

The following invariants are contract-level and must be enforced by schema
shape:

| Invariant | SQL expression | Why it must be physical |
|---|---|---|
| one current row per logical lineage | partial `UNIQUE INDEX` on `(capture_id, evidence_kind, lineage_variant)` where `superseded_by IS NULL` | Trust Trace cannot guess between multiple current rows |
| superseded rows are never silently deleted | `ON DELETE RESTRICT` through the evidence chain | audit history must remain anchored |
| no default cascade or nulling delete behavior in evidence chain | explicit prohibition of `ON DELETE CASCADE` and `ON DELETE SET NULL` | protects against accidental chain collapse |

> Note: cross-lineage supersession defense relies on app write-path discipline,
> not SQL. Trigger-level enforcement is deferred to Phase 2A per §1.2 + §1.3.
> This is the honest cut under current SQLite capability, not a design
> compromise.

### 1.2 Enforced In App

The following remain app-layer or reporting-layer concerns:

| Concern | Owner | Why not SQL |
|---|---|---|
| supersession links must stay within the same logical lineage | orchestrator / write-path discipline (verifies `A.capture_id`, `evidence_kind`, and `lineage_variant` match `B` before setting `superseded_by`) | SQLite cannot enforce cross-row equality without a trigger; trigger-level enforcement is deferred per §1.3 to Phase 2A first implementation task |
| which current version Trust Trace shows first | storage / projection layer | display policy, not identity |
| supersession-triggered events or notifications | service / orchestration layer | procedural behavior |
| UI treatment of historical versions | reporting / UI | presentation concern |
| future cross-kind compatibility rules beyond current contract | app rule + future amendment | still evolving |

### 1.3 Deferred

- event emission policy for supersession
- historical-chain performance optimizations
- UI ordering of superseded rows

## 2. Purge / Deletion Boundary

Purge is identity-level at the default-policy layer and implementation-level at
the mechanism layer.

### 2.1 Abstract Purge Policy

1. Physical deletion from the evidence chain requires user-explicit
   confirmation and a dedicated purge path.
2. Deleting an upstream entity must not silently cascade through evidence,
   artifacts, receipts, or events.
3. Referenced evidence-chain rows reject deletion by default.
4. Purge activity itself must be audit-visible and must not disappear through
   ordinary delete paths.

### 2.2 SQL Defaults

The following defaults are part of this amendment's contract:

- no `ON DELETE CASCADE` anywhere in the evidence chain
- no `ON DELETE SET NULL` where nulling would erase audit meaning
- `ON DELETE RESTRICT` as the default identity-preserving behavior

Reverse rule:

> Any FK in the evidence chain (`captures` / `evidence_ledger` /
> `artifact_assets` / `receipt_ledger` / `job_events`) that uses
> `ON DELETE CASCADE` or `ON DELETE SET NULL` is a contract violation and
> requires a separate amendment plus external audit.

### 2.3 Deferred

- tombstone vs hard-delete-with-audit
- vacuum and space reclamation strategy
- maintenance flow (`manual` / API / cron)
- retention window policy
- concrete purge-op function signature
- purge audit-log schema

## 3. `lineage_variant` Contract

`lineage_variant` identifies evidence-layer claim variants, not artifact-layer
byte variants.

### 3.1 Meaning

Current uniqueness is defined by:

`(capture_id, evidence_kind, lineage_variant)` where `superseded_by IS NULL`

This preserves correct re-probe supersession while leaving one explicit axis
for multiple legitimate lineages.

### 3.2 Active SQL Vocabulary

The amendment activates these `lineage_variant` values in SQL:

- `auth_present`
- `dry_run`
- `pipeline_default`

### 3.3 Mapping

| `lineage_variant` | Source | Status |
|---|---|---|
| `auth_present` | T-P1A-011C / T-P1A-012 metadata probe evidence path | active |
| `dry_run` | T-P1A-019 dry-run orchestrator path when durable evidence is admitted | active but path-gated |
| `pipeline_default` | default lineage slot for Phase 2A transcript / normalization evidence kinds | active as target shape only |
| `no_auth_bounded` | future T-P1A-021A bounded live probe | reserved, not enabled in SQL |
| `manual_self_reported` | future manual evidence route | reserved, not enabled in SQL |

Adding a new active value requires an amendment update. Reserved values do not
enter the SQL `CHECK (...)` until separately approved.

### 3.4 What Does Not Belong In `lineage_variant`

The following dimensions are explicitly excluded:

| Dimension | Why excluded | Proper home |
|---|---|---|
| tool version | implementation metadata, not claim identity | `metadata_json` |
| timestamps | audit timeline, not lineage identity | receipt / event timestamps |
| trigger path or operator path | execution trace, not lineage identity | trace metadata |
| `sha256` / `file_path` | artifact identity, not evidence identity | `artifact_assets` |
| receipt row ids | accounting trace, not lineage identity | `receipt_ledger` |

## 4. Candidate DDL

> This section is **not** a migration script. Do **not** copy it directly into
> `services/api/migrations/`.
>
> It is a shape-only contract for SRD-v3 candidate review. Final SQL syntax
> tuning, migration order, transaction boundaries, backfill logic, and rollback
> behavior are deferred to Phase 2A implementation.

### 4.1 `captures` (carried over with a specific change)

Source: extends the Phase 1A `captures` table with explicit contract-level
checks for current bounded scope. The table remains the root of the evidence
chain.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- Table: captures
-- Status: carried over with a specific change
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
CREATE TABLE captures (
    capture_id TEXT PRIMARY KEY,
    platform TEXT NOT NULL CHECK (platform IN ('bilibili')),
    platform_item_id TEXT NOT NULL,
    canonical_url TEXT NOT NULL,
    source_kind TEXT NOT NULL CHECK (source_kind = 'manual_url'),
    capture_mode TEXT NOT NULL CHECK (capture_mode = 'metadata_only'),
    created_by_path TEXT NOT NULL CHECK (created_by_path = 'quick_capture'),
    status TEXT NOT NULL CHECK (
        status IN (
            'discovered',
            'metadata_fetched',
            'queued',
            'media_downloading',
            'media_ready',
            'audio_extracting',
            'audio_ready',
            'transcribing',
            'transcript_ready',
            'normalizing',
            'doc_ready',
            'indexing',
            'indexed',
            'linking',
            'linked',
            'archived',
            'superseded'
        )
    ),
    artifact_root_path TEXT NOT NULL,
    manifest_path TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(platform, platform_item_id)
);
```

### 4.2 `receipt_ledger` (NEW in v3)

Source: new in SRD-v3 candidate. This materializes durable receipt identity
without relying on `job_events.event_json` as the only long-term receipt
surface.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- Table: receipt_ledger
-- Status: NEW in v3
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
CREATE TABLE receipt_ledger (
    receipt_id TEXT PRIMARY KEY,
    capture_id TEXT NOT NULL
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    job_id TEXT NOT NULL,
    job_type TEXT NOT NULL,
    dedupe_key TEXT NOT NULL,
    producer TEXT NOT NULL,
    producer_version TEXT NOT NULL,
    engine TEXT,
    engine_version TEXT,
    platform_result TEXT NOT NULL,
    artifact_count INTEGER NOT NULL CHECK (artifact_count >= 0),
    duration_seconds REAL CHECK (duration_seconds IS NULL OR duration_seconds >= 0),
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, dedupe_key)
);
```

### 4.3 `artifact_assets` (carried over with a specific change)

Source: carries forward the current file ledger while binding artifacts to
logical evidence rows through nullable `evidence_id`.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- Table: artifact_assets
-- Status: carried over with a specific change
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
CREATE TABLE artifact_assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capture_id TEXT NOT NULL
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    evidence_id TEXT
        REFERENCES evidence_ledger(evidence_id) ON DELETE RESTRICT,
    artifact_zone TEXT NOT NULL CHECK (
        artifact_zone IN (
            'bundle',
            'media',
            'transcript',
            'normalized',
            'links',
            'logs'
        )
    ),
    artifact_kind TEXT NOT NULL,
    file_path TEXT NOT NULL,
    size_bytes INTEGER NOT NULL CHECK (size_bytes >= 0),
    sha256 TEXT NOT NULL,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(capture_id, file_path)
);
```

> Note: `artifact_assets.evidence_id` ↔
> `evidence_ledger.source_artifact_asset_id` is an intentional bidirectional
> reference, and both columns are nullable. Phase 2A implementation will need a
> 2-pass insertion pattern when both rows are created together: insert the
> artifact with `evidence_id NULL` first, then insert evidence referencing that
> artifact, then optionally back-fill `artifact_assets.evidence_id`.
> Transaction sequencing is deferred per §5.

### 4.4 `evidence_ledger` (NEW in v3)

Source: new in SRD-v3 candidate. This table materializes evidence-claim
identity separately from file storage and receipt accounting.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- Table: evidence_ledger
-- Status: NEW in v3
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
CREATE TABLE evidence_ledger (
    evidence_id TEXT PRIMARY KEY,
    capture_id TEXT NOT NULL
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    evidence_kind TEXT NOT NULL CHECK (
        evidence_kind IN (
            'metadata_probe',
            'transcript_segments',
            'normalized_summary',
            'normalized_claims',
            'normalized_quotes',
            'normalized_topic_candidates',
            'normalized_structured'
        )
    ),
    lineage_variant TEXT NOT NULL CHECK (
        lineage_variant IN (
            'auth_present',
            'dry_run',
            'pipeline_default'
        )
    ),
    source_artifact_asset_id INTEGER
        REFERENCES artifact_assets(id) ON DELETE RESTRICT,
    receipt_id TEXT
        REFERENCES receipt_ledger(receipt_id) ON DELETE RESTRICT,
    superseded_by TEXT
        REFERENCES evidence_ledger(evidence_id) ON DELETE RESTRICT,
    source_task_id TEXT,
    source_report_path TEXT,
    producer TEXT NOT NULL,
    producer_version TEXT NOT NULL,
    platform_result TEXT,
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    CHECK ((source_task_id IS NULL) = (source_report_path IS NULL)),
    CHECK (
        source_artifact_asset_id IS NOT NULL
        OR receipt_id IS NOT NULL
    )
);

CREATE UNIQUE INDEX idx_evidence_current_per_lineage
    ON evidence_ledger (capture_id, evidence_kind, lineage_variant)
    WHERE superseded_by IS NULL;
```

#### 4.4.1 `evidence_kind` Mapping

| `evidence_kind` | Primary frozen source | Why it exists now |
|---|---|---|
| `metadata_probe` | T-P1A-011C / T-P1A-012 | carries forward the proven metadata evidence lane already wired into receipts |
| `transcript_segments` | T-P1A-022 | captures the candidate ASR segment layer as future evidence input |
| `normalized_summary` | T-P1A-023 | summary layer proposed by normalization research; downstream consumer context also appears in T-P1A-024 |
| `normalized_claims` | T-P1A-023 | structured claim extraction candidate from normalization research |
| `normalized_quotes` | T-P1A-023 | quote extraction candidate from normalization research |
| `normalized_topic_candidates` | T-P1A-023 | topic candidate layer from normalization research; downstream Explore consumption context appears in T-P1A-024 |
| `normalized_structured` | T-P1A-023 | long-form structured synthesis candidate; review/consumption context also appears in T-P1A-024 |

Extending this vocabulary requires an amendment update.

### 4.5 `job_events` (carried over with a specific change)

Source: carries forward the append-only job event log while making the evidence
chain self-contained through `capture_id` and optional `receipt_id`.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- Table: job_events
-- Status: carried over with a specific change
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
CREATE TABLE job_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    capture_id TEXT NOT NULL
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    job_id TEXT NOT NULL,
    receipt_id TEXT
        REFERENCES receipt_ledger(receipt_id) ON DELETE RESTRICT,
    event_type TEXT NOT NULL,
    event_json TEXT NOT NULL,
    created_at TEXT NOT NULL
);
```

## 5. Deferred To Phase 2A First Implementation Task

The following decisions are intentionally **not** fixed in this amendment:

| Topic | Deferred to | Why deferred |
|---|---|---|
| query patterns and access paths | Phase 2A first implementation task | depends on final Explore shape and real caller behavior |
| index strategy beyond `idx_evidence_current_per_lineage` | Phase 2A first implementation task | requires `EXPLAIN` and real data shape |
| migration step sequence | Phase 2A first implementation task | execution-time concern, not target-state contract |
| transaction boundaries | Phase 2A first implementation task | depends on real SQLite migration mechanics |
| rollback / backfill behavior | Phase 2A first implementation task | procedural concern |
| tombstone vs hard-delete-with-audit | Phase 2A first implementation task | implementation-time purge mechanism |
| vacuum / space reclamation | Phase 2A ops task if needed | environment-dependent |
| maintenance flow | Phase 2A ops task if needed | deployment-dependent |
| backup / retention implementation | Phase 2A ops task if needed | solo-dev local-first and not migration-blocking |
| observability / metrics | defer indefinitely unless required | no current SLO surface |

## 6. Migration Principles

These principles are fixed now, even though migration sequence is deferred:

1. additive-first over destructive-first
2. no default physical deletion path in the evidence chain
3. no silent cascade or nulling delete semantics
4. preserve receipt and evidence lineage through migration
5. promote only after revalidating against the then-current `main`

## 7. How To Consume This Amendment

- Use this file as the sole SRD-v3 candidate target shape for DB vNext.
- Do not treat it as executable migration SQL.
- Before promotion, revalidate all `carried over` table shapes against the
  then-current `main`.
- When writing the first Phase 2A migration, adapt from this shape and the
  actual merged research inputs, not from stale PR URLs or historical branch
  diffs.

## 8. References

- [SRD-v2-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/SRD-v2-2026-05-04.md)
- [PRD-v2-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/PRD-v2-2026-05-04.md)
- [t-p1a-025-db-ledger-vnext.md](/Users/wanglei/workspace/ScoutFlow/docs/research/t-p1a-025-db-ledger-vnext.md)
- [t-p1a-022-asr-pipeline-prestudy-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md)
- [t-p1a-023-llm-normalization-schema-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/research/t-p1a-023-llm-normalization-schema-2026-05-04.md)
- [t-p1a-024-explore-capture-scope-state-table-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md)
- [db-vnext-design-2026-05-04.md](/Users/wanglei/workspace/ScoutFlow/docs/specs/db-vnext-design-2026-05-04.md)
- [001_phase1a_capture_creation.sql](/Users/wanglei/workspace/ScoutFlow/services/api/migrations/001_phase1a_capture_creation.sql)
- [002_phase1a_jobs_receipt.sql](/Users/wanglei/workspace/ScoutFlow/services/api/migrations/002_phase1a_jobs_receipt.sql)
