import { STATE_COPY_ZH, type CaptureSurfaceState } from "../../styles/state-tokens";
import type { StateBadgeTone } from "./StateBadge";

export type TrustTraceToneInput = {
  routeStatus: "idle" | "loading" | "success" | "error";
  captureStateStatus?: string | null;
  metadataJobStatus?: string | null;
  platformResult?: string | null;
};

const STATE_BADGE_ALIASES: Record<StateBadgeTone, CaptureSurfaceState> = {
  idle: "empty",
  loading: "loading",
  ready: "preview",
  candidate: "partial",
  blocked: "blocked",
  stale: "skipped",
  metadataLoaded: "committed",
  previewOnly: "preview",
  metadataOnly: "preview",
  locked: "disabled",
  error: "failed",
  success: "committed",
  empty: "empty",
  disabled: "disabled",
  preview: "preview",
  committed: "committed",
  failed: "failed",
  partial: "partial",
  skipped: "skipped",
};

const CAPTURE_STATE_TO_TONE: Record<string, CaptureSurfaceState> = {
  created: "preview",
  queued: "loading",
  running: "loading",
  metadata_fetched: "committed",
  failed: "failed",
  blocked: "blocked",
  skipped: "skipped",
  partial: "partial",
};

const JOB_STATE_TO_TONE: Record<string, CaptureSurfaceState> = {
  succeeded: "committed",
  success: "committed",
  queued: "loading",
  running: "loading",
  failed: "failed",
  blocked: "blocked",
};

const PLATFORM_RESULT_TO_TONE: Record<string, CaptureSurfaceState> = {
  metadata_fetched: "committed",
  ok: "committed",
  failed: "failed",
  blocked: "blocked",
  not_approved: "disabled",
};

export function resolveStateBadgeTone(tone: StateBadgeTone): CaptureSurfaceState {
  return STATE_BADGE_ALIASES[tone];
}

export function getDefaultStateLabel(state: CaptureSurfaceState): string {
  return STATE_COPY_ZH[state];
}

export function deriveTrustTraceTone(input: TrustTraceToneInput): CaptureSurfaceState {
  if (input.routeStatus === "error") {
    return "failed";
  }

  if (input.routeStatus === "loading") {
    return "loading";
  }

  if (input.routeStatus === "idle") {
    return "empty";
  }

  if (input.captureStateStatus && CAPTURE_STATE_TO_TONE[input.captureStateStatus]) {
    return CAPTURE_STATE_TO_TONE[input.captureStateStatus];
  }

  if (input.metadataJobStatus && JOB_STATE_TO_TONE[input.metadataJobStatus]) {
    return JOB_STATE_TO_TONE[input.metadataJobStatus];
  }

  if (input.platformResult && PLATFORM_RESULT_TO_TONE[input.platformResult]) {
    return PLATFORM_RESULT_TO_TONE[input.platformResult];
  }

  return "preview";
}

