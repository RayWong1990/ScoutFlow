import type { TopicCardPreviewCandidateData } from "../topic-card-preview/topicCardLite";
import { buildPlaceholderTopicCardPreviewCandidateData } from "../topic-card-preview/topicCardLite";

export type TopicCardEvidenceRow = {
  label: string;
  stance: "support" | "counter" | "process";
  note: string;
};

export type TopicCardVaultCandidateData = {
  title: string;
  hypothesisSummary: string;
  exportPosture: "local_only" | "handoff_candidate";
  gate: "write_disabled";
  targetPath: string;
  markdownPreview: string;
  evidence: TopicCardEvidenceRow[];
};

export function buildTopicCardLiteMarkdownCandidate(topicCard: TopicCardPreviewCandidateData): string {
  return [
    `# ${topicCard.title}`,
    "",
    `- capture_id: ${topicCard.captureId}`,
    `- platform_item_id: ${topicCard.platformItemId}`,
    `- canonical_url: ${topicCard.canonicalUrl}`,
    `- export_posture: ${topicCard.exportPosture}`,
    `- frontmatter_status: ${topicCard.frontmatterStatus}`,
    "",
    "## Evidence",
    `- support: capture_mode and preview target are present`,
    `- process: target_path=${topicCard.targetPath}`,
    `- counter: human usefulness verdict is still pending`,
  ].join("\n");
}

export function buildTopicCardVaultCandidateData(topicCard: TopicCardPreviewCandidateData): TopicCardVaultCandidateData {
  return {
    title: "Topic Card Vault",
    hypothesisSummary: `将 ${topicCard.platformItemId} 的 preview 证据压成可审阅 markdown companion，但仍停在 write-disabled 候选层。`,
    exportPosture: topicCard.exportPosture,
    gate: "write_disabled",
    targetPath: topicCard.targetPath,
    markdownPreview: buildTopicCardLiteMarkdownCandidate(topicCard),
    evidence: [
      {
        label: "capture truth",
        stance: "support",
        note: `capture_id=${topicCard.captureId} and canonical_url are carried forward without inventing new source facts.`,
      },
      {
        label: "review process",
        stance: "process",
        note: "The markdown companion keeps the preview in a handoff_candidate posture and does not claim vault commit.",
      },
      {
        label: "counter-evidence",
        stance: "counter",
        note: "Human usefulness verdict and RAW intake are still downstream gates, so this note remains candidate-only.",
      },
    ],
  };
}

export function buildPlaceholderTopicCardVaultCandidateData(): TopicCardVaultCandidateData {
  return buildTopicCardVaultCandidateData(buildPlaceholderTopicCardPreviewCandidateData());
}
