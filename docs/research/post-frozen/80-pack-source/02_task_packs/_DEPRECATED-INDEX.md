# Deprecated Dispatch Index — PF-META-01

status: candidate / not-authority
created_at: 2026-05-06

| legacy dispatch | superseded_by | deprecation_reason |
|---|---|---|
| `PF-C0-02` | `../../_PACK-DEFAULTS.md#0-frozen-historical-boundary` | frozen boundary is now inherited from _PACK-DEFAULTS §0; no standalone dispatch is needed |
| `PF-C0-04` | `PF-C0-MERGED-03+04` | preview-only scope merged into successor entry and preview-only scope memo |
| `PF-C0-05` | `PF-C0-MERGED-03+04` | dispatch naming reset belongs inside the successor entry memo |
| `PF-O1-02` | `PF-O1-01R row 1` | true vault write is represented as row 1 in the overflow registry |
| `PF-O1-03` | `PF-O1-01R row 2` | runtime tools are represented as row 2 in the overflow registry |
| `PF-O1-04` | `PF-O1-01R row 3` | browser automation is represented as row 3 in the overflow registry |
| `PF-O1-05` | `PF-O1-01R row 4` | DBvNext and migration are represented as row 4 in the overflow registry |
| `PF-O1-06` | `PF-O1-01R row 5` | full Signal Workbench is represented as row 5 in the overflow registry |

All eight entries are frozen authoring artifacts. They must not be reopened, reordered, or re-executed; later work must use the superseding R-version or shared default reference.
