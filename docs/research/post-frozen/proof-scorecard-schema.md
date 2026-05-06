---
title: Proof scorecard schema
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-04
---

# Proof scorecard schema

## schema

```yaml
scorecard_version: v0
artifact_id: required
scope_class: preview_only | docs_only | raw_intake | screenshot_visual
source_class: doc | localhost | fixture | human_review | github_truth
proof_shape_present: true | false
human_gate_required: true | false
human_gate_state: none | pending | pass | fail
blocked_claims_intact: true | false
runtime_unlock_claimed: true | false
notes: list
```

## scoring_guidance

| dimension | pass_bar | red_flag |
|---|---|---|
| provenance | source class explicit | source hidden behind generic `evidence` |
| proof shape | required fields present | doc exists but shape missing |
| human gate | pending/pass separated | screenshots used as final verdict |
| blocked claims | all remain blocked | wording implies runtime unlock |
| boundary scope | allowed paths respected | authority or runtime paths touched |

## usage_note

- This schema is meant for cross-PR comparison, not for ranking products.
- Prefer `verdict + note` over fake numeric certainty when the gate is human-dependent.

## verdict

- `T-PASS` means the schema is ready for candidate use in audit packets.
