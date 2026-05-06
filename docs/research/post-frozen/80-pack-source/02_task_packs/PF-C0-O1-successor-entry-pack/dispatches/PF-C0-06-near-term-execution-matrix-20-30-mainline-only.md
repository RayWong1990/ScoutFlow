# PF-C0-06R — Near-term execution matrix 20-30 mainline only

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-C0
dispatch_class: successor_entry
open_after_state: successor_entry_ready
proof_kind: shape_only
human_gate: none
priority: high
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Build `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md` to classify all 80 authored tasks into near-term mainline, reservoir, and overflow with priority and open_after_state.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md`; depends: PF-C0-MERGED-03+04, PF-O1-01R

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md
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
```

## 8. T-PASS condition
The matrix contains 80 rows and keeps near-term mainline between 20 and 30 rows; every row has code, cluster, priority, open_after_state, status, and reason.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/near-term-execution-matrix-2026-05-06.md
  required_rows: 80
  required_columns: [code, cluster, priority, open_after_state, status, reason]
  near_term_count_range: [20, 30]
```
