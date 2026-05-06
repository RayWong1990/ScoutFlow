---
title: PF-C1 Three-URL Preview Proof Set
status: candidate / proof / not-authority
created_at: 2026-05-06
related_dispatch: PF-C1-07
proof_kind: real_url_preview
runtime_mode: localhost_http
verdict: pass
---

# PF-C1 Three-URL Preview Proof Set

## Summary

All three locked canary URLs produced:

- `POST /captures/discover` capture truth
- `GET /captures/{capture_id}/vault-preview` preview JSON
- preview markdown extracted from `body_markdown`
- `topic-card-lite` JSON constrained to the `PF-C1-02` field contract

This proves the current preview-only bridge path can generate bounded proof artifacts from real canary URLs without enabling true write.

## Artifact Set

| Slot | Capture ID | Preview MD | Topic-Card-Lite | Result |
| --- | --- | --- | --- | --- |
| `ordinary` | `01KQYY9KP26SSZA6285MAY706S` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-ordinary-preview-01KQYY9KP26SSZA6285MAY706S.md` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-ordinary-card-01KQYY9KP26SSZA6285MAY706S.json` | `generated` |
| `edge` | `01KQYY9KREQS9BVRZWVJ4N0DVB` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-edge-preview-01KQYY9KREQS9BVRZWVJ4N0DVB.md` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-edge-card-01KQYY9KREQS9BVRZWVJ4N0DVB.json` | `generated` |
| `high-signal` | `01KQYY9KT8WSQRAH1T2B2DPHVA` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-high-signal-preview-01KQYY9KT8WSQRAH1T2B2DPHVA.md` | `docs/research/post-frozen/proof-artifacts/run-3-c1-07/URL-high-signal-card-01KQYY9KT8WSQRAH1T2B2DPHVA.json` | `generated` |

## Observed Shape

- Each preview markdown stayed inside the bridge preview boundary:
  - `preview_only=true`
  - `write_enabled=false`
  - `runtime_tools_enabled=false`
- Each `topic-card-lite` JSON stayed inside the `6`-field contract:
  - `title`
  - `platform_item_id`
  - `canonical_url`
  - `capture_id`
  - `export_posture`
  - `target_path`

## What This Does Not Prove

- It does not prove human usefulness.
- It does not prove RAW handoff.
- It does not prove visual quality.
- It does not approve true vault write, browser automation, or any runtime beyond the current preview-only localhost loop.
