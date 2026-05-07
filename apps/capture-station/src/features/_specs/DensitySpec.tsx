import AppShellOverview from "../../components/AppShell/AppShellOverview";
import PanelCard from "../../components/PanelCard/PanelCard";
import SurfaceFrame from "../../components/SurfaceFrame/SurfaceFrame";
import styles from "./SpecPages.module.css";

export default function DensitySpec() {
  return (
    <SurfaceFrame title="密度规格 · V3 紧凑密度" description="密度覆盖保持为 token layer，而不是散落到单个组件里。">
      <div className={styles.stack}>
        <PanelCard title="Compact baseline" eyebrow="density-spec" description="仅通过 density-compact.css 覆盖 type-title、type-body、space-md、space-sm。">
          <p className={styles.note}>这页复用 App Shell 总览作为 V3 compact reference，证明密度调节不需要重写 IA。</p>
        </PanelCard>
        <AppShellOverview embedded />
      </div>
    </SurfaceFrame>
  );
}
