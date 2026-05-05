import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TrustTraceGraph from "./TrustTraceGraph";

describe("TrustTraceGraph", () => {
  it("shows the blocked media audio lane", () => {
    render(<TrustTraceGraph />);

    expect(screen.getByText("Trust Trace")).toBeTruthy();
    expect(screen.getByText("Media Audio")).toBeTruthy();
    expect(screen.getByText("audio_transcript remains blocked and stays outside the current runtime lane.")).toBeTruthy();
  });
});
