---
status: candidate_not_authority
doc_type: research_matrix
scope: full_80_task_classification
historical_reference_date: 2026-05-06
live_truth_readback_date: 2026-05-08
authority_note: "This file is candidate only. It is not docs/current.md, docs/task-index.md, or execution approval."
near_term_count: 20
overflow_count: 18
reservoir_count: 42
verdict_target: full_80_row_classification_clear
historical_reference_disclaimer: Row classifications below are execution-time candidate routing output only. Live GitHub truth, current authority, and pack supersession must be refreshed before merge.
---

# W3E PF-C0/O1 近端主线执行矩阵

## 结论先行

- 本文按 `PF-C0-06R` source contract 补全为 `80` 行 authored-task 分类矩阵。
- `near_term_mainline = 20`，位于要求的 `20-30` 区间内。
- `overflow = 18`，覆盖 `PF-O1` 与 `PF-GLOBAL`。
- `reservoir / gated_reservoir = 42`，覆盖 `PF-C0` deprecated rows、`PF-C1/C2/C3/C4` 与 `PF-LP` reservoir rows。
- 这里的 `near_term_mainline` 是 pack-routing 口径，不等于“现在全部立即执行”。它表示 source inventory 和 suggested order 认定的近端主线集合。

## Classification Rules

- `near_term_mainline`: `PF-C0-01/03/06`, `PF-LP-01..13`, and the earliest `4` `PF-C1` tasks supported by suggested execution order.
- `overflow`: `PF-O1` hold-lane rows plus `PF-GLOBAL` permanent overflow rows.
- `reservoir`: `PF-C3` rows explicitly marked reservoir by pack index.
- `gated_reservoir`: `PF-C0` deprecated rows, `PF-C1` non-canary rows, `PF-C2/C4` rows, and `PF-LP-14..18`.

## 80-row classification matrix

| code | cluster | priority | open_after_state | status | reason |
|---|---|---|---|---|---|
| `PF-C0-01` | `PF-C0/PF-O1` | `🔴 blocker` | `live_authority_readback_after_PR194` | `near_term_mainline` | successor entry authored task; thin opening line before localhost preview and later proof packs |
| `PF-C0-02` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `gated_reservoir` | deprecated by PF-META replacement and stop-line; keep as historical/reference row, not current near-term mainline |
| `PF-C0-03` | `PF-C0/PF-O1` | `🟠 high` | `live_authority_readback_after_PR194` | `near_term_mainline` | successor entry authored task; thin opening line before localhost preview and later proof packs |
| `PF-C0-04` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `gated_reservoir` | deprecated after merged successor memo path; retain only as lineage/reference row |
| `PF-C0-05` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `gated_reservoir` | deprecated dispatch naming reset row; current successor naming lives in superseding surfaces, not this row |
| `PF-C0-06` | `PF-C0/PF-O1` | `🟠 high` | `live_authority_readback_after_PR194` | `near_term_mainline` | successor entry authored task; thin opening line before localhost preview and later proof packs |
| `PF-C1-01` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `near_term_mainline` | suggested execution order opens 4-6 C1 tasks immediately after localhost preview; this canary selector is part of that first usable slice |
| `PF-C1-02` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `near_term_mainline` | suggested execution order supports an early C1 prep slice; topic-card-lite contract is part of the first 4-task canary bundle |
| `PF-C1-03` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `near_term_mainline` | suggested execution order supports an early C1 prep slice; historical asset extraction feeds the first proof pair |
| `PF-C1-04` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `near_term_mainline` | suggested execution order supports an early C1 prep slice; transformer candidate is the first code-bearing proof step after LP |
| `PF-C1-05` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-06` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-07` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-08` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-09` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-10` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-11` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C1-12` | `PF-C1` | `🟡 medium` | `preview_only_localhost_ready` | `gated_reservoir` | open_after_state=preview_only_localhost_ready keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-01` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-02` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-03` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-04` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-05` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-06` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-07` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-08` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-09` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-10` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-11` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C2-12` | `PF-C2` | `🟡 medium` | `c1_partial_or_pass` | `gated_reservoir` | open_after_state=c1_partial_or_pass keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C3-01` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C3-02` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C3-03` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C3-04` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C3-05` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C3-06` | `PF-C3` | `🔵 reservoir` | `parallel_prep_after_successor_entry` | `reservoir` | pack index marks PF-C3 as reservoir/compression support, not current mainline |
| `PF-C4-01` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-02` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-03` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-04` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-05` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-06` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-07` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-C4-08` | `PF-C4` | `🔵 reservoir` | `c1_c2_pass_or_strong_partial` | `gated_reservoir` | open_after_state=c1_c2_pass_or_strong_partial keeps this task behind preview/proof gates; not current near-term mainline |
| `PF-GLOBAL-01` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-02` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-03` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-04` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-05` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-06` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-07` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-08` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-09` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-10` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-11` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-GLOBAL-12` | `PF-overflow/global-reservoir` | `⚪ permanent_overflow` | `never_auto_open` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-LP-01` | `PF-localhost-preview` | `🔴 blocker` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-02` | `PF-localhost-preview` | `🔴 blocker` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-03` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-04` | `PF-localhost-preview` | `🔴 blocker` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-05` | `PF-localhost-preview` | `🔴 blocker` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-06` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-07` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-08` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-09` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-10` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-11` | `PF-localhost-preview` | `🟡 medium` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-12` | `PF-localhost-preview` | `🟡 medium` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-13` | `PF-localhost-preview` | `🟠 high` | `successor_entry_ready` | `near_term_mainline` | pack inventory marks localhost preview as near-term and suggested execution order places it directly after PF-C0/O1 |
| `PF-LP-14` | `PF-localhost-preview` | `🔵 reservoir` | `successor_entry_ready` | `gated_reservoir` | row-level pack index marks this as reservoir, so it stays outside the current 24h near-term slice even though the pack itself is near-term |
| `PF-LP-15` | `PF-localhost-preview` | `🔵 reservoir` | `successor_entry_ready` | `gated_reservoir` | row-level pack index marks this as reservoir, so it stays outside the current 24h near-term slice even though the pack itself is near-term |
| `PF-LP-16` | `PF-localhost-preview` | `🔵 reservoir` | `successor_entry_ready` | `gated_reservoir` | manual localhost evidence note depends on implementation already landing; it is not the same-layer near-term mainline step |
| `PF-LP-17` | `PF-localhost-preview` | `🔵 reservoir` | `successor_entry_ready` | `gated_reservoir` | row-level pack index marks this as reservoir and it reads like post-implementation readback rather than the first 24h mainline slice |
| `PF-LP-18` | `PF-localhost-preview` | `🔵 reservoir` | `successor_entry_ready` | `gated_reservoir` | closeout/handoff row is authority-safe late-packaging, not the same-layer near-term mainline step |
| `PF-O1-01` | `PF-C0/PF-O1` | `🔴 blocker` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-O1-02` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-O1-03` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-O1-04` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-O1-05` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |
| `PF-O1-06` | `PF-C0/PF-O1` | `⚪ deprecated` | `live_authority_readback_after_PR194` | `overflow` | overflow or permanent-overflow lane; stays out of near-term product execution even when documented now |

## Count Check

- `near_term_mainline = 20`
- `overflow = 18`
- `reservoir/gated_reservoir = 42`
- `20 + 18 + 42 = 80`

## Self-flag

- This matrix keeps deprecated `PF-C0-02/04/05` as historical/reference rows, not current near-term mainline.
- `PF-LP-14` through `PF-LP-18` stay outside the 24h near-term slice because their row-level source signals are reservoir / post-implementation / closeout shaped.
- The `near_term_mainline = 20` threshold is reached by the 3 live `PF-C0` successor-entry rows, 13 non-reservoir `PF-LP` rows, and the earliest 4 `PF-C1` canary/proof-prep rows permitted by suggested execution order.
