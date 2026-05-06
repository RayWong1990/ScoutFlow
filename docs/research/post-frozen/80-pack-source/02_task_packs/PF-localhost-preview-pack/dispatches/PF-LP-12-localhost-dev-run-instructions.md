# PF-LP-12 — Localhost dev run instructions

```yaml
status: candidate_task_draft_not_authority
pack: PF-localhost-preview-pack
cluster: PF-localhost-preview
dispatch_class: proof_mainline
open_after_state: successor_entry_ready
proof_kind: shape_only
human_gate: none
priority: medium
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Write `docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md` with backend and H5 run commands plus evidence capture steps for the preview-only loop.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md`; depends: PF-LP-01, PF-LP-04

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md
files_to_modify:
  []
files_will_NOT_touch:
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - docs/decision-log.md
  - services/api/migrations/**
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
  - services/**
  - apps/**
```

## 8. T-PASS condition
Runbook includes backend start, H5 start, env setup, manual evidence capture, and stop-lines for no browser automation.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/localhost-preview-dev-runbook-2026-05-06.md
  required_sections: [backend_start, h5_start, env_setup, manual_evidence_capture, stop_lines]
  required_rows: not_applicable
```
