---
version: alpha
name: MIDU-MenaQ7-design-system
description: "A joyful pediatric-health brand built on one signature move: an indigo-to-magenta gradient that carries every hero, every primary CTA, and the wordmark itself — cooled down by white clinical surfaces and warmed up by MIGI, a bespectacled giraffe doctor in a lab coat. Sunshine yellow is the energy accent, floating nutrient bubbles (Ca+, D3, K2, Mg, Arg) are the decorative vocabulary, and a ruler motif runs through the identity because the product's whole promise is measurable height growth for kids. Science you can trust, drawn like a cartoon your child already loves."

colors:
  primary: "#384B98"
  magenta: "#C1368D"
  on-primary: "#FFFFFF"
  grad-brand-start: "#384B98"
  grad-brand-end: "#C1368D"
  grad-sun-start: "#EFCA3D"
  grad-sun-end: "#E4E254"
  sun: "#EFCA3D"
  lime: "#E4E254"
  ink: "#221F1F"
  ink-soft: "#4A4660"
  canvas: "#FFFFFF"
  surface-soft: "#EEF1FA"
  surface-tint: "#F7F4FB"
  hairline: "#DDE2F0"
  migi-yellow: "#FFDA69"
  migi-purple: "#5F469B"
  migi-magenta: "#B84190"
  migi-deep: "#432C79"
  migi-orange: "#F68500"
  bubble-purple: "#5F469B"
  bubble-purple-light: "#8A6CC7"
  bubble-orange: "#F68500"
  semantic-success: "#2E7D46"
  semantic-error: "#C93A3A"
  overlay-scrim: "#221F1F"

typography:
  display-xl:
    fontFamily: Fz Rubik
    fontSize: 64px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.5px
    fontFeature: kern
  display:
    fontFamily: Fz Rubik
    fontSize: 44px
    fontWeight: 900
    lineHeight: 1.10
    letterSpacing: -0.25px
    fontFeature: kern
  headline:
    fontFamily: Fz Rubik
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    fontFeature: kern
  title:
    fontFamily: Fz Rubik
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
    fontFeature: kern
  tagline:
    fontFamily: Quicksand
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 1px
    fontFeature: kern
  body-lg:
    fontFamily: Fz Rubik
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: 0
    fontFeature: kern
  body:
    fontFamily: Fz Rubik
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
    fontFeature: kern
  body-sm:
    fontFamily: Fz Rubik
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
    fontFeature: kern
  button:
    fontFamily: Fz Rubik
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0.2px
    fontFeature: kern
  eyebrow:
    fontFamily: Fz Rubik
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 1.5px
    fontFeature: kern
  caption:
    fontFamily: Fz Rubik
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.3px
    fontFeature: kern
  sticker:
    fontFamily: Patrick Hand
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.5px
    fontFeature: kern

rounded:
  sm: 8px
  md: 12px
  lg: 20px
  xl: 28px
  pill: 999px
  full: 9999px

spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.grad-brand-start}"
    backgroundColorEnd: "{colors.grad-brand-end}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
  button-sun:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
  chip-nutrient:
    backgroundColor: "{colors.bubble-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.full}"
    size: 48px
  chip-nutrient-orange:
    backgroundColor: "{colors.bubble-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.full}"
    size: 40px
  card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-tinted:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px
  hero-gradient:
    backgroundColor: "{colors.grad-brand-start}"
    backgroundColorEnd: "{colors.grad-brand-end}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.xl}"
    padding: 48px
  section-tint:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.xl}"
    padding: 48px
  eyebrow-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.magenta}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  eyebrow-badge-on-tint:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.magenta}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.pill}"
    padding: 6px 14px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  progress-ruler:
    backgroundColor: "{colors.surface-soft}"
    fillColor: "{colors.sun}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    height: 12px
  stat-tile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.display}"
    rounded: "{rounded.lg}"
    padding: 24px
  mascot-slot:
    backgroundColor: "{colors.surface-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.sticker}"
    rounded: "{rounded.xl}"
    padding: 24px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    height: 64px
  footer-gradient:
    backgroundColor: "{colors.grad-brand-end}"
    backgroundColorEnd: "{colors.grad-brand-start}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 48px 32px
---

## Overview

MIDU MenaQ7 is a Vietnamese children's height-growth supplement ("Chuyên gia chiều cao" — *the height expert*), and its design system fuses two registers that usually repel each other: **clinical credibility** and **cartoon warmth**. The credibility layer is white canvas, generous spacing, Rubik set in confident heavy weights, and a restrained two-hue brand core. The warmth layer is MIGI — a giraffe doctor with round glasses, a white lab coat, and a purple-striped tie — plus a floating cloud of nutrient bubbles (Ca+, D3, K2, Mg, Arg) that turns ingredient science into toy-like decoration.

The system's signature move is the **brand gradient**: indigo `{colors.grad-brand-start}` flowing into magenta `{colors.grad-brand-end}`. It appears in the wordmark letterforms, on hero panels, on every primary CTA, and in full-bleed footer bands. It always flows in one direction per surface (indigo → magenta, left to right or top-left to bottom-right) and it is the *only* gradient allowed on interactive chrome. A second, supporting gradient — sunshine `{colors.grad-sun-start}` → lime `{colors.grad-sun-end}` — is reserved for illustrative highlights and progress fills, never for buttons.

The third pillar is the **ruler motif**. The logo hides a ruler inside the "I", a lightbulb dot above it, and a reaching child inside the "U". Measurement is the product promise, so height charts, growth trackers, and tick-marked progress bars are first-class citizens, not afterthoughts.

**Key Characteristics:**
- One signature gradient (`{colors.grad-brand-start}` → `{colors.grad-brand-end}`) owns all primary actions and hero moments.
- Sunshine yellow `{colors.sun}` is the energy accent — badges, highlights, progress fill, MIGI's own body color echoes it.
- White `{colors.canvas}` dominates; lavender-tinted `{colors.surface-soft}` sections give rhythm without competing with the gradient.
- Everything is round: pill buttons, circular nutrient chips, `{rounded.lg}`+ cards. There are no sharp corners anywhere in the brand.
- MIGI the giraffe doctor carries emotional states across the product — 15+ named poses map to UX moments (onboarding, success, errors, reminders, bedtime).
- Bold black comic outlines (`{colors.ink}`) belong to *illustration only* — UI chrome never uses black borders.
- Rubik at weights 400 / 500 / 700 / 900 is the single UI voice; the round, thin Quicksand tagline face appears only next to the logo lockup.

## Logo

Assets in `design-system/assets/`: `logo-midu.png` (primary color version, transparent), `logo-midu-white.png` (all-white version), `logo-midu-tagline.png` (lockup with the "Chuyên gia chiều cao" tagline).

Three ideas hide inside the wordmark — they are the brand's motif source:
- **Lightbulb** dotting the "i": the idea/expertise spark. Reusable as a list bullet in tips content.
- **Ruler** in the letter stem: the measurement promise. Echoed by `{components.progress-ruler}`.
- **Reaching child** inside the "U": growth. Lockup-only — never redraw as standalone iconography.

Usage rules:
- Color version on `{colors.canvas}` and light grounds; white version on the brand gradient or dark imagery. No other recolorings exist.
- Prefer the tagline lockup on first appearance per surface (hero, packaging front); the bare logo elsewhere.
- Clearspace: the height of the "m" on all sides. Minimum width 96px (below that, diacritics and the lightbulb blur — use the "m" + lightbulb mark instead).
- Never stretch, rotate, outline, drop-shadow, or detach elements from the wordmark.

## Colors

> Source: official brand guideline (palette + gradients), mascot vector art (sampled), logo lockups.

### Brand Core
- **Indigo** ({colors.primary}): The trust color. Headlines on white, secondary-button text/border, stat numbers, links. One of the two gradient poles.
- **Magenta** ({colors.magenta}): The warmth pole of the gradient. Used solo for eyebrow text, active states, small accents — but its main job is inside the gradient.
- **Brand Gradient** ({colors.grad-brand-start} → {colors.grad-brand-end}): The single most recognizable brand element. Primary CTAs, hero panels, footer bands, section dividers, the wordmark itself.
- **Sun Yellow** ({colors.sun}) and **Lime** ({colors.lime}): The official secondary pair, usually as the sun gradient ({colors.grad-sun-start} → {colors.grad-sun-end}). Energy, highlights, star ratings, progress fill, promotional badges. Yellow surfaces always carry `{colors.ink}` text, never white.

### Surface
- **Canvas** ({colors.canvas}): Default page ground. The clinical, trustworthy base that lets the gradient and mascot pop.
- **Surface Soft** ({colors.surface-soft}): Lavender-tinted section ground (sampled from the guideline's own slide background). Alternate long pages between canvas and this tint.
- **Surface Tint** ({colors.surface-tint}): Warmer, subtler lavender for mascot display slots and testimonial cards.
- **Hairline** ({colors.hairline}): 1px input borders, card strokes, table dividers. Indigo-biased, never pure grey.

### Mascot (illustration-only palette)
- **MIGI Yellow** ({colors.migi-yellow}): The giraffe's coat. Warmer than `{colors.sun}` — do not swap them.
- **MIGI Purple** ({colors.migi-purple}): Spots, shoes, and the nutrient bubbles' base.
- **MIGI Magenta → Deep** ({colors.migi-magenta} → {colors.migi-deep}): The shirt's vertical gradient; echoes the brand gradient one octave darker.
- **MIGI Orange** ({colors.migi-orange}): Ears, blush, tail tip, the Arg bubble. Never used in UI chrome.
- **Ink** ({colors.ink}): The comic outline black. Also the UI text color on light surfaces.
- **Ink Soft** ({colors.ink-soft}): Secondary/body-copy text — captions, meta lines, supporting paragraphs — anywhere `{colors.ink}` would read too heavy.

### Nutrient Bubbles
- **Bubble Purple** ({colors.bubble-purple}): Ca+, K2, D3, Mg spheres — radial gradient from `{colors.bubble-purple-light}` (top-left) through `{colors.bubble-purple}` to `{colors.migi-deep}`, white bold label, soft white specular highlight top-right. The full gradients are tokenized in `tokens.css` (`--midu-grad-bubble`, `--midu-grad-bubble-orange`).
- **Bubble Orange** ({colors.bubble-orange}): The Arg sphere only. One orange bubble per cluster, like a grace note.

### Semantic
- **Success** ({colors.semantic-success}): Confirmation ticks, "đạt chuẩn" growth states. Glyph/text fill, not large surfaces.
- **Error** ({colors.semantic-error}): Form errors, missed-dose alerts. Pair with MIGI's cry pose for empty/error states rather than scary red panels.
- **Overlay Scrim** ({colors.overlay-scrim}): Ink at ~50% opacity behind modals (opacity applied at render time).

## Typography

### Font Family

- **FZ Rubik** — The brand face, bundled in this kit at `design-system/fonts/FzRubik/` (TTF, weights 400/500/700/900, full Vietnamese coverage — verified; the type scale never uses 300/600/800, so those weights aren't shipped). Register it with `design-system/fonts/fzrubik.css` and use the stack `"Fz Rubik", system-ui, sans-serif`. **Important:** Google Fonts Rubik has *no Vietnamese subset* — never substitute it for Vietnamese copy; the bundled FZ Rubik is the Vietnamese-adapted cut the guideline calls "Rubik MKT".
- **Quicksand** — Substitute for the thin rounded tagline face used in "Chuyên gia chiều cao" lockups. Logo-adjacent use only.
- **Patrick Hand** (or any casual hand-print face with Vietnamese support) — Substitute for the sticker lettering ("WOW", "Cố LÊN!", "GOOD NIGHT") that accompanies MIGI poses. Decorative callouts only, never body copy.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 64px | 900 | 1.05 | -0.5px | Hero headlines, campaign titles |
| `{typography.display}` | 44px | 900 | 1.10 | -0.25px | Section openers, big stat numbers |
| `{typography.headline}` | 30px | 700 | 1.25 | 0 | Card group titles, article headings |
| `{typography.title}` | 22px | 700 | 1.35 | 0 | Card titles, modal titles |
| `{typography.tagline}` | 22px | 400 | 1.35 | 1px | "Chuyên gia chiều cao" lockup line only |
| `{typography.body-lg}` | 18px | 500 | 1.55 | 0 | Lead paragraphs, hero subcopy |
| `{typography.body}` | 16px | 400 | 1.60 | 0 | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Card body, meta text, footer links |
| `{typography.button}` | 16px | 700 | 1.20 | 0.2px | All buttons and pill tabs |
| `{typography.eyebrow}` | 13px | 700 | 1.30 | 1.5px | UPPERCASE section eyebrows, nutrient labels |
| `{typography.caption}` | 12px | 500 | 1.40 | 0.3px | Ruler tick labels, disclaimers, image credits |
| `{typography.sticker}` | 24px | 400 | 1.20 | 0.5px | Hand-lettered callouts beside MIGI poses |

### Principles

- **Black (900) is for moments, Bold (700) is for structure.** Heroes and stats get 900; everything that must be read comfortably runs 400–500. Skip weight 600 entirely — the brand voice jumps, it doesn't slide.
- **Display type may wear the gradient.** `{typography.display-xl}` and `{typography.display}` can be filled with the brand gradient (background-clip: text) on white grounds — exactly like the guideline's own "COLOR PALETTE" headings. Body copy never does.
- **Vietnamese-first.** Line heights are set for stacked diacritics (ắ, ễ, ộ). Do not tighten body line-height below 1.5 or headlines below 1.05, or diacritics will clip.
- **Eyebrows are uppercase with +1.5px tracking** and usually sit in an `{components.eyebrow-badge}` pill rather than floating bare. On `{colors.surface-soft}` sections use `{components.eyebrow-badge-on-tint}` (white badge ground) — magenta keeps AA contrast on white (5.0:1) but falls just short on the tint (4.45:1).

## Layout

### Spacing System

- **Base unit**: 8px, halved to 4px for chip and badge interiors.
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px.
- Section rhythm: `{spacing.section}` (80px) vertical between major blocks; hero and footer panels get `{spacing.xxl}` interior padding.
- Card interiors: `{spacing.lg}` (24px). Inputs: 12px vertical · 16px horizontal.

### Grid & Container

- Max content width 1200px, gutters `{spacing.lg}` mobile → `{spacing.xxl}` desktop.
- Product/benefit grids run 3-up desktop, 2-up tablet, 1-up mobile.
- **The mascot breaks the grid.** MIGI overlaps section edges — a hand over the hero boundary, a head poking above a card — always by design. Reserve overflow room; never `overflow: hidden` a mascot slot.

### Whitespace Philosophy

White space is the credibility layer. The gradient and the mascot are loud, so everything between them must be quiet: white canvas, one focal point per viewport, decoration budget of one bubble cluster per section. When a section feels empty, add breathing room or one nutrient bubble — not another color.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow | Tinted sections, footer, eyebrow badges |
| 1 (hairline) | 1px `{colors.hairline}` border | Inputs, comparison tables, quiet cards |
| 2 (soft) | 0 8px 24px rgba(56,75,152,0.10) | Default cards, nav dropdown — shadow is indigo-tinted, never grey |
| 3 (floating) | 0 16px 40px rgba(56,75,152,0.16) | Modals, mascot cards on tinted grounds |

Shadows always inherit the indigo hue. The nutrient bubbles carry their own painted specular highlight and drop no CSS shadow.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 8px | Tags, table cells, footer chips |
| `{rounded.md}` | 12px | Inputs, small tiles, thumbnails |
| `{rounded.lg}` | 20px | Cards, stat tiles |
| `{rounded.xl}` | 28px | Hero panels, section tints, mascot slots |
| `{rounded.pill}` | 999px | Every button, tab, badge, progress track |
| `{rounded.full}` | 9999px | Nutrient chips, avatar circles, icon buttons |

There is no square corner in this system. If a rectangle must read "technical" (a data table), use `{rounded.sm}` — never 0.

### Signature Motifs

- **Ruler ticks**: evenly spaced hairline marks on progress tracks, section dividers, and height-chart edges — the logo's "I" writ large.
- **Lightbulb dot**: the logo's idea-spark; usable as a list bullet in tips/advice content.
- **Reaching-child swoosh**: the logo's "U" figure; reserve for brand lockups, do not redraw as UI iconography.
- **Nutrient bubble cluster**: 3–5 spheres of varied sizes (one orange max), scattered with slight overlap around a focal image or stat.

## Components

### Buttons

**`button-primary`** — The gradient pill. "Mua ngay", "Bắt đầu đo", every hero CTA.
- Background: linear-gradient 90° `{colors.grad-brand-start}` → `{colors.grad-brand-end}`, text `{colors.on-primary}`, type `{typography.button}`, rounded `{rounded.pill}`, padding 14px 28px.
- Hover: lift 1px + deepen shadow; do not change the gradient. Pressed: remove lift.

**`button-secondary`** — White pill, 2px `{colors.primary}` border, `{colors.primary}` text. The calm partner ("Tìm hiểu thêm") beside every primary.

**`button-sun`** — `{colors.sun}` pill with `{colors.ink}` text. Promotional moments only (sale badges, gamified actions, kid-facing screens). Never place it in the same group as `button-primary` twice — one sun per viewport.

### Nutrient Chips

**`chip-nutrient`** — 48px circle, radial gradient `{colors.bubble-purple-light}` → `{colors.bubble-purple}` → `{colors.migi-deep}` (top-left to bottom-right), white specular dot top-right, uppercase white label (Ca+, K2, D3, Mg).
**`chip-nutrient-orange`** — 40px, `{colors.bubble-orange}` base, same anatomy. Only Arg wears orange; max one per cluster.
- Clusters float around imagery with slight size variance (32–56px) and gentle CSS float animation (6–8s ease-in-out, respects `prefers-reduced-motion`).

### Cards & Containers

**`card`** — White, `{rounded.lg}`, `{spacing.lg}` padding, level-2 indigo shadow. Benefit cards, article cards, product tiles.
**`card-tinted`** — `{colors.surface-soft}` ground, no shadow. Use inside white sections for FAQs, testimonials.
**`stat-tile`** — White card whose number is set in `{typography.display}` `{colors.primary}` (or gradient-filled), label in `{typography.eyebrow}` `{colors.magenta}`. For "+3–5cm/năm"-style claims, always with a source footnote in `{typography.caption}`.
**`mascot-slot`** — `{colors.surface-tint}` rounded-`{rounded.xl}` stage for a MIGI pose + `{typography.sticker}` hand-lettered caption. The pose may overflow the slot edge by up to 15%.

### Hero & Sections

**`hero-gradient`** — Full-width panel, brand gradient, `{rounded.xl}` corners (full-bleed below 768px), `{spacing.xxl}` padding. White display type left, MIGI pose right, bubble cluster scattered between. One per page.
**`section-tint`** — `{colors.surface-soft}` band for alternating rhythm: white → tint → white. Never two tinted sections adjacent.

### Forms

**`text-input`** — White, 1px `{colors.hairline}`, `{rounded.md}`, 12px/16px padding. Focus: border becomes `{colors.primary}` + 3px rgba(56,75,152,0.15) ring. Error: `{colors.semantic-error}` border + caption message; for empty states, prefer MIGI's cry pose over red banners.

### Progress & Measurement

**`progress-ruler`** — The brand's own progress bar: `{colors.surface-soft}` pill track with hairline ruler ticks every 10%, `{colors.sun}`→`{colors.lime}` gradient fill, `{typography.caption}` tick labels beneath. Use for height tracking, quiz progress, loyalty points — anywhere growth is shown.

### Navigation

**`top-nav`** — White bar, 64px, logo left, links center in `{typography.body-sm}` weight 500, `button-primary` right. Sticky with a level-2 shadow after scroll. Mobile: hamburger overlay; the primary pill stays on the bar.
**`footer-gradient`** — The gradient reversed (magenta → indigo) as a full-bleed band, white text, white outline logo variant, `{spacing.xxl}` padding. The page's closing brand moment.

### Mascot Usage (MIGI)

Assets live in `design-system/assets/` at 1871×1871 transparent PNG. Map poses to UX moments:

| Pose file | Moment |
|---|---|
| `migi-hello.png` | Onboarding, welcome screens, chat greeting |
| `migi-measure.png` | Height input, growth-chart empty state |
| `migi-medicine.png` | Dose reminder, product usage guide |
| `migi-cheer.png` / `migi-celebrate.png` | Goal reached, streak milestones |
| `migi-wow.png` | Feature reveal, achievement unlock |
| `migi-love.png` / `migi-grin.png` | Reviews, thank-you, social proof |
| `migi-cry.png` / `migi-sulk.png` | Error pages, empty results (soft, never blaming) |
| `migi-goodnight.png` | Evening reminders, sleep-tips content |
| `migi-exercise.png` | Activity tips, gamified challenges |
| `migi-birthday.png` | Birthday coupons, anniversary emails |
| `migi-bye.png` / `migi-wave-fullbody.png` | Logout, unsubscribe, order-complete send-off |

Rules: one MIGI per viewport · never mirror-flip (the coat, tie and "m" pocket badge break) · never recolor · minimum render height 120px so the glasses stay legible · `-plain` variants (no floating elements) are for tight layouts where bubbles would collide with UI.

## Do's and Don'ts

### Do

- Route every primary action through the **one** gradient pill — `{components.button-primary}` is the brand's handshake.
- Keep the gradient direction consistent: indigo left/top → magenta right/bottom. The footer may reverse it as a deliberate "closing bracket".
- Alternate white and `{colors.surface-soft}` sections so long pages breathe.
- Put `{colors.ink}` text on yellow surfaces — white-on-yellow fails contrast at any size.
- Use nutrient bubbles as the default decorative element before reaching for any new shape or emoji.
- Set all customer-facing copy in Vietnamese-subset fonts and test with stacked diacritics ("Chuyên gia chiều cao" is the canonical test string).
- Give every growth claim a `{typography.caption}` source line — credibility is half the brand.

### Don't

- Don't use the brand gradient on body text, icons, borders, or more than one CTA per view.
- Don't put black outlines on UI chrome — comic outlines belong to MIGI and illustration only.
- Don't swap `{colors.sun}` and `{colors.migi-yellow}` — UI yellow and giraffe yellow are different temperatures on purpose.
- Don't introduce new hues. The system is indigo, magenta, yellow/lime, purple-family mascot colors, and two semantic tones — nothing else.
- Don't square any corner or flatten any pill into a rectangle.
- Don't scatter more than one bubble cluster per section, and never more than one orange bubble per cluster.
- Don't use MIGI at tiny sizes (favicon, 24px icons) — use the lightbulb dot or logo "m" instead.
- Don't write shouting ALL-CAPS body copy; uppercase is reserved for `{typography.eyebrow}`.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Desktop-XL | 1440px | Content holds 1200px; gutters widen |
| Desktop | 1200px | Default 3-up card grids |
| Tablet | 960px | Grids 3-up → 2-up; nav collapses to hamburger |
| Mobile-L | 768px | Hero/tint panels go full-bleed (corners removed); MIGI moves below headline |
| Mobile | 560px | display-xl 64px → 40px; pills go full-width; bubble clusters thin to 3 |
| Mobile-S | 400px | Stat tiles stack 1-up; footer columns collapse |

### Touch Targets

- All pills ≥ 48px tall on touch viewports (padding already guarantees this).
- Nutrient chips are decorative — if made tappable (ingredient info), enforce 44px minimum and add a visible pressed state.
- Inputs ≥ 48px tall.

### Collapsing Strategy

- **Hero**: two-column (copy | mascot) → stacked with mascot at 60% scale below the CTA pair. Never crop MIGI's head.
- **Nav**: links fold into a full-canvas overlay; logo and `button-primary` stay visible.
- **Stat rows**: 3-up → horizontal scroll snap at Mobile-L rather than stacking, keeping numbers comparable.
- **Progress-ruler**: tick labels drop to every 25% below 560px; the track never shrinks below 8px.

## Iteration Guide

1. Reference components by token name (`{components.button-primary}`, `{components.progress-ruler}`) when asking for changes.
2. Choose the section ground first — `{colors.canvas}` or `{colors.surface-soft}` — before styling anything inside it.
3. Default text to `{typography.body}`; escalate to display sizes only for the one focal message per viewport.
4. New button variants must stay pill-shaped and must not invent new fills — derive from gradient, white+border, or sun.
5. When a screen feels flat, the fix order is: (a) add whitespace, (b) add one bubble cluster, (c) add a MIGI pose — never a new color.
6. Web-ready ≤560px copies of every asset ship inside the `midu-design-system` skill (`assets/`); full-res files in `design-system/assets/` are for print and packaging.
7. Validate token references and contrast after edits. Known traps: white text on `{colors.sun}` (always use `{colors.ink}`), `{colors.magenta}` eyebrows on `{colors.surface-soft}` (use `{components.eyebrow-badge-on-tint}`), and white labels on `{colors.bubble-orange}` (decorative only — exempt from AA, but never make the orange bubble a text-bearing control).

## Known Gaps

- **Font licensing** — FZ Rubik ships in `design-system/fonts/` from the company's font pack; confirm the license covers web embedding (`@font-face`) before public deployment. Do not substitute Google-Fonts Rubik for Vietnamese copy (it has no Vietnamese subset — diacritics would render in a mismatched fallback face mid-word).
- **The tagline script face is unidentified.** Quicksand approximates its thin rounded geometry; the original may be a Vietnamese foundry face (UTM/SVN family). Confirm before print work.
- **The guideline PDF documents only palette, logo variations, and font weights** — spacing, radii, elevation, components, and breakpoints in this file are *derived* from the brand's visual logic, not from an official spec. Treat them as the proposed system, adjustable as the brand team weighs in.
- **No official dark mode exists.** If one is required, start from `{colors.migi-deep}` as the canvas and keep the gradient for CTAs — but this is unexplored territory.
- **Print values**: the guideline lists CMYK equivalents (e.g. indigo 95/82/3/0, magenta 6/93/1/0); this file is screen-first and records hex only.
- **Vector sources are not in this kit.** The original `.ai`/`.pdf` files (mascot vectors, logo, guideline) live in the brand team's Drive folder; the kit ships rasterized PNGs (1871px mascot poses, 1224px logo), which cover web use but not large-format print. Request the vector files from the brand team for print work.
