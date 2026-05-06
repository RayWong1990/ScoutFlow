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
  canonical_url: string;
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
  target_path: string | null;
  error: BridgeError | null;
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
    createCapture: async (canonicalUrl: string): Promise<CreateCaptureResponse> => {
      const response = await requestJson<Omit<CreateCaptureResponse, "canonical_url">>(baseUrl, "/captures/discover", {
        method: "POST",
        body: JSON.stringify({
          platform: "bilibili",
          canonical_url: canonicalUrl,
          source_kind: "manual_url",
          quick_capture_preset: "metadata_only"
        })
      });

      return {
        ...response,
        canonical_url: canonicalUrl
      };
    },
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
