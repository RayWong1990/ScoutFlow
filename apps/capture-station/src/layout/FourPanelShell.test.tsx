import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import FourPanelShell from "./FourPanelShell";

describe("FourPanelShell", () => {
  it("renders the workstation panels including preview surfaces", () => {
    render(<FourPanelShell />);

    expect(screen.getByText("Manual URL")).toBeTruthy();
    expect(screen.getByText("Vault Preview")).toBeTruthy();
    expect(screen.getByText("Vault Commit Dry Run")).toBeTruthy();
    expect(screen.getByText("Live Metadata")).toBeTruthy();
    expect(screen.getByText("Capture Scope")).toBeTruthy();
    expect(screen.getByText("Trust Trace")).toBeTruthy();
  });

  it("bridges capture success into preview loading and clears stale preview on url edits", async () => {
    const createCapture = vi.fn().mockResolvedValue({
      capture_id: "cap_123",
      canonical_url: "https://www.bilibili.com/video/BV1AB411c7mD"
    });
    const loadPreview = vi.fn().mockResolvedValue({
      capture_id: "cap_123",
      target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1ab411c7md.md",
      frontmatter: {
        title: "ScoutFlow BV1AB411c7mD",
        date: "2026-05-06",
        tags: "调研/ScoutFlow采集",
        status: "pending"
      },
      body_markdown: "# ScoutFlow BV1AB411c7mD\n\n- capture_id: `cap_123`\n- canonical_url: https://www.bilibili.com/video/BV1AB411c7mD",
      warnings: []
    });

    render(<FourPanelShell createCapture={createCapture} loadPreview={loadPreview} />);

    fireEvent.click(screen.getByText("Create capture"));

    await waitFor(() => expect(loadPreview).toHaveBeenCalledWith("cap_123"));
    await waitFor(() => expect(screen.getByText("cap_123")).toBeTruthy());

    fireEvent.change(screen.getByPlaceholderText("https://www.bilibili.com/video/BV..."), {
      target: { value: "https://www.bilibili.com/video/BV1Qx411c7mE" }
    });

    await waitFor(() =>
      expect(screen.getByText("Create a metadata-only capture to load preview.")).toBeTruthy()
    );
  });
});
