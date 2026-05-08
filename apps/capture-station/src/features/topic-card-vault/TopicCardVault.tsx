import Button from "../../components/Button/Button";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import Icon from "../../components/Icon/Icon";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import Modal from "../../components/Modal/Modal";
import PanelCard from "../../components/PanelCard/PanelCard";
import PromoteGate from "../../components/PromoteGate/PromoteGate";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import SyncBadge from "../../components/SyncBadge/SyncBadge";
import TopicCard from "../../components/TopicCard/TopicCard";
import type { PromoteGateItem } from "../../components/PromoteGate/PromoteGate";
import { syncCards } from "../shared/fixtures";
import styles from "./TopicCardVault.module.css";

export default function TopicCardVault() {
  const runtime = useW2CRuntime();
  const currentCaptureId = runtime.currentCaptureId ?? "capture_pending";
  const titleFromPreview = runtime.vaultPreview.data?.frontmatter.title ?? `ScoutFlow ${currentCaptureId}`;
  const vaultAsideTone = runtime.bridgeVaultConfig.data?.write_enabled ? "success" : "previewOnly";
  const vaultAsideLabel = runtime.bridgeVaultConfig.data?.write_enabled ? "write_enabled" : "write_disabled";
  const promoteGateItems: PromoteGateItem[] = [
    { label: "capture 已绑定", status: runtime.currentCaptureId ? "met" : "pending" },
    { label: "vault preview 已返回", status: runtime.vaultPreview.data ? "met" : "pending" },
    { label: "receipt ledger 已出现", status: runtime.trustTrace.data?.receipt_ledger.present ? "met" : "pending" },
    { label: "真实写入仍 blocked", status: runtime.isVaultWriteBlocked || runtime.isRuntimeBlocked ? "pending" : "met" },
  ];

  return (
    <SurfaceFrame
      title="Topic Card Vault 状态集"
      description="当前 capture 与 vault preview 接线到同一 surface；缺失 multi-card / true-write contract 的部分继续明确 blocked。"
    >
      <SurfaceSection title="状态: 默认">
        <PanelCard title="Topic Card Vault" eyebrow="topic-card-vault" aside={<StateBadge tone={vaultAsideTone} label={vaultAsideLabel} />}>
          <TopicCard
            captureId={currentCaptureId}
            source="vault list"
            title={titleFromPreview}
            abstract={
              runtime.vaultPreview.data
                ? `target_path=${runtime.vaultPreview.data.target_path}；仍是 preview/dry-run，不代表写入获批。`
                : "默认态保持候选列表视角；没有 preview 时不虚构 vault 文件。"
            }
            badge={{ tone: runtime.vaultPreview.data ? "previewOnly" : "candidate", label: runtime.vaultPreview.data ? "preview_ready" : "candidate_only" }}
          />
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Source URL 聚合">
        <PanelCard
          title="Source URL aggregate"
          eyebrow="topic-card-vault"
          description="当前 runtime 只暴露单 capture 上下文；跨 capture 聚合仍待独立 contract。"
        >
          <div className={styles.aggregate}>
            <div className={styles.headerMeta}>
              <CaptureIdChip value="source_url" muted />
              <span>{runtime.captureSourceUrl ?? runtime.canonicalUrl}</span>
            </div>
            <div className={styles.cards}>
              <TopicCard
                captureId={currentCaptureId}
                source="current source_url"
                title={titleFromPreview}
                abstract="当前只展示 active capture 对应的 source_url 语境。"
              />
              <TopicCard
                captureId="aggregate_pending"
                source="future-gated aggregate"
                title="多 capture 聚合待后续 contract"
                abstract="没有 source_url group API，就不把单卡假装成真实聚合。"
                badge={{ tone: "blocked", label: "contract_missing" }}
              />
            </div>
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 晋升准备度">
        <PanelCard title="Promote readiness" eyebrow="topic-card-vault" description="这里只表达候选准备度，不表达 runtime 或写入批准。">
          <div className={styles.stack}>
            <TopicCard
              captureId={currentCaptureId}
              source="selected candidate"
              title={titleFromPreview}
              abstract="进入下一系统前先看 capture / preview / ledger 是否齐全；true write 仍 blocked。"
              selected={Boolean(runtime.currentCaptureId)}
            />
            <PromoteGate title="晋升 DiloFlow 准备度" items={promoteGateItems} />
            <Button icon={<Icon name="plan" />} variant="blocked" disabled>
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
              <Button variant="blocked" disabled>
                确认晋升
              </Button>
            </>
          }
        >
          <p>当前只允许预览当前 capture 会带出的卡片上下文。跨系统 promote 仍是 candidate，不构成 runtime approval。</p>
          <p>来源: <code>{currentCaptureId}</code> → 目标: DiloFlow 草案（future-gated）</p>
        </Modal>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Obsidian 同步状态">
        <PanelCard
          title="Cross-system sync"
          eyebrow="topic-card-vault"
          description="sync badge 仍保留三态；当前 runtime 只补充 preview / dry-run 真实状态，不假装已发生真同步。"
        >
          <div className={styles.cards}>
            {runtime.vaultPreview.data ? (
              <TopicCard
                captureId={currentCaptureId}
                source="current preview"
                title={titleFromPreview}
                abstract={`target_path=${runtime.vaultPreview.data.target_path}`}
                footer={<SyncBadge state="pending" />}
              />
            ) : null}
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
