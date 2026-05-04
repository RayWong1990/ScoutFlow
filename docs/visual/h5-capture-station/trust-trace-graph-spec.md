---
title: ScoutFlow Trust Trace Graph Spec
date: 2026-05-05
status: candidate / design-only / not-frontend-implementation-approval
related_task: T-P1A-046
---

# ScoutFlow Trust Trace Graph Spec

## 1. Purpose

The Trust Trace graph is the right-hand deep inspection surface in the H5 Capture Station. It visualizes how one capture moves through layered proof objects without implying that later blocked layers are already active.

## 2. Canonical node chain

The default chain is:

1. `capture`
2. `capture_state`
3. `metadata_job`
4. `probe_evidence`
5. `receipt_ledger`
6. `media_audio`
7. `audit`

The graph should render left-to-right on desktop and top-to-bottom on narrow screens.

## 3. Node semantics

| Node | Meaning | Weight |
|---|---|---|
| `capture` | operator intent and source identity | medium |
| `capture_state` | current phase truth | high |
| `metadata_job` | machine work unit | medium |
| `probe_evidence` | proof payload entering the system | high |
| `receipt_ledger` | normalized accounting layer | high |
| `media_audio` | downstream blocked/future layer in current phase | low when blocked |
| `audit` | operator/reviewer confirmation layer | medium |

## 4. Edge rules

- edges show actual dependency, not decorative relation
- one active path at a time
- blocked downstream edges must remain visible but visually downgraded
- failed branches should branch clearly instead of mutating the main success line

## 5. Visual encoding

Recommended encoding:

- active success path: cyan to green
- blocked future path: muted amber
- hard failure path: red
- inactive but available context: cool gray

Node treatment:

- active node: filled, stronger border, readable label
- inactive node: lower fill, same geometry
- blocked node: visible icon/label plus reduced saturation

## 6. Detail payloads

Each node may expose a side detail view or tooltip with:

- state word
- timestamp
- identity fields
- brief machine-readable notes

Do not dump raw JSON by default in the graph itself. The graph is the structure view; detailed raw payload should remain a secondary inspection mode.

## 7. Default right-column composition

The right column should contain:

- panel title
- graph canvas
- compact detail shelf below or beside the graph

The graph canvas must dominate the panel. Secondary legends should not out-weigh the graph.

## 8. Non-goals

- not a BPMN editor
- not a freeform topology explorer
- not an analytics dashboard chart
- not a decorative "network" background

## 9. Carry-forward to implementation

Later implementation should preserve:

- stable node order
- blocked-layer visibility
- one-source-of-truth state wording
- active-path emphasis without visual clutter
