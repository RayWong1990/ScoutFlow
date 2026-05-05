---
title: Batch2 Stage A Node And Slot98 Correction
status: candidate
authority: not-authority
execution_approval: not-approved
runtime_approval: not-approved
created_at: 2026-05-05
scope: historical correction note for Batch2 Stage A Node validation and slot98 repair wording
depends_on: PR #119
---

# Batch2 Stage A Node And Slot98 Correction

> State: candidate / not authority / historical correction note.

## Boundary

This note records the current historical interpretation after PR #119. It does not rewrite the original Batch2 report, checkpoint, diff bundle, RAW dispatch pack, or task authority surfaces.

This note is not:

- an execution approval
- a runtime unlock
- a migration approval
- a bridge/vault write approval
- a replacement for the original Batch2 report

## Corrected Reading

The #118 Batch2 summary remains historical and is not rewritten in place. Its statement that the slot98 repair only added `apps/capture-station/index.html` was incomplete when compared with the later b2v4 working pack and merge evidence.

The slot98 b2v4 scope added exactly these two paths:

- `apps/capture-station/index.html`
- `tools/check-docs-redlines.py`

This correction matters because `tools/check-docs-redlines.py` is an authority-surface validator. Treating that path as absent from the repair scope would understate the control-plane change that made slot98 mergeable.

## Stage A Node Boundary

Stage A Node validation was not proven by the original Batch2 terminal report. The original evidence still has to be read as a historical run report, not as proof that Node tests and production bundle cleanliness were already clear.

PR #119 supplied the later repair evidence:

- `FourPanelShell` narrowed its Vite glob so production bundle discovery no longer includes `*.test.tsx`.
- `LiveMetadataPanel` aligned the controlled label to `audio_transcript`.
- Stage A Node tests and build evidence were rerun in the follow-up repair note.

That later evidence repairs the Stage A Node blocker on the PR #119 baseline. It does not retroactively make the original Batch2 report a Node-validation proof.

## Bridge Runtime Boundary

Bridge code remains tracked under `services/api/scoutflow_api/bridge/**`, but it is still unmounted from `services/api/scoutflow_api/main.py`. The current `main.py` includes only the captures and jobs routers.

Therefore this correction does not unlock:

- bridge runtime
- vault true write
- migration work
- BBDown / yt-dlp / ffmpeg / ASR
- `audio_transcript` runtime

## Evidence Pointers

- [batch2-audit-summary-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow-PR121-batch2-correction/docs/research/repairs/batch2-audit-summary-2026-05-05.md:1)
- [wave4-batch2-stageA-node-and-slot98-fixup-2026-05-05.md](/Users/wanglei/workspace/ScoutFlow-PR121-batch2-correction/docs/research/repairs/wave4-batch2-stageA-node-and-slot98-fixup-2026-05-05.md:1)
- [main.py](/Users/wanglei/workspace/ScoutFlow-PR121-batch2-correction/services/api/scoutflow_api/main.py:1)

## Practical Consequence

Future Batch2 readbacks should use this narrower interpretation:

- Batch2 reached a terminal report state.
- slot98 repair scope included `apps/capture-station/index.html` and `tools/check-docs-redlines.py`.
- Stage A Node validation was repaired by PR #119, not proven by the original Batch2 run.
- Runtime, migration, bridge/vault write, and `audio_transcript` remain gated.
