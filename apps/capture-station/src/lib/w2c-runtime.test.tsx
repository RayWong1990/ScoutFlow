import { act, render, screen, waitFor } from "@testing-library/react";
import { afterEach, describe, expect, it, vi } from "vitest";

import { W2CRuntimeProvider, useW2CRuntime } from "./w2c-runtime";

function RuntimeProbe() {
  const runtime = useW2CRuntime();

  return (
    <div>
      <div data-testid="capture-status">{runtime.capture.status}</div>
      <div data-testid="metadata-status">{runtime.metadataFetch.status}</div>
      <div data-testid="trust-trace-status">{runtime.trustTrace.status}</div>
      <div data-testid="vault-preview-status">{runtime.vaultPreview.status}</div>
      <div data-testid="capture-id">{runtime.currentCaptureId ?? "none"}</div>
      <button type="button" onClick={() => runtime.createCapture()}>
        create
      </button>
      <button type="button" onClick={() => runtime.clearCapture()}>
        clear
      </button>
    </div>
  );
}

afterEach(() => {
  vi.unstubAllGlobals();
});

describe("W2CRuntimeProvider", () => {
  it("loads bridge state on mount", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          vault_root_resolved: false,
          vault_root: null,
          preview_enabled: false,
          write_enabled: false,
          frontmatter_mode: "raw_4_field",
          error: { code: "vault_root_unset", message: "Vault root is not configured." },
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await waitFor(() => {
      expect(fetchMock).toHaveBeenCalledTimes(2);
    });
    expect(screen.getByTestId("capture-status").textContent).toBe("idle");
  });

  it("creates a capture, enqueues metadata fetch, and loads capture-bound data", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          vault_root_resolved: true,
          vault_root: "/tmp/scoutflow-vault",
          preview_enabled: true,
          write_enabled: false,
          frontmatter_mode: "raw_4_field",
          error: null,
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({
          capture_id: "cap_123",
          platform: "bilibili",
          platform_item_id: "BV1AB411c7mD",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
          status: "discovered",
          artifact_root_path: "data/artifacts/bilibili/cap_123",
          manifest_path: "data/artifacts/bilibili/cap_123/bundle/capture-manifest.json",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          job_id: "job_123",
          capture_id: "cap_123",
          job_type: "metadata_fetch",
          status: "queued",
          dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
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
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          capture_id: "cap_123",
          target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_123.md",
          frontmatter: {
            title: "ScoutFlow BV1AB411c7mD",
            date: "2026-05-06",
            tags: "调研/ScoutFlow采集",
            status: "pending",
          },
          body_markdown: "# ScoutFlow BV1AB411c7mD",
          warnings: [],
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await act(async () => {
      screen.getByRole("button", { name: "create" }).click();
    });

    await waitFor(() => {
      expect(screen.getByTestId("capture-id").textContent).toBe("cap_123");
      expect(screen.getByTestId("metadata-status").textContent).toBe("success");
      expect(screen.getByTestId("trust-trace-status").textContent).toBe("success");
      expect(screen.getByTestId("vault-preview-status").textContent).toBe("success");
    });
  });

  it("clears stale capture context while a new discover request is in flight", async () => {
    let resolveCreateCapture: ((value: { ok: boolean; status: number; json: () => Promise<unknown> }) => void) | null = null;
    const createCapturePromise = new Promise<{ ok: boolean; status: number; json: () => Promise<unknown> }>((resolve) => {
      resolveCreateCapture = resolve;
    });

    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          vault_root_resolved: true,
          vault_root: "/tmp/scoutflow-vault",
          preview_enabled: true,
          write_enabled: false,
          frontmatter_mode: "raw_4_field",
          error: null,
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({
          capture_id: "cap_old",
          platform: "bilibili",
          platform_item_id: "BV1AB411c7mD",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
          status: "discovered",
          artifact_root_path: "data/artifacts/bilibili/cap_old",
          manifest_path: "data/artifacts/bilibili/cap_old/bundle/capture-manifest.json",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          job_id: "job_old",
          capture_id: "cap_old",
          job_type: "metadata_fetch",
          status: "queued",
          dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          label: "Status / Trust Trace / 采集状态",
          capture: {
            capture_id: "cap_old",
            platform: "bilibili",
            platform_item_id: "BV1AB411c7mD",
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
            job_id: "job_old",
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
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          capture_id: "cap_old",
          target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_old.md",
          frontmatter: {
            title: "ScoutFlow BV1AB411c7mD",
            date: "2026-05-06",
            tags: "调研/ScoutFlow采集",
            status: "pending",
          },
          body_markdown: "# ScoutFlow BV1AB411c7mD",
          warnings: [],
        }),
      })
      .mockImplementationOnce(() => createCapturePromise)
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          job_id: "job_new",
          capture_id: "cap_new",
          job_type: "metadata_fetch",
          status: "queued",
          dedupe_key: "bilibili:BV1NEW:metadata_fetch",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          label: "Status / Trust Trace / 采集状态",
          capture: {
            capture_id: "cap_new",
            platform: "bilibili",
            platform_item_id: "BV1NEW",
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
            job_id: "job_new",
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
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          capture_id: "cap_new",
          target_path: "/tmp/scoutflow-vault/00-Inbox/scoutflow-cap_new.md",
          frontmatter: {
            title: "ScoutFlow BV1NEW",
            date: "2026-05-08",
            tags: "调研/ScoutFlow采集",
            status: "pending",
          },
          body_markdown: "# ScoutFlow BV1NEW",
          warnings: [],
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await act(async () => {
      screen.getByRole("button", { name: "create" }).click();
    });

    await waitFor(() => {
      expect(screen.getByTestId("capture-id").textContent).toBe("cap_old");
    });

    await act(async () => {
      screen.getByRole("button", { name: "create" }).click();
    });

    expect(screen.getByTestId("capture-status").textContent).toBe("loading");
    expect(screen.getByTestId("capture-id").textContent).toBe("none");
    expect(screen.getByTestId("trust-trace-status").textContent).toBe("idle");
    expect(screen.getByTestId("vault-preview-status").textContent).toBe("idle");

    await act(async () => {
      resolveCreateCapture?.({
        ok: true,
        status: 201,
        json: async () => ({
          capture_id: "cap_new",
          platform: "bilibili",
          platform_item_id: "BV1NEW",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
          status: "discovered",
          artifact_root_path: "data/artifacts/bilibili/cap_new",
          manifest_path: "data/artifacts/bilibili/cap_new/bundle/capture-manifest.json",
        }),
      });
    });

    await waitFor(() => {
      expect(screen.getByTestId("capture-id").textContent).toBe("cap_new");
      expect(screen.getByTestId("metadata-status").textContent).toBe("success");
      expect(screen.getByTestId("trust-trace-status").textContent).toBe("success");
      expect(screen.getByTestId("vault-preview-status").textContent).toBe("success");
    });
  });

  it("preserves trust-trace success when vault preview fails independently", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          vault_root_resolved: true,
          vault_root: "/tmp/scoutflow-vault",
          preview_enabled: true,
          write_enabled: false,
          frontmatter_mode: "raw_4_field",
          error: null,
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 201,
        json: async () => ({
          capture_id: "cap_123",
          platform: "bilibili",
          platform_item_id: "BV1AB411c7mD",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
          status: "discovered",
          artifact_root_path: "data/artifacts/bilibili/cap_123",
          manifest_path: "data/artifacts/bilibili/cap_123/bundle/capture-manifest.json",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          job_id: "job_123",
          capture_id: "cap_123",
          job_type: "metadata_fetch",
          status: "queued",
          dedupe_key: "bilibili:BV1AB411c7mD:metadata_fetch",
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
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
      })
      .mockResolvedValueOnce({
        ok: false,
        status: 503,
        json: async () => ({
          code: "capture_state_blocked",
          message: "Vault preview route unavailable",
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await act(async () => {
      screen.getByRole("button", { name: "create" }).click();
    });

    await waitFor(() => {
      expect(screen.getByTestId("trust-trace-status").textContent).toBe("success");
      expect(screen.getByTestId("vault-preview-status").textContent).toBe("error");
    });
  });

  it("preserves bridge health success when bridge config fails independently", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: false,
        status: 503,
        json: async () => ({
          code: "vault_root_unset",
          message: "Vault root is not configured.",
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await waitFor(() => {
      expect(fetchMock).toHaveBeenCalledTimes(2);
      expect(screen.getByTestId("capture-status").textContent).toBe("idle");
    });
  });

  it("clears capture-bound state explicitly", async () => {
    const fetchMock = vi
      .fn()
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          bridge_available: true,
          spec_version: "0.1.0",
          write_enabled: false,
          blocked_by: ["write_disabled"],
        }),
      })
      .mockResolvedValueOnce({
        ok: true,
        status: 200,
        json: async () => ({
          vault_root_resolved: false,
          vault_root: null,
          preview_enabled: false,
          write_enabled: false,
          frontmatter_mode: "raw_4_field",
          error: { code: "vault_root_unset", message: "Vault root is not configured." },
        }),
      });

    vi.stubGlobal("fetch", fetchMock);

    render(
      <W2CRuntimeProvider>
        <RuntimeProbe />
      </W2CRuntimeProvider>,
    );

    await act(async () => {
      screen.getByRole("button", { name: "clear" }).click();
    });

    expect(screen.getByTestId("capture-id").textContent).toBe("none");
    expect(screen.getByTestId("metadata-status").textContent).toBe("idle");
    expect(screen.getByTestId("trust-trace-status").textContent).toBe("idle");
    expect(screen.getByTestId("vault-preview-status").textContent).toBe("idle");
  });
});
