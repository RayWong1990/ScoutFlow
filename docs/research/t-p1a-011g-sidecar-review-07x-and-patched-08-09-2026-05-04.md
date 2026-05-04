# T-P1A-011G Sidecar Review — 07.x + Patched 08/09 — 2026-05-04

T-P1A-011G sidecar review complete.

Verdict: `PASS_WITH_FIXES`

Blocking issues:

- none

Non-blocking issues:

- pre-review authority docs still framed `T-P1A-011C` as the current end state and had not yet written back `T-P1A-011D/E/F` completion or patched `08/09` readiness

Evidence:

- `docs/research/t-p1a-011d-second-retro-remediation-triage-2026-05-04.md` confirmed `011` blocked / `011B` done / `011C` success and locked `012/013` numbering
- `docs/retro/README.md` and `docs/retro/2026-05-04-week-1.md` kept retro scope minimal and did not expand into a 19-file governance package
- `/Users/wanglei/Downloads/scoutflow-dispatch-7x-to-09-patched-pack/08-dispatch-t-p1a-012-metadata-receipt-ledger-wiring-PATCHED.md` depends on `011C` evidence and forbids new BBDown runtime
- `/Users/wanglei/Downloads/scoutflow-dispatch-7x-to-09-patched-pack/09-dispatch-t-p1a-013-explore-trust-trace-minimal-PATCHED.md` separates probe evidence / receipt ledger / capture state / media-audio readiness
- `docs/current.md`, `docs/task-index.md`, `docs/decision-log.md`, `AGENTS.md`, and `README.md` were synced in this branch to remove the stale `011C-only` focus

Minimal fix:

- sync repo authority docs to `07.x remediation complete`
- keep `T-P1A-012` and `T-P1A-013` reserved for patched Dispatch 08/09
- leave legal/vendor notes as optional candidate-only `011H`, not a pre-08 blocker

Dispatch 08 readiness:

- `ready`

Dispatch 09 readiness:

- `ready`

Still not approved:

- new live BBDown
- new `BBDown -info`
- media download
- ffmpeg
- ASR
- QR/login
- browser profile
- `audio_transcript`
- frontend / workers without explicit dispatch approval
- legal/vendor authority claims without verification
