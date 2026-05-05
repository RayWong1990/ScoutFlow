---
title: Topic Card Entity Surface Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-114
dispatch_slot: 135
---

# Topic Card Entity Surface Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Candidate entity surface for topic-card docs and bounded UI exploration.

## 2. Source Anchors

- `docs/PRD-v2-2026-05-04.md`
- `docs/visual/h5-capture-station/design-brief.md`
- `docs/research/wave5/hypothesis-lifecycle-candidate-2026-05-05.md`

## 3. Candidate Payload

| Field | Candidate Role | Visual Weight | Boundary |
| --- | --- | --- | --- |
| title | operator-readable narrative headline | high | must stay grounded in evidence |
| hypothesis summary | what claim the card is testing | high | not final truth |
| evidence links | proof and counter-proof references | medium | no hidden runtime fetch |
| export posture | whether the card is still local-only or handoff-ready | medium | not a publish action |

## 4. Boundaries

- Topic card is a review surface, not a marketing tile.
- The entity shape must support both evidence and counter-evidence.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
