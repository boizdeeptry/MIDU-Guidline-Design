## Elevation and Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow | Tinted sections, footer, eyebrow badges |
| 1a (hairline, passive) | 1px `{colors.hairline}` border | Passive dividers, table rules — non-interactive only |
| 1b (hairline, interactive) | 1px `{colors.hairline-strong}` border | `{components.text-input}` and any hairline-only interactive boundary (WCAG 1.4.11 needs ≥3:1 on interactive boundaries; plain `{colors.hairline}` measures only 1.30:1) |
| 2 (soft) | 0 8px 24px rgba(56,75,152,0.10) | Default cards, nav dropdown — shadow is indigo-tinted, never grey |
| 3 (floating) | 0 16px 40px rgba(56,75,152,0.16) | Modals, toasts, mascot cards on tinted grounds |

Shadows always inherit the indigo hue. The nutrient bubbles carry their own painted specular highlight and drop no CSS shadow.

