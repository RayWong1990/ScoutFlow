import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import TopicCardVault from "./TopicCardVault";

describe("TopicCardVault", () => {
  it("renders the default vault state", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("状态: 默认")).toBeTruthy();
    expect(screen.getByText("Topic Card Vault")).toBeTruthy();
  });

  it("renders the promote readiness state", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("状态: 晋升准备度")).toBeTruthy();
    expect(screen.getByText("晋升 DiloFlow 准备度")).toBeTruthy();
    expect(screen.getByRole("button", { name: /晋升 DiloFlow/i })).toBeTruthy();
  });

  it("keeps the three sync-badge states visible", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("已同步")).toBeTruthy();
    expect(screen.getByText("待同步")).toBeTruthy();
    expect(screen.getByText("外部已改")).toBeTruthy();
  });
});
