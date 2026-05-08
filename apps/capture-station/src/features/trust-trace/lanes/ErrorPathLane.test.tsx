import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import type { TrustTraceResponse } from "../../../lib/api-client";
import ErrorPathLane from "./ErrorPathLane";

function buildTrace(overrides?: Partial<TrustTraceResponse>): TrustTraceResponse {
  return {
    label: "Status / Trust Trace / 采集状态",
    capture: {
      capture_id: "cap_123",
      platform: "bilibili",
      platform_item_id: "BV1xK4y1f7yC",
      source_kind: "manual_url",
      capture_mode: "metadata_only",
      created_by_path: "captures/discover",
    },
    capture_state: {
      capture_created: true,
      status: "metadata_loaded",
    },
    metadata_job: {
      present: true,
      job_id: "job_123",
      job_type: "metadata_fetch",
      status: "succeeded",
      platform_result: "ok",
    },
    probe_evidence: {
      present: true,
      probe_mode: "task_report",
      source_task_id: "T-P1A-011C",
      source_report_path: "docs/reports/report.md",
      platform_result: "ok",
    },
    receipt_ledger: {
      present: true,
      artifact_count: 2,
      artifact_kinds: ["metadata_snapshot", "receipt"],
      redaction: "safe",
    },
    media_audio: {
      status: "not_requested",
      audio_transcript: "transcript present",
    },
    audit: {
      platform_result: "ok",
      evidence_file_path: "docs/evidence.json",
      artifact_count: 2,
      redaction_policy: "safe",
      safe_parsed_fields: {},
    },
    ...overrides,
  };
}

describe("ErrorPathLane", () => {
  it("shows an honest empty state when trace is absent", () => {
    render(<ErrorPathLane trace={null} routeStatus="idle" routeErrorCode={null} />);

    expect(screen.getByText("W1B error-path lane")).toBeTruthy();
    expect(screen.getByText("暂无 error-path readback")).toBeTruthy();
    expect(screen.getByText("没有 trace 时，只能保留空态，不能虚构受阻步骤。")).toBeTruthy();
  });

  it("surfaces route failure truth when the trust-trace route errors", () => {
    render(<ErrorPathLane trace={buildTrace()} routeStatus="error" routeErrorCode="trust_trace_not_ready" />);

    expect(screen.getByRole("alert")).toBeTruthy();
    expect(screen.getByText("GET /captures/{id}/trust-trace 返回错误")).toBeTruthy();
    expect(screen.getByText("routeErrorCode=trust_trace_not_ready")).toBeTruthy();
    expect(screen.getByText("错误态只回显 route failure truth，不根据旧 trace 反推业务错误路径。")).toBeTruthy();
  });

  it("derives blocked and degraded path cards from DTO gaps without inventing backend errors", () => {
    render(
      <ErrorPathLane
        trace={buildTrace({
          metadata_job: {
            present: false,
            job_id: null,
            job_type: null,
            status: null,
            platform_result: null,
          },
          probe_evidence: {
            present: false,
            probe_mode: "none",
            source_task_id: null,
            source_report_path: null,
            platform_result: null,
          },
          receipt_ledger: {
            present: true,
            artifact_count: 0,
            artifact_kinds: [],
            redaction: "safe",
          },
          media_audio: {
            status: "blocked",
            audio_transcript: "",
          },
          audit: {
            platform_result: null,
            evidence_file_path: null,
            artifact_count: 0,
            redaction_policy: "safe",
            safe_parsed_fields: {},
          },
        })}
        routeStatus="success"
        routeErrorCode={null}
      />,
    );

    expect(screen.getByText("受阻 3")).toBeTruthy();
    expect(screen.getByText("降级 2")).toBeTruthy();
    expect(screen.getByText("正常 1")).toBeTruthy();
    expect(screen.getByText("metadata_job.present=false")).toBeTruthy();
    expect(screen.getByText("probe_evidence.present=false")).toBeTruthy();
    expect(screen.getByText("receipt_ledger.artifact_count=0")).toBeTruthy();
    expect(screen.getByText("media_audio.status=blocked")).toBeTruthy();
    expect(screen.getByText("audit.evidence_file_path=null")).toBeTruthy();
  });

  it("keeps unknown metadata status strings out of the clear bucket", () => {
    render(
      <ErrorPathLane
        trace={buildTrace({
          metadata_job: {
            present: true,
            job_id: "job_123",
            job_type: "metadata_fetch",
            status: "future_unknown_status",
            platform_result: "ok",
          },
        })}
        routeStatus="success"
        routeErrorCode={null}
      />,
    );

    expect(screen.getByText("降级 1")).toBeTruthy();
    expect(screen.getByText("metadata_job.status=future_unknown_status")).toBeTruthy();
    expect(screen.getByText("status 为开放字符串，当前仅按保守 degraded 处理，不推断为 clear。")).toBeTruthy();
  });
});
