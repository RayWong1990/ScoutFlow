---
title: T-P1A-024 Explore / Capture Scope Wireframe + State Table
date: 2026-05-04
owner_tool: codex-desktop
status: candidate-research-note
not_authority: true
not_frontend_implementation: true
not_runtime_approval: true
not_schema_authority: true
prototype_local_path: "/Users/wanglei/workspace/scoutflow-prototypes/explore-capture-scope/index.html"
prototype_sha256: "f65a3bc39fe2d33bbea0f5768987cda96d373200761bb13aeeda508bcaf0606b"
depends_on:
  - T-P1A-017 merged via PR #36
  - T-P1A-020 not merged at authoring time; DTO hardening fields marked TBD
allowed_repo_path: "docs/research/t-p1a-024-explore-capture-scope-state-table-2026-05-04.md"
---

# 1. Boundary

This note is a candidate Explore / Capture Scope interaction packet. It is not authority, not a frontend implementation approval, not schema authority, and not runtime approval.

Repo-side scope is only this research note. The wireframe HTML is local-only and outside the repo:

```text
/Users/wanglei/workspace/scoutflow-prototypes/explore-capture-scope/index.html
```

The wireframe uses only placeholder sample data:

- URL placeholder: `https://example.bilibili.com/video/BV1xxx111xxx`
- BV placeholder: `BV1xxx111xxx`
- UP placeholder: `示例UP-001`
- No real Bilibili URL, cookie, token, account screenshot, QR image, signed URL, or platform request.

Current authority sources used:

- [docs/current.md](../current.md)
- [docs/task-index.md](../task-index.md)
- [docs/PRD-v2-2026-05-04.md](../PRD-v2-2026-05-04.md)
- [docs/SRD-v2-2026-05-04.md](../SRD-v2-2026-05-04.md)
- [docs/research/t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md](./t-p1a-007-explore-url-ux-brainstorm-2026-05-03.md)

# 2. Wireframe Intent

The prototype frames Explore as a capture intent confirmation surface:

```text
empty
  -> local validation
  -> preview candidate
  -> metadata_only capture decision
  -> receipt / Trust Trace follow-up
```

The screen separates two user intents:

| User intent | UI copy | Current behavior |
|---|---|---|
| Try / inspect locally | `试一下` | local placeholder BV validation only; no capture creation |
| Create current approved capture | `只采 metadata` | the only enabled creation-style action in the wireframe |
| Evaluate future audio lane | `评估 audio_transcript` | disabled / blocked; evaluation copy only |
| Plan non-manual sources | `打开 Scope` | required for recommendation / keyword / RAW gap |

# 3. Candidate State Machine

This is a UI candidate state machine, not an API state contract.

```text
empty
  -> local_url_parsed
    -> invalid_url
    -> unsupported_url_type
    -> preview_ready_manual_low_risk
      -> capture_created_metadata_only
        -> metadata_fetch_running
        -> metadata_fetched
        -> metadata_failed
    -> preview_ready_non_manual_scope_required
    -> preview_ready_manual_probe_blocked
    -> parser_drift_blocked
```

Transition rules:

| From | To | Gate | Notes |
|---|---|---|---|
| `empty` | `local_url_parsed` | user provides placeholder URL/BV | local only; no platform request |
| `local_url_parsed` | `invalid_url` | unsupported host, scheme, or missing BV shape | local validation only |
| `local_url_parsed` | `preview_ready_manual_low_risk` | `source_kind=manual_url` and local BV parse clears | candidate preview; no capture yet |
| `preview_ready_manual_low_risk` | `capture_created_metadata_only` | user explicitly chooses `metadata_only` | current approved quick capture action |
| `local_url_parsed` | `preview_ready_non_manual_scope_required` | `recommendation / keyword / raw_gap` context | LP-001 gate; no direct capture |
| `preview_ready_manual_low_risk` | `preview_ready_manual_probe_blocked` | future probe returns `auth_required / vip_required / region_blocked / forbidden` | adapter/probe evidence only; not guessed locally |
| any probe/adapter state | `parser_drift_blocked` | parser drift or required field missing | repair gate; not a soft success |

# 4. Candidate UI State Table

| State | capture created? | Primary action | Secondary action | Right panel label | Allowed now? | Boundary |
|---|---:|---|---|---|---|---|
| `empty` | no | disabled | none | `Status / Trust Trace` | yes, UI idle only | no capture, no probe |
| `local_url_parsed` | no | disabled | none | `Status / Trust Trace` | candidate | local parse shell only |
| `invalid_url` | no | none | fix hint | `Status / Trust Trace` | candidate | no platform claim |
| `unsupported_url_type` | no | none | fix hint | `Status / Trust Trace` | candidate | Bilibili non-video stays blocked |
| `preview_ready_manual_low_risk` | no | `只采 metadata` | `评估 audio_transcript` disabled | `Status / Trust Trace` | candidate | preview does not create capture |
| `preview_ready_non_manual_scope_required` | no | `打开 Scope` | `查看详情` | `Status / Trust Trace` | candidate | recommendation / keyword / RAW gap cannot direct capture |
| `preview_ready_manual_probe_blocked` | no | disabled | `打开 Scope` | `Status / Trust Trace` | future TBD | requires probe evidence; no local guessing |
| `capture_created_metadata_only` | yes | `复制审计块` | `查看状态` | `Receipt / Ledger Trace` | current-approved concept | only after `/captures/discover` style creation |
| `metadata_fetch_running` | yes | `查看状态` | failure detail when available | `Receipt / Ledger Trace` | current/future mixed | API job fields remain authority |
| `metadata_fetched` | yes | `复制审计块` | `复制脱敏专业审计块` | `Receipt / Ledger Trace` | current/future mixed | receipt exists; no media/audio implication |
| `metadata_failed` | yes | `查看错误` | `打开 Scope` | `Receipt / Ledger Trace` | current/future mixed | failure state must not auto-expand runtime |
| `parser_drift_blocked` | yes/no | none | repair note / scope | context-dependent | candidate | stop-the-line style repair gate |

# 5. Field Status Table

| UI field / concept | Current status | Authority source | Wireframe treatment |
|---|---|---|---|
| `platform=bilibili` | current approved for Phase 1A | PRD/SRD v2 + API baseline | implicit platform label |
| `source_kind=manual_url` | current approved quick capture source | PRD/SRD v2 | selector default |
| `quick_capture_preset=metadata_only` | current approved preset | PRD/SRD v2 + API baseline | only enabled creation-style action |
| `canonical_url` | current API input, but wireframe sample is placeholder only | API baseline | placeholder URL only |
| `platform_item_id` / BV | current parsed identity concept | API baseline | placeholder `BV1xxx111xxx` only |
| `capture_id` | current after capture creation | API baseline | not shown before capture creation |
| `capture_mode=metadata_only` | current capture mode | storage/API baseline | label only; no schema change |
| Trust Trace layers: `capture`, `capture_state`, `metadata_job`, `probe_evidence`, `receipt_ledger`, `media_audio`, `audit` | current safe surface from SRD v2; T-P1A-020 hardening not merged | SRD v2 / T-P1A-013 baseline | shown as cards; detailed DTO fields `<TBD per T-P1A-020>` |
| title / UP / duration / page count | future preview/probe display fields | adapter/probe evidence, not local validation | placeholder values only |
| `auth_required / vip_required / region_blocked / forbidden` | future risk states from probe/adapter evidence | Platform risk contract direction | risk chips only; never guessed from URL |
| `parser_drift` | stop-line style repair state | platform adapter risk direction | blocked state, not a warning-only success |
| `audio_transcript` | blocked / not approved | PRD/SRD v2 | disabled `评估 audio_transcript` button |
| comments / danmaku / screenshot | not current scope | PRD/SRD v2 boundaries | not enabled; listed as out of action scope |
| cost estimate | future TBD | no current formula | no final cost formula; do not show numeric estimate |

# 6. Wireframe Surface Inventory

The external HTML prototype contains:

- URL input with placeholder-only BV validation.
- `manual_url / recommendation / keyword / raw_gap` source selector.
- Current enabled `metadata_only` card and blocked `audio_transcript` card.
- Primary action copy `只采 metadata`.
- Disabled action copy `评估 audio_transcript`.
- Metadata preview placeholder with fake title, fake UP, fake BV, and no real media.
- Trust Trace 7-layer card stack using current layer names.
- Empty, invalid, scope-required, low-risk, blocked, and risk-state representations.
- Scope table marking metadata current, audio blocked, comments/danmaku/screenshot out of scope, cost estimate future TBD.

It does not contain:

- frontend app code under `apps/`
- screenshots committed to repo
- real Bilibili URL or real BV sample
- cookie / token / signed URL / account information
- BBDown / yt-dlp / ffmpeg / ASR execution
- API calls, browser automation, or platform requests

# 7. Open Brainstorm Questions

These are the user-review questions before any future frontend implementation:

| Question | Candidate fork |
|---|---|
| Should URL input split `试一下` and formal capture intent? | Current wireframe says yes: `试一下` is local preview, `只采 metadata` is creation intent. |
| Should Trust Trace 7 layers be collapsed or flat? | Current wireframe uses flat cards; future UI may collapse after the user understands the structure. |
| When should cost estimate appear? | Current note says no final formula; future cost may appear only inside an audio evaluation gate. |
| How strong should the disabled audio affordance be? | Current wireframe uses visible disabled button plus blocked card; hiding it may reduce discovery but avoids false readiness. |
| Should VIP / region / parser drift share one error container? | Current wireframe keeps a shared risk area plus typed tags; parser drift remains repair-gate language. |

# 8. Shared 5-Part Self-Audit

1. Scope check - repo change should remain this single `docs/research/` note; prototype HTML stays outside the repo at `prototype_local_path`.
2. Authority check - no PRD, SRD, locked principles, contracts index, task index, current pointer, schema, code, or tests should be changed by this lane.
3. Safety check - placeholder-only data; no credentials; no real platform URL; no raw response; `audio_transcript` remains blocked; comments/danmaku/screenshot are not enabled.
4. Validation result - T-PASS scoped to docs/prototype static validation:
   - `python tools/check-docs-redlines.py`
   - `python tools/check-secrets-redlines.py`
   - `python -m pytest tests/api tests/contracts -q` -> `109 passed`
   - `git diff --check`
   - `git ls-files | rg '^(data|referencerepo|example|examples)/'` -> no tracked matches
   - `find . -maxdepth 1 ...` forbidden root dirs -> no matches
   - prototype SHA256 recorded in frontmatter
   - no `www.bilibili.com` / credential-token patterns in the prototype or this note
   - no `开始 audio_transcript` / current-enabled comments-danmaku-screenshot wording in the prototype or this note
5. Next gate - user review of wireframe + state table; future frontend implementation still needs a separate lane and visual 5-gate self-audit.
