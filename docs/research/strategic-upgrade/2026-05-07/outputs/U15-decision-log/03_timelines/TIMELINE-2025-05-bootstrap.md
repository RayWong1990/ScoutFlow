---
title: "2025-05 bootstrap timeline"
status: candidate / timeline / not-authority
authority: not-authority
---

# 2025-05 bootstrap timeline

This timeline view is sorted by `merged_at`, not by PR number. That distinction matters because several PRs in the #199-#230 window were created and merged in tight batches where number order and merge order can differ. The timeline is a retrieval surface, not a canonical chronology replacement.

| merged_at | PR | cluster | introduced/exposed | title |
|---|---:|---|---|---|
| 2025-05-04T21:29:10Z | #1 | C00 Bootstrap / Dispatch Import | introduced | feat(dispatch): import Dispatch-002 audit bundle and smoke script |

```mermaid
flowchart TD
    P1["#1 feat(dispatch): import Dispatch-002 au"]
```

## Reading note

Read candidate and authority-sync PRs differently. Candidate PRs introduce planning or evidence surfaces; authority-sync PRs may write canonical wording but still often preserve `NOT_EXECUTION_APPROVED`. Amendment PRs should be read as corrections to the historical record, not as blame assignment to the latest PR.
