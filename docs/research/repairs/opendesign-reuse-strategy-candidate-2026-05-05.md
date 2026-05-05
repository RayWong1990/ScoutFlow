---
title: OpenDesign Frontend Reuse Strategy Candidate
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
migration_approval: not-approved
package_approval: not-approved
created_at: 2026-05-05
scope: Dispatch127-176 OpenDesign/frontend reuse policy candidate for STEP3 cloud prompt authoring
---

# OpenDesign Frontend Reuse Strategy Candidate

> State: candidate / not authority / not execution approval / not runtime approval / not migration approval / not package approval.
> This file is a canonical input candidate for STEP3 prompt authoring. It does not mutate V3, the STEP2 checklist, backbone taxonomy, cloud inventory, or any runtime/package surface.

## 1. Problem Framing

[tentative candidate] Dispatch127-176 needs a frontend reuse policy that Cloud GPT Pro can read before it drafts 50 dispatches. The missing question is not whether ScoutFlow has an H5 frontend. The missing question is how OpenDesign, shadcn-admin, visual language, and implementation seams enter the next cloud generation chain without turning external reference material into approved runtime dependency.

[canonical fact] The tracked frontend surface already exists under `apps/capture-station`, but its current package surface is minimal: `React 18.3.1`, `Vite 5.4.10`, and no approved shadcn, Tailwind, Panda, or token package dependency.

[tentative candidate] Therefore this document defines a reuse policy that is strong enough to improve visual quality, but narrow enough to keep package adoption, React upgrade, transplant, browser automation, and runtime approval behind later gates.

## 2. Current Truths

- [canonical fact] `docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md` is the canonical spec-level candidate for Dispatch127-176 cloud generation.
- [canonical fact] `docs/research/repairs/step3-handoff-packet-2026-05-05.md` is the STEP3 author handoff packet.
- [canonical fact] `docs/research/prototypes/h5-opendesign-probe-2026-05-04.md` and `docs/research/prototypes/opendesign-v0.3-deep-visual-probe-2026-05-05.md` keep OpenDesign as repo-external visual/prototype evidence, not tracked frontend implementation.
- [canonical fact] `docs/research/shoulders/adapt-decision-table-2026-05-05.md` makes `satnaing/shadcn-admin` the only `adapt` shoulder in that batch, limited to panel/layout/data-shell ideas.
- [canonical fact] The tracked shadcn-admin mirror records upstream `satnaing/shadcn-admin` at commit `a6352e7df0de652e4349f6bf53ca246de6ff013f` in `docs/research/shoulders/referencerepo-index-2026-05-05.md`.
- [canonical fact] Runtime, migration, vault true write, `audio_transcript`, and browser automation remain gated by current authority.
- [promoted_addendum-aware inference] PRD-v2.1 and SRD-v3 H5/Bridge are usable as B2 planning/contract addenda, but they do not approve frontend runtime, walking skeleton, vault commit, package adoption, or final visual approval.

## 3. Reuse Role Split: OpenDesign vs shadcn-admin

### 3.1 OpenDesign

[tentative candidate] OpenDesign role is:

- visual proof source
- design-language donor
- visual vocabulary candidate
- interaction-mood reference

[tentative candidate] OpenDesign is not:

- code donor
- package donor
- runtime dependency
- layout primitive donor
- information architecture owner
- CSS token contract approval

### 3.2 shadcn-admin

[tentative candidate] `satnaing/shadcn-admin` role is:

- app-shell pattern donor
- panel-system donor
- component-organization donor
- data-shell pattern donor

[tentative candidate] Its allowed reuse level is `adapt`: translate patterns into ScoutFlow-native docs/specs/tasks. It is not `transplant`: do not copy or near-copy donor files, IA, layout primitives, package assumptions, styling system, or class names as approved ScoutFlow implementation.

### 3.3 Precedence Rule

[tentative candidate] If shadcn-admin patterns produce a generic admin/dashboard tone, OpenDesign-derived operator-workstation visual policy takes precedence for visual mood only.

[tentative candidate] This visual override does not approve OpenDesign code reuse, package reuse, IA transplant, CSS token contracts, runtime dependencies, or L1/L2 ownership changes.

## 4. H5 Design Layer Ownership

[tentative candidate] H5 design presentation has three owners:

| Layer | Owner | Content | Boundary |
|---|---|---|---|
| `L1 information architecture` | ScoutFlow internal H5 IA source | four-panel flow, URL is not capture, Trust Trace is evidence/audit not decoration, preview-before-capture posture | OpenDesign and shadcn-admin must not override |
| `L2 structural components` | shadcn-admin `adapt` | app shell, panel organization, Card/Tabs/Form/Button/Table/Empty/Loading patterns | adapt only; no transplant |
| `L3 visual mood` | OpenDesign `reference` | strong visual, operator workstation mood, palette direction, spacing rhythm, typography feel, micro-interaction and motion vocabulary | visual policy only; no package/token approval |

[promoted_addendum-aware inference] L1 should be referenced as `ScoutFlow internal H5 IA source`, anchored by `T-P1A-007` and `docs/visual/h5-capture-station/design-brief.md`. This document should not restate the full T-P1A-007 history.

[tentative candidate] Cloud-generated dispatch prose for relevant H5/app/visual rows should state an affected layer note such as `Affected H5 design layer: L2+L3 mixed`. This is prose-only. It must not create a new `manifest.jsonl` field, pack_lint rule, or backbone taxonomy schema.

[tentative candidate] Mixed slots are not mixed authorization. They must be judged by layer priority:

1. `L1 IA cannot be overridden`.
2. `L2 structure may adapt shadcn-admin patterns`.
3. `L3 visual mood may override generic admin tone only`.

## 5. Technical Reuse Policy

### 5.1 Reuse Levels

[tentative candidate] Use these terms consistently:

- `reference`: may cite or observe as evidence; no code, package, IA, file-structure, or styling-system reuse.
- `adapt`: may translate patterns into ScoutFlow-native docs/specs/tasks; no direct file/package transplant.
- `transplant`: direct copy or near-copy of donor files, primitives, IA, styling system, or package assumptions.

[tentative candidate] Locked reuse posture:

- OpenDesign = `reference`.
- shadcn-admin = `adapt`.
- `transplant` = rejected by default. A future slot may only propose it as a separately gated candidate, not approve it.

### 5.2 Package and Styling

[tentative candidate] Package/styling strategy is `future strategy candidate only`:

- do not approve shadcn, Tailwind, Panda, or any other styling package
- allow future styling/token strategy candidate slots
- require those slots to align with the current `apps/capture-station` minimal surface
- do not write package install steps, default dependencies, or approved CSS token contracts

### 5.3 React Version

[canonical fact] Current tracked `apps/capture-station/package.json` uses `React 18.3.1` and `Vite 5.4.10`.

[tentative candidate] Dispatch127-176 should default to current React 18 alignment. React 19 may be proposed only as a later upgrade/spike candidate, not as a default assumption.

### 5.4 shadcn-admin Reference Freeze

[canonical fact] The tracked mirror records `satnaing/shadcn-admin` at commit `a6352e7df0de652e4349f6bf53ca246de6ff013f`.

[tentative candidate] STEP3 should cite that frozen reference when it refers to shadcn-admin. Rolling with upstream requires a later rebase/spike candidate. Cloud GPT Pro must not infer current donor behavior from a newer upstream state unless a future readback updates the frozen reference.

## 6. Engineering Seam Patches

### E1. Zero-Install Styling Layer

[tentative candidate] Because package adoption is not approved, visual slots need an explicit zero-install styling path:

- CSS Variables in `:root` for design tokens
- per-component CSS Modules using `*.module.css`
- container queries where useful for panel density and responsive behavior
- View Transition API only where it degrades safely

[tentative candidate] This is not package installation. For any future visual slot touching `apps/**`, Cloud should prefer this zero-install path unless the slot is explicitly a separately gated package strategy candidate.

### E2. Donor Freeze

[canonical fact] shadcn-admin donor evidence is frozen to commit `a6352e7df0de652e4349f6bf53ca246de6ff013f`.

[tentative candidate] Future donor refresh is a separate spike candidate. It should not be folded into visual implementation or styling/token slots.

### E3. L2/L3 Horizontal Collision Rule

[tentative candidate] When shadcn-admin L2 structure and OpenDesign L3 visual mood conflict, L3 may override visual values through CSS Variables only.

[tentative candidate] Do not fork shadcn-style component files, copy donor class names, or mutate L2 component ownership to force the visual mood. Visual override means token/value injection, not component transplant.

### E4. Visual Mode Contract

[tentative candidate] Default visual mode should be `Tech Utility / operator workstation`.

[tentative candidate] A reduced-density option should be available through CSS variables, and `prefers-reduced-motion` should be supported by default. This is a zero-install ergonomics guard for long single-operator sessions, not a second product mode or theme package approval.

### E5. Visual Touchpoint Evidence

[tentative candidate] For future visual touchpoint rows or dispatches touching `apps/**`, merge-readiness should require screenshot evidence in the raw run bundle before the row is considered visually reviewable:

- `screenshots/{slot}/desktop.png`
- `screenshots/{slot}/tablet.png`
- `screenshots/{slot}/mobile.png`

[tentative candidate] This is a candidate merge/readiness rule for future visual dispatches. It is not a present-tense browser automation unlock. If screenshot generation remains blocked by authority at execution time, the slot must stop, defer, or obtain explicit gate approval instead of pretending visual review happened.

### E6. Token Consumption

[tentative candidate] Token consumption should be CSS Variables primary and TypeScript mirror secondary:

- CSS Variables support runtime theme/density changes with near-zero runtime cost.
- `tokens.ts` may mirror token names for typed imports only.
- components must not hardcode color strings or magic number visual constants.
- if both forms exist, they should be synchronized through a build-time codegen proposal in a future candidate slot.

## 7. Visual Language Policy

[tentative candidate] The target mood is strong visual operator workstation, not generic dashboard.

[tentative candidate] Visual policy should preserve:

- visible four-panel scan order
- Trust Trace as evidence/audit surface
- blocked future lanes visible but downgraded
- dark utility base with controlled contrast
- machine-originated values readable without decorative noise
- motion used only to clarify state change

[tentative candidate] If a still or screen violates visual hierarchy, occlusion safety, and scan path together, it should be classified as a design gate failure, not a minor polish issue.

## 8. Dispatch127-176 Slot Influence

[tentative candidate] This strategy should constrain existing H5/visual backbone rows rather than add OpenDesign-specific slots.

[tentative candidate] Rows such as `128`, `140`, `152-157`, and `166-167` should be treated as high-priority beneficiaries of this policy. Any dispatch touching `apps/**` must also trigger visual review.

[tentative candidate] For any Dispatch127-176 item touching `apps/**` or marked as an H5/visual touchpoint, the dispatch body must include a `visual review required` acceptance clause. This is prose-level acceptance guidance, not a new manifest field, schema change, pack_lint rule, or global authority gate.

## 9. What Goes Into STEP3 Prompt

[tentative candidate] STEP3 prompt author should include this strategy as a canonical candidate input after it lands in `docs/research/repairs/step3-handoff-packet-2026-05-05.md`.

[tentative candidate] The prompt should tell Cloud GPT Pro:

- consume this policy while drafting Dispatch127-176
- do not rewrite this policy into authority
- do not decide the input package itself
- mark affected H5 layers in relevant dispatch prose
- keep visual review clauses in relevant dispatch acceptance sections
- keep package, React, transplant, and runtime changes as separately gated candidates

## 10. Reject List

[tentative candidate] Cloud GPT Pro must not:

- turn OpenDesign into a ScoutFlow runtime dependency
- install shadcn, Tailwind, Panda, or any styling package
- upgrade React or Vite by default
- transplant donor files, IA, layout primitives, class names, or package assumptions
- inherit generic admin/dashboard IA
- write repo-external prototypes as tracked ScoutFlow implementation facts
- write visual proof as implementation approval
- create a new manifest field, pack_lint rule, or backbone taxonomy schema for H5 design layer notation
- treat browser automation or screenshot generation as already approved current fact
- hardcode donor behavior from an upstream commit newer than the frozen reference without a future readback

## 11. Future Amend Target

[tentative candidate] If this candidate is accepted, the only immediate tracked amend target is:

- `docs/research/repairs/step3-handoff-packet-2026-05-05.md`

[tentative candidate] Amend exactly two areas:

1. Add this document to the canonical input list.
2. Add one assumption sentence summarizing the OpenDesign/shadcn-admin/H5 layer boundary.

[tentative candidate] Do not amend V3, the STEP2 checklist, backbone taxonomy, or cloud input package inventory in this pass.

## 12. Prompt-ready Frontend Reuse Policy Block

[tentative candidate] The following block may be copied into the Cloud GPT Pro dispatch-authoring prompt. It is not authority, runtime approval, package approval, schema change, or implementation instruction.

```text
Frontend reuse policy is a hard constraint for Dispatch127-176 authoring.

OpenDesign is only the L3 visual proof source, design-language donor, visual vocabulary candidate, and interaction-mood reference. It is not a ScoutFlow runtime dependency, package dependency, code donor, layout primitive donor, information architecture owner, or approved implementation source.

satnaing/shadcn-admin is the L2 app-shell, panel-system, component-organization, and data-shell pattern donor, frozen to commit a6352e7df0de652e4349f6bf53ca246de6ff013f for this candidate. It may be adapted into ScoutFlow-native dispatch/spec language, but it must not be transplanted as files, IA, package assumptions, class names, or default styling stack.

L1 H5 information architecture remains owned by ScoutFlow internal H5 IA sources, anchored by T-P1A-007 and docs/visual/h5-capture-station/design-brief.md. OpenDesign and shadcn-admin must not override L1.

If shadcn-admin patterns produce a generic admin/dashboard tone, OpenDesign-derived operator-workstation visual policy takes precedence for visual mood only. This visual override does not approve OpenDesign code reuse, package reuse, IA transplant, CSS token contracts, component forks, runtime dependency changes, or L1/L2 ownership changes.

For relevant H5/app/visual dispatches, include an affected layer prose note such as "Affected H5 design layer: L2+L3 mixed". Do not add a manifest field, pack_lint rule, or backbone taxonomy schema for this.

For any dispatch touching apps/** or marked as an H5/visual touchpoint, include a "visual review required" acceptance clause. Merge-readiness for future visual rows should expect raw-run screenshot evidence at screenshots/{slot}/desktop.png, screenshots/{slot}/tablet.png, and screenshots/{slot}/mobile.png, unless screenshot generation remains gated and the slot explicitly stops or defers.

For Dispatch127-176, Cloud GPT Pro may propose visual touchpoint slots and styling/token strategy candidate slots. It must not write package.json changes, approve shadcn/Tailwind/Panda adoption, upgrade React, transplant donor files/IA/layout primitives, or treat any frontend package/styling system as already approved.

All frontend continuation dispatches must align with the currently tracked apps/capture-station minimal surface unless a future slot explicitly requests a separately gated candidate for package strategy, token strategy, React upgrade, donor refresh, screenshot automation, or transplant review.
```

## 13. Decision Ledger

| # | Decision | Locked choice | Boundary |
|---|---|---|---|
| D1 | OpenDesign role | `visual proof source + design-language donor + visual vocabulary candidate` | not code/package/runtime/layout donor |
| D2 | Cloud entry layer | local candidate doc + local lightweight handoff amend | Cloud consumes policy; Cloud does not decide policy integration |
| D3 | donor split | hard split + limited visual override | shadcn-admin owns structure; OpenDesign owns visual mood |
| D4 | reuse level | OpenDesign=`reference`; shadcn-admin=`adapt`; transplant rejected by default | future transplant only as separately gated candidate |
| D5 | package/styling | future strategy candidate only | no shadcn/Tailwind/Panda package approval |
| D6 | React posture | current React 18 alignment | React 19 only later spike/candidate |
| D7 | STEP3 prompt | `Frontend Reuse Policy` hard clause | prompt constraint, not runtime approval |
| D8 | visual slot influence | constrain existing H5/visual rows | no OpenDesign-only slot expansion |
| D9 | reject list | full reject list, no Cloud carve-out | no package/upgrade/transplant/admin IA drift |
| D10 | amend target | only `step3-handoff-packet-2026-05-05.md` two areas | do not reopen V3/STEP2/backbone/inventory |
| D11 | claim labeling | label key conclusions | `canonical fact` / `promoted_addendum-aware inference` / `tentative candidate` |
| D13 | H5 design layer ownership | L1 internal / L2 shadcn-admin / L3 OpenDesign | mixed slots judged by L1 > L2 > L3 |
| D13a | layer notation | prose-only affected layer note | no schema/manifest change |
| D13b | L1 source mention | mention T-P1A-007 + design brief | internal H5 IA source only |
| D14 | visual review acceptance | `apps/**` or H5 visual touchpoint must include `visual review required` | prose-level acceptance only |
| D15 | prompt-ready clause | allowed in this candidate doc | tentative candidate; not authority/runtime/package/schema approval |
| E1 | zero-install styling | CSS Variables + CSS Modules + container queries + safe View Transition API | no package install |
| E2 | donor freeze | shadcn-admin frozen to `a6352e7df0de652e4349f6bf53ca246de6ff013f` | future upstream refresh is separate spike |
| E3 | L2/L3 collision | L3 values override through CSS Variables only | no component fork/transplant |
| E4 | visual modes | default Tech Utility + reduced-density variables + reduced-motion support | no theme package approval |
| E5 | visual evidence | future visual rows expect desktop/tablet/mobile screenshots in raw run bundle | not current browser automation unlock |
| E6 | token consumption | CSS Variables primary + `tokens.ts` mirror secondary | no hardcoded visual constants |

## 14. Self-Review Notes

- [tentative candidate] This document does not approve runtime, package install, migration, browser automation, vault true write, or React upgrade.
- [tentative candidate] This document does not modify V3, STEP2 checklist, backbone taxonomy, or cloud input package inventory.
- [tentative candidate] D12 is intentionally unused after brainstorm numbering correction; new H5 layer ownership starts at D13.
