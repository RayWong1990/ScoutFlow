import EvidenceTable from "../../components/EvidenceTable/EvidenceTable";
import PromoteGate from "../../components/PromoteGate/PromoteGate";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import PanelCard from "../../components/PanelCard/PanelCard";
import { capturePlanHooks, executionLogColumns, executionLogRows } from "../shared/fixtures";
import styles from "./CapturePlan.module.css";

export default function CapturePlan() {
  return (
    <SurfaceFrame title="采集计划信息架构状态集" description="输入输出契约、计划干跑和执行日志保持候选但可审的工作站语义。">
      <SurfaceSection title="状态: 计划输入 / 输出契约">
        <PanelCard title="I/O contract" eyebrow="capture-plan">
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>输入 URL</dt>
              <dd>https://www.bilibili.com/video/BV1xK4y1f7yC</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输入抓取范围</dt>
              <dd>metadata, comments, asr</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出 Markdown</dt>
              <dd>~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出 Frontmatter</dt>
              <dd>title, capture_id, status, write_enabled</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出预览</dt>
              <dd>仅预览</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 计划干跑">
        <PromoteGate title="计划干跑钩子" items={capturePlanHooks.map((hook) => ({ label: hook.label, status: hook.status }))} />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 计划执行日志">
        <PanelCard title="执行日志" eyebrow="capture-plan">
          <EvidenceTable columns={executionLogColumns} rows={executionLogRows} />
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
