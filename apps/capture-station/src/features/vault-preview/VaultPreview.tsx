import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import FrontmatterBlock from "../../components/FrontmatterBlock/FrontmatterBlock";
import Icon from "../../components/Icon/Icon";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { previewFrontmatterFields, previewMarkdown } from "../shared/fixtures";
import styles from "./VaultPreview.module.css";

export default function VaultPreview() {
  return (
    <SurfaceFrame title="入库预览状态集" description="idle、ready、blocked、frontmatter-expanded 与 copy-action 都停留在 preview boundary 内。">
      <SurfaceSection title="状态: 空闲">
        <PanelCard title="入库预览" eyebrow="vault-preview" aside={<StateBadge tone="idle" label="idle" />}>
          <p>创建 metadata-only capture 后再加载 preview。</p>
          <div className={styles.actions}>
            <Button icon={<Icon name="preview" />} variant="blocked" disabled>
              Copy markdown
            </Button>
            <Button icon={<Icon name="commit" />} variant="blocked" disabled>
              Download .md
            </Button>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 预览就绪">
        <PanelCard title="Preview ready" eyebrow="vault-preview" aside={<StateBadge tone="ready" label="preview loaded" />}>
          <div className={styles.stack}>
            <FrontmatterBlock mode="code" content={previewMarkdown} />
            <div className={styles.target}>
              <span>capture_id:</span>
              <CaptureIdChip value="cap_20260506_8a3f2" />
              <span>target_path:</span>
              <CaptureIdChip value="~/workspace/raw/00-Inbox/cap_20260506_8a3f2.md" muted />
            </div>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 写禁用阻塞">
        <PanelCard title="Preview blocked" eyebrow="vault-preview" aside={<StateBadge tone="candidate" label="write_disabled" />}>
          <p>Bridge write path is not approved in the current phase.</p>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Frontmatter 展开">
        <PanelCard title="Frontmatter 展开" eyebrow="vault-preview">
          <FrontmatterBlock mode="fields" fields={[...previewFrontmatterFields]} />
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Copy action">
        <PanelCard title="Copy markdown" eyebrow="vault-preview">
          <div className={styles.stack}>
            <div className={styles.actions}>
              <Button icon={<Icon name="preview" />} variant="primary">
                Copy markdown
              </Button>
              <Button icon={<Icon name="commit" />} variant="secondary">
                Download .md
              </Button>
            </div>
            <p className={styles.message}>Markdown copied.</p>
          </div>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
