---
title: Topic Card Vault Rendering Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-124
dispatch_slot: 145
---

# Topic Card Vault Rendering Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Bounded Capture Station candidate for rendering a topic-card-shaped markdown bundle without enabling vault write or backend runtime coupling.

## 2. Source Anchors

- `docs/research/wave5/topic-card-entity-surface-candidate-2026-05-05.md`
- `docs/research/wave5/trust-trace-to-topic-card-mapping-candidate-2026-05-05.md`
- `docs/visual/h5-capture-station/design-brief.md`

## 3. Candidate Surface

| Surface | Candidate Role | What It Shows | Boundary |
| --- | --- | --- | --- |
| header block | orient the operator quickly | title, hypothesis summary, export posture, gate chip | not a publish action |
| evidence balance | keep support / process / counter evidence visible together | stance-tagged rows for proof and counter-proof | no hidden fetch or derived score engine |
| markdown preview | show the bundle shape before any write step | note path + markdown-like preview body | not a live vault preview route |
| footer gate | preserve current phase truth | `write_disabled` and `deferred_visual_evidence` wording | not screenshot proof |

## 4. Visual Review Notes

- The component should read as an operator review surface, not a promotional card.
- Evidence and counter-evidence must stay on screen at the same time so the card does not overclaim confidence.
- Screenshot evidence remains deferred; manual visual review is still required before treating the surface as visually clear.

## 5. Tracked Scope Note

- allowed app path: `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx`
- allowed app path: `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.test.tsx`
- this note is the tracked dispatch scope note for the current app diff; historical app surfaces do not expand scope beyond the two files above

## 6. Boundaries

- This candidate does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write.
- The component is intentionally unmounted from the current four-panel shell and exists as a bounded feature candidate only.
- Follow-up work may reuse the surface as a reference, but must still pass a later internal audit before merge-readiness claims.
