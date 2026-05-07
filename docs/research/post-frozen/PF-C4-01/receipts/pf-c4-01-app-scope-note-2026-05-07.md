# PF-C4-01 app scope note

```yaml
status: candidate_scope_note_not_authority
lane: PF-C4-01
source_dispatch: docs/research/post-frozen/80-pack-source/02_task_packs/PF-C4-controlled-hardening-pack/dispatches/PF-C4-01-local-frontend-dependency-bootstrap-repair.md
boundary: apps/capture-station only
runtime_unlock: false
authority_write: false
```

This note records the explicit `apps/capture-station/**` write scope used by PF-C4-01. The lane replaces earlier placeholder/candidate app surfaces with the new P7-driven TSX/CSS Module shell, and removes superseded tracked placeholders in the same bounded app subtree. No `services/**`, `workers/**`, `packages/**`, authority files, runtime unlock, migration, or true vault write is involved.

- allowed path: `apps/capture-station/pnpm-lock.yaml`
- allowed path: `apps/capture-station/src/App.tsx`
- allowed path: `apps/capture-station/src/App.test.tsx`
- allowed path: `apps/capture-station/src/main.tsx`
- allowed path: `apps/capture-station/src/assets/icons/system.svg`
- allowed path: `apps/capture-station/src/assets/icons/state.svg`
- allowed path: `apps/capture-station/src/styles/tokens/tokens.css`
- allowed path: `apps/capture-station/src/styles/tokens/density-compact.css`
- allowed path: `apps/capture-station/src/styles/tokens/type-weight-heavy.css`
- allowed path: `apps/capture-station/src/styles/tokens/README.md`
- allowed path: `apps/capture-station/src/components/AppShell/AppShell.tsx`
- allowed path: `apps/capture-station/src/components/AppShell/AppShell.module.css`
- allowed path: `apps/capture-station/src/components/AppShell/AppShellOverview.tsx`
- allowed path: `apps/capture-station/src/components/AppShell/AppShellOverview.module.css`
- allowed path: `apps/capture-station/src/components/Button/Button.tsx`
- allowed path: `apps/capture-station/src/components/Button/Button.module.css`
- allowed path: `apps/capture-station/src/components/CaptureIdChip/CaptureIdChip.tsx`
- allowed path: `apps/capture-station/src/components/CaptureIdChip/CaptureIdChip.module.css`
- allowed path: `apps/capture-station/src/components/EvidenceTable/EvidenceTable.tsx`
- allowed path: `apps/capture-station/src/components/EvidenceTable/EvidenceTable.module.css`
- allowed path: `apps/capture-station/src/components/FrontmatterBlock/FrontmatterBlock.tsx`
- allowed path: `apps/capture-station/src/components/FrontmatterBlock/FrontmatterBlock.module.css`
- allowed path: `apps/capture-station/src/components/GovernanceTooltip/GovernanceTooltip.tsx`
- allowed path: `apps/capture-station/src/components/GovernanceTooltip/GovernanceTooltip.module.css`
- allowed path: `apps/capture-station/src/components/Icon/Icon.tsx`
- allowed path: `apps/capture-station/src/components/Icon/Icon.module.css`
- allowed path: `apps/capture-station/src/components/LifecycleStepper/LifecycleStepper.tsx`
- allowed path: `apps/capture-station/src/components/LifecycleStepper/LifecycleStepper.module.css`
- allowed path: `apps/capture-station/src/components/LivePulse/LivePulse.tsx`
- allowed path: `apps/capture-station/src/components/LivePulse/LivePulse.module.css`
- allowed path: `apps/capture-station/src/components/Modal/Modal.tsx`
- allowed path: `apps/capture-station/src/components/Modal/Modal.module.css`
- allowed path: `apps/capture-station/src/components/PanelCard/PanelCard.tsx`
- allowed path: `apps/capture-station/src/components/PanelCard/PanelCard.module.css`
- allowed path: `apps/capture-station/src/components/PromoteGate/PromoteGate.tsx`
- allowed path: `apps/capture-station/src/components/PromoteGate/PromoteGate.module.css`
- allowed path: `apps/capture-station/src/components/StateBadge/StateBadge.tsx`
- allowed path: `apps/capture-station/src/components/StateBadge/StateBadge.module.css`
- allowed path: `apps/capture-station/src/components/SurfaceFrame/SurfaceFrame.tsx`
- allowed path: `apps/capture-station/src/components/SurfaceFrame/SurfaceFrame.module.css`
- allowed path: `apps/capture-station/src/components/SyncBadge/SyncBadge.tsx`
- allowed path: `apps/capture-station/src/components/SyncBadge/SyncBadge.module.css`
- allowed path: `apps/capture-station/src/components/TagList/TagList.tsx`
- allowed path: `apps/capture-station/src/components/TagList/TagList.module.css`
- allowed path: `apps/capture-station/src/components/TopicCard/TopicCard.tsx`
- allowed path: `apps/capture-station/src/components/TopicCard/TopicCard.module.css`
- allowed path: `apps/capture-station/src/components/UrlInput/UrlInput.tsx`
- allowed path: `apps/capture-station/src/components/UrlInput/UrlInput.module.css`
- allowed path: `apps/capture-station/src/features/shared/fixtures.ts`
- allowed path: `apps/capture-station/src/features/surfaces.smoke.test.tsx`
- allowed path: `apps/capture-station/src/features/url-bar/UrlBar.tsx`
- allowed path: `apps/capture-station/src/features/url-bar/UrlBar.module.css`
- allowed path: `apps/capture-station/src/features/url-bar/UrlBar.test.tsx`
- allowed path: `apps/capture-station/src/features/live-metadata/LiveMetadata.tsx`
- allowed path: `apps/capture-station/src/features/live-metadata/LiveMetadata.module.css`
- allowed path: `apps/capture-station/src/features/capture-scope/CaptureScope.tsx`
- allowed path: `apps/capture-station/src/features/capture-scope/CaptureScope.module.css`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTrace.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTrace.module.css`
- allowed path: `apps/capture-station/src/features/vault-preview/VaultPreview.tsx`
- allowed path: `apps/capture-station/src/features/vault-preview/VaultPreview.module.css`
- allowed path: `apps/capture-station/src/features/vault-commit/VaultCommit.tsx`
- allowed path: `apps/capture-station/src/features/vault-commit/VaultCommit.module.css`
- allowed path: `apps/capture-station/src/features/topic-card-preview/TopicCardLite.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-preview/TopicCardLite.module.css`
- allowed path: `apps/capture-station/src/features/topic-card-vault/TopicCardVault.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-vault/TopicCardVault.module.css`
- allowed path: `apps/capture-station/src/features/topic-card-vault/TopicCardVault.test.tsx`
- allowed path: `apps/capture-station/src/features/signal-hypothesis/SignalHypothesis.tsx`
- allowed path: `apps/capture-station/src/features/signal-hypothesis/SignalHypothesis.module.css`
- allowed path: `apps/capture-station/src/features/capture-plan/CapturePlan.tsx`
- allowed path: `apps/capture-station/src/features/capture-plan/CapturePlan.module.css`
- allowed path: `apps/capture-station/src/features/_specs/DensitySpec.tsx`
- allowed path: `apps/capture-station/src/features/_specs/TypeSpec.tsx`
- allowed path: `apps/capture-station/src/features/_specs/SpecPages.module.css`
- allowed path: `apps/capture-station/src/features/capture-scope/CaptureScopePanel.tsx`
- allowed path: `apps/capture-station/src/features/capture-scope/CaptureScopePanel.test.tsx`
- allowed path: `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.tsx`
- allowed path: `apps/capture-station/src/features/live-metadata/LiveMetadataPanel.test.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-preview/TopicCardPreviewCandidate.test.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-preview/topicCardLite.ts`
- allowed path: `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-vault/TopicCardVaultCandidate.test.tsx`
- allowed path: `apps/capture-station/src/features/topic-card-vault/topicCardVaultCandidateData.ts`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTraceGraph.tsx`
- allowed path: `apps/capture-station/src/features/trust-trace/TrustTraceGraph.test.tsx`
- allowed path: `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.tsx`
- allowed path: `apps/capture-station/src/features/vault-preview/VaultPreviewPanel.test.tsx`
- allowed path: `apps/capture-station/src/features/vault-commit/VaultCommitDryRunButton.tsx`
- allowed path: `apps/capture-station/src/layout/FourPanelShell.tsx`
- allowed path: `apps/capture-station/src/layout/FourPanelShell.test.tsx`
- allowed path: `apps/capture-station/src/layout/panels.ts`
- allowed path: `docs/research/post-frozen/PF-C4-01/receipts/pf-c4-01-app-scope-note-2026-05-07.md`
