import systemSpriteUrl from "../../assets/icons/system.svg?url";
import stateSpriteUrl from "../../assets/icons/state.svg?url";
import styles from "./Icon.module.css";

type IconSprite = "system" | "state";

export type IconProps = {
  name: string;
  sprite?: IconSprite;
  className?: string;
  title?: string;
};

const spriteUrlCache = new Map<string, string>();

function toUsableSpriteUrl(url: string): string {
  if (!url.startsWith("data:image/svg+xml")) {
    return url;
  }

  const cached = spriteUrlCache.get(url);
  if (cached) {
    return cached;
  }

  const svgMarkup = decodeURIComponent(url.slice(url.indexOf(",") + 1));
  const blobUrl = URL.createObjectURL(new Blob([svgMarkup], { type: "image/svg+xml" }));
  spriteUrlCache.set(url, blobUrl);
  return blobUrl;
}

const spriteMap: Record<IconSprite, string> = {
  system: toUsableSpriteUrl(systemSpriteUrl),
  state: toUsableSpriteUrl(stateSpriteUrl),
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
