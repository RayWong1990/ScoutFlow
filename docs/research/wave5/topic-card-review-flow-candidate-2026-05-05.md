---
title: Topic-Card Review Flow Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-120
dispatch_slot: 141
---

# Topic-Card Review Flow Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Candidate review flow for topic-card shaping and defer/retain decisions.

## 2. Source Anchors

- `docs/research/wave5/topic-card-entity-surface-candidate-2026-05-05.md`
- `docs/research/wave5/trust-trace-to-topic-card-mapping-candidate-2026-05-05.md`
- `docs/current.md`

## 3. Candidate Payload

| Stage | Operator Question | Output | Deferred If |
| --- | --- | --- | --- |
| intake | does the card have enough grounded metadata? | candidate card shell | core evidence missing |
| evidence review | is the proof chain understandable? | mapped evidence set | trust trace is ambiguous |
| narrative tightening | is the title/hypothesis honest? | reviewable copy | claim drifts beyond proof |
| retain or defer | should this stay in Wave 5? | retained/deferred status | overflow or missing future proof |

## 4. Boundaries

- Review flow remains manual-first.
- A deferred result is valid and should not be presented as a failure.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
