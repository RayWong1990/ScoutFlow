import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import UrlBar from "./UrlBar";

describe("UrlBar", () => {
  it("keeps the create action disabled until the value looks like a URL", () => {
    render(<UrlBar />);

    const input = screen.getByPlaceholderText("https://www.bilibili.com/video/BV...");
    const button = screen.getByText("Create capture") as HTMLButtonElement;

    fireEvent.change(input, { target: { value: "not-a-url" } });
    expect(button.disabled).toBe(true);

    fireEvent.change(input, { target: { value: "https://www.bilibili.com/video/BV1AB411c7mD" } });
    expect(button.disabled).toBe(false);
  });
});
