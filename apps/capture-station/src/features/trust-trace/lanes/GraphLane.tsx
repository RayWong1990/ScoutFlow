import { useState, type CSSProperties } from "react";

import PanelCard from "../../../components/PanelCard/PanelCard";
import StateBadge from "../../../components/StateBadge/StateBadge";
import type { TrustTraceResponse } from "../../../lib/api-client";
import styles from "./GraphLane.module.css";

type GraphLaneProps = {
  trace: TrustTraceResponse | null;
};

type NodeKey = "capture" | "metadata_job" | "probe_evidence" | "receipt_ledger" | "media_audio" | "audit";

type NodeTone = "ready" | "attention" | "muted";

type NodeField = {
  label: string;
  value: string;
};

type GraphNode = {
  id: NodeKey;
  title: string;
  summary: string;
  tone: NodeTone;
  x: string;
  y: string;
  fields: NodeField[];
};

function stringifyValue(value: string | number | boolean | null): string {
  if (value === null) {
    return "null";
  }
  return typeof value === "boolean" ? String(value) : `${value}`;
}

function formatList(items: string[]): string {
  return items.length > 0 ? items.join(", ") : "[]";
}

function formatSafeFields(fields: Record<string, string | number | null>): string {
  const entries = Object.entries(fields);
  if (entries.length === 0) {
    return "[]";
  }
  return entries.map(([key, value]) => `${key}=${stringifyValue(value)}`).join(", ");
}

function normalizeSignal(value: string | null | undefined): string {
  return value == null ? "" : value.trim().toLowerCase();
}

function isFailureLike(value: string | null | undefined): boolean {
  const normalized = normalizeSignal(value);
  return normalized.includes("fail") || normalized.includes("error") || normalized.includes("blocked") || normalized.includes("not_ready");
}

function isSuccessLike(value: string | null | undefined): boolean {
  const normalized = normalizeSignal(value);
  return normalized === "success" || normalized === "succeeded" || normalized === "completed" || normalized === "ok" || normalized === "metadata_fetched";
}

function getNodeTone(hasSignal: boolean, attention = false): NodeTone {
  if (attention) {
    return "attention";
  }
  return hasSignal ? "ready" : "muted";
}

function getMetadataTone(trace: TrustTraceResponse): NodeTone {
  if (!trace.metadata_job.present) {
    return "muted";
  }
  if (isFailureLike(trace.metadata_job.status) || isFailureLike(trace.metadata_job.platform_result)) {
    return "attention";
  }
  if (isSuccessLike(trace.metadata_job.status) || isSuccessLike(trace.metadata_job.platform_result)) {
    return "ready";
  }
  return "muted";
}

function getAuditTone(trace: TrustTraceResponse): NodeTone {
  if (isFailureLike(trace.audit.platform_result)) {
    return "attention";
  }
  if (trace.audit.artifact_count > 0 && isSuccessLike(trace.audit.platform_result)) {
    return "ready";
  }
  return "muted";
}

function buildGraphNodes(trace: TrustTraceResponse): GraphNode[] {
  return [
    {
      id: "capture",
      title: "capture",
      summary: trace.capture_state.status,
      tone: getNodeTone(trace.capture_state.capture_created),
      x: "12%",
      y: "38%",
      fields: [
        { label: "capture.capture_id", value: trace.capture.capture_id },
        { label: "capture.platform", value: trace.capture.platform },
        { label: "capture.platform_item_id", value: trace.capture.platform_item_id },
        { label: "capture.source_kind", value: trace.capture.source_kind },
        { label: "capture.capture_mode", value: trace.capture.capture_mode },
        { label: "capture.created_by_path", value: trace.capture.created_by_path },
        { label: "capture_state.capture_created", value: stringifyValue(trace.capture_state.capture_created) },
        { label: "capture_state.status", value: trace.capture_state.status },
      ],
    },
    {
      id: "metadata_job",
      title: "metadata_job",
      summary:
        trace.metadata_job.job_type && trace.metadata_job.status
          ? `${trace.metadata_job.job_type} / ${trace.metadata_job.status}`
          : trace.metadata_job.status ?? trace.metadata_job.job_type ?? (trace.metadata_job.present ? "present" : "absent"),
      tone: getMetadataTone(trace),
      x: "40%",
      y: "14%",
      fields: [
        { label: "present", value: stringifyValue(trace.metadata_job.present) },
        { label: "job_id", value: trace.metadata_job.job_id ?? "null" },
        { label: "job_type", value: trace.metadata_job.job_type ?? "null" },
        { label: "status", value: trace.metadata_job.status ?? "null" },
        { label: "platform_result", value: trace.metadata_job.platform_result ?? "null" },
      ],
    },
    {
      id: "probe_evidence",
      title: "probe_evidence",
      summary: trace.probe_evidence.present ? trace.probe_evidence.probe_mode : "absent",
      tone: getNodeTone(trace.probe_evidence.present),
      x: "69%",
      y: "10%",
      fields: [
        { label: "present", value: stringifyValue(trace.probe_evidence.present) },
        { label: "probe_mode", value: trace.probe_evidence.probe_mode },
        { label: "source_task_id", value: trace.probe_evidence.source_task_id ?? "null" },
        { label: "source_report_path", value: trace.probe_evidence.source_report_path ?? "null" },
        { label: "platform_result", value: trace.probe_evidence.platform_result ?? "null" },
      ],
    },
    {
      id: "receipt_ledger",
      title: "receipt_ledger",
      summary: trace.receipt_ledger.present ? `artifacts ${trace.receipt_ledger.artifact_count}` : "absent",
      tone: getNodeTone(trace.receipt_ledger.present || trace.receipt_ledger.artifact_count > 0),
      x: "74%",
      y: "44%",
      fields: [
        { label: "present", value: stringifyValue(trace.receipt_ledger.present) },
        { label: "artifact_count", value: `${trace.receipt_ledger.artifact_count}` },
        { label: "artifact_kinds", value: formatList(trace.receipt_ledger.artifact_kinds) },
        { label: "redaction", value: trace.receipt_ledger.redaction },
      ],
    },
    {
      id: "media_audio",
      title: "media_audio",
      summary: `${trace.media_audio.status} / ${trace.media_audio.audio_transcript}`,
      tone: getNodeTone(false, trace.media_audio.audio_transcript === "blocked"),
      x: "43%",
      y: "70%",
      fields: [
        { label: "status", value: trace.media_audio.status },
        { label: "audio_transcript", value: trace.media_audio.audio_transcript },
      ],
    },
    {
      id: "audit",
      title: "audit",
      summary: trace.audit.platform_result ?? `fields ${Object.keys(trace.audit.safe_parsed_fields).length}`,
      tone: getAuditTone(trace),
      x: "74%",
      y: "76%",
      fields: [
        { label: "platform_result", value: trace.audit.platform_result ?? "null" },
        { label: "evidence_file_path", value: trace.audit.evidence_file_path ?? "null" },
        { label: "artifact_count", value: `${trace.audit.artifact_count}` },
        { label: "redaction_policy", value: trace.audit.redaction_policy ?? "null" },
        { label: "safe_parsed_fields", value: formatSafeFields(trace.audit.safe_parsed_fields) },
      ],
    },
  ];
}

function nodeStyle(node: GraphNode): CSSProperties {
  return {
    "--node-x": node.x,
    "--node-y": node.y,
  } as CSSProperties;
}

export default function GraphLane({ trace }: GraphLaneProps) {
  const [activeNodeId, setActiveNodeId] = useState<NodeKey | null>(null);

  if (!trace) {
    return (
      <PanelCard title="W1B graph lane" eyebrow="trust-trace" aside={<StateBadge tone="idle" label="empty" />}>
        <div className={styles.cardBody}>
          <div className={styles.emptyState}>
            <p className={styles.emptyTitle}>capture readback 为空时，不伪造 section 节点或连线。</p>
            <p className={styles.muted}>等待 trust-trace readback 后再显示基于 DTO 的 section map。</p>
          </div>
        </div>
      </PanelCard>
    );
  }

  const nodes = buildGraphNodes(trace);
  const activeNode = nodes.find((node) => node.id === activeNodeId) ?? null;

  return (
    <PanelCard title="W1B graph lane" eyebrow="trust-trace" aside={<StateBadge tone="candidate" label="dto-bounded" />}>
      <div className={styles.cardBody}>
        <p className={styles.boundaryNote}>当前图仅表示 trust-trace DTO section 邻接关系，不表示时间线、执行顺序或服务端确认因果。</p>

        <div className={styles.graphShell}>
          <div className={styles.graphViewport} onMouseLeave={() => setActiveNodeId(null)}>
            <svg
              aria-label="Trust Trace graph"
              className={styles.graphSvg}
              role="img"
              viewBox="0 0 640 360"
            >
              <title>Trust Trace graph</title>
              <defs>
                <pattern id="trust-trace-grid" width="32" height="32" patternUnits="userSpaceOnUse">
                  <path d="M 32 0 L 0 0 0 32" className={styles.gridLine} fill="none" />
                </pattern>
                <linearGradient id="trust-trace-wire" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stopColor="rgba(117, 251, 253, 0.18)" />
                  <stop offset="100%" stopColor="rgba(81, 162, 255, 0.62)" />
                </linearGradient>
              </defs>
              <rect className={styles.viewportBackground} height="360" width="640" x="0" y="0" />
              <rect className={styles.gridField} height="360" width="640" x="0" y="0" />
              <path className={styles.primaryWire} d="M 166 168 C 236 136, 212 98, 284 86" />
              <path className={styles.primaryWire} d="M 166 168 C 264 148, 352 100, 454 76" />
              <path className={styles.primaryWire} d="M 166 168 C 286 174, 382 192, 490 196" />
              <path className={styles.primaryWire} d="M 166 168 C 254 226, 276 266, 310 286" />
              <path className={styles.primaryWire} d="M 490 196 C 516 236, 522 262, 506 302" />
              <path className={styles.secondaryWire} d="M 284 86 C 362 72, 402 68, 454 76" />
              <path className={styles.secondaryWire} d="M 454 76 C 500 116, 510 146, 490 196" />
              <path className={styles.secondaryWire} d="M 310 286 C 392 292, 438 298, 506 302" />
            </svg>

            <div className={styles.nodeLayer}>
              {nodes.map((node) => {
                const isActive = activeNode?.id === node.id;
                return (
                  <button
                    key={node.id}
                    aria-label={`section node ${node.title}`}
                    className={[
                      styles.nodeButton,
                      styles[`tone${node.tone[0].toUpperCase()}${node.tone.slice(1)}`],
                      isActive ? styles.nodeActive : "",
                    ].filter(Boolean).join(" ")}
                    data-tone={node.tone}
                    onBlur={() => setActiveNodeId((current) => (current === node.id ? null : current))}
                    onFocus={() => setActiveNodeId(node.id)}
                    onMouseEnter={() => setActiveNodeId(node.id)}
                    style={nodeStyle(node)}
                    type="button"
                  >
                    <span className={styles.nodeTitle}>{node.title}</span>
                    <span className={styles.nodeSummary}>{node.summary}</span>
                  </button>
                );
              })}
            </div>
          </div>

          <div className={styles.detailPane}>
            {activeNode ? (
              <section aria-label={`node detail ${activeNode.id}`} className={styles.detailCard} role="region">
                <header className={styles.detailHeader}>
                  <span className={styles.detailEyebrow}>bounded detail</span>
                  <h3>{activeNode.title}</h3>
                  <p>{activeNode.summary}</p>
                </header>
                <dl className={styles.detailGrid}>
                  {activeNode.fields.map((field) => (
                    <div key={field.label} className={styles.detailRow}>
                      <dt>{field.label}</dt>
                      <dd>{field.value}</dd>
                    </div>
                  ))}
                </dl>
              </section>
            ) : (
              <div className={styles.detailEmpty}>
                <p>悬停或聚焦节点后再查看限定字段。</p>
                <p className={styles.muted}>细节仅来自当前 TrustTraceResponse；不补时间戳、不补 route 外字段。</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </PanelCard>
  );
}
