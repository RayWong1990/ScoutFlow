import type { BridgeVaultPreviewResponse, CreateCaptureResponse } from "../../lib/api-client";

export type PreviewMetric = {
  label: string;
  value: string;
  tone: "support" | "counter" | "process";
};

export type ReviewStep = {
  label: string;
  state: "ready" | "deferred" | "needs_review";
};

export type TopicCardPreviewCandidateData = {
  title: string;
  hypothesisSummary: string;
  reviewState: "mapped" | "reviewed";
  exportPosture: "local_only" | "handoff_candidate";
  metrics: PreviewMetric[];
  reviewSteps: ReviewStep[];
  counterNote: string;
  captureId: string;
  platformItemId: string;
  canonicalUrl: string;
  targetPath: string;
  frontmatterStatus: string;
};

export function buildPlaceholderTopicCardPreviewCandidateData(): TopicCardPreviewCandidateData {
  return {
    title: "ScoutFlow topic-card candidate",
    hypothesisSummary: "metadata proof is enough to frame a review card, but not enough to claim human visual clarity.",
    reviewState: "mapped",
    exportPosture: "local_only",
    metrics: [
      { label: "source_kind", value: "manual_url", tone: "process" },
      { label: "capture_mode", value: "metadata_only", tone: "support" },
      { label: "frontmatter_status", value: "pending", tone: "counter" },
    ],
    reviewSteps: [
      { label: "preview generated", state: "ready" },
      { label: "topic-card review", state: "needs_review" },
      { label: "human usefulness verdict", state: "deferred" },
    ],
    counterNote: "Counter-evidence stays visible: preview_only=true, write_enabled=false, and no RAW handoff claim exists yet.",
    captureId: "cap_placeholder",
    platformItemId: "BV_placeholder",
    canonicalUrl: "https://www.bilibili.com/video/BV_placeholder/",
    targetPath: "/tmp/scoutflow-vault/00-Inbox/topic-card-cap_placeholder.md",
    frontmatterStatus: "pending",
  };
}

export function buildTopicCardPreviewCandidateData(
  capture: Pick<CreateCaptureResponse, "capture_id" | "platform_item_id" | "canonical_url" | "source_kind" | "capture_mode">,
  preview: Pick<BridgeVaultPreviewResponse, "target_path" | "frontmatter" | "warnings">,
): TopicCardPreviewCandidateData {
  const frontmatterStatus = String(preview.frontmatter.status || "pending");
  const warningCount = Array.isArray(preview.warnings) ? preview.warnings.length : 0;

  return {
    title: String(preview.frontmatter.title || `ScoutFlow ${capture.platform_item_id}`),
    hypothesisSummary: `Preview-only candidate for ${capture.platform_item_id}; preserve source truth first, then ask whether a human would actually follow it.`,
    reviewState: warningCount > 0 ? "reviewed" : "mapped",
    exportPosture: "handoff_candidate",
    metrics: [
      { label: "source_kind", value: capture.source_kind, tone: "process" },
      { label: "capture_mode", value: capture.capture_mode, tone: "support" },
      { label: "frontmatter_status", value: frontmatterStatus, tone: frontmatterStatus === "pending" ? "counter" : "support" },
    ],
    reviewSteps: [
      { label: "preview generated", state: "ready" },
      { label: "topic-card review", state: "ready" },
      { label: "human usefulness verdict", state: "needs_review" },
    ],
    counterNote: `Counter-evidence stays visible: preview_only=true, write_enabled=false, canonical_url=${capture.canonical_url}.`,
    captureId: capture.capture_id,
    platformItemId: capture.platform_item_id,
    canonicalUrl: capture.canonical_url,
    targetPath: preview.target_path,
    frontmatterStatus,
  };
}
