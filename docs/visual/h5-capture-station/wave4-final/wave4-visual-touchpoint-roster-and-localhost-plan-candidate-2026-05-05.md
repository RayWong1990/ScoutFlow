---
title: Wave 4 Visual Touchpoint Roster and Localhost Plan
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-107
dispatch_slot: 128
---

# Wave 4 Visual Touchpoint Roster and Localhost Plan

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Wave 4 visual review surface inventory after the mid checkpoint; docs-only and manual-review-first.

## 2. Source Anchors

- `docs/current.md`
- `docs/visual/h5-capture-station/design-brief.md`
- `docs/research/repairs/backbone-taxonomy-2026-05-05.md`

## 3. Candidate Payload

| Surface | Current Truth | Manual Review Focus | Deferred Evidence |
| --- | --- | --- | --- |
| URL Bar | static panel landed | scan order, long-URL stability, blocked-vs-ready copy | screenshots still gated |
| Live Metadata | fixture-only surface landed | evidence density, empty-state honesty, label clarity | screenshots still gated |
| Capture Scope | blocked future layers remain visible | state hierarchy, blocked styling, future-lane downgrade | screenshots still gated |
| Trust Trace | graph surface landed as deep inspection zone | node emphasis, reading path, blocked downstream hints | screenshots still gated |
| Vault Preview / Commit placeholders | landed as placeholder-only surfaces | truthful gating copy, non-live posture, no fake readiness | browser/runtime still gated |

## 4. Boundaries

- Localhost review remains a manual roster, not an authorization to run browser automation.
- Every visual touchpoint must preserve the operator-workstation posture from the design brief.
- Any future screenshot pack must separate static layout proof from runtime proof and human visual verdict.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only

## 5. Visual Review Note

- visual review required
- screenshot generation remains separately gated; if still blocked, record `deferred_visual_evidence`
- keep desktop / tablet / mobile expectations in the manual review lane, not as fake completed artifacts

## 6. Localhost Review Plan

- step 1: use the current `apps/capture-station` build target only after the repo branch already proves type/build/test truth
- step 2: review the first viewport in desktop order, then tablet stacking, then mobile linearization
- step 3: record findings by surface using `visual hierarchy / spacing / blocked-state honesty / scan path / readability`
- step 4: if browser automation remains gated, keep the result as manual-review-only and carry `deferred_visual_evidence`
