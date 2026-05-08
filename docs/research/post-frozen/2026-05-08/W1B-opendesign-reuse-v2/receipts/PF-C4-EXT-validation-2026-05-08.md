---
title: PF-C4-EXT Validation Receipt
status: candidate / receipt / not-authority
authority: not-authority
cluster: W1B-PF-C4-EXT
path_choice: path-A-self-rolled
created_at: 2026-05-08
---

# PF-C4-EXT Validation Receipt

## Commands

- `pnpm test` in `apps/capture-station`
- `pnpm run lint` in `apps/capture-station`
- `pnpm run typecheck` in `apps/capture-station`
- `pnpm run build` in `apps/capture-station`
- `pytest tests/contracts/test_trust_trace_dto_snapshot_contract.py -q`
- `python3 tools/check-docs-redlines.py docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/receipts`
- `python3 tools/check-secrets-redlines.py docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/receipts`

## Results

- `pnpm test`: `18` files / `64` tests passed; existing non-blocking `App.test.tsx act()` warning still present.
- `pnpm run lint`: pass.
- `pnpm run typecheck`: pass.
- `pnpm run build`: pass; bundle output `dist/assets/index-C9-bycyC.js 240.35 kB` / `gzip 72.85 kB`.
- `pytest tests/contracts/test_trust_trace_dto_snapshot_contract.py -q`: `6 passed`.
- docs/secrets redline on receipts: pass.

## Boundary checks

- path choice: `path-A-self-rolled`
- package diff: `none`
- `d3` fallback: not used
- DTO/enum/schema drift: not observed in current validation scope
- authority files touched: `no`
- runtime/browser/vault/migration unlock: `no`
- visual evidence: `not collected due to gate`
