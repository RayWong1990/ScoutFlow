# T-P1A-012 Receipt-Wiring Single-Point Retro — 2026-05-04

## 1. What Dispatch 08 Tried To Do

`T-P1A-012` 的目标是：

- consume `T-P1A-011C` redacted metadata evidence
- wire safe evidence into the existing receipt / artifact ledger baseline
- avoid new runtime

这次任务明确不是新的 BBDown probe，也不是 media / ffmpeg / ASR lane。

## 2. What Actually Happened

- status: `completed`
- changed files:
  - `services/api/scoutflow_api/metadata_probe_receipt_bridge.py`
  - `services/api/scoutflow_api/models.py`
  - `services/api/scoutflow_api/storage.py`
  - `tests/api/test_jobs_complete.py`
  - `tests/contracts/test_worker_receipt_contract.py`
  - `tests/contracts/test_metadata_probe_receipt_bridge_contract.py`
  - authority writeback files
- tests passed:
  - `python tools/check-docs-redlines.py`
  - `python tools/check-secrets-redlines.py`
  - `python -m pytest tests/contracts -q` -> `68 passed`
  - `python -m pytest tests/api tests/contracts -q` -> `95 passed`
- receipt rows / artifacts:
  - created in tests only
  - no real local runtime receipt rows were created against the shared repo DB
- capture state advancement:
  - happened in tests only
  - no real local runtime capture state was advanced in the shared repo DB

## 3. What This Proves

- the receipt mapping from safe `011C` auth-present metadata evidence into `artifact_assets` works on the current API-side baseline
- artifact ledger validation still catches path / bytes / sha mismatches before insert
- redaction metadata is sufficient for the new safe metadata evidence path
- `metadata_fetch` can be narrowed to safe artifact kinds without breaking existing receipt baseline
- blocked `T-P1A-011` and successful `T-P1A-011C` can be kept semantically separate in code and tests

## 4. What This Does Not Prove

- no media readiness
- no ffmpeg readiness
- no ASR readiness
- no `audio_transcript` readiness
- no broad worker readiness
- no frontend readiness

## 5. Ceremony Tax Check

Was this retro useful enough to keep?

- yes
- Reason: `012` 是第一条真正把 probe evidence 接到 receipt / artifact ledger 的代码路径。没有这篇 retro，后续 `013` 很容易把“tests 里入账成功”误说成“更广泛 runtime readiness”。这次 retro 的价值在于把证据边界重新压回文件里，而不是继续靠聊天记忆。

## 6. Next Gate

patched Dispatch `09` can proceed.

前提是继续保持：

- API/CLI mode preferred
- no frontend expansion
- `probe evidence != receipt ledger != capture state != media/audio readiness`
