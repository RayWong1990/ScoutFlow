import Button from "../../components/Button/Button";
import Icon from "../../components/Icon/Icon";
import Modal from "../../components/Modal/Modal";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import styles from "./VaultCommit.module.css";

export default function VaultCommit() {
  return (
    <SurfaceFrame title="入库提交状态集" description="标准干跑、知识飞轮提示、通过/失败弹窗与批量干跑表都明确保持 write_disabled posture。">
      <SurfaceSection title="状态: 标准干跑">
        <PanelCard title="标准干跑" eyebrow="vault-commit" aside={<StateBadge tone="candidate" label="dry-run only" />}>
          <div className={styles.stack}>
            <p>This surface exposes the current-phase commit contract without claiming actual vault writes.</p>
            <Button icon={<Icon name="dry-run" />} variant="blocked" disabled>
              Commit to vault (disabled)
            </Button>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 知识飞轮提示">
        <PanelCard title="知识飞轮提示" eyebrow="vault-commit">
          <p>ScoutFlow 只把干净 Markdown 交付到 raw vault inbox；enrich、wiki link backfill 和知识飞轮在 Obsidian 内发生。</p>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 干跑通过弹窗">
        <Modal title="Dry-run passed" tone="pass" footer={<Button variant="success">继续预览</Button>}>
          <p>Frontmatter 校验通过，target path containment 通过，但仍未解禁 true vault write。</p>
        </Modal>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 干跑失败弹窗">
        <Modal title="Dry-run failed" tone="fail" footer={<Button variant="blocked">回到修正</Button>}>
          <p>写入开关仍关闭，当前阶段只能停留在 preview / report posture。</p>
        </Modal>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 批量干跑">
        <PanelCard title="批量干跑" eyebrow="vault-commit">
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>capture_id</dt>
              <dd>cap_20260506_8a3f2</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>dry_run</dt>
              <dd>true</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>committed</dt>
              <dd>false</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>gate</dt>
              <dd>write_disabled</dd>
            </div>
          </dl>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
