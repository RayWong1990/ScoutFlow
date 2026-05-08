import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import PromoteGate from "./PromoteGate";

describe("PromoteGate", () => {
  it("renders blocked gates distinctly from pending gates", () => {
    render(
      <PromoteGate
        title="晋升 DiloFlow 准备度"
        items={[
          { label: "visual truth cleared", status: "met" },
          { label: "true write still blocked", status: "blocked" },
          { label: "manual localhost review pending", status: "pending" },
        ]}
      />,
    );

    expect(screen.getByText("true write still blocked").closest("li")?.className).toMatch(/blocked/);
    expect(screen.getByText("manual localhost review pending").closest("li")?.className).toMatch(/pending/);
  });
});
