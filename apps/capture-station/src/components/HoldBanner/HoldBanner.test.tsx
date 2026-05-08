import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import HoldBanner from "./HoldBanner";

describe("HoldBanner", () => {
  it("shows hold reason and unlock path without hover affordances", () => {
    render(
      <HoldBanner
        title="True write 保持关闭"
        holdId="HOLD-TRUE-WRITE"
        reason="write_enabled=False 仍是硬真相。"
        unlockPath="等待 Lane C readiness 和显式 user gate。"
      />,
    );

    expect(screen.getByText("write_enabled=False 仍是硬真相。")).toBeTruthy();
    expect(screen.getByText("等待 Lane C readiness 和显式 user gate。")).toBeTruthy();
    expect(screen.getByText("HOLD-TRUE-WRITE")).toBeTruthy();
  });
});
