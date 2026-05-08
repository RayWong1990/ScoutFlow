import type { ReactNode } from "react";

import { render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import App from "./App";
import type { W2CRuntimeValue } from "./lib/w2c-runtime";
import { useW2CRuntime } from "./lib/w2c-runtime";

vi.mock("./lib/w2c-runtime", async () => {
  const actual = await vi.importActual<typeof import("./lib/w2c-runtime")>("./lib/w2c-runtime");
  return {
    ...actual,
    W2CRuntimeProvider: ({ children }: { children: ReactNode }) => <>{children}</>,
    useW2CRuntime: vi.fn(),
  };
});

const mockedUseW2CRuntime = vi.mocked(useW2CRuntime);

function buildRuntime(): W2CRuntimeValue {
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
        status: "queued",
        dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch",
      },
      error: null,
    },
    bridgeHealth: {
      status: "success",
      data: {
        bridge_available: true,
        spec_version: "0.1.0",
        write_enabled: false,
        blocked_by: ["write_disabled"],
      },
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
            duration: "12:34",
          },
        },
      },
      error: null,
    },
    vaultPreview: {
      status: "success",
      data: {
        capture_id: "cap_123",
        target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
        frontmatter: {
          title: "ScoutFlow W2C Demo",
          status: "preview_only",
        },
        body_markdown: "# ScoutFlow W2C Demo",
        warnings: [],
      },
      error: null,
    },
    vaultCommitDryRun: {
      status: "idle",
      data: null,
      error: null,
    },
    currentCaptureId: "cap_123",
    createCapture: vi.fn(),
    refreshCaptureBoundData: vi.fn(),
    runVaultCommitDryRun: vi.fn(),
    clearCapture: vi.fn(),
    isRuntimeBlocked: true,
    isVaultWriteBlocked: true,
  };
}

afterEach(() => {
  vi.clearAllMocks();
});

describe("App", () => {
  it("renders a single-screen workstation flow instead of the old gallery shell", () => {
    mockedUseW2CRuntime.mockReturnValue(buildRuntime());

    render(<App />);

    expect(screen.getByText("Capture Station 单屏操作流")).toBeTruthy();
    expect(screen.getByText("Top-fold truth summary")).toBeTruthy();
    expect(screen.getByText("Rewrite Output V1")).toBeTruthy();
    expect(screen.queryByRole("navigation", { name: /surface navigation/i })).toBeNull();
  });
});
