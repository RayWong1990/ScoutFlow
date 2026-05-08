import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import type { AsyncState, W2CRuntimeValue } from "../../lib/w2c-runtime";
import { useW2CRuntime } from "../../lib/w2c-runtime";
import VaultCommit from "./VaultCommit";

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

describe("VaultCommit", () => {
  it("keeps true write disabled while allowing manual dry-run probes", () => {
    const runVaultCommitDryRun = vi.fn();
    mockedUseW2CRuntime.mockReturnValue(
      makeRuntime({
        runVaultCommitDryRun,
      }),
    );

    render(<VaultCommit />);

    fireEvent.click(screen.getByRole("button", { name: /run dry-run check/i }));

    expect(runVaultCommitDryRun).toHaveBeenCalledTimes(1);
    expect(screen.getByRole("button", { name: /commit to vault/i })).toHaveProperty("disabled", true);
    expect(screen.getByText(/write_enabled=false 仍是硬门/i)).toBeTruthy();
  });

  it("renders dry-run results as preview-only truth, not a successful commit", () => {
    mockedUseW2CRuntime.mockReturnValue(
      makeRuntime({
        vaultCommitDryRun: state({
          status: "success",
          data: {
            capture_id: "cap_123",
            committed: false,
            dry_run: true,
            write_enabled: false,
            target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
            error: {
              code: "write_disabled",
              message: "Bridge write path is not approved in the current phase",
            },
          },
        }),
      }),
    );

    render(<VaultCommit />);

    expect(screen.getByText(/dry-run-only/i)).toBeTruthy();
    expect(screen.getByText(/committed=false/i)).toBeTruthy();
    expect(screen.getByText("/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md")).toBeTruthy();
    expect(screen.queryByText(/已写入 vault/i)).toBeNull();
  });

  it("shows route errors as blocked copy", () => {
    mockedUseW2CRuntime.mockReturnValue(
      makeRuntime({
        vaultCommitDryRun: state({
          status: "error",
          error: {
            name: "CaptureStationApiError",
            status: 409,
            code: "vault_root_unset",
            message: "Vault root is not configured.",
          } as never,
        }),
      }),
    );

    render(<VaultCommit />);

    expect(screen.getByText(/Dry-run blocked/i)).toBeTruthy();
    expect(screen.getAllByText(/vault_root_unset/i).length).toBeGreaterThan(0);
    expect(screen.getByText(/不是 commit 成功/i)).toBeTruthy();
  });
});
