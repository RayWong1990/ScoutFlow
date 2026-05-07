import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import TagList from "../../components/TagList/TagList";
import TopicCard from "../../components/TopicCard/TopicCard";
import styles from "./TopicCardLite.module.css";

export default function TopicCardLite() {
  return (
    <SurfaceFrame title="Topic Card Lite 状态集" description="新闻、视频、多信号、证据指针和双卡对比全部转为 React TSX。">
      <SurfaceSection title="状态: 新闻文章">
        <TopicCard
          captureId="cap_20260506_8a3f2"
          source="新闻 / 长文"
          title="深度工作流正在把高频研究从即时响应改成证据先入账"
          abstract="将高频输入先收进候选选题卡，再做人工裁决，能显著降低上下文切换。"
          footer={<div className={styles.footerMeta}><span>支持证据 4 条</span><span>冲突证据 1 条</span></div>}
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Bilibili 视频">
        <TopicCard
          captureId="cap_20260506_91b7c"
          source="Bilibili / 视频"
          title="深度工作流 vs 普通工作流 — 高效操作员的 5 个习惯"
          abstract="保留视频态的缩略图、时长与 capture_id 语义。"
          thumbnailLabel="12:34"
          selected
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 多信号">
        <div className={styles.stack}>
          <TopicCard
            captureId="cap_20260506_a02ef"
            source="多信号聚合"
            title="异步协作、证据入账与知识飞轮正在收敛成同一条研究动作链"
            abstract="多条信号可以并排汇总，但不直接跳到 runtime 或晋升结论。"
          />
          <TagList items={[{ label: "异步协作", tone: "success" }, { label: "证据入账", tone: "focus" }, { label: "知识飞轮" }]} />
        </div>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 证据指针">
        <TopicCard
          captureId="cap_20260506_7f31a"
          source="证据指针"
          title="Counter-evidence stays visible before promote"
          abstract="保留支持 / 反证并存的工作台语义，不把冲突证据藏起来。"
          footer={
            <div className={styles.footerMeta}>
              <CaptureIdChip value="dom.meta.og:title" muted />
              <CaptureIdChip value="json.ld.duration" muted />
              <CaptureIdChip value="deferred_visual_evidence" muted />
            </div>
          }
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 双卡对比">
        <div className={styles.compare}>
          <TopicCard
            captureId="cap_20260506_8a3f2"
            source="候选 A"
            title="异步优先更稳定"
            abstract="高频采集场景中，异步先收集证据再判断。"
            badge={{ tone: "ready", label: "76.4%" }}
          />
          <TopicCard
            captureId="cap_20260506_91b7c"
            source="候选 B"
            title="同步确认更可靠"
            abstract="人工裁决更稳，但交互成本更高。"
            badge={{ tone: "candidate", label: "43.1%" }}
          />
        </div>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
