# DB vNext Design

---
status: draft
topic: db-vnext
date: 2026-05-04
scope: ScoutFlow Phase 1A closeout to Phase 2A pre-migration DB vNext design
source_pr: PR #42
source_pr_status: draft research input, not merged at spec write time
authority_base:
  - docs/PRD-v2-2026-05-04.md
  - docs/SRD-v2-2026-05-04.md
not_runtime_approval: true
not_migration_approval: true
---

## 1. Goal

Define the DB vNext design gate for ScoutFlow at the correct phase boundary:
after Phase 1A research signals are frozen and before the first Phase 2A
migration is written.

This design does not authorize any migration, runtime expansion, or authority
promotion by itself. It defines:

- what Stage 1 must freeze
- what the SRD amendment must contain
- what must be explicitly deferred
- how the resulting amendment will later feed Phase 2A migration work

## 2. Why Now

The correct DB vNext design window is:

- preferred: Phase 1A tail, after candidate research lanes are frozen
- latest acceptable: immediately before the first Phase 2A migration task

Too early means schema candidates are still moving. Too late means migration
and implementation decisions begin to harden against an unreviewed target
shape.

## 3. Locked Decisions

The following decisions are treated as locked inputs for this design.

1. Primary artifact model: `A'`
   `#42` is a frozen research artifact; the spec is the main contract-bearing
   deliverable.
2. Sequencing: `A`
   Merge/freeze `#42` first, then write the DB vNext spec.
3. Spec carrier: `A`
   Use an `SRD-amendment` style document, not a separate fifth document class,
   and do not inline Phase 2A design into `SRD-v2` base.
4. Amendment scope: `A`
   Minimal contract plus explicit deferred section.
5. SQL depth: `B`
   ER plus candidate DDL shape, but no migration step sequence.
6. DDL carrier: `A`
   Inline fenced `sql` inside the amendment Markdown.
7. Supersession boundary: `C`
   Identity-level rules in SQL; flow/display semantics in the app layer.
8. Lineage key granularity: `B`
   Current uniqueness is scoped by `(capture_id, evidence_kind, lineage_variant)`.
9. Purge strategy: `C`
   Abstract purge policy and SQL defaults are in scope now; purge mechanism is
   deferred to Phase 2A implementation.
10. DDL coverage: `A`
    The amendment carries the full evidence-chain v3 candidate target shape,
    not only touched fragments.

## 4. Stage 1 - Freeze Research Input

Stage 1 is a repository-governance action, not schema implementation work.
Its job is to turn `#42` into a stable research input before any amendment is
written.

### 4.1 Objective

Freeze `PR #42` as a merged research note on `main`, then prohibit further
decision edits in that note. After merge, all DB decision changes must land in
the amendment or an amendment addendum, never by reopening or mutating the
research artifact.

### 4.2 Required Actions

1. Checkout the `#42` branch.
2. Align the research note filename to the prevailing dated research-note
   convention used by `021/022/023/024`, with the final name determined by the
   actual merge-time repository state.
3. Keep the PR as a research-only PR.
4. Squash or otherwise tidy the PR history before merge if needed.
5. Merge `#42`.
6. Run post-merge ledger sync in the same pattern as the existing post-merge
   sync chores:
   `docs/task-index.md`, `docs/current.md`, `docs/decision-log.md`, and
   `AGENTS.md`.
7. Treat the merged research path as frozen input from that point onward.

### 4.3 Stage 1 Constraints

- `#42` remains research only.
- No DB migration is written in Stage 1.
- No schema authority is promoted in Stage 1.
- No runtime gate is widened in Stage 1.
- The final merged research file path must be the path referenced by the
  amendment's `research_inputs` section. The path must not be invented ahead of
  the merge.

## 5. Stage 2 - SRD Amendment Shape

Stage 2 produces a candidate amendment under `docs/SRD-amendments/` using the
actual write date in the filename, for example:

`docs/SRD-amendments/db-vnext-srd-v3-candidate-YYYY-MM-DD.md`

### 5.1 Amendment Header

The amendment should self-label as a candidate promote target and clearly pin
its basis with these fields:

- `status: amendment / candidate-for-SRD-v3-promote`
- `authority_base: docs/SRD-v2-2026-05-04.md`
- `based_on_main_commit`: the actual `main` commit hash at amendment write time
- `research_inputs`: the actual merged path from `#42`, plus the relevant
  merged research notes from `022/023/024`
- `promote_target: SRD-v3`
- `revalidate_before_promote: true`
- `not_runtime_approval: true`
- `not_migration_approval: true`

### 5.2 Amendment Must Include

- schema shape for the evidence chain
- core invariants
- migration principles
- supersession semantics
- deletion and purge defaults
- explicit deferred section
- full v3 candidate target shape for the evidence chain

### 5.3 Amendment Must Not Include

- migration execution order
- transaction choreography
- rollback playbook
- concrete purge implementation
- backup/retention/ops/observability implementation detail
- query/index optimization decisions that depend on real usage or data

## 6. Candidate DDL Policy

The amendment carries candidate DDL as a shape-only contract.

The DDL must be:

- inline in the amendment Markdown
- readable without opening another file
- clearly marked as candidate and not migration-ready
- sufficient for paper review of FK consistency, delete behavior, and
  uniqueness semantics

The DDL must not contain:

- migration ordering
- data backfill statements
- transaction wrappers
- implementation-time `CREATE INDEX` decisions beyond identity-level
  uniqueness requirements

### 6.1 Required Framing Around SQL Blocks

Every candidate SQL block should be defended at three layers:

1. section heading
2. prose warning
3. SQL comment header

Example pattern:

````text
## CANDIDATE DDL (shape-only contract)

> This block is not a migration script. Do not copy it directly into
> `services/api/migrations/`. Final SQL syntax, step order, transaction
> boundary, and rollback strategy are deferred to the Phase 2A first
> implementation task.

```sql
-- ============================================================
-- CANDIDATE DDL — SRD-v3 shape contract
-- NOT A MIGRATION. NOT EXECUTABLE AS-IS.
-- ============================================================
```
````

### 6.2 Machine-Consumption Note

The amendment may include a short extraction recipe for implementation-time
reuse, but extraction is a consumer behavior, not a reason to split the source
of truth into multiple files.

## 7. Evidence-Chain Coverage

The amendment should carry the full v3 candidate target shape for the evidence
chain:

- `captures`
- `evidence_ledger`
- `artifact_assets`
- `receipt_ledger`
- `job_events`

Each table block should be labeled with one of:

- `carried over from v2`
- `carried over with a specific change`
- `reshaped in v3`
- `NEW in v3`

The amendment should also include a short `v2 -> v3` diff summary table before
the full DDL blocks so the reader can preview the meaningful deltas before
reading the complete target shape.

## 8. Supersession Boundary

Supersession is split by identity vs flow:

- SQL owns identity-level invariants.
- App code owns flow, rendering, and operational behavior.

### 8.1 Enforced In SQL

The amendment should treat the following as SQL-owned identity invariants:

- one current row per `(capture_id, evidence_kind, lineage_variant)`
- self-FK for `superseded_by`
- no silent physical deletion of referenced evidence rows
- no default cascade deletion across the evidence chain
- clear `NULL` semantics for current rows

### 8.2 Enforced In App

The amendment should treat the following as app-owned flow semantics:

- which version a Trust Trace projection chooses to display
- event emission or notifications around supersession
- purge workflow orchestration
- reporting and UI presentation of history chains
- compatibility policy across future evidence kinds when not yet contractually
  stabilized

## 9. Lineage Variant Contract

The lineage key is evidence-layer identity, not artifact-layer identity.

### 9.1 Current Uniqueness

Current uniqueness is scoped by:

`(capture_id, evidence_kind, lineage_variant)` where `superseded_by IS NULL`

This prevents re-probe from creating parallel current rows for the same logical
lineage while still leaving a stable hook for multiple legitimate lineage
variants.

### 9.2 `lineage_variant` Rules

The amendment should define:

- `lineage_variant` as `NOT NULL`
- a bounded vocabulary via `CHECK (...)`
- a mapping from values to approved or reserved task origins
- an explicit note about what metadata does not belong in
  `lineage_variant`

Examples of things that do not belong in `lineage_variant`:

- tool version
- timestamps
- triggering path
- `sha256`
- `file_path`
- receipt row ids

Those belong to metadata, timeline, or artifact layers rather than lineage
identity.

## 10. Purge Boundary

Purge follows the same split as supersession:

- abstract policy and default SQL boundary are in scope now
- operational purge implementation is deferred

### 10.1 Abstract Purge Policy

The amendment should state at least these identity-level rules:

1. Physical deletion in the evidence chain requires user-explicit confirmation
   and a dedicated purge path.
2. Deleting upstream entities must not silently cascade through the evidence
   chain.
3. Referenced evidence-chain rows reject deletion by default.
4. The purge action itself must leave an audit trail and must not be silently
   removable by the same ordinary path.

### 10.2 SQL Defaults

The amendment should explicitly treat the following as contract defaults:

- no `ON DELETE CASCADE` in the evidence chain
- `ON DELETE RESTRICT` for identity-preserving relationships
- no `ON DELETE SET NULL` where it would erase audit meaning

Any future desire to introduce `CASCADE` or `SET NULL` in the evidence chain
should require a separate amendment and external audit.

### 10.3 Deferred Purge Implementation

The amendment should defer:

- tombstone vs hard-delete-with-audit
- vacuum / space reclamation
- maintenance flow
- retention timing
- concrete purge function signature
- final audit-log schema for purge events

## 11. Deferred To Phase 2A First Task

The amendment should explicitly defer, rather than silently omit:

- query patterns and access paths
- index strategy beyond identity-level requirements
- backup / retention implementation
- observability / metrics
- purge mechanism details
- migration step sequence
- transaction boundaries
- rollback script

The deferred table should name the owning future task category and explain why
the decision is deferred.

## 12. Stage-1 Completion Criteria

For the design to consider Stage 1 complete:

1. `#42` is merged to `main`.
2. The final merged research note path is known and frozen.
3. Authority bookkeeping reflects `T-P1A-025` as frozen research rather than a
   mutable draft.
4. The amendment can reference a stable local path rather than a mutable PR URL.

## 13. Risks

- The final research filename is not knowable until `#42` is actually merged;
  the amendment must consume the real merged path, not a guessed name.
- `PR #42` currently reports `mergeStateStatus=UNKNOWN`; Stage 1 must verify
  mergeability again immediately before merge.
- `T-P1A-020` is still active. While it is not expected to rewrite schema, any
  mainline drift before amendment writing should be captured by
  `based_on_main_commit` plus `revalidate_before_promote`.

## 14. Out Of Scope

- implementation of the amendment
- writing migrations
- changing runtime gates
- changing `PlatformResult`
- changing `WorkerReceipt`
- widening `audio_transcript`
- BBDown live runtime enablement

## 15. Recommended Next Steps

1. Complete Stage 1 by freezing and merging `#42`.
2. Run the post-merge authority sync for `T-P1A-025`.
3. Write the amendment against the actual merged research path and pinned
   `main` commit.
4. Review the amendment as a self-contained v3 candidate target shape before
   any Phase 2A migration dispatch is written.
