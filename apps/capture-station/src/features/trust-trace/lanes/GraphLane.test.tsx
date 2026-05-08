import { fireEvent, render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import type { TrustTraceResponse } from "../../../lib/api-client";
import GraphLane from "./GraphLane";

function buildTraceResponse(overrides?: Partial<TrustTraceResponse>): TrustTraceResponse {
  return {
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
      status: "metadata_fetched",
    },
    metadata_job: {
      present: true,
      job_id: "job_123",
      job_type: "metadata_fetch",
      status: "succeeded",
      platform_result: "metadata_fetched",
    },
    probe_evidence: {
      present: true,
      probe_mode: "auth_present",
      source_task_id: "T-P1A-013",
      source_report_path: "docs/research/probe.md",
      platform_result: "auth_present",
    },
    receipt_ledger: {
      present: true,
      artifact_count: 2,
      artifact_kinds: ["capture_manifest", "metadata_snapshot"],
      redaction: "safe_fields_only",
    },
    media_audio: {
      status: "not_approved",
      audio_transcript: "blocked",
    },
    audit: {
      platform_result: "metadata_fetched",
      evidence_file_path: "data/artifacts/bilibili/cap_123/evidence.json",
      artifact_count: 2,
      redaction_policy: "safe_fields_only",
      safe_parsed_fields: {
        title: "ScoutFlow W2C Demo",
        duration_seconds: 123,
      },
    },
    ...overrides,
  };
}

describe("GraphLane", () => {
  it("shows an honest empty state when trust trace readback is absent", () => {
    render(<GraphLane trace={null} />);

    expect(screen.getByText("W1B graph lane")).toBeTruthy();
    expect(screen.getByText("capture readback 为空时，不伪造 section 节点或连线。")).toBeTruthy();
    expect(screen.queryByRole("button", { name: /section node/i })).toBeNull();
  });

  it("renders only DTO-backed section nodes and explains the bounded graph meaning", () => {
    render(<GraphLane trace={buildTraceResponse()} />);

    expect(screen.getByRole("img", { name: "Trust Trace graph" })).toBeTruthy();
    expect(screen.getByText("当前图仅表示 trust-trace DTO section 邻接关系，不表示时间线、执行顺序或服务端确认因果。")).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node capture" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node metadata_job" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node probe_evidence" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node receipt_ledger" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node media_audio" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "section node audit" })).toBeTruthy();
    expect(within(screen.getByRole("button", { name: "section node metadata_job" })).getByText(/metadata_fetch/)).toBeTruthy();
    expect(within(screen.getByRole("button", { name: "section node receipt_ledger" })).getByText(/artifacts 2/)).toBeTruthy();
  });

  it("reveals bounded node detail on focus without inventing extra fields", () => {
    render(<GraphLane trace={buildTraceResponse()} />);

    expect(screen.getByText("悬停或聚焦节点后再查看限定字段。")).toBeTruthy();
    expect(screen.queryByText("source_report_path")).toBeNull();

    fireEvent.focus(screen.getByRole("button", { name: "section node probe_evidence" }));

    const detail = screen.getByRole("region", { name: "node detail probe_evidence" });
    expect(within(detail).getByText("source_task_id")).toBeTruthy();
    expect(within(detail).getByText("T-P1A-013")).toBeTruthy();
    expect(within(detail).getByText("source_report_path")).toBeTruthy();
    expect(within(detail).getByText("docs/research/probe.md")).toBeTruthy();
    expect(within(detail).queryByText("timestamp")).toBeNull();
  });

  it("does not mark failed-but-present nodes as ready", () => {
    render(
      <GraphLane
        trace={buildTraceResponse({
          metadata_job: {
            present: true,
            job_id: "job_123",
            job_type: "metadata_fetch",
            status: "failed",
            platform_result: "error",
          },
          audit: {
            platform_result: "failed",
            evidence_file_path: "data/artifacts/bilibili/cap_123/evidence.json",
            artifact_count: 2,
            redaction_policy: "safe_fields_only",
            safe_parsed_fields: {
              title: "ScoutFlow W2C Demo",
              duration_seconds: 123,
            },
          },
        })}
      />,
    );

    expect(screen.getByRole("button", { name: "section node metadata_job" }).getAttribute("data-tone")).toBe("attention");
    expect(screen.getByRole("button", { name: "section node audit" }).getAttribute("data-tone")).toBe("attention");
  });
});
