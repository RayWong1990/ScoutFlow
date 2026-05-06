# PF-C0-01R — Live authority readback after PR194

```yaml
status: candidate_task_draft_not_authority
pack: PF-C0-O1-successor-entry-pack
cluster: PF-C0
dispatch_class: successor_entry
open_after_state: successor_entry_ready
proof_kind: shape_only
human_gate: none
priority: blocker
inherits: ../../_PACK-DEFAULTS.md
```

## 0/5/6/7/9/10/11. Shared clauses
Inherits `_PACK-DEFAULTS.md`.


## 1. Goal
Record `docs/research/post-frozen/live-authority-readback-after-pr194.md` as a live truth table separating zip-derived fact, PR192-era readback, PR193/PR194 GitHub fact, and current localhost code seams.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/live-authority-readback-after-pr194.md`; depends: none

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/live-authority-readback-after-pr194.md
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
The readback table contains five evidence rows: zip upload truth, PR192 readback, PR193 authority sync, PR194 STEP0 templates, and current main.py / UrlBar / bridge config seams.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/live-authority-readback-after-pr194.md
  required_sections: [source_boundary, live_truth_table, conflict_verdict]
  required_rows: 5
  required_columns: [claim, source_class, evidence_path_or_sha, verdict]
```
