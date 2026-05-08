import type { TrustTraceResponse } from "../../../lib/api-client";
import PanelCard from "../../../components/PanelCard/PanelCard";
import StateBadge from "../../../components/StateBadge/StateBadge";
import styles from "./ErrorPathLane.module.css";

type ErrorPathLaneProps = {
  trace: TrustTraceResponse | null;
  routeStatus: "idle" | "loading" | "success" | "error";
  routeErrorCode: string | null;
};

type StepTone = "clear" | "degraded" | "blocked";

type StepCard = {
  key: string;
  label: string;
  tone: StepTone;
  summary: string;
  detail: string;
};

function isBlank(value: string | null | undefined): boolean {
  return value == null || value.trim().length === 0;
}

function normalizeStatus(value: string | null | undefined): string {
  return value == null ? "" : value.trim().toLowerCase();
}

function isFailureLike(value: string | null | undefined): boolean {
  const normalized = normalizeStatus(value);
  return (
    normalized.includes("fail")
    || normalized.includes("error")
    || normalized.includes("blocked")
    || normalized.includes("not_ready")
    || normalized === "rejected"
  );
}

function isSuccessLike(value: string | null | undefined): boolean {
  const normalized = normalizeStatus(value);
  return normalized === "success" || normalized === "succeeded" || normalized === "completed" || normalized === "metadata_fetched" || normalized === "ok";
}

function classifyAudio(trace: TrustTraceResponse): StepCard {
  const normalizedStatus = trace.media_audio.status.toLowerCase();

  if (normalizedStatus.includes("blocked") || normalizedStatus.includes("disabled") || normalizedStatus.includes("unavailable")) {
    return {
      key: "audio",
      label: "audio transcript",
      tone: "blocked",
      summary: `media_audio.status=${trace.media_audio.status}`,
      detail: "音频转写字段本身标记为 blocked/disabled/unavailable，本 lane 只回显该状态。",
    };
  }

  if (isBlank(trace.media_audio.audio_transcript)) {
    return {
      key: "audio",
      label: "audio transcript",
      tone: "degraded",
      summary: "audio_transcript 为空",
      detail: `media_audio.status=${trace.media_audio.status}`,
    };
  }

  return {
    key: "audio",
    label: "audio transcript",
    tone: "clear",
    summary: `media_audio.status=${trace.media_audio.status}`,
    detail: "audio_transcript 已有内容，当前不展开 transcript 细节。",
  };
}

function buildStepCards(trace: TrustTraceResponse): StepCard[] {
  const metadataStatus = normalizeStatus(trace.metadata_job.status);
  const metadataCard: StepCard = !trace.metadata_job.present
    ? {
        key: "metadata",
        label: "metadata job",
        tone: "blocked",
        summary: "metadata_job.present=false",
        detail: "没有 metadata job readback；这里只标记缺口，不虚构后端报错。",
      }
      : isFailureLike(trace.metadata_job.status)
      ? {
          key: "metadata",
          label: "metadata job",
          tone: "blocked",
          summary: `metadata_job.status=${trace.metadata_job.status}`,
          detail: `platform_result=${trace.metadata_job.platform_result ?? "null"}`,
        }
        : metadataStatus === "queued"
          || metadataStatus === "running"
          || metadataStatus === "pending"
          || metadataStatus === "blocked"
          || metadataStatus === "not_ready"
          || metadataStatus === "partial"
          || metadataStatus === "degraded"
        ? {
            key: "metadata",
            label: "metadata job",
            tone: "degraded",
            summary: `metadata_job.status=${trace.metadata_job.status}`,
            detail: "metadata fetch 尚未到达 succeeded；当前只标记中间态。",
          }
          : isSuccessLike(trace.metadata_job.status)
            ? {
            key: "metadata",
            label: "metadata job",
            tone: "clear",
            summary: `metadata_job.status=${trace.metadata_job.status ?? "null"}`,
            detail: `platform_result=${trace.metadata_job.platform_result ?? "null"}`,
            }
            : {
                key: "metadata",
                label: "metadata job",
                tone: "degraded",
                summary: `metadata_job.status=${trace.metadata_job.status ?? "null"}`,
                detail: "status 为开放字符串，当前仅按保守 degraded 处理，不推断为 clear。",
              };

  const probeCard: StepCard = !trace.probe_evidence.present
    ? {
        key: "probe",
        label: "probe evidence",
        tone: "degraded",
        summary: "probe_evidence.present=false",
        detail: "缺少 probe evidence，只能标记为证据缺口。",
      }
    : isBlank(trace.probe_evidence.source_report_path) || isBlank(trace.probe_evidence.source_task_id)
      ? {
          key: "probe",
          label: "probe evidence",
          tone: "degraded",
          summary: "probe_evidence source linkage 不完整",
          detail: `source_task_id=${trace.probe_evidence.source_task_id ?? "null"} / source_report_path=${trace.probe_evidence.source_report_path ?? "null"}`,
        }
      : {
          key: "probe",
          label: "probe evidence",
          tone: "clear",
          summary: `probe_mode=${trace.probe_evidence.probe_mode}`,
          detail: `source_task_id=${trace.probe_evidence.source_task_id}`,
        };

  const receiptCard: StepCard = !trace.receipt_ledger.present
    ? {
        key: "receipts",
        label: "receipt ledger",
        tone: "blocked",
        summary: "receipt_ledger.present=false",
        detail: "receipt ledger 缺席，当前路径在收据层中断。",
      }
    : trace.receipt_ledger.artifact_count === 0
      ? {
          key: "receipts",
          label: "receipt ledger",
          tone: "blocked",
          summary: "receipt_ledger.artifact_count=0",
          detail: `artifact_kinds=${trace.receipt_ledger.artifact_kinds.length > 0 ? trace.receipt_ledger.artifact_kinds.join(", ") : "[]"}`,
        }
      : {
          key: "receipts",
          label: "receipt ledger",
          tone: "clear",
          summary: `artifact_count=${trace.receipt_ledger.artifact_count}`,
          detail: `redaction=${trace.receipt_ledger.redaction}`,
        };

  const auditCard: StepCard = isFailureLike(trace.audit.platform_result)
    ? {
        key: "audit",
        label: "audit evidence",
        tone: "blocked",
        summary: `audit.platform_result=${trace.audit.platform_result ?? "null"}`,
        detail: `evidence_file_path=${trace.audit.evidence_file_path ?? "null"} / artifact_count=${trace.audit.artifact_count}`,
      }
    : isBlank(trace.audit.evidence_file_path) || trace.audit.artifact_count === 0
    ? {
        key: "audit",
        label: "audit evidence",
        tone: "degraded",
        summary: `audit.evidence_file_path=${trace.audit.evidence_file_path ?? "null"}`,
        detail: `audit.artifact_count=${trace.audit.artifact_count}`,
      }
    : {
        key: "audit",
        label: "audit evidence",
        tone: "clear",
        summary: `audit.artifact_count=${trace.audit.artifact_count}`,
        detail: `platform_result=${trace.audit.platform_result ?? "null"}`,
      };

  return [
    trace.capture_state.capture_created
      ? {
          key: "capture",
          label: "capture",
          tone: "clear",
          summary: `capture_state.status=${trace.capture_state.status}`,
          detail: `capture_id=${trace.capture.capture_id}`,
        }
      : {
          key: "capture",
          label: "capture",
          tone: "blocked",
          summary: "capture_state.capture_created=false",
          detail: `capture_state.status=${trace.capture_state.status}`,
        },
    metadataCard,
    probeCard,
    receiptCard,
    auditCard,
    classifyAudio(trace),
  ];
}

export default function ErrorPathLane({ trace, routeStatus, routeErrorCode }: ErrorPathLaneProps) {
  const stepCards = routeStatus === "error" || !trace ? [] : buildStepCards(trace);
  const blockedCount = stepCards.filter((step) => step.tone === "blocked").length;
  const degradedCount = stepCards.filter((step) => step.tone === "degraded").length;
  const clearCount = stepCards.filter((step) => step.tone === "clear").length;

  return (
    <PanelCard title="W1B error-path lane" eyebrow="trust-trace" aside={<StateBadge tone="candidate" label="bounded readback" />}>
      <div className={styles.cardBody}>
        {routeStatus === "error" ? (
          <>
            <div className={styles.routeFailure} role="alert">
              <div className={styles.failureHeader}>
                <span className={`${styles.stepTone} ${styles.error}`}>route failure</span>
                <strong>GET /captures/&#123;id&#125;/trust-trace 返回错误</strong>
              </div>
              <p className={styles.failureDetail}>
                {routeErrorCode ? `routeErrorCode=${routeErrorCode}` : "routeErrorCode 未提供"}
              </p>
            </div>
            <p className={styles.muted}>错误态只回显 route failure truth，不根据旧 trace 反推业务错误路径。</p>
          </>
        ) : null}

        {routeStatus !== "error" && !trace ? (
          <>
            <div className={styles.emptyState}>
              <strong>暂无 error-path readback</strong>
              <p>没有 trace 时，只能保留空态，不能虚构受阻步骤。</p>
            </div>
            <p className={styles.muted}>先拿到 trust-trace readback，再按 DTO 字段标记 blocked / degraded path。</p>
          </>
        ) : null}

        {routeStatus !== "error" && trace ? (
          <>
            <div className={styles.summaryRow} aria-label="error-path summary">
              <span className={`${styles.stepTone} ${styles.blocked}`}>受阻 {blockedCount}</span>
              <span className={`${styles.stepTone} ${styles.degraded}`}>降级 {degradedCount}</span>
              <span className={`${styles.stepTone} ${styles.clear}`}>正常 {clearCount}</span>
            </div>

            <div className={styles.breadcrumb} aria-label="error-path breadcrumb">
              {stepCards.map((step) => (
                <div key={step.key} className={`${styles.crumb} ${styles[step.tone]}`}>
                  <span className={styles.crumbLabel}>{step.label}</span>
                </div>
              ))}
            </div>

            <div className={styles.stepGrid}>
              {stepCards.map((step) => (
                <article key={step.key} className={`${styles.stepCard} ${styles[step.tone]}`}>
                  <div className={styles.stepHeader}>
                    <strong>{step.label}</strong>
                    <span className={`${styles.stepTone} ${styles[step.tone]}`}>{step.tone}</span>
                  </div>
                  <p className={styles.stepSummary}>{step.summary}</p>
                  <p className={styles.stepDetail}>{step.detail}</p>
                </article>
              ))}
            </div>

            <p className={styles.muted}>当前视图只依据 readback DTO 标记缺口，不把缺字段包装成后端异常。</p>
          </>
        ) : null}
      </div>
    </PanelCard>
  );
}
