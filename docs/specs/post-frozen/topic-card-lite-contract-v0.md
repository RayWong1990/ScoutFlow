---
title: Topic-Card-Lite Contract v0
status: candidate / contract / not-authority
created_at: 2026-05-06
related_dispatch: PF-C1-02
proof_kind: shape_only
---

# Topic-Card-Lite Contract v0

## Purpose

Define the smallest field set that lets `PF-C1` prove preview usefulness without sliding into a full Signal Workbench, ranking engine, or final knowledge-card schema.

## Contract

`topic-card-lite` is a review object, not a publish object. Field count stays at `6`.

| Field | Type | Required | Meaning | Notes |
| --- | --- | --- | --- | --- |
| `title` | string | yes | Human-readable preview title | Usually comes from bridge preview frontmatter title or `ScoutFlow {platform_item_id}` fallback. |
| `platform_item_id` | string | yes | Platform-native item id | For current C1 scope this is the bilibili BV id. |
| `canonical_url` | string | yes | Canonical source URL | Query strings stripped before proof artifacts are written. |
| `capture_id` | string | yes | Capture identity from `POST /captures/discover` | Keeps proof tied to existing capture truth. |
| `export_posture` | enum | yes | `local_only` or `handoff_candidate` | Current C1 proof should land as `handoff_candidate`, not publish-ready. |
| `target_path` | string | yes | Candidate note path from bridge preview | May point to a future inbox target, but does not approve true write. |

## Explicit Non-Goals

The following are intentionally excluded from `topic-card-lite v0`:

- ranking
- score
- explanation engine
- recommendation strength
- full tag taxonomy
- downstream publish state
- any field that implies human creative judgment is already complete

## Allowed Source Inputs

- `CreateCaptureResponse` from `POST /captures/discover`
- `BridgeVaultPreviewResponse` from `GET /captures/{capture_id}/vault-preview`

## Guardrail

- `topic-card-lite` must remain readable when only machine-visible preview truth exists.
- If a future change needs more than these `6` fields, it should be treated as a new contract revision, not silently appended here.
