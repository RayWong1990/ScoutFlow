import { useMemo, useState } from "react";

import { type CreateCaptureResponse, createCaptureStationApi } from "../../lib/api-client";

const sampleSuggestions = [
  "https://www.bilibili.com/video/BV1AB411c7mD",
  "https://www.bilibili.com/video/BV1Qx411c7mE"
];

type UrlBarProps = {
  createCapture?: (canonicalUrl: string) => Promise<CreateCaptureResponse>;
  onCaptureCreated?: (capture: CreateCaptureResponse) => void;
  onDraftChange?: (canonicalUrl: string) => void;
};

const defaultCreateCapture = createCaptureStationApi("http://127.0.0.1:8000").createCapture;

export default function UrlBar({ createCapture = defaultCreateCapture, onCaptureCreated, onDraftChange }: UrlBarProps) {
  const [value, setValue] = useState(sampleSuggestions[0]);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const trimmed = value.trim();
  const isManualUrlReady = useMemo(() => /^https?:\/\//.test(trimmed), [trimmed]);

  async function handleSubmit() {
    if (!isManualUrlReady || isSubmitting) {
      return;
    }

    setIsSubmitting(true);
    setErrorMessage(null);

    try {
      const capture = await createCapture(trimmed);
      onCaptureCreated?.(capture);
    } catch (error) {
      const message = error instanceof Error ? error.message : "Create capture failed.";
      setErrorMessage(message);
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <section
      data-testid="panel-url-bar"
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
      <p style={{ margin: 0, color: "#6d8099", fontSize: "12px" }}>url-bar</p>
      <h2 style={{ margin: 0, fontSize: "20px", lineHeight: 1.15 }}>Manual URL</h2>
      <p style={{ margin: 0, color: "#a6b8cf", fontSize: "14px", lineHeight: 1.45 }}>
        Only `manual_url` can create a capture. recommendation / keyword / RAW gap stay blocked.
      </p>

      <label style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
        <span style={{ color: "#a6b8cf", fontSize: "12px" }}>Canonical URL</span>
        <input
          value={value}
          onChange={(event) => {
            const nextValue = event.target.value;
            setValue(nextValue);
            setErrorMessage(null);
            onDraftChange?.(nextValue);
          }}
          placeholder="https://www.bilibili.com/video/BV..."
          style={{
            width: "100%",
            borderRadius: "10px",
            border: "1px solid #27415d",
            background: "#0b1624",
            color: "#eef4ff",
            padding: "12px 14px",
            fontSize: "14px"
          }}
        />
      </label>

      <div style={{ display: "flex", gap: "8px", flexWrap: "wrap" }}>
        {sampleSuggestions.map((suggestion) => (
          <button
            key={suggestion}
            type="button"
            onClick={() => setValue(suggestion)}
            style={{
              borderRadius: "999px",
              border: "1px solid #27415d",
              background: "#16263c",
              color: "#a6b8cf",
              padding: "6px 10px",
              fontSize: "12px",
              cursor: "pointer"
            }}
          >
            Fill sample
          </button>
        ))}
      </div>

      {errorMessage ? (
        <p
          role="alert"
          style={{
            margin: 0,
            borderRadius: "8px",
            border: "1px solid #6c2f3f",
            background: "#24131b",
            color: "#ff9db2",
            padding: "10px 12px",
            fontSize: "13px",
            lineHeight: 1.45
          }}
        >
          {errorMessage}
        </p>
      ) : null}

      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: "auto" }}>
        <span style={{ color: isManualUrlReady ? "#7adf9b" : "#ff7b7b", fontSize: "12px" }}>
          {isSubmitting ? "submitting capture..." : isManualUrlReady ? "manual_url ready" : "manual_url required"}
        </span>
        <button
          type="button"
          disabled={!isManualUrlReady || isSubmitting}
          onClick={handleSubmit}
          style={{
            borderRadius: "10px",
            border: "1px solid #50d4ff",
            background: isManualUrlReady && !isSubmitting ? "#50d4ff" : "#27415d",
            color: isManualUrlReady && !isSubmitting ? "#07111b" : "#6d8099",
            padding: "10px 14px",
            fontSize: "14px",
            fontWeight: 600,
            cursor: isManualUrlReady && !isSubmitting ? "pointer" : "not-allowed"
          }}
        >
          Create capture
        </button>
      </div>
    </section>
  );
}
