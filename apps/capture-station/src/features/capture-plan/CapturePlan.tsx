import EvidenceTable from "../../components/EvidenceTable/EvidenceTable";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import PromoteGate from "../../components/PromoteGate/PromoteGate";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import PanelCard from "../../components/PanelCard/PanelCard";
import { executionLogColumns } from "../shared/fixtures";
import styles from "./CapturePlan.module.css";

export default function CapturePlan() {
  const runtime = useW2CRuntime();
  const frontmatterMode = runtime.bridgeVaultConfig.data?.frontmatter_mode ?? "candidate";
  const frontmatterFields = runtime.vaultPreview.data
    ? Object.keys(runtime.vaultPreview.data.frontmatter).join(" / ")
    : "title / date / tags / status";
  const hookItems = [
    { label: "URL 已绑定当前输入", status: runtime.canonicalUrl ? "met" : "pending" },
    { label: "capture 已创建", status: runtime.currentCaptureId ? "met" : "pending" },
    { label: "metadata job 已排队", status: runtime.metadataFetch.data ? "met" : "pending" },
    { label: "vault preview 已生成", status: runtime.vaultPreview.data ? "met" : "pending" },
    { label: "true write 仍 blocked", status: runtime.isRuntimeBlocked || runtime.isVaultWriteBlocked ? "pending" : "met" },
  ] as const;
  const executionLogRows = [
    {
      id: "capture-context",
      cells: {
        time: "runtime",
        event: "capture_context",
        note: runtime.currentCaptureId ? `${runtime.currentCaptureId} / ${runtime.capture.data?.status ?? "pending"}` : "no active capture",
      },
    },
    {
      id: "metadata-fetch",
      cells: {
        time: "runtime",
        event: "metadata_fetch",
        note: runtime.metadataFetch.data
          ? `${runtime.metadataFetch.data.job_id} / ${runtime.metadataFetch.data.status}`
          : `status=${runtime.metadataFetch.status}`,
      },
    },
    {
      id: "vault-preview",
      cells: {
        time: "runtime",
        event: "vault_preview",
        note: runtime.vaultPreview.data ? runtime.vaultPreview.data.target_path : `status=${runtime.vaultPreview.status}`,
      },
    },
    {
      id: "runtime-gate",
      tone: "error" as const,
      cells: {
        time: "runtime",
        event: "runtime_gate",
        note: runtime.isRuntimeBlocked ? "future-gated; no runtime approval language" : "candidate",
      },
    },
  ];

  return (
    <SurfaceFrame title="采集计划信息架构状态集" description="输入输出、干跑钩子和执行日志都绑定当前 runtime 状态；未获批部分继续显式 blocked。">
      <SurfaceSection title="状态: 计划输入 / 输出契约">
        <PanelCard title="I/O contract" eyebrow="capture-plan">
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>输入 URL</dt>
              <dd>{runtime.captureSourceUrl ?? runtime.canonicalUrl}</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输入抓取范围</dt>
              <dd>{runtime.capture.data?.capture_mode ?? "candidate_only"}; comments / asr blocked</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出 Markdown</dt>
              <dd>{runtime.vaultPreview.data?.target_path ?? "vault preview pending"}</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出 Frontmatter</dt>
              <dd>{frontmatterMode}; {frontmatterFields}</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>输出预览</dt>
              <dd>{runtime.bridgeVaultConfig.data?.preview_enabled ? "preview enabled" : "preview blocked / pending"}</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 计划干跑">
        <PromoteGate title="计划干跑钩子" items={[...hookItems]} />
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
