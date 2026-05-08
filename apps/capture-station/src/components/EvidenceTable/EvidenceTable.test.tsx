import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import EvidenceTable from "./EvidenceTable";

describe("EvidenceTable", () => {
  it("renders panel grammar header and row tones", () => {
    render(
      <EvidenceTable
        title="Trust Trace 证据"
        description="error-path first primitives"
        columns={[
          { key: "field", label: "字段" },
          { key: "value", label: "值", code: true },
        ]}
        rows={[
          { id: "preview", tone: "preview", cells: { field: "preview hash", value: "sha256:abc" } },
          { id: "blocked", tone: "blocked", cells: { field: "audio_transcript", value: "blocked" } },
        ]}
      />,
    );

    expect(screen.getByText("Trust Trace 证据")).toBeTruthy();
    expect(screen.getByText("audio_transcript").closest("tr")?.getAttribute("data-tone")).toBe("blocked");
  });
});
