# SRD-v3 Candidate Amendment - H5 Bridge PARA Vault

---
title: H5 Bridge PARA Vault SRD v3 Candidate
status: amendment / promoted
task_id: T-P1A-034
pr_number: PR #59
candidate: false
not_authority: false
not_runtime_approval: true
not_frontend_approval: true
not_migration_approval: true
promoted_at: 2026-05-05
promoted_via: T-P1A-102
authority_base: docs/SRD-v2-2026-05-04.md
based_on_main_commit: 554f497feb31e60022542eb06bf21a74487e4e09
related_inputs:
  - docs/research/pr55-pr74-worklist-candidate-2026-05-04.md
  - docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md
  - docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md
  - docs/research/doc1-doc2-doc3-v1.1-acceptance-errata-report-2026-05-04.md
  - docs/research/opus-v3-acceptance-prd-srd-amendment-roadmap-review-2026-05-04.md
  - docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md
  - /Users/wanglei/workspace/ScoutFlow-PR58/docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md
sunset_trigger: Deprecated when equivalent sections are promoted into a later SRD base after Wave 3A closeout, Wave 4 walking skeleton evidence, and explicit user promotion gate.
revalidate_before_promote: false
---

> Status: `promoted / not runtime approval / not frontend approval / not migration approval` (promoted at T-P1A-102, 2026-05-05; runtime + frontend + migration approval still gated; revalidation folded into promotion gate).
> This amendment extends `docs/SRD-v2-2026-05-04.md` as a read-only base reference. It does not modify the promoted SRD baseline.

## 0. Boundary

This amendment defines the target engineering shape for a future H5 Capture
Station projection, a Thin API Bridge route group, and a VaultWriter contract
that writes into the existing PARA vault boundary.

Allowed in this amendment:

- L3 H5 projection shape and panel responsibilities
- L2 Bridge route-group shape inside the existing FastAPI surface
- local Bridge/Vault error vocabulary
- vault preview / vault commit request and response shapes
- VaultWriter path policy, frontmatter contract, and fixed body sections
- explicit out-of-scope and promotion gates

Not allowed in this amendment:

- edits to `docs/SRD-v2-2026-05-04.md`
- edits to `docs/SRD-amendments/db-vnext-srd-v3-candidate-2026-05-04.md`
- `services/**`, `apps/**`, `workers/**`, `packages/**`, `migrations/**`
- runtime approval for BBDown live, ffmpeg, Whisper family, or browser automation
- frontend implementation approval
- migration approval
- extra signing / cryptographic receipt layers
- remote vault sync or cross-vault replication

Dependency note: section shape is intentionally aligned to the stable six-section
candidate skeleton already landed in the parallel PR58 worktree at
`docs/PRD-amendments/prd-v2.1-strong-visual-h5-para-pr-factory-candidate-2026-05-04.md`.
That file is a candidate reference, not a promoted authority input inside this
branch.

### §17.1 H5 Capture Station

The future H5 Capture Station is the L3 projection layer for ScoutFlow. Its
role is to make capture-time state, scope, and evidence legible in one screen.
It is not an authority writer, and it is not a second storage system.

L3 responsibilities:

- receive bounded operator input for manual URL capture
- project metadata, scope, and trust-trace state from the existing API
- expose blocked layers explicitly instead of implying hidden approval
- preview future vault output before any write step

L3 non-responsibilities:

- no direct SQLite writes
- no direct file writes into the vault
- no direct BBDown execution
- no direct Whisper / ffmpeg execution
- no direct state-word mutation

Candidate stack family:

| Layer | Candidate family | Notes |
|---|---|---|
| bundler | `Vite` | default dev surface; later lock belongs to frontend-specific spec |
| UI runtime | `React + TypeScript` | family only, not version lock |
| primitives | `shadcn/ui + Radix UI` | component family only |
| async / form / data grid | `TanStack Query + Form + Table` | H5 data projection, not authority |
| graph | `React Flow` | trust trace + scope graph projection |
| local state | `Zustand` | bounded client state only |
| styling | `Tailwind` | token family only |
| icons | `Lucide` | consistent tool affordances |

The H5 surface is a four-panel single-page projection:

| Panel | Inputs | Outputs | Internal state | API calls |
|---|---|---|---|---|
| `URL Bar` | manual URL, source kind, bounded action trigger | request intent, validation hints, blocked reasons | `idle -> editing -> ready -> requested` | `POST /captures/discover` only |
| `Live Metadata` | capture id, pending job state, probe summary | title, uploader, duration, page count, last probe result | `empty -> loading -> visible -> stale` | existing metadata/trust-trace reads only |
| `Capture Scope` | current preset, blocked phase flags, policy summary | visible allow/deny scope, future-stage grey states | `projected -> confirmed_or_blocked` | read-only projection from existing capture/trust-trace state |
| `Trust Trace` | capture lifecycle entities, receipt summary, probe evidence summary | graph / timeline / badges | `empty -> partial -> layered` | `GET /captures/{capture_id}/trust-trace` |

State projection model:

```text
manual_url_entered
  -> capture_requested
  -> metadata_visible
  -> scope_visible
  -> vault_preview_ready
  -> future_commit_gate
```

Gate interpretation:

- `manual_url_entered -> capture_requested`: only for approved manual URL entry
- `capture_requested -> metadata_visible`: only after safe API-side creation and allowed probe evidence
- `metadata_visible -> scope_visible`: only after the blocked layers are explicitly rendered
- `scope_visible -> vault_preview_ready`: preview only; no file write
- `vault_preview_ready -> future_commit_gate`: route exists as candidate boundary only

Network / runtime assumptions:

- default local port is `8080`
- future configurability may use `H5_PORT`
- browser surface remains local-only
- the H5 layer must fail soft when unavailable; it does not replace API truth

### §17.2 Bridge / Thin API Route Group

Bridge is not a second Python process and not a sidecar authority service. It
is a Thin API route group inside the existing `services/api/scoutflow_api`
surface so that storage, receipt, and state semantics stay under one authority
boundary.

Shape:

```text
H5 Capture Station
  -> existing FastAPI app
     -> Bridge route group
        -> storage / trust-trace readers
        -> future VaultWriter capability
```

Route-group principles:

- keep current FastAPI app as the only authority write boundary
- reuse existing capture identity and trust-trace projection semantics
- never bypass receipt/state discipline with a second write channel
- keep local Bridge/Vault errors separate from platform probe results

Candidate route list:

1. `GET /bridge/health`
2. `GET /bridge/vault/config`
3. `GET /captures/{capture_id}/vault-preview`
4. `POST /captures/{capture_id}/vault-commit`
5. `POST /captures/{capture_id}/transcribe` (future, still gated)

Candidate OpenAPI-level input/output shapes:

| Route | Input shape | Output shape | Notes |
|---|---|---|---|
| `GET /bridge/health` | no body | `{ "ok": true, "service": "bridge", "mode": "candidate_route_group", "authority_base": "services/api/scoutflow_api" }` | liveness only; not runtime approval |
| `GET /bridge/vault/config` | no body | `{ "ok": true, "configured": true, "vault_root": "...", "inbox_path": "...", "write_mode": "preview_or_commit" }` | if unset or invalid, return `BridgeErrorCode.*` |
| `GET /captures/{capture_id}/vault-preview` | path=`capture_id`; optional query for preview mode | `{ "ok": true, "capture_id": "...", "target_path": "...", "frontmatter": {...}, "sections": [...], "markdown_preview": "..." }` | preview only; no file write |
| `POST /captures/{capture_id}/vault-commit` | path=`capture_id`; body with idempotency / operator confirmation fields | `{ "ok": true, "capture_id": "...", "target_path": "...", "bytes_written": 1234, "frontmatter_fields": 4, "body_sections": 4 }` | actual file write remains future gated capability |
| `POST /captures/{capture_id}/transcribe` | path=`capture_id`; future request body | `{ "ok": false, "blocked": true, "reason": "audio_transcript_blocked" }` until Wave 6 gate | exists as reserved future route only |

Local Bridge/Vault failures must use a dedicated local error vocabulary:

```python
BridgeErrorCode = Literal[
    "vault_root_not_configured",
    "vault_root_not_found",
    "vault_inbox_not_found",
    "vault_path_escape",
    "vault_file_exists",
    "frontmatter_invalid",
    "markdown_render_failed",
]
```

Candidate error response shape:

```json
{
  "ok": false,
  "error": {
    "code": "vault_root_not_found",
    "message": "Configured vault root does not exist.",
    "details": {}
  }
}
```

Boundary rule: `PlatformResult` remains platform-only. It describes platform
boundary results such as BBDown / Bilibili probe outcomes and must not absorb
Bridge / Vault local errors. `ToolPreflightResult` remains the tool-availability
layer. This amendment preserves that split.

Reserved semantics per route:

- `GET /bridge/health` does not imply vault write readiness
- `GET /bridge/vault/config` must fail loud when `SCOUTFLOW_VAULT_ROOT` is not configured or invalid
- `GET /captures/{capture_id}/vault-preview` may render markdown in memory only
- `POST /captures/{capture_id}/vault-commit` must not run until a future dispatch unlocks the write path
- `POST /captures/{capture_id}/transcribe` remains blocked until a later phase explicitly unlocks `audio_transcript`

### §17.3 VaultWriter Contract

VaultWriter is the future write capability behind Bridge. It targets the
existing PARA vault boundary instead of creating a second knowledge system.

Configuration policy:

- product guidance may recommend `${SCOUTFLOW_VAULT_ROOT:-~/workspace/raw}`
- SRD / implementation must treat `SCOUTFLOW_VAULT_ROOT` as explicit runtime configuration
- when unset, the route must fail loud with `BridgeErrorCode.vault_root_not_configured`
- when the configured root does not exist, fail loud with `BridgeErrorCode.vault_root_not_found`
- when `00-Inbox/` is missing, fail loud with `BridgeErrorCode.vault_inbox_not_found`

Allowed target path:

```text
${SCOUTFLOW_VAULT_ROOT}/00-Inbox/scoutflow-{capture_id}-{slug}.md
```

Path policy:

- target path must stay under `${SCOUTFLOW_VAULT_ROOT}/00-Inbox/`
- `..`, symlink escape, or alternate vault roots must be rejected with `BridgeErrorCode.vault_path_escape`
- existing target file must not be overwritten; use `BridgeErrorCode.vault_file_exists`
- the writer emits one markdown file per approved capture export

Frontmatter contract is fixed to the raw four-field template family:

| Field | Type | Candidate value rule |
|---|---|---|
| `title` | string | derived from capture title or safe fallback |
| `date` | string | write-time or capture-time ISO date string |
| `tags` | string or list form per template family | includes `调研/ScoutFlow采集`-style tagging family, final formatting follows the upstream template |
| `status` | string | default `pending` |

Rendered markdown body is fixed to four sections:

1. `## ScoutFlow Capture`
2. `## Metadata`
3. `## Trust Trace`
4. `## Notes`

Candidate section contents:

| Section | Required fields / semantics |
|---|---|
| `## ScoutFlow Capture` | `capture_id`, `platform`, `source_url`, `source_kind`, `quick_capture_preset` |
| `## Metadata` | bounded metadata surfaced from probe evidence such as title, uploader, duration, page count, and safe summary fields |
| `## Trust Trace` | trust-trace URL or locator, receipt summary, probe evidence summary, `media_audio: not_approved` until later phase gate |
| `## Notes` | operator-editable placeholder left intentionally sparse; ScoutFlow does not prefill downstream wiki interpretation |

Preview vs commit rules:

- preview returns full markdown content and target path without writing a file
- commit writes exactly the previewed contract shape
- commit should carry an explicit operator confirmation / idempotency field in a later implementation spec

Explicit prohibitions:

- do not move the file into `02-Raw/`
- do not write into `01-Wiki/`
- do not write into `System/`
- do not trigger `/intake`
- do not trigger `/compile`
- do not create a custom Obsidian schema
- do not create direct writes outside `00-Inbox/`

This amendment only defines the contract shape. It does not approve an actual
runtime writer implementation.

### §17.4 PR Factory Protocol Dependency

This amendment depends on, but does not itself promote, the future PR factory
protocol candidate. The enforced baseline today remains:

- `Active product lane max = 3`
- `Authority writer max = 1`
- same-file writer max remains serialized
- research / prototype lanes stay advisory unless they write authority

Candidate dependency shape for later protocol work:

- possible surge model may raise product lanes to `5`
- research / prototype / audit pools remain advisory capacity, not authority
- every wave must declare a file-domain matrix before code-bearing work
- authority merge ordering remains explicit and serialized

Operational interpretation for this amendment:

- this file is a candidate SRD input, not a protocol override
- any H5 / Bridge / VaultWriter implementation step still needs later dispatches
- merge ordering and concurrency caps continue to be governed by current repo authority until a later closeout promotes new wording

Cross-reference note: the future protocol candidate is expected to land
separately and should be treated as a dependency note, not as an enforced
constraint authored by this file.

### §17.5 Out of Scope

Out of scope for this candidate amendment:

- remote vault sync
- multi-vault replication
- Notion / Logseq / third-party remote export
- Sigstore or other additional signing layers
- cryptographic receipt expansion beyond the current receipt ledger baseline
- direct `01-Wiki/**` writes
- direct `02-Raw/**` writes
- auto-run `/intake`, `/compile`, `/enrich`, `/query`, or `/lint`
- frontend implementation approval
- bridge code implementation
- vault writer code implementation
- migration scripts
- direct BBDown / Whisper / ffmpeg execution from the H5 layer

This file therefore narrows the candidate surface instead of expanding the
runtime promise.

### §17.6 Acceptance Criteria for Promotion

This amendment may only be promoted when engineering evidence, visual evidence,
and vault-boundary evidence converge.

Required promotion gates:

1. Wave 3A closeout records this candidate without changing the base SRD early.
2. A later Wave 4 walking skeleton proves the future H5 -> Bridge -> authority -> vault path coheres end to end.
3. The H5 direction passes the five-check visual gate in the relevant prototype or implementation review.
4. Vault preview / commit behavior proves the four-field frontmatter and four-section body shape without drifting from the upstream template family.
5. Placeholder or bounded export trials demonstrate stable write-path behavior before any broader runtime claim.
6. The user gives an explicit promotion gate.

Promotion state machine:

```text
candidate_written
  -> wave_3a_closed
  -> walking_skeleton_clear
  -> visual_gate_clear
  -> vault_contract_clear
  -> user_gate_granted
  -> promoted_or_deprecated
```

Failure interpretation:

- if the walking skeleton is technically valid but the visual gate fails, this file stays candidate
- if the vault write path works but drifts from the frontmatter / section contract, this file stays candidate
- if later SRD authority text supersedes these sections, this file becomes deprecated per `sunset_trigger`

Until those gates are satisfied, this file remains a stable candidate reference
for later spec-only work and future implementation dispatches.
