import { afterEach, describe, expect, it, vi } from "vitest";

import { CaptureStationApiError, buildApiUrl, createCaptureStationApi } from "./api-client";

afterEach(() => {
  vi.unstubAllGlobals();
});

describe("api-client", () => {
  it("normalizes the base URL and path join", () => {
    expect(buildApiUrl("http://127.0.0.1:8000/", "/bridge/health")).toBe("http://127.0.0.1:8000/bridge/health");
    expect(buildApiUrl("http://127.0.0.1:8000", "bridge/health")).toBe("http://127.0.0.1:8000/bridge/health");
  });

  it("posts a fixed manual_url metadata_only payload for createCapture", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      status: 201,
      json: async () => ({
        capture_id: "01JABCDEF0123456789ABCDEFG",
        platform: "bilibili",
        platform_item_id: "BV1AB411c7mD",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
        created_by_path: "quick_capture",
        status: "discovered",
        artifact_root_path: "data/artifacts/bilibili/01JABCDEF0123456789ABCDEFG",
        manifest_path: "data/artifacts/bilibili/01JABCDEF0123456789ABCDEFG/bundle/capture-manifest.json"
      })
    });

    vi.stubGlobal("fetch", fetchMock);

    const result = await api.createCapture("https://www.bilibili.com/video/BV1AB411c7mD");

    expect(fetchMock).toHaveBeenCalledWith("http://127.0.0.1:8000/captures/discover", {
      headers: { "Content-Type": "application/json" },
      method: "POST",
      body: JSON.stringify({
        platform: "bilibili",
        canonical_url: "https://www.bilibili.com/video/BV1AB411c7mD",
        source_kind: "manual_url",
        quick_capture_preset: "metadata_only"
      })
    });
    expect(result).toMatchObject({
      capture_id: "01JABCDEF0123456789ABCDEFG",
      canonical_url: "https://www.bilibili.com/video/BV1AB411c7mD"
    });
  });

  it("loads vault preview data for a capture id", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const previewPayload = {
      capture_id: "cap_123",
      target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123-bv1ab411c7md.md",
      frontmatter: {
        title: "ScoutFlow BV1AB411c7mD",
        date: "2026-05-06",
        tags: "调研/ScoutFlow采集",
        status: "pending"
      },
      body_markdown: "# ScoutFlow BV1AB411c7mD",
      warnings: []
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => previewPayload
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.getVaultPreview("cap_123")).resolves.toEqual(previewPayload);
    expect(fetchMock).toHaveBeenCalledWith("http://127.0.0.1:8000/captures/cap_123/vault-preview", {
      headers: { "Content-Type": "application/json" }
    });
  });

  it("raises a typed error for non-2xx responses", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 409,
      json: async () => ({ code: "write_disabled", message: "Bridge write path is not approved" })
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.postVaultCommitDryRun("cap_demo")).rejects.toBeInstanceOf(CaptureStationApiError);
  });

  it("preserves status, code, and payload for createCapture failures", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const payload = {
      code: "unsupported_platform",
      message: "canonical_url must be a bilibili URL."
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 422,
      json: async () => payload
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.createCapture("https://example.com/video/123")).rejects.toMatchObject({
      status: 422,
      code: "unsupported_platform",
      payload
    });
  });

  it("falls back to a default message when an error body is not json", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 500,
      json: async () => {
        throw new Error("invalid json");
      }
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.getBridgeHealth()).rejects.toMatchObject({
      status: 500,
      message: "Bridge request failed with status 500",
      payload: null
    });
  });
});
