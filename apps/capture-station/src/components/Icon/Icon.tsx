import systemSpriteUrl from "../../assets/icons/system.svg";
import stateSpriteUrl from "../../assets/icons/state.svg";
import styles from "./Icon.module.css";

type IconSprite = "system" | "state";

export type IconProps = {
  name: string;
  sprite?: IconSprite;
  className?: string;
  title?: string;
};

const spriteMap: Record<IconSprite, string> = {
  system: systemSpriteUrl,
  state: stateSpriteUrl,
};

export default function Icon({ name, sprite = "system", className, title }: IconProps) {
  const href = `${spriteMap[sprite]}#icon-${name}`;
  const classes = [styles.icon, styles.decorative, className].filter(Boolean).join(" ");

  if (title) {
    return (
      <svg className={classes} role="img" aria-label={title}>
        <title>{title}</title>
        <use href={href} />
      </svg>
    );
  }

  return (
    <svg className={classes} aria-hidden="true">
      <use href={href} />
    </svg>
  );
}
