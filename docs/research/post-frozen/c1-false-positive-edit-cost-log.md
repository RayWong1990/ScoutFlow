---
title: PF-C1 False-Positive and Edit-Cost Log
status: candidate / audit / not-authority
created_at: 2026-05-06
related_dispatch: PF-C1-09
proof_kind: human_verdict
---

# PF-C1 False-Positive and Edit-Cost Log

## Summary

The current `topic-card-lite` path is useful enough to keep moving, but it still over-compresses source meaning into a very thin metadata shell. The main risk is not factual corruption; it is usefulness inflation.

## Findings

| Slot | False-positive / edit-cost risk | Why it matters | Edit cost |
| --- | --- | --- | --- |
| `ordinary` | title-only card may look more semantically rich than it really is | current preview only preserves `capture_id / BV / canonical_url / target_path`; no content semantics, uploader, duration, or tags survive into the card | `medium` |
| `edge` | over-objectification risk is highest here | the card shape can imply “reviewable topic” even when the source signal may still be weak or noisy | `high` |
| `high-signal` | strongest downstream potential, but still thin | the slot is likely worth carrying, yet the proof artifact still reads more like a bounded intake container than a true insight card | `medium` |

## Structural Cost Notes

1. `title = ScoutFlow {BV}` is stable but semantically weak.
2. `export_posture = handoff_candidate` is doing important honesty work; removing it would overclaim readiness.
3. `target_path` helps handoff traceability, but if shown too prominently it can make the card feel operational rather than informative.

## Decision Use

- This log does not overturn the human `pass`.
- It explains why the user marked all three rows `needs-edit` rather than `follow`.
- If `PF-C1` is revisited later, the next improvement priority is not visual polish; it is adding one or two low-risk semantic fields without turning the object into a full workbench.
