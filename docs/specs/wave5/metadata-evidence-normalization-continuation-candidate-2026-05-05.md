---
title: Metadata Evidence Normalization Continuation
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-118
dispatch_slot: 139
---

# Metadata Evidence Normalization Continuation

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Continuation note for normalizing metadata evidence into later candidate docs without inventing new runtime fields.

## 2. Source Anchors

- `docs/SRD-v2-2026-05-04.md`
- `docs/research/repairs/backbone-taxonomy-2026-05-05.md`
- `docs/research/wave5/trust-trace-to-topic-card-mapping-candidate-2026-05-05.md`

## 3. Candidate Payload

| Normalization Rule | Keep | Avoid |
| --- | --- | --- |
| identity | carry `capture_id`, canonical URL, and platform item identity together | splitting the same proof into unrelated labels |
| provenance | preserve which layer produced the fact | flattening all evidence into one confidence bucket |
| empties | use explicit missing/blocked wording | fake placeholder completion |
| future docs | derive candidate docs from normalized evidence summaries | directly implying runtime proof or manual verdict |

## 4. Boundaries

- This note governs wording and structure only.
- No new DTO, enum, or storage contract is approved here.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
