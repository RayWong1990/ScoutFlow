# Token Layers

Import order:

1. `tokens.css`
2. `density-compact.css`
3. `type-weight-heavy.css`

Rules:

- `tokens.css` is the single source of truth for color tokens.
- `density-compact.css` only overrides density-related variables.
- `type-weight-heavy.css` only overrides typography-weight variables.
- Component styles must reference `var(--token-name)` instead of hardcoded hex values.
