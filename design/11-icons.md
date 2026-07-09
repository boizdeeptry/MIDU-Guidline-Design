## Icons

No icon system existed before this revision — a real gap the moment any nav, form, or social-share row extends past the current landing page.

- **Library**: [Lucide](https://lucide.dev) — round line-cap/line-join extends the "no sharp corners" rule already governing buttons, cards, and chips.
- **Style**: outline only, 2px stroke, round joins/caps. Never filled/solid or duotone — filled shapes belong to MIGI's illustration world; this preserves the illustration-vs-chrome boundary the Do/Don't section already draws for black outlines.
- **Sizes**: `icon-sm` 16px (inline with `{typography.body-sm}`/`{typography.caption}`) · `icon-md` 20px (default; nav, buttons, `{typography.body}`) · `icon-lg` 24px (standalone tap targets, empty-state accents). Icons under `{spacing.touch-target-min-decorative}` get a padded invisible hit area per Accessibility.
- **Color**: `{colors.ink}` on light surfaces, `{colors.on-primary}` on gradient/dark surfaces, `{colors.primary}` for interactive/link icons. Never gradient-fill an icon.
- **Don't** mix in a second icon library for one missing glyph, and don't recolor icons into `{colors.sun}` or the mascot palette — those hues are illustration-only.
- **Never use an emoji as a UI icon.** Emoji render differently per platform (Apple/Google/Windows/Android each ship their own) and carry uncontrollable color, breaking both visual consistency and the closed palette. Every glyph comes from Lucide; emoji remain legal only inside `{typography.sticker}` caption copy.

