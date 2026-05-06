# Kill Switch List

| ID | Trigger | Action |
|---|---|---|
| KS-FROZEN-REOPEN | Any task reopens Dispatch126-176 | Stop and rewrite task |
| KS-DOCS-AS-PROOF | Candidate doc claims proof | Downgrade to shape_only |
| KS-PREVIEW-FAKE-CLOSURE | Preview/dry-run claims closed loop | Mark partial/fail |
| KS-SECOND-INBOX | RAW notes pile up without intake/seed | Fail C2 |
| KS-RUNTIME-CREEP | Task enables runtime tools | Move to O1 |
| KS-TRUE-WRITE-CREEP | Task writes vault files | Stop unless explicit true_write_approval |
| KS-VISUAL-CHECKLIST-ONLY | Checklist claims visual proof without screenshots/human verdict | Fail C4 visual |
| KS-OVEROBJECTIFICATION | Adds full objects before proof | Route to C3 compression/O1 |
