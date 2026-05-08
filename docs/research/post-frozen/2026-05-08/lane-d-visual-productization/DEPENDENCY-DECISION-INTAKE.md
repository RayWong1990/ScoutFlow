---
title: Dependency Decision Intake
status: candidate / docs-only / not-authority
authority: not-authority
ingest_basis:
  - GPT Pro pack A `01-ui-stack-decision-candidate.md`
  - GPT Pro pack A `06-dependency-risk-table.md`
---

# Dependency Decision Intake

## Decision Table

| Option | What it helps with | What it does not solve | Risk summary | Recommendation |
|---|---|---|---|---|
| Current self-rolled CSS/TSX | Keeps dependency surface minimal; matches current React/Vite/CSS Modules/tokens baseline; fastest path for first Lane D PR. | Complex graph layout, mature focus-trap primitives, richer overlay ergonomics. | Lowest blast radius and lowest style drift risk. | Default |
| Self-rolled + Radix primitives | Solves dialog/popover/menu/focus-trap primitives if they repeat across multiple surfaces. | Does not provide PF-V visual language or graph/timeline behavior. | Medium risk if kept primitives-only; high if it expands into themed adoption. | Conditional only |
| Self-rolled + graph library (`React Flow` or lighter graph package) | Helps Trust Trace graph layout and node/edge interaction when self-rolled SVG becomes unreadable or brittle. | Does not solve typography, panel grammar, copy tone, or broader UI system questions. | Medium to high risk depending on scope and CSS integration. | Conditional only |
| Tailwind | Speeds utility-class layout work. | Does not preserve existing token discipline or PF-V operator-workstation specificity. | High style drift and broad refactor pressure. | Reject now |
| shadcn | Quick access to polished common patterns. | Pulls Tailwind and admin/SaaS defaults into a workstation UI. | High blast radius and high style drift. | Reject now |
| Full design-system suite (`Mantine`, `Chakra`, `MUI`, `Ant`, similar) | Broad component coverage. | Grossly exceeds Lane D needs and turns a visual truth pass into platform work. | Very high blast radius, install risk, and migration pressure. | Hard reject |
| Icon library (`Lucide`, similar) | Supplies many ready-made icons. | PF-V already offers state/system sprite direction; icon quantity is not the blocker. | Medium risk of generic feel and semantic mismatch. | Reject now |

## Default Position

`self-rolled first`

The first code-bearing Lane D should assume no new dependency unless proven necessary by repeated, bounded pain in real components.

## Dependency Introduction Triggers

A new dependency may be considered only when all seven conditions are true:

1. The problem repeats across at least two real production surfaces.
2. Self-rolled implementation has already shown visible quality loss, maintenance pain, or accessibility failure.
3. The dependency can be isolated to a minimum integration point.
4. The change remains inside Lane D and does not contaminate A/B/C.
5. No runtime/source/true-write/migration scope is bundled with the dependency decision.
6. The user explicitly approves the dependency gate.
7. An Opus dependency audit runs before merge.

## Minimum Integration Points

- Radix: `Dialog` / `Popover` only.
- Graph library: `Trust Trace Graph` only.
- No global theme package.
- No lockfile/package install hidden inside a visual productization PR.

## Explicit Reject Set

- Tailwind as default styling path.
- shadcn as bundled UI baseline.
- Full design-system suite adoption.
- Automatic icon-library swap.
- Any dependency framed as "PF-V asset reuse".

## Decision Output Shape for Future PR

If a future code-bearing Lane D proposes a dependency, it must include:

- visual value gained,
- implementation cost,
- package/build risk,
- style-drift risk,
- blast radius to A/B/C lanes,
- stop-line if the dependency leaks beyond its isolated scope.
