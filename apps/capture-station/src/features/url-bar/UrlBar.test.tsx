import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import UrlBar from "./UrlBar";

describe("UrlBar", () => {
  it("renders the empty state section", () => {
    render(<UrlBar />);

    expect(screen.getByText("状态: 空闲")).toBeTruthy();
    expect(screen.getAllByText("创建采集").length).toBeGreaterThan(0);
  });

  it("renders the validating state without implying success", () => {
    render(<UrlBar />);

    expect(screen.getByText("状态: 校验中")).toBeTruthy();
    expect(screen.getByText("解析中...")).toBeTruthy();
  });

  it("renders the history-open state with capture history", () => {
    render(<UrlBar />);

    expect(screen.getByText("状态: 历史下拉")).toBeTruthy();
    expect(screen.getByText("cap_20260506_8a3f2")).toBeTruthy();
    expect(screen.getByText("https://example.com/article/workflow")).toBeTruthy();
  });
});
