import { useMemo, useState } from "react";

import type { BridgeVaultPreviewResponse } from "../../lib/api-client";

export type VaultPreviewPanelError = {
  code?: string;
  message: string;
};

type VaultPreviewPanelProps = {
  state?: "idle" | "loading" | "error" | "ready";
  preview?: BridgeVaultPreviewResponse | null;
  error?: VaultPreviewPanelError | null;
};

function sanitizeDownloadFilename(captureId: string): string {
  return `scoutflow-preview-${captureId.replace(/[^A-Za-z0-9_-]/g, "-")}.md`;
}

export default function VaultPreviewPanel({
  state = "idle",
  preview = null,
  error = null
}: VaultPreviewPanelProps) {
  const [copyState, setCopyState] = useState<"idle" | "success" | "error">("idle");
  const [downloadMessage, setDownloadMessage] = useState<string | null>(null);

  const hasPreview = state === "ready" && preview !== null;
  const statusLabel =
    state === "ready" ? "preview loaded" : state === "error" ? "preview blocked" : state === "loading" ? "loading" : "idle";
  const statusColor =
    state === "ready" ? "#50d4ff" : state === "error" ? "#ff9db2" : state === "loading" ? "#ffcf7a" : "#a6b8cf";
  const downloadFilename = useMemo(() => (hasPreview && preview ? sanitizeDownloadFilename(preview.capture_id) : null), [
    hasPreview,
    preview
  ]);

  async function handleCopy() {
    if (!hasPreview || !preview) {
      return;
    }

    try {
      await navigator.clipboard.writeText(preview.body_markdown);
      setCopyState("success");
    } catch {
      setCopyState("error");
    }
  }

  function handleDownload() {
    if (!hasPreview || !preview || !downloadFilename) {
      return;
    }

    const blob = new Blob([preview.body_markdown], { type: "text/markdown;charset=utf-8" });
    const blobUrl = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = blobUrl;
    anchor.download = downloadFilename;
    anchor.click();
    URL.revokeObjectURL(blobUrl);
    setDownloadMessage(`Downloaded ${downloadFilename}.`);
  }

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
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: "12px" }}>
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

      <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
        <button
          type="button"
          disabled={!hasPreview}
          onClick={handleCopy}
          style={{
            borderRadius: "10px",
            border: "1px solid #50d4ff",
            background: hasPreview ? "#50d4ff" : "#27415d",
            color: hasPreview ? "#07111b" : "#6d8099",
            padding: "10px 14px",
            fontSize: "13px",
            fontWeight: 600,
            cursor: hasPreview ? "pointer" : "not-allowed"
          }}
        >
          Copy markdown
        </button>
        <button
          type="button"
          disabled={!hasPreview}
          onClick={handleDownload}
          style={{
            borderRadius: "10px",
            border: "1px solid #27415d",
            background: hasPreview ? "#16263c" : "#0f1824",
            color: hasPreview ? "#eef4ff" : "#6d8099",
            padding: "10px 14px",
            fontSize: "13px",
            fontWeight: 600,
            cursor: hasPreview ? "pointer" : "not-allowed"
          }}
        >
          Download .md
        </button>
      </div>

      {copyState === "success" ? (
        <p style={{ margin: 0, color: "#7adf9b", fontSize: "12px" }}>Markdown copied.</p>
      ) : null}
      {copyState === "error" ? (
        <p style={{ margin: 0, color: "#ff9db2", fontSize: "12px" }}>Copy failed.</p>
      ) : null}
      {downloadMessage ? <p style={{ margin: 0, color: "#7adf9b", fontSize: "12px" }}>{downloadMessage}</p> : null}

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

      {hasPreview && preview ? (
        <>
          <div
            style={{
              display: "grid",
              gridTemplateColumns: "minmax(0, 120px) minmax(0, 1fr)",
              gap: "8px 12px"
            }}
          >
            <span style={{ color: "#6d8099", fontSize: "12px" }}>capture_id</span>
            <span style={{ color: "#eef4ff", fontSize: "14px" }}>{preview.capture_id}</span>
            <span style={{ color: "#6d8099", fontSize: "12px" }}>target_path</span>
            <span style={{ color: "#eef4ff", fontSize: "14px", wordBreak: "break-all" }}>{preview.target_path}</span>
            <span style={{ color: "#6d8099", fontSize: "12px" }}>frontmatter</span>
            <span style={{ color: "#eef4ff", fontSize: "14px" }}>
              {preview.frontmatter.date} / {preview.frontmatter.tags} / {preview.frontmatter.status}
            </span>
          </div>

          <pre
            style={{
              margin: 0,
              borderRadius: "8px",
              border: "1px solid #27415d",
              background: "#0b1624",
              color: "#d8e3f2",
              padding: "12px",
              fontSize: "12px",
              lineHeight: 1.5,
              whiteSpace: "pre-wrap"
            }}
          >
            {preview.body_markdown}
          </pre>

          {preview.warnings.length > 0 ? (
            <ul style={{ margin: 0, paddingLeft: "18px", color: "#ffcf7a", fontSize: "12px" }}>
              {preview.warnings.map((warning) => (
                <li key={warning}>{warning}</li>
              ))}
            </ul>
          ) : null}
        </>
      ) : null}
    </section>
  );
}
