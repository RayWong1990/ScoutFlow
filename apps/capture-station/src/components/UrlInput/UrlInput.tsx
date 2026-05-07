import styles from "./UrlInput.module.css";

export type UrlInputProps = {
  id: string;
  label: string;
  value: string;
  placeholder?: string;
  mode?: "default" | "focus" | "error";
  errorMessage?: string;
  onChange?: (value: string) => void;
  readOnly?: boolean;
};

export default function UrlInput({ errorMessage, id, label, mode = "default", onChange, placeholder, readOnly = false, value }: UrlInputProps) {
  const classes = [styles.field, mode === "focus" ? styles.focus : "", mode === "error" ? styles.error : ""].filter(Boolean).join(" ");

  return (
    <label className={styles.root} htmlFor={id}>
      <span className={styles.label}>{label}</span>
      <input
        id={id}
        className={classes}
        type="url"
        value={value}
        readOnly={readOnly}
        aria-invalid={mode === "error"}
        placeholder={placeholder}
        onChange={(event) => onChange?.(event.target.value)}
      />
      {errorMessage ? <p className={styles.message}>{errorMessage}</p> : null}
    </label>
  );
}
