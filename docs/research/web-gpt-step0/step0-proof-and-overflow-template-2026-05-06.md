---
title: STEP0 Proof And Overflow Template
status: candidate / research / not-authority
created_at: 2026-05-06
---

# STEP0 Proof And Overflow Template

## 1. Purpose

This template exists to keep `C1/C2 proof lanes` and `O1 overflow lanes` from being mixed together.

## 2. C1/C2 proof lanes

Use for:

- real URL canary pack
- topic-card-lite contract
- human usefulness verdict
- RAW note candidate
- intake acceptance
- script seed proof

Required posture:

```yaml
dispatch_class: proof_mainline | proof_prep
cluster: PF-C1 | PF-C2
proof_kind: real_url_preview | human_verdict | raw_intake | script_seed
```

Minimum rule:

- `candidate doc` is not proof
- `placeholder` is not proof
- `preview` without human verdict is not proof
- `manual transfer` without intake/seed is not proof

## 3. O1 overflow lanes

Use for:

- DBvNext
- migrations
- BBDown live
- ASR / `audio_transcript`
- browser automation
- true vault write
- full Signal Workbench

Required posture:

```yaml
dispatch_class: overflow
cluster: PF-O1
proof_kind: none
human_gate: true_write_approval | visual_verdict | explicit_runtime_approval
```

## 4. Reopen conditions

Every overflow item must include:

| Field | Requirement |
|---|---|
| `blocked_reason` | why it is not on the mainline now |
| `reopen_condition` | what proof or human gate is needed |
| `kill_switch_ref` | which kill switch prevents accidental promotion |

## 5. Hard rule

If a task touches runtime, migration, browser automation, or true write but does not name an explicit reopen condition, it is malformed and should not be treated as mainline-ready.

