import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import EvidenceTable from "./EvidenceTable";

describe("EvidenceTable", () => {
  it("preserves row-level preview and blocked tones for evidence-first scanning", () => {
    render(
      <EvidenceTable
        columns={[
          { key: "field", label: "字段" },
          { key: "value", label: "值" },
        ]}
        rows={[
          { id: "preview", tone: "preview", cells: { field: "preview_hash", value: "sha256:abc" } },
          { id: "blocked", tone: "blocked", cells: { field: "transcript", value: "blocked" } },
        ]}
      />,
    );

    expect(screen.getByText("sha256:abc").closest("tr")?.getAttribute("data-tone")).toBe("preview");
    expect(screen.getByText("blocked").closest("tr")?.getAttribute("data-tone")).toBe("blocked");
  });
});
