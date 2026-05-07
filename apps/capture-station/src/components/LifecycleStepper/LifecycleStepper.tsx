import Icon from "../Icon/Icon";
import styles from "./LifecycleStepper.module.css";

export type LifecycleStepStatus = "idle" | "active" | "done";

export type LifecycleStep = {
  label: string;
  status: LifecycleStepStatus;
};

export type LifecycleStepperProps = {
  steps: LifecycleStep[];
  ariaLabel: string;
};

export default function LifecycleStepper({ ariaLabel, steps }: LifecycleStepperProps) {
  return (
    <ol className={styles.root} aria-label={ariaLabel}>
      {steps.map((step, index) => {
        const classes = [styles.item, step.status === "active" ? styles.active : "", step.status === "done" ? styles.done : ""]
          .filter(Boolean)
          .join(" ");

        return (
          <li key={step.label} className={classes}>
            <span className={styles.marker}>
              {step.status === "done" ? <Icon sprite="state" name="success" /> : <span>{index + 1}</span>}
            </span>
            <span className={styles.label}>{step.label}</span>
          </li>
        );
      })}
    </ol>
  );
}
