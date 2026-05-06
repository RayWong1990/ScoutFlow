import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TopicCardVaultCandidate from "./TopicCardVaultCandidate";
import { buildTopicCardLiteMarkdownCandidate, buildTopicCardVaultCandidateData } from "./topicCardVaultCandidateData";
import { buildTopicCardPreviewCandidateData } from "../topic-card-preview/topicCardLite";

describe("TopicCardVaultCandidate", () => {
  it("keeps the vault path in candidate-only, write-disabled posture", () => {
    render(<TopicCardVaultCandidate />);

    expect(screen.getByText("Topic Card Vault")).toBeTruthy();
    expect(screen.getByText("write_disabled")).toBeTruthy();
    expect(screen.getByText("counter-evidence")).toBeTruthy();
    expect(screen.getByText(/deferred_visual_evidence/i)).toBeTruthy();
  });

  it("renders markdown companion from real topic-card-lite input", () => {
    const previewData = buildTopicCardPreviewCandidateData(
      {
        capture_id: "cap_real_123",
        platform_item_id: "BV16ooQBsEah",
        canonical_url: "https://www.bilibili.com/video/BV16ooQBsEah/",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
      },
      {
        target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_real_123-bv16ooqbseah.md",
        frontmatter: {
          title: "ScoutFlow BV16ooQBsEah",
          date: "2026-05-06",
          tags: "调研/ScoutFlow采集",
          status: "pending",
        },
        warnings: [],
      },
    );
    const vaultData = buildTopicCardVaultCandidateData(previewData);
    const markdown = buildTopicCardLiteMarkdownCandidate(previewData);

    expect(vaultData.exportPosture).toBe("handoff_candidate");
    expect(vaultData.targetPath).toContain("cap_real_123");
    expect(markdown).toContain("capture_id: cap_real_123");
    expect(markdown).toContain("canonical_url: https://www.bilibili.com/video/BV16ooQBsEah/");
  });
});
