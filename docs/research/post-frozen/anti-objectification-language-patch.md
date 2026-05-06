---
title: Anti-objectification language patch
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-C3-05
---

# Anti-objectification language patch

## problem_patterns

- Candidate docs often overstate scope by turning every note into a named object.
- The drift pattern is `candidate note -> named object -> implied product lane`.
- This patch keeps wording tied to proof seams instead of multiplying product nouns.

## replacement_table

| avoid | prefer | reason |
|---|---|---|
| `new module` | `candidate note` | prevents docs-only work from sounding implemented |
| `engine` | `rule set` | keeps abstraction weight low |
| `workbench surface` | `preview surface` | matches current phase truth |
| `artifact family` | `supporting file set` | reduces object proliferation |
| `pipeline` | `review loop` | better reflects current manual evidence posture |
| `runtime-ready` | `candidate / not runtime approval` | preserves blocked-lane truth |
| `proof complete` | `proof shape present` | separates shape from human gate |

## sentence_templates

- Preferred: `This note narrows the preview-only seam and does not unlock runtime.`
- Preferred: `Keep this as a supporting file under the topic-card-lite loop.`
- Preferred: `Use the registry row as boundary control, not as product scope expansion.`
- Avoid: `This module now owns...`
- Avoid: `This engine powers...`

## apply_now_targets

| target_file | patch_direction |
|---|---|
| `c3-object-keep-list.md` | keep visible objects tied to preview loop only |
| `c3-object-compress-list.md` | rename peer objects to appendices or support notes |
| `commander-prompt-near-term-mainline.md` | describe gates and receipts, not product capability |

## verdict

- The patch is lexical and governance-oriented only.
- `T-PASS` does not approve any new object, runtime lane, or UI scope.
