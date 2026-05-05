---
title: Global pool staging health-check contract
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-150
dispatch_slot: 171
---

# Global pool staging health-check contract

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Define health checks required before increasing the pool from phase 3a to phase 3b.

## 2. Source Anchors

- `docs/current.md`
- `docs/task-index.md`
- `AGENTS.md`

## 3. Candidate Payload

| Area | Candidate Role | Blocked Claim | Carry-forward Note |
| --- | --- | --- | --- |
| artifact shape | structured note or schema candidate | execution approval | candidate docs only |
| evidence floor | ground claims in current authority and prior dispatch outputs | fresh runtime proof | manual readback first |
| defer path | capture missing proof and blocked lanes explicitly | silent omission of risk | feed later batch audit |
| handoff | use dispatch slots and task IDs only | live PR or branch references | keep recovery deterministic |

## 4. Boundaries

- Global pool staging health-check contract should stay upstream of runtime, migration, and package decisions.
- Candidate language must keep current blocked lanes visible instead of smoothing them away.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
