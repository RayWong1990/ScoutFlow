import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import CaptureScopePanel from "./CaptureScopePanel";

describe("CaptureScopePanel", () => {
  it("surfaces blocked audio_transcript state", () => {
    render(<CaptureScopePanel />);

    expect(screen.getByText("Capture Scope")).toBeTruthy();
    expect(screen.getByText("audio_transcript")).toBeTruthy();
    expect(screen.getByText("Runtime remains blocked.")).toBeTruthy();
  });
});
