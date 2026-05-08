import CaptureIdChip from "../../components/CaptureIdChip/CaptureIdChip";
import Button from "../../components/Button/Button";
import Icon from "../../components/Icon/Icon";
import Modal from "../../components/Modal/Modal";
import PanelCard from "../../components/PanelCard/PanelCard";
import StateBadge from "../../components/StateBadge/StateBadge";
import SurfaceFrame, { SurfaceDivider, SurfaceSection } from "../../components/SurfaceFrame/SurfaceFrame";
import { type AsyncState, type W2CRuntimeValue, useW2CRuntime } from "../../lib/w2c-runtime";
import styles from "./VaultCommit.module.css";

function useVaultRuntimeOrNull(): W2CRuntimeValue | null {
  try {
    return useW2CRuntime();
  } catch {
    return null;
  }
}

function mapStatusBadge<T>(state: AsyncState<T>, options: { ready: string; loading: string; idle: string }) {
  if (state.status === "loading") {
    return { tone: "loading" as const, label: options.loading };
  }

  if (state.status === "error") {
    return { tone: "error" as const, label: state.error?.code ?? "route_error" };
  }

  if (state.status === "success") {
    return { tone: "ready" as const, label: options.ready };
  }

  return { tone: "idle" as const, label: options.idle };
}

export default function VaultCommit() {
  const runtime = useVaultRuntimeOrNull();
  const dryRunState = runtime?.vaultCommitDryRun;
  const configState = runtime?.bridgeVaultConfig;
  const healthState = runtime?.bridgeHealth;
  const currentCaptureId = runtime?.currentCaptureId ?? null;
  const configBadge = runtime
    ? mapStatusBadge(runtime.bridgeVaultConfig, {
        ready: runtime.bridgeVaultConfig.data?.error ? runtime.bridgeVaultConfig.data.error.code : "config_loaded",
        loading: "config_loading",
        idle: "config_idle",
      })
    : { tone: "blocked" as const, label: "runtime_missing" };
  const dryRunBadge =
    !runtime ? { tone: "blocked" as const, label: "runtime_missing" } :
    dryRunState?.status === "success" && dryRunState.data?.dry_run ? { tone: "candidate" as const, label: "dry_run_only" } :
    mapStatusBadge(runtime.vaultCommitDryRun, {
      ready: "route_returned",
      loading: "dry_run_loading",
      idle: currentCaptureId ? "ready_to_probe" : "no_capture",
    });
  const trueWriteReason = healthState?.data?.blocked_by?.join(", ") || "write_disabled";
  const overflowHoldCopy = "true_vault_write / runtime_tools / browser_automation / dbvnext_migration / full_signal_workbench";

  return (
    <SurfaceFrame title="入库提交状态集" description="W2C 里的 vault-commit 只允许 dry-run probe，true write 永远保持 visible-but-disabled。">
      <SurfaceSection title="状态: gate / config">
        <PanelCard title="Vault commit gate" eyebrow="vault-commit" aside={<StateBadge tone={configBadge.tone} label={configBadge.label} />}>
          {!runtime ? (
            <p>当前是 isolated render，commit surface 只保留 blocked shell，不伪造 runtime 成功。</p>
          ) : configState?.status === "loading" ? (
            <p>正在读取 bridge config，true write gate 还未确认。</p>
          ) : configState?.status === "error" ? (
            <div className={styles.stack}>
              <p>配置请求失败，当前不能把 commit surface 说成已就绪。</p>
              <p className={styles.messageError}>
                {configState.error?.code ?? "route_error"}: {configState.error?.message ?? "Vault config route failed."}
              </p>
            </div>
          ) : configState?.data ? (
            <div className={styles.stack}>
              <dl className={styles.grid}>
                <div className={styles.contents}>
                  <dt>capture_id</dt>
                  <dd>{currentCaptureId ? <CaptureIdChip value={currentCaptureId} /> : "none"}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>vault_root</dt>
                  <dd>{configState.data.vault_root ?? "unset"}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>preview_enabled</dt>
                  <dd>{String(configState.data.preview_enabled)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>write_enabled</dt>
                  <dd>{String(configState.data.write_enabled)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>blocked_by</dt>
                  <dd>{healthState?.data?.blocked_by?.join(", ") || "none"}</dd>
                </div>
              </dl>
              {configState.data.error ? (
                <p className={styles.messageError}>
                  {configState.data.error.code}: {configState.data.error.message}
                </p>
              ) : null}
              <p className={styles.helper}>Overflow hold lanes: {overflowHoldCopy}</p>
            </div>
          ) : (
            <p>配置尚未加载。</p>
          )}
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: manual dry-run only">
        <PanelCard title="Dry-run contract" eyebrow="vault-commit" aside={<StateBadge tone={dryRunBadge.tone} label={dryRunBadge.label} />}>
          <div className={styles.stack}>
            <p>这块 surface 允许手动触发 dry-run route，但不允许把它解释成真实 vault write。</p>
            <div className={styles.actions}>
              <Button
                icon={<Icon name="dry-run" />}
                variant="secondary"
                onClick={() => void runtime?.runVaultCommitDryRun()}
                disabled={!runtime?.currentCaptureId || runtime.vaultCommitDryRun.status === "loading"}
              >
                Run dry-run check
              </Button>
              <Button
                icon={<Icon name="blocked" />}
                variant="blocked"
                disabled
                title={`true write blocked: ${trueWriteReason}`}
              >
                Commit to vault (disabled)
              </Button>
            </div>
            {!currentCaptureId ? <p className={styles.helper}>先创建 capture，dry-run route 才有真实目标。</p> : null}
            {runtime?.isVaultWriteBlocked ? (
              <p className={styles.messageError}>write_enabled=false 仍是硬门，手动 dry-run 也不会解禁 true write。</p>
            ) : null}
          </div>
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: dry-run result">
        <PanelCard title="Dry-run result" eyebrow="vault-commit">
          {!runtime ? (
            <p>runtime 缺失时不显示 commit 成功，只保留 blocked shell。</p>
          ) : dryRunState?.status === "loading" ? (
            <p>正在调用 `/captures/{'{capture_id}'}/vault-commit` dry-run route，结果出来前不预写 success copy。</p>
          ) : dryRunState?.status === "error" ? (
            <div className={styles.stack}>
              <Modal
                title="Dry-run blocked"
                tone="fail"
                footer={
                  <Button variant="blocked" disabled>
                    True write still blocked
                  </Button>
                }
              >
                <p>这次是 route error，不是 commit 成功。</p>
                <p className={styles.messageError}>
                  {dryRunState.error?.code ?? "route_error"}: {dryRunState.error?.message ?? "Vault commit dry-run failed."}
                </p>
              </Modal>
              <p className={styles.helper}>若 config / preview 本身失败，这里继续保持 blocked 或 error copy，不伪造已写入。</p>
            </div>
          ) : dryRunState?.status === "success" && dryRunState.data ? (
            <div className={styles.stack}>
              <Modal
                title="Dry-run route returned preview-only truth"
                tone="promote"
                footer={
                  <Button variant="blocked" disabled>
                    committed=false
                  </Button>
                }
              >
                <p>Route 已返回，但结果仍是 dry-run-only。它只验证 target preview / guard posture，不代表 vault 已写入。</p>
              </Modal>
              <dl className={styles.grid}>
                <div className={styles.contents}>
                  <dt>capture_id</dt>
                  <dd>{dryRunState.data.capture_id}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>dry_run</dt>
                  <dd>{String(dryRunState.data.dry_run)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>committed</dt>
                  <dd>{String(dryRunState.data.committed)}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>target_path</dt>
                  <dd>{dryRunState.data.target_path ?? "none"}</dd>
                </div>
                <div className={styles.contents}>
                  <dt>error_code</dt>
                  <dd>{dryRunState.data.error?.code ?? "none"}</dd>
                </div>
              </dl>
              {dryRunState.data.error ? (
                <p className={styles.helper}>
                  route message: {dryRunState.data.error.message}
                </p>
              ) : null}
            </div>
          ) : (
            <p>还没有手动触发 dry-run；在此之前，这个 surface 只保持 candidate / write-disabled posture。</p>
          )}
        </PanelCard>
      </SurfaceSection>

      <SurfaceDivider />

      <SurfaceSection title="状态: 知识飞轮提示">
        <PanelCard title="知识飞轮提示" eyebrow="vault-commit">
          <p>ScoutFlow 只把干净 Markdown 交付到 raw vault inbox；enrich、wiki link backfill 和知识飞轮仍留在 Obsidian 内，不在 W2C 当前面解禁。</p>
        </PanelCard>
      </SurfaceSection>
    </SurfaceFrame>
  );
}
