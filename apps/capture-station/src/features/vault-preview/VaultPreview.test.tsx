import { act, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { AsyncState, W2CRuntimeValue } from "../../lib/w2c-runtime";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import VaultPreview from "./VaultPreview";

vi.mock("../../lib/w2c-runtime", () => ({
  useW2CRuntime: vi.fn(),
}));

function state<T>(value: Partial<AsyncState<T>>): AsyncState<T> {
  return {
    status: "idle",
    data: null,
    error: null,
    ...value,
  };
}

function makeRuntime(overrides: Partial<W2CRuntimeValue> = {}): W2CRuntimeValue {
  const captureSourceUrl = overrides.captureSourceUrl ?? "https://www.bilibili.com/video/BV1AB411c7mD";
  const baseRuntime: W2CRuntimeValue = {
    canonicalUrl: "https://www.bilibili.com/video/BV1AB411c7mD",
    setCanonicalUrl: vi.fn(),
    captureSourceUrl,
    capture: state({ status: "idle" }),
    metadataFetch: state({ status: "idle" }),
    bridgeHealth: state({
      status: "success",
      data: {
        bridge_available: true,
        spec_version: "0.1.0",
        write_enabled: false,
        blocked_by: ["write_disabled"],
      },
    }),
    bridgeVaultConfig: state({
      status: "success",
      data: {
        vault_root_resolved: true,
        vault_root: "/tmp/scoutflow-vault",
        preview_enabled: true,
        write_enabled: false,
        frontmatter_mode: "raw_4_field",
        error: null,
      },
    }),
    trustTrace: state({ status: "idle" }),
    vaultPreview: state({ status: "idle" }),
    vaultCommitDryRun: state({ status: "idle" }),
    currentCaptureId: "cap_123",
    createCapture: vi.fn(),
    refreshCaptureBoundData: vi.fn(),
    runVaultCommitDryRun: vi.fn(),
    clearCapture: vi.fn(),
    isRuntimeBlocked: true,
    isVaultWriteBlocked: true,
  };

  return {
    ...baseRuntime,
    ...overrides,
    captureSourceUrl,
  };
}

const mockedUseW2CRuntime = vi.mocked(useW2CRuntime);

afterEach(() => {
  vi.clearAllMocks();
});

describe("VaultPreview", () => {
  it("shows config failure as blocked copy instead of fake preview success", () => {
    mockedUseW2CRuntime.mockReturnValue(
      makeRuntime({
        currentCaptureId: "cap_456",
        bridgeVaultConfig: state({
          status: "success",
          data: {
            vault_root_resolved: false,
            vault_root: null,
            preview_enabled: false,
            write_enabled: false,
            frontmatter_mode: "raw_4_field",
            error: {
              code: "vault_root_unset",
              message: "Vault root is not configured.",
            },
          },
        }),
        vaultPreview: state({ status: "idle" }),
      }),
    );

    render(<VaultPreview />);

    expect(screen.getAllByText(/vault_root_unset/i).length).toBeGreaterThan(0);
    expect(screen.getByText(/当前配置阻断 preview/i)).toBeTruthy();
    expect(screen.getByText(/write_enabled=false/i)).toBeTruthy();
  });

  it("renders real preview payload and lets the user refresh or copy preview-only markdown", async () => {
    const refreshCaptureBoundData = vi.fn();
    const writeText = vi.fn().mockResolvedValue(undefined);
    mockedUseW2CRuntime.mockReturnValue(
      makeRuntime({
        refreshCaptureBoundData,
        vaultPreview: state({
          status: "success",
          data: {
            capture_id: "cap_123",
            target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
            frontmatter: {
              title: "ScoutFlow BV1AB411c7mD",
              status: "pending",
            },
            body_markdown: "---\ntitle: ScoutFlow BV1AB411c7mD\n---\nbody",
            warnings: [],
          },
        }),
      }),
    );
    Object.defineProperty(navigator, "clipboard", {
      configurable: true,
      value: {
        writeText,
      },
    });

    render(<VaultPreview />);

    await act(async () => {
      fireEvent.click(screen.getByRole("button", { name: /copy markdown/i }));
    });
    fireEvent.click(screen.getByRole("button", { name: /refresh preview/i }));

    expect(writeText).toHaveBeenCalledWith("---\ntitle: ScoutFlow BV1AB411c7mD\n---\nbody");
    expect(refreshCaptureBoundData).toHaveBeenCalledTimes(1);
    expect(screen.getByText("/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md")).toBeTruthy();
    expect(screen.getByText("ScoutFlow BV1AB411c7mD")).toBeTruthy();
    expect(screen.getByText(/Markdown copied from preview response only/i)).toBeTruthy();
  });
});
