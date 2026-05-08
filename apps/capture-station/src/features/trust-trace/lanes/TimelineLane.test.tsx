import { fireEvent, render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import type { TrustTraceResponse } from "../../../lib/api-client";
import TimelineLane from "./TimelineLane";

function buildTrace(overrides?: Partial<TrustTraceResponse>): TrustTraceResponse {
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

describe("TimelineLane", () => {
  it("shows an honest empty state when trust-trace readback is absent", () => {
    render(<TimelineLane trace={null} />);

    expect(screen.getByText("W1B timeline lane")).toBeTruthy();
    expect(screen.getByText("没有 trust-trace readback，不生成伪时间轴或假时间戳。")).toBeTruthy();
  });

  it("renders dto-derived evidence order instead of pretending wall-clock truth", () => {
    render(<TimelineLane trace={buildTrace()} />);

    expect(screen.getByText("证据顺序，不代表真实时间轴")).toBeTruthy();
    expect(screen.getByText("顺序只来自现有 DTO section 与 status，不代表真实时间戳。")).toBeTruthy();
    expect(screen.getByRole("button", { name: /capture /i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /capture_state/i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /metadata_job/i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /probe_evidence/i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /receipt_ledger/i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /media_audio/i })).toBeTruthy();
    expect(screen.getByRole("button", { name: /audit/i })).toBeTruthy();
  });

  it("moves evidence focus on hover or focus and shows bounded detail for the selected dto section", () => {
    render(<TimelineLane trace={buildTrace()} />);

    const detail = screen.getByRole("region", { name: "当前证据详情" });
    expect(within(detail).getByText("capture")).toBeTruthy();
    expect(within(detail).queryByText("capture_manifest")).toBeNull();

    fireEvent.focus(screen.getByRole("button", { name: /receipt_ledger/i }));

    expect(within(detail).getByText("receipt_ledger")).toBeTruthy();
    expect(within(detail).getByText("capture_manifest")).toBeTruthy();
    expect(within(detail).getByText("metadata_snapshot")).toBeTruthy();
    expect(within(detail).getByText("redaction")).toBeTruthy();
  });

  it("does not render raw long audio transcript in media audio detail", () => {
    const longTranscript = "future transcript with private operator context ".repeat(8);
    render(
      <TimelineLane
        trace={buildTrace({
          media_audio: {
            status: "ok",
            audio_transcript: longTranscript,
          },
        })}
      />,
    );

    fireEvent.focus(screen.getByRole("button", { name: /media_audio/i }));

    const detail = screen.getByRole("region", { name: "当前证据详情" });
    expect(within(detail).queryByText(longTranscript)).toBeNull();
    expect(within(detail).getByText("audio_transcript_preview")).toBeTruthy();
    expect(within(detail).getByText(/\[truncated\]/)).toBeTruthy();
    expect(screen.queryByText(longTranscript)).toBeNull();
  });

  it("renders blocked and empty audio transcript as bounded status words", () => {
    const { rerender } = render(
      <TimelineLane
        trace={buildTrace({
          media_audio: {
            status: "not_approved",
            audio_transcript: "blocked",
          },
        })}
      />,
    );

    fireEvent.focus(screen.getByRole("button", { name: /media_audio/i }));
    expect(within(screen.getByRole("region", { name: "当前证据详情" })).getByText("blocked")).toBeTruthy();

    rerender(
      <TimelineLane
        trace={buildTrace({
          media_audio: {
            status: "not_requested",
            audio_transcript: "",
          },
        })}
      />,
    );

    fireEvent.focus(screen.getByRole("button", { name: /media_audio/i }));
    expect(within(screen.getByRole("region", { name: "当前证据详情" })).getByText("not_present")).toBeTruthy();
  });
});
