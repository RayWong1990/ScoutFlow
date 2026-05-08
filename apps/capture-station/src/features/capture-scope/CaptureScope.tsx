import Button from "../../components/Button/Button";
import GovernanceTooltip from "../../components/GovernanceTooltip/GovernanceTooltip";
import Icon from "../../components/Icon/Icon";
import LifecycleStepper from "../../components/LifecycleStepper/LifecycleStepper";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame from "../../components/SurfaceFrame/SurfaceFrame";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import {
  getBlockedReasons,
  getLifecycleSteps,
  getMetadataSummary,
  getPreviewSummary,
} from "../url-bar/w2cSurfaceState";
import styles from "./CaptureScope.module.css";

export default function CaptureScope() {
  const runtime = useW2CRuntime();
  const metadataSummary = getMetadataSummary(runtime);
  const previewSummary = getPreviewSummary(runtime);
  const blockedReasons = getBlockedReasons(runtime);

  return (
    <SurfaceFrame title="采集范围" description="显示 W2C 当前生命周期与治理边界：读回可以前进，runtime 与 true write 仍然保持 blocked。">
      <div className={styles.stack}>
        <PanelCard
          title="生命周期"
          eyebrow="capture-scope"
          description="step 只反映 existing-route 真实进度；并不把 metadata_fetch enqueue 当成 metadata loaded。"
          aside={<StateBadge tone={previewSummary.tone} label={previewSummary.label} />}
        >
          <div className={styles.stack}>
            <LifecycleStepper ariaLabel="生命周期阶段" steps={getLifecycleSteps(runtime)} />
            <dl className={styles.grid}>
              <div style={{ display: "contents" }}>
                <dt>capture_id</dt>
                <dd>{runtime.currentCaptureId ?? "未创建 capture"}</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>capture_state</dt>
                <dd>{runtime.trustTrace.data?.capture_state.status ?? runtime.capture.data?.status ?? runtime.capture.status}</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>metadata_fetch</dt>
                <dd>{runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status}</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>vault_preview</dt>
                <dd>{runtime.vaultPreview.data?.target_path ?? previewSummary.detail}</dd>
              </div>
            </dl>
            <div className={styles.actions}>
              <Button
                icon={<Icon name="dry-run" />}
                variant="secondary"
                onClick={() => void runtime.refreshCaptureBoundData()}
                disabled={!runtime.currentCaptureId}
              >
                刷新 readback
              </Button>
            </div>
            <p className={styles.note}>{metadataSummary.detail}</p>
          </div>
        </PanelCard>

        <PanelCard
          title="治理边界"
          eyebrow="capture-scope"
          description="这些边界是 live gate，不是文案提示。"
          aside={<StateBadge tone="blocked" label="write_enabled=false" />}
        >
          <div className={styles.stack}>
            <dl className={styles.grid}>
              <div style={{ display: "contents" }}>
                <dt>write_enabled</dt>
                <dd>write_enabled=false</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>preview_enabled</dt>
                <dd>{runtime.bridgeVaultConfig.data?.preview_enabled ? "true" : "false"}</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>bridge_available</dt>
                <dd>{runtime.bridgeHealth.data?.bridge_available ? "true" : "false"}</dd>
              </div>
              <div style={{ display: "contents" }}>
                <dt>audio_transcript</dt>
                <dd>audio_transcript runtime 仍 blocked</dd>
              </div>
            </dl>
            <GovernanceTooltip title="治理边界">
              <p>W2C 当前只允许 discover / metadata_fetch enqueue / trust-trace / vault-preview readback。</p>
              <p>true vault write、runtime tools、browser automation、full signal workbench 都不在本轮 scope。</p>
              <p>blocked_by: {blockedReasons.join(", ") || "none"}</p>
            </GovernanceTooltip>
          </div>
        </PanelCard>
      </div>
    </SurfaceFrame>
  );
}
