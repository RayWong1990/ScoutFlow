import { useEffect, useState } from "react";

import type { CaptureStationApiError, CreateCaptureResponse, BridgeVaultPreviewResponse } from "../lib/api-client";
import { createCaptureStationApi } from "../lib/api-client";
import CaptureScopePanel from "../features/capture-scope/CaptureScopePanel";
import LiveMetadataPanel from "../features/live-metadata/LiveMetadataPanel";
import TrustTraceGraph from "../features/trust-trace/TrustTraceGraph";
import UrlBar from "../features/url-bar/UrlBar";
import VaultCommitDryRunButton from "../features/vault-commit/VaultCommitDryRunButton";
import VaultPreviewPanel from "../features/vault-preview/VaultPreviewPanel";

type FourPanelShellProps = {
  createCapture?: (canonicalUrl: string) => Promise<CreateCaptureResponse>;
  loadPreview?: (captureId: string) => Promise<BridgeVaultPreviewResponse>;
};

type PreviewSurfaceError = {
  code?: string;
  message: string;
};

const previewApi = createCaptureStationApi("http://127.0.0.1:8000");

function normalizePreviewError(error: unknown): PreviewSurfaceError {
  if (typeof error === "object" && error !== null) {
    const apiError = error as CaptureStationApiError;
    if (typeof apiError.message === "string" && apiError.message.length > 0) {
      return {
        code: typeof apiError.code === "string" ? apiError.code : undefined,
        message: apiError.message
      };
    }
  }

  return {
    message: "Preview request failed."
  };
}

function PreviewSurface({
  state,
  preview,
  error
}: {
  state: "idle" | "loading" | "error" | "ready";
  preview: BridgeVaultPreviewResponse | null;
  error: PreviewSurfaceError | null;
}) {
  if (state === "ready" && preview) {
    return <VaultPreviewPanel preview={preview} />;
  }

  const statusLabel =
    state === "error" ? "preview blocked" : state === "loading" ? "loading" : "idle";
  const statusColor = state === "error" ? "#ff9db2" : state === "loading" ? "#ffcf7a" : "#a6b8cf";

  return (
    <section
      data-testid="panel-vault-preview"
      style={{
        minHeight: "220px",
        borderRadius: "8px",
        border: "1px solid #27415d",
        background: "#111f31",
        padding: "16px",
        display: "flex",
        flexDirection: "column",
        gap: "12px"
      }}
    >
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>vault-preview</p>
          <h2 style={{ margin: "8px 0 0", fontSize: "20px", lineHeight: 1.15 }}>Vault Preview</h2>
        </div>
        <span
          style={{
            borderRadius: "999px",
            border: "1px solid #27415d",
            background: "#16263c",
            color: statusColor,
            padding: "6px 10px",
            fontSize: "12px"
          }}
        >
          {statusLabel}
        </span>
      </div>

      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        This surface previews the raw 4-field note contract without claiming true vault write or runtime approval.
      </p>

      {state === "idle" ? (
        <div
          style={{
            borderRadius: "8px",
            border: "1px dashed #27415d",
            background: "#0b1624",
            color: "#a6b8cf",
            padding: "16px",
            fontSize: "14px",
            lineHeight: 1.45
          }}
        >
          Create a metadata-only capture to load preview.
        </div>
      ) : null}

      {state === "loading" ? (
        <div
          style={{
            borderRadius: "8px",
            border: "1px solid #5b4b24",
            background: "#1d1810",
            color: "#ffcf7a",
            padding: "16px",
            fontSize: "14px",
            lineHeight: 1.45
          }}
        >
          Loading preview draft from `/captures/{'{capture_id}'}/vault-preview`...
        </div>
      ) : null}

      {state === "error" && error ? (
        <div
          style={{
            borderRadius: "8px",
            border: "1px solid #6c2f3f",
            background: "#24131b",
            color: "#ff9db2",
            padding: "16px",
            display: "grid",
            gap: "6px"
          }}
        >
          <strong style={{ fontSize: "14px" }}>{error.code ?? "preview_error"}</strong>
          <span style={{ fontSize: "13px", lineHeight: 1.45 }}>{error.message}</span>
        </div>
      ) : null}
    </section>
  );
}

export default function FourPanelShell({
  createCapture = previewApi.createCapture,
  loadPreview = previewApi.getVaultPreview
}: FourPanelShellProps) {
  const [captureId, setCaptureId] = useState<string | null>(null);
  const [previewState, setPreviewState] = useState<"idle" | "loading" | "error" | "ready">("idle");
  const [preview, setPreview] = useState<BridgeVaultPreviewResponse | null>(null);
  const [previewError, setPreviewError] = useState<PreviewSurfaceError | null>(null);

  useEffect(() => {
    if (!captureId) {
      return;
    }

    let cancelled = false;
    setPreviewState("loading");
    setPreview(null);
    setPreviewError(null);

    loadPreview(captureId)
      .then((response) => {
        if (cancelled) {
          return;
        }
        setPreview(response);
        setPreviewState("ready");
      })
      .catch((error) => {
        if (cancelled) {
          return;
        }
        setPreview(null);
        setPreviewError(normalizePreviewError(error));
        setPreviewState("error");
      });

    return () => {
      cancelled = true;
    };
  }, [captureId, loadPreview]);

  function resetPreviewDraft() {
    setCaptureId(null);
    setPreview(null);
    setPreviewError(null);
    setPreviewState("idle");
  }

  return (
    <main
      style={{
        minHeight: "100vh",
        background: "#07111b",
        color: "#eef4ff",
        fontFamily: 'Inter, "PingFang SC", "Helvetica Neue", sans-serif',
        padding: "24px"
      }}
    >
      <section
        style={{
          maxWidth: "1360px",
          margin: "0 auto",
          border: "1px solid #1d3148",
          borderRadius: "8px",
          background: "#0d1826",
          boxShadow: "0 24px 48px rgba(0, 0, 0, 0.32)",
          padding: "24px",
          display: "grid",
          gap: "24px"
        }}
      >
        <header>
          <p style={{ margin: 0, color: "#50d4ff", fontSize: "12px", letterSpacing: 0 }}>ScoutFlow</p>
          <h1 style={{ margin: "8px 0 4px", fontSize: "28px", lineHeight: 1.1 }}>Capture Station</h1>
          <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
            Preview-only localhost workstation. Metadata-only capture stays visible without implying runtime unlock.
          </p>
        </header>

        <UrlBar
          createCapture={createCapture}
          onCaptureCreated={(capture) => {
            setCaptureId(capture.capture_id);
          }}
          onDraftChange={() => {
            if (captureId || previewState !== "idle") {
              resetPreviewDraft();
            }
          }}
        />

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "minmax(0, 2fr) minmax(320px, 1fr)",
            gap: "24px"
          }}
        >
          <PreviewSurface state={previewState} preview={preview} error={previewError} />
          <VaultCommitDryRunButton />
        </div>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "minmax(0, 1fr) minmax(0, 1fr) minmax(0, 1.4fr)",
            gap: "24px"
          }}
        >
          <LiveMetadataPanel />
          <CaptureScopePanel />
          <TrustTraceGraph />
        </div>
      </section>
    </main>
  );
}
