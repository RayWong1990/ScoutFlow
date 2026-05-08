import type { ReactNode } from "react";

import { render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

import type { W2CRuntimeValue } from "../lib/w2c-runtime";
import { useW2CRuntime } from "../lib/w2c-runtime";
import AppShellOverview from "../components/AppShell/AppShellOverview";
import CapturePlan from "./capture-plan/CapturePlan";
import CaptureScope from "./capture-scope/CaptureScope";
import DensitySpec from "./_specs/DensitySpec";
import LiveMetadata from "./live-metadata/LiveMetadata";
import RewriteOutputPreview from "./rewrite-output/RewriteOutputPreview";
import SignalHypothesis from "./signal-hypothesis/SignalHypothesis";
import TopicCardLite from "./topic-card-preview/TopicCardLite";
import TopicCardVault from "./topic-card-vault/TopicCardVault";
import TrustTrace from "./trust-trace/TrustTrace";
import UrlBar from "./url-bar/UrlBar";
import VaultCommit from "./vault-commit/VaultCommit";
import VaultPreview from "./vault-preview/VaultPreview";
import TypeSpec from "./_specs/TypeSpec";
import { rewriteOutputFixtures } from "../fixtures/rewrite-output-v1";

vi.mock("../lib/w2c-runtime", async () => {
  const actual = await vi.importActual<typeof import("../lib/w2c-runtime")>("../lib/w2c-runtime");
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
            uploader: "RayWong1990",
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
          date: "2026-05-08",
          tags: "调研/ScoutFlow采集",
          status: "pending",
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

beforeEach(() => {
  mockedUseW2CRuntime.mockReturnValue(buildRuntime());
});

afterEach(() => {
  vi.clearAllMocks();
});

describe("surface smoke tests", () => {
  it("renders app shell overview", () => {
    render(<AppShellOverview />);
    expect(screen.getByText("应用总览")).toBeTruthy();
  });

  it("renders url bar surface", () => {
    render(<UrlBar />);
    expect(screen.getByText("URL 输入栏")).toBeTruthy();
  });

  it("renders live metadata surface", () => {
    render(<LiveMetadata />);
    expect(screen.getByText("实时元数据")).toBeTruthy();
  });

  it("renders capture scope surface", () => {
    render(<CaptureScope />);
    expect(screen.getByText("采集范围")).toBeTruthy();
  });

  it("renders trust trace surface", () => {
    render(<TrustTrace />);
    expect(screen.getByText("信任溯源状态集")).toBeTruthy();
  });

  it("renders vault preview surface", () => {
    render(<VaultPreview />);
    expect(screen.getByText("入库预览状态集")).toBeTruthy();
  });

  it("renders vault commit surface", () => {
    render(<VaultCommit />);
    expect(screen.getByText("入库提交状态集")).toBeTruthy();
  });

  it("renders topic card lite surface", () => {
    render(<TopicCardLite />);
    expect(screen.getByText("Topic Card Lite 状态集")).toBeTruthy();
  });

  it("renders topic card vault surface", () => {
    render(<TopicCardVault />);
    expect(screen.getByText("Topic Card Vault 状态集")).toBeTruthy();
  });

  it("renders signal hypothesis surface", () => {
    render(<SignalHypothesis />);
    expect(screen.getByText("信号 / 假设信息架构状态集")).toBeTruthy();
  });

  it("renders capture plan surface", () => {
    render(<CapturePlan />);
    expect(screen.getByText("采集计划信息架构状态集")).toBeTruthy();
  });

  it("renders density spec surface", () => {
    render(<DensitySpec />);
    expect(screen.getByText("密度规格 · V3 紧凑密度")).toBeTruthy();
  });

  it("renders type spec surface", () => {
    render(<TypeSpec />);
    expect(screen.getByText("字重规格 · V4 高字重")).toBeTruthy();
  });

  it("renders rewrite output surface", () => {
    render(
      <RewriteOutputPreview
        fixture={rewriteOutputFixtures["ok-with-transcript"].output}
        fixtureName={rewriteOutputFixtures["ok-with-transcript"].fileName}
      />,
    );
    expect(screen.getByText("Rewrite Output V1")).toBeTruthy();
  });
});
