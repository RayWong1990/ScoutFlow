export type BridgeError = {
  code: string;
  message: string;
};

export type BridgeHealthResponse = {
  bridge_available: boolean;
  spec_version: string;
  write_enabled: boolean;
  blocked_by: string[];
};

export type CreateCaptureResponse = {
  capture_id: string;
  platform: string;
  platform_item_id: string;
  source_kind: string;
  capture_mode: string;
  created_by_path: string;
  status: string;
  artifact_root_path: string;
  manifest_path: string;
};

export type MetadataFetchJobResponse = {
  job_id: string;
  capture_id: string;
  job_type: "metadata_fetch";
  status: "queued" | "running" | "succeeded" | "failed";
  dedupe_key: string;
};

export type BridgeVaultConfigResponse = {
  vault_root_resolved: boolean;
  vault_root: string | null;
  preview_enabled: boolean;
  write_enabled: boolean;
  frontmatter_mode: string;
  error: BridgeError | null;
};

export type BridgeVaultPreviewResponse = {
  capture_id: string;
  target_path: string;
  frontmatter: Record<string, string>;
  body_markdown: string;
  warnings: string[];
};

export type BridgeVaultCommitResponse = {
  capture_id: string;
  committed: boolean;
  dry_run: boolean;
  write_enabled: false;
  target_path: string | null;
  error: BridgeError | null;
};

export type TrustTraceResponse = {
  label: string;
  capture: {
    capture_id: string;
    platform: string;
    platform_item_id: string;
    source_kind: string;
    capture_mode: string;
    created_by_path: string;
  };
  capture_state: {
    capture_created: boolean;
    status: string;
  };
  metadata_job: {
    present: boolean;
    job_id: string | null;
    job_type: string | null;
    status: string | null;
    platform_result: string | null;
  };
  probe_evidence: {
    present: boolean;
    probe_mode: string;
    source_task_id: string | null;
    source_report_path: string | null;
    platform_result: string | null;
  };
  receipt_ledger: {
    present: boolean;
    artifact_count: number;
    artifact_kinds: string[];
    redaction: string;
  };
  media_audio: {
    status: string;
    audio_transcript: string;
  };
  audit: {
    platform_result: string | null;
    evidence_file_path: string | null;
    artifact_count: number;
    redaction_policy: string | null;
    safe_parsed_fields: Record<string, string | number | null>;
  };
};

export class CaptureStationApiError extends Error {
  status: number;
  code?: string;
  payload?: unknown;

  constructor(message: string, options: { status: number; code?: string; payload?: unknown }) {
    super(message);
    this.name = "CaptureStationApiError";
    this.status = options.status;
    this.code = options.code;
    this.payload = options.payload;
  }
}

export function buildApiUrl(baseUrl: string, path: string): string {
  const normalizedBase = baseUrl.endsWith("/") ? baseUrl.slice(0, -1) : baseUrl;
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  return `${normalizedBase}${normalizedPath}`;
}

async function requestJson<T>(baseUrl: string, path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(buildApiUrl(baseUrl, path), {
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {})
    },
    ...init
  });

  const payload = await response.json().catch(() => null);
  if (!response.ok) {
    const bridgeError = payload as Partial<BridgeError> | null;
    throw new CaptureStationApiError(
      bridgeError?.message ?? `Bridge request failed with status ${response.status}`,
      {
        status: response.status,
        code: bridgeError?.code,
        payload
      }
    );
  }

  return payload as T;
}

export function createCaptureStationApi(baseUrl = "") {
  return {
    createCapture: (canonicalUrl: string): Promise<CreateCaptureResponse> =>
      requestJson<CreateCaptureResponse>(baseUrl, "/captures/discover", {
        method: "POST",
        body: JSON.stringify({
          platform: "bilibili",
          canonical_url: canonicalUrl,
          source_kind: "manual_url",
          quick_capture_preset: "metadata_only"
        })
      }),
    postMetadataFetchJob: (captureId: string) =>
      requestJson<MetadataFetchJobResponse>(baseUrl, `/captures/${captureId}/metadata-fetch/jobs`, {
        method: "POST"
      }),
    getTrustTrace: (captureId: string) =>
      requestJson<TrustTraceResponse>(baseUrl, `/captures/${captureId}/trust-trace`),
    getBridgeHealth: () => requestJson<BridgeHealthResponse>(baseUrl, "/bridge/health"),
    getBridgeVaultConfig: () => requestJson<BridgeVaultConfigResponse>(baseUrl, "/bridge/vault/config"),
    getVaultPreview: (captureId: string) =>
      requestJson<BridgeVaultPreviewResponse>(baseUrl, `/captures/${captureId}/vault-preview`),
    postVaultCommitDryRun: (captureId: string) =>
      requestJson<BridgeVaultCommitResponse>(baseUrl, `/captures/${captureId}/vault-commit`, {
        method: "POST"
      })
  };
}
