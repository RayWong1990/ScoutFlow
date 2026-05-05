import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TopicCardPreviewCandidate from "./TopicCardPreviewCandidate";

describe("TopicCardPreviewCandidate", () => {
  it("keeps the preview in manual-review-only posture", () => {
    render(<TopicCardPreviewCandidate />);

    expect(screen.getByText("ScoutFlow topic-card candidate")).toBeTruthy();
    expect(screen.getByText("manual-first")).toBeTruthy();
    expect(screen.getByText(/Counter-evidence stays visible/i)).toBeTruthy();
    expect(screen.getByText(/deferred_visual_evidence/i)).toBeTruthy();
  });
});
