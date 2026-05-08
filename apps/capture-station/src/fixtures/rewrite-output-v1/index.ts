import blockedNoTranscript from "./blocked-no-transcript.json";
import okWithTranscript from "./ok-with-transcript.json";
import partialRewrite from "./partial-rewrite.json";

export type RewriteOutputV1 = {
  style_id: "obsidian_capture_note_v1";
  title: string;
  source_summary: string;
  key_points: string[];
  transcript_backed_details: string;
  trust_evidence_notes: string;
  follow_up_questions: string[];
  source_hash: string;
  transcript_hash: string | null;
  rewrite_hash: string;
};

type RewriteFixtureRecord = {
  fileName: string;
  label: string;
  output: RewriteOutputV1;
};

export const rewriteOutputFixtures = {
  "ok-with-transcript": {
    fileName: "ok-with-transcript.json",
    label: "happy path",
    output: okWithTranscript as RewriteOutputV1,
  },
  "blocked-no-transcript": {
    fileName: "blocked-no-transcript.json",
    label: "blocked by transcript handoff",
    output: blockedNoTranscript as RewriteOutputV1,
  },
  "partial-rewrite": {
    fileName: "partial-rewrite.json",
    label: "partial rewrite",
    output: partialRewrite as RewriteOutputV1,
  },
} satisfies Record<string, RewriteFixtureRecord>;
