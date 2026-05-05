# ScoutFlow Wave 4 Entry Gate

> Status: research-only / authority support / not-runtime-approval
> Task: `T-P1A-072`

## 1. Gate Basis

Wave 4 entry is opened on top of the already landed authority truth:

- `T-P1A-103`
- `B2_PREFLIGHT_CLOSED`
- `B2_COMMANDER_READY`
- `user_override_for_B2_preflight`

This means the control-plane and planning/contract baseline are sufficient to start bounded Wave 4 dispatch execution.
It does **not** mean walking skeleton, frontend runtime, bridge runtime, vault commit, migration, or media/runtime lanes are already approved.

## 2. What Opens

- `T-P1A-073 ~ T-P1A-085` may proceed under their own explicit dispatch boundaries
- `apps/**` and `services/**` are no longer blanket-forbidden, but remain dispatch-path-gated
- authority writer remains serial and exclusive

## 3. What Stays Gated

- `workers/**`
- `packages/**`
- `services/api/migrations/**`
- `data/**`
- `referencerepo/**`
- BBDown live / yt-dlp / ffmpeg / ASR / browser automation
- any unscoped frontend/runtime implementation

## 4. Next Gate

Current next gate after Wave 4 entry open:

- `T-P1A-073 / slot-label PR #98`
- topic: `Capture Station App Scaffold`

## 5. Carry-forward

Use this note as the authority-support explanation for why Wave 4 code-bearing slots can start without re-arguing the B2 preflight truth each time.
