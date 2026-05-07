import EvidenceTable from "../../components/EvidenceTable/EvidenceTable";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { traceColumns, traceRows } from "../shared/fixtures";
import styles from "./TrustTrace.module.css";

export default function TrustTrace() {
  return (
    <SurfaceFrame title="信任溯源状态集" description="图谱、时间轴和错误路径都以诚实 TODO placeholder 呈现，不偷开 runtime 或 vendor 决策。">
      <SurfaceSection title="状态: DOM 过滤">
        <PanelCard title="DOM 过滤" eyebrow="trust-trace">
          <div className={styles.stack}>
            <ul className={styles.filters}>
              <li className={[styles.filter, styles.active].join(" ")}>DOM</li>
              <li className={styles.filter}>JSON-LD</li>
              <li className={styles.filter}>OpenGraph</li>
              <li className={styles.filter}>Microdata</li>
            </ul>
            {/* TODO P1: D3/cytoscape decision (PF-C4-EXT) */}
            <div className={styles.placeholder} data-todo="trust-trace-graph">
              信任溯源图谱（结构占位）
            </div>
            <EvidenceTable columns={traceColumns} rows={traceRows} />
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 时间轴">
        <PanelCard title="时间轴定位" eyebrow="trust-trace">
          <div className={styles.stack}>
            {/* TODO P2: timeline hover and evidence focus wiring */}
            <div className={styles.placeholder} data-todo="trust-trace-timeline">
              时间轴占位，后续补 hover timestamp 与证据定位
            </div>
            <EvidenceTable columns={traceColumns} rows={traceRows.slice(0, 3)} />
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 错误路径">
        <PanelCard title="错误路径高亮" eyebrow="trust-trace">
          <div className={styles.stack}>
            {/* TODO P1: error-path highlight wiring with graph implementation */}
            <div className={styles.placeholder} data-todo="trust-trace-error-path">
              错误路径高亮占位，等待图谱实现接线
            </div>
            <EvidenceTable columns={traceColumns} rows={traceRows} />
          </div>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
