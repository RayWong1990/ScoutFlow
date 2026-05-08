import EvidenceTable from "../../components/EvidenceTable/EvidenceTable";
import LifecycleStepper from "../../components/LifecycleStepper/LifecycleStepper";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import styles from "./SignalHypothesis.module.css";

const compareColumns = [
  { key: "hypothesis", label: "假设" },
  { key: "confidence", label: "置信度", code: true },
  { key: "support", label: "支持证据" },
  { key: "conflict", label: "冲突证据" },
] as const;

export default function SignalHypothesis() {
  const runtime = useW2CRuntime();
  const currentTitle = typeof runtime.trustTrace.data?.audit.safe_parsed_fields.title === "string"
    ? runtime.trustTrace.data.audit.safe_parsed_fields.title
    : runtime.currentCaptureId
      ? `当前 capture ${runtime.currentCaptureId}`
      : "暂无 active capture";
  const signalItems = [
    runtime.currentCaptureId
      ? `capture_state=${runtime.trustTrace.data?.capture_state.status ?? runtime.capture.data?.status ?? "pending"}，当前只有元数据级上下文。`
      : "还没有 active capture，当前不生成真实假设。",
    runtime.metadataFetch.data
      ? `metadata_fetch job=${runtime.metadataFetch.data.job_id} status=${runtime.metadataFetch.data.status}。`
      : "metadata_fetch 尚未返回，正文与评论信号保持 future-gated。",
    runtime.trustTrace.data?.probe_evidence.present
      ? `probe evidence 已挂接，platform_result=${runtime.trustTrace.data.probe_evidence.platform_result ?? "pending"}。`
      : "probe evidence 尚未出现，不把外部证据假装成已验证。",
  ];
  const compareRows = [
    {
      id: "row-current",
      cells: {
        hypothesis: "当前 capture 的最小可证实假设",
        confidence: runtime.trustTrace.data ? "candidate" : "pending",
        support: runtime.trustTrace.data?.receipt_ledger.present
          ? `artifacts ${runtime.trustTrace.data.receipt_ledger.artifact_count}`
          : `metadata ${runtime.trustTrace.data?.metadata_job.status ?? runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status}`,
        conflict: runtime.isRuntimeBlocked ? "runtime blocked" : "—",
      },
    },
    {
      id: "row-future",
      tone: "error" as const,
      cells: {
        hypothesis: "评论 / ASR / 自动晋升",
        confidence: "future-gated",
        support: "待后续 contract",
        conflict: "当前 API 未批准",
      },
    },
  ];
  const lifecycleSteps = [
    { label: "原始信号", status: runtime.currentCaptureId ? "done" : "active" },
    { label: "元数据回填", status: runtime.metadataFetch.data ? "done" : runtime.currentCaptureId ? "active" : "idle" },
    { label: "形成假设", status: runtime.trustTrace.data ? "active" : "idle" },
    { label: "已晋升", status: "idle" },
  ] as const;

  return (
    <SurfaceFrame title="信号 / 假设信息架构状态集" description="只消费当前 trust-trace 与 metadata 状态；缺失的评论、ASR、晋升契约继续明确 future-gated。">
      <SurfaceSection title="状态: 信号展开">
        <PanelCard title="信号展开" eyebrow="signal-hypothesis">
          <details className={styles.details} open>
            <summary>
              <strong>{currentTitle}</strong> <code>{runtime.currentCaptureId ?? "candidate_only"}</code>
            </summary>
            <ol className={styles.list}>
              {signalItems.map((item) => <li key={item}>{item}</li>)}
            </ol>
          </details>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 假设对比">
        <PanelCard title="假设对比" eyebrow="signal-hypothesis">
          <EvidenceTable columns={[...compareColumns]} rows={compareRows} />
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 信号生命周期">
        <PanelCard title="信号生命周期" eyebrow="signal-hypothesis">
          <LifecycleStepper ariaLabel="信号生命周期" steps={[...lifecycleSteps]} />
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
