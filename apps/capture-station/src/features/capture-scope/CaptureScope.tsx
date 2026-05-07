import GovernanceTooltip from "../../components/GovernanceTooltip/GovernanceTooltip";
import LifecycleStepper from "../../components/LifecycleStepper/LifecycleStepper";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { captureScopeStepsCommit, captureScopeStepsPreview, captureScopeStepsStart } from "../shared/fixtures";
import styles from "./CaptureScope.module.css";

export default function CaptureScope() {
  return (
    <SurfaceFrame title="采集范围状态集" description="生命周期开始、预览完成和治理边界提示都维持在明确 stop-line 内。">
      <SurfaceSection title="状态: 生命周期开始">
        <PanelCard title="采集范围" eyebrow="capture-scope" aside={<StateBadge tone="metadataOnly" label="仅元数据" />}>
          <LifecycleStepper ariaLabel="生命周期阶段" steps={captureScopeStepsStart} />
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>状态</dt>
              <dd>仅元数据</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>抓取范围</dt>
              <dd>已折叠</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 生命周期完成">
        <PanelCard title="采集范围" eyebrow="capture-scope" aside={<StateBadge tone="locked" label="已锁定" />}>
          <LifecycleStepper ariaLabel="生命周期阶段" steps={captureScopeStepsCommit} />
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>状态</dt>
              <dd>已锁定</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>预览路径</dt>
              <dd>~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 阻塞层提示">
        <PanelCard title="治理边界" eyebrow="capture-scope" aside={<StateBadge tone="previewOnly" label="仅预览" />}>
          <LifecycleStepper ariaLabel="生命周期阶段" steps={captureScopeStepsPreview} />
          <GovernanceTooltip title="治理边界">
            <p>
              ScoutFlow 交付干净 Markdown 到 Obsidian raw vault inbox（<code>~/workspace/raw/00-Inbox/</code>）。
            </p>
            <p>之后增强、双链回填与知识飞轮在 Obsidian 内发生，ScoutFlow 不参与。</p>
          </GovernanceTooltip>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
