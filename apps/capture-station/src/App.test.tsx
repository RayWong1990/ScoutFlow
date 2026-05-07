import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import App from "./App";

describe("App", () => {
  it("renders the PF-C4-01 shell and allows surface navigation", () => {
    render(<App />);

    expect(screen.getByText("Capture Station · 本地操作员工作站")).toBeTruthy();
    expect(screen.getByRole("button", { name: /08 Topic Card Vault/i })).toBeTruthy();

    fireEvent.click(screen.getByRole("button", { name: /10 Capture Plan/i }));

    expect(screen.getByText("采集计划信息架构状态集")).toBeTruthy();
  });
});
