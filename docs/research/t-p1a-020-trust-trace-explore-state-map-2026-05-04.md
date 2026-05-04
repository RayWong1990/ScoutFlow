# T-P1A-020 Trust Trace / Explore State Map

> Status: research / candidate state map. Not authority. Not frontend approval. Not runtime approval.
> Scope: derive an Explore-consumable table from the current Phase 1A Trust Trace DTO without adding fields, opening `apps/`, or weakening media/audio gates.

## 1. Source Contract

- API surface: `GET /captures/{capture_id}/trust-trace`
- Current DTO layers: `capture`, `capture_state`, `metadata_job`, `probe_evidence`, `receipt_ledger`, `media_audio`, `audit`
- Current approved capture input: `platform=bilibili`, `source_kind=manual_url`, `capture_mode=metadata_only`
- Current hard blocker: `media_audio.status=not_approved` and `media_audio.audio_transcript=blocked` in every state below
- Future-only values such as comments, danmaku, screenshots, token counts, cost estimates, media readiness, ASR, and `audio_transcript` runtime stay `<TBD future gate>`

## 2. Explore Input State Table

| Explore state | Trust Trace condition | Primary user meaning | Allowed next API action | Not allowed |
|---|---|---|---|---|
| `empty` | no selected `capture_id` | nothing selected yet | paste manual Bilibili URL through `/captures/discover` | recommendation / keyword / RAW gap direct capture |
| `created` | `capture_state.status=discovered`, `metadata_job.present=false`, `receipt_ledger.present=false` | capture shell exists; no metadata job yet | show `Fetch metadata` button | show media/audio readiness |
| `queued` | `metadata_job.status=queued` | metadata job is queued but has not started | show queued indicator; disable duplicate fetch action | imply platform result exists |
| `running` | `metadata_job.status=running` | metadata fetch is in progress | show loading state; keep trace card visible | show raw stdout/stderr |
| `failed` | `metadata_job.status=failed`, `metadata_job.platform_result!=ok`, `receipt_ledger.present=false` | platform/probe failed safely; capture remains discovered | show retry candidate affordance `<TBD future gate>` | move capture to `metadata_fetched` |
| `metadata_fetched` | `capture_state.status=metadata_fetched`, `metadata_job.status=succeeded`, `receipt_ledger.present=true` | safe metadata evidence is available | show evidence summary and trust trace card | unlock media, ffmpeg, ASR, transcript, comments, danmaku, screenshots |

Merge-gated alignment note: after T-P1A-019 merges with its current non-ok failure receipt path, `failed` is produced by non-ok failure receipt completion from the dry-run orchestrator; no success evidence artifacts are emitted. Until T-P1A-019 is merged and #43 is rebased, this remains a sequencing gate, not independent authority.

## 3. Button State Table

| Explore state | `Fetch metadata` | `Open Trust Trace` | `Use in topic work` | Media / transcript buttons |
|---|---|---|---|---|
| `empty` | disabled until a valid manual URL is submitted | disabled | disabled | hidden / disabled |
| `created` | enabled | enabled | disabled | hidden / disabled |
| `queued` | disabled; label can read `Queued` | enabled | disabled | hidden / disabled |
| `running` | disabled; loading | enabled | disabled | hidden / disabled |
| `failed` | disabled or retry-candidate only `<TBD future gate>` | enabled | disabled | hidden / disabled |
| `metadata_fetched` | disabled or replay-safe | enabled | candidate enabled for metadata-only planning `<TBD future gate>` | hidden / disabled |

## 4. Trust Trace Card Mapping

| Card row | DTO source | Display rule |
|---|---|---|
| Capture | `capture.platform`, `capture.platform_item_id`, `capture.source_kind`, `capture.capture_mode` | show stable source facts only |
| Capture state | `capture_state.status` | show `discovered` or `metadata_fetched`; do not show future lifecycle as current |
| Metadata job | `metadata_job.present/status/platform_result` | show `queued/running/failed/succeeded`; only show `platform_result` after completion |
| Probe evidence | `probe_evidence.present/probe_mode/source_task_id/source_report_path/platform_result` | show safe evidence provenance; no raw response fields |
| Receipt ledger | `receipt_ledger.present/artifact_count/artifact_kinds/redaction` | show artifact count and approved artifact kinds only |
| Media/audio | `media_audio.status/audio_transcript` | always show blocked/not approved in Phase 1A |
| Audit | `audit.redaction_policy`, `audit.safe_parsed_fields`, `audit.evidence_file_path` | show safe parsed fields; no stdout/stderr/cookie/token/signed URL |

## 5. Error / Empty / Risk States

| Condition | Explore treatment | Boundary |
|---|---|---|
| invalid or missing `capture_id` | empty or not-found panel | no implicit capture creation |
| `capture_not_found` | not-found panel with manual URL entry | do not scan sources |
| `trust_trace_source_kind_not_allowed` | scope-gate error | recommendation / keyword / RAW gap cannot bypass LP-001 |
| `metadata_job.status=failed` | safe failure panel with `platform_result` | do not promote to receipt ledger |
| `receipt_ledger.present=false` | hide evidence summary; show status trace | do not claim metadata evidence exists |
| `media_audio.status=not_approved` | keep media/transcript controls disabled | no media / ffmpeg / ASR / `audio_transcript` runtime |
| future fields requested by UI | render as `<TBD future gate>` | no current DTO or authority expansion |

## 6. Candidate UI State Machine

```text
empty
  -> created
  -> queued
  -> running
  -> failed
  -> created
  -> queued
  -> running
  -> metadata_fetched
```

Transition gates:

- `empty -> created`: only `POST /captures/discover` with approved manual Bilibili metadata-only input
- `created -> queued`: only `POST /captures/{capture_id}/metadata-fetch/jobs`
- `queued -> running`: worker/orchestrator claim path `<TBD future gate>`
- `running -> failed`: non-ok `PlatformResult` through receipt completion
- `running -> metadata_fetched`: ok metadata receipt with approved artifact kinds
- `metadata_fetched -> media/audio`: blocked until a separate future dispatch approves runtime

## 7. T-P1A-020 Self-Audit Notes

- No new capture scope enum is proposed.
- No `audio_transcript` runtime is proposed.
- No cost estimate, token count, comments, danmaku, screenshot, media, ffmpeg, ASR, worker, or frontend implementation is proposed.
- This table is intended for Explore prototype consumption only after PR review and human check.
