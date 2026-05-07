# PF-C4-01 App Scope Repair Note

state: `dispatch-scope-note`
date: `2026-05-07`
dispatch_id: `PF-C4-01`
slot_label: `local-frontend-bootstrap-and-surface-translation`

## Scope

This note records the explicit tracked app paths used by PF-C4-01 inside the bounded `apps/capture-station/**` subtree. The lane both lands new P7-driven surfaces and removes superseded placeholder surfaces in the same authorized app boundary.

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
- allowed path: `docs/research/repairs/pf-c4-01-app-scope-repair-2026-05-07.md`

## Boundary

- This note is a dispatch scope note only.
- It does not approve runtime unlock, browser automation, migrations, or true vault write.
- It records replacement/removal of superseded placeholder surfaces under the already-authorized PF-C4-01 app boundary.
