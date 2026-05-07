import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import Icon from "../../components/Icon/Icon";
import Modal from "../../components/Modal/Modal";
import PanelCard from "../../components/PanelCard/PanelCard";
import PromoteGate from "../../components/PromoteGate/PromoteGate";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import SyncBadge from "../../components/SyncBadge/SyncBadge";
import TopicCard from "../../components/TopicCard/TopicCard";
import { promoteGateItems, syncCards } from "../shared/fixtures";
import styles from "./TopicCardVault.module.css";

export default function TopicCardVault() {
  return (
    <SurfaceFrame title="Topic Card Vault 状态集" description="默认、聚合、晋升准备、晋升确认与 sync 三态全部在同一语义系统内。">
      <SurfaceSection title="状态: 默认">
        <PanelCard title="Topic Card Vault" eyebrow="topic-card-vault" aside={<StateBadge tone="previewOnly" label="write_disabled" />}>
          <TopicCard
            captureId="cap_20260506_8a3f2"
            source="vault list"
            title="深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯"
            abstract="默认态保持候选列表视角，不越界到写入通过。"
          />
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Source URL 聚合">
        <PanelCard title="Source URL aggregate" eyebrow="topic-card-vault">
          <div className={styles.aggregate}>
            <div className={styles.headerMeta}>
              <CaptureIdChip value="source_url" muted />
              <span>同一来源下聚合 3 张候选卡</span>
            </div>
            <div className={styles.cards}>
              <TopicCard captureId="cap_20260506_8a3f2" source="source_url A" title="深度工作流" abstract="选题卡按来源聚合。" />
              <TopicCard captureId="cap_20260506_91b7c" source="source_url A" title="异步协作" abstract="同源候选卡可以并排比对。" />
            </div>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 晋升准备度">
        <PanelCard title="Promote readiness" eyebrow="topic-card-vault">
          <div className={styles.stack}>
            <TopicCard
              captureId="cap_20260506_a02ef"
              source="selected candidate"
              title="知识飞轮"
              abstract="进入 DiloFlow 前先走 promote-gate。"
              selected
            />
            <PromoteGate title="晋升 DiloFlow 准备度" items={promoteGateItems} />
            <Button icon={<Icon name="plan" />} variant="primary">
              晋升 DiloFlow
            </Button>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 晋升确认弹窗">
        <Modal
          title={
            <>
              <Icon name="plan" />
              <span>确认晋升 DiloFlow</span>
            </>
          }
          tone="promote"
          footer={
            <>
              <Button variant="secondary">取消</Button>
              <Button variant="primary">确认晋升</Button>
            </>
          }
        >
          <p>将选题卡、信号、假设与证据指针转入 DiloFlow 草案。ScoutFlow 不写入 Obsidian 之外的持久库。</p>
          <p>来源: <code>cap_20260506_8a3f2</code> → 目标: DiloFlow 草案</p>
        </Modal>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Obsidian 同步状态">
        <PanelCard title="Cross-system sync" eyebrow="topic-card-vault" description="L8 contract: synced / pending / external-changed 三态不能塌缩。">
          <div className={styles.cards}>
            {syncCards.map((card) => (
              <TopicCard
                key={card.captureId}
                captureId={card.captureId}
                source="Obsidian sync"
                title={card.title}
                abstract="跨系统状态对齐保留为独立视觉语义。"
                footer={<SyncBadge state={card.state} />}
              />
            ))}
          </div>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
