---
title: STEP3 Handoff Packet
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: STEP2 item 2B-4 handoff to STEP3 prompt author
---

# STEP3 Handoff Packet

> State: candidate / not authority / not execution approval.

## 1. What STEP3 Author Must Read

Canonical:

1. [dispatch127-176-pack-design-v3-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/dispatch127-176-pack-design-v3-2026-05-05.md:1)
2. [step2-prep-checklist-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/step2-prep-checklist-2026-05-05.md:1)
3. [batch2-audit-summary-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/batch2-audit-summary-2026-05-05.md:1)
4. [readback-manifest-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/readback-manifest-2026-05-05.md:1)
5. [backbone-taxonomy-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/backbone-taxonomy-2026-05-05.md:1)
6. [cloud-input-package-inventory-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/cloud-input-package-inventory-2026-05-05.md:1)
7. [opendesign-reuse-strategy-candidate-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/opendesign-reuse-strategy-candidate-2026-05-05.md:1)

Supporting:

1. [step2-local-mode-and-packlint-surface-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/step2-local-mode-and-packlint-surface-2026-05-05.md:1)
2. [step2-runtime-readiness-and-screenshot-note-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/step2-runtime-readiness-and-screenshot-note-2026-05-05.md:1)
3. [step2-runner-api-disk-budget-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/step2-runner-api-disk-budget-2026-05-05.md:1)
4. [wave5-scope-and-template-extraction-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow/docs/research/repairs/wave5-scope-and-template-extraction-2026-05-05.md:1)

## 2. What STEP3 Author Must Assume

- Cloud ChatGPT Pro accesses GitHub-visible files
- `V3` is the only canonical spec-level design doc
- `V1/V2` are archive-only context, not primary inputs
- Batch2 is terminal enough for cloud drafting
- Dispatch125 terminal is still the later execution gate
- local Codex mode is required for later commander execution
- `pack_lint v2.5` is still a defined upgrade surface, not yet implemented
- `product_lane_max=5` is a run-only override candidate, not a global default
- current runner/API evidence supports `10`, maybe `12` after health checks, not a proven `20`
- OpenDesign/shadcn-admin frontend reuse policy is a candidate input only: L1 H5 IA remains ScoutFlow-owned, L2 structure may adapt shadcn-admin patterns, and L3 visual mood may reference OpenDesign without approving package, runtime, transplant, or React upgrade.

## 3. What STEP3 Author Must Not Do

- do not treat candidate addenda as globally promoted base docs
- do not hardcode live GitHub PR numbers in dependency fields
- do not paste raw credentials, token material, or unsafe stdout
- do not assume browser automation is already approved fact
- do not assume `BBDown live`, `audio_transcript`, migrations, or vault true write are unlocked

## 4. Expected Cloud Outputs

Cloud draft should eventually produce:

- full `dispatch.md` files
- `manifest.jsonl`
- `worklist-amendment.md`
- `COMMANDER-RUN-PROMPT.md`
- archived candidate pack at `/Users/wanglei/workspace/raw/05-Projects/ScoutFlow/dispatches/packs/ScoutFlow-Dispatch127-176-candidate-pack/`
- optional packaging/continuation artifacts

## 5. Current Status

`STEP2A` is complete.

`STEP2B` has produced:

- Batch2 summary
- readback manifest
- cloud input inventory
- backbone taxonomy
- this handoff packet

Remaining work after this packet is PR/merge visibility for the `2B-*` artifacts if Cloud ChatGPT Pro must consume them through GitHub.
