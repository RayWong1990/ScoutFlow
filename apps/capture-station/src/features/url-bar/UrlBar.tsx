import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import Icon from "../../components/Icon/Icon";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame from "../../components/SurfaceFrame/SurfaceFrame";
import UrlInput from "../../components/UrlInput/UrlInput";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import { assessCanonicalUrl, getCreateSummary, getMetadataSummary } from "./w2cSurfaceState";
import styles from "./UrlBar.module.css";

export default function UrlBar() {
  const runtime = useW2CRuntime();
  const createSummary = getCreateSummary(runtime);
  const metadataSummary = getMetadataSummary(runtime);
  const urlAssessment = assessCanonicalUrl(runtime.canonicalUrl);
  const canCreate = urlAssessment.isValid && runtime.capture.status !== "loading";

  return (
    <SurfaceFrame title="URL 输入栏" description="manual_url + metadata_only 的真实入口；只接 discover，不暗示 runtime 已解禁。">
      <PanelCard
        title="URL 地址"
        eyebrow="url-bar"
        description="当前只允许 bilibili canonical URL；创建 capture 与 metadata 读回是两段独立状态。"
        aside={<StateBadge tone={createSummary.tone} label={createSummary.label} />}
      >
        <div className={styles.stack}>
          <UrlInput
            id="url-live"
            label="URL 地址"
            value={runtime.canonicalUrl}
            placeholder="粘贴 Bilibili canonical URL（含 BV id）"
            mode={urlAssessment.mode}
            errorMessage={urlAssessment.errorMessage}
            onChange={runtime.setCanonicalUrl}
          />

          <div className={styles.actions}>
            <Button
              icon={<Icon name="capture" />}
              variant={canCreate ? "primary" : "blocked"}
              onClick={() => void runtime.createCapture()}
              disabled={!canCreate}
            >
              {runtime.capture.status === "loading" ? "创建中..." : "创建采集"}
            </Button>
            <Button
              variant="secondary"
              onClick={runtime.clearCapture}
              disabled={!runtime.currentCaptureId}
            >
              清空当前 capture
            </Button>
          </div>

          <p className={styles.note}>{createSummary.detail}</p>

          {runtime.currentCaptureId ? (
            <div className={styles.currentCapture}>
              <div className={styles.currentRow}>
                <span className={styles.currentLabel}>当前 capture</span>
                <CaptureIdChip value={runtime.currentCaptureId} />
              </div>
              <div className={styles.currentRow}>
                <span className={styles.currentLabel}>discover 状态</span>
                <span>{runtime.capture.data?.status ?? runtime.capture.status}</span>
              </div>
              <div className={styles.currentRow}>
                <span className={styles.currentLabel}>metadata_fetch</span>
                <span>{runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status}</span>
              </div>
              <p className={styles.note}>{metadataSummary.detail}</p>
            </div>
          ) : null}
        </div>
      </PanelCard>
    </SurfaceFrame>
  );
}
