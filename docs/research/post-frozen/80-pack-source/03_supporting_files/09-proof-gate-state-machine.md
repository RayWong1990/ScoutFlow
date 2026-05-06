# Proof Gate State Machine

```mermaid
stateDiagram-v2
  [*] --> successor_entry_gate
  successor_entry_gate --> preview_only_localhost: C0/O1 pass
  preview_only_localhost --> real_url_topic_card_proof: markdown loop pass
  real_url_topic_card_proof --> manual_RAW_handoff_proof: >=2 useful canaries
  manual_RAW_handoff_proof --> controlled_hardening: RAW intake + script seed pass
  controlled_hardening --> future_runtime_consideration: visual/hardening pass + human gate

  preview_only_localhost --> partial_or_fail: placeholder only / no copy-download
  real_url_topic_card_proof --> partial_or_fail: no human usefulness
  manual_RAW_handoff_proof --> partial_or_fail: second inbox behavior
  controlled_hardening --> partial_or_fail: checklist only / no visual verdict
  partial_or_fail --> successor_entry_gate: rewrite smaller
```
