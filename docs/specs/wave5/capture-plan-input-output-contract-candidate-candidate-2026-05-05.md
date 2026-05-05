---
title: Capture-Plan Input Output Contract Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-121
dispatch_slot: 142
---

# Capture-Plan Input Output Contract Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Docs-only contract sketch for capture-plan inputs and outputs without enabling execution.

## 2. Source Anchors

- `docs/PRD-v2-2026-05-04.md`
- `docs/SRD-v2-2026-05-04.md`
- `docs/research/wave5/capture-plan-entity-surface-candidate-2026-05-05.md`

## 3. Candidate Payload

| Side | Field | Meaning | Constraint |
| --- | --- | --- | --- |
| input | source references | what evidence or signals the plan draws from | must support current manual-url truth |
| input | scope note | what the plan is trying to cover | cannot imply runtime execution |
| output | plan summary | operator-readable plan body | docs-only candidate |
| output | defer reasons | why execution is blocked or postponed | must stay explicit |

## 4. Boundaries

- This contract is preparation-only.
- No `POST /capture-plans` runtime approval is implied.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
