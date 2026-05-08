import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { W2CRuntimeValue } from "../../lib/w2c-runtime";
import SignalHypothesis from "./SignalHypothesis";

const mockUseW2CRuntime = vi.fn();

vi.mock("../../lib/w2c-runtime", () => ({
  useW2CRuntime: () => mockUseW2CRuntime(),
}));

function createRuntimeValue(overrides: Partial<W2CRuntimeValue> = {}): W2CRuntimeValue {
  return {
    canonicalUrl: "https://www.bilibili.com/video/BV1xK4y1f7yC",
    setCanonicalUrl: vi.fn(),
    captureSourceUrl: "https://www.bilibili.com/video/BV1xK4y1f7yC",
    capture: {
      status: "success",
      data: {
        capture_id: "cap_123",
        platform: "bilibili",
        platform_item_id: "BV1xK4y1f7yC",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
        created_by_path: "quick_capture",
        status: "discovered",
        artifact_root_path: "data/artifacts/bilibili/cap_123",
        manifest_path: "data/artifacts/bilibili/cap_123/manifest.json",
      },
      error: null,
    },
    metadataFetch: { status: "success", data: { job_id: "job_123", capture_id: "cap_123", job_type: "metadata_fetch", status: "queued", dedupe_key: "dedupe" }, error: null },
    bridgeHealth: { status: "success", data: { bridge_available: true, spec_version: "0.1.0", write_enabled: false, blocked_by: ["write_disabled"] }, error: null },
    bridgeVaultConfig: { status: "success", data: { vault_root_resolved: true, vault_root: "/tmp/scoutflow-vault", preview_enabled: true, write_enabled: false, frontmatter_mode: "raw_4_field", error: null }, error: null },
    trustTrace: {
      status: "success",
      data: {
        label: "Status / Trust Trace / 采集状态",
        capture: {
          capture_id: "cap_123",
          platform: "bilibili",
          platform_item_id: "BV1xK4y1f7yC",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
        },
        capture_state: { capture_created: true, status: "discovered" },
        metadata_job: { present: true, job_id: "job_123", job_type: "metadata_fetch", status: "queued", platform_result: null },
        probe_evidence: { present: false, probe_mode: "not-run", source_task_id: null, source_report_path: null, platform_result: null },
        receipt_ledger: { present: true, artifact_count: 2, artifact_kinds: ["safe_metadata_evidence"], redaction: "applied" },
        media_audio: { status: "not_approved", audio_transcript: "blocked" },
        audit: { platform_result: null, evidence_file_path: null, artifact_count: 2, redaction_policy: null, safe_parsed_fields: { title: "ScoutFlow BV1xK4y1f7yC" } },
      },
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

beforeEach(() => {
  mockUseW2CRuntime.mockReturnValue(createRuntimeValue());
});

describe("SignalHypothesis", () => {
  it("shows runtime-backed signal detail", () => {
    render(<SignalHypothesis />);

    expect(screen.getByText("ScoutFlow BV1xK4y1f7yC")).toBeTruthy();
    expect(screen.getByText(/metadata_fetch job=job_123 status=queued/i)).toBeTruthy();
  });

  it("keeps future-gated comparison visible", () => {
    render(<SignalHypothesis />);

    expect(screen.getByText("评论 / ASR / 自动晋升")).toBeTruthy();
    expect(screen.getByText("future-gated")).toBeTruthy();
  });
});
