---
title: ScoutFlow OpenDesign v0.3 Deep Visual Probe
date: 2026-05-05
type: prototype-probe-report
status: candidate / repo-external-prototype / not-authority / not-runtime-approval / not-frontend-implementation-approval
wave: 3B
related_task: T-P1A-057
---

# ScoutFlow OpenDesign v0.3 Deep Visual Probe

## Scope

- This dispatch deepens the earlier OpenDesign still/probe lane by reading the repo-external Vite/React mock rather than only pointing at it.
- Tracked repo output remains limited to this report; no frontend code is copied into ScoutFlow.
- The goal is visual/prototype evidence only, not implementation approval.

## Inputs

- The earlier OpenDesign v0 report already locked the four-panel operator posture, the right-column trust-trace emphasis, and the repo-external isolation rule ([docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L73-L83](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L123-L147](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md)).
- The tracked mock pointer confirms a repo-external Vite/React mock exists under `/Users/wanglei/workspace/scoutflow-prototypes/h5-capture-station-mock/` ([docs/research/h5-prototype-mock-pointer-2026-05-05.md:L1-L2](docs/research/h5-prototype-mock-pointer-2026-05-05.md)).
- The repo-external mock README and audit file make the artifact set explicit and keep the five-gate result attached to the mock itself ([../../scoutflow-prototypes/h5-capture-station-mock/README.md:L1-L16](../../scoutflow-prototypes/h5-capture-station-mock/README.md), [../../scoutflow-prototypes/h5-capture-station-mock/five-gate-audit.md:L1-L9](../../scoutflow-prototypes/h5-capture-station-mock/five-gate-audit.md)).
- The tracked design brief, trust-trace graph spec, and five-gate checklist define the visual contract that the mock must satisfy ([docs/visual/h5-capture-station/design-brief.md:L35-L60](docs/visual/h5-capture-station/design-brief.md), [docs/visual/h5-capture-station/trust-trace-graph-spec.md:L14-L27](docs/visual/h5-capture-station/trust-trace-graph-spec.md), [docs/visual/h5-capture-station/five-gate-checklist.md:L5-L18](docs/visual/h5-capture-station/five-gate-checklist.md), [docs/visual/h5-capture-station/five-gate-checklist.md:L27-L58](docs/visual/h5-capture-station/five-gate-checklist.md)).

## Batch verdict

| artifact | decision | integration proposal | confidence | next_action |
|---|---|---|---:|---|
| `OpenDesign v0.3 deep visual probe` | continue | `reference_only -> design/input carry-forward` | 0.83 | keep repo-external mock as strongest visual proof source |

## Probe findings

### shoulder OPENDESIGN / repo-external H5 mock

Decision: keep the repo-external H5 mock as the strongest current visual proof source and treat it as the `v0.3 deep` upgrade over the earlier still/probe lane.

Why:

- The mock is no longer just a pointer: `src/App.tsx` implements the exact four-panel operator surface with a full-width URL bar, three-column lower grid, explicit `metadata_only/receipt_ledger/vault_commit/audio_transcript` scope stack, and a seven-node trust-trace chain (`capture -> capture_state -> metadata_job -> probe_evidence -> receipt_ledger -> media_audio -> audit`) ([../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L29-L45](../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L29-L45), [../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L58-L105](../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L58-L105), [../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L122-L180](../../scoutflow-prototypes/h5-capture-station-mock/src/App.tsx:L122-L180)).
- That structure matches the tracked design contract closely: the design brief requires a four-panel operator surface and the trust-trace spec requires the same canonical node chain with blocked-layer visibility preserved ([docs/visual/h5-capture-station/design-brief.md:L35-L60](docs/visual/h5-capture-station/design-brief.md), [docs/visual/h5-capture-station/trust-trace-graph-spec.md:L14-L27](docs/visual/h5-capture-station/trust-trace-graph-spec.md), [docs/visual/h5-capture-station/trust-trace-graph-spec.md:L40-L61](docs/visual/h5-capture-station/trust-trace-graph-spec.md)).
- The repo-external audit also clears all five visual gates at mock level: hierarchy, spacing/alignment, occlusion safety, typography legibility, and visual weight ([../../scoutflow-prototypes/h5-capture-station-mock/five-gate-audit.md:L1-L9](../../scoutflow-prototypes/h5-capture-station-mock/five-gate-audit.md), [docs/visual/h5-capture-station/five-gate-checklist.md:L5-L18](docs/visual/h5-capture-station/five-gate-checklist.md), [docs/visual/h5-capture-station/five-gate-checklist.md:L27-L58](docs/visual/h5-capture-station/five-gate-checklist.md)).
- Compared with the earlier v0 still/probe report, the mock provides stronger evidence because it expresses layout, blocked-state hierarchy, and right-column graph composition in code rather than prose alone, while still honoring the repo-external isolation rule ([docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L51-L56](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md), [docs/research/prototypes/h5-opendesign-probe-2026-05-04.md:L127-L145](docs/research/prototypes/h5-opendesign-probe-2026-05-04.md)).

Carry-forward:

- keep the repo-external mock as the primary visual proof source
- preserve the four-panel operator layout and canonical trust-trace chain
- keep blocked future lanes visible but visually downgraded
- do not promote the mock into tracked frontend implementation from this report alone

## Result

This dispatch clears a narrow but real upgrade:

- `v0.3 deep` now has code-level mock evidence
- tracked ScoutFlow diff is still report-only
- the visual contract is stronger, but frontend implementation remains gated
