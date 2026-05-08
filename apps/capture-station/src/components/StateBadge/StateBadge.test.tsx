import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import StateBadge from "./StateBadge";
import { deriveTrustTraceTone, getDefaultStateLabel } from "./derive";

describe("StateBadge", () => {
  it("renders canonical nine-state tones through the new semantic mapping", () => {
    render(<StateBadge tone="blocked" label={getDefaultStateLabel("blocked")} />);

    const badge = screen.getByText(/已阻止/).closest("[data-state]");
    expect(badge?.getAttribute("data-state")).toBe("blocked");
  });

  it("derives trust-trace badge tones from business state rather than route success alone", () => {
    expect(
      deriveTrustTraceTone({
        routeStatus: "success",
        captureStateStatus: "metadata_fetched",
        metadataJobStatus: "succeeded",
      }),
    ).toBe("committed");

    expect(
      deriveTrustTraceTone({
        routeStatus: "success",
        captureStateStatus: "failed",
      }),
    ).toBe("failed");
  });
});
