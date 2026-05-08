import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import PromoteGate from "./PromoteGate";

describe("PromoteGate", () => {
  it("renders blocked items distinctly from pending ones", () => {
    render(
      <PromoteGate
        title="晋升准备度"
        items={[
          { label: "证据已链接", status: "met" },
          { label: "真实写入仍 blocked", status: "blocked" },
          { label: "等待回填", status: "pending" },
        ]}
      />,
    );

    expect(screen.getByText("真实写入仍 blocked").closest("li")?.getAttribute("data-status")).toBe("blocked");
    expect(screen.getByText("等待回填").closest("li")?.getAttribute("data-status")).toBe("pending");
  });
});
