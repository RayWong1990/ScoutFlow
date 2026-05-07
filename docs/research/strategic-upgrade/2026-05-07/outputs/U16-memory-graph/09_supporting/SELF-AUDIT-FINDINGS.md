---
title: U16 Self Audit Findings
status: candidate / supplementary / not-authority
created_at: 2026-05-07
---

# U16 Self Audit Findings

| ID | Check | Verdict |
|---|---|---|
| SA-01 | All node files include frontmatter with node_id/kind/source/source_path/first_seen_at/linked_nodes/risk_if_forgotten | PASS |
| SA-02 | linked_nodes are symmetrized in generation | PASS |
| SA-03 | Adjacency JSON generated from same edge set as Mermaid | PASS |
| SA-04 | Master graph contains all nodes | PASS |
| SA-05 | No writes to ~/.claude memory | PASS; path unavailable |
| SA-06 | No writes to GitHub authority docs | PASS |
| SA-07 | No modification to uploaded ZIP | PASS |
| SA-08 | No fabricated claude-mem observation IDs | PASS; count 0 |
| SA-09 | No jsonl full-read | PASS; no jsonl accessible |
| SA-10 | PII/credentials masked | PASS; no credential material copied |
| SA-11 | DiloFlow/ContentFlow marked unavailable | PASS |
| SA-12 | ZIP current vs GitHub live current separated | PASS |
| SA-13 | Dispatch126-176 frozen correction incorporated | PASS |
| SA-14 | candidate/not-authority surfaced in every file | PASS |
| SA-15 | runtime approval drift guarded | PASS |
| SA-16 | migration approval drift guarded | PASS |
| SA-17 | frontend/visual verdict drift guarded | PASS |
| SA-18 | Vault preview vs true write guarded | PASS |
| SA-19 | RAW vs ScoutFlow SoR guarded | PASS |
| SA-20 | single-user/local-first retained | PASS |
| SA-21 | max horsepower reconciled with authority writer max=1 | PASS |
| SA-22 | Product proof not breadth extracted as main post176 thesis | PASS |
| SA-23 | Topic-card proof pair linked to Dispatch145/146 | PASS |
| SA-24 | Overflow registry does not unlock blocked lanes | PASS |
| SA-25 | Source inventory includes sha256 and sizes | PASS |
| SA-26 | Mermaid diagrams count >=6 | PASS |
| SA-27 | Graph has no orphan node by generation guard | PASS |
| SA-28 | Prompt min 150 thinking minutes not claimed | PASS; bounded run disclosed |
| SA-29 | Memory files referenced truthfully as 0 actual original memory files | PASS |
| SA-30 | Ready for user audit with limitation ledger | PASS |

## Interpretation

The self-audit intentionally refuses to claim unavailable local evidence. This means the deliverable is useful as a candidate atlas, but it should not be merged into any canonical memory store without a later local pass that can read real `~/.claude`, handoff trail, claude-mem corpora, and masked jsonl samples.
