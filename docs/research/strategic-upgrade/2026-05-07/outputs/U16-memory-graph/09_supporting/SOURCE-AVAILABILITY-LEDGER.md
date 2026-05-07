---
title: Source Availability Ledger
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# Source Availability Ledger

## Available in this run

| Source class | Status | Count / note |
|---|---|---|
| Uploaded U16 prompt | available | `/mnt/data/cloud-prompt-U16-cross-session-memory-graph-2026-05-07.md` |
| Uploaded ZIP | available | `/mnt/data/ScoutFlow-post176-cloud-audit-pack-2026-05-05.zip` |
| Extracted files | available | 100 actual files |
| Dispatch127-176 manifest | available | 50 JSONL rows |
| Dispatch markdown files | available | 50 files |
| GitHub decision-log | connector-read | api_tool citation turn1file0 |
| GitHub current.md | connector-read | api_tool citation turn2file0 |
| GitHub task-index.md | connector-read | api_tool citation turn3file0 |

## Unavailable in this sandbox

| Prompt-specified source | Treatment |
|---|---|
| `~/.claude/projects/-Users-wanglei-workspace-ScoutFlow/memory/` | not found; not fabricated |
| `~/.claude/projects/.../bd735ce1*.jsonl` | not found; jsonl_sample_turns_referenced=0 |
| claude-mem corpora SQLite + ChromaDB | not accessible; claude_mem_observations_referenced=0 |
| `~/workspace/ScoutFlow/plan/handoffs/` | not accessible; replaced by ZIP Dispatch127-176 pack evidence only |
| `~/workspace/contentflow/L/ retrospective` | not accessible; ContentFlow node marked unavailable |
| `~/workspace/DiloFlow/ memory` | not accessible; DiloFlow node marked unavailable |
| `~/.claude/rules/*` | not accessible; global-rule claims only from prompt/ZIP where visible |

## Boundary

Because the full local memory corpus was unavailable, this atlas is **not** the full 150-minute, local-authority-backed U16 pass described in the prompt. It is a bounded candidate reconstruction over the sources that were actually readable in this ChatGPT sandbox plus GitHub connector citations. That limitation is intentionally surfaced in every relevant node rather than hidden.
