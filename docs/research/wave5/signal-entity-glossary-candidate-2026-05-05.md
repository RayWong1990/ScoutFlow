---
title: Signal Entity Glossary Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-110
dispatch_slot: 131
---

# Signal Entity Glossary Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Candidate vocabulary for Wave 5 signal-facing product docs and future contracts.

## 2. Source Anchors

- `docs/PRD-v2-2026-05-04.md`
- `docs/SRD-v2-2026-05-04.md`
- `docs/research/repairs/backbone-taxonomy-2026-05-05.md`

## 3. Candidate Payload

| Term | Candidate Meaning | Source Layer | Boundary |
| --- | --- | --- | --- |
| signal | a reusable pattern or observation extracted from capture evidence | PRD Phase 2 entity outline | not a live DB row yet |
| signal cluster | operator grouping of related signals for review | Wave 5 candidate docs | UI-only concept until later contract |
| signal status | candidate lifecycle marker such as draft / reviewed / deferred | Wave 5 docs candidate | must not mutate current Phase 1A state words |
| signal source set | the evidence bundle a signal can cite | capture + trust-trace carry-forward | no direct runtime fetch implied |

## 4. Boundaries

- The glossary exists to reduce term drift across Wave 5 docs.
- Terms here are candidate language, not promoted authority or API schema.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
