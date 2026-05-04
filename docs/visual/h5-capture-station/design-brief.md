---
title: ScoutFlow H5 Capture Station Design Brief
date: 2026-05-05
status: candidate / design-only / not-frontend-implementation-approval
related_task: T-P1A-046
---

# ScoutFlow H5 Capture Station Design Brief

## 1. Product posture

ScoutFlow's H5 Capture Station is a local operator surface. It is not:

- a SaaS admin dashboard
- a landing page
- a desktop dictation shell

The page should read as a focused workstation for one operator who pastes a URL, watches metadata settle, checks state boundaries, and decides whether a capture should later enter the vault path.

## 2. Audience

Primary user:

- one technical operator
- high repetition workflow
- comfortable reading structured status, IDs, timestamps, and machine-originated fields

The surface should therefore prefer:

- clear scan order
- restrained copy
- visible state transitions
- low ambiguity around blocked vs ready layers

## 3. Surface structure

The first viewport is the full working surface. No hero, no marketing layer.

The station keeps a fixed 4 面板 layout:

1. `URL Bar`
   - top strip
   - input + capture action + current route mode
   - visually first stop

2. `Live Metadata`
   - left column
   - title, uploader, duration, page count, selected page, tags, stats
   - should feel like evidence arriving, not like a form

3. `Capture Scope`
   - middle column
   - state machine from `metadata_only` to blocked future layers
   - blocked layers must stay visible but visually downgraded

4. `Trust Trace`
   - right column, widest
   - graph view of `capture -> state -> job -> probe -> receipt -> media/audio -> audit`
   - the graph is secondary to the primary action, but it is the main deep-inspection surface

## 4. Layout rules

- desktop: top URL bar full width; lower area 3-column grid with Trust Trace taking the widest column
- tablet: URL bar full width; lower area stacks into 2 columns with Trust Trace below metadata/scope
- mobile: still use the same 4 panels, but linearize in the same order

The layout must avoid dashboard chrome:

- no persistent sidebar
- no top navigation tabs unrelated to capture flow
- no card-inside-card treatment

## 5. Visual direction

The visual direction should stay in "operator workstation" territory:

- dark neutral base with cool highlight accents
- active proof path in cyan/green
- blocked future layers in muted amber/red
- emphasis comes from contrast and structure, not decorative gradients

OpenDesign probe carry-forward:

- clean panel edges
- explicit panel zoning
- graph/right-column emphasis

Rejected carry-forward:

- admin-template sidebar shell
- decorative KPI board look
- neon-heavy cyberpunk styling

## 6. Typography

Recommended scale:

- station title: 24-28px
- panel titles: 16-18px
- primary machine values: 14-16px
- secondary metadata: 12-13px

Typography rules:

- panel titles must be short and stable
- long machine strings should wrap or truncate safely
- monospace is reserved for IDs, routes, and timestamps

## 7. Panel behavior

### 7.1 URL Bar

- dominant action area
- input should accept long URLs without layout shift
- action state should distinguish idle / validating / captured / blocked

### 7.2 Live Metadata

- values should settle from sparse to full
- unknown fields use explicit empty states, not fake placeholders
- title and uploader should carry the most visual weight inside this panel

### 7.3 Capture Scope

- show the currently proven layer first
- keep blocked future layers visible:
  - `audio_transcript`
  - `media processing`
  - `vault commit`
- blocked layers should look unavailable, not hidden

### 7.4 Trust Trace

- graph nodes should mirror the actual layered DTO chain
- node expansion should reveal state and evidence details
- edge direction must match the real capture lifecycle, never a decorative graph

## 8. Motion and transitions

Motion should be sparse and meaningful:

- metadata rows fade/slide in as proof arrives
- state machine highlights one active step at a time
- trust-trace graph can pulse the active path, but only mildly

Avoid:

- generic hover animation noise
- overscaled spring motion
- loading shimmer on every surface

## 9. Safety boundaries

This design package must keep these truths visible:

- current path is metadata-first
- runtime remains gated
- vault write is not yet approved
- trust-trace is evidence, not decoration

Any later implementation that obscures blocked state, hides trust trace, or visually promotes future lanes as already active should fail design review.
