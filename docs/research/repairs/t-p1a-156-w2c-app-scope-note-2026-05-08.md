# T-P1A-156 W2C App Scope Note

state: `repair-scope-note`
date: `2026-05-08`
task_id: `T-P1A-156`
lane: `W2C PF-C4-02 real-data wiring`
source_spec: `docs/research/post-frozen/2026-05-08/W2-w2c/01-w2c-cluster-spec.md`
source_dispatch: `docs/research/post-frozen/2026-05-08/W2-w2c/02-w2c-dispatch-pack.md`

## Scope

This note records the explicit tracked `apps/**` write scope added by the W2C implementation branch. These paths are frontend/runtime adapter and test-only surfaces inside `apps/capture-station/**`; they do not authorize `services/**`, authority files, runtime unlock, migrations, browser automation, or true vault write.

- allowed path: `apps/capture-station/src/components/AppShell/AppShellOverview.test.tsx`
- allowed path: `apps/capture-station/src/features/capture-plan/CapturePlan.test.tsx`
- allowed path: `apps/capture-station/src/features/capture-scope/CaptureScope.test.tsx`
- allowed path: `apps/capture-station/src/features/live-metadata/LiveMetadata.test.tsx`
- allowed path: `apps/capture-station/src/features/signal-hypothesis/SignalHypothesis.test.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-preview/TopicCardLite.test.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTrace.test.tsx`
- allowed path: `apps/capture-station/src/features/url-bar/w2cSurfaceState.ts`
- allowed path: `apps/capture-station/src/features/vault-commit/VaultCommit.test.tsx`
- allowed path: `apps/capture-station/src/features/vault-preview/VaultPreview.test.tsx`
- allowed path: `apps/capture-station/src/lib/w2c-runtime.test.tsx`
- allowed path: `apps/capture-station/src/lib/w2c-runtime.tsx`

## Boundary

- This note is a dispatch/repair scope note only.
- It does not promote W2C candidate/receipt materials to authority.
- It does not approve `write_enabled=true`, true vault commit, ASR/runtime tools, browser automation, migration, or Trust Trace graph/timeline/error-path implementation.
