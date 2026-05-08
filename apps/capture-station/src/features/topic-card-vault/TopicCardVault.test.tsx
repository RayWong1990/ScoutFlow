import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

import type { W2CRuntimeValue } from "../../lib/w2c-runtime";
import TopicCardVault from "./TopicCardVault";

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
    bridgeHealth: {
      status: "success",
      data: { bridge_available: true, spec_version: "0.1.0", write_enabled: false, blocked_by: ["write_disabled"] },
      error: null,
    },
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
        receipt_ledger: { present: false, artifact_count: 0, artifact_kinds: [], redaction: "not_applicable" },
        media_audio: { status: "not_approved", audio_transcript: "blocked" },
        audit: { platform_result: null, evidence_file_path: null, artifact_count: 0, redaction_policy: null, safe_parsed_fields: { title: "ScoutFlow BV1xK4y1f7yC" } },
      },
      error: null,
    },
    vaultPreview: {
      status: "success",
      data: {
        capture_id: "cap_123",
        target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
        frontmatter: { title: "ScoutFlow BV1xK4y1f7yC" },
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

describe("TopicCardVault", () => {
  it("renders the default vault state", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("状态: 默认")).toBeTruthy();
    expect(screen.getByText("Topic Card Vault")).toBeTruthy();
    expect(screen.getAllByText(/target_path=\/tmp\/scoutflow-vault\/00-Inbox\/scoutflow-cap_123\.md/i).length).toBeGreaterThan(0);
  });

  it("renders the promote readiness state", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("状态: 晋升准备度")).toBeTruthy();
    expect(screen.getByText("晋升 DiloFlow 准备度")).toBeTruthy();
    const button = screen.getByRole("button", { name: /晋升 DiloFlow/i }) as HTMLButtonElement;
    expect(button).toBeTruthy();
    expect(button.disabled).toBe(true);
  });

  it("keeps the three sync-badge states visible", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("已同步")).toBeTruthy();
    expect(screen.getAllByText("待同步").length).toBeGreaterThan(0);
    expect(screen.getByText("外部已改")).toBeTruthy();
  });

  it("keeps missing aggregate contract explicit", () => {
    render(<TopicCardVault />);

    expect(screen.getByText("多 capture 聚合待后续 contract")).toBeTruthy();
    expect(screen.getByText("当前 runtime 只暴露单 capture 上下文；跨 capture 聚合仍待独立 contract。")).toBeTruthy();
  });
});
