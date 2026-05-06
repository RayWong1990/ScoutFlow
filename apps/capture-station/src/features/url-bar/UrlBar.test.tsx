import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

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

  it("submits a valid manual url exactly once and forwards the capture result", async () => {
    const createCapture = vi.fn().mockResolvedValue({
      capture_id: "cap_123",
      canonical_url: "https://www.bilibili.com/video/BV1AB411c7mD"
    });
    const onCaptureCreated = vi.fn();

    render(<UrlBar createCapture={createCapture} onCaptureCreated={onCaptureCreated} />);

    fireEvent.click(screen.getByText("Create capture"));

    await waitFor(() =>
      expect(createCapture).toHaveBeenCalledWith("https://www.bilibili.com/video/BV1AB411c7mD")
    );
    await waitFor(() =>
      expect(onCaptureCreated).toHaveBeenCalledWith({
        capture_id: "cap_123",
        canonical_url: "https://www.bilibili.com/video/BV1AB411c7mD"
      })
    );
  });

  it("renders an operator-visible error when createCapture fails", async () => {
    const createCapture = vi.fn().mockRejectedValue(new Error("canonical_url must be a bilibili URL."));

    render(<UrlBar createCapture={createCapture} />);

    fireEvent.click(screen.getByText("Create capture"));

    await waitFor(() =>
      expect(screen.getByText("canonical_url must be a bilibili URL.")).toBeTruthy()
    );
  });
});
