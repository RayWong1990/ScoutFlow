import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import RewriteOutputPreview from "./RewriteOutputPreview";
import { rewriteOutputFixtures } from "../../fixtures/rewrite-output-v1";

describe("RewriteOutputPreview", () => {
  it("shows a truthful blocked state when transcript handoff is incomplete", () => {
    render(
      <RewriteOutputPreview
        fixture={rewriteOutputFixtures["blocked-no-transcript"].output}
        fixtureName={rewriteOutputFixtures["blocked-no-transcript"].fileName}
      />,
    );

    expect(screen.getAllByText("RewriteOutputV1 blocked: TranscriptHandoffV1 incomplete").length).toBeGreaterThan(0);
    expect(screen.getAllByText("transcript_hash").length).toBeGreaterThan(0);
    expect(screen.getAllByText("transcript_backed_details").length).toBeGreaterThan(0);
  });

  it("renders all six obsidian_capture_note_v1 sections on the happy path", () => {
    render(
      <RewriteOutputPreview
        fixture={rewriteOutputFixtures["ok-with-transcript"].output}
        fixtureName={rewriteOutputFixtures["ok-with-transcript"].fileName}
      />,
    );

    expect(screen.getByText("1. Title")).toBeTruthy();
    expect(screen.getByText("2. Source summary")).toBeTruthy();
    expect(screen.getByText("3. Key points")).toBeTruthy();
    expect(screen.getByText("4. Transcript-backed details")).toBeTruthy();
    expect(screen.getByText("5. Trust / evidence notes")).toBeTruthy();
    expect(screen.getByText("6. Follow-up questions or open uncertainties")).toBeTruthy();
  });

  it("keeps partial sections visible without faking completeness", () => {
    render(
      <RewriteOutputPreview
        fixture={rewriteOutputFixtures["partial-rewrite"].output}
        fixtureName={rewriteOutputFixtures["partial-rewrite"].fileName}
      />,
    );

    expect(screen.getByText("partial rewrite")).toBeTruthy();
    expect(screen.getAllByText("section incomplete").length).toBeGreaterThan(0);
  });
});
