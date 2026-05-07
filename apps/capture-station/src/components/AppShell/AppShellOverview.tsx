import Button from "../Button/Button";
import CaptureIdChip from "../CaptureIdChip/CaptureIdChip";
import EvidenceTable from "../EvidenceTable/EvidenceTable";
import FrontmatterBlock from "../FrontmatterBlock/FrontmatterBlock";
import Icon from "../Icon/Icon";
import LifecycleStepper from "../LifecycleStepper/LifecycleStepper";
import PanelCard from "../PanelCard/PanelCard";
import StateBadge from "../StateBadge/StateBadge";
import SurfaceFrame from "../SurfaceFrame/SurfaceFrame";
import TagList from "../TagList/TagList";
import UrlInput from "../UrlInput/UrlInput";
import { captureScopeStepsPreview, metadataFields, metadataTags, previewMarkdown, traceColumns, traceRows } from "../../features/shared/fixtures";
import styles from "./AppShellOverview.module.css";

function AppShellOverviewContent() {
  return (
    <>
      <div className={styles.topBar}>
        <div className={styles.urlRow}>
          <UrlInput
            id="overview-url"
            label="URL 地址"
            value="https://www.bilibili.com/video/BV1xK4y1f7yC"
            mode="focus"
            readOnly
          />
          <Button icon={<Icon name="capture" />} variant="primary">
            创建采集
          </Button>
          <Button icon={<Icon name="dry-run" />} variant="secondary">
            仅预览
          </Button>
        </div>
      </div>

      <div className={styles.panels}>
        <PanelCard title="实时元数据" eyebrow="live-metadata" aside={<StateBadge tone="metadataLoaded" label="元数据已加载" />}>
          <dl className={styles.metadataGrid}>
            {metadataFields.map((field) => (
              <div key={field.label} style={{ display: "contents" }}>
                <dt>{field.label}</dt>
                <dd>{field.label === "capture_id" ? <CaptureIdChip value={field.value} /> : field.value}</dd>
              </div>
            ))}
          </dl>
          <TagList items={metadataTags} />
        </PanelCard>

        <PanelCard title="采集范围" eyebrow="capture-scope" aside={<StateBadge tone="previewOnly" label="仅预览" />}>
          <LifecycleStepper ariaLabel="生命周期阶段" steps={captureScopeStepsPreview} />
          <dl className={styles.metadataGrid}>
            <div style={{ display: "contents" }}>
              <dt>写入开关</dt>
              <dd>关闭</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>预览路径</dt>
              <dd>~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md</dd>
            </div>
          </dl>
        </PanelCard>

        <PanelCard title="信任溯源" eyebrow="trust-trace" aside={<StateBadge tone="ready" label="就绪" />}>
          <div className={styles.placeholder}>信任溯源图谱（结构占位）</div>
          <EvidenceTable columns={traceColumns} rows={traceRows.slice(0, 3)} />
        </PanelCard>
      </div>

      <div className={styles.previewRow}>
        <PanelCard title="入库预览" eyebrow="vault-preview" aside={<StateBadge tone="ready" label="预览就绪" />}>
          <FrontmatterBlock mode="code" content={previewMarkdown} />
          <div className={styles.previewFooter}>
            <span>目标: Obsidian raw vault inbox</span>
            <CaptureIdChip value="~/workspace/raw/00-Inbox/" muted />
          </div>
        </PanelCard>

        <PanelCard title="入库提交（干跑）" eyebrow="vault-commit" aside={<StateBadge tone="candidate" label="write_disabled" />}>
          <p>仅展示当前阶段的提交边界，不解禁 true vault write。</p>
          <Button icon={<Icon name="dry-run" />} variant="blocked" disabled>
            入库提交（干跑）
          </Button>
        </PanelCard>
      </div>
    </>
  );
}

export default function AppShellOverview({ embedded = false }: { embedded?: boolean }) {
  if (embedded) {
    return <AppShellOverviewContent />;
  }

  return (
    <SurfaceFrame title="应用总览" description="本地操作员工作站总览，对应 P7 的 00-app-shell 组合态。">
      <AppShellOverviewContent />
    </SurfaceFrame>
  );
}
