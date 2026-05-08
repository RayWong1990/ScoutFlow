import PanelCard from "./components/PanelCard/PanelCard";
import PromoteGate, { type PromoteGateItem } from "./components/PromoteGate/PromoteGate";
import StateBadge from "./components/StateBadge/StateBadge";
import { deriveTrustTraceBadge, type StateBadgeTone } from "./components/StateBadge/derive";
import EvidenceTable, { type EvidenceColumn, type EvidenceRow } from "./components/EvidenceTable/EvidenceTable";
import HoldBanner from "./components/HoldBanner/HoldBanner";
import { DEFAULT_HOLDS } from "./components/HoldBanner/holds";
import LiveMetadata from "./features/live-metadata/LiveMetadata";
import RewriteOutputPreview from "./features/rewrite-output/RewriteOutputPreview";
import { rewriteOutputFixtures } from "./fixtures/rewrite-output-v1";
import SignalHypothesis from "./features/signal-hypothesis/SignalHypothesis";
import TrustTrace from "./features/trust-trace/TrustTrace";
import UrlBar from "./features/url-bar/UrlBar";
import VaultCommit from "./features/vault-commit/VaultCommit";
import VaultPreview from "./features/vault-preview/VaultPreview";
import type { W2CRuntimeValue } from "./lib/w2c-runtime";
import { W2CRuntimeProvider, useW2CRuntime } from "./lib/w2c-runtime";
import { assessCanonicalUrl, getBlockedReasons, getCreateSummary, getMetadataSummary, getPreviewSummary } from "./features/url-bar/w2cSurfaceState";
import styles from "./App.module.css";

const FLOW_SUMMARY_COLUMNS: EvidenceColumn[] = [
  { key: "status", label: "状态" },
  { key: "surface", label: "Surface" },
  { key: "source", label: "来源", code: true },
  { key: "truth", label: "当前 truth" },
];

const OVERFLOW_HOLDS = [
  "true_vault_write",
  "runtime_tools",
  "browser_automation",
  "dbvnext_migration",
  "full_signal_workbench",
] as const;

type RewriteFixtureKey = keyof typeof rewriteOutputFixtures;

function isBlockedTranscript(runtime: W2CRuntimeValue): boolean {
  const transcript = runtime.trustTrace.data?.media_audio.audio_transcript?.trim().toLowerCase();
  const status = runtime.trustTrace.data?.media_audio.status?.trim().toLowerCase() ?? "";
  return transcript === "blocked" || transcript === "" || status.includes("blocked") || status.includes("not_approved");
}

function selectRewriteFixtureKey(runtime: W2CRuntimeValue): RewriteFixtureKey {
  if (!runtime.currentCaptureId || !runtime.trustTrace.data || isBlockedTranscript(runtime)) {
    return "blocked-no-transcript";
  }

  if (!runtime.trustTrace.data.receipt_ledger.present || Object.keys(runtime.trustTrace.data.audit.safe_parsed_fields).length < 2) {
    return "partial-rewrite";
  }

  return "ok-with-transcript";
}

function getRewriteMissingFields(output: (typeof rewriteOutputFixtures)[RewriteFixtureKey]["output"]): string[] {
  const missing: string[] = [];
  if (output.transcript_hash === null) {
    missing.push("transcript_hash");
  }
  if (!output.transcript_backed_details.trim()) {
    missing.push("transcript_backed_details");
  }
  if (!output.source_summary.trim()) {
    missing.push("source_summary");
  }
  if (output.key_points.length === 0) {
    missing.push("key_points");
  }
  if (!output.trust_evidence_notes.trim()) {
    missing.push("trust_evidence_notes");
  }
  if (output.follow_up_questions.length === 0) {
    missing.push("follow_up_questions");
  }
  return missing;
}

function getRewriteBadgeTone(output: (typeof rewriteOutputFixtures)[RewriteFixtureKey]["output"]): StateBadgeTone {
  if (output.transcript_hash === null) {
    return "blocked";
  }

  return getRewriteMissingFields(output).length > 0 ? "partial" : "preview";
}

function toEvidenceTone(tone: StateBadgeTone): EvidenceRow["tone"] {
  switch (tone) {
    case "blocked":
    case "disabled":
      return "blocked";
    case "failed":
      return "failed";
    case "partial":
    case "loading":
      return "partial";
    case "committed":
      return "committed";
    case "preview":
      return "preview";
    default:
      return "default";
  }
}

function buildPromoteItems(runtime: W2CRuntimeValue, rewriteFixtureKey: RewriteFixtureKey): PromoteGateItem[] {
  const urlReady = assessCanonicalUrl(runtime.canonicalUrl).isValid;
  const trustTraceReady = runtime.trustTrace.status === "success" || runtime.trustTrace.status === "error";
  const previewReady = runtime.vaultPreview.status === "success";
  const rewriteTone = getRewriteBadgeTone(rewriteOutputFixtures[rewriteFixtureKey].output);

  return [
    { label: "manual URL accepted", status: urlReady ? "met" : "pending" },
    { label: "Trust Trace visible", status: trustTraceReady ? "met" : runtime.currentCaptureId ? "pending" : "disabled" },
    { label: "Vault Preview visible", status: previewReady ? "met" : runtime.currentCaptureId ? "pending" : "disabled" },
    {
      label: "RewriteOutputV1 truthful",
      status: rewriteTone === "blocked" ? "blocked" : rewriteTone === "partial" ? "pending" : "met",
    },
    { label: "write_enabled=False explicit", status: runtime.isVaultWriteBlocked ? "met" : "blocked" },
    { label: "true_vault_write remains held", status: "blocked" },
  ];
}

function buildFlowSummaryRows(runtime: W2CRuntimeValue, rewriteFixtureKey: RewriteFixtureKey): EvidenceRow[] {
  const createSummary = getCreateSummary(runtime);
  const metadataSummary = getMetadataSummary(runtime);
  const previewSummary = getPreviewSummary(runtime);
  const trustTraceSummary = deriveTrustTraceBadge({
    trace: runtime.trustTrace.data,
    routeStatus: runtime.trustTrace.status,
    currentCaptureId: runtime.currentCaptureId,
  });
  const rewriteFixture = rewriteOutputFixtures[rewriteFixtureKey];
  const rewriteMissingFields = getRewriteMissingFields(rewriteFixture.output);
  const blockedReasons = getBlockedReasons(runtime);

  return [
    {
      id: "url",
      tone: toEvidenceTone(createSummary.tone),
      cells: {
        status: createSummary.label,
        surface: "URL input",
        source: "POST /captures/discover",
        truth: createSummary.detail,
      },
    },
    {
      id: "metadata",
      tone: toEvidenceTone(metadataSummary.tone),
      cells: {
        status: metadataSummary.label,
        surface: "Live metadata",
        source: "metadata_fetch + trust-trace",
        truth: metadataSummary.detail,
      },
    },
    {
      id: "trust-trace",
      tone: toEvidenceTone(trustTraceSummary.tone),
      cells: {
        status: trustTraceSummary.label,
        surface: "Trust Trace",
        source: "GET /captures/{id}/trust-trace",
        truth: runtime.trustTrace.status === "error"
          ? runtime.trustTrace.error?.code ?? "route_error"
          : runtime.trustTrace.data
            ? "error-path first; graph downgraded to diagnostic"
            : "waiting for readback",
      },
    },
    {
      id: "vault-preview",
      tone: toEvidenceTone(previewSummary.tone),
      cells: {
        status: previewSummary.label,
        surface: "Vault Preview",
        source: "GET /captures/{id}/vault-preview",
        truth: previewSummary.detail,
      },
    },
    {
      id: "rewrite-output",
      tone: toEvidenceTone(getRewriteBadgeTone(rewriteFixture.output)),
      cells: {
        status: rewriteFixture.output.transcript_hash === null ? "truthfully blocked" : rewriteMissingFields.length > 0 ? "partial rewrite" : "preview fixture loaded",
        surface: "RewriteOutputV1",
        source: `fixture:${rewriteFixture.fileName}`,
        truth: rewriteFixture.output.transcript_hash === null
          ? `TranscriptHandoffV1 incomplete; missing=${rewriteMissingFields.join(", ")}`
          : rewriteMissingFields.length > 0
            ? `missing=${rewriteMissingFields.join(", ")}`
            : "obsidian_capture_note_v1 six-section preview ready",
      },
    },
    {
      id: "write-gate",
      tone: "blocked",
      cells: {
        status: "write gate held",
        surface: "Vault Commit",
        source: "bridge health + vault config",
        truth: blockedReasons.join(", ") || "write_enabled=false",
      },
    },
  ];
}

function SingleFlowWorkstation() {
  const runtime = useW2CRuntime();
  const rewriteFixtureKey = selectRewriteFixtureKey(runtime);
  const rewriteFixture = rewriteOutputFixtures[rewriteFixtureKey];
  const trustTraceSummary = deriveTrustTraceBadge({
    trace: runtime.trustTrace.data,
    routeStatus: runtime.trustTrace.status,
    currentCaptureId: runtime.currentCaptureId,
  });
  const overallBadge = runtime.currentCaptureId ? trustTraceSummary : getCreateSummary(runtime);

  return (
    <div className={styles.page}>
      <header className={styles.hero}>
        <div className={styles.heroCopy}>
          <p className={styles.eyebrow}>Lane A P3 preview vertical slice</p>
          <h1 className={styles.title}>Capture Station 单屏操作流</h1>
          <p className={styles.description}>
            URL 输入、live metadata、Trust Trace summary、Vault Preview、write gate 与 RewriteOutputV1 在同一屏内可扫读。
            当前只产出 preview-only operator flow，不声明 runtime tools、true write、browser automation、DB migration 已解禁。
          </p>
        </div>
        <StateBadge tone={overallBadge.tone} label={overallBadge.label} />
      </header>

      <section className={styles.topFold}>
        <PanelCard
          title="Top-fold truth summary"
          eyebrow="single-flow IA"
          description="业务态优先，不把 route success、dry-run return 或 fixture 存在误写成 committed truth。"
        >
          <EvidenceTable
            columns={FLOW_SUMMARY_COLUMNS}
            rows={buildFlowSummaryRows(runtime, rewriteFixtureKey)}
            emptyCopy="单屏流还没有可展示的 truth。"
          />
        </PanelCard>

        <div className={styles.sideStack}>
          <PanelCard
            title="Promote / hold posture"
            eyebrow="preview-only gate"
            description="PromoteGate 只说明当前单屏流能否被诚实扫读，不代表 Phase 1A runtime approval。"
          >
            <PromoteGate title="Single-flow operator scanline" items={buildPromoteItems(runtime, rewriteFixtureKey)} />
          </PanelCard>

          <PanelCard
            title="Rewrite fixture binding"
            eyebrow="obsidian_capture_note_v1"
            description="Rewrite surface 只 consume mock fixture，不接 runtime rewrite。"
            aside={<StateBadge tone={getRewriteBadgeTone(rewriteFixture.output)} label={rewriteFixture.label} />}
          >
            <dl className={styles.fixtureGrid}>
              <div className={styles.fixtureRow}>
                <dt>fixture</dt>
                <dd><code>{rewriteFixture.fileName}</code></dd>
              </div>
              <div className={styles.fixtureRow}>
                <dt>style_id</dt>
                <dd><code>{rewriteFixture.output.style_id}</code></dd>
              </div>
              <div className={styles.fixtureRow}>
                <dt>binding rule</dt>
                <dd>{rewriteFixtureKey === "blocked-no-transcript" ? "transcript handoff incomplete -> blocked" : "fixture chosen by current readback posture"}</dd>
              </div>
            </dl>
          </PanelCard>
        </div>
      </section>

      <section className={styles.holdGrid} aria-label="Remaining holds">
        {OVERFLOW_HOLDS.map((holdKey) => (
          <HoldBanner key={holdKey} {...DEFAULT_HOLDS[holdKey]} />
        ))}
      </section>

      <section className={styles.flowStack}>
        <UrlBar />
        <LiveMetadata />
        <TrustTrace />
        <VaultPreview />
        <VaultCommit />
        <RewriteOutputPreview fixture={rewriteFixture.output} fixtureName={rewriteFixture.fileName} />
        <SignalHypothesis />
      </section>
    </div>
  );
}

export default function App() {
  return (
    <W2CRuntimeProvider>
      <SingleFlowWorkstation />
    </W2CRuntimeProvider>
  );
}
