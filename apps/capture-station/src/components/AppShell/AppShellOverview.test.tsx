import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import type { AsyncState, W2CRuntimeValue } from "../../lib/w2c-runtime";
import AppShellOverview from "./AppShellOverview";

const runtimeHolder = vi.hoisted(() => ({
  value: null as W2CRuntimeValue | null,
}));

vi.mock("../../lib/w2c-runtime", () => ({
  useW2CRuntime: () => runtimeHolder.value,
}));

function asyncState<T>(status: AsyncState<T>["status"], data: T | null = null): AsyncState<T> {
  return { status, data, error: null };
}

function buildRuntime(overrides: Partial<W2CRuntimeValue> = {}): W2CRuntimeValue {
  return {
    canonicalUrl: "https://www.bilibili.com/video/BV1xK4y1f7yC",
    setCanonicalUrl: vi.fn(),
    captureSourceUrl: "https://www.bilibili.com/video/BV1xK4y1f7yC",
    capture: asyncState("success", {
      capture_id: "cap_123",
      platform: "bilibili",
      platform_item_id: "BV1xK4y1f7yC",
      source_kind: "manual_url",
      capture_mode: "metadata_only",
      created_by_path: "quick_capture",
      status: "discovered",
      artifact_root_path: "data/artifacts/bilibili/cap_123",
      manifest_path: "data/artifacts/bilibili/cap_123/bundle/capture-manifest.json",
    }),
    metadataFetch: asyncState("success", {
      job_id: "job_123",
      capture_id: "cap_123",
      job_type: "metadata_fetch",
      status: "queued",
      dedupe_key: "bilibili:BV1xK4y1f7yC:metadata_fetch",
    }),
    bridgeHealth: asyncState("success", {
      bridge_available: true,
      spec_version: "0.1.0",
      write_enabled: false,
      blocked_by: ["write_disabled"],
    }),
    bridgeVaultConfig: asyncState("success", {
      vault_root_resolved: true,
      vault_root: "/tmp/scoutflow-vault",
      preview_enabled: true,
      write_enabled: false,
      frontmatter_mode: "raw_4_field",
      error: null,
    }),
    trustTrace: asyncState("success", {
      label: "Status / Trust Trace / 采集状态",
      capture: {
        capture_id: "cap_123",
        platform: "bilibili",
        platform_item_id: "BV1xK4y1f7yC",
        source_kind: "manual_url",
        capture_mode: "metadata_only",
        created_by_path: "quick_capture",
      },
      capture_state: {
        capture_created: true,
        status: "discovered",
      },
      metadata_job: {
        present: true,
        job_id: "job_123",
        job_type: "metadata_fetch",
        status: "queued",
        platform_result: null,
      },
      probe_evidence: {
        present: false,
        probe_mode: "not-run",
        source_task_id: null,
        source_report_path: null,
        platform_result: null,
      },
      receipt_ledger: {
        present: false,
        artifact_count: 0,
        artifact_kinds: [],
        redaction: "not_applicable",
      },
      media_audio: {
        status: "not_approved",
        audio_transcript: "blocked",
      },
      audit: {
        platform_result: null,
        evidence_file_path: null,
        artifact_count: 0,
        redaction_policy: null,
        safe_parsed_fields: {},
      },
    }),
    vaultPreview: asyncState("success", {
      capture_id: "cap_123",
      target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
      frontmatter: {
        title: "ScoutFlow BV1xK4y1f7yC",
        date: "2026-05-08",
        tags: "ScoutFlow",
        status: "preview_only",
      },
      body_markdown: "# ScoutFlow BV1xK4y1f7yC",
      warnings: [],
    }),
    vaultCommitDryRun: asyncState("idle"),
    currentCaptureId: "cap_123",
    createCapture: vi.fn().mockResolvedValue(undefined),
    refreshCaptureBoundData: vi.fn().mockResolvedValue(undefined),
    runVaultCommitDryRun: vi.fn().mockResolvedValue(undefined),
    clearCapture: vi.fn(),
    isRuntimeBlocked: true,
    isVaultWriteBlocked: true,
    ...overrides,
  };
}

describe("AppShellOverview", () => {
  it("summarizes live bridge, capture, and preview truth", () => {
    runtimeHolder.value = buildRuntime();

    render(<AppShellOverview embedded />);

    expect(screen.getByText("Bridge / Vault")).toBeTruthy();
    expect(screen.getByText("spec_version")).toBeTruthy();
    expect(screen.getAllByText("/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md").length).toBeGreaterThan(0);
    expect(screen.getAllByText("write_enabled=false").length).toBeGreaterThan(0);
  });
});
