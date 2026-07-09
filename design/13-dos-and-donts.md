## Do's and Don'ts

### Do

- Route every primary action through the **one** gradient pill — `{components.button-primary}` is the brand's handshake.
- Keep the gradient direction consistent: indigo left/top → magenta right/bottom. The footer may reverse it as a deliberate "closing bracket".
- Alternate white and `{colors.surface-soft}` sections so long pages breathe.
- Put `{colors.ink}` text on yellow surfaces — white-on-yellow fails contrast at any size.
- Use nutrient bubbles as the default decorative element before reaching for any new shape or emoji.
- Set all customer-facing copy in Vietnamese-subset fonts and test with stacked diacritics ("Chuyên gia chiều cao" is the canonical test string).
- Give every growth claim a `{typography.caption}` source line — credibility is half the brand.
- Give every interactive element a visible `:focus-visible` ring — see Accessibility. This is not the "no black outline" rule; it's a different pseudo-class, purpose, and color.
- Pair every mascot pose that communicates state (error, success, reminder) with real text saying the same thing.
- Give every **enabled** interactive element `cursor: pointer` — links, buttons, clickable cards and rows. It pairs with the disabled rule (`cursor: not-allowed`); a clickable surface that keeps the default arrow reads as broken.

### Don't

- Don't use the brand gradient on body text, icons, borders, or more than one CTA per view.
- Don't put black outlines on UI chrome — comic outlines belong to MIGI and illustration only. (The indigo focus ring is not a black outline — see Do's above.)
- Don't swap `{colors.sun}` and `{colors.migi-yellow}` — UI yellow and giraffe yellow are different temperatures on purpose.
- Don't introduce new hues. The system is indigo, magenta, yellow/lime, purple-family mascot colors, and two semantic tones — including every tint/shade ramp step, which are lightness variants of these same hues, not additions.
- Don't square any corner or flatten any pill into a rectangle.
- Don't scatter more than one bubble cluster per section, and never more than one orange bubble per cluster.
- Don't use MIGI at tiny sizes (favicon, 24px icons) — use the lightbulb dot, an icon, or the logo "m" instead.
- Don't write shouting ALL-CAPS body copy; uppercase is reserved for `{typography.eyebrow}`.
- Don't rely on color alone for success/error signaling — always pair with a glyph or text.
- Don't suppress the focus ring to satisfy the "no outline" brand rule — that rule governs decorative comic strokes, not keyboard-navigation affordances.
- Don't use emoji as UI icons. Emoji render differently per platform and carry their own uncontrollable color — both break the closed palette. UI glyphs come from the icon set (see Icons); emoji stay legal only inside `{typography.sticker}` caption copy.

