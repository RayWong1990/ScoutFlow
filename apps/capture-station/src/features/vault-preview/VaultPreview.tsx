import { useState } from "react";

import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import FrontmatterBlock from "../../components/FrontmatterBlock/FrontmatterBlock";
import Icon from "../../components/Icon/Icon";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { type AsyncState, type W2CRuntimeValue, useW2CRuntime } from "../../lib/w2c-runtime";
import styles from "./VaultPreview.module.css";

function useVaultRuntimeOrNull(): W2CRuntimeValue | null {
  try {
    return useW2CRuntime();
  } catch {
    return null;
  }
}

function mapStatusBadge<T>(state: AsyncState<T>, options: { ready: string; loading: string; idle: string }) {
  if (state.status === "loading") {
    return { tone: "loading" as const, label: options.loading };
  }

  if (state.status === "error") {
    return { tone: "error" as const, label: state.error?.code ?? "route_error" };
  }

  if (state.status === "success") {
    return { tone: "ready" as const, label: options.ready };
  }

  return { tone: "idle" as const, label: options.idle };
}

function previewBlockedCopy(runtime: W2CRuntimeValue, captureReady: boolean) {
  const config = runtime.bridgeVaultConfig.data;
  const configError = runtime.bridgeVaultConfig.error ?? config?.error;

  if (!captureReady) {
    return "先创建 metadata-only capture，Vault Preview 才会请求真实 preview route。";
  }

  if (configError) {
    return `当前配置阻断 preview：${configError.code}。${configError.message}`;
  }

  if (config?.preview_enabled === false) {
    return "Bridge config 明确把 preview 关着，当前只能停留在 blocked posture。";
  }

  return "Preview route 还没返回结果，当前只保留 preview-only posture。";
}

export default function VaultPreview() {
  const runtime = useVaultRuntimeOrNull();
  const [copyMessage, setCopyMessage] = useState<"idle" | "success" | "error">("idle");
  const previewState = runtime?.vaultPreview;
  const configState = runtime?.bridgeVaultConfig;
  const bridgeHealth = runtime?.bridgeHealth.data;
  const currentCaptureId = runtime?.currentCaptureId ?? null;
  const hasPreview = previewState?.status === "success" && previewState.data !== null;
  const hasCapture = currentCaptureId !== null;
  const configBadge = runtime
    ? mapStatusBadge(runtime.bridgeVaultConfig, {
        ready: runtime.bridgeVaultConfig.data?.error ? runtime.bridgeVaultConfig.data.error.code : "config_loaded",
        loading: "config_loading",
        idle: "config_idle",
      })
    : { tone: "blocked" as const, label: "runtime_missing" };
  const previewBadge =
    !runtime ? { tone: "blocked" as const, label: "runtime_missing" } :
    previewState?.status === "success" && runtime.bridgeVaultConfig.data?.preview_enabled === false ? { tone: "blocked" as const, label: "preview_disabled" } :
    previewState?.status === "success" && runtime.bridgeVaultConfig.data?.error ? { tone: "blocked" as const, label: runtime.bridgeVaultConfig.data.error.code } :
    mapStatusBadge(runtime.vaultPreview, {
      ready: "preview_loaded",
      loading: "preview_loading",
      idle: hasCapture ? "preview_pending" : "no_capture",
    });

  async function handleCopyMarkdown() {
    if (!hasPreview || !previewState?.data) {
      return;
    }

    try {
      if (!navigator.clipboard) {
        throw new Error("clipboard unavailable");
      }
      await navigator.clipboard.writeText(previewState.data.body_markdown);
      setCopyMessage("success");
    } catch {
      setCopyMessage("error");
    }
  }

  function handleDownloadMarkdown() {
    if (!hasPreview || !previewState?.data) {
      return;
    }

    const blob = new Blob([previewState.data.body_markdown], { type: "text/markdown;charset=utf-8" });
    const href = window.URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = href;
    anchor.download = `scoutflow-${previewState.data.capture_id}-preview.md`;
    anchor.click();
    window.URL.revokeObjectURL(href);
  }

  return (
    <SurfaceFrame title="入库预览状态集" description="W2C 只消费 bridge config 与 preview route，不把 fixture 成功态伪装成真实入库。">
      <SurfaceSection title="状态: Bridge 配置">
        <PanelCard title="Vault config" eyebrow="vault-preview" aside={<StateBadge tone={configBadge.tone} label={configBadge.label} />}>
          {!runtime ? (
            <p>当前是 isolated render，缺少 `W2CRuntimeProvider`，所以只显示 blocked shell。</p>
          ) : configState?.status === "loading" ? (
            <p>正在读取 `/bridge/vault/config`，write gate 与 preview gate 还未确认。</p>
          ) : configState?.status === "error" ? (
            <div className={styles.stack}>
              <p>配置请求失败，当前不能把 preview 渲染成成功态。</p>
              <p className={styles.messageError}>
                {configState.error?.code ?? "route_error"}: {configState.error?.message ?? "Vault config route failed."}
              </p>
            </div>
          ) : configState?.data ? (
            <div className={styles.stack}>
              <dl className={styles.grid}>
                <div className={styles.contents}>
                  <dt>capture_id</dt>
                  <dd>{currentCaptureId ? <CaptureIdChip value={currentCaptureId} /> : "none"}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>vault_root</dt>
                  <dd>{configState.data.vault_root ?? "unset"}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>vault_root_resolved</dt>
                  <dd>{String(configState.data.vault_root_resolved)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>preview_enabled</dt>
                  <dd>{String(configState.data.preview_enabled)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>write_enabled</dt>
                  <dd>{String(configState.data.write_enabled)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>frontmatter_mode</dt>
                  <dd>{configState.data.frontmatter_mode}</dd>
                </div>
              </dl>
              {configState.data.error ? (
                <p className={styles.messageError}>
                  {configState.data.error.code}: {configState.data.error.message}
                </p>
              ) : null}
              <p className={styles.helper}>
                bridge_available={String(bridgeHealth?.bridge_available ?? false)}; blocked_by=
                {bridgeHealth?.blocked_by?.join(", ") || "none"}
              </p>
            </div>
          ) : (
            <p>配置尚未加载。</p>
          )}
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Preview 响应">
        <PanelCard title="Vault preview" eyebrow="vault-preview" aside={<StateBadge tone={previewBadge.tone} label={previewBadge.label} />}>
          {!runtime ? (
            <p>runtime 缺失时不伪造 preview 成功；这里只保留 blocked copy。</p>
          ) : previewState?.status === "loading" ? (
            <p>正在读取 `/captures/{'{capture_id}'}/vault-preview`，旧 preview 不会被冒充成新 capture 结果。</p>
          ) : previewState?.status === "error" ? (
            <div className={styles.stack}>
              <p>Preview route 返回错误，当前不能展示 fake success。</p>
              <p className={styles.messageError}>
                {previewState.error?.code ?? "route_error"}: {previewState.error?.message ?? "Vault preview route failed."}
              </p>
            </div>
          ) : hasPreview && previewState.data ? (
            <div className={styles.stack}>
              <FrontmatterBlock mode="code" content={previewState.data.body_markdown} />
              <div className={styles.target}>
                <span>capture_id:</span>
                <CaptureIdChip value={previewState.data.capture_id} />
                <span>target_path:</span>
                <CaptureIdChip value={previewState.data.target_path} muted />
              </div>
              {previewState.data.warnings.length > 0 ? (
                <ul className={styles.warnings}>
                  {previewState.data.warnings.map((warning) => (
                    <li key={warning}>{warning}</li>
                  ))}
                </ul>
              ) : (
                <p className={styles.helper}>warnings: none</p>
              )}
            </div>
          ) : runtime.bridgeVaultConfig.status === "success" ? (
            <p>{previewBlockedCopy(runtime, hasCapture)}</p>
          ) : (
            <p>Preview 还在等 config truth。</p>
          )}
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Frontmatter / preview-only actions">
        <PanelCard title="Frontmatter / actions" eyebrow="vault-preview">
          {hasPreview && previewState?.data ? (
            <div className={styles.stack}>
              <FrontmatterBlock
                mode="fields"
                fields={Object.entries(previewState.data.frontmatter).map(([label, value]) => ({ label, value }))}
              />
              <div className={styles.actions}>
                <Button icon={<Icon name="preview" />} variant="primary" onClick={() => void handleCopyMarkdown()}>
                  Copy markdown
                </Button>
                <Button icon={<Icon name="commit" />} variant="secondary" onClick={handleDownloadMarkdown}>
                  Download .md
                </Button>
                <Button
                  icon={<Icon name="preview" />}
                  variant="secondary"
                  onClick={() => void runtime?.refreshCaptureBoundData()}
                  disabled={!runtime?.currentCaptureId || runtime.vaultPreview.status === "loading"}
                >
                  Refresh preview
                </Button>
              </div>
              {copyMessage === "success" ? <p className={styles.messageSuccess}>Markdown copied from preview response only.</p> : null}
              {copyMessage === "error" ? <p className={styles.messageError}>Clipboard copy failed; preview stayed local and preview-only.</p> : null}
            </div>
          ) : (
            <div className={styles.stack}>
              <p>没有 preview payload 时，copy/download 仍保持 disabled，不把空白态包装成 ready。</p>
              <div className={styles.actions}>
                <Button icon={<Icon name="preview" />} variant="blocked" disabled>
                  Copy markdown
                </Button>
                <Button icon={<Icon name="commit" />} variant="blocked" disabled>
                  Download .md
                </Button>
              </div>
            </div>
          )}
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: write gate">
        <PanelCard title="Write gate remains closed" eyebrow="vault-preview" aside={<StateBadge tone="blocked" label="write_enabled=false" />}>
          <p>
            Preview surface 只展示 read-only / preview-only truth。即使 config 已解析、preview 已返回，也不会在这里解禁 true vault write。
          </p>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
