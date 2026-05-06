# PF-C0-MERGED-03+04 — Successor entry and preview-only scope memo

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
Write `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md` to join PF-cluster routing, preview-only localhost pass bar, and rejection of automatic `Dispatch177+` sequencing.

## 2-3. Output / dependencies
output: `docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md`; depends: PF-C0-01R

## 4. Files preview
```yaml
files_to_create:
  - docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md
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
  - 80-pack-source/**
```

## 8. T-PASS condition
The memo has three native sections: successor route diagram, seven-step preview-only pass bar, and PF-* naming reset that rejects automatic `Dispatch177+` sequencing.


## 12. Validation
```bash
python tools/check-docs-redlines.py docs/research/post-frozen/ && python tools/check-secrets-redlines.py docs/research/post-frozen/ && git diff --check docs/research/post-frozen/
```

## 13. Evidence shape
```yaml
proof_kind: shape_only
evidence_shape:
  output_path: docs/research/post-frozen/successor-entry-and-preview-scope-2026-05-06.md
  required_sections: [successor_route_diagram, preview_only_pass_bar, dispatch_naming_reset]
```
