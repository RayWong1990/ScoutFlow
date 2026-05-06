import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TopicCardPreviewCandidate from "./TopicCardPreviewCandidate";
import { buildTopicCardPreviewCandidateData } from "./topicCardLite";

describe("TopicCardPreviewCandidate", () => {
  it("keeps the preview in manual-review-only posture", () => {
    render(<TopicCardPreviewCandidate />);

    expect(screen.getByText("ScoutFlow topic-card candidate")).toBeTruthy();
    expect(screen.getByText("manual-first")).toBeTruthy();
    expect(screen.getByText(/Counter-evidence stays visible/i)).toBeTruthy();
    expect(screen.getByText(/deferred_visual_evidence/i)).toBeTruthy();
  });

  it("maps real capture and preview truth into topic-card-lite fields", () => {
    const data = buildTopicCardPreviewCandidateData(
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

    expect(data.title).toBe("ScoutFlow BV16ooQBsEah");
    expect(data.exportPosture).toBe("handoff_candidate");
    expect(data.metrics[0]?.value).toBe("manual_url");
    expect(data.canonicalUrl).toContain("BV16ooQBsEah");
    expect(data.targetPath).toContain("cap_real_123");
  });
});
