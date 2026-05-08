---
title: Lane D PF-V visual productization scope note
status: reference storage
type: repair-note
created_at: 2026-05-08
related_pr: 271
related_task: T-P1A-LANE-D-CODE-BEARING
---

# Lane D PF-V visual productization scope note

## Allowed app paths

- `apps/capture-station/src/components/Button/Button.module.css`
- `apps/capture-station/src/components/Button/Button.test.tsx`
- `apps/capture-station/src/components/Button/Button.tsx`
- `apps/capture-station/src/components/Button/derive.ts`
- `apps/capture-station/src/components/EvidenceTable/EvidenceTable.module.css`
- `apps/capture-station/src/components/EvidenceTable/EvidenceTable.test.tsx`
- `apps/capture-station/src/components/EvidenceTable/EvidenceTable.tsx`
- `apps/capture-station/src/components/HoldBanner/HoldBanner.module.css`
- `apps/capture-station/src/components/HoldBanner/HoldBanner.test.tsx`
- `apps/capture-station/src/components/HoldBanner/HoldBanner.tsx`
- `apps/capture-station/src/components/HoldBanner/holds.ts`
- `apps/capture-station/src/components/PromoteGate/PromoteGate.module.css`
- `apps/capture-station/src/components/PromoteGate/PromoteGate.test.tsx`
- `apps/capture-station/src/components/PromoteGate/PromoteGate.tsx`
- `apps/capture-station/src/components/StateBadge/StateBadge.module.css`
- `apps/capture-station/src/components/StateBadge/StateBadge.test.tsx`
- `apps/capture-station/src/components/StateBadge/StateBadge.tsx`
- `apps/capture-station/src/components/StateBadge/derive.ts`
- `apps/capture-station/src/components/__visual__/StateMatrixDemo.tsx`
- `apps/capture-station/src/styles/state-tokens.css`
- `apps/capture-station/src/styles/state-tokens.test.ts`
- `apps/capture-station/src/styles/state-tokens.ts`
- `apps/capture-station/src/styles/trust-trace-lane-order.css`

## Boundary

- no `apps/capture-station/src/features/**` changes
- no `apps/capture-station/src/App.tsx` or `apps/capture-station/src/components/AppShell/**` changes
- no `package.json` / `pnpm-lock.yaml` change
- no runtime approval / no true-write approval / no migration approval / no browser automation approval
- this note records Lane D primitive-only scope for PR #271 and does not upgrade any candidate surface to authority
