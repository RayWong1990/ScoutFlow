---
title: C3 object keep list
status: candidate / research / not-authority
created_at: 2026-05-06
related_dispatch: PF-C3-02
---

# C3 object keep list

## scope

- Source input is the inventory in [c3-object-inventory-131-144.md](/Users/wanglei/workspace/ScoutFlow/docs/research/post-frozen/c3-object-inventory-131-144.md:1).
- Goal is to keep the smallest object set that still supports topic-card-lite, capture-plan-lite, and evidence-source review.

## keep_now

| object | source_task | why_keep | reduction_rule |
|---|---|---|---|
| `topic_card_lite` | `T-P1A-131` | primary usefulness carrier | one card surface, not a family of cards |
| `capture_plan_lite` | `T-P1A-132` | pairs with topic card for actionability | stay preview-only and bounded |
| `evidence_source_matrix` | `T-P1A-136` + `T-P1A-139` | preserves provenance and review trace | keep one matrix, not parallel inventories |
| `overflow_registry` | `T-P1A-140` | keeps blocked lanes in one place | any future blocked lane must append here first |
| `vault_preview_contract` | `T-P1A-142` | clarifies preview semantics without write unlock | preview wording must stay explicit |

## keep_as_reference_only

| object | source_task | rule |
|---|---|---|
| `signal_ingestion_audit_note` | `T-P1A-134` | cite when explaining evidence intake, do not surface in preview UI line |
| `bridge_hardening_note` | `T-P1A-141` | reference-only until proof-bearing preview work is stable |

## keep_language_rules

- Use `surface`, `seam`, `matrix`, `note`, `registry`.
- Avoid multiplying nouns like `system`, `module`, `engine`, `workbench` when the artifact is only a candidate doc.
- Keep one visible user loop: `topic card -> capture plan -> evidence source review`.

## verdict

- Minimal keep set is intentionally smaller than the authored object set.
- `T-PASS` means the keep list is ready to guide wording and file compression, not that the kept surfaces are approved for runtime or product launch.
