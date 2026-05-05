import { describe, expect, it, vi } from "vitest";

import { CaptureStationApiError, buildApiUrl, createCaptureStationApi } from "./api-client";

describe("api-client", () => {
  it("normalizes the base URL and path join", () => {
    expect(buildApiUrl("http://127.0.0.1:8000/", "/bridge/health")).toBe("http://127.0.0.1:8000/bridge/health");
    expect(buildApiUrl("http://127.0.0.1:8000", "bridge/health")).toBe("http://127.0.0.1:8000/bridge/health");
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
});
