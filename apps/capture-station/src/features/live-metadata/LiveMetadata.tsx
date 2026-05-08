import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame from "../../components/SurfaceFrame/SurfaceFrame";
import TagList from "../../components/TagList/TagList";
import type { TagItem } from "../../components/TagList/TagList";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import { getMetadataSummary, getSafeParsedEntries } from "../url-bar/w2cSurfaceState";
import styles from "./LiveMetadata.module.css";

export default function LiveMetadata() {
  const runtime = useW2CRuntime();
  const metadataSummary = getMetadataSummary(runtime);
  const safeEntries = getSafeParsedEntries(runtime.trustTrace.data);

  const metadataRows = safeEntries.length > 0 ? safeEntries : [
    ["capture_id", runtime.currentCaptureId ?? "未创建 capture"],
    ["platform_item_id", runtime.capture.data?.platform_item_id ?? "等待 discover"],
    ["capture_state.status", runtime.trustTrace.data?.capture_state.status ?? runtime.capture.data?.status ?? runtime.capture.status],
    ["metadata_fetch.status", runtime.trustTrace.data?.metadata_job.status ?? runtime.metadataFetch.data?.status ?? runtime.metadataFetch.status],
    ["probe_evidence", runtime.trustTrace.data?.probe_evidence.present ? "present" : "absent"],
    ["receipt_ledger", runtime.trustTrace.data?.receipt_ledger.present ? `present (${runtime.trustTrace.data.receipt_ledger.artifact_count})` : "absent"],
    ["audit.platform_result", runtime.trustTrace.data?.audit.platform_result ?? "null"],
    ["metadata detail readback", "future-gated / not routed"],
  ];

  const tags: TagItem[] = [
    { label: "discover", tone: "info" as const },
    { label: "metadata_fetch enqueue", tone: "focus" as const },
    { label: runtime.trustTrace.data ? "trust_trace readback" : "trust_trace pending", tone: runtime.trustTrace.data ? "success" : "blocked" as const },
    { label: safeEntries.length > 0 ? "safe_metadata_evidence" : "metadata detail route missing", tone: safeEntries.length > 0 ? "success" : "blocked" as const },
    { label: "audio_transcript blocked", tone: "blocked" as const },
  ];

  return (
    <SurfaceFrame title="实时元数据" description="只展示 discover / metadata_fetch / trust-trace 当前能证明的 truth，不把 enqueue 伪装成 loaded metadata。">
      <div className={styles.stack}>
        <PanelCard
          title="元数据读回"
          eyebrow="live-metadata"
          description="safe fields 来自 trust-trace audit；没有 readback 证据时会明确保留路由缺口。"
          aside={<StateBadge tone={metadataSummary.tone} label={metadataSummary.label} />}
        >
          <div className={styles.stack}>
            <p className={styles.note}>{metadataSummary.detail}</p>
            <dl className={styles.grid}>
              {metadataRows.map(([label, value]) => (
                <div key={label} style={{ display: "contents" }}>
                  <dt>{label}</dt>
                  <dd className={typeof value === "string" && /\d/.test(value) ? styles.numberValue : undefined}>{value}</dd>
                </div>
              ))}
            </dl>
            <TagList items={tags} />
          </div>
        </PanelCard>

        <PanelCard
          title="字段来源"
          eyebrow="live-metadata"
          description="当前没有独立 metadata detail route；这里只说明字段能否被现有路由证明。"
        >
          <dl className={styles.grid}>
            <div style={{ display: "contents" }}>
              <dt>discover</dt>
              <dd>capture_id / platform_item_id / source_kind / capture_mode</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>metadata_fetch enqueue</dt>
              <dd>job_id / job_type / queued|running|succeeded|failed</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>trust_trace</dt>
              <dd>capture_state / probe_evidence / receipt_ledger / audit.safe_parsed_fields</dd>
            </div>
            <div style={{ display: "contents" }}>
              <dt>metadata detail readback</dt>
              <dd>future-gated；当前未见独立 GET route</dd>
            </div>
          </dl>
        </PanelCard>
      </div>
    </SurfaceFrame>
  );
}
