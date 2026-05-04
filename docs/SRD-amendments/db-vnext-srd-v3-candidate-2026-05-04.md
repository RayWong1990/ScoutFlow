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
| `captures` | `carried over with a specific change` | downstream evidence-chain FKs must be explicit `ON DELETE RESTRICT`; actual 17-value `captures.status` enum is admitted in SQL while reachability remains phase-bounded |
| `receipt_ledger` | `NEW in v3` | separates durable receipt identity from `job_events` append log; adds composite FK `(job_id, capture_id, job_type, dedupe_key) -> jobs(...)` to forbid cross-capture mismatch |
| `artifact_assets` | `carried over with a specific change` | adds nullable `evidence_id` to bind file artifacts to evidence claims; delete semantics tightened; adds composite FK `(evidence_id, capture_id) -> evidence_ledger(...)` to forbid cross-capture forward link (F-011) |
| `evidence_ledger` | `NEW in v3` | materializes evidence-claim identity with `lineage_variant`, `receipt_id`, and `superseded_by`; adds composite FKs `(receipt_id, capture_id) -> receipt_ledger(...)` and `(source_artifact_asset_id, capture_id) -> artifact_assets(id, capture_id)` to forbid cross-capture references (F-011) |
| `job_events` | `carried over with a specific change` | becomes self-contained inside the evidence chain via composite FK `(job_id, capture_id) -> jobs(job_id, capture_id)`; optional receipt link also binds on `(receipt_id, capture_id)`; no single-column orphan path |

> All FK rules in this table presume `PRAGMA foreign_keys=ON` per §1.5
> (F-012). Phase 2A migration must enable foreign-key enforcement before
> relying on these constraints.

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
| `superseded_by` must reference same `(capture_id, evidence_kind, lineage_variant)` and must not self-reference | SQLite triggers `trg_evidence_supersession_lineage_check_insert` (BEFORE INSERT) + `trg_evidence_supersession_lineage_check_update` (BEFORE UPDATE OF `superseded_by`) | cross-row equality cannot be expressed via FK or partial unique index alone; SQLite triggers are the lowest-cost physical guard; identity-level invariants must not rely on app write-path discipline alone; INSERT path covers backfill / debug-script / CLI direct writes; UPDATE path covers outbound supersession rewiring |
| evidence identity columns are immutable after insert | SQLite trigger `trg_evidence_identity_columns_immutable` (BEFORE UPDATE OF `capture_id` / `evidence_kind` / `lineage_variant`) | closes the inbound target-lineage mutation gap: once a row is referenced by another row's `superseded_by`, its identity tuple must not be mutated into a different lineage; simpler rule is to make the identity tuple immutable for every evidence row |
| superseded rows are never silently deleted | `ON DELETE RESTRICT` through the evidence chain | audit history must remain anchored |
| no default cascade or nulling delete behavior in evidence chain | explicit prohibition of `ON DELETE CASCADE` and `ON DELETE SET NULL` | protects against accidental chain collapse |

#### 1.1.1 SQLite Trigger Contract

```sql
-- Candidate DDL only. Not a migration script. Phase 2A migration dispatch must
-- generate ALL THREE triggers as part of the evidence_ledger creation
-- transaction.

CREATE TRIGGER IF NOT EXISTS trg_evidence_supersession_lineage_check_insert
BEFORE INSERT ON evidence_ledger
WHEN NEW.superseded_by IS NOT NULL
BEGIN
    SELECT CASE
        WHEN NEW.superseded_by = NEW.evidence_id
        THEN RAISE(ABORT, 'supersession_self_reference')
    END;
    SELECT CASE
        WHEN NOT EXISTS (
            SELECT 1
            FROM evidence_ledger ref
            WHERE ref.evidence_id = NEW.superseded_by
              AND ref.capture_id = NEW.capture_id
              AND ref.evidence_kind = NEW.evidence_kind
              AND ref.lineage_variant = NEW.lineage_variant
        )
        THEN RAISE(ABORT, 'supersession_lineage_mismatch')
    END;
END;

CREATE TRIGGER IF NOT EXISTS trg_evidence_supersession_lineage_check_update
BEFORE UPDATE OF superseded_by
ON evidence_ledger
WHEN NEW.superseded_by IS NOT NULL
BEGIN
    SELECT CASE
        WHEN NEW.superseded_by = NEW.evidence_id
        THEN RAISE(ABORT, 'supersession_self_reference')
    END;
    SELECT CASE
        WHEN NOT EXISTS (
            SELECT 1
            FROM evidence_ledger ref
            WHERE ref.evidence_id = NEW.superseded_by
              AND ref.capture_id = NEW.capture_id
              AND ref.evidence_kind = NEW.evidence_kind
              AND ref.lineage_variant = NEW.lineage_variant
        )
        THEN RAISE(ABORT, 'supersession_lineage_mismatch')
    END;
END;

CREATE TRIGGER IF NOT EXISTS trg_evidence_identity_columns_immutable
BEFORE UPDATE OF capture_id, evidence_kind, lineage_variant
ON evidence_ledger
BEGIN
    SELECT RAISE(ABORT, 'evidence_identity_columns_immutable');
END;
```

Rationale: Identity invariants (one current row per logical lineage;
supersession must stay within same lineage; supersession must not
self-reference) cannot be enforced by FK + partial unique index alone because
cross-row multi-column equality has no relational primitive in SQLite. The
triggers are the minimum physical guard.

Coverage: INSERT trigger covers backfill scripts, SQLite CLI direct inserts,
and migration tooling. Supersession UPDATE trigger covers outbound
`superseded_by` rewiring. Identity immutable trigger covers direct identity
tuple mutation and the inbound referenced-target gap where row A points to row
B, then row B's `(capture_id, evidence_kind, lineage_variant)` is mutated
after the reference exists.

Solo-dev multi-entry-point reality (SQLite CLI / debug script / future worker /
migration backfill) makes app-only enforcement insufficient for an identity
invariant.

### 1.2 Enforced In App

The following remain app-layer or reporting-layer concerns:

| Concern | Owner | Why not SQL |
|---|---|---|
| which current version Trust Trace shows first | storage / projection layer | display policy, not identity |
| supersession-triggered events or notifications | service / orchestration layer | procedural behavior |
| UI treatment of historical versions | reporting / UI | presentation concern |
| future cross-kind compatibility rules beyond current contract | app rule + future amendment | still evolving |

### 1.3 Deferred

- event emission policy for supersession
- historical-chain performance optimizations
- UI ordering of superseded rows

### 1.4 Cross-Capture Identity Invariant (F-011)

Multiple evidence-chain references in this amendment carry both an identity
column and a separate `capture_id`. Without composite physical guards, the two
can diverge: `evidence_ledger.source_artifact_asset_id` could point to an
`artifact_assets` row from a different capture than
`evidence_ledger.capture_id`. This is an identity-level invariant, not a flow
concern.

#### 1.4.1 Composite identity unique indexes (REQUIRED in Phase 2A migration)

```sql
-- Each evidence-chain table must expose its identity tuple as a composite
-- unique index so downstream tables can FK against (id, capture_id) and
-- physically reject cross-capture references.

CREATE UNIQUE INDEX IF NOT EXISTS idx_receipt_ledger_id_capture
ON receipt_ledger(receipt_id, capture_id);

CREATE UNIQUE INDEX IF NOT EXISTS idx_artifact_assets_id_capture
ON artifact_assets(id, capture_id);

CREATE UNIQUE INDEX IF NOT EXISTS idx_evidence_ledger_id_capture
ON evidence_ledger(evidence_id, capture_id);
```

#### 1.4.2 Composite FKs (REQUIRED in Phase 2A migration target shape)

```sql
-- evidence_ledger references both receipt and artifact while sharing
-- capture_id. Composite FK rejects "evidence in capture A points to
-- receipt/artifact in capture B".

-- (Within evidence_ledger CREATE TABLE)
FOREIGN KEY (receipt_id, capture_id)
    REFERENCES receipt_ledger(receipt_id, capture_id)
    ON DELETE RESTRICT,

FOREIGN KEY (source_artifact_asset_id, capture_id)
    REFERENCES artifact_assets(id, capture_id)
    ON DELETE RESTRICT

-- (Within artifact_assets CREATE TABLE, where evidence_id is nullable forward
-- link)
FOREIGN KEY (evidence_id, capture_id)
    REFERENCES evidence_ledger(evidence_id, capture_id)
    ON DELETE RESTRICT

-- (Within job_events CREATE TABLE, where receipt_id is nullable append-log
-- linkage)
FOREIGN KEY (receipt_id, capture_id)
    REFERENCES receipt_ledger(receipt_id, capture_id)
    ON DELETE RESTRICT
```

#### 1.4.3 Circular reference handling

`artifact_assets ↔ evidence_ledger` is bidirectional (artifacts may exist
before evidence; evidence may reference an artifact that is later linked back).
This implies 2-pass insertion under composite FK enforcement:

1. Insert artifact rows with `evidence_id IS NULL`.
2. Insert evidence rows referencing artifact via composite FK.
3. UPDATE artifact rows to set `evidence_id` (composite FK back to evidence).

Phase 2A migration must script this 2-pass shape into a single transaction so
that `PRAGMA foreign_keys=ON` (see §1.5 / F-012) does not reject intermediate
state.

#### 1.4.4 Rationale

Cross-capture mismatch is an identity-level invariant. Solo-dev
multi-entry-point reality (SQLite CLI / debug script / migration backfill /
future worker) makes app-only enforcement insufficient. Composite physical FK
is preferred over trigger-based check because it is more readable, more
debuggable, and has zero runtime overhead.

### 1.5 SQLite FK Enforcement Precondition (F-012)

All FK / `ON DELETE RESTRICT` / composite FK guards declared in this amendment
are decorative until SQLite foreign-key enforcement is enabled at the
connection level. As of `main` HEAD `fdf0673` (PR #51), `Storage._connect()`
in `services/api/scoutflow_api/storage.py` does NOT enable foreign-key
enforcement.

#### 1.5.1 Phase 2A Implementation Hard Gate

Phase 2A migration approval is BLOCKED until all of the following are true:

```python
# Required change in services/api/scoutflow_api/storage.py:
def _connect(self) -> sqlite3.Connection:
    self.config.db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(self.config.db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")  # F-012
    return conn
```

#### 1.5.2 Required Test Evidence

```python
# tests/api/test_storage_fk_enforcement_contract.py (or equivalent)
def test_pragma_foreign_keys_on_every_connection(storage):
    with storage._connect() as conn:
        assert conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1

def test_on_delete_restrict_rejects_evidence_chain_delete(storage):
    # Delete attempt on captures with evidence_ledger / receipt_ledger /
    # artifact_assets / job_events references must raise sqlite3.IntegrityError.
    ...

def test_composite_fk_rejects_cross_capture_evidence(storage):
    # Insert evidence in capture A pointing to receipt in capture B must fail.
    ...

def test_supersession_lineage_trigger_rejects_mismatch(storage):
    # INSERT or UPDATE that sets superseded_by to a different lineage must fail.
    ...

def test_supersession_lineage_trigger_rejects_self_reference(storage):
    # superseded_by = evidence_id must fail.
    ...

def test_evidence_identity_columns_immutable_after_insert(storage):
    # UPDATE capture_id / evidence_kind / lineage_variant after insert must
    # fail, even when the row has no superseded_by value.
    ...
```

#### 1.5.3 Owner

The PRAGMA enabling change belongs to a separate code-bearing Phase 2A
migration-prep dispatch. It is NOT addressed in this amendment because this PR
is docs-only and forbids `services/**` edits.

#### 1.5.4 Drift Risk

If Phase 2A migration is approved before §1.5.1 lands, all FK / `ON DELETE
RESTRICT` / composite FK guards in this amendment become silently inert.
Storage CHECK clauses remain enforced because they do not depend on the
foreign_keys PRAGMA. Triggers also remain enforced because SQLite triggers fire
independently of foreign-key enforcement. Composite and single FKs are silently
inert — this is the failure mode F-012 prevents.

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

### 3.5 PlatformResult Vocabulary Binding

Every `platform_result TEXT` column in this amendment is bound to the
`C-PLT-001 PlatformResult` enum (see `../specs/contracts-index.md`,
implementation in `services/api/scoutflow_api/platform_result.py`).

Authoritative 12-value vocabulary (alphabetical):

```text
auth_required
forbidden
network_error
not_found
ok
parser_drift
rate_limited
region_blocked
timeout
unavailable
unknown_error
vip_required
```

Drift policy: any vocabulary expansion must:

1. Add the new value to `services/api/scoutflow_api/platform_result.py:PlatformResult`.
2. Update this amendment's CHECK clauses in §4 (both NOT NULL and nullable forms).
3. Generate a separate `services/api/migrations/NNN_*.sql` performing CHECK
   re-creation (SQLite does not support `ALTER COLUMN`; CHECK migration
   requires a table-rebuild migration pattern).
4. Pass external audit before merge.

Until the migration lands, dual-layer enforcement is required: Pydantic enum
at API boundary + SQL CHECK at storage boundary. Drift between layers is a
contract violation.

### 3.6 Phase Reachability Vocabulary

Status enums in this amendment include Phase 2+ reserved values (for example
`queued`, `media_*`, `audio_*`, `transcribing`, and `archived`). These are
SQL-physical (`CHECK`-allowed) but PRD/SRD/LP-001 enforce that they are NOT
reachable under the current `metadata_only` `quick_capture_preset`.

Reachable in Phase 1A (current):

- `discovered`
- `metadata_fetched`

Reserved (Phase 2+; NOT reachable now):

- `queued`, `media_downloading`, `media_ready`, `audio_extracting`,
  `audio_ready`, `transcribing`, `transcript_ready`, `normalizing`,
  `doc_ready`, `indexing`, `indexed`, `linking`, `linked`, `archived`,
  `superseded`

Promotion rules: enabling any reserved value requires:

1. PRD/SRD amendment opening the lifecycle.
2. LP-001 capture scope gate amendment.
3. Explicit user gate (decision-log entry).
4. External audit.

SQL-shape admission ≠ reachability. UI / Trust Trace consumers MUST display
status with scope prefix (per §9.1 of
`../research/t-p1a-020-trust-trace-explore-state-map-2026-05-04.md`): do not
render bare `Status: queued`; render `metadata_job.status: queued` or
`capture_state.status: discovered`.

`captures.status = 'queued'` is reserved and not currently reachable; current
queued/running semantics live in `jobs.status` / `metadata_job.status`. The two
`queued` values are scope-isolated by their owning table. Do not collapse them
in UI or in Trust Trace projections.

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
            -- Phase 1A reachable under current `metadata_only` /
            -- `quick_capture` contract
            'discovered',
            'metadata_fetched',

            -- Phase 2+ reserved; NOT reachable under current contract.
            -- Reachability requires PRD/SRD amendment + LP-001 capture scope
            -- gate amendment + explicit user gate + external audit. SQL CHECK
            -- admits these values to allow a single-pass migration in Phase
            -- 2A; the reachability gate is enforced at the application /
            -- lifecycle layer, not by storage shape.
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
    platform_result TEXT NOT NULL CHECK (
        platform_result IN (
            'ok',
            'auth_required',
            'rate_limited',
            'forbidden',
            'not_found',
            'region_blocked',
            'vip_required',
            'parser_drift',
            'network_error',
            'timeout',
            'unavailable',
            'unknown_error'
        )
    ),
    artifact_count INTEGER NOT NULL CHECK (artifact_count >= 0),
    duration_seconds REAL CHECK (duration_seconds IS NULL OR duration_seconds >= 0),
    receipt_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    UNIQUE(job_id, dedupe_key),
    FOREIGN KEY (job_id, capture_id, job_type, dedupe_key)
        REFERENCES jobs(job_id, capture_id, job_type, dedupe_key)
        ON DELETE RESTRICT
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_receipt_ledger_id_capture
    ON receipt_ledger(receipt_id, capture_id);
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
    capture_id TEXT NOT NULL,
    evidence_id TEXT,
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
    FOREIGN KEY (capture_id)
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    FOREIGN KEY (evidence_id, capture_id)
        REFERENCES evidence_ledger(evidence_id, capture_id)
        ON DELETE RESTRICT,
    UNIQUE(capture_id, file_path)
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_artifact_assets_id_capture
    ON artifact_assets(id, capture_id);
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
    capture_id TEXT NOT NULL,
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
    source_artifact_asset_id INTEGER,
    receipt_id TEXT,
    superseded_by TEXT
        REFERENCES evidence_ledger(evidence_id) ON DELETE RESTRICT,
    source_task_id TEXT,
    source_report_path TEXT,
    producer TEXT NOT NULL,
    producer_version TEXT NOT NULL,
    platform_result TEXT CHECK (
        platform_result IS NULL
        OR platform_result IN (
            'ok',
            'auth_required',
            'rate_limited',
            'forbidden',
            'not_found',
            'region_blocked',
            'vip_required',
            'parser_drift',
            'network_error',
            'timeout',
            'unavailable',
            'unknown_error'
        )
    ),
    metadata_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    CHECK ((source_task_id IS NULL) = (source_report_path IS NULL)),
    CHECK (
        source_artifact_asset_id IS NOT NULL
        OR receipt_id IS NOT NULL
    ),
    FOREIGN KEY (capture_id)
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    FOREIGN KEY (source_artifact_asset_id, capture_id)
        REFERENCES artifact_assets(id, capture_id)
        ON DELETE RESTRICT,
    FOREIGN KEY (receipt_id, capture_id)
        REFERENCES receipt_ledger(receipt_id, capture_id)
        ON DELETE RESTRICT
);

CREATE UNIQUE INDEX IF NOT EXISTS idx_evidence_ledger_id_capture
    ON evidence_ledger(evidence_id, capture_id);

CREATE UNIQUE INDEX IF NOT EXISTS idx_evidence_current_per_lineage
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
    capture_id TEXT NOT NULL,
    job_id TEXT NOT NULL,
    receipt_id TEXT,
    event_type TEXT NOT NULL,
    event_json TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (capture_id)
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    FOREIGN KEY (job_id, capture_id)
        REFERENCES jobs(job_id, capture_id)
        ON DELETE RESTRICT,
    FOREIGN KEY (receipt_id, capture_id)
        REFERENCES receipt_ledger(receipt_id, capture_id)
        ON DELETE RESTRICT
);
```

### 4.6 Carried-Over `jobs` Table Shape (FK boundary)

`receipt_ledger` / `job_events` both reference the v2 baseline `jobs` table
from `../../services/api/migrations/002_phase1a_jobs_receipt.sql`. Phase 2A
migration MUST reuse that schema rather than recreating `jobs`.

#### Reference shape (do not recreate in migration)

```sql
-- v2 baseline shape — for reference only.
CREATE TABLE jobs (
    job_id TEXT PRIMARY KEY,
    capture_id TEXT NOT NULL,
    job_type TEXT NOT NULL,
    status TEXT NOT NULL,
    dedupe_key TEXT NOT NULL,
    platform_result TEXT,
    -- ... other v2 columns
);

-- Phase 2A migration MUST add BOTH composite identity indexes BEFORE any
-- evidence-chain table FK declarations below. SQLite requires the parent key
-- tuple of a composite FOREIGN KEY to be an EXACT primary key or unique index.
-- The existing PRIMARY KEY on job_id and idx_jobs_capture_type_dedupe are not
-- sufficient for the 4-column or 2-column child FKs below.

-- (a) 4-column index — parent key for receipt_ledger composite FK
CREATE UNIQUE INDEX IF NOT EXISTS idx_jobs_identity_tuple
ON jobs(job_id, capture_id, job_type, dedupe_key);

-- (b) 2-column index — parent key for job_events composite FK
-- Required because job_events is an append log and intentionally does NOT
-- carry job_type / dedupe_key.
CREATE UNIQUE INDEX IF NOT EXISTS idx_jobs_id_capture
ON jobs(job_id, capture_id);
```

#### Composite consistency target (preferred over single-column FK)

`receipt_ledger` / `job_events` carry not just `job_id` but also `capture_id`,
`job_type`, and `dedupe_key`. A single-column FK on `job_id` alone allows
physical inconsistency (for example `receipt.capture_id = A` but `job_id`
actually belongs to capture `B`). Phase 2A migration target shape must use
composite FK across the identity tuple:

```sql
-- Inline FK in receipt_ledger CREATE TABLE (target shape; not ALTER).
-- In SQLite, foreign-key constraints must be declared inside CREATE TABLE;
-- post-create constraint attachment is not supported.
CREATE TABLE receipt_ledger (
    receipt_id TEXT PRIMARY KEY,
    capture_id TEXT NOT NULL
        REFERENCES captures(capture_id) ON DELETE RESTRICT,
    job_id TEXT NOT NULL,
    job_type TEXT NOT NULL,
    dedupe_key TEXT NOT NULL,
    -- ...
    FOREIGN KEY (job_id, capture_id, job_type, dedupe_key)
        REFERENCES jobs(job_id, capture_id, job_type, dedupe_key)
        ON DELETE RESTRICT
);

CREATE TABLE job_events (
    -- Match v2 baseline column name `id` (not `event_id`); do NOT introduce
    -- column rename drift via this audit-fix.
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_id TEXT NOT NULL,
    capture_id TEXT NOT NULL,
    -- ...
    FOREIGN KEY (job_id, capture_id)
        REFERENCES jobs(job_id, capture_id)
        ON DELETE RESTRICT
);
```

#### Rationale

Composite FK rejects `receipt.capture_id = A` while the actual parent job
belongs to capture `B` at the storage boundary. Single-column FK + app-only
check is an identity invariant violation under solo-dev multi-entry reality
(SQLite CLI direct insert / debug script / migration backfill / future worker).
`ON DELETE RESTRICT` aligns with §2.2 SQL Defaults.

## 5. Deferred To Phase 2A First Implementation Task

The following decisions are intentionally **not** fixed in this amendment:

| Topic | Deferred to | Why deferred |
|---|---|---|
| query patterns and access paths | Phase 2A first implementation task | depends on final Explore shape and real caller behavior |
| index strategy beyond the identity-level unique indexes in §1.4 + §4.6 and `idx_evidence_current_per_lineage` | Phase 2A first implementation task | requires `EXPLAIN` and real data shape |
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

- [SRD-v2-2026-05-04.md](../SRD-v2-2026-05-04.md)
- [PRD-v2-2026-05-04.md](../PRD-v2-2026-05-04.md)
- [t-p1a-025-db-ledger-vnext.md](../research/t-p1a-025-db-ledger-vnext.md)
- [t-p1a-022-asr-pipeline-prestudy-2026-05-04.md](../research/t-p1a-022-asr-pipeline-prestudy-2026-05-04.md)
- [t-p1a-023-llm-normalization-schema-2026-05-04.md](../research/t-p1a-023-llm-normalization-schema-2026-05-04.md)
- [t-p1a-024-explore-capture-scope-state-table-2026-05-04.md](../research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md)
- [db-vnext-design-2026-05-04.md](../specs/db-vnext-design-2026-05-04.md)
- [001_phase1a_capture_creation.sql](../../services/api/migrations/001_phase1a_capture_creation.sql)
- [002_phase1a_jobs_receipt.sql](../../services/api/migrations/002_phase1a_jobs_receipt.sql)

## 99. Known Follow-up Debt (Not Addressed by This Audit-Fix)

The following items are tracked but explicitly out of scope for this
audit-fix:

- F-009: PR #48 superseded notation. Addressed by T-P1A-027 (S0)
  decision-log entry, not this PR.
- F-010: `WorkerReceipt.next_status="metadata_fetched"` semantics on failure
  receipts. The field is currently set on failure receipts
  (`produced_assets=[]`, `platform_result != ok`) but is ignored by storage
  when `job_status=failed`. This is a misleading-by-naming schema design smell.
  Defer to Phase 2A migration prep. `WorkerReceipt` schema change requires
  API/storage/test PR with external audit and is not addressable in this
  docs-only audit-fix.
- F-012 implementation: `PRAGMA foreign_keys=ON` enabling is a code change in
  `services/api/scoutflow_api/storage.py` plus FK enforcement test suite.
  Tracked as Phase 2A first migration-prep task. Out of scope for this
  docs-only PR but recorded in §1.5 as a Phase 2A hard gate.
- captures lifecycle full reachability promotion for Phase 2+ statuses
  requires a separate PRD/SRD amendment + LP-001 amendment (per §3.6).
