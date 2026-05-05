# Batch3 PR140 Pre-merge Audit Repair Scope Note

> Status: repair-scope-note / not authority / not runtime approval / not visual approval
> Date: 2026-05-05
> Scope: pre-merge repair for Wave 4 Batch 3 GitHub-only audit findings

## Purpose

This note records the exact tracked paths allowed for the pre-merge audit repair that addresses:

- frontend commit dry-run response contract alignment
- visual reporting GitHub-only portability
- no runtime, no browser automation, no vault true write approval

## Allowed app paths for this repair

- `apps/capture-station/src/lib/api-client.ts`
- `apps/capture-station/src/features/vault-commit/VaultCommitDryRunButton.tsx`

## Allowed test path for this repair

- `tests/e2e/test_h5_bridge_commit_dry_run_placeholder.py`

## Allowed docs paths for this repair

- `docs/research/prototypes/visual-regression-reporting-2026-05-05.md`
- `docs/research/repairs/batch3-pr140-premerge-audit-repair-scope-note-2026-05-05.md`

## Boundary

- This note is a repair scope note only.
- It does not promote H5 preview or H5 commit surfaces to final authority.
- It does not approve live H5 to Bridge request wiring.
- It does not approve actual vault writes.
- It does not approve browser automation, Playwright execution, screenshot generation, human visual verdict, migration, BBDown live runtime, yt-dlp, ffmpeg, ASR, or `audio_transcript` runtime.
- It does not change PRD/SRD baseline authority.
