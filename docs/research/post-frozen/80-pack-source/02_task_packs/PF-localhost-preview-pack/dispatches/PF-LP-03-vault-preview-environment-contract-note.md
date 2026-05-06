# PF-LP-03 — Vault preview environment contract note

```yaml
status: candidate_task_draft_not_authority
pack: PF-localhost-preview-pack
cluster: PF-localhost-preview
dispatch_class: proof_mainline
open_after_state: successor_entry_ready
proof_kind: shape_only
human_gate: none
priority: high
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Document `SCOUTFLOW_VAULT_ROOT` preview semantics in `docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md` so unset, invalid, and configured states are explicit before H5 consumes preview.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md`; depends: PF-O1-01R

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md
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
The note defines unset, invalid/missing, and configured preview states and states that preview is not true write.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/vault-preview-env-contract-2026-05-06.md
  required_sections: [unset_state, invalid_or_missing_root_state, configured_preview_state, no_true_write_boundary]
  required_columns: [state, expected_response, operator_message]
```
