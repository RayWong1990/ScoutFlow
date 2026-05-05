---
title: Capture Plan Entity Surface Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-113
dispatch_slot: 134
---

# Capture Plan Entity Surface Candidate

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Future-facing entity surface for capture-plan docs without opening runtime or migration work.

## 2. Source Anchors

- `docs/PRD-v2-2026-05-04.md`
- `docs/SRD-v2-2026-05-04.md`
- `docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md`

## 3. Candidate Payload

| Field | Candidate Meaning | Source | Non-goal |
| --- | --- | --- | --- |
| plan_id | stable plan handle for later review surfaces | PRD Phase 2 outline | not a current DB key |
| scope | what sources or entities the plan covers | manual-url continuity + signal chain | not an auto-crawl request |
| budget note | qualitative cost/scope warning | future planning layer | not a billing engine |
| review outcome | manual accept / defer / revise signal | operator review lane | not a background worker action |

## 4. Boundaries

- Capture-plan language should stay upstream of runtime execution.
- A plan can exist as a docs object before any future API route is approved.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
