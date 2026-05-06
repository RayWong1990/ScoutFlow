---
title: PR review checklist for preview-only tasks
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-GLOBAL-03
---

# PR review checklist for preview-only tasks

## review_table

| check | question | fail_if |
|---|---|---|
| boundary truth | Does the PR keep `preview-only` explicit? | wording implies runtime or true-write unlock |
| provenance | Are evidence sources named as doc, fixture, localhost, or human review? | source class is hidden or collapsed |
| blocked claims | Are runtime, migration, browser automation, and ASR still blocked? | any blocked lane is softened |
| placeholder discipline | Are placeholder, fixture, and dry-run outputs labeled honestly? | placeholder is treated as product proof |
| authority drift | Does the PR avoid `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `AGENTS.md`? | authority files are touched without dispatch |
| visual honesty | If screenshots exist, is human terminal verdict still separate? | screenshot note is called final visual pass |
| bridge honesty | If Bridge is mentioned, is `write_enabled=False` preserved? | mount is described as write unlock |

## reviewer_receipt

```yaml
verdict: T-PASS | partial_missing_human_gate | FAIL_ENV | REJECT_AS_X
claims_checked:
  - preview_only
  - blocked_claims_intact
  - provenance_named
notes:
  - free text
```

## verdict

- Use this only for preview-only and docs-only review lanes.
- `T-PASS` here is a review receipt, not product proof.
