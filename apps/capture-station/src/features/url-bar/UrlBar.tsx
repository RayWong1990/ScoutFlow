import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import Icon from "../../components/Icon/Icon";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import UrlInput from "../../components/UrlInput/UrlInput";
import { urlHistory } from "../shared/fixtures";
import styles from "./UrlBar.module.css";

export default function UrlBar() {
  return (
    <SurfaceFrame title="URL 输入栏状态集" description="粘贴入口、校验、错误与历史下拉，对应 P7 的 01-url-bar surface。">
      <div className={styles.stack}>
        <SurfaceSection title="状态: 空闲">
          <PanelCard title="URL 地址" eyebrow="url-bar" description="空输入时保持 blocked posture。">
            <div className={styles.section}>
              <UrlInput id="url-empty" label="URL 地址" value="" placeholder="粘贴一个 URL 或拖入文件" readOnly />
              <div className={styles.actions}>
                <Button icon={<Icon name="capture" />} variant="blocked" disabled>
                  创建采集
                </Button>
              </div>
            </div>
          </PanelCard>
        </SurfaceSection>

        <SurfaceDivider />

        <SurfaceSection title="状态: 聚焦">
          <PanelCard title="URL 地址" eyebrow="url-bar" description="输入框聚焦时以 accent-live 强化边界。">
            <div className={styles.section}>
              <UrlInput id="url-focus" label="URL 地址" value="" placeholder="粘贴一个 URL 或拖入文件" mode="focus" readOnly />
              <div className={styles.actions}>
                <Button icon={<Icon name="capture" />} variant="blocked" disabled>
                  创建采集
                </Button>
              </div>
            </div>
          </PanelCard>
        </SurfaceSection>

        <SurfaceDivider />

        <SurfaceSection title="状态: 校验中">
          <PanelCard title="URL 地址" eyebrow="url-bar" description="解析中时保留 ready-to-validate 视觉，但不假装已经入账。">
            <div className={styles.section}>
              <UrlInput
                id="url-validating"
                label="URL 地址"
                value="https://www.bilibili.com/video/BV1xK4y1f7yC"
                mode="focus"
                readOnly
              />
              <div className={styles.statusRow}>
                <StateBadge tone="loading" label="解析中..." />
                <Button icon={<Icon name="capture" />} variant="blocked" disabled>
                  创建采集
                </Button>
              </div>
            </div>
          </PanelCard>
        </SurfaceSection>

        <SurfaceDivider />

        <SurfaceSection title="状态: 错误">
          <PanelCard title="URL 地址" eyebrow="url-bar" description="错误态只收窄到输入问题，不误导为 runtime failure。">
            <div className={styles.section}>
              <UrlInput
                id="url-error"
                label="URL 地址"
                value="https://invalid-url"
                mode="error"
                errorMessage="URL 格式无效"
                readOnly
              />
              <div className={styles.actions}>
                <Button icon={<Icon name="capture" />} variant="blocked" disabled>
                  创建采集
                </Button>
              </div>
            </div>
          </PanelCard>
        </SurfaceSection>

        <SurfaceDivider />

        <SurfaceSection title="状态: 历史下拉">
          <PanelCard title="最近采集记录" eyebrow="url-bar" description="历史状态维持中文文案与 metadata-loaded 词汇。">
            <div className={styles.section}>
              <UrlInput
                id="url-history"
                label="URL 地址"
                value="https://www.bilibili.com/video/BV1xK4y1f7yC"
                mode="focus"
                readOnly
              />
              <div className={styles.actions}>
                <Button icon={<Icon name="capture" />} variant="primary">
                  创建采集
                </Button>
              </div>
              <ul className={styles.history}>
                {urlHistory.map((item) => (
                  <li key={item.captureId} className={styles.historyItem}>
                    <div className={styles.historyMeta}>
                      <CaptureIdChip value={item.captureId} />
                      <span>{item.time}</span>
                    </div>
                    <span>{item.url}</span>
                    <StateBadge tone="metadataLoaded" label={item.label} />
                  </li>
                ))}
              </ul>
            </div>
          </PanelCard>
        </SurfaceSection>
      </div>
    </SurfaceFrame>
  );
}
