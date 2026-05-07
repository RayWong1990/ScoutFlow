import LivePulse from "../../components/LivePulse/LivePulse";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import TagList from "../../components/TagList/TagList";
import { metadataFields, metadataTags } from "../shared/fixtures";
import styles from "./LiveMetadata.module.css";

export default function LiveMetadata() {
  return (
    <SurfaceFrame title="实时元数据状态集" description="长标题、数字强调、标签溢出、实时计数和缩略图占位都保持为 React surface。">
      <SurfaceSection title="状态: 长标题（中文换行）">
        <PanelCard title="实时元数据" eyebrow="live-metadata" description="长标题保持中文换行和 metadata grid 对齐。">
          <dl className={styles.grid}>
            {metadataFields.map((field, index) => (
              <div key={field.label} style={{ display: "contents" }}>
                <dt>{field.label}</dt>
                <dd>{index === 0 ? "深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯：从低摩擦记录到证据入账的完整链路" : field.value}</dd>
              </div>
            ))}
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 数字高权重">
        <PanelCard title="数字强调" eyebrow="live-metadata">
          <dl className={styles.grid}>
            {metadataFields.map((field) => (
              <div key={field.label} style={{ display: "contents" }}>
                <dt>{field.label}</dt>
                <dd className={field.label === "播放量" || field.label === "点赞" || field.label === "评论" ? styles.numberValue : undefined}>
                  {field.value}
                </dd>
              </div>
            ))}
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 标签溢出">
        <PanelCard title="标签溢出" eyebrow="live-metadata">
          <div className={styles.stack}>
            <dl className={styles.grid}>
              {metadataFields.slice(0, 6).map((field) => (
                <div key={field.label} style={{ display: "contents" }}>
                  <dt>{field.label}</dt>
                  <dd>{field.value}</dd>
                </div>
              ))}
            </dl>
            <TagList items={metadataTags} />
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 实时计数">
        <PanelCard title="实时计数" eyebrow="live-metadata">
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>播放量</dt>
              <dd className={styles.pulseRow}>
                <LivePulse />
                <span className={styles.numberValue}>24,914</span>
              </dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>点赞</dt>
              <dd className={styles.pulseRow}>
                <LivePulse />
                <span className={styles.numberValue}>3,151</span>
              </dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>评论</dt>
              <dd>287</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>最后更新</dt>
              <dd>2026-05-06 14:32 UTC</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 缩略图字段">
        <PanelCard title="缩略图字段" eyebrow="live-metadata" description="保持诚实 TODO，占位不伪装为真实缩略图。">
          <div className={styles.stack}>
            {/* TODO P1: bind to BBDown metadata pipeline */}
            <div className={styles.thumbnail} data-todo="thumbnail-fetch">
              <span>视频缩略图占位</span>
            </div>
            <dl className={styles.grid}>
              {metadataFields.map((field) => (
                <div key={field.label} style={{ display: "contents" }}>
                  <dt>{field.label}</dt>
                  <dd>{field.value}</dd>
                </div>
              ))}
            </dl>
          </div>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
