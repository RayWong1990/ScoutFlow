---
pattern_id: candidate_not_authority_frontmatter
title: "Candidate / not-authority frontmatter"
status: candidate / decision-pattern / not-authority
authority: not-authority
related_prs: [161, 162, 165, 166, 168, 169, 170, 171, 172, 175, 177, 179, 180, 182, 188, 190, 191, 196]
---

# Candidate / not-authority frontmatter

## Definition

Mark research, planning, preview, and atlas material as candidate/not-authority so future readers do not mistake it for canonical state.

## Why this pattern exists

ScoutFlow's project memory has a recurring failure mode: a merged artifact can look more final than it really is. The pattern library prevents this by turning repeated governance moves into explicit retrieval handles. A reader can search for a pattern and find the PRs where the pattern appeared, the decisions that made it useful, and the limits that prevent over-claiming.

## Recognition signals

- The PR body uses language such as candidate-only, docs-only, preview-only, no authority writeback, partial, blocked, or not execution approved.
- A later amendment narrows a previous claim or records a scope deviation.
- A chain of PRs needs topology: replacement, coverage, closeout, repair, or rollback.
- A pass/fail verdict is too coarse and needs a more honest state label.

## Operating rule

Use this pattern when a future PR needs the same decision shape. The rule is not to copy the wording blindly. The rule is to preserve the distinction between evidence, authority, and readiness. A candidate can be useful without becoming canonical. A partial result can be successful without being full proof. A merged implementation can remain bounded if a later amendment records the risk.

## Related PRs in this package

#161, #162, #165, #166, #168, #169, #170, #171, #172, #175, #177, #179, #180, #182, #188, #190, #191, #196



## Failure mode prevented

Without this pattern, the project tends to drift toward smooth narratives: every merge looks like progress, every closeout looks complete, and every preview looks like runtime proof. The pattern forces retrieval of the caveat. It also gives future prompts a compact vocabulary, so a new audit can say “apply `introduced_vs_exposed_attribution`” instead of re-explaining the entire history.

## Checklist

1. Identify source PRs and never invent missing PR numbers.
2. Write the candidate/not-authority boundary before synthesis.
3. Separate the PR that introduced a condition from the PR that exposed it.
4. Attach amendments only when the relationship is visible in evidence.
5. Leave registry-based links blank when the registry is not loaded.
