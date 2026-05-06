---
title: Preview-only Localhost Loop Readback
status: candidate / preview_only_readback / not-authority
date: 2026-05-06
dispatch_id: PF-LP-17
verdict: works
---

# PF-LP-17 Readback

## Inputs read back

- PF-LP-09 forensic verdict: `COVERED_BY_228` via PR `#233` / merge commit `b4fc8b51e90de70364583398dbb463c813adb623`
- PF-LP-10 forensic verdict: `COVERED_BY_228` via PR `#232` / merge commit `9512f9ee558f270500d669f90389476454b97869`
- PF-LP-14 forensic verdict: `COVERED_BY_228` via PR `#234` / merge commit `244576124f5003f6c062bda88d8cca6b74c5d4f3`
- PF-LP-16 synthetic evidence: `docs/research/post-frozen/evidence/PF-LP-16-manual-localhost-run-2026-05-06.md` via PR `#235` / merge commit `91a2deabb18efb2560fe483f40497acad7cdf0ff`

## Loop readback

- create-capture entrypoint stayed on `POST /captures/discover`; synthetic probe returned `capture_id=01KQYEXWJYZ9X8FW7TGD1QW0XP`
- preview entrypoint stayed on `GET /captures/{capture_id}/vault-preview`; returned a `23`-line markdown body with the original query string preserved in `canonical_url`
- copy action readback: `success`
  source: `VaultPreviewPanel.test.tsx` green JSDOM assertions plus `pnpm test -- VaultPreviewPanel UrlBar` passing `22/22`
- download action readback: `success`
  source: same JSDOM run; expected filename `scoutflow-preview-01KQYEXWJYZ9X8FW7TGD1QW0XP.md`

## Pass / partial / fail classification

- verdict: `works`
- why not `partial`:
  backend probe succeeded, `capture_id` was created, preview markdown was returned, and copy/download assertions stayed green
- why not `product proof`:
  this is still a preview-only localhost loop using `curl` plus JSDOM tests, not a human visual verdict and not a true browser execution proof

## Boundary reminder

- no true vault write
- no runtime approval
- no browser automation
- no migration approval
- no RAW handoff claim
