---
title: Signal Scoring Vocabulary Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-122
dispatch_slot: 143
---

# Signal Scoring Vocabulary Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Vocabulary note for talking about signal strength without pretending a scoring engine already exists.

## 2. Source Anchors

- `docs/research/wave5/signal-entity-glossary-candidate-2026-05-05.md`
- `docs/research/wave5/hypothesis-evidence-source-matrix-2026-05-05.md`
- `docs/current.md`

## 3. Candidate Payload

| Term | Candidate Use | Should Mean | Should Not Mean |
| --- | --- | --- | --- |
| strength | how much support a signal currently has | evidence sufficiency | product success probability |
| coverage | breadth of evidence sources | how many proof surfaces are present | runtime completeness |
| novelty | whether the signal adds something new | operator differentiation cue | automatic quality score |
| risk | likelihood the signal is misleading or under-proven | review caution | hard reject by itself |

## 4. Boundaries

- Vocabulary only; no scoring algorithm or metric threshold is approved.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
