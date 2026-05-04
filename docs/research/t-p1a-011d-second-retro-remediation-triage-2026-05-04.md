# T-P1A-011D Second Retro / Remediation Triage — 2026-05-04

> 状态：`complete / docs-only second retro triage`。
> 作用：基于 GitHub 真相、`T-P1A-011/011B/011C` repo-side reports、PR `#26/#27`、以及外部 Opus probe/remediation drafts，收口 `07.2 / 07.3 / 07.4 / patched 08 / patched 09` 的执行边界。

## 1. GitHub Truth

当前已确认的 GitHub / repo 真相是：

```text
T-P1A-011 = no-auth probe blocked / preflight repair input
T-P1A-011B = manual-auth QR local-only gate done
T-P1A-011C = auth-present metadata probe done with platform_result=ok
```

补充事实：

- PR `#26` 已合并：`T-P1A-011` preflight repair + `T-P1A-011B` gate hardening
- PR `#27` 已合并：`T-P1A-011C` auth-present metadata probe
- Dispatch 06 对应的 no-auth probe 没有成功，成功证据来自 `T-P1A-011C`

本报告明确不写成“06 成功”。正确口径是：`06 remained blocked; 011C provided the successful evidence.`

## 2. Opus Findings Triage

| Opus claim | accept / narrow / postpone / reject | reasoning | next dispatch |
|---|---|---|---|
| H4 meta-governance gap | accept | `docs/` 当前确实缺一个最小 retro / reversal / scope-shrink 落点；但 pre-08 只补最小 scaffold，不开重治理包 | `07.2` |
| H2 over-governance weakened by high multi-agent switching | narrow | user 已明确多 agent 切换频率高，4-layer + ledger discipline 不应被推翻；只接受“补最小 retro，拒绝大包整改”这部分收缩建议 | `07.2` |
| BBDown / vendor / legal signals candidate-only | postpone | 这些外部事实对后续路径有价值，但在当前 repo 内仍是 candidate-only；未验证前不能进入 authority | `07.5` optional |
| 19-file remediation too large | accept | 当前最合理的 pre-08 收缩是 `011D/011E/011F/011G` 四步，不把整改扩大成新主线 | `07.2` / `07.3` |
| velocity gate cancelled before 08 | accept | `011C` 已经给出真实 `platform_result=ok` metadata evidence；08 是 evidence-consumption，不应再被 velocity gate 卡住 | `08` |
| minimal retro scaffold | accept | retro 不该永远后推，但当前只做 README + 3 templates + week-1，保持“small retrospective scaffold” | `07.2` |
| receipt-wiring retro after 08 | accept | receipt retro 需要真实 08 产物做输入，放在 08 前只会空转 | `08.1` |

## 3. Numbering Repair

```text
T-P1A-012 remains Dispatch 08.
T-P1A-013 remains Dispatch 09.
Retro/remediation before Dispatch 08 uses T-P1A-011D/E/F/G/H.
```

本次修复同时锁定一个简单规则：`012/013` 不再被 pre-08 retro / remediation 占用。

## 4. Dispatch Repair Plan

推荐顺序如下：

```text
07.2 = T-P1A-011E minimal retro skeleton
07.3 = T-P1A-011F patch Dispatch 08/09 prompts
07.4 = T-P1A-011G read-only sidecar review of 07.x + patched 08/09
07.5 = T-P1A-011H optional candidate-only legal/vendor notes
08 = patched T-P1A-012 evidence-consumption receipt wiring
08.1 = T-P1A-012R receipt-wiring retro after 08
09 = patched T-P1A-013 Trust Trace minimal surface
```

## 5. Boundary Statement

当前仍未批准：

- new live BBDown
- new `BBDown -info`
- media download
- ffmpeg
- ASR
- browser profile
- QR/login
- receipt/capture state until Dispatch 08
- frontend/workers until specific dispatch approval
- legal/vendor authority claims

## 6. Why This Order

`07.1 -> 07.4` 的顺序不是形式化流程，而是为了避免把 stale premise 带进 code-bearing `08`：

- `07.1` 先把 GitHub truth、编号修复、Opus triage 固定下来
- `07.2` 只补最小 retro routine，不把 pre-08 范围膨胀成治理包
- `07.3` 再修 Dispatch 08/09 的前提，确保它们从 `011C` 而不是 blocked `011` 出发
- `07.4` 最后做只读侧审，检查 repo-side writeback 与 patched prompts 是否还存在 drift

## 7. Recommended Next Dispatch

如果 user 继续授权，下一步默认是：

```text
patched Dispatch 08 = T-P1A-012 evidence-consumption receipt wiring
```

`07.5` 只在 user 明确要求先开 candidate-only legal/vendor lane 时才插入。
