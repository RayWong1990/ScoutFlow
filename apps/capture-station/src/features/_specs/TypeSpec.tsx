import AppShellOverview from "../../components/AppShell/AppShellOverview";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame from "../../components/SurfaceFrame/SurfaceFrame";
import styles from "./SpecPages.module.css";

export default function TypeSpec() {
  return (
    <SurfaceFrame title="字重规格 · V4 高字重" description="字重覆盖保持为单独 overlay layer，和密度轴正交。">
      <div className={styles.stack}>
        <PanelCard title="Weight-heavy baseline" eyebrow="type-spec" description="仅通过 type-weight-heavy.css 覆盖 font-weight 与 type-mono。">
          <p className={styles.note}>这页同样复用 App Shell 总览作为 V4 heavy reference，证明 typography 调整仍保持工作站骨架不变。</p>
        </PanelCard>
        <AppShellOverview embedded />
      </div>
    </SurfaceFrame>
  );
}
