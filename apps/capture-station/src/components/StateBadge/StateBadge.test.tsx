import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import StateBadge from "./StateBadge";
import { deriveTrustTraceBadge } from "./derive";

describe("StateBadge", () => {
  it("normalizes legacy ready tone into preview semantics", () => {
    render(<StateBadge tone="ready" label="可创建" />);

    const badge = screen.getByText("可创建").closest("span[data-state]");
    expect(badge?.getAttribute("data-state")).toBe("preview");
  });

  it("derives trust-trace badge from business state instead of route success", () => {
    const badge = deriveTrustTraceBadge({
      routeStatus: "success",
      currentCaptureId: "cap_123",
      trace: {
        label: "Status / Trust Trace / 采集状态",
        capture: {
          capture_id: "cap_123",
          platform: "bilibili",
          platform_item_id: "BV1xK4y1f7yC",
          source_kind: "manual_url",
          capture_mode: "metadata_only",
          created_by_path: "quick_capture",
        },
        capture_state: {
          capture_created: true,
          status: "discovered",
        },
        metadata_job: {
          present: true,
          job_id: "job_123",
          job_type: "metadata_fetch",
          status: "queued",
          platform_result: null,
        },
        probe_evidence: {
          present: false,
          probe_mode: "not-run",
          source_task_id: null,
          source_report_path: null,
          platform_result: null,
        },
        receipt_ledger: {
          present: false,
          artifact_count: 0,
          artifact_kinds: [],
          redaction: "not_applicable",
        },
        media_audio: {
          status: "not_approved",
          audio_transcript: "blocked",
        },
        audit: {
          platform_result: null,
          evidence_file_path: null,
          artifact_count: 0,
          redaction_policy: null,
          safe_parsed_fields: {},
        },
      },
    });

    expect(badge.tone).toBe("loading");
    expect(badge.label).toBe("metadata_fetch 处理中");
  });
});
