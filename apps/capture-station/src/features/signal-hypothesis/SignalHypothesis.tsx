import EvidenceTable from "../../components/EvidenceTable/EvidenceTable";
import LifecycleStepper from "../../components/LifecycleStepper/LifecycleStepper";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { signalRows } from "../shared/fixtures";
import styles from "./SignalHypothesis.module.css";

const compareColumns = [
  { key: "hypothesis", label: "假设" },
  { key: "confidence", label: "置信度", code: true },
  { key: "support", label: "支持证据" },
  { key: "conflict", label: "冲突证据" },
] as const;

const compareRows = [
  { id: "row-a", cells: { hypothesis: "异步优先更稳定", confidence: "76.4%", support: "证据 1", conflict: "—" } },
  { id: "row-b", cells: { hypothesis: "同步确认更可靠", confidence: "43.1%", support: "证据 3", conflict: "证据 4" } },
];

export default function SignalHypothesis() {
  return (
    <SurfaceFrame title="信号 / 假设信息架构状态集" description="展开、对比和生命周期三块都直接转为 TSX。">
      <SurfaceSection title="状态: 信号展开">
        <PanelCard title="信号展开" eyebrow="signal-hypothesis">
          <details className={styles.details} open>
            <summary>
              <strong>{signalRows[0]?.title}</strong> <code>{signalRows[0]?.score}</code>
            </summary>
            <ol className={styles.list}>
              {signalRows[0]?.hypotheses.map((item) => <li key={item}>{item}</li>)}
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
          <LifecycleStepper
            ariaLabel="信号生命周期"
            steps={[
              { label: "原始信号", status: "done" },
              { label: "已验证", status: "done" },
              { label: "形成假设", status: "active" },
              { label: "已晋升", status: "idle" },
            ]}
          />
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
