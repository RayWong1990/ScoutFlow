---
title: Signal State Map Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-111
dispatch_slot: 132
---

# Signal State Map Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Candidate state progression for signals without mutating current repo state words.

## 2. Source Anchors

- `docs/SRD-v2-2026-05-04.md`
- `docs/current.md`
- `docs/research/wave5/signal-entity-glossary-candidate-2026-05-05.md`

## 3. Candidate Payload

| Candidate State | Meaning | Entry Gate | Exit Gate |
| --- | --- | --- | --- |
| draft | raw signal is proposed but not yet normalized | capture evidence is present | operator promotes to mapped |
| mapped | signal has explicit relation to hypothesis or topic-card surface | basic glossary alignment complete | evidence sufficiency review |
| reviewed | operator has checked wording and evidence fit | manual review happened | either retain or defer |
| deferred | useful idea but not merge-ready for current pack | review finds missing proof or overflow pressure | future wave or overflow registry |

## 4. Boundaries

- These names are Wave 5 candidate states only.
- They must not be mistaken for current Capture / Job / PlatformResult state vocabulary.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
