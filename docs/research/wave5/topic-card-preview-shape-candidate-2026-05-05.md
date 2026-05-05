---
title: Topic Card Preview Shape Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-125
dispatch_slot: 146
---

# Topic Card Preview Shape Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Bounded Capture Station preview candidate that exposes topic-card review structure without backend runtime coupling or shell wiring changes.

## 2. Source Anchors

- `docs/research/wave5/topic-card-entity-surface-candidate-2026-05-05.md`
- `docs/research/wave5/topic-card-review-flow-candidate-2026-05-05.md`
- `docs/research/wave5/topic-card-vault-rendering-candidate-2026-05-05.md`
- `docs/visual/h5-capture-station/design-brief.md`

## 3. Candidate Surface

| Surface | Candidate Role | What It Shows | Boundary |
| --- | --- | --- | --- |
| preview header | anchor the card quickly | title, hypothesis summary, review state, export posture | not a final verdict |
| metric row | show review vocabulary in compact form | strength / coverage / risk as candidate labels | not a scoring engine |
| counter-evidence block | keep caution visible | missing screenshot or human verdict | not a reject by itself |
| review flow rail | expose manual review stages | intake, evidence review, retain/defer | not an automated workflow |

## 4. Visual Review Notes

- The preview should feel like a dense operator card, not a marketing tile or content feed item.
- Counter-evidence must remain visible even when the card headline looks strong.
- Screenshot evidence remains deferred; any visual pass still needs a later authorized review packet.

## 5. Boundaries

- This candidate does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write.
- The component is intentionally unmounted from the current four-panel shell and exists as a bounded preview reference only.
- Follow-up work may reuse the shape, but it must still pass a later internal audit before any merge-readiness or IA promotion claim.
