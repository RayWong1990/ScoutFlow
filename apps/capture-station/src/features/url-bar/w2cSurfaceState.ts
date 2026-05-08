import type { LifecycleStep } from "../../components/LifecycleStepper/LifecycleStepper";
import type { StateBadgeTone } from "../../components/StateBadge/StateBadge";
import type {
  BridgeVaultPreviewResponse,
  CaptureStationApiError,
  TrustTraceResponse,
} from "../../lib/api-client";
import type { W2CRuntimeValue } from "../../lib/w2c-runtime";

type RuntimeSlice = Pick<
  W2CRuntimeValue,
  | "canonicalUrl"
  | "capture"
  | "metadataFetch"
  | "bridgeHealth"
  | "bridgeVaultConfig"
  | "trustTrace"
  | "vaultPreview"
  | "vaultCommitDryRun"
  | "currentCaptureId"
  | "isRuntimeBlocked"
  | "isVaultWriteBlocked"
>;

export type SurfaceSummary = {
  tone: StateBadgeTone;
  label: string;
  detail: string;
};

export type CanonicalUrlAssessment = {
  isValid: boolean;
  mode: "default" | "focus" | "error";
  errorMessage?: string;
};

function isBilibiliHost(hostname: string): boolean {
  const normalized = hostname.toLowerCase();
  return normalized === "bilibili.com" || normalized.endsWith(".bilibili.com");
}

export function assessCanonicalUrl(value: string): CanonicalUrlAssessment {
  const trimmed = value.trim();
  if (!trimmed) {
    return { isValid: false, mode: "default" };
  }

  let parsed: URL;
  try {
    parsed = new URL(trimmed);
  } catch {
    return {
      isValid: false,
      mode: "error",
      errorMessage: "canonical_url 必须是完整 URL。",
    };
  }

  if (!["http:", "https:"].includes(parsed.protocol)) {
    return {
      isValid: false,
      mode: "error",
      errorMessage: "canonical_url 仅允许 http 或 https。",
    };
  }

  if (!isBilibiliHost(parsed.hostname)) {
    return {
      isValid: false,
      mode: "error",
      errorMessage: "当前只允许 bilibili canonical URL。",
    };
  }

  if (!/BV[0-9A-Za-z]+/.test(trimmed)) {
    return {
      isValid: false,
      mode: "error",
      errorMessage: "canonical_url 必须包含 Bilibili BV id。",
    };
  }

  return {
    isValid: true,
    mode: "focus",
  };
}

export function formatApiError(error: CaptureStationApiError | null | undefined): string {
  if (!error) {
    return "unknown error";
  }

  return error.code ? `${error.code}: ${error.message}` : error.message;
}

export function hasMetadataEvidence(trace: TrustTraceResponse | null | undefined): boolean {
  if (!trace) {
    return false;
  }

  return (
    trace.probe_evidence.present ||
    trace.receipt_ledger.present ||
    trace.receipt_ledger.artifact_count > 0 ||
    Object.keys(trace.audit.safe_parsed_fields).length > 0
  );
}

export function getSafeParsedEntries(trace: TrustTraceResponse | null | undefined): Array<[string, string]> {
  if (!trace) {
    return [];
  }

  return Object.entries(trace.audit.safe_parsed_fields).map(([key, value]) => [key, value == null ? "null" : String(value)]);
}

export function getCreateSummary(runtime: RuntimeSlice): SurfaceSummary {
  const urlAssessment = assessCanonicalUrl(runtime.canonicalUrl);

  if (runtime.capture.status === "error") {
    return {
      tone: "error",
      label: "创建失败",
      detail: formatApiError(runtime.capture.error),
    };
  }

  if (runtime.capture.status === "loading") {
    return {
      tone: "loading",
      label: "创建中",
      detail: "正在调用 POST /captures/discover。",
    };
  }

  if (runtime.currentCaptureId && runtime.capture.data) {
    return {
      tone: "success",
      label: "capture 已创建",
      detail: `${runtime.currentCaptureId} 已由 discover 创建，后续 truth 仍要看 metadata_fetch 与 trust-trace。`,
    };
  }

  if (urlAssessment.isValid) {
    return {
      tone: "ready",
      label: "可创建",
      detail: "仅允许 bilibili + manual_url + metadata_only。",
    };
  }

  return {
    tone: "idle",
    label: "等待 URL",
    detail: "输入合法 canonical_url 后才会调用 discover。",
  };
}

export function getMetadataSummary(runtime: RuntimeSlice): SurfaceSummary {
  if (!runtime.currentCaptureId) {
    return {
      tone: "idle",
      label: "等待 capture",
      detail: "先通过 discover 创建 capture，再看 metadata_fetch 和 trust-trace。",
    };
  }

  if (runtime.metadataFetch.status === "error") {
    return {
      tone: "error",
      label: "metadata_fetch 失败",
      detail: formatApiError(runtime.metadataFetch.error),
    };
  }

  if (runtime.trustTrace.status === "error") {
    return {
      tone: "error",
      label: "trust-trace 读取失败",
      detail: formatApiError(runtime.trustTrace.error),
    };
  }

  if (runtime.metadataFetch.status === "loading" || runtime.trustTrace.status === "loading") {
    return {
      tone: "loading",
      label: "读取中",
      detail: "正在等待 metadata_fetch enqueue 或 trust-trace readback。",
    };
  }

  if (runtime.trustTrace.data && hasMetadataEvidence(runtime.trustTrace.data)) {
    return {
      tone: "metadataLoaded",
      label: "证据已回填",
      detail: "当前展示的是 trust-trace / receipt-derived 安全字段，不是假装全量 metadata route 已落地。",
    };
  }

  const metadataJobStatus = runtime.trustTrace.data?.metadata_job.status ?? runtime.metadataFetch.data?.status ?? null;
  if (metadataJobStatus === "failed") {
    return {
      tone: "error",
      label: "metadata_fetch 失败",
      detail: "job 已失败；当前没有可展示的 readback metadata。",
    };
  }

  if (runtime.metadataFetch.data || runtime.trustTrace.data?.metadata_job.present) {
    return {
      tone: "candidate",
      label: "等待元数据证据",
      detail: "metadata_fetch 已排队，但当前路由只证明 enqueue，不等于元数据已加载。",
    };
  }

  return {
    tone: "metadataOnly",
    label: "capture 已创建",
    detail: "discover 已成功，但 metadata_fetch 尚未建立可读证据。",
  };
}

export function getBridgeSummary(runtime: RuntimeSlice): SurfaceSummary {
  if (runtime.bridgeHealth.status === "error" || runtime.bridgeVaultConfig.status === "error") {
    return {
      tone: "error",
      label: "bridge 读取失败",
      detail: formatApiError(runtime.bridgeHealth.error ?? runtime.bridgeVaultConfig.error),
    };
  }

  if (runtime.bridgeHealth.status === "loading" || runtime.bridgeVaultConfig.status === "loading") {
    return {
      tone: "loading",
      label: "bridge 读取中",
      detail: "正在刷新 /bridge/health 与 /bridge/vault/config。",
    };
  }

  if (!runtime.bridgeHealth.data || !runtime.bridgeVaultConfig.data) {
    return {
      tone: "idle",
      label: "等待 bridge state",
      detail: "App shell 需要 bridge/vault config truth 才能判断 preview 与 gate。",
    };
  }

  if (!runtime.bridgeHealth.data.bridge_available) {
    return {
      tone: "blocked",
      label: "bridge 未就绪",
      detail: runtime.bridgeHealth.data.blocked_by.join(", "),
    };
  }

  return {
    tone: "ready",
    label: "bridge read-only",
    detail: `spec=${runtime.bridgeHealth.data.spec_version}; blocked_by=${runtime.bridgeHealth.data.blocked_by.join(", ") || "none"}`,
  };
}

export function getPreviewSummary(runtime: RuntimeSlice): SurfaceSummary {
  if (!runtime.currentCaptureId) {
    return {
      tone: "idle",
      label: "等待 preview",
      detail: "先创建 capture，才能读取 vault preview。",
    };
  }

  if (runtime.vaultPreview.status === "error") {
    return {
      tone: "error",
      label: "preview 不可读",
      detail: formatApiError(runtime.vaultPreview.error),
    };
  }

  if (runtime.vaultPreview.status === "loading") {
    return {
      tone: "loading",
      label: "preview 读取中",
      detail: "正在调用 GET /captures/{id}/vault-preview。",
    };
  }

  if (runtime.vaultPreview.data) {
    return {
      tone: "previewOnly",
      label: "preview 可读",
      detail: "当前仅展示 dry-run / preview truth，不等于允许 true vault write。",
    };
  }

  return {
    tone: "candidate",
    label: "等待 preview route",
    detail: "capture 已存在，但还没有拿到 vault-preview readback。",
  };
}

export function getLifecycleSteps(runtime: RuntimeSlice): LifecycleStep[] {
  return [
    {
      label: "URL 准备",
      status: runtime.currentCaptureId ? "done" : assessCanonicalUrl(runtime.canonicalUrl).isValid ? "active" : "idle",
    },
    {
      label: "capture discover",
      status: runtime.currentCaptureId ? "done" : runtime.capture.status === "loading" ? "active" : "idle",
    },
    {
      label: "metadata_fetch 入队",
      status: runtime.metadataFetch.data ? "done" : runtime.metadataFetch.status === "loading" ? "active" : "idle",
    },
    {
      label: "Trust Trace / Preview",
      status:
        runtime.trustTrace.data || runtime.vaultPreview.data ? "done" :
        runtime.trustTrace.status === "loading" || runtime.vaultPreview.status === "loading" ? "active" :
        "idle",
    },
    {
      label: "Vault Commit",
      status: runtime.vaultCommitDryRun.data ? "done" : runtime.vaultCommitDryRun.status === "loading" ? "active" : "idle",
    },
  ];
}

export function getBlockedReasons(runtime: RuntimeSlice): string[] {
  const reasons = new Set<string>();

  if (runtime.isRuntimeBlocked) {
    reasons.add("runtime_tools blocked");
  }
  if (runtime.isVaultWriteBlocked) {
    reasons.add("write_enabled=false");
  }
  runtime.bridgeHealth.data?.blocked_by.forEach((item) => reasons.add(item));
  if (runtime.trustTrace.data?.media_audio.audio_transcript === "blocked") {
    reasons.add("audio_transcript blocked");
  }

  return [...reasons];
}

export function toPreviewMarkdown(preview: BridgeVaultPreviewResponse | null, captureId: string | null): string {
  if (!preview) {
    return `---
capture_id: ${captureId ?? "not_created"}
status: preview_unavailable
write_enabled: false
---`;
  }

  const frontmatter = Object.entries(preview.frontmatter)
    .map(([key, value]) => `${key}: ${value}`)
    .join("\n");

  return `---
${frontmatter}
---

${preview.body_markdown}`;
}
