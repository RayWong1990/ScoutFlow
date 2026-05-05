---
title: STEP2 Runtime Readiness And Screenshot Note
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: STEP2A items 2A-4 and 2A-5
---

# STEP2 Runtime Readiness And Screenshot Note

> State: candidate / not authority / not runtime approval.

## 1. Raw Directory Scaffold

Keep STEP2 run artifacts and future Dispatch127-176 run artifacts separate.

Current STEP2 run root:

- `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/runs/STEP2-2026-05-05/`

Recommended future Dispatch127-176 run root:

- `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/runs/Dispatch127-176-<YYYYMMDD-HHMM>/`

Recommended minimum structure:

- `cloud-drafts/`
- `screenshots/desktop/`
- `screenshots/tablet/`
- `screenshots/mobile/`
- `audit/`
- `progress.jsonl`
- `RUN-SUMMARY.md`

Intent:

- `cloud-drafts/` stores Cloud ChatGPT Pro raw outputs and continuation fragments
- `screenshots/` stores Playwright and manual captures
- `audit/` stores visual notes, Batch2 summary, and handoff-sidecar evidence

## 2. Current Frontend Reality

The frontend is not hypothetical anymore.

Verified facts:

- `apps/capture-station` already exists
- Vite config exists
- component tests exist

Primary evidence:

- [apps/capture-station/package.json](/Users/wanglei/workspace/ScoutFlow/apps/capture-station/package.json:1)
- [apps/capture-station/vite.config.ts](/Users/wanglei/workspace/ScoutFlow/apps/capture-station/vite.config.ts:1)

Known localhost target if a dev server is later started:

- `http://127.0.0.1:4173`

## 3. What Is Ready Now

Ready now:

- raw directory conventions
- localhost target convention
- screenshot naming/layout convention
- audit output path convention
- STEP3 rule that `apps/**` touches should trigger screenshot pipeline

## 4. What Is Not Yet Honestly Runnable

Not yet ready to claim as executable fact:

- Playwright automation harness
- browser automation governance unlock
- guaranteed `pnpm dev` review flow

Reasons:

- no confirmed `playwright.config.*` or established E2E harness is present
- current authority still treats browser automation as gated/blocked
- package install/runtime state is not being asserted by STEP2

Evidence:

- [docs/current.md](/Users/wanglei/workspace/ScoutFlow/docs/current.md:20)
- [docs/shoulders-index.md](/Users/wanglei/workspace/ScoutFlow/docs/shoulders-index.md:32)

## 5. Operational Conclusion

`2A-4` can complete now as directory and naming preparation.

`2A-5` should complete now as a readiness note with this exact truth:

- frontend scaffold exists
- localhost target is known
- screenshot/audit path conventions can be prepared
- browser automation and fully runnable Playwright flow are not yet approved facts
