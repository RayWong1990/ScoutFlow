import { render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { CaptureStationApiError, type TrustTraceResponse } from "../../lib/api-client";
import type { W2CRuntimeValue } from "../../lib/w2c-runtime";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import TrustTrace from "./TrustTrace";

vi.mock("../../lib/w2c-runtime", async () => {
  const actual = await vi.importActual<typeof import("../../lib/w2c-runtime")>("../../lib/w2c-runtime");
  return {
    ...actual,
    useW2CRuntime: vi.fn(),
  };
});

const mockedUseW2CRuntime = vi.mocked(useW2CRuntime);

function buildTraceResponse(): TrustTraceResponse {
  return {
    label: "Status / Trust Trace / 采集状态",
    capture: {
      capture_id: "cap_123",
      platform: "bilibili",
      platform_item_id: "BV1AB411c7mD",
      source_kind: "manual_url",
      capture_mode: "metadata_only",
      created_by_path: "quick_capture",
    },
    capture_state: {
      capture_created: true,
      status: "metadata_fetched",
    },
    metadata_job: {
      present: true,
      job_id: "job_123",
      job_type: "metadata_fetch",
      status: "succeeded",
      platform_result: "metadata_fetched",
    },
    probe_evidence: {
      present: true,
      probe_mode: "auth_present",
      source_task_id: "T-P1A-013",
      source_report_path: "docs/research/probe.md",
      platform_result: "auth_present",
    },
    receipt_ledger: {
      present: true,
      artifact_count: 2,
      artifact_kinds: ["capture_manifest", "metadata_snapshot"],
      redaction: "safe_fields_only",
    },
    media_audio: {
      status: "not_approved",
      audio_transcript: "blocked",
    },
    audit: {
      platform_result: "metadata_fetched",
      evidence_file_path: "data/artifacts/bilibili/cap_123/evidence.json",
      artifact_count: 2,
      redaction_policy: "safe_fields_only",
      safe_parsed_fields: {
        title: "ScoutFlow W2C Demo",
        duration_seconds: 123,
        uploader: "RayWong1990",
      },
    },
  };
}

function buildRuntime(overrides?: Partial<W2CRuntimeValue>): W2CRuntimeValue {
  return {
    canonicalUrl: "https://www.bilibili.com/video/BV1AB411c7mD",
    setCanonicalUrl: vi.fn(),
    captureSourceUrl: "https://www.bilibili.com/video/BV1AB411c7mD",
    capture: {
      status: "success",
      data: {
        capture_id: "cap_123",
        platform: "bilibili",
        platform_item_id: "BV1AB411c7mD",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
        created_by_path: "quick_capture",
        status: "discovered",
        artifact_root_path: "data/artifacts/bilibili/cap_123",
        manifest_path: "data/artifacts/bilibili/cap_123/bundle/capture-manifest.json",
      },
      error: null,
    },
    metadataFetch: {
      status: "success",
      data: {
        job_id: "job_123",
        capture_id: "cap_123",
        job_type: "metadata_fetch",
        status: "succeeded",
        dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch",
      },
      error: null,
    },
    bridgeHealth: { status: "idle", data: null, error: null },
    bridgeVaultConfig: { status: "idle", data: null, error: null },
    trustTrace: {
      status: "success",
      data: buildTraceResponse(),
      error: null,
    },
    vaultPreview: { status: "idle", data: null, error: null },
    vaultCommitDryRun: { status: "idle", data: null, error: null },
    currentCaptureId: "cap_123",
    createCapture: vi.fn(),
    refreshCaptureBoundData: vi.fn(),
    runVaultCommitDryRun: vi.fn(),
    clearCapture: vi.fn(),
    isRuntimeBlocked: true,
    isVaultWriteBlocked: true,
    ...overrides,
  };
}

afterEach(() => {
  vi.clearAllMocks();
});

describe("TrustTrace", () => {
  it("renders layered trust-trace readback without flattening metadata, receipt, media_audio, and audit truth", () => {
    mockedUseW2CRuntime.mockReturnValue(buildRuntime());

    render(<TrustTrace />);

    expect(screen.getByText("Status / Trust Trace / 采集状态")).toBeTruthy();
    expect(screen.getByText("capture / capture_state")).toBeTruthy();
    expect(screen.getAllByText("metadata_job").length).toBeGreaterThan(0);
    expect(screen.getAllByText("receipt_ledger").length).toBeGreaterThan(0);
    expect(screen.getAllByText("media_audio").length).toBeGreaterThan(0);
    expect(screen.getAllByText("audit").length).toBeGreaterThan(0);
    expect(screen.getByText("metadata_snapshot")).toBeTruthy();
    expect(screen.getByText("blocked")).toBeTruthy();
    expect(screen.getByText("W1B graph lane")).toBeTruthy();
  });

  it("shows an honest empty state before a capture exists", () => {
    mockedUseW2CRuntime.mockReturnValue(
      buildRuntime({
        currentCaptureId: null,
        capture: { status: "idle", data: null, error: null },
        metadataFetch: { status: "idle", data: null, error: null },
        trustTrace: { status: "idle", data: null, error: null },
      }),
    );

    render(<TrustTrace />);

    expect(screen.getByText("创建 metadata-only capture 后再查看 Trust Trace readback。")).toBeTruthy();
    expect(screen.getByText("graph / timeline / error-path 仍保留给 W1B")).toBeTruthy();
  });

  it("surfaces route failure truth instead of fake trace data", () => {
    mockedUseW2CRuntime.mockReturnValue(
      buildRuntime({
        trustTrace: {
          status: "error",
          data: null,
          error: new CaptureStationApiError("Trust trace route unavailable", {
            status: 503,
            code: "trust_trace_not_ready",
          }),
        },
      }),
    );

    render(<TrustTrace />);

    expect(screen.getAllByText("Trust trace route unavailable").length).toBeGreaterThan(0);
    expect(screen.getByText("GET /captures/{id}/trust-trace 返回错误")).toBeTruthy();
    expect(screen.getByText("trust_trace_not_ready")).toBeTruthy();
    expect(screen.getByText("不生成假图谱，不把 503 包装成 success。")).toBeTruthy();
  });

  it("shows only a bounded transcript preview in the media audio panel", () => {
    const longTranscript = "private transcript segment ".repeat(10);
    mockedUseW2CRuntime.mockReturnValue(
      buildRuntime({
        trustTrace: {
          status: "success",
          data: {
            ...buildTraceResponse(),
            media_audio: {
              status: "ok",
              audio_transcript: longTranscript,
            },
          },
          error: null,
        },
      }),
    );

    render(<TrustTrace />);

    expect(screen.getByText("audio_transcript_preview")).toBeTruthy();
    expect(screen.getAllByText(/\[truncated\]/).length).toBeGreaterThan(0);
    expect(screen.queryByText(longTranscript)).toBeNull();
  });
});
