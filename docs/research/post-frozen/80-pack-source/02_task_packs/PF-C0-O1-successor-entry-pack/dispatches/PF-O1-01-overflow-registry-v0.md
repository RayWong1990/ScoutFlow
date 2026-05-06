# PF-O1-01R — Overflow registry v0

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-O1
dispatch_class: overflow
open_after_state: successor_entry_ready
proof_kind: none
human_gate: none
priority: blocker
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Write `docs/research/post-frozen/overflow-registry-v0.md` with five overflow gate rows for true write, runtime tools, browser automation, DBvNext/migration, and full Signal Workbench.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/overflow-registry-v0.md`; depends: none

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/overflow-registry-v0.md
files_to_modify:
  []
files_will_NOT_touch:
  - services/**
  - apps/**
  - workers/**
  - packages/**
  - data/**
  - referencerepo/**
  - docs/current.md
  - AGENTS.md
  - docs/task-index.md
  - docs/decision-log.md
```

## 8. T-PASS condition
The registry contains exactly five high-risk topic rows, each with blocked_reason, reopen_condition, human_gate, kill_switch_ref, and owner.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: none
evidence_shape:
  output_path: docs/research/post-frozen/overflow-registry-v0.md
  required_rows: 5
  required_columns: [topic, blocked_reason, reopen_condition, human_gate, kill_switch_ref, owner]
  topics_required: [true_vault_write, runtime_tools, browser_automation, dbvnext_migration, full_signal_workbench]
```
