import { useEffect, useState } from "react";

import type { CaptureStationApiError, CreateCaptureResponse, BridgeVaultPreviewResponse } from "../lib/api-client";
import { createCaptureStationApi } from "../lib/api-client";
import CaptureScopePanel from "../features/capture-scope/CaptureScopePanel";
import LiveMetadataPanel from "../features/live-metadata/LiveMetadataPanel";
import TrustTraceGraph from "../features/trust-trace/TrustTraceGraph";
import UrlBar from "../features/url-bar/UrlBar";
import VaultCommitDryRunButton from "../features/vault-commit/VaultCommitDryRunButton";
import VaultPreviewPanel, { type VaultPreviewPanelError } from "../features/vault-preview/VaultPreviewPanel";

type FourPanelShellProps = {
  createCapture?: (canonicalUrl: string) => Promise<CreateCaptureResponse>;
  loadPreview?: (captureId: string) => Promise<BridgeVaultPreviewResponse>;
};

const previewApi = createCaptureStationApi("http://127.0.0.1:8000");

function normalizePreviewError(error: unknown): VaultPreviewPanelError {
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

export default function FourPanelShell({
  createCapture = previewApi.createCapture,
  loadPreview = previewApi.getVaultPreview
}: FourPanelShellProps) {
  const [captureId, setCaptureId] = useState<string | null>(null);
  const [previewState, setPreviewState] = useState<"idle" | "loading" | "error" | "ready">("idle");
  const [preview, setPreview] = useState<BridgeVaultPreviewResponse | null>(null);
  const [previewError, setPreviewError] = useState<VaultPreviewPanelError | null>(null);

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
          <VaultPreviewPanel state={previewState} preview={preview} error={previewError} />
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
