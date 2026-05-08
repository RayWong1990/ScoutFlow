---
title: Component Target Map
status: candidate / docs-only / not-authority
authority: not-authority
ingest_basis:
  - GPT Pro pack A `03-component-target-map.md`
  - GPT Pro pack C `Lane-D-visual-productization-candidate-handoff.md`
---

# Component Target Map

## Priority

`Vault Preview` / `Blocked-Hold Banner` > `Trust Trace` > `URL Bar` / `Live Metadata` > `Topic Card` > `Batch`

## Target Table

| Component | Current state | Desired productized state | Minimum change | No-go condition |
|---|---|---|---|---|
| URL Bar | Real input wiring exists; PF-V gives denser operator reference only. | Dense manual input surface with validation, source-risk cue, state badge, and blocked/disabled honesty. | Tighten spacing, state badge hierarchy, validation copy, focus styling. | Mixing UI polish with source runtime or route-strategy work |
| Live Metadata | Read-only and dry-run oriented; thumbnail/media may remain absent. | Metadata panel that clearly shows available vs unavailable evidence, with consistent placeholder grammar. | Productize empty/loading/blocked/preview states and thumbnail fallback layout. | Visually implying metadata or thumbnail was fetched when it was not |
| Trust Trace Graph | Self-rolled bounded graph exists. | Readable provenance graph with stronger node/edge hierarchy and error-path emphasis. | First pass stays self-rolled; only polish layout, labels, and error emphasis. | Sneaking graph dependency adoption into visual PR |
| Trust Trace Timeline | Timeline exists in bounded form. | Timeline that supports quick scanning and clear event-to-evidence linkage. | Improve timestamp legibility, hover/focus grammar, evidence highlight rules. | Turning UI polish into runtime/source proof claims |
| Trust Trace Error Path | Error-path lane exists but can visually blur with generic state treatment. | Failure path that clearly separates source, preview, write, and blocked states. | Unify copy tone and state treatment with blocked/failed grammar. | Hiding partial or blocked truth behind success styling |
| Vault Preview | Preview surface exists while true write remains held. | Reviewable preview that cannot be mistaken for committed write. | Add explicit preview border/status/copy, hash/path receipt area, and non-commit emphasis. | Preview visually resembles committed success |
| Topic Card Lite/Vault | Candidate card surfaces exist with mixed density patterns. | Compact card with state icon, evidence chips, and scan-first structure across single-item and vault contexts. | Apply density/type overlays, sync-badge semantics, and clearer chip hierarchy. | Card implies vault write or product completion without evidence |
| Batch Item Row | Future-facing surface, not yet a mature UI. | Row state grammar for 3/10 URL batch outcomes and stop-line visibility. | Define row-level final badges, elapsed/cost slots, and failure/skip layout only. | Creating scheduler/worker/DB queue product UI in Lane D |
| Batch Closeout Panel | Future-facing summary surface. | One-page closeout that highlights outcome distribution and remaining holds. | Reuse panel grammar, summary cards, and evidence/failure table structure. | Enterprise dashboard sprawl or runtime metrics platform scope |
| Blocked-Hold Banner | Boundary exists in authority, but productized visual treatment is still candidate. | Strong blocked banner with hold reason, unlock path, and evidence link. | Standardize icon, copy tone, disabled affordance, and hierarchy. | Blocked banner looks like transient loading or informational hint |

## Lane Isolation

- Lane A may consume future productized visual truth, but should not own dependency decisions.
- Lane B can expose runtime evidence, but should not expand UI scope beyond bounded read surfaces.
- Lane C must not redesign `Vault Preview` while working on true-write gates.
- Lane D owns visual grammar, PF-V translation, and any future dependency candidate discussion.

## Required vs Deferrable

- Required before serious Lane A promotion: `Vault Preview`, `Blocked-Hold Banner`, `Trust Trace` core states, `URL Bar`, `Live Metadata`.
- Deferrable until batch-facing work opens: `Batch Item Row`, `Batch Closeout Panel`.

## Productization Guard

This table is a target map only. It does not allocate a product lane slot or authorize code-bearing implementation by itself.
