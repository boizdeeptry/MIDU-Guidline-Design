## Colors

> Source: official brand guideline (palette + gradients), mascot vector art (sampled), logo lockups. Tint/shade ramps and the disabled/hairline-strong tokens below are *derived* for this revision — same rigor as the rest of the "Known Gaps"-flagged derived system, not from the original guideline PDF.

### Brand Core
- **Indigo** ({colors.primary}): The trust color. Headlines on white, secondary-button text/border, stat numbers, links. One of the two gradient poles.
- **Magenta** ({colors.magenta}): The warmth pole of the gradient. Used solo for eyebrow text, active states, small accents — but its main job is inside the gradient.
- **Brand Gradient** ({colors.grad-brand-start} → {colors.grad-brand-end}): The single most recognizable brand element. Primary CTAs, hero panels, footer bands, section dividers, the wordmark itself.
- **Sun Yellow** ({colors.sun}) and **Lime** ({colors.lime}): The official secondary pair, usually as the sun gradient ({colors.grad-sun-start} → {colors.grad-sun-end}). Energy, highlights, star ratings, progress fill, promotional badges. Yellow surfaces always carry `{colors.ink}` text, never white.

### Tint/Shade Ramps
Every brand hue now has a 10-step ramp (50 lightest → 900 darkest), all at the *same* hue/saturation as the approved base token — these are lightness variants, not new colors. `{colors.indigo-600}` = `{colors.primary}`, `{colors.magenta-500}` = `{colors.magenta}`, `{colors.sun-400}` = `{colors.sun}`; the base tokens stay the primary names to reference in prose, the ramp exists for states and subtle surfaces that previously had no token to reach for:
- **50–200**: subtle backgrounds and hover fills on white (e.g. `{components.button-secondary}` hover = `{colors.indigo-50}`).
- **300–400**: accents on *dark* grounds — reserved for the dark-mode starting palette (see Known Gaps), not used on light UI.
- **500–700**: pressed/active states, chart strokes, anything that needs to read "darker version of the brand color" without going near-black.
- **800–900**: near-black surfaces — dark-mode canvas territory, or `{components.toast-snackbar}`'s solid background.
- `{colors.sun-700}`–`{colors.sun-900}` read as olive/mustard rather than "sunshine" — correct for small text/borders/chart strokes, but never use them as a large brand-accent surface; that job stays with `{colors.sun}` itself.

### Surface
- **Canvas** ({colors.canvas}): Default page ground. The clinical, trustworthy base that lets the gradient and mascot pop.
- **Surface Soft** ({colors.surface-soft}): Lavender-tinted section ground (sampled from the guideline's own slide background). Alternate long pages between canvas and this tint.
- **Surface Tint** ({colors.surface-tint}): Warmer, subtler lavender for mascot display slots and testimonial cards.
- **Hairline** ({colors.hairline}): 1px passive dividers and table rules only — see Elevation for why interactive boundaries use `{colors.hairline-strong}` instead.
- **Hairline Strong** ({colors.hairline-strong}): 1px borders on `{components.text-input}` and any hairline-only interactive boundary. `{colors.hairline}` measures 1.30:1 against white, which fails WCAG 1.4.11's 3:1 minimum for interactive component boundaries; `{colors.hairline-strong}` clears ~3.2:1.
- **Disabled Bg / Disabled Text** ({colors.disabled-bg} / {colors.disabled-text}): The inert state for any button or input. Deliberately desaturated indigo-grey so a disabled control reads as "off," not as "a paler brand color." `{colors.disabled-text}` is intentionally sub-AA (~2.6:1) — disabled controls are exempt under WCAG 1.4.3/1.4.11 — but always pair it with `cursor: not-allowed` and `aria-disabled`, since color alone won't communicate "disabled" to everyone.
- **On-Primary Soft** ({colors.on-primary-soft}): Dimmed white for subcopy, captions, and links sitting on the brand gradient — footer link descriptions, the legal-band disclaimer, hero subheads. Measured **4.61:1 against the magenta pole `{colors.magenta}`** (the weaker end of the gradient) and ~7:1 against indigo, so it clears WCAG AA for text at any size across the whole gradient. It reads as a distinct, softer tier next to full-strength `{colors.on-primary}` headings — most visibly over the indigo half; near the magenta pole it is necessarily close to opaque white (pure white itself is only 5.02:1 there). Headings and buttons on the gradient stay full `{colors.on-primary}`; never drop on-gradient body text below this token.

### Mascot (illustration-only palette)
- **MIGI Yellow** ({colors.migi-yellow}): The giraffe's coat. Warmer than `{colors.sun}` — do not swap them.
- **MIGI Purple** ({colors.migi-purple}): Spots, shoes, and the nutrient bubbles' base.
- **MIGI Magenta → Deep** ({colors.migi-magenta} → {colors.migi-deep}): The shirt's vertical gradient; echoes the brand gradient one octave darker. Illustration-only — never a UI-chrome background (see `{components.toast-snackbar}`, which deliberately uses `{colors.indigo-800}` instead).
- **MIGI Orange** ({colors.migi-orange}): Ears, blush, tail tip, the Arg bubble. Never used in UI chrome.
- **Ink** ({colors.ink}): The comic outline black. Also the UI text color on light surfaces.
- **Ink Soft** ({colors.ink-soft}): Secondary/body-copy text — captions, meta lines, supporting paragraphs — anywhere `{colors.ink}` would read too heavy.

### Nutrient Bubbles
- **Bubble Purple** ({colors.bubble-purple}): Ca+, K2, D3, Mg spheres — radial gradient from `{colors.bubble-purple-light}` (top-left) through `{colors.bubble-purple}` to `{colors.migi-deep}`, white bold label, soft white specular highlight top-right. The full gradients are tokenized in `tokens.css` (`--midu-grad-bubble`, `--midu-grad-bubble-orange`). The white label at the lightest stop measures only 4.16:1 — since this is functional ingredient text (Ca+/K2/D3/Mg), not decoration, keep the label vertically centered/lower in the circle (away from the top-left highlight) or add a 1px `rgba(0,0,0,0.25)` text-shadow so legibility survives regardless of exact gradient position.
- **Bubble Orange** ({colors.bubble-orange}): The Arg sphere only. One orange bubble per cluster, like a grace note. This one *is* exempt from the AA requirement above — it's decorative and never carries a distinct ingredient label beyond "Arg," which is reinforced elsewhere.

### Semantic
- **Success** ({colors.semantic-success}): Confirmation ticks, "đạt chuẩn" growth states. Glyph/text fill, not large surfaces.
- **Error** ({colors.semantic-error}): Form errors, missed-dose alerts. Pair with MIGI's cry pose *alongside* the existing caption error message — never *instead of* it; see Accessibility.
- **Overlay Scrim** ({colors.overlay-scrim}): Ink at ~50% opacity behind modals (opacity applied at render time).
- **Never color-only.** `{colors.semantic-success}` and `{colors.semantic-error}` have near-identical luminance (~0.16) and sit on the red/green axis that deuteranopia/protanopia compress hardest — under simulation they read as nearly the same muddy tone. Every use pairs the color with a redundant non-color signal: a ✓ glyph for success, a ✕/! glyph or real text for error. Never ship a bare colored dot, pill, or row highlight.

### Data Visualization
No chart exists yet, but the product's core premise is a height-growth chart, so this is a near-term need, not a hypothetical — spec it now, using zero new hues:
- **Single-series growth line** (most likely first use): line `{colors.primary}`, area fill `{colors.indigo-100}` (or `rgba(56,75,152,0.08)`); a healthy-range/percentile band fills `{colors.sun-200}` with a dashed `{colors.sun-700}` reference line, reusing `{components.progress-ruler}`'s tick vocabulary.
- **Categorical, ≤4 series** (e.g. multiple children, or a multi-nutrient comparison): `{colors.primary}`, `{colors.magenta}`, `{colors.sun-700}` (raw `{colors.sun}` is too light to read as a line stroke on white), `{colors.migi-orange}`.
- **Do not** add `{colors.migi-purple}` as a 5th categorical series — its hue sits only ~30° from indigo, the exact confusion zone for red-green/blue-purple colorblindness. If a 5th series is ever needed, reach for `{colors.semantic-success}` first — it's already well hue-separated from the rest of the set.

