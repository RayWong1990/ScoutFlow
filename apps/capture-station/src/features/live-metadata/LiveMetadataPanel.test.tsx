import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import LiveMetadataPanel from "./LiveMetadataPanel";

describe("LiveMetadataPanel", () => {
  it("renders the fixture-only guardrails", () => {
    render(<LiveMetadataPanel />);

    expect(screen.getByText("Live Metadata")).toBeTruthy();
    expect(screen.getByText("fixture only")).toBeTruthy();
    expect(screen.getByText("audio_transcript", { exact: false })).toBeTruthy();
  });
});
