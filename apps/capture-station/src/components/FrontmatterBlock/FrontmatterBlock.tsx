import styles from "./FrontmatterBlock.module.css";

export type FrontmatterField = {
  label: string;
  value: string;
};

export type FrontmatterBlockProps =
  | {
      mode: "code";
      content: string;
      fields?: never;
    }
  | {
      mode: "fields";
      fields: FrontmatterField[];
      content?: never;
    };

export default function FrontmatterBlock(props: FrontmatterBlockProps) {
  if (props.mode === "code") {
    return (
      <pre className={styles.root}>
        <code>{props.content}</code>
      </pre>
    );
  }

  return (
    <div className={styles.root}>
      <dl className={styles.fields}>
        {props.fields.map((field) => (
          <div key={field.label} style={{ display: "contents" }}>
            <dt>{field.label}</dt>
            <dd>{field.value}</dd>
          </div>
        ))}
      </dl>
    </div>
  );
}
