import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import VaultPreviewPanel from "./VaultPreviewPanel";

const samplePreview = {
  capture_id: "cap_123",
  target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1ab411c7md.md",
  frontmatter: {
    title: "ScoutFlow BV1AB411c7mD",
    date: "2026-05-06",
    tags: "调研/ScoutFlow采集",
    status: "pending"
  },
  body_markdown: "# ScoutFlow BV1AB411c7mD\n\n- capture_id: `cap_123`\n- canonical_url: https://www.bilibili.com/video/BV1AB411c7mD",
  warnings: ["preview only"]
};

describe("VaultPreviewPanel", () => {
  const originalClipboard = navigator.clipboard;
  const originalCreateObjectUrl = URL.createObjectURL;
  const originalRevokeObjectUrl = URL.revokeObjectURL;

  beforeEach(() => {
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      value: {
        writeText: vi.fn().mockResolvedValue(undefined)
      }
    });
    URL.createObjectURL = vi.fn().mockReturnValue("blob:preview");
    URL.revokeObjectURL = vi.fn();
  });

  afterEach(() => {
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      value: originalClipboard
    });
    URL.createObjectURL = originalCreateObjectUrl;
    URL.revokeObjectURL = originalRevokeObjectUrl;
    vi.restoreAllMocks();
  });

  it("renders an idle state with copy and download disabled", () => {
    render(<VaultPreviewPanel state="idle" />);

    expect(screen.getByText("Create a metadata-only capture to load preview.")).toBeTruthy();
    expect((screen.getByRole("button", { name: "Copy markdown" }) as HTMLButtonElement).disabled).toBe(true);
    expect((screen.getByRole("button", { name: "Download .md" }) as HTMLButtonElement).disabled).toBe(true);
  });

  it("renders real preview data and enables copy/download actions", () => {
    render(<VaultPreviewPanel state="ready" preview={samplePreview} />);

    expect(screen.getByText("cap_123")).toBeTruthy();
    expect(screen.getByText("/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1ab411c7md.md")).toBeTruthy();
    expect(screen.getByText("preview only")).toBeTruthy();
    expect((screen.getByRole("button", { name: "Copy markdown" }) as HTMLButtonElement).disabled).toBe(false);
    expect((screen.getByRole("button", { name: "Download .md" }) as HTMLButtonElement).disabled).toBe(false);
  });

  it("copies the exact markdown payload and reports success", async () => {
    const writeText = vi.fn().mockResolvedValue(undefined);
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      value: { writeText }
    });

    render(<VaultPreviewPanel state="ready" preview={samplePreview} />);

    fireEvent.click(screen.getByRole("button", { name: "Copy markdown" }));

    await waitFor(() => expect(writeText).toHaveBeenCalledWith(samplePreview.body_markdown));
    await waitFor(() => expect(screen.getByText("Markdown copied.")).toBeTruthy());
  });

  it("keeps markdown visible when clipboard copy fails", async () => {
    const writeText = vi.fn().mockRejectedValue(new Error("clipboard unavailable"));
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      value: { writeText }
    });

    render(<VaultPreviewPanel state="ready" preview={samplePreview} />);

    fireEvent.click(screen.getByRole("button", { name: "Copy markdown" }));

    await waitFor(() => expect(screen.getByText("Copy failed.")).toBeTruthy());
    expect(screen.getByText((_, element) => element?.tagName === "PRE" && element.textContent === samplePreview.body_markdown)).toBeTruthy();
  });

  it("downloads the exact markdown payload with a sanitized filename", async () => {
    const originalBlob = globalThis.Blob;
    const blobPayloads: Array<{ parts: BlobPart[]; options?: BlobPropertyBag }> = [];
    // Capture constructor input because the jsdom Blob shim in this environment does not expose text()/arrayBuffer().
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    globalThis.Blob = class FakeBlob {
      constructor(parts: BlobPart[], options?: BlobPropertyBag) {
        blobPayloads.push({ parts, options });
      }
    } as any;
    try {
      const clickSpy = vi.spyOn(HTMLAnchorElement.prototype, "click").mockImplementation(() => {});
      const anchors: HTMLAnchorElement[] = [];
      const originalCreateElement = document.createElement.bind(document);
      const createElementSpy = vi.spyOn(document, "createElement").mockImplementation((tagName: string) => {
        const element = originalCreateElement(tagName) as HTMLElement;
        if (tagName === "a") {
          anchors.push(element as HTMLAnchorElement);
        }
        return element;
      });

      render(
        <VaultPreviewPanel
          state="ready"
          preview={{
            ...samplePreview,
            capture_id: "cap:/unsafe*id"
          }}
        />
      );

      fireEvent.click(screen.getByRole("button", { name: "Download .md" }));

      await waitFor(() => expect(URL.createObjectURL).toHaveBeenCalledTimes(1));
      expect(blobPayloads[0]?.parts).toEqual([samplePreview.body_markdown]);
      expect(blobPayloads[0]?.options?.type).toBe("text/markdown;charset=utf-8");
      expect(anchors[0]?.download).toBe("scoutflow-preview-cap--unsafe-id.md");
      expect(clickSpy).toHaveBeenCalledTimes(1);
      expect(createElementSpy).toHaveBeenCalledWith("a");
      expect(URL.revokeObjectURL).toHaveBeenCalledWith("blob:preview");
    } finally {
      globalThis.Blob = originalBlob;
    }
  });

  it("renders fail-loud blocked states without implying true write", () => {
    render(
      <VaultPreviewPanel
        state="error"
        error={{
          code: "write_disabled",
          message: "Bridge write path is not approved in the current phase."
        }}
      />
    );

    expect(screen.getByText("write_disabled")).toBeTruthy();
    expect(screen.getByText("Bridge write path is not approved in the current phase.")).toBeTruthy();
    expect(screen.queryByText("Commit executed")).toBeNull();
  });
});
