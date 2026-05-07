# PF-C4-01 lane closeout

```yaml
status: candidate_closeout_not_authority
lane: PF-C4-01
phases: 4/4
dispatches: 20/20
pr_strategy: single_pr_recommended
runtime_unlock: false
migration_unlock: false
authority_write: false
```

## 1. Lane summary

PF-C4-01 按 commander prompt 的单 lane、单 PR 路线完成了 `apps/capture-station/**` 内的本地前端 bootstrap 与 P7 surface 翻译，没有触碰 authority 文件，没有触碰 `services/api/migrations/**`，也没有引入 BBDown live、yt-dlp、ffmpeg、ASR、browser automation 或 true vault write。最终交付不是把 P7 raw HTML 直接搬进运行时，而是把它翻译成 React TSX + CSS Modules + token overlays + SVG sprite 引用的工作站壳层。应用入口现在以 `src/App.tsx` 为导航壳，`src/components/AppShell/**` 承担 00-app-shell 的工作站总览，剩余 12 个 surface 通过导航切换进入，对应 P7 的 `01` 到 `12`。

Phase 1 先完成了 bootstrap 探测。锁策略被确认是 `pnpm`，`pnpm install --frozen-lockfile` 能直接通过，TypeScript、Vitest、Vite build 也都能在初始基线上运行。唯一初始故障是旧 placeholder 测试中的 `any` 触发 lint fail，这不是环境问题，而是 repo 内历史占位实现的问题，因此按 PF-C4-01 的正当 scope 直接用“新 surface 替换旧占位”的方式修复，而不是给旧壳子继续打补丁。对应的 narrow report 已写入 `docs/research/post-frozen/frontend-local-bootstrap-repair.md`。

Phase 2 把 P7 的 token 和 icon 体系迁入本地前端，并建立了 15 个基础组件骨架。`tokens.css`、`density-compact.css`、`type-weight-heavy.css` 被按规定顺序导入，`system.svg` 与 `state.svg` 作为 sprite 保留，`Icon` 组件统一走 `<use href="...#icon-id">` 语义。按钮、面板、状态徽标、sync 徽标、stepper、evidence table、tag list、capture id chip、topic card、modal、governance tooltip、live pulse、frontmatter block、promote gate、url input 等骨架都落到了 `src/components/**`。这一步的重点不是“像素级照抄 P7 class name”，而是把组件语义压实到项目自己的 production naming 上，同时继续只用 token 变量，不在 `tokens.css` 外写硬编码 hex。

Phase 3 完成了 13 个 surface 的 TSX 翻译。`00-app-shell` 以 `AppShellOverview` 呈现 4 区块工作站总览；`01-url-bar` 保留 empty/focus/validating/error/history-open 五态；`02-live-metadata` 保留长标题、数字高权重、标签溢出、live counter、thumbnail placeholder 五态；`03-capture-scope` 保留 start / complete / governance tooltip 三态；`04-trust-trace` 保留 DOM filter / timeline / error-path 三态，并对图谱、时间轴、错误高亮各自保留诚实 TODO；`05-vault-preview` 保留 idle / ready / blocked / frontmatter-expanded / copy-action；`06-vault-commit` 保留 standard / tooltip / modal-pass / modal-fail / batch；`07-topic-card-lite` 保留新闻、视频、多信号、证据指针、双卡对比；`08-topic-card-vault` 保留 default / aggregated / promote / promote-modal / sync；`09-signal-hypothesis`、`10-capture-plan`、`11-density-spec`、`12-type-spec` 也都已经按 P7 rough surface 收口为可渲染的 React 页。这里特别注意没有把 PNG 当成 pixel-perfect spec，而是保持层级、扫描路径、状态语法和 token discipline。

Phase 3 的 cross-surface consistency 也已经做了统一整理。中文 UI 文案保留，`sync-badge` 在 `TopicCardVault` 中保留了 `synced / pending / external-changed` 三态，且继续与 `state.svg#icon-success / icon-warning / icon-focus` 配对，没有塌缩成二元 saved/not-saved。颜色全部通过 token 变量流转，密度和字重覆盖继续保持为全局 overlay 文件，而不是散落在组件 prop drilling 里。`DensitySpec` 与 `TypeSpec` 通过嵌入式 overview reference 证明：V3 compact 和 V4 weight-heavy 都是通过 token 层组合出来的，不需要另写一套 IA。

## 2. Honest TODO and boundary notes

这条 lane 没有伪装自己解决了 P7 明确留给后续的动态接线问题。四个 TODO placeholder 仍然诚实存在，而且都被显式标注为后续工作，不被伪造成“已经完成的图谱/缩略图/时间轴/错误高亮”。`LiveMetadata` 里的 thumbnail 区块仍是 `data-todo="thumbnail-fetch"` 的占位；`TrustTrace` 里的 graph、timeline、error-path 仍是三个独立占位区，并在 JSX 注释中保留了 `TODO P1/P2` 说明。这是符合 prompt §7 第 4 项要求的，防止把未选型的 vendor、未接线的 runtime 数据，或者未决定的 D3/cytoscape 方案偷偷塞进当前 lane。

另一个关键诚实点是“旧候选壳层的处理方式”。PF-C4-01 并不是在旧 `FourPanelShell`、旧 `*Panel.tsx`、旧 `TopicCard*Candidate.tsx` 上继续叠加补丁，而是明确把这些 placeholder/candidate 壳层视为被当前 lane 取代的旧实现，并在同一受控 `apps/capture-station/**` 范围内删除。由于仓库 redline 工具会对 `apps/**` 的 tracked diff 做 scope 审核，本轮额外写了一份 `docs/research/post-frozen/PF-C4-01/receipts/pf-c4-01-app-scope-note-2026-05-07.md`，逐路径记录哪些 app 文件被新增、替换或删除，以及这件事为什么仍然属于 PF-C4-01 授权，而不是越界重构。

## 3. Dispatch verdicts

- P1-01 bootstrap-repair: `clear`
- P2-01 tokens scaffold: `clear`
- P2-02 icons scaffold: `clear`
- P2-03 component scaffold: `clear`
- P3-00 app shell: `clear`
- P3-01 URL bar: `clear`
- P3-02 live metadata: `clear`
- P3-03 capture scope: `clear`
- P3-04 trust trace: `clear`
- P3-05 vault preview: `clear`
- P3-06 vault commit: `clear`
- P3-07 topic card lite: `clear`
- P3-08 topic card vault: `clear`
- P3-09 signal / hypothesis: `clear`
- P3-10 capture plan: `clear`
- P3-11 density spec: `clear`
- P3-12 type spec: `clear`
- P3-CC cross-surface consistency check: `clear`
- P4-01 verification bundle: `clear`
- P4-02 closeout + checkpoint: `clear`

本次没有触发自主 amend。没有 silent flexibility。没有触碰 authority 文件。没有把 candidate 文档写成 final authority，也没有把 local-only raw vault 路径写入 repo 外部。

## 4. Verification and residual risk

最终本地验证结果如下：`pnpm run typecheck` 通过，`pnpm run lint` 通过，`pnpm run test` 通过（5 个测试文件，26 个测试），`pnpm run build` 通过。`python3 tools/check-secrets-redlines.py` 通过，`git diff --check` 通过。`rg` 检查 `apps/capture-station/src/**/*.css` 中除 `tokens.css` 外的 hex 硬编码为 0 命中，说明 token 单源要求成立。`pnpm run dev` 的本地服务能够在 `127.0.0.1:4173` 响应 `HTTP 200`，证明开发服务器可起；但由于当前 lane 的 boundary 明确不允许 browser automation，本次没有使用 Playwright 或 in-app browser 去做自动化视觉巡检，也没有给出“已人工浏览器终判”的结论。这个限制需要在后续人工审阅或外审阶段补上。

所以当前 closeout 的真实口径是：PF-C4-01 已经完成“本地前端 bootstrap + P7 reference scaffold + 13 surface TSX translation + build/test/lint/typecheck green + boundary preserved”的候选交付，已经 ready for user audit，但仍不是 runtime approval，不是 migration approval，不是真写 vault approval，也不是视觉终局判决。下一步适合按 prompt §5 的默认路径走单 PR，随后由用户/外审决定直接 merge、amend 后 merge，还是继续提审。
