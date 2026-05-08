import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { W2CRuntimeValue } from "../../lib/w2c-runtime";
import CapturePlan from "./CapturePlan";

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
    bridgeVaultConfig: {
      status: "success",
      data: {
        vault_root_resolved: true,
        vault_root: "/tmp/scoutflow-vault",
        preview_enabled: true,
        write_enabled: false,
        frontmatter_mode: "raw_4_field",
        error: null,
      },
      error: null,
    },
    trustTrace: { status: "idle", data: null, error: null },
    vaultPreview: {
      status: "success",
      data: {
        capture_id: "cap_123",
        target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
        frontmatter: {
          title: "ScoutFlow BV1xK4y1f7yC",
          date: "2026-05-08",
          tags: "调研/ScoutFlow采集",
          status: "pending",
        },
        body_markdown: "# ScoutFlow BV1xK4y1f7yC",
        warnings: [],
      },
      error: null,
    },
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

describe("CapturePlan", () => {
  it("renders current runtime-backed io contract", () => {
    render(<CapturePlan />);

    expect(screen.getByText("https://www.bilibili.com/video/BV1xK4y1f7yC")).toBeTruthy();
    expect(screen.getAllByText("/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md").length).toBeGreaterThan(0);
    expect(screen.getByText("raw_4_field; title / date / tags / status")).toBeTruthy();
  });

  it("keeps the runtime gate explicit in execution log", () => {
    render(<CapturePlan />);

    expect(screen.getByText("runtime_gate")).toBeTruthy();
    expect(screen.getByText("future-gated; no runtime approval language")).toBeTruthy();
  });
});
