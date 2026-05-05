import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TopicCardVaultCandidate from "./TopicCardVaultCandidate";

describe("TopicCardVaultCandidate", () => {
  it("keeps the vault path in candidate-only, write-disabled posture", () => {
    render(<TopicCardVaultCandidate />);

    expect(screen.getByText("Topic Card Vault")).toBeTruthy();
    expect(screen.getByText("write_disabled")).toBeTruthy();
    expect(screen.getByText("counter-evidence")).toBeTruthy();
    expect(screen.getByText(/deferred_visual_evidence/i)).toBeTruthy();
  });
});
