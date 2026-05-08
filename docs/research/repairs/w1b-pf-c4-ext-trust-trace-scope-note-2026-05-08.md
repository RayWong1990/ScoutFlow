# W1B PF-C4-EXT Trust Trace Scope Note

state: `repair-scope-note`
date: `2026-05-08`
lane: `W1B PF-C4-EXT`
source_spec: `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/01-w1b-cluster-spec.md`
source_dispatch: `docs/research/post-frozen/2026-05-08/W1B-opendesign-reuse-v2/02-w1b-dispatch-pack.md`

## Scope

This note records the explicit tracked `apps/**` write scope for the W1B trust-trace lane implementation. These paths are limited to the Trust Trace shell plus the three bounded lane components and their tests/styles. They do not authorize `services/**`, authority files, runtime unlock, browser automation, migration, or true vault write.

- allowed path: `apps/capture-station/src/features/trust-trace/TrustTrace.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTrace.test.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/GraphLane.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/GraphLane.module.css`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/GraphLane.test.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.module.css`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/TimelineLane.test.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.module.css`
- allowed path: `apps/capture-station/src/features/trust-trace/lanes/ErrorPathLane.test.tsx`
- allowed path: `docs/research/repairs/w1b-pf-c4-ext-trust-trace-scope-note-2026-05-08.md`

## Boundary

- This note is a dispatch/repair scope note only.
- It does not approve `write_enabled=true`, runtime tools, browser automation, migration, or true vault write.
- It does not promote W1B candidate docs or receipts to authority.
