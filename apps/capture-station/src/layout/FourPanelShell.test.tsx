import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import FourPanelShell from "./FourPanelShell";

describe("FourPanelShell", () => {
  it("renders the four panel headings", () => {
    render(<FourPanelShell />);

    expect(screen.getByText("Manual URL")).toBeTruthy();
    expect(screen.getByText("Live Metadata")).toBeTruthy();
    expect(screen.getByText("Capture Scope")).toBeTruthy();
    expect(screen.getByText("Trust Trace")).toBeTruthy();
  });
});
