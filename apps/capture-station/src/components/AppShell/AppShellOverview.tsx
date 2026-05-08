import Button from "../Button/Button";
import CaptureIdChip from "../CaptureIdChip/CaptureIdChip";
import FrontmatterBlock from "../FrontmatterBlock/FrontmatterBlock";
import Icon from "../Icon/Icon";
import PanelCard from "../PanelCard/PanelCard";
import StateBadge from "../StateBadge/StateBadge";
import SurfaceFrame from "../SurfaceFrame/SurfaceFrame";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import {
  assessCanonicalUrl,
  getBlockedReasons,
  getBridgeSummary,
  getCreateSummary,
  getMetadataSummary,
  getPreviewSummary,
  toPreviewMarkdown,
} from "../../features/url-bar/w2cSurfaceState";
import styles from "./AppShellOverview.module.css";

function AppShellOverviewContent() {
  const runtime = useW2CRuntime();
  const createSummary = getCreateSummary(runtime);
  const bridgeSummary = getBridgeSummary(runtime);
  const metadataSummary = getMetadataSummary(runtime);
  const previewSummary = getPreviewSummary(runtime);
  const urlAssessment = assessCanonicalUrl(runtime.canonicalUrl);
  const blockedReasons = getBlockedReasons(runtime);
  const canCreate = urlAssessment.isValid && runtime.capture.status !== "loading";

  const bridgeRows = [
    { label: "spec_version", value: runtime.bridgeHealth.data?.spec_version ?? "pending" },
    { label: "bridge_available", value: runtime.bridgeHealth.data?.bridge_available ? "true" : "false" },
    { label: "frontmatter_mode", value: runtime.bridgeVaultConfig.data?.frontmatter_mode ?? "pending" },
    { label: "blocked_by", value: runtime.bridgeHealth.data?.blocked_by.join(", ") || "none" },
  ];

  const captureRows = [
    { label: "capture_id", value: runtime.currentCaptureId ?? "未创建 capture" },
    { label: "discover", value: runtime.capture.data?.status ?? runtime.capture.status },
    { label: "metadata_fetch", value: runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status },
    { label: "trust_trace", value: runtime.trustTrace.status },
    { label: "receipt_ledger", value: runtime.trustTrace.data?.receipt_ledger.present ? `present (${runtime.trustTrace.data.receipt_ledger.artifact_count})` : "absent" },
  ];

  const previewRows = [
    { label: "preview_target", value: runtime.vaultPreview.data?.target_path ?? "pending" },
    { label: "warnings", value: runtime.vaultPreview.data?.warnings.join(", ") || "none" },
    { label: "write_gate", value: "write_enabled=false" },
    { label: "runtime_gate", value: blockedReasons.join(", ") || "none" },
  ];

  return (
    <>
      <div className={styles.topBar}>
        <div className={styles.urlRow}>
          <label style={{ display: "grid", gap: "var(--space-xs)" }}>
            <span style={{ color: "var(--text-muted)" }}>canonical_url</span>
            <input
              aria-label="canonical_url"
              value={runtime.canonicalUrl}
              onChange={(event) => runtime.setCanonicalUrl(event.target.value)}
              style={{
                minWidth: 0,
                borderRadius: "var(--radius-panel)",
                border: `1px solid ${urlAssessment.mode === "error" ? "var(--state-error)" : "var(--border-soft)"}`,
                background: "var(--surface-base)",
                color: "var(--text-primary)",
                padding: "var(--space-sm) var(--space-md)",
              }}
            />
          </label>
          <Button
            icon={<Icon name="capture" />}
            variant={canCreate ? "primary" : "blocked"}
            onClick={() => void runtime.createCapture()}
            disabled={!canCreate}
          >
            {runtime.capture.status === "loading" ? "创建中..." : "创建采集"}
          </Button>
          <Button
            icon={<Icon name="dry-run" />}
            variant="secondary"
            onClick={() => void runtime.refreshCaptureBoundData()}
            disabled={!runtime.currentCaptureId}
          >
            刷新 readback
          </Button>
        </div>
        <p style={{ margin: 0, color: "var(--text-secondary)" }}>{urlAssessment.errorMessage ?? createSummary.detail}</p>
      </div>

      <div className={styles.panels}>
        <PanelCard title="Bridge / Vault" eyebrow="app-shell" aside={<StateBadge tone={bridgeSummary.tone} label={bridgeSummary.label} />}>
          <div style={{ display: "grid", gap: "var(--space-sm)" }}>
            <p style={{ margin: 0, color: "var(--text-secondary)" }}>{bridgeSummary.detail}</p>
            <dl className={styles.metadataGrid}>
              {bridgeRows.map((field) => (
                <div key={field.label} style={{ display: "contents" }}>
                  <dt>{field.label}</dt>
                  <dd>{field.value}</dd>
                </div>
              ))}
            </dl>
          </div>
        </PanelCard>

        <PanelCard title="当前 Capture" eyebrow="app-shell" aside={<StateBadge tone={createSummary.tone} label={createSummary.label} />}>
          <div style={{ display: "grid", gap: "var(--space-sm)" }}>
            <p style={{ margin: 0, color: "var(--text-secondary)" }}>{metadataSummary.detail}</p>
            <dl className={styles.metadataGrid}>
              {captureRows.map((field) => (
                <div key={field.label} style={{ display: "contents" }}>
                  <dt>{field.label}</dt>
                  <dd>{field.label === "capture_id" && runtime.currentCaptureId ? <CaptureIdChip value={runtime.currentCaptureId} /> : field.value}</dd>
                </div>
              ))}
            </dl>
          </div>
        </PanelCard>

        <PanelCard title="Preview / Governance" eyebrow="app-shell" aside={<StateBadge tone={previewSummary.tone} label={previewSummary.label} />}>
          <div style={{ display: "grid", gap: "var(--space-sm)" }}>
            <p style={{ margin: 0, color: "var(--text-secondary)" }}>{previewSummary.detail}</p>
            <dl className={styles.metadataGrid}>
              {previewRows.map((field) => (
                <div key={field.label} style={{ display: "contents" }}>
                  <dt>{field.label}</dt>
                  <dd>{field.value}</dd>
                </div>
              ))}
            </dl>
          </div>
        </PanelCard>
      </div>

      <div className={styles.previewRow}>
        <PanelCard title="Vault Preview" eyebrow="vault-preview" aside={<StateBadge tone={previewSummary.tone} label={previewSummary.label} />}>
          <FrontmatterBlock mode="code" content={toPreviewMarkdown(runtime.vaultPreview.data, runtime.currentCaptureId)} />
          <div className={styles.previewFooter}>
            <span>preview_target</span>
            <CaptureIdChip value={runtime.vaultPreview.data?.target_path ?? "pending"} muted />
          </div>
        </PanelCard>

        <PanelCard title="Vault Commit（干跑）" eyebrow="vault-commit" aside={<StateBadge tone="blocked" label="write_enabled=false" />}>
          <p style={{ margin: 0, color: "var(--text-secondary)" }}>dry-run contract 可见，但本轮不宣称 true vault write 已解禁。</p>
          <Button icon={<Icon name="dry-run" />} variant="blocked" disabled>
            入库提交（干跑）
          </Button>
        </PanelCard>
      </div>
    </>
  );
}

export default function AppShellOverview({ embedded = false }: { embedded?: boolean }) {
  if (embedded) {
    return <AppShellOverviewContent />;
  }

  return (
    <SurfaceFrame title="应用总览" description="W2C app shell 只汇总 live bridge / capture / preview truth，不为后续 blocked lane 做越权背书。">
      <AppShellOverviewContent />
    </SurfaceFrame>
  );
}
