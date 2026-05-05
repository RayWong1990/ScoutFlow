---
title: Wave 5 file-domain matrix draft
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
related_task: T-P1A-128
dispatch_slot: 149
---

# Wave 5 file-domain matrix draft

> State: candidate / not authority / not execution approval / not runtime approval.

## 1. Scope

Create a file-domain matrix that prevents same-file concurrent writers and separates docs, app, authority, bridge, and vault lanes.

## 2. Source Anchors

- `docs/current.md`
- `docs/task-index.md`
- `AGENTS.md`

## 3. Candidate Payload

| Area | Candidate Direction | Blocked Claim | Carry-forward Note |
| --- | --- | --- | --- |
| scope | stay within the named candidate surface only | runtime or migration approval | docs/spec only |
| inputs | reuse current manual-url and metadata-first truth | new source-discovery entrypoint | preserve Phase 1A boundary |
| outputs | prepare later handoff or review structure | live route or DTO change | no schema promotion here |
| gates | record blocked lanes explicitly | silent unlock of BBDown/browser/vault write | defer to later dispatch |

## 4. Boundaries

- Wave 5 file-domain matrix draft remains candidate-only and cannot mutate existing service, DTO, or filesystem contracts.
- When evidence is missing, prefer explicit defer wording over placeholder completeness.
- this file does not approve runtime, migration, package adoption, browser automation, ASR, `audio_transcript`, or vault true write
- this file is allowed to shape later candidate docs/spec work only
