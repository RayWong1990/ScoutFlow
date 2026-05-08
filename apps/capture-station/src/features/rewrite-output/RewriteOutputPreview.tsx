import PanelCard from "../../components/PanelCard/PanelCard";
import EvidenceTable, { type EvidenceColumn, type EvidenceRow } from "../../components/EvidenceTable/EvidenceTable";
import StateBadge from "../../components/StateBadge/StateBadge";
import type { RewriteOutputV1 } from "../../fixtures/rewrite-output-v1";
import styles from "./RewriteOutputPreview.module.css";

export type RewriteOutputPreviewProps = {
  fixture: RewriteOutputV1;
  fixtureName: string;
};

const HASH_COLUMNS: EvidenceColumn[] = [
  { key: "field", label: "字段", code: true },
  { key: "value", label: "值", code: true },
  { key: "status", label: "状态" },
];

function getMissingFields(fixture: RewriteOutputV1): string[] {
  const missing: string[] = [];
  if (fixture.transcript_hash === null) {
    missing.push("transcript_hash");
  }
  if (!fixture.transcript_backed_details.trim()) {
    missing.push("transcript_backed_details");
  }
  if (!fixture.source_summary.trim()) {
    missing.push("source_summary");
  }
  if (fixture.key_points.length === 0) {
    missing.push("key_points");
  }
  if (!fixture.trust_evidence_notes.trim()) {
    missing.push("trust_evidence_notes");
  }
  if (fixture.follow_up_questions.length === 0) {
    missing.push("follow_up_questions");
  }
  return missing;
}

function buildHashRows(fixture: RewriteOutputV1): EvidenceRow[] {
  return [
    {
      id: "source-hash",
      tone: "preview",
      cells: {
        field: "source_hash",
        value: fixture.source_hash,
        status: "present",
      },
    },
    {
      id: "transcript-hash",
      tone: fixture.transcript_hash === null ? "blocked" : "preview",
      cells: {
        field: "transcript_hash",
        value: fixture.transcript_hash ?? "null",
        status: fixture.transcript_hash === null ? "blocked" : "present",
      },
    },
    {
      id: "rewrite-hash",
      tone: "preview",
      cells: {
        field: "rewrite_hash",
        value: fixture.rewrite_hash,
        status: "present",
      },
    },
  ];
}

function getBadge(fixture: RewriteOutputV1) {
  const missingFields = getMissingFields(fixture);
  if (fixture.transcript_hash === null) {
    return {
      tone: "blocked" as const,
      label: "truthfully blocked",
      detail: "RewriteOutputV1 blocked: TranscriptHandoffV1 incomplete",
      missingFields,
    };
  }

  if (missingFields.length > 0) {
    return {
      tone: "partial" as const,
      label: "partial rewrite",
      detail: `RewriteOutputV1 partial: ${missingFields.length} field(s) incomplete`,
      missingFields,
    };
  }

  return {
    tone: "preview" as const,
    label: "preview fixture loaded",
    detail: "obsidian_capture_note_v1 six-section mock is fully populated.",
    missingFields,
  };
}

function SectionBlock({ body, title }: { body: string | string[]; title: string }) {
  const isList = Array.isArray(body);
  const isEmpty = isList ? body.length === 0 : body.trim().length === 0;

  return (
    <article className={styles.sectionCard}>
      <header className={styles.sectionHeader}>
        <h3>{title}</h3>
      </header>
      {isEmpty ? (
        <p className={styles.emptyCopy}>section incomplete</p>
      ) : isList ? (
        <ul className={styles.bulletList}>
          {body.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      ) : (
        <p className={styles.sectionBody}>{body}</p>
      )}
    </article>
  );
}

export default function RewriteOutputPreview({ fixture, fixtureName }: RewriteOutputPreviewProps) {
  const badge = getBadge(fixture);

  return (
    <div className={styles.stack}>
      <PanelCard
        title="Rewrite Output V1"
        eyebrow="rewrite-output"
        description="固定 style_id=obsidian_capture_note_v1；本 surface 只消费 mock fixture，不接 runtime rewrite。"
        aside={<StateBadge tone={badge.tone} label={badge.label} />}
      >
        <div className={styles.overview}>
          <div className={styles.copyStack}>
            <p className={styles.detail}>{badge.detail}</p>
            <dl className={styles.grid}>
              <div className={styles.row}>
                <dt>fixture</dt>
                <dd><code>{fixtureName}</code></dd>
              </div>
              <div className={styles.row}>
                <dt>style_id</dt>
                <dd><code>{fixture.style_id}</code></dd>
              </div>
              <div className={styles.row}>
                <dt>title</dt>
                <dd>{fixture.title || "missing"}</dd>
              </div>
            </dl>
          </div>

          {badge.missingFields.length > 0 ? (
            <div className={styles.blockedBox} role="status" aria-live="polite">
              <strong>RewriteOutputV1 blocked: TranscriptHandoffV1 incomplete</strong>
              <p>缺失字段：</p>
              <ul className={styles.bulletList}>
                {badge.missingFields.map((field) => (
                  <li key={field}><code>{field}</code></li>
                ))}
              </ul>
            </div>
          ) : null}
        </div>
      </PanelCard>

      <PanelCard
        title="Rewrite hashes / gate facts"
        eyebrow="rewrite-output"
        description="frontend-only schema，不回写 backend DTO。"
      >
        <EvidenceTable columns={HASH_COLUMNS} rows={buildHashRows(fixture)} emptyCopy="rewrite hashes unavailable" />
      </PanelCard>

      <div className={styles.sectionGrid}>
        <SectionBlock title="1. Title" body={fixture.title} />
        <SectionBlock title="2. Source summary" body={fixture.source_summary} />
        <SectionBlock title="3. Key points" body={fixture.key_points} />
        <SectionBlock title="4. Transcript-backed details" body={fixture.transcript_backed_details} />
        <SectionBlock title="5. Trust / evidence notes" body={fixture.trust_evidence_notes} />
        <SectionBlock title="6. Follow-up questions or open uncertainties" body={fixture.follow_up_questions} />
      </div>
    </div>
  );
}
