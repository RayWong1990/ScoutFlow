---
decision_id: LEGACY-003-single-user-first-operating-model
status: candidate / legacy-decision / not-authority
authority: not-authority
source_project: ContentFlow / ScoutFlow cross-project memory, not fully live-verified in this build
introduced_or_exposed: legacy
attribution_confidence: low-medium
---

# Single-user first operating model

## Candidate legacy claim

The governance should remain scaled to one operator, not a heavy enterprise audit process. Logs, gates, and receipts must help the user, not bury the user.

## Evidence posture

This file is intentionally not counted as a ScoutFlow PR decision card. It exists because the U15 mission asked for ContentFlow → ScoutFlow legacy decisions, but the ContentFlow L1 retrospective source was not loaded in this run. Therefore the decision is preserved as a candidate legacy pattern, not as canonical cross-project fact.

## How it appears in ScoutFlow

The pattern is visible indirectly through repeated ScoutFlow boundaries: candidate/not-authority frontmatter, no authority writeback, no true vault write, preview-only proof, human gate language, and source-of-record separation. Those are real patterns in the PR cards, but the cross-project origin needs a separate source lock before promotion.

## Promotion gate

To promote this legacy decision, load the ContentFlow L1 retrospective, map exact source excerpts, and attach PR or document references. Until then, use this file as a retrieval hypothesis only.
