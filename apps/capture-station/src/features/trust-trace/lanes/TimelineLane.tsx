import { useEffect, useState, type ReactNode } from "react";
import type { TrustTraceResponse } from "../../../lib/api-client";
import PanelCard from "../../../components/PanelCard/PanelCard";
import StateBadge from "../../../components/StateBadge/StateBadge";
import styles from "./TimelineLane.module.css";

type TimelineLaneProps = {
  trace: TrustTraceResponse | null;
};

type SequenceDetail = {
  label: string;
  value: ReactNode;
};

type SequenceItem = {
  id: string;
  summary: string;
  details: SequenceDetail[];
};

function formatNullable(value: string | number | null): string {
  return value == null ? "null" : String(value);
}

function formatStringList(items: string[]): ReactNode {
  if (items.length === 0) {
    return "none";
  }

  return (
    <ul className={styles.detailList}>
      {items.map((item) => (
        <li key={item}>{item}</li>
      ))}
    </ul>
  );
}

function formatSafeParsedFields(fields: TrustTraceResponse["audit"]["safe_parsed_fields"]): ReactNode {
  const entries = Object.entries(fields);
  if (entries.length === 0) {
    return "none";
  }

  return (
    <ul className={styles.detailList}>
      {entries.map(([key, value]) => (
        <li key={key}>
          <strong>{key}</strong>: {formatNullable(value)}
        </li>
      ))}
    </ul>
  );
}

function buildSequence(trace: TrustTraceResponse): SequenceItem[] {
  return [
    {
      id: "capture",
      summary: `${trace.capture.platform} / ${trace.capture.platform_item_id}`,
      details: [
        { label: "capture_id", value: trace.capture.capture_id },
        { label: "source_kind", value: trace.capture.source_kind },
        { label: "capture_mode", value: trace.capture.capture_mode },
        { label: "created_by_path", value: trace.capture.created_by_path },
      ],
    },
    {
      id: "capture_state",
      summary: trace.capture_state.capture_created ? trace.capture_state.status : "capture_not_created",
      details: [
        { label: "capture_created", value: String(trace.capture_state.capture_created) },
        { label: "status", value: trace.capture_state.status },
      ],
    },
    {
      id: "metadata_job",
      summary: trace.metadata_job.present ? trace.metadata_job.status ?? "present_without_status" : "absent",
      details: [
        { label: "present", value: String(trace.metadata_job.present) },
        { label: "job_id", value: formatNullable(trace.metadata_job.job_id) },
        { label: "job_type", value: formatNullable(trace.metadata_job.job_type) },
        { label: "status", value: formatNullable(trace.metadata_job.status) },
        { label: "platform_result", value: formatNullable(trace.metadata_job.platform_result) },
      ],
    },
    {
      id: "probe_evidence",
      summary: trace.probe_evidence.present ? trace.probe_evidence.platform_result ?? trace.probe_evidence.probe_mode : "absent",
      details: [
        { label: "present", value: String(trace.probe_evidence.present) },
        { label: "probe_mode", value: trace.probe_evidence.probe_mode },
        { label: "source_task_id", value: formatNullable(trace.probe_evidence.source_task_id) },
        { label: "source_report_path", value: formatNullable(trace.probe_evidence.source_report_path) },
        { label: "platform_result", value: formatNullable(trace.probe_evidence.platform_result) },
      ],
    },
    {
      id: "receipt_ledger",
      summary: trace.receipt_ledger.present ? `${trace.receipt_ledger.artifact_count} artifact(s)` : "absent",
      details: [
        { label: "present", value: String(trace.receipt_ledger.present) },
        { label: "artifact_count", value: String(trace.receipt_ledger.artifact_count) },
        { label: "artifact_kinds", value: formatStringList(trace.receipt_ledger.artifact_kinds) },
        { label: "redaction", value: trace.receipt_ledger.redaction },
      ],
    },
    {
      id: "media_audio",
      summary: trace.media_audio.status,
      details: [
        { label: "status", value: trace.media_audio.status },
        { label: "audio_transcript", value: trace.media_audio.audio_transcript },
      ],
    },
    {
      id: "audit",
      summary: trace.audit.platform_result ?? "no_platform_result",
      details: [
        { label: "platform_result", value: formatNullable(trace.audit.platform_result) },
        { label: "evidence_file_path", value: formatNullable(trace.audit.evidence_file_path) },
        { label: "artifact_count", value: String(trace.audit.artifact_count) },
        { label: "redaction_policy", value: formatNullable(trace.audit.redaction_policy) },
        { label: "safe_parsed_fields", value: formatSafeParsedFields(trace.audit.safe_parsed_fields) },
      ],
    },
  ];
}

export default function TimelineLane({ trace }: TimelineLaneProps) {
  const sequence = trace ? buildSequence(trace) : [];
  const [activeId, setActiveId] = useState<string | null>(sequence[0]?.id ?? null);

  useEffect(() => {
    if (!trace) {
      if (activeId !== null) {
        setActiveId(null);
      }
      return;
    }

    const nextSequence = buildSequence(trace);

    if (!activeId || !nextSequence.some((item) => item.id === activeId)) {
      setActiveId(nextSequence[0]?.id ?? null);
    }
  }, [activeId, trace]);

  const activeItem = sequence.find((item) => item.id === activeId) ?? sequence[0] ?? null;

  return (
    <PanelCard title="W1B timeline lane" eyebrow="trust-trace" aside={<StateBadge tone="candidate" label="readback-only" />}>
      <div className={styles.cardBody}>
        {trace ? (
          <>
            <div className={styles.headingBlock}>
              <h3 className={styles.heading}>证据顺序，不代表真实时间轴</h3>
              <p className={styles.muted}>顺序只来自现有 DTO section 与 status，不代表真实时间戳。</p>
            </div>
            <div className={styles.timelineGrid}>
              <ol className={styles.sequenceList}>
                {sequence.map((item, index) => {
                  const isActive = item.id === activeItem?.id;

                  return (
                    <li key={item.id}>
                      <button
                        type="button"
                        className={isActive ? styles.sequenceButtonActive : styles.sequenceButton}
                        aria-pressed={isActive}
                        onMouseEnter={() => setActiveId(item.id)}
                        onFocus={() => setActiveId(item.id)}
                      >
                        <span className={styles.stepIndex}>{index + 1}</span>
                        <span className={styles.stepCopy}>
                          <span className={styles.stepId}>{item.id}</span>
                          <span className={styles.stepSummary}>{item.summary}</span>
                        </span>
                      </button>
                    </li>
                  );
                })}
              </ol>
              {activeItem ? (
                <section className={styles.detailPanel} role="region" aria-label="当前证据详情">
                  <p className={styles.detailEyebrow}>当前证据详情</p>
                  <h4 className={styles.detailTitle}>{activeItem.id}</h4>
                  <p className={styles.detailSummary}>{activeItem.summary}</p>
                  <dl className={styles.detailGrid}>
                    {activeItem.details.map((detail) => (
                      <div key={detail.label} className={styles.detailRow}>
                        <dt>{detail.label}</dt>
                        <dd>{detail.value}</dd>
                      </div>
                    ))}
                  </dl>
                </section>
              ) : null}
            </div>
            <p className={styles.muted}>hover 或键盘 focus 只切换当前 DTO section 的证据详情；不推断 wall-clock time。</p>
          </>
        ) : (
          <div className={styles.emptyState}>
            <p className={styles.emptyTitle}>没有 trust-trace readback，不生成伪时间轴或假时间戳。</p>
            <p className={styles.muted}>只有 route readback 到位后，才按 DTO section 顺序展示证据。</p>
          </div>
        )}
      </div>
    </PanelCard>
  );
}
