# Dispatch127-176 Topic Card Visual Evidence

- status: `BOUNDED_TOPIC_CARD_VISUAL_EVIDENCE_COLLECTED`
- authority: `not-authority`
- execution_approval: `not-approved`
- runtime_approval: `not-approved`
- global_visual_terminal_verdict: `not-provided`
- date: `2026-05-06`

## Scope

This evidence applies only to the bounded topic-card candidate surfaces:

- `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx`
- `apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.tsx`

## Local-Only Preview Method

- local dev server:
  - `npm run dev -- --host 127.0.0.1 --port 4174 --strictPort`
- temporary local-only HTML/TSX entrypoints mounted the candidate components directly
- no change was made to:
  - `main.tsx`
  - `App.tsx`
  - `FourPanelShell`
  - any tracked runtime route

## Playwright / Static Run Summary

- page used for screenshots:
  - `http://127.0.0.1:4174/.topic-card-combined-visual.html`
- auxiliary single-surface probes:
  - `http://127.0.0.1:4174/.topic-card-vault-visual.html`
  - `http://127.0.0.1:4174/.topic-card-preview-visual.html`
- screenshot flow:
  - Playwright MCP opened the local page
  - viewport resized to desktop / tablet / mobile
  - full-page screenshots captured

## Local Screenshot Packet

- packet path:
  - `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/visual-packets/Dispatch145-146-topic-card-2026-05-06/`
- files:
  - `desktop.png`
  - `tablet.png`
  - `mobile.png`
  - `README.md`

## Visual Review Conclusion

- conclusion: `BOUNDED_TOPIC_CARD_VISUAL_EVIDENCE_COLLECTED`
- companion boundary: `NO_GLOBAL_VISUAL_TERMINAL_VERDICT`

## Boundary

- not product UI approval
- not runtime approval
- not route or shell wiring approval
- not browser automation approval beyond this evidence run
- no screenshot files are committed to the repo
