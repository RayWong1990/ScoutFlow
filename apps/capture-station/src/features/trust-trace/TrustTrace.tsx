import type { ReactNode } from "react";

import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import ErrorPathLane from "./lanes/ErrorPathLane";
import GraphLane from "./lanes/GraphLane";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import { deriveTrustTraceBadge } from "../../components/StateBadge/derive";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import TimelineLane from "./lanes/TimelineLane";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import "../../styles/trust-trace-lane-order.css";
import styles from "./TrustTrace.module.css";

type Field = {
  label: string;
  value: ReactNode;
};

function FieldGrid({ fields }: { fields: Field[] }) {
  return (
    <dl className={styles.grid}>
      {fields.map((field) => (
        <div key={field.label} style={{ display: "contents" }}>
          <dt>{field.label}</dt>
          <dd>{field.value}</dd>
        </div>
      ))}
    </dl>
  );
}

function stringifyValue(value: string | number | boolean | null): string {
  if (value === null) {
    return "null";
  }
  return typeof value === "boolean" ? String(value) : `${value}`;
}

function renderList(items: string[]) {
  if (items.length === 0) {
    return <span className={styles.muted}>[]</span>;
  }

  return (
    <ul className={styles.inlineList}>
      {items.map((item) => (
        <li key={item}>
          <code>{item}</code>
        </li>
      ))}
    </ul>
  );
}

function renderAuditFields(fields: Record<string, string | number | null>) {
  const entries = Object.entries(fields);
  if (entries.length === 0) {
    return <span className={styles.muted}>safe_parsed_fields=[]</span>;
  }

  return (
    <ul className={styles.inlineList}>
      {entries.map(([key, value]) => (
        <li key={key}>
          <code>{key}</code>
          <span>{stringifyValue(value)}</span>
        </li>
      ))}
    </ul>
  );
}

function formatAudioTranscriptDisplay(value: string): string {
  const normalized = value.trim();
  if (!normalized) {
    return "not_present";
  }
  if (normalized.toLowerCase() === "blocked") {
    return "blocked";
  }
  if (normalized.length > 80) {
    return `${normalized.slice(0, 80)}... [truncated]`;
  }
  return `${normalized} [preview]`;
}

export default function TrustTrace() {
  const runtime = useW2CRuntime();
  const { currentCaptureId, trustTrace } = runtime;
  const trace = trustTrace.data;
  const audioTranscriptDisplay = trace ? formatAudioTranscriptDisplay(trace.media_audio.audio_transcript) : null;
  const trustTraceBadge = deriveTrustTraceBadge({
    trace,
    routeStatus: trustTrace.status,
    currentCaptureId,
  });
  const statusBadge = <StateBadge tone={trustTraceBadge.tone} label={trustTraceBadge.label} />;

  return (
    <SurfaceFrame
      title="信任溯源状态集"
      description="GET /captures/{id}/trust-trace 的 readback shell 只消费分层 DTO；顶层先看 error-path summary，graph 降级为 secondary diagnostic。"
    >
      <SurfaceSection title="状态: error-path first">
        <div className="trustTraceLaneOrder">
          <div className="trustTraceLaneErrorPath">
            <ErrorPathLane
              trace={trace ?? null}
              routeStatus={trustTrace.status}
              routeErrorCode={trustTrace.error?.code ?? null}
            />
          </div>
          <div className="trustTraceLaneTimeline">
            <TimelineLane trace={trace ?? null} />
          </div>
          <div className="trustTraceLaneGraph">
            <GraphLane trace={trace ?? null} />
          </div>
        </div>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: route readback">
        <PanelCard
          title="Trust Trace readback"
          eyebrow="trust-trace"
          description="只读回显 capture / capture_state / metadata_job / probe_evidence / receipt_ledger / media_audio / audit；业务风险先由 error-path lane 表达。"
          aside={statusBadge}
        >
          <div className={styles.stack}>
            <div className={styles.routeMeta}>
              <span>route:</span>
              <code>GET /captures/{currentCaptureId ?? "{id}"}/trust-trace</code>
              <span>capture_id:</span>
              {currentCaptureId ? <CaptureIdChip value={currentCaptureId} /> : <span className={styles.muted}>none</span>}
            </div>

            {trustTrace.status === "loading" ? (
              <p className={styles.notice}>正在读取 trust-trace readback；不替换为 fixture success。</p>
            ) : null}

            {trustTrace.status === "error" && trustTrace.error ? (
              <div className={styles.errorBox} role="alert">
                <p className={styles.errorTitle}>Trust trace route unavailable</p>
                <FieldGrid
                  fields={[
                    { label: "status", value: trustTrace.error.status },
                    { label: "code", value: trustTrace.error.code ?? "unknown_error" },
                    { label: "message", value: trustTrace.error.message },
                  ]}
                />
                <p className={styles.errorNote}>不生成假图谱，不把 503 包装成 success。</p>
              </div>
            ) : null}

            {!trace && trustTrace.status === "idle" ? (
              <div className={styles.emptyState}>
                <p>创建 metadata-only capture 后再查看 Trust Trace readback。</p>
                <p className={styles.muted}>graph / timeline / error-path 仍保留给 W1B</p>
              </div>
            ) : null}

            {!trace && trustTrace.status === "loading" ? (
              <div className={styles.placeholder} data-todo="trust-trace-loading">
                trust-trace route 正在加载，当前不渲染旧 fixture。
              </div>
            ) : null}

            {trace ? (
              <div className={styles.panelGrid}>
                <PanelCard title="capture / capture_state" eyebrow="trust-trace">
                  <div className={styles.stack}>
                    <p className={styles.label}>{trace.label}</p>
                    <FieldGrid
                      fields={[
                        { label: "capture.capture_id", value: <CaptureIdChip value={trace.capture.capture_id} /> },
                        { label: "capture.platform", value: trace.capture.platform },
                        { label: "capture.platform_item_id", value: trace.capture.platform_item_id },
                        { label: "capture.source_kind", value: trace.capture.source_kind },
                        { label: "capture.capture_mode", value: trace.capture.capture_mode },
                        { label: "capture.created_by_path", value: trace.capture.created_by_path },
                        { label: "capture_state.capture_created", value: stringifyValue(trace.capture_state.capture_created) },
                        { label: "capture_state.status", value: trace.capture_state.status },
                      ]}
                    />
                  </div>
                </PanelCard>

                <PanelCard title="metadata_job" eyebrow="trust-trace">
                  <FieldGrid
                    fields={[
                      { label: "present", value: stringifyValue(trace.metadata_job.present) },
                      { label: "job_id", value: trace.metadata_job.job_id ?? "null" },
                      { label: "job_type", value: trace.metadata_job.job_type ?? "null" },
                      { label: "status", value: trace.metadata_job.status ?? "null" },
                      { label: "platform_result", value: trace.metadata_job.platform_result ?? "null" },
                    ]}
                  />
                </PanelCard>

                <PanelCard title="probe_evidence" eyebrow="trust-trace">
                  <FieldGrid
                    fields={[
                      { label: "present", value: stringifyValue(trace.probe_evidence.present) },
                      { label: "probe_mode", value: trace.probe_evidence.probe_mode },
                      { label: "source_task_id", value: trace.probe_evidence.source_task_id ?? "null" },
                      { label: "source_report_path", value: trace.probe_evidence.source_report_path ?? "null" },
                      { label: "platform_result", value: trace.probe_evidence.platform_result ?? "null" },
                    ]}
                  />
                </PanelCard>

                <PanelCard title="receipt_ledger" eyebrow="trust-trace">
                  <FieldGrid
                    fields={[
                      { label: "present", value: stringifyValue(trace.receipt_ledger.present) },
                      { label: "artifact_count", value: trace.receipt_ledger.artifact_count },
                      { label: "artifact_kinds", value: renderList(trace.receipt_ledger.artifact_kinds) },
                      { label: "redaction", value: trace.receipt_ledger.redaction },
                    ]}
                  />
                </PanelCard>

                <PanelCard title="media_audio" eyebrow="trust-trace">
                  <FieldGrid
                    fields={[
                      { label: "status", value: trace.media_audio.status },
                      { label: "audio_transcript_preview", value: audioTranscriptDisplay ?? "not_present" },
                    ]}
                  />
                </PanelCard>

                <PanelCard title="audit" eyebrow="trust-trace">
                  <FieldGrid
                    fields={[
                      { label: "platform_result", value: trace.audit.platform_result ?? "null" },
                      { label: "evidence_file_path", value: trace.audit.evidence_file_path ?? "null" },
                      { label: "artifact_count", value: trace.audit.artifact_count },
                      { label: "redaction_policy", value: trace.audit.redaction_policy ?? "null" },
                      { label: "safe_parsed_fields", value: renderAuditFields(trace.audit.safe_parsed_fields) },
                    ]}
                  />
                </PanelCard>
              </div>
            ) : null}
          </div>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
