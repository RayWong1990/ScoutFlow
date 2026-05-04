---
title: ScoutFlow OpenDesign H5 Visual Probe
date: 2026-05-04
task: T-P1A-036
pr: PR #61
status: prototype-report-only / not-authority / not-runtime-approval / not-frontend-implementation-approval
artifact_mode: repo_external_prototype
---

# ScoutFlow OpenDesign H5 Visual Probe

## 1. Scope

This report records the `PR61 / T-P1A-036` repo-external prototype lane only. Tracked ScoutFlow diff is intentionally limited to this file. No frontend code, daemon output, or upstream source is written into the ScoutFlow repo.

## 2. Dispatch authority

- dispatch: `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/PR61-T-P1A-036-opendesign-h5-visual-probe.md`
- worktree: `/Users/wanglei/workspace/ScoutFlow-PR61`
- branch: `task/T-P1A-036-opendesign-h5-visual-probe`
- baseline gate: `554f497feb31e60022542eb06bf21a74487e4e09` is ancestor of `HEAD`

## 3. Source inputs used

- `docs/architecture/baseline-roadmap-after-pr54-candidate-2026-05-04.md`
  - section 1.1 defines the 4-panel H5 operator story
  - section 2 locks the H5 stack and trust-trace position
- `docs/PRD-v2-2026-05-04.md`
  - section 5.3 separates `probe evidence`, `receipt ledger`, `capture state`, and `media/audio readiness`
  - section 6.1 locks the current metadata-only proof path
- `docs/SRD-v2-2026-05-04.md`
  - section 2.4 through 2.6 locks the layered trust-trace DTOs and phase split
- `docs/research/pr55-pr74-worklist-candidate-2026-05-04.md`
  - section 6 defines the OpenDesign probe deliverable and repo-external boundary
- `docs/architecture/shoulders-lifecycle-handbook-candidate-2026-05-04.md`
  - section 9.2 classifies OpenDesign as `reference (repo 外 prototype)`
- `~/.claude/rules/aesthetic-first-principles.md`
  - 5 Gate audit basis

## 4. Numbering drift note

`dispatch` and current ScoutFlow ledger map `PR #61 / T-P1A-036` to the OpenDesign H5 visual probe. The older `worklist` still contains a stale row that used `T-P1A-036` for a different shoulder-scan item, while its detailed section 6 already describes the OpenDesign probe. This implementation follows the dispatch and current ledger authority, not the stale summary row.

## 5. Upstream and license isolation

- upstream reference: `https://github.com/nexu-io/open-design`
- local read-only clone: `/Users/wanglei/workspace/ScoutFlow/referencerepo/open-design/`
- observed license file: `/Users/wanglei/workspace/ScoutFlow/referencerepo/open-design/LICENSE`
- license posture: Apache-2.0 upstream, used here as read-only visual/process reference

Isolation rules applied in this PR:

1. No upstream source file is copied into ScoutFlow tracked paths.
2. No OpenDesign daemon output is written into `apps/`, `services/`, `workers/`, or any ScoutFlow tracked frontend path.
3. Prototype source stays under `~/workspace/scoutflow-prototypes/h5-capture-station/`.
4. The ScoutFlow repo keeps only this report as a research/prototype artifact.

## 6. Repo-external artifact set

All prototype outputs live in:

`/Users/wanglei/workspace/scoutflow-prototypes/h5-capture-station/`

Files produced:

1. `capture-station-v0.html`
2. `capture-station-v0.png`
3. `design-tokens.json`
4. `state-machine-vis-spec.md`
5. `trust-trace-live-spec.md`
6. `five-gate-audit.md`

## 7. Visual decisions extracted

### 7.1 Layout

- 4-panel structure kept explicit:
  - top bar = `URL Bar`
  - lower left = `Live Metadata`
  - lower middle = `Capture Scope`
  - lower right = `Trust Trace`
- No sidebar and no dashboard chrome. The composition is a single operator surface, not an admin shell.
- Trust Trace takes the widest column, but the capture action remains the first visual stop.

### 7.2 Color

- canvas: dark blue-black base to keep the prototype in workstation territory
- active proof path: cyan / green
- gated receipt state: amber
- blocked future lanes: muted red
- focus transition: restrained violet

### 7.3 Typography

- display/title/body/caption scale: `28 / 20 / 14 / 12`
- display and body stack stay sans-serif; monospace only marks machine-originated content like URL/ticks
- copy avoids authority words such as `done`, `production-ready`, or `approved`

### 7.4 State visibility

- `audio_transcript` remains visible but downgraded as blocked
- receipt and trust trace are separate visual objects
- audit exists in the graph but remains secondary weight

## 8. Five Gate result

Artifact self-audit is recorded in:

`/Users/wanglei/workspace/scoutflow-prototypes/h5-capture-station/five-gate-audit.md`

Summary:

| Gate | Result | Note |
|---|---|---|
| Visual Hierarchy | pass | URL action first, graph second |
| Spacing & Alignment | pass | fixed rhythm, aligned panel grid |
| Occlusion Safety | pass | no overlays crossing critical data |
| Typography Legibility | pass | contrast and scale kept readable |
| Visual Weight | pass | blocked lanes downgraded, action emphasized |

Overall: `5/5 pass`

## 9. Prototype boundaries

What this probe does:

- tests whether ScoutFlow's H5 capture surface can hold a strong-visual direction without drifting into marketing hero or SaaS dashboard patterns
- extracts reusable tokens and state-machine/trust-trace visual contracts for later waves
- records a safe license/source isolation pattern for using OpenDesign as a shoulder

What this probe does not do:

- approve any runtime
- create `apps/capture-station/`
- approve browser automation, BBDown live, media download, ffmpeg, ASR, or vault auto-commit
- modify `docs/current.md`, `docs/task-index.md`, `docs/specs/**`, `services/**`, `apps/**`, or `workers/**`

## 10. Verdict

`verdict=clear` for the narrow scope of this prototype lane:

- repo-external six-piece artifact set exists
- tracked repo diff remains a single report file
- OpenDesign source remains isolated
- Five Gate self-audit clears the still/prototype threshold

Any move from this still/probe lane to real ScoutFlow frontend code requires a later dispatch and separate approval.
