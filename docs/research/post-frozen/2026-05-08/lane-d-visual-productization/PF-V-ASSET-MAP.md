---
title: PF-V Asset Map
status: candidate / docs-only / not-authority
authority: not-authority
ingest_basis:
  - GPT Pro pack A `02-pfv-asset-runtime-reference-map.md`
  - PF-V reference-only assets under `docs/research/visual-prototypes/PF-V/**`
---

# PF-V Asset Map

## Purpose

This document classifies PF-V materials into runtime-eligible carry-forward, reference-only input, and explicit reject buckets. It is a translation map for future Lane D work, not approval to import raw PF-V output into runtime.

## Classification

| Class | PF-V material | Reason | Product surface | Risk | Acceptance check |
|---|---|---|---|---|---|
| runtime/product asset | `tokens.css`, state/background tokens, selected CSS variables | Existing Capture Station already uses tokenized styling; PF-V adds stronger operator-workstation contrast and state separation. | Shared shell, state badges, evidence panels, hold banner | Hardcoded colors or per-component drift | New styling remains token-driven; no raw PF-V file import |
| runtime/product asset | `density-compact.css`, `type-weight-heavy.css` overlays | Density and type weight are reusable scanning primitives, not one-off page styling. | URL bar, metadata panel, topic card, batch row, closeout panel | Baking density into component-specific hacks | Overlay stays additive and reversible |
| runtime/product asset | `icons/system.svg`, `icons/state.svg` semantic subsets | State icons can clarify blocked/preview/committed/failed without adding dependencies. | `StateBadge`, hold banner, trust trace states, topic-card indicators | Icon ID drift or generic substitution | Icon semantics stay mapped to exact state words |
| token/motif | PF-V palette, spacing, radius, shadow, type rhythm, Chinese UI chrome | Defines the visual language without forcing a framework switch. | All Lane D productized surfaces | Copying style mechanically into generic dashboard chrome | Visual hierarchy stays evidence-first, not decorative-first |
| empty/running/blocked visual | State modifier sections, sync-badge three-state treatment, preview emphasis | PF-V's strongest contribution is state legibility under operator scanning. | URL bar, metadata, trust trace, vault preview, batch rows | Preview/blocked/disabled collapsing visually | Manual visual review can distinguish each state in under 10 seconds |
| panel grammar | Panel-card, evidence-table, frontmatter-block, promote-gate, topic-card grammar from the 13 PF-V surfaces | Reusable layout vocabulary for information-dense workstation UI. | Evidence panels, preview panels, closeout panels, blocked banner stacks | Over-translating raw HTML structure into runtime | Translate semantics only; do not import rough HTML/CSS as runtime |
| reference-only | 152 PNGs, screenshot sets, `PF-V-INDEX.csv` | Best source for visual comparison and review receipts, not runtime assets. | Human review, later audit packets | Pixel-perfect copying or false authority claims | Used only as comparison evidence |
| reference-only | `html5-rough/*.html`, `*.model.json`, snippet files, handoff docs | Useful for reasoning about intended structure and TODOs. | Lane D planning and review | Hidden fixture/runtime coupling | No raw file import into `apps/**` |
| reference-only | PF-V handoff docs, acceptance checklist, README, maintenance docs | Preserve candidate constraints and receiving rules. | Dispatch design, audit design, review checklist | Treating candidate handoff as authority | Every cite must preserve `candidate / not-authority` wording |
| reject | Tailwind, shadcn, Panda, or any third-party framework described as a PF-V "asset" | These are stack choices, not PF-V assets. | None | Style drift and scope smuggling | No framework adoption by default |
| final-reject | Mutating PF-V lane files after handoff | PF-V is closed evidence for this wave. | None | Moving-source drift; audit becomes unreplayable | `docs/research/visual-prototypes/PF-V/**` remains read-only |

## Carry-forward Rules

1. A PF-V item becomes runtime-eligible only after separate code-bearing approval.
2. Runtime translation must preserve token discipline and state semantics.
3. Raw PF-V HTML/JSON stays reference-only even when its visual intent is adopted.
4. Visual pass depends on state honesty, not on visual polish alone.
5. PF-V assets cannot be used to imply runtime, true-write, or migration approval.

## Highest-value Carry-forward Set

1. Tokenized state colors and background treatment.
2. Density and typography overlays as composable layers.
3. Semantic state icons and sync-badge vocabulary.
4. Evidence-table and panel grammar for scan order.
5. Preview-vs-committed visual separation.
6. Chinese operator-workstation copy tone.

## Non-goals

- This file does not authorize dependency install.
- This file does not authorize editing `apps/**`.
- This file does not convert PF-V reference files into repository authority.
