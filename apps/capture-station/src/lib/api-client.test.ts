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
      capture_id: "01JABCDEF0123456789ABCDEFG"
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

  it("enqueues metadata fetch for a capture id without implying readback success", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const enqueuePayload = {
      job_id: "job_123",
      capture_id: "cap_123",
      job_type: "metadata_fetch",
      status: "queued",
      dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch"
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => enqueuePayload
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.postMetadataFetchJob("cap_123")).resolves.toEqual(enqueuePayload);
    expect(fetchMock).toHaveBeenCalledWith("http://127.0.0.1:8000/captures/cap_123/metadata-fetch/jobs", {
      headers: { "Content-Type": "application/json" },
      method: "POST"
    });
  });

  it("loads layered trust trace for a capture id without flattening dto names", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const trustTracePayload = {
      label: "Status / Trust Trace / 采集状态",
      capture: {
        capture_id: "cap_123",
        platform: "bilibili",
        platform_item_id: "BV1AB411c7mD",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
        created_by_path: "quick_capture"
      },
      capture_state: {
        capture_created: true,
        status: "discovered"
      },
      metadata_job: {
        present: true,
        job_id: "job_123",
        job_type: "metadata_fetch",
        status: "queued",
        platform_result: null
      },
      probe_evidence: {
        present: false,
        probe_mode: "not-run",
        source_task_id: null,
        source_report_path: null,
        platform_result: null
      },
      receipt_ledger: {
        present: false,
        artifact_count: 0,
        artifact_kinds: [],
        redaction: "not_applicable"
      },
      media_audio: {
        status: "not_approved",
        audio_transcript: "blocked"
      },
      audit: {
        platform_result: null,
        evidence_file_path: null,
        artifact_count: 0,
        redaction_policy: null,
        safe_parsed_fields: {}
      }
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => trustTracePayload
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.getTrustTrace("cap_123")).resolves.toEqual(trustTracePayload);
    expect(fetchMock).toHaveBeenCalledWith("http://127.0.0.1:8000/captures/cap_123/trust-trace", {
      headers: { "Content-Type": "application/json" }
    });
  });

  it("raises a typed error for non-2xx responses", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 409,
      json: async () => ({ code: "write_disabled", message: "Bridge write path is not approved", write_enabled: false })
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

  it("preserves typed errors for trust trace load failures", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const payload = {
      code: "capture_not_found",
      message: "Capture cap_missing was not found."
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: false,
      status: 404,
      json: async () => payload
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.getTrustTrace("cap_missing")).rejects.toMatchObject({
      status: 404,
      code: "capture_not_found",
      payload
    });
  });

  it("keeps write_enabled=false on vault commit dry-run responses", async () => {
    const api = createCaptureStationApi("http://127.0.0.1:8000");
    const payload = {
      capture_id: "cap_123",
      committed: false,
      dry_run: true,
      write_enabled: false as const,
      target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
      error: null,
    };
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => payload,
    });

    vi.stubGlobal("fetch", fetchMock);

    await expect(api.postVaultCommitDryRun("cap_123")).resolves.toEqual(payload);
  });
});
