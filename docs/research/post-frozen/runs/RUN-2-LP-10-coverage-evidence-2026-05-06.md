---
title: RUN-2 LP-10 Coverage Evidence under PR #228
status: candidate / forensic_evidence / covered_by_228
date: 2026-05-06
dispatch: PF-LP-10
verdict: COVERED_BY_228
source_pr: 228
source_merge_commit: bd1f38241f613b0766704af1173f3e1760e8ab93
---

# PF-LP-10 Coverage Verdict

- verdict: `COVERED_BY_228`
- dispatch goal: add a download `.md` action to `VaultPreviewPanel.tsx` with a safe `scoutflow-preview-{capture_id}.md` filename
- allowed-path check: PR `#228` modified `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx` and `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx`, which stays inside PF-LP-10 `files_to_modify`

## Implementation evidence

- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:16-18` adds `sanitizeDownloadFilename(...)`
- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:33-36` derives the download filename from real preview state
- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:51-64` creates a markdown `Blob`, uses an anchor download, and reports `Downloaded {filename}.`
- `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx:121-137` wires the `Download .md` button and keeps it disabled until `hasPreview`

## Acceptance assertion evidence

1. Disabled until real markdown exists:
   `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx:45-50`
2. Exact markdown blob payload:
   `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx:93-129`
3. Safe filename generation:
   `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx:115-133`

## Classification note

- No authority file was touched for this verdict.
- No true vault write, runtime approval, or browser automation is implied.
