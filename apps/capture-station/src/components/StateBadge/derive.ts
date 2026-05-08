import type { TrustTraceResponse } from "../../lib/api-client";
import { STATE_COPY_ZH, type CaptureSurfaceState } from "../../styles/state-tokens";

export type LegacyStateBadgeTone =
  | "idle"
  | "ready"
  | "candidate"
  | "stale"
  | "metadataLoaded"
  | "previewOnly"
  | "metadataOnly"
  | "locked"
  | "error"
  | "success";

export type StateBadgeTone = CaptureSurfaceState | LegacyStateBadgeTone;

const LEGACY_TONE_MAP: Record<LegacyStateBadgeTone, CaptureSurfaceState> = {
  idle: "empty",
  ready: "preview",
  candidate: "preview",
  stale: "partial",
  metadataLoaded: "partial",
  previewOnly: "preview",
  metadataOnly: "preview",
  locked: "disabled",
  error: "failed",
  success: "partial",
};

const BLOCKED_STATUSES = new Set(["blocked", "not_approved", "disabled", "write_disabled"]);
const LOADING_STATUSES = new Set(["queued", "running", "loading"]);
const FAILED_STATUSES = new Set(["failed", "error"]);
const PARTIAL_STATUSES = new Set(["metadata_fetched", "succeeded", "success", "complete"]);
const COMMITTED_STATUSES = new Set(["committed", "written"]);
const SKIPPED_STATUSES = new Set(["skipped", "not_applicable"]);
const PREVIEW_STATUSES = new Set(["created", "discovered", "metadata_only", "preview_only"]);

export function normalizeStateBadgeTone(tone: StateBadgeTone): CaptureSurfaceState {
  return tone in LEGACY_TONE_MAP ? LEGACY_TONE_MAP[tone as LegacyStateBadgeTone] : (tone as CaptureSurfaceState);
}

export function deriveStateFromStatus(status: string | null | undefined): CaptureSurfaceState {
  const normalized = status?.trim().toLowerCase();
  if (!normalized) {
    return "empty";
  }
  if (BLOCKED_STATUSES.has(normalized)) {
    return "blocked";
  }
  if (FAILED_STATUSES.has(normalized)) {
    return "failed";
  }
  if (LOADING_STATUSES.has(normalized)) {
    return "loading";
  }
  if (COMMITTED_STATUSES.has(normalized)) {
    return "committed";
  }
  if (PARTIAL_STATUSES.has(normalized)) {
    return "partial";
  }
  if (SKIPPED_STATUSES.has(normalized)) {
    return "skipped";
  }
  if (PREVIEW_STATUSES.has(normalized)) {
    return "preview";
  }
  return "preview";
}

export function deriveTrustTraceBadge(args: {
  trace: TrustTraceResponse | null | undefined;
  routeStatus: "idle" | "loading" | "error" | "success";
  currentCaptureId?: string | null;
}) {
  if (args.routeStatus === "loading") {
    return {
      tone: "loading" as const,
      label: "正在读取 trust-trace",
    };
  }

  if (args.routeStatus === "error") {
    return {
      tone: "failed" as const,
      label: "trust-trace 路由失败",
    };
  }

  if (!args.trace) {
    return {
      tone: args.currentCaptureId ? ("empty" as const) : ("empty" as const),
      label: args.currentCaptureId ? "等待 trust-trace" : STATE_COPY_ZH.empty,
    };
  }

  const captureState = deriveStateFromStatus(args.trace.capture_state.status);
  const metadataState = deriveStateFromStatus(args.trace.metadata_job.status);
  const platformState = deriveStateFromStatus(args.trace.metadata_job.platform_result ?? args.trace.audit.platform_result);

  if (!args.trace.capture_state.capture_created) {
    return {
      tone: "empty" as const,
      label: "capture 尚未创建",
    };
  }

  if (captureState === "blocked" || metadataState === "blocked" || platformState === "blocked") {
    return {
      tone: "blocked" as const,
      label: "业务态已阻止",
    };
  }

  if (captureState === "failed" || metadataState === "failed" || platformState === "failed") {
    return {
      tone: "failed" as const,
      label: "失败已记录",
    };
  }

  if (captureState === "committed") {
    return {
      tone: "committed" as const,
      label: STATE_COPY_ZH.committed,
    };
  }

  if (metadataState === "loading") {
    return {
      tone: "loading" as const,
      label: "metadata_fetch 处理中",
    };
  }

  if (
    args.trace.receipt_ledger.present ||
    args.trace.receipt_ledger.artifact_count > 0 ||
    Object.keys(args.trace.audit.safe_parsed_fields).length > 0 ||
    metadataState === "partial" ||
    platformState === "partial"
  ) {
    return {
      tone: "partial" as const,
      label: "证据部分回填",
    };
  }

  return {
    tone: captureState,
    label: captureState === "preview" ? "capture 已发现" : STATE_COPY_ZH[captureState],
  };
}
