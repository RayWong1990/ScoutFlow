import { useW2CRuntime } from "../../lib/w2c-runtime";
import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import TagList from "../../components/TagList/TagList";
import TopicCard from "../../components/TopicCard/TopicCard";
import styles from "./TopicCardLite.module.css";

export default function TopicCardLite() {
  const runtime = useW2CRuntime();
  const titleFromTrace = typeof runtime.trustTrace.data?.audit.safe_parsed_fields.title === "string"
    ? runtime.trustTrace.data.audit.safe_parsed_fields.title
    : null;
  const durationFromTrace = runtime.trustTrace.data?.audit.safe_parsed_fields.duration;
  const durationLabel = typeof durationFromTrace === "string" ? durationFromTrace : undefined;
  const currentCaptureId = runtime.currentCaptureId ?? "capture_pending";
  const currentTitle = titleFromTrace ?? `当前 capture ${currentCaptureId}`;
  const metadataJobStatus = runtime.trustTrace.data?.metadata_job.status ?? runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status;
  const captureAbstract = runtime.currentCaptureId
    ? `capture_state=${runtime.trustTrace.data?.capture_state.status ?? runtime.capture.data?.status ?? "pending"}；metadata_fetch=${metadataJobStatus}。`
    : "当前还没有 active capture；此 surface 只显示 candidate 壳，不推断后续 runtime。";
  const artifactKinds = runtime.trustTrace.data?.receipt_ledger.artifact_kinds ?? [];
  const safeParsedFields = Object.entries(runtime.trustTrace.data?.audit.safe_parsed_fields ?? {}).slice(0, 3);

  return (
    <SurfaceFrame
      title="Topic Card Lite 状态集"
      description="当前 capture 上下文优先展示；缺失 contract 的部分保留 candidate / blocked 口径，不推断 runtime 已获批。"
    >
      <SurfaceSection title="状态: 当前 capture 上下文">
        <TopicCard
          captureId={currentCaptureId}
          source={runtime.capture.data ? `${runtime.capture.data.platform} / ${runtime.capture.data.capture_mode}` : "candidate context"}
          title={currentTitle}
          abstract={captureAbstract}
          badge={{
            tone: runtime.currentCaptureId ? "metadataOnly" : "candidate",
            label: runtime.currentCaptureId ? "capture_bound" : "candidate_only",
          }}
          footer={
            <div className={styles.footerMeta}>
              <span>metadata_fetch {metadataJobStatus}</span>
              <span>receipt_artifacts {runtime.trustTrace.data?.receipt_ledger.artifact_count ?? 0}</span>
              <span>runtime {runtime.isRuntimeBlocked ? "blocked" : "future"}</span>
            </div>
          }
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: Bilibili 视频">
        <TopicCard
          captureId={currentCaptureId}
          source={runtime.capture.data?.platform === "bilibili" ? "Bilibili / metadata_only" : "视频 contract 待补齐"}
          title={currentTitle}
          abstract={
            runtime.capture.data?.platform === "bilibili"
              ? "沿用当前 capture 的平台上下文；缩略图、正文、评论仍受后续 contract gating。"
              : "当前 capture 不是 Bilibili 视频态，视频专属字段保持 future-gated。"
          }
          thumbnailLabel={durationLabel}
          selected={Boolean(runtime.currentCaptureId)}
          badge={{ tone: runtime.currentCaptureId ? "candidate" : "blocked", label: runtime.currentCaptureId ? "metadata_only" : "not_loaded" }}
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 多信号">
        <div className={styles.stack}>
          <TopicCard
            captureId={currentCaptureId}
            source="多信号候选"
            title={runtime.currentCaptureId ? "当前 capture 的已知信号外壳" : "多信号聚合仍是候选壳"}
            abstract={
              runtime.currentCaptureId
                ? "当前只复用 trust-trace 已回传的 artifact kinds；评论、ASR、聚合排序都保持 future-gated。"
                : "没有 active capture 时，不虚构信号聚合或排序结果。"
            }
          />
          <TagList
            items={
              artifactKinds.length > 0
                ? artifactKinds.slice(0, 4).map((label, index) => ({
                    label,
                    tone: index === 0 ? "focus" : undefined,
                  }))
                : [{ label: "future_gated", tone: "info" }, { label: "no_artifact_kinds", tone: "blocked" }]
            }
          />
        </div>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 证据指针">
        <TopicCard
          captureId={currentCaptureId}
          source="证据指针"
          title="Safe parsed fields stay visible before promote"
          abstract="当前只暴露 trust-trace 已返回的 safe_parsed_fields；未回传字段保持 blocked / deferred。"
          footer={
            <div className={styles.footerMeta}>
              {safeParsedFields.length > 0 ? (
                safeParsedFields.map(([key, value]) => <CaptureIdChip key={key} value={`${key}:${String(value)}`} muted />)
              ) : (
                <>
                  <CaptureIdChip value="safe_parsed_fields:pending" muted />
                  <CaptureIdChip value="comments:blocked" muted />
                  <CaptureIdChip value="visual_evidence:deferred" muted />
                </>
              )}
            </div>
          }
        />
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 双卡对比">
        <div className={styles.compare}>
          <TopicCard
            captureId={currentCaptureId}
            source="当前 capture"
            title={currentTitle}
            abstract="左侧永远绑定当前 capture 真状态，不把 candidate 推断写成已验证结论。"
            badge={{ tone: runtime.currentCaptureId ? "candidate" : "blocked", label: runtime.currentCaptureId ? "current_context" : "pending_capture" }}
          />
          <TopicCard
            captureId="future_gate"
            source="future-gated lane"
            title="评论 / ASR / 多卡排序仍待后续 contract"
            abstract="没有 runtime approval、没有新增 API、没有后台扩写；这里只保留下一阶段占位。"
            badge={{ tone: "blocked", label: "future_gated" }}
          />
        </div>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
