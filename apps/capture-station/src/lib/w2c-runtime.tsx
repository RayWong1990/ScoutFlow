/* eslint-disable react-refresh/only-export-components */
import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from "react";

import {
  CaptureStationApiError,
  type BridgeHealthResponse,
  type BridgeVaultCommitResponse,
  type BridgeVaultConfigResponse,
  type BridgeVaultPreviewResponse,
  type CreateCaptureResponse,
  createCaptureStationApi,
  type MetadataFetchJobResponse,
  type TrustTraceResponse,
} from "./api-client";
import { createQueryClient } from "./query-client";

type AsyncStatus = "idle" | "loading" | "success" | "error";

export type AsyncState<T> = {
  status: AsyncStatus;
  data: T | null;
  error: CaptureStationApiError | null;
};

export type W2CRuntimeValue = {
  canonicalUrl: string;
  setCanonicalUrl: (value: string) => void;
  captureSourceUrl: string | null;
  capture: AsyncState<CreateCaptureResponse>;
  metadataFetch: AsyncState<MetadataFetchJobResponse>;
  bridgeHealth: AsyncState<BridgeHealthResponse>;
  bridgeVaultConfig: AsyncState<BridgeVaultConfigResponse>;
  trustTrace: AsyncState<TrustTraceResponse>;
  vaultPreview: AsyncState<BridgeVaultPreviewResponse>;
  vaultCommitDryRun: AsyncState<BridgeVaultCommitResponse>;
  currentCaptureId: string | null;
  createCapture: () => Promise<void>;
  refreshCaptureBoundData: () => Promise<void>;
  runVaultCommitDryRun: () => Promise<void>;
  clearCapture: () => void;
  isRuntimeBlocked: boolean;
  isVaultWriteBlocked: boolean;
};

const W2CRuntimeContext = createContext<W2CRuntimeValue | null>(null);

function idleState<T>(): AsyncState<T> {
  return { status: "idle", data: null, error: null };
}

function loadingState<T>(previous: T | null = null): AsyncState<T> {
  return { status: "loading", data: previous, error: null };
}

function successState<T>(data: T): AsyncState<T> {
  return { status: "success", data, error: null };
}

function errorState<T>(error: CaptureStationApiError, previous: T | null = null): AsyncState<T> {
  return { status: "error", data: previous, error };
}

function asApiError(error: unknown): CaptureStationApiError {
  if (error instanceof CaptureStationApiError) {
    return error;
  }

  return new CaptureStationApiError("Unexpected request failure", {
    status: 500,
    payload: error,
  });
}

function trustTraceKey(captureId: string): string {
  return `trust-trace:${captureId}`;
}

function vaultPreviewKey(captureId: string): string {
  return `vault-preview:${captureId}`;
}

function metadataFetchKey(captureId: string): string {
  return `metadata-fetch:${captureId}`;
}

function preserveOrError<T>(error: CaptureStationApiError, previous: AsyncState<T>): AsyncState<T> {
  return errorState(error, previous.data);
}

export function W2CRuntimeProvider({ children }: { children: ReactNode }) {
  const apiRef = useRef(createCaptureStationApi(import.meta.env.VITE_API_BASE ?? ""));
  const queryClientRef = useRef(createQueryClient());
  const captureGenerationRef = useRef(0);
  const currentCaptureIdRef = useRef<string | null>(null);

  const [canonicalUrl, setCanonicalUrl] = useState("https://www.bilibili.com/video/BV1xK4y1f7yC");
  const [captureSourceUrl, setCaptureSourceUrl] = useState<string | null>(null);
  const [capture, setCapture] = useState<AsyncState<CreateCaptureResponse>>(idleState());
  const [metadataFetch, setMetadataFetch] = useState<AsyncState<MetadataFetchJobResponse>>(idleState());
  const [bridgeHealth, setBridgeHealth] = useState<AsyncState<BridgeHealthResponse>>(idleState());
  const [bridgeVaultConfig, setBridgeVaultConfig] = useState<AsyncState<BridgeVaultConfigResponse>>(idleState());
  const [trustTrace, setTrustTrace] = useState<AsyncState<TrustTraceResponse>>(idleState());
  const [vaultPreview, setVaultPreview] = useState<AsyncState<BridgeVaultPreviewResponse>>(idleState());
  const [vaultCommitDryRun, setVaultCommitDryRun] = useState<AsyncState<BridgeVaultCommitResponse>>(idleState());

  const currentCaptureId = capture.data?.capture_id ?? null;

  useEffect(() => {
    currentCaptureIdRef.current = currentCaptureId;
  }, [currentCaptureId]);

  useEffect(() => {
    let cancelled = false;

    async function loadBridgeState() {
      setBridgeHealth(loadingState());
      setBridgeVaultConfig(loadingState());

      const [healthResult, configResult] = await Promise.allSettled([
        apiRef.current.getBridgeHealth(),
        apiRef.current.getBridgeVaultConfig(),
      ]);
      if (cancelled) {
        return;
      }

      if (healthResult.status === "fulfilled") {
        setBridgeHealth(successState(healthResult.value));
      } else {
        setBridgeHealth((previous) => preserveOrError(asApiError(healthResult.reason), previous));
      }

      if (configResult.status === "fulfilled") {
        setBridgeVaultConfig(successState(configResult.value));
      } else {
        setBridgeVaultConfig((previous) => preserveOrError(asApiError(configResult.reason), previous));
      }
    }

    void loadBridgeState();

    return () => {
      cancelled = true;
    };
  }, []);

  useEffect(() => {
    if (!currentCaptureId) {
      setTrustTrace(idleState());
      setVaultPreview(idleState());
      setVaultCommitDryRun(idleState());
      return;
    }

    let cancelled = false;
    const captureId = currentCaptureId;
    const generation = captureGenerationRef.current;

    async function loadCaptureBoundData() {
      setTrustTrace(loadingState());
      setVaultPreview(loadingState());

      const [trustTraceResult, vaultPreviewResult] = await Promise.allSettled([
        queryClientRef.current.get(trustTraceKey(captureId), () => apiRef.current.getTrustTrace(captureId)),
        queryClientRef.current.get(vaultPreviewKey(captureId), () => apiRef.current.getVaultPreview(captureId)),
      ]);
      if (cancelled || generation != captureGenerationRef.current || currentCaptureIdRef.current !== captureId) {
        return;
      }

      if (trustTraceResult.status === "fulfilled") {
        setTrustTrace(successState(trustTraceResult.value));
      } else {
        queryClientRef.current.invalidate(trustTraceKey(captureId));
        setTrustTrace((previous) => preserveOrError(asApiError(trustTraceResult.reason), previous));
      }

      if (vaultPreviewResult.status === "fulfilled") {
        setVaultPreview(successState(vaultPreviewResult.value));
      } else {
        queryClientRef.current.invalidate(vaultPreviewKey(captureId));
        setVaultPreview((previous) => preserveOrError(asApiError(vaultPreviewResult.reason), previous));
      }
    }

    void loadCaptureBoundData();

    return () => {
      cancelled = true;
    };
  }, [currentCaptureId]);

  async function createCapture() {
    captureGenerationRef.current += 1;
    queryClientRef.current.clear();
    setCaptureSourceUrl(null);
    setCapture(loadingState());
    setMetadataFetch(idleState());
    setTrustTrace(idleState());
    setVaultPreview(idleState());
    setVaultCommitDryRun(idleState());

    try {
      const nextCapture = await apiRef.current.createCapture(canonicalUrl);
      setCapture(successState(nextCapture));
      setCaptureSourceUrl(canonicalUrl);

      setMetadataFetch(loadingState());
      try {
        const nextMetadataFetch = await apiRef.current.postMetadataFetchJob(nextCapture.capture_id);
        queryClientRef.current.invalidate(metadataFetchKey(nextCapture.capture_id));
        setMetadataFetch(successState(nextMetadataFetch));
      } catch (error) {
        setMetadataFetch(errorState(asApiError(error)));
      }
    } catch (error) {
      const apiError = asApiError(error);
      setCapture(errorState(apiError));
    }
  }

  async function refreshCaptureBoundData() {
    if (!currentCaptureId) {
      return;
    }

    const captureId = currentCaptureId;
    const generation = captureGenerationRef.current;
    queryClientRef.current.invalidate(trustTraceKey(captureId));
    queryClientRef.current.invalidate(vaultPreviewKey(captureId));
    setTrustTrace(loadingState());
    setVaultPreview(loadingState());

    const [trustTraceResult, vaultPreviewResult] = await Promise.allSettled([
      apiRef.current.getTrustTrace(captureId),
      apiRef.current.getVaultPreview(captureId),
    ]);

    if (generation != captureGenerationRef.current || currentCaptureIdRef.current !== captureId) {
      return;
    }

    if (trustTraceResult.status === "fulfilled") {
      setTrustTrace(successState(trustTraceResult.value));
    } else {
      setTrustTrace((previous) => preserveOrError(asApiError(trustTraceResult.reason), previous));
    }

    if (vaultPreviewResult.status === "fulfilled") {
      setVaultPreview(successState(vaultPreviewResult.value));
    } else {
      setVaultPreview((previous) => preserveOrError(asApiError(vaultPreviewResult.reason), previous));
    }
  }

  async function runVaultCommitDryRun() {
    if (!currentCaptureId) {
      return;
    }

    setVaultCommitDryRun(loadingState(vaultCommitDryRun.data));
    try {
      const nextDryRun = await apiRef.current.postVaultCommitDryRun(currentCaptureId);
      setVaultCommitDryRun(successState(nextDryRun));
    } catch (error) {
      setVaultCommitDryRun(errorState(asApiError(error), vaultCommitDryRun.data));
    }
  }

  function clearCapture() {
    captureGenerationRef.current += 1;
    queryClientRef.current.clear();
    setCapture(idleState());
    setCaptureSourceUrl(null);
    setMetadataFetch(idleState());
    setTrustTrace(idleState());
    setVaultPreview(idleState());
    setVaultCommitDryRun(idleState());
  }

  const isRuntimeBlocked = true;
  const isVaultWriteBlocked = bridgeHealth.data?.write_enabled !== true || bridgeVaultConfig.data?.write_enabled !== true;

  return (
    <W2CRuntimeContext.Provider
      value={{
        canonicalUrl,
        setCanonicalUrl,
        captureSourceUrl,
        capture,
        metadataFetch,
        bridgeHealth,
        bridgeVaultConfig,
        trustTrace,
        vaultPreview,
        vaultCommitDryRun,
        currentCaptureId,
        createCapture,
        refreshCaptureBoundData,
        runVaultCommitDryRun,
        clearCapture,
        isRuntimeBlocked,
        isVaultWriteBlocked,
      }}
    >
      {children}
    </W2CRuntimeContext.Provider>
  );
}

export function useW2CRuntime(): W2CRuntimeValue {
  const value = useContext(W2CRuntimeContext);
  if (!value) {
    throw new Error("useW2CRuntime must be used within W2CRuntimeProvider");
  }
  return value;
}
