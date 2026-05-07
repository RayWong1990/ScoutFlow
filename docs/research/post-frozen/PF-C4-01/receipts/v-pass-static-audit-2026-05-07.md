---
title: PF-C4-01 V-PASS Static Audit Receipt
status: candidate
not_authority: true
created_at: 2026-05-07
auditor: codex
target_pr: 243
target_commit: a848e70
purpose: 帮战友先扫一遍 V-PASS 可发现的硬伤, 不替代浏览器视觉终判
---

# Static Audit Findings

## Context

- repo: `/Users/wanglei/workspace/ScoutFlow`
- branch guard: `codex/pf-c4-01-2026-05-07`
- commit guard: `a848e70`
- dev server: `http://localhost:4173`

## 1. Hex hardcode scan

Command:

```bash
grep -rEn '#[0-9a-fA-F]{3,8}' apps/capture-station/src --include='*.tsx' --include='*.module.css' \
  | grep -v 'tokens.css' \
  | grep -v 'density-compact.css' \
  | grep -v 'type-weight-heavy.css'
```

Result:

- `0` hits
- conclusion: no stray hex color hardcodes outside token / overlay files

## 2. Inline style hex scan

Command:

```bash
grep -rEn 'style=\{\{.*#[0-9a-fA-F]{3,8}' apps/capture-station/src --include='*.tsx'
```

Result:

- `0` hits
- conclusion: no inline-style hex anti-pattern found

## 3. SVG sprite wiring

Commands:

```bash
grep -rEn '<Icon ' apps/capture-station/src --include='*.tsx' | wc -l
grep -rEn '<use href' apps/capture-station/src/components/Icon/Icon.tsx | wc -l
```

Result:

- `<Icon ...>` call sites: `18`
- `<use href>` inside `Icon.tsx`: `2`
- conclusion: sprite indirection is wired and reused broadly enough for the current shell

## 4. L8 sync-badge 3-state contract

Result:

- `SyncBadge.tsx` defines `synced / pending / external-changed`
- `SyncBadge.module.css` defines `.synced / .pending / .externalChanged`
- `TopicCardVault.tsx` explicitly states `synced / pending / external-changed` cannot collapse
- conclusion: L8 contract is present in both logic and style layers

## 5. Honest TODO placeholders

Observed markers:

- `LiveMetadata.tsx`
  - `TODO P1: bind to BBDown metadata pipeline`
  - `data-todo="thumbnail-fetch"`
- `TrustTrace.tsx`
  - `TODO P1: D3/cytoscape decision (PF-C4-EXT)`
  - `data-todo="trust-trace-graph"`
  - `TODO P2: timeline hover and evidence focus wiring`
  - `data-todo="trust-trace-timeline"`
  - `TODO P1: error-path highlight wiring with graph implementation`
  - `data-todo="trust-trace-error-path"`

Conclusion:

- thumbnail / graph / timeline / error-path all remain honestly marked
- no fake “already wired” signal detected from static scan

## 6. Token reference density

Command:

```bash
grep -rEn 'var\(--' apps/capture-station/src --include='*.module.css' | wc -l
```

Result:

- token var references: `375`
- conclusion: token consumption density is high and consistent with CSS Variables primary path

## 7. Styling / UI / stack anti-pattern scan

Commands covered:

- `styled-components`
- `@emotion`
- `@stitches`
- `vanilla-extract`
- `panda-css`
- `@mui`
- `antd`
- `@chakra-ui`
- `@mantine`
- `lucide-react`
- `@radix-ui`
- `@tanstack`
- `reactflow` / `react-flow`
- `zustand`

Result:

- `0` hits across all three anti-pattern groups
- conclusion: no styling package adoption drift, no UI framework drift, no extra stack drift found in static imports

## Static verdict

- verdict: `clear_for_human_v-pass_review`
- static concern count: `0 hard blockers`
- residual limit:
  - this receipt does **not** replace browser-side 5 Gate human review
  - visual hierarchy / spacing rhythm / weight balance still require human eyes on `http://localhost:4173`
