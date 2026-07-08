---
version: 0.3.0
status: alpha
name: MIDU-MenaQ7-design-system
description: "A joyful pediatric-health brand built on one signature move: an indigo-to-magenta gradient that carries every hero, every primary CTA, and the wordmark itself — cooled down by white clinical surfaces and warmed up by MIGI, a bespectacled giraffe doctor in a lab coat. Sunshine yellow is the energy accent, floating nutrient bubbles (Ca+, D3, K2, Mg, Arg) are the decorative vocabulary, and a ruler motif runs through the identity because the product's whole promise is measurable height growth for kids. Science you can trust, drawn like a cartoon your child already loves."

colors:
  primary: "#384B98"
  magenta: "#C1368D"
  on-primary: "#FFFFFF"
  on-primary-soft: "rgba(255,255,255,0.94)"
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
  hairline-strong: "#8A8F9E"
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
  disabled-bg: "#EBECEF"
  disabled-text: "#9C9FAB"
  # Tint/shade ramps — same hue/saturation as the approved base token, lightness only.
  # Not new hues: indigo-600 = {colors.primary}, magenta-500 = {colors.magenta}, sun-400 = {colors.sun}.
  indigo-50: "#F4F5FB"
  indigo-100: "#E5E8F5"
  indigo-200: "#C7CEEA"
  indigo-300: "#9EAADB"
  indigo-400: "#6A7DC8"
  indigo-500: "#455CBA"
  indigo-600: "#384B98"
  indigo-700: "#2D3D7B"
  indigo-800: "#243061"
  indigo-900: "#192143"
  magenta-50: "#FCF3F9"
  magenta-100: "#F7E3F0"
  magenta-200: "#EEC3DF"
  magenta-300: "#E298C7"
  magenta-400: "#D260A8"
  magenta-500: "#C1368D"
  magenta-600: "#9F2D75"
  magenta-700: "#7F245E"
  magenta-800: "#5F1B46"
  magenta-900: "#40122F"
  sun-50: "#FDFAEC"
  sun-100: "#FCF3D5"
  sun-200: "#F9EAB4"
  sun-300: "#F4DB7B"
  sun-400: "#EFCA3D"
  sun-500: "#ECBF13"
  sun-600: "#C6A010"
  sun-700: "#A0820D"
  sun-800: "#7A630A"
  sun-900: "#554507"

typography:
  display-xl:
    fontFamily: Fz Rubik
    fontSize: "clamp(2.5rem, 2rem + 2.222vw, 4rem)"
    fontWeight: 900
    lineHeight: 1.125
    letterSpacing: -0.5px
    fontFeature: kern
  display:
    fontFamily: Fz Rubik
    fontSize: "clamp(2rem, 1.75rem + 1.111vw, 2.75rem)"
    fontWeight: 900
    lineHeight: 1.10
    letterSpacing: -0.25px
    fontFeature: "kern, tnum"
  headline:
    fontFamily: Fz Rubik
    fontSize: "clamp(1.5rem, 1.375rem + 0.556vw, 1.875rem)"
    fontWeight: 700
    lineHeight: 1.333
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
    lineHeight: 1.75
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
    lineHeight: 1.54
    letterSpacing: 1.5px
    fontFeature: kern
  caption:
    fontFamily: Fz Rubik
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.667
    letterSpacing: 0.3px
    fontFeature: kern
  sticker:
    fontFamily: Patrick Hand
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.5px
    fontFeature: kern
  link:
    # Decoration overlay, not a type-scale entry — a link takes its size from
    # whatever body/body-sm/caption text it sits inside. See Typography > Links.
    color: "{colors.primary}"
    textDecoration: underline
    textDecorationColor: "rgba(56,75,152,0.4)"
    textDecorationThickness: 1px
    textUnderlineOffset: 2px

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
  touch-target-min: 48px
  touch-target-min-decorative: 44px

breakpoints:
  desktop-xl: 1440px
  desktop: 1200px
  tablet: 960px
  mobile-l: 768px
  mobile: 560px
  mobile-s: 400px

container:
  max-width: 1200px
  reading-width: 760px

motion:
  duration-fast: 120ms
  duration-base: 200ms
  duration-slow: 400ms
  duration-float: 7000ms
  duration-count: 1600ms
  easing-standard: "cubic-bezier(0.4, 0, 0.2, 1)"
  easing-emphasized: "cubic-bezier(0.34, 1.56, 0.64, 1)"

focus:
  ring-color: "{colors.primary}"
  ring-color-on-gradient: "{colors.on-primary}"
  ring-width: 2px
  ring-offset: 2px
  ring-style: solid

components:
  button-primary:
    backgroundColor: "{colors.grad-brand-start}"
    backgroundColorEnd: "{colors.grad-brand-end}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
    pressedGradientStart: "{colors.indigo-700}"
    pressedGradientEnd: "{colors.magenta-700}"
    disabledBackgroundColor: "{colors.disabled-bg}"
    disabledTextColor: "{colors.disabled-text}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
    hoverBackgroundColor: "{colors.indigo-50}"
    disabledBackgroundColor: "{colors.disabled-bg}"
    disabledTextColor: "{colors.disabled-text}"
  button-sun:
    backgroundColor: "{colors.sun}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
    hoverBackgroundColor: "{colors.sun-500}"
    disabledBackgroundColor: "{colors.disabled-bg}"
    disabledTextColor: "{colors.disabled-text}"
  chip-nutrient:
    backgroundColor: "{colors.bubble-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.full}"
    minWidth: 48px
    minHeight: 48px
    aspectRatio: 1
    padding: 4px
    overflow: visible
  chip-nutrient-orange:
    backgroundColor: "{colors.bubble-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.full}"
    minWidth: 40px
    minHeight: 40px
    aspectRatio: 1
    padding: 4px
    overflow: visible
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
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    disabledBackgroundColor: "{colors.disabled-bg}"
    disabledTextColor: "{colors.disabled-text}"
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
    minHeight: 64px
    linkHoverColor: "{colors.primary}"
    linkCurrentColor: "{colors.primary}"
    linkCurrentIndicator: "2px solid {colors.primary}, bottom edge"
  footer-gradient:
    backgroundColor: "{colors.grad-brand-end}"
    backgroundColorEnd: "{colors.grad-brand-start}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 48px 32px
  product-grid:
    columns-desktop: 3
    columns-tablet: 2
    columns-mobile: 1
    gap: "{spacing.lg}"
  toast-snackbar:
    backgroundColor: "{colors.indigo-800}"
    backgroundColorSuccess: "{colors.semantic-success}"
    backgroundColorError: "{colors.semantic-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.pill}"
    padding: 12px 20px
    elevation: 3
  empty-state:
    container: "{components.mascot-slot}"
    heading: "{typography.title}"
    headingColor: "{colors.ink}"
    body: "{typography.body-sm}"
    bodyColor: "{colors.ink-soft}"
    cta: "{components.button-secondary}"
  modal-dialog:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xl}"
    padding: "{spacing.xl}"
    elevation: 3
    overlayColor: "{colors.overlay-scrim}"
    overlayOpacity: 0.5
    title: "{typography.title}"
    body: "{typography.body}"
    primaryAction: "{components.button-primary}"
    secondaryAction: "{components.button-secondary}"
  date-picker:
    field: "{components.text-input}"
    focusBorderColor: "{colors.primary}"
    popoverElevation: 2
    popoverRounded: "{rounded.md}"
    monthHeader: "{typography.eyebrow}"
    todayDot: "{colors.sun}"
    selectedDayBackground: "{colors.primary}"
    selectedDayText: "{colors.on-primary}"
    errorBorderColor: "{colors.semantic-error}"
    disabledBackgroundColor: "{colors.disabled-bg}"
  tabs:
    trackBackgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.pill}"
    typography: "{typography.button}"
    activeTextColor: "{colors.primary}"
    activeBackgroundColor: "{colors.canvas}"
    inactiveTextColor: "{colors.ink-soft}"
  button-primary-on-gradient:
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 14px 28px
    hoverBackgroundColor: "{colors.indigo-50}"
    pressedBackgroundColor: "{colors.indigo-100}"
    disabledBackgroundColor: "rgba(255,255,255,0.35)"
    disabledTextColor: "{colors.on-primary-soft}"
    focusRing: "{focus.ring-color-on-gradient}"
  button-secondary-on-gradient:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    borderColor: "{colors.on-primary}"
    borderWidth: 2px
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 12px 26px
    hoverBackgroundColor: "rgba(255,255,255,0.12)"
    focusRing: "{focus.ring-color-on-gradient}"
  stat-counter:
    valueTypography: "{typography.display}"
    valueColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.ink-soft}"
    fontVariantNumeric: tabular-nums
    duration: "{motion.duration-count}"
    easing: "{motion.easing-standard}"
    numberLocale: vi-VN
    role: img
  card-hover-lift:
    kind: behavior-mixin
    liftY: -2px
    elevationFrom: 2
    elevationTo: 3
    duration: "{motion.duration-fast}"
    easing: "{motion.easing-standard}"
    triggers: "hover, focus-visible"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    imageRounded: "{rounded.md}"
    imageAspectRatio: 1
    imageFadeIn: "{motion.duration-base}"
    promoBadgeBackground: "{colors.sun}"
    promoBadgeText: "{colors.ink}"
    name: "{typography.title}"
    price: "{typography.body-lg}"
    priceColor: "{colors.primary}"
    cta: "{components.button-primary}"
    hover: "{components.card-hover-lift}"
    outOfStockBackground: "{colors.disabled-bg}"
    outOfStockText: "{colors.disabled-text}"
  ingredient-facts-table:
    rounded: "{rounded.md}"
    header: "{typography.body-sm}"
    cell: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowRuleColor: "{colors.hairline}"
    rowRuleWidth: 1px
    zebraBackground: "{colors.surface-soft}"
  testimonial-card:
    backgroundColor: "{colors.surface-tint}"
    rounded: "{rounded.lg}"
    avatarSize: 48px
    avatarRounded: "{rounded.full}"
    name: "{typography.body-sm}"
    meta: "{typography.caption}"
    metaColor: "{colors.ink-soft}"
    excerpt: "{typography.body}"
    excerptLineClamp: 3
    link: "{typography.link}"
  expert-endorsement-card:
    backgroundColor: "{colors.surface-tint}"
    rounded: "{rounded.lg}"
    avatarSize: 48px
    avatarRounded: "{rounded.full}"
    name: "{typography.body-sm}"
    credential: "{typography.caption}"
    credentialColor: "{colors.ink-soft}"
    quote: "{typography.body}"
    source: "{typography.caption}"
    mascotAccent: migi-love
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
- MIGI the giraffe doctor carries emotional states across the product — 15+ named poses map to UX moments (onboarding, success, errors, reminders, bedtime) — but the illustration always travels with real text; see Accessibility.
- Bold black comic outlines (`{colors.ink}`) belong to *illustration only* — UI chrome never uses black borders. The one exception is the indigo `:focus-visible` ring, which is a different color, purpose, and pseudo-class — see Accessibility.
- Rubik at weights 400 / 500 / 700 / 900 is the single UI voice; the round, thin Quicksand tagline face appears only next to the logo lockup.
- Every hue in this system — including the new tint/shade ramps below — is a lightness variant of an already-approved brand color. The palette is still closed: no new hues were introduced in this revision.

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

## Voice and Tone

MIDU speaks with two voices layered on one personality: a **trusted pediatric expert** (the credibility layer) who travels with a **cheerful giraffe sidekick** (the warmth layer). Copy should never fully commit to either — pure clinical copy reads cold for a kids' brand; pure mascot-cute copy undermines a supplement claim.

1. **Address the parent as "bạn," the child as "con" or "bé" — never "em" or "cháu" for the parent.** The reader is an adult customer, not a subordinate. Reserve exclamation-heavy, mascot-voiced lines ("Wow!", "Cố lên nào!") for MIGI's own speech bubbles and micro-copy (empty states, celebrations) — never for headlines making a health claim.
2. **Every measurable claim needs a number and a source caption.** "Hỗ trợ phát triển chiều cao" is fine as a headline; "+3–5cm/năm" needs a `{typography.caption}` footnote citing the study/condition — see `{components.stat-tile}`. This is a trust and regulatory requirement, not a style preference.
3. **No fear, no guilt, no scarcity pressure.** Avoid "Con bạn đang thấp hơn bạn bè?" framing, countdown timers, or "chỉ còn X suất" copy. Pair any shortfall message with an encouraging MIGI pose (`migi-cheer`) — never `migi-cry`/`migi-sulk` used to shame the reader into buying.
4. **Mascot exclamations stay short, singular, and read like real speech — not shouty body copy.** "Wow!", "Cố lên!", "Tuyệt vời!" are one-line `{typography.sticker}` captions beside a MIGI pose. They never appear in `{typography.body}` paragraphs or on button labels.
5. **Never fabricate data.** Product names, ingredient dosages, prices, customer counts, satisfaction %, ratings, doctor names, and citations must come from a real Midu source — never invented, not even as "*illustrative" placeholder. If a real figure isn't available: omit the number, use a clearly-labelled structural placeholder (e.g. "[nội dung minh họa — chưa có đánh giá thật]"), or drop the element. Specific danger zones: **ingredient dosages** (Midu MenaQ7 K2 comes only in 45 / 180 / 360 mcg — never invent a mg value the packaging doesn't state), **expert endorsements** (attribute only to real advisory-board doctors, with a real cited source; rank-and-file staff may not self-style as "bác sĩ"), and **testimonials/social proof** (Midu's own rule: "hỏi hiện trạng, không bịa social proof"). Real company figures to reach for instead of invented ones: ~20.000 chuyên gia đã đào tạo, 91+ khóa học, ~300.000 phác đồ (source: midu.vn).

| | Copy |
|---|---|
| ❌ Don't | "CON BẠN ĐANG THUA KÉM BẠN BÈ VỀ CHIỀU CAO?? Đặt hàng NGAY để không bỏ lỡ ưu đãi cuối cùng!!!" |
| ✅ Do | "Hỗ trợ con phát triển chiều cao mỗi ngày, cùng MIGI." — button: `{components.button-primary}` "Bắt đầu đo" |

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

## Typography

### Font Family

- **FZ Rubik** — The brand face, bundled in this kit at `design-system/fonts/FzRubik/` (TTF, weights 400/500/700/900, full Vietnamese coverage — verified; the type scale never uses 300/600/800, so those weights aren't shipped). Register it with `design-system/fonts/fzrubik.css` and use the stack `"Fz Rubik", system-ui, sans-serif`. **Important:** Google Fonts Rubik has *no Vietnamese subset* — never substitute it for Vietnamese copy; the bundled FZ Rubik is the Vietnamese-adapted cut the guideline calls "Rubik MKT".
- **Quicksand** — Substitute for the thin rounded tagline face used in "Chuyên gia chiều cao" lockups. Logo-adjacent use only.
- **Patrick Hand** (or any casual hand-print face with Vietnamese support) — Substitute for the sticker lettering ("WOW", "Cố LÊN!", "GOOD NIGHT") that accompanies MIGI poses. Decorative callouts only, never body copy.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | clamp 40→64px | 900 | 1.125 | -0.5px | Hero headlines, campaign titles |
| `{typography.display}` | clamp 32→44px | 900 | 1.10 | -0.25px | Section openers, big stat numbers (tabular figures) |
| `{typography.headline}` | clamp 24→30px | 700 | 1.333 | 0 | Card group titles, article headings |
| `{typography.title}` | 22px | 700 | 1.35 | 0 | Card titles, modal titles |
| `{typography.tagline}` | 22px | 400 | 1.35 | 1px | "Chuyên gia chiều cao" lockup line only |
| `{typography.body-lg}` | 18px | 500 | 1.55 | 0 | Lead paragraphs, hero subcopy |
| `{typography.body}` | 16px | 400 | 1.75 | 0 | Default body |
| `{typography.body-sm}` | 14px | 400 | 1.55 | 0 | Card body, meta text, footer links |
| `{typography.button}` | 16px | 700 | 1.20 | 0.2px | All buttons and pill tabs |
| `{typography.eyebrow}` | 13px | 700 | 1.54 | 1.5px | UPPERCASE section eyebrows, nutrient labels |
| `{typography.caption}` | 12px | 500 | 1.667 | 0.3px | Ruler tick labels, disclaimers, image credits, source footnotes |
| `{typography.sticker}` | 24px | 400 | 1.20 | 0.5px | Hand-lettered callouts beside MIGI poses |
| `{typography.link}` | inherits | inherits | inherits | inherits | Inline text links only — see Links below |

### Fluid Type

`display-xl`, `display`, and `headline` now scale continuously with `clamp()` instead of jumping once at a single breakpoint — the old spec had no defined size at all between 561–767px ("Mobile-L"), which meant a 64px hero headline rendered at full size on a 700px-wide phone-landscape/small-tablet viewport. Formulas are anchored 360px (small phone) → 1440px (Desktop-XL, matching the breakpoints table):

```
display-xl:  clamp(2.5rem, 2rem + 2.222vw, 4rem)      /* 40px → 64px */
display:     clamp(2rem, 1.75rem + 1.111vw, 2.75rem)  /* 32px → 44px */
headline:    clamp(1.5rem, 1.375rem + 0.556vw, 1.875rem) /* 24px → 30px */
```

`title` and smaller stay fixed-size — their content (card titles, body copy, badges) doesn't carry the same hero-scale overflow risk.

### Links

No inline-link treatment existed before this revision, despite `{colors.primary}` already being described as the link color in prose. `{typography.link}` is a decoration overlay, not a new type-scale size — it inherits whatever body/body-sm/caption role it's embedded in:

- Default: `color: {colors.primary}`, 1px underline at 40% opacity, 2px underline offset.
- Hover: `color: {colors.magenta}`, underline color matches.
- Focus: the global `:focus-visible` ring (see Accessibility) — no separate link-only focus style.
- No visited state — this is a marketing/e-commerce site with no forum or citation-heavy content that benefits from distinguishing visited links.
- Underlined by default (not hover-only): WCAG 1.4.1 requires links inside body text be distinguishable by more than color alone unless surrounding-text contrast clears 3:1 — safer to underline unconditionally in running copy. `{components.top-nav}` and `{components.footer-gradient}` links are positionally distinct components already and are exempt from this rule.
- `{colors.primary}` on `{colors.canvas}` computes to ~8.0:1 (AAA) — a stronger, safer default than magenta, which the eyebrow-badge note below already flags at only 5.0:1 on canvas / 4.45:1 on tint.

### Principles

- **Black (900) is for moments, Bold (700) is for structure.** Heroes and stats get 900; everything that must be read comfortably runs 400–500. Skip weight 600 entirely — the brand voice jumps, it doesn't slide.
- **Display type may wear the gradient.** `{typography.display-xl}` and `{typography.display}` can be filled with the brand gradient (background-clip: text) on white grounds — exactly like the guideline's own "COLOR PALETTE" headings. Body copy never does.
- **Tabular figures on stat numerals.** `{typography.display}` carries `fontFeature: kern, tnum` so digits align in stat rows and any animated counter doesn't jitter. *Unverified: confirm FZ Rubik 900 actually ships a `tnum` OpenType feature before shipping this CSS — flagged in Known Gaps.*
- **Vietnamese-first, and not uniformly safe at every size.** Line heights are set for stacked diacritics (ắ, ễ, ộ), but the margin isn't equal across the scale. `{typography.caption}` (12px) is the highest-risk token in the system — it's the smallest size *and* it carries the brand's credibility claims (source footnotes, disclaimers), so its line-height was raised to 1.667. `{typography.eyebrow}` (13px, UPPERCASE) is next-highest risk — Vietnamese uppercase still stacks tone marks *above* cap-height (Ắ, Ễ, Ộ), which a tight line-height clips regardless of badge padding; raised to 1.54. Do not tighten either below these values, or `{typography.body}` below 1.75, or `{typography.display-xl}` below 1.125.
- **Eyebrows are uppercase with +1.5px tracking** and usually sit in an `{components.eyebrow-badge}` pill rather than floating bare. **On `{colors.surface-soft}` sections, `{components.eyebrow-badge-on-tint}` is mandatory, not optional**: `{components.eyebrow-badge}` direct-on-tint measures 4.45:1, a genuine AA failure at 13px/700 (which is not WCAG large text). A bare (unbadged) eyebrow — e.g. a section kicker directly on white canvas — defaults to `color: {colors.primary}`; magenta is reserved for the badge-on-canvas contrast story, not bare text.

## Layout

### Spacing System

- **Base unit**: 8px, halved to 4px for chip and badge interiors.
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px · `{spacing.touch-target-min}` 48px · `{spacing.touch-target-min-decorative}` 44px.
- Section rhythm: `{spacing.section}` (80px) vertical between major blocks; hero and footer panels get `{spacing.xxl}` interior padding.
- Card interiors: `{spacing.lg}` (24px). Inputs: 12px vertical · 16px horizontal.
- Grids: `{components.product-grid}` formalizes gap at `{spacing.lg}` (24px) — replaces the ad hoc 14–48px gap values that had crept into shipped code with no token backing them.

### Breakpoints

Tokenized as `{breakpoints.*}` (see frontmatter) so implementers reference `@media (max-width: {breakpoints.tablet})` instead of re-typing raw pixel values — two undocumented breakpoints (860px, 700px) had already appeared in shipped code before these tokens existed. Values map 1:1 to the Responsive Behavior table below.

### Grid & Container

- Max content width `{container.max-width}` (1200px), gutters `{spacing.lg}` mobile → `{spacing.xxl}` desktop.
- `{container.reading-width}` (760px) — the second real max-width in this system, for FAQ lists, lead-capture forms, and other single-column reading content. Previously a repeated magic number with no token; use it instead of inventing 720/780/800px on the next narrow-content component.
- Product/benefit grids run `{components.product-grid}`: 3-up desktop, 2-up tablet, 1-up mobile, `{spacing.lg}` gap.
- **The mascot breaks the grid.** MIGI overlaps section edges — a hand over the hero boundary, a head poking above a card — always by design. Reserve overflow room; never `overflow: hidden` a mascot slot.

### Whitespace Philosophy

White space is the credibility layer. The gradient and the mascot are loud, so everything between them must be quiet: white canvas, one focal point per viewport, decoration budget of one bubble cluster per section. When a section feels empty, add breathing room or one nutrient bubble — not another color.

## Page Anatomy

The default skeleton for a MIDU marketing/landing page — not a straitjacket, but the order an agent should reach for before inventing one. The white→`{colors.surface-soft}` alternation (see Layout) is what drives the rhythm; each band below flips the ground.

1. **`{components.top-nav}`** — white bar, logo left, one `{components.button-primary}` right.
2. **`{components.hero-gradient}`** — the gradient panel, ~55/45 copy|mascot split, one bubble cluster, on-gradient CTA pair. This surface holds the page's single gradient CTA.
3. **Benefits band (white)** — `{components.product-grid}` of `{components.card}`; **every efficacy/growth claim pairs with a stat or visual and a `{typography.caption}` source line** (Voice §2). Claims never float unsupported.
4. **Social-proof band (`{colors.surface-soft}`)** — `{components.testimonial-card}` grid + optional `{components.expert-endorsement-card}`.
5. **Stat/CTA row (white)** — `{components.stat-counter}` trust numbers, then the closing call to action.
6. **`{components.footer-gradient}`** — reversed gradient, link columns, and the mandatory `legal-band` disclaimer.

Sections may be added, removed, or reordered, but two rules always hold: **no two tinted sections are ever adjacent**, and **only one gradient CTA is visible per viewport**.

### Density

Section rhythm is not one-size-fits-all — a marketing page breathes, an in-app data screen packs tighter:

| Surface | Section gap | Card-grid gap |
|---|---|---|
| Marketing / landing | `{spacing.section}` (80px) | `{spacing.lg}` (24px) |
| App / height-tracker screens | 32–48px (`{spacing.xl}`–`{spacing.xxl}`) | `{spacing.md}` (16px) |

The 80px `{spacing.section}` rhythm is the landing-page default; app screens (growth charts, dose logs, settings) use the tighter scale so functional density doesn't force endless scrolling.

## Elevation and Depth

| Level | Treatment | Use |
|---|---|---|
| 0 (flat) | No shadow | Tinted sections, footer, eyebrow badges |
| 1a (hairline, passive) | 1px `{colors.hairline}` border | Passive dividers, table rules — non-interactive only |
| 1b (hairline, interactive) | 1px `{colors.hairline-strong}` border | `{components.text-input}` and any hairline-only interactive boundary (WCAG 1.4.11 needs ≥3:1 on interactive boundaries; plain `{colors.hairline}` measures only 1.30:1) |
| 2 (soft) | 0 8px 24px rgba(56,75,152,0.10) | Default cards, nav dropdown — shadow is indigo-tinted, never grey |
| 3 (floating) | 0 16px 40px rgba(56,75,152,0.16) | Modals, toasts, mascot cards on tinted grounds |

Shadows always inherit the indigo hue. The nutrient bubbles carry their own painted specular highlight and drop no CSS shadow.

## Motion

Two timing families, referenced by every animated component — never a hand-rolled duration/easing outside this set:

- `{motion.duration-fast}` (120ms) / `{motion.duration-base}` (200ms) / `{motion.duration-slow}` (400ms) + `{motion.easing-standard}` for **functional** UI feedback: hover, focus, pressed, error, sweep, dismiss.
- `{motion.easing-emphasized}` (slight overshoot) is reserved for **playful, mascot-triggered** moments only — never for ordinary hover/focus feedback.
- `{motion.duration-float}` (7s) is specifically the nutrient-bubble ambient float; not reused elsewhere.
- `{motion.duration-count}` (1600ms) is specifically the stat count-up (`{components.stat-counter}`); single-purpose like `duration-float`, pairs with `{motion.easing-standard}`. 400ms `duration-slow` was measured unreadable for a count-up (~56% through at cutoff), so counting gets its own token rather than stretching a functional one.

Applied to existing components:
- `{components.button-primary}` hover/pressed: `transform/box-shadow {motion.duration-fast} {motion.easing-standard}` — lift 1px + deepen shadow on hover; on press, swap to `pressedGradientStart`/`pressedGradientEnd` (one ramp step darker) *and* remove the lift, since a fixed 1px lift alone is barely visible on touch devices with no hover state.
- `{components.chip-nutrient}` float: `bubble-float {motion.duration-float} {motion.easing-standard} infinite alternate`.
- `{components.chip-nutrient}` tap (if ever made interactive): scale `1 → 1.12 → 1` on `{motion.duration-fast} {motion.easing-emphasized}` — the brand's first signature micro-interaction.
- `{components.progress-ruler}` value change: fill-width sweep over `{motion.duration-slow} {motion.easing-standard}`, tick labels count up in place rather than snapping — this is the highest-leverage micro-interaction available, since the ruler *is* the brand's core measurement metaphor.

### Scroll and reveal patterns

Three vanilla patterns (no animation library) that make a page feel alive without breaking the two-family discipline. All are `IntersectionObserver`-driven — never a scroll listener.

**`scroll-reveal`** — sections/cards fade in + slide up 8px on first entry. Group siblings stagger via an inline `--reveal-index` × 70ms `transition-delay`; JS only assigns indices and toggles `.is-visible`, so all timing lives in CSS and no `setTimeout` stacks. One shared observer for all reveal elements; each reveals once (`unobserve` after firing). This is **decorative entrance motion** → fully disabled under reduced motion.

**Prefer the `data-reveal-group` authoring path** (put the attribute on a container; the script adds `data-reveal` to each child and observes it). That path is self-safe: if the script never runs, no child ever gets the hidden `[data-reveal]` state, so content stays visible. If you author `data-reveal` directly in markup instead, add a no-JS fallback so a blocked/failed script can't hide content permanently — either a `<noscript>` rule setting `[data-reveal]{opacity:1}`, or a one-line `document.documentElement.classList.add('js')` gate with `.js [data-reveal]:not(.is-visible){opacity:0}`.

```css
[data-reveal] {
  --reveal-stagger: 70ms;
  opacity: 1; transform: translateY(0);
  transition: opacity var(--midu-duration-slow) var(--midu-easing-standard),
              transform var(--midu-duration-slow) var(--midu-easing-standard);
  transition-delay: calc(min(var(--reveal-index, 0), 12) * var(--reveal-stagger)); /* cap 12 so a long list can't stack a multi-second tail */
}
/* Hidden state on the negation, NOT on .is-visible — keeps the settled post-reveal
   specificity at one attribute (0,1,0) so .card-hover-lift:hover (0,2,0) reliably
   wins `transform` after reveal, regardless of stylesheet order. */
[data-reveal]:not(.is-visible) { opacity: 0; transform: translateY(8px); }
@media (prefers-reduced-motion: reduce) {
  /* scoped to :not(.is-visible), not bare [data-reveal]: a bare !important transform
     here would also override .card-hover-lift:hover's lift on any element carrying both. */
  [data-reveal]:not(.is-visible) { opacity: 1 !important; transform: none !important; transition: none !important; }
}
```

```js
document.querySelectorAll('[data-reveal-group]').forEach(function (g) {
  Array.from(g.children).forEach(function (c, i) { c.style.setProperty('--reveal-index', i); c.setAttribute('data-reveal', ''); });
});
var ro = new IntersectionObserver(function (entries, obs) {
  entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-visible'); obs.unobserve(e.target); } });
}, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('[data-reveal]').forEach(function (el) { ro.observe(el); });
```

**`card-hover-lift`** — the reusable form of the mascot-card hover: lift 2px + deepen shadow (`shadow-card` → `shadow-float`) on `{motion.duration-fast} {motion.easing-standard}`, on both `:hover` and `:focus-visible`. This is **functional feedback** → collapses to ~1ms under reduced motion (via the global override), never removed. 2px sits between `button-primary`'s 1px press and a card's larger surface, keeping a size-based motion hierarchy.

```css
/* Selector doubled to (0,2,0): CSS doesn't merge two rules' transition lists — an
   equal-specificity tie lets [data-reveal]'s 400ms transition silently win the whole
   property (including box-shadow). Doubling guarantees this rule owns the hover transition. */
.card-hover-lift.card-hover-lift {
  transition: transform var(--midu-duration-fast) var(--midu-easing-standard),
              box-shadow var(--midu-duration-fast) var(--midu-easing-standard);
}
.card-hover-lift:hover, .card-hover-lift:focus-visible {
  transform: translateY(-2px); box-shadow: var(--midu-shadow-float);
}
```

**`stat-counter`** (motion contract; full recipe in Components) — a number counts up from 0 to its target on first intersection (threshold 0.4), ease-out-cubic over `{motion.duration-count}`, landing on the exact target. **Decorative** → under reduced motion the value is painted at its final state immediately, with no `requestAnimationFrame` loop at all.

**Reduced motion is a global rule, not a per-component afterthought:**

```css
@media (prefers-reduced-motion: reduce) {
  [data-motion="decorative"] { animation: none !important; } /* bubble-float, any future mascot idle-loop */
  [data-reveal]:not(.is-visible) { opacity: 1 !important; transform: none !important; } /* scroll-reveal: appear immediately, don't gate on intersection */
  :root {
    /* these are the token names the recipes actually consume (see tokens.css) — collapsing
       them near-zero is how functional feedback like card-hover-lift stays visible-but-instant */
    --midu-duration-fast: 1ms;
    --midu-duration-base: 1ms;
    --midu-duration-slow: 1ms;
  }
}
```

Rule of thumb: **decorative/ambient/infinite motion (bubble float, mascot idle-loops, scroll-reveal entrance, stat count-up) is removed entirely; functional state-feedback motion (hover, focus, pressed, error, card-hover-lift) collapses to near-zero duration but is never removed** — a button still needs to visually register a click.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.sm}` | 8px | Tags, table cells, footer chips |
| `{rounded.md}` | 12px | Inputs, small tiles, thumbnails |
| `{rounded.lg}` | 20px | Cards, stat tiles |
| `{rounded.xl}` | 28px | Hero panels, section tints, mascot slots, modals |
| `{rounded.pill}` | 999px | Every button, tab, badge, progress track, toast |
| `{rounded.full}` | 9999px | Nutrient chips, avatar circles, icon buttons |

There is no square corner in this system. If a rectangle must read "technical" (a data table), use `{rounded.sm}` — never 0.

### Signature Motifs

- **Ruler ticks**: evenly spaced hairline marks on progress tracks, section dividers, and height-chart edges — the logo's "I" writ large.
- **Lightbulb dot**: the logo's idea-spark; usable as a list bullet in tips/advice content, and as the basis for a branded loading spinner (see Icons).
- **Reaching-child swoosh**: the logo's "U" figure; reserve for brand lockups, do not redraw as UI iconography.
- **Nutrient bubble cluster**: 3–5 spheres of varied sizes (one orange max), scattered with slight overlap around a focal image or stat.

## Icons

No icon system existed before this revision — a real gap the moment any nav, form, or social-share row extends past the current landing page.

- **Library**: [Lucide](https://lucide.dev) — round line-cap/line-join extends the "no sharp corners" rule already governing buttons, cards, and chips.
- **Style**: outline only, 2px stroke, round joins/caps. Never filled/solid or duotone — filled shapes belong to MIGI's illustration world; this preserves the illustration-vs-chrome boundary the Do/Don't section already draws for black outlines.
- **Sizes**: `icon-sm` 16px (inline with `{typography.body-sm}`/`{typography.caption}`) · `icon-md` 20px (default; nav, buttons, `{typography.body}`) · `icon-lg` 24px (standalone tap targets, empty-state accents). Icons under `{spacing.touch-target-min-decorative}` get a padded invisible hit area per Accessibility.
- **Color**: `{colors.ink}` on light surfaces, `{colors.on-primary}` on gradient/dark surfaces, `{colors.primary}` for interactive/link icons. Never gradient-fill an icon.
- **Don't** mix in a second icon library for one missing glyph, and don't recolor icons into `{colors.sun}` or the mascot palette — those hues are illustration-only.
- **Never use an emoji as a UI icon.** Emoji render differently per platform (Apple/Google/Windows/Android each ship their own) and carry uncontrollable color, breaking both visual consistency and the closed palette. Every glyph comes from Lucide; emoji remain legal only inside `{typography.sticker}` caption copy.

## Components

### Buttons

**`button-primary`** — The gradient pill. "Mua ngay", "Bắt đầu đo", every hero CTA.
- Background: linear-gradient 90° `{colors.grad-brand-start}` → `{colors.grad-brand-end}`, text `{colors.on-primary}`, type `{typography.button}`, rounded `{rounded.pill}`, padding 14px 28px.
- Hover: lift 1px + deepen shadow, `{motion.duration-fast}` `{motion.easing-standard}`; gradient itself doesn't change. Pressed: gradient darkens to `pressedGradientStart`/`pressedGradientEnd`, lift removed.
- Disabled: `{colors.disabled-bg}` background, `{colors.disabled-text}` text, `cursor: not-allowed`.
- Focus: global `:focus-visible` ring — see Accessibility. On this gradient background, the ring swaps to `{focus.ring-color-on-gradient}` (white).

**`button-secondary`** — White pill, 2px `{colors.primary}` border, `{colors.primary}` text. The calm partner ("Tìm hiểu thêm") beside every primary.
- Hover: fill `{colors.indigo-50}` behind the existing border/text.
- Disabled: `{colors.disabled-bg}` background, `{colors.disabled-text}` text/border.

**`button-sun`** — `{colors.sun}` pill with `{colors.ink}` text. Promotional moments only (sale badges, gamified actions, kid-facing screens). Never place it in the same group as `button-primary` twice — one sun per viewport.
- Hover/active: swap to `{colors.sun-500}` (one ramp step darker; `{colors.ink}` text stays comfortably AA).
- Disabled: `{colors.disabled-bg}` background, `{colors.disabled-text}` text.

**`button-primary-on-gradient`** — The primary CTA *when the surface behind it is already the brand gradient* (hero panel, footer band). A gradient pill on a gradient ground is invisible, so on these surfaces the primary action inverts: white fill `{colors.on-primary}`, `{colors.primary}` text, same `{typography.button}` / `{rounded.pill}` / `14px 28px` padding as `button-primary`. This does **not** create a second gradient — it *is* the one primary CTA for that view (the one-gradient-CTA law counts the gradient surface itself; the white pill sitting on it is the call to action).
- Hover: fill `{colors.indigo-50}`. Pressed: `{colors.indigo-100}`.
- Disabled: `rgba(255,255,255,0.35)` fill, `{colors.on-primary-soft}` text, `cursor: not-allowed`.
- Focus: global `:focus-visible` ring in `{focus.ring-color-on-gradient}` (white).

**`button-secondary-on-gradient`** — The calm partner beside `button-primary-on-gradient` on a gradient ground. Transparent fill, 2px `{colors.on-primary}` outline, white text.
- Hover: fill `rgba(255,255,255,0.12)` behind the existing outline/text.
- Focus: white `:focus-visible` ring. Neither on-gradient variant uses the gradient itself — that keeps the "one gradient per view" rule intact.

### Nutrient Chips

**`chip-nutrient`** — 48px-minimum circle, radial gradient `{colors.bubble-purple-light}` → `{colors.bubble-purple}` → `{colors.migi-deep}` (top-left to bottom-right), white specular dot top-right, uppercase white label (Ca+, K2, D3, Mg).
**`chip-nutrient-orange`** — 40px-minimum, `{colors.bubble-orange}` base, same anatomy. Only Arg wears orange; max one per cluster.
- Sizing uses `min-width`/`min-height` + `aspect-ratio: 1` + `overflow: visible`, not a fixed `size` — a hard pixel circle clips its uppercase label under a browser text-size override or 200% zoom (WCAG 1.4.4). If a label would exceed the circle at scaled sizes, let the radius fall back from `{rounded.full}` toward `{rounded.pill}` rather than clip.
- Clusters float around imagery with slight size variance (32–56px) and a `{motion.duration-float}` `{motion.easing-standard}` float animation that fully stops under `prefers-reduced-motion` (see Motion) — continuous ambient float is a known vestibular trigger even at reduced amplitude, so this is a full removal, not a slow-down.
- If ever made tappable: a bubble tap-bounce (scale `1 → 1.12 → 1`, `{motion.duration-fast}` `{motion.easing-emphasized}`) is the spec — see Motion.

### Cards & Containers

**`card`** — White, `{rounded.lg}`, `{spacing.lg}` padding, level-2 indigo shadow. Benefit cards, article cards, product tiles.
**`card-tinted`** — `{colors.surface-soft}` ground, no shadow. Use inside white sections for FAQs, testimonials.
**`stat-tile`** — White card whose number is set in `{typography.display}` `{colors.primary}` (or gradient-filled) with tabular figures, label in `{typography.eyebrow}` `{colors.magenta}`. For "+3–5cm/năm"-style claims, always with a source footnote in `{typography.caption}` — see Voice and Tone §2.
**`stat-counter`** — A `stat-tile` whose number **counts up from 0 to its target when it scrolls into view** (see Motion for the timing contract). The trust-number workhorse for the stat/CTA row.

- Markup — the label is the accessible source of truth; the animated numeral is hidden from screen readers so they never hear intermediate frames:

```html
<div class="stat-counter" role="img" data-target="91" data-suffix="+" aria-label="Hơn 91 khóa học trên toàn quốc">
  <span class="stat-counter__value" aria-hidden="true">0</span>
  <span class="stat-counter__label">khóa học trên toàn quốc</span>
</div>
```

- **Use real, sourced figures — never invent stats.** The example above is a real Midu company figure (source: midu.vn). Do not fabricate customer counts, satisfaction %, or ratings; if a real number isn't available, don't ship the stat.
- **`role="img"` + `aria-label` carry the accessible name** — the full value ("Hơn 91 khóa học trên toàn quốc") lives in the label, the animating numeral is `aria-hidden`. `aria-label` on a bare `<div>` (implicit `generic` role) is unreliably announced; `role="img"` makes the name dependable and the children presentational, so a screen reader hears the final figure once, never the intermediate frames.
- `.stat-counter__value` uses `font-variant-numeric: tabular-nums` so digit width is fixed and the layout doesn't jitter while counting. Value in `{typography.display}` `{colors.primary}`, label in `{typography.body-sm}` `{colors.ink-soft}`.
- Numbers are formatted with the **`vi-VN`** locale so the visible numeral matches Vietnamese convention ("10.000+", "4,9") and the `aria-label`. Never `en-US` here — "10,000" reads as a decimal to a Vietnamese user, and would contradict the label.
- Decimal precision is inferred from the `data-target` string: `data-target="4.9"` counts in tenths (0.0 → 4.9), never rounding through a wrong whole number. `data-suffix` appends `+`, `%`, etc.
- Counts **once** (the observer unobserves after firing); under `prefers-reduced-motion` it paints the final value immediately with no rAF loop; with no `IntersectionObserver` it also paints the final value (progressive enhancement). Any placeholder figure still carries an `*Illustrative` caption.

```js
(function () {
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var DURATION = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--midu-duration-count')) || 1600;
  function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }
  function decimalPlaces(s) { var i = s.indexOf('.'); return i === -1 ? 0 : s.length - i - 1; }
  function paint(node, v, d, suffix) {
    node.textContent = v.toLocaleString('vi-VN', { minimumFractionDigits: d, maximumFractionDigits: d }) + suffix;
  }
  function render(el, v) {
    var d = decimalPlaces(el.dataset.target);
    paint(el.querySelector('.stat-counter__value'), v, d, el.dataset.suffix || '');
  }
  function animate(el) {
    var t = parseFloat(el.dataset.target); if (isNaN(t)) return;
    var d = decimalPlaces(el.dataset.target);
    var node = el.querySelector('.stat-counter__value'); // resolve once, not per frame
    var suffix = el.dataset.suffix || '';
    if (prefersReduced) { paint(node, t, d, suffix); return; }
    var start = null;
    requestAnimationFrame(function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / DURATION, 1);
      paint(node, t * easeOutCubic(p), d, suffix);
      if (p < 1) requestAnimationFrame(step); else paint(node, t, d, suffix);
    });
  }
  var counters = document.querySelectorAll('.stat-counter[data-target]');
  if (!('IntersectionObserver' in window)) { counters.forEach(function (el) { render(el, parseFloat(el.dataset.target)); }); return; }
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { animate(e.target); obs.unobserve(e.target); } });
  }, { threshold: 0.4 });
  counters.forEach(function (el) { obs.observe(el); });
})();
```

**`mascot-slot`** — `{colors.surface-tint}` rounded-`{rounded.xl}` stage for a MIGI pose + `{typography.sticker}` hand-lettered caption. The pose may overflow the slot edge by up to 15%. The mascot illustration is reinforcement only — a real text string carrying the same information sits alongside it; see Accessibility.

### Commerce & Data

**`product-card`** — The online-store tile for a MenaQ7 SKU. Slots, top-to-bottom:
1. **Image slot** — 1:1, clipped to `{rounded.md}`, `opacity {motion.duration-base} {motion.easing-standard}` fade-in on load. Optional promo badge top-right on `{colors.sun}` with `{colors.ink}` text (ink-on-yellow law — never white).
2. **Name** — `{typography.title}`.
3. **Price** — đ-format, `{typography.body-lg}` weight 700 `{colors.primary}`.
4. **CTA** — "Mua ngay". **In a `{components.product-grid}` the cards use `{components.button-secondary}`** so the page keeps its single gradient CTA elsewhere (one-gradient-CTA law); a lone featured product outside a grid may use `{components.button-primary}`.
- States: default / hover (`{components.card-hover-lift}`) / out-of-stock (`{colors.disabled-bg}` image veil + `{colors.disabled-text}` "Hết hàng" text — never color-only).

**`ingredient-facts-table`** — The dosage/composition table (Ca, D3, K2 MenaQ7, Mg, Arg per serving) — MIDU's whole premise is ingredient science, so this is a first-class component, not a generic table. Nutrient label left, per-dose value right. Row rule 1px `{colors.hairline}` below each row; header `{typography.body-sm}` weight 700; cells `{typography.body-sm}` with unit qualifiers in `{typography.caption}`; outer clip `{rounded.md}` (the ≥8px table-corner rule holds); optional zebra `{colors.surface-soft}`. Every efficacy claim printed next to the table keeps its own `{typography.caption}` source line (Voice §2).

### Social Proof

Social proof is the core trust surface for a pediatric supplement — attribution is the mechanism, not decoration. Both cards sit on the `{colors.surface-tint}` skin (the testimonial-band ground).

**`testimonial-card`** — A parent's words. Slots, top-to-bottom:
1. **Attribution row** — avatar `{rounded.full}` 48px → name `{typography.body-sm}` weight 700 + child's age in `{typography.caption}` `{colors.ink-soft}` (e.g. "Mẹ Bột · con 4 tuổi").
2. **Excerpt** — `{typography.body}`, clamped to 3 lines (`-webkit-line-clamp: 3`).
3. **Optional "Xem thêm"** — `{typography.link}` to the full review.
Grid of 3 on desktop, horizontal scroll on mobile. A testimonial without a name + child's age fails brand review (attribution is what makes it trustworthy, not just a floating quote).

**`expert-endorsement-card`** — A clinician's endorsement, higher-authority than a parent quote. Slots:
1. **Attribution row** — doctor avatar 48px `{rounded.full}` → name `{typography.body-sm}` weight 700 + credential line in `{typography.caption}` `{colors.ink-soft}` (e.g. "BS.CKII · Nhi khoa").
2. **Quote** — `{typography.body}`, one claim, with a **mandatory `{typography.caption}` source line** (Voice §2) — an expert claim without a citation is worse than no claim.
3. **Optional `migi-love` accent** ≥120px (all Mascot rules apply; counts toward one-MIGI-per-viewport).
An expert quote missing its credential + source fails brand review.

### Hero & Sections

**`hero-gradient`** — Full-width brand-gradient panel, `{rounded.xl}` corners (full-bleed below `{breakpoints.mobile-l}`), `{spacing.xxl}` padding. One per page. Slots, top-to-bottom / left-to-right:
1. **Copy column (~55% width)** — `{typography.eyebrow}` badge (use `eyebrow-badge`, white ground) → `{typography.display-xl}` headline in `{colors.on-primary}` → optional subhead in `{colors.on-primary-soft}`.
2. **CTA row** (in the copy column) — `{components.button-primary-on-gradient}` + optional `{components.button-secondary-on-gradient}`. These are the view's CTAs; do not add a gradient pill here (the panel is already the gradient).
3. **Mascot column (~45% width)** — one MIGI pose ≥120px (`migi-hello`/`migi-measure` for a landing hero), may overflow the panel edge ≤15%.
4. **Bubble cluster** — one cluster only, scattered around the mascot, never overlapping the headline or CTAs.
Below `{breakpoints.mobile-l}` the columns stack (copy above mascot) and the split no longer applies.
**`section-tint`** — `{colors.surface-soft}` band for alternating rhythm: white → tint → white. Never two tinted sections adjacent.

### Forms

**`text-input`** — White, 1px `{colors.hairline-strong}`, `{rounded.md}`, 12px/16px padding. Focus: border becomes `{colors.primary}` + the global `:focus-visible` ring (see Accessibility) — replaces the previous low-alpha glow, which was too faint to reliably register as a focus indicator. Error: `{colors.semantic-error}` border + caption message; pair MIGI's cry pose *alongside* this message for empty states, never instead of it. Disabled: `{colors.disabled-bg}` background, `{colors.disabled-text}` text.

**`select-dropdown`, `checkbox`/`radio`, `toggle-switch`, `textarea`** — real needs (onboarding fields, reminder settings, consent capture) identified in this revision but not yet spec'd at full detail; tracked in Known Gaps as a v0.3 backlog rather than rushed.

**`date-picker`** — Same shell/states as `{components.text-input}` (`{colors.canvas}`, `{colors.hairline-strong}` border, `{rounded.md}`, `{typography.body}`), same focus/error/disabled behavior. Popover: level-2 elevation, `{rounded.md}`, month header in `{typography.eyebrow}`, today marked with a `{colors.sun}` dot (never the gradient), selected day fills `{colors.primary}`/`{colors.on-primary}`. Purpose: collects the child's birthdate, which drives age-appropriate MenaQ7 dosing — the first non-text form input this system needs in practice.

### Progress and Measurement

**`progress-ruler`** — The brand's own progress bar: `{colors.surface-soft}` pill track with hairline ruler ticks every 10%, `{colors.sun}`→`{colors.lime}` gradient fill, `{typography.caption}` tick labels beneath. Use for height tracking, quiz progress, loyalty points — anywhere growth is shown. On value change, animate the fill-width sweep (`{motion.duration-slow}` `{motion.easing-standard}`) with tick labels counting up in place, rather than snapping instantly — see Motion.

### Feedback

**`toast-snackbar`** — The brand's short confirmation for the daily habit loop: "Đã lưu chiều cao hôm nay!" Background `{colors.indigo-800}` (default), `{colors.semantic-success}`/`{colors.semantic-error}` for status variants — never the mascot's `{colors.migi-deep}`, which is illustration-only. Text `{colors.on-primary}`, type `{typography.body-sm}`, `{rounded.pill}`, elevation 3. States: entering / visible (auto-dismiss ~4s or swipe) / dismissing / with-icon (status variants always pair color with a glyph, never color alone — see Colors > Semantic). Slides up above the primary CTA's reach zone; never a second gradient surface competing with the one CTA on screen.

**`modal-dialog`** — The component that finally uses the elevation-3 + `{colors.overlay-scrim}` tokens this system already reserved. Background `{colors.canvas}`, `{rounded.xl}`, `{spacing.xl}` padding, scrim at ~50% opacity. Title `{typography.title}`, body `{typography.body}`. One `{components.button-primary}` action, one `{components.button-secondary}` exit — never two gradient pills in the same dialog. Destructive confirms set the secondary label in `{colors.semantic-error}` rather than adding a third button style. States: default / entering-exiting (fade+scale, `{motion.duration-base}`) / scrollable-body / destructive-confirm.

**`empty-state`** — MIGI fills the silence before data does — never a blank white card. Slots, top-to-bottom:
1. **Mascot** — one pose in a `{components.mascot-slot}`, ≥120px: `migi-hello`/`migi-measure` for first-run, `migi-cry`/`migi-sulk` for error/empty (soft, never blaming).
2. **Heading** — `{typography.title}` `{colors.ink}`, e.g. "Chưa có số đo nào".
3. **Body** — `{typography.body-sm}` `{colors.ink-soft}`, the real in-DOM text that carries the state (the mascot is reinforcement only — see Accessibility). For errors this is the actual error message, never mascot-only.
4. **CTA** — `{components.button-secondary}` (or `button-primary` if this is the page's one focal action), e.g. "Đo chiều cao đầu tiên nhé!".
States: first-run / error / with-CTA / informational-only.

**`inline-alert`, `tooltip`** — real needs (page-level notices distinct from per-field errors; inline jargon explanations for "K2 MenaQ7®") identified but not yet spec'd at full detail; tracked as v0.3 backlog.

### Navigation

**`top-nav`** — White bar, `min-height` 64px (not a fixed height, so it can grow if links wrap at larger text sizes), logo left, links center in `{typography.body-sm}` weight 500, `button-primary` right. Sticky with a level-2 shadow after scroll. Link hover and current-page both use `{colors.primary}` (current page additionally gets a 2px bottom-edge indicator). Mobile: hamburger overlay; the primary pill stays on the bar. Every link maintains a `{spacing.touch-target-min-decorative}` (44px) hit area via `inline-flex` + `padding-inline`, even though the visible text stays at body-sm size.

**`tabs`** — The pill track `{typography.button}`'s own hierarchy row already anticipated ("All buttons and pill tabs") but no component ever formalized. Track `{colors.surface-soft}`, `{rounded.pill}`; active tab lifts onto `{colors.canvas}` with `{colors.primary}` text, inactive tabs stay `{colors.ink-soft}`. Usage: "Biểu đồ / Lịch sử / Mẹo hay" — sibling views once height-tracking has more than one screen. States: active / inactive / hover / disabled / scrollable-overflow (mobile).

**`footer-gradient`** — The gradient reversed (magenta → indigo) as a full-bleed band, white outline logo variant, `{spacing.xxl}` padding. The page's closing brand moment. Slots, top-to-bottom:
1. **Logo + link columns** — white logo variant left; link columns with heads in `{typography.body-sm}` weight 700 `{colors.on-primary}`, links in `{colors.on-primary-soft}` (hover → `{colors.on-primary}`). Every link keeps the 44px hit area (`inline-flex` + `padding-inline`) like `top-nav`; white `:focus-visible` ring.
2. **Contact row** — hotline + Zalo, same link treatment as the columns.
3. **`legal-band`** — separated from the columns above by a 1px `rgba(255,255,255,0.24)` hairline. Carries, in `{typography.caption}` `{colors.on-primary-soft}`: the © line, and the **mandatory Vietnamese supplement disclaimer**:
   > "Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."

The legal-band disclaimer is a **regulatory requirement on every MIDU product-facing page**, not decoration — its absence is a compliance failure, flagged as a Blocker in the brand-review checklist. Exact wording is pending brand/legal-team confirmation (see Known Gaps); ship the standard formula above as the placeholder of record.

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

Rules: one MIGI per viewport · never mirror-flip (the coat, tie and "m" pocket badge break) · never recolor · minimum render height 120px so the glasses stay legible · `-plain` variants (no floating elements) are for tight layouts where bubbles would collide with UI · **every pose ships with a real, in-DOM text string conveying the same information — the illustration is reinforcement, never the sole carrier of state.** See Accessibility.

**Framing standard (v0.3.0):** every pose PNG is normalized so the character's bounding box fills **~85% of canvas height** (less for an unusually wide pose — a width clamp keeps arms/props from clipping the sides), horizontally centered, vertical margins split **54:46 top:bottom** (a grounded stance with slight headroom). This keeps mascots visually consistent in any grid regardless of pose (full-body vs close-up). Run `design-system/scripts/normalize_mascots.py <pose.png> <out.png>` on any new pose before adding it (canvas size defaults to the input's own resolution, so it never downscales a master). Normalization re-frames the transparent canvas only; it never crops into, flips, or recolors the character.

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

## Responsive Behavior

### Breakpoints

| Name | Token | Width | Key Changes |
|---|---|---|---|
| Desktop-XL | `{breakpoints.desktop-xl}` | 1440px | Content holds 1200px; gutters widen |
| Desktop | `{breakpoints.desktop}` | 1200px | Default 3-up card grids |
| Tablet | `{breakpoints.tablet}` | 960px | Grids 3-up → 2-up; nav collapses to hamburger |
| Mobile-L | `{breakpoints.mobile-l}` | 768px | Hero/tint panels go full-bleed (corners removed); MIGI moves below headline; fluid type is now continuous through this band instead of jumping |
| Mobile | `{breakpoints.mobile}` | 560px | display-xl reaches its 40px floor; pills go full-width; bubble clusters thin to 3 |
| Mobile-S | `{breakpoints.mobile-s}` | 400px | Stat tiles stack 1-up; footer columns collapse |

Reference these by token in new code, not raw pixel values — two undocumented breakpoints (860px, 700px) had already crept into shipped example code before these tokens existed.

### Touch Targets

- All pills ≥ `{spacing.touch-target-min}` (48px) tall on touch viewports (padding already guarantees this).
- Nutrient chips are decorative — if made tappable (ingredient info), enforce `{spacing.touch-target-min-decorative}` (44px) minimum and add the tap-bounce pressed state (see Motion).
- Inputs ≥ 48px tall.
- FAQ/accordion rows: the entire question row is the tappable trigger, min-height 48px, full-width — never just the disclosure icon.
- `top-nav` and `footer-gradient` text links: 44px hit area via `inline-flex` + `padding-inline`, even at body-sm visible text size.

### Collapsing Strategy

- **Hero**: two-column (copy | mascot) → stacked with mascot at 60% scale below the CTA pair. Never crop MIGI's head.
- **Nav**: links fold into a full-canvas overlay; logo and `button-primary` stay visible.
- **Stat rows**: 3-up → horizontal scroll snap at Mobile-L rather than stacking, keeping numbers comparable.
- **Progress-ruler**: tick labels drop to every 25% below 560px; the track never shrinks below 8px.

## Accessibility

**Focus.** All interactive elements (buttons, links, tabs, nav items, tappable chips, inputs) get, via `:focus-visible` only (never bare `:focus`, so mouse/touch interaction stays visually clean):

```css
:focus-visible {
  outline: {focus.ring-width} {focus.ring-style} {focus.ring-color};
  outline-offset: {focus.ring-offset};
}
.on-brand-gradient :focus-visible { outline-color: {focus.ring-color-on-gradient}; }
```

This is the one outline permitted on UI chrome — a different color, purpose, and pseudo-class from the Don'ts-list "no black outlines" rule, which bans decorative `{colors.ink}` comic strokes and does not apply here. On `button-primary`, `hero-gradient`, `footer-gradient` — anywhere the control sits directly on the brand gradient — swap to `{focus.ring-color-on-gradient}` (white), because an indigo ring on indigo-to-magenta collapses at the gradient's warm end. `text-input`'s previous ring (0.15-alpha, hover-adjacent glow) is replaced by this token; the border-color-to-primary shift on focus stays alongside it.

**Color is never the only signal.** `{colors.semantic-success}` and `{colors.semantic-error}` have near-identical luminance and sit on the axis deuteranopia/protanopia compress hardest. Every use pairs the color with a redundant signal: a glyph, an icon, or real text. Never ship a bare colored dot, pill, or row highlight — see Colors > Semantic.

**Mascot poses are reinforcement, never the sole carrier of state.** Every pose ships with a real, in-DOM text string conveying the same information (e.g. `migi-cry.png` + visible text "Không tìm thấy kết quả phù hợp"); the `<img>` gets `alt=""` (decorative) — the adjacent text carries the semantics, not the illustration. Applies especially to `migi-cry`/`migi-sulk` (errors/empty states), `migi-cheer`/`migi-celebrate`/`migi-wow` (success/milestones), and `migi-medicine` (dose reminders). The rule "prefer MIGI's cry pose over red banners" means pair the pose alongside the existing caption error message — it's the large color-only banner that's discouraged, never the text itself.

**Touch targets and zoom.** See Responsive Behavior > Touch Targets for the full list. `{components.chip-nutrient}` and `{components.top-nav}` use `min-width`/`min-height`/`aspect-ratio`/`overflow: visible` rather than a fixed `size`/`height`, so a browser text-size override or 200% zoom doesn't clip a label or crop a row of content.

**Motion sensitivity.** See Motion — decorative/ambient animation is removed entirely under `prefers-reduced-motion`, not merely slowed, since continuous floating content is a known vestibular trigger even at reduced amplitude.

**Language.** `<html lang="vi">` (or set per-locale dynamically) — this system is Vietnamese-first throughout; without an explicit `lang` attribute, screen readers default to English phoneme rules on Vietnamese diacritic text. No English-secondary-market plan currently exists; if one is added later, re-validate the eyebrow tracking and body line-height (both tuned for stacked Vietnamese diacritics) against plain Latin text, which will look comparatively loose.

## Iteration Guide

### What do I use for…

The fastest way to stay on-system: pick the component by the job, not by eyeballing a layout.

| You want | Use |
|---|---|
| Primary CTA | `{components.button-primary}` (one per viewport; on a gradient ground use `{components.button-primary-on-gradient}`) |
| Secondary action | `{components.button-secondary}` (`-on-gradient` variant on gradient grounds) |
| Promo / gamified action | `{components.button-sun}` (max one per viewport) |
| Section kicker / label | `{components.eyebrow-badge}` (`-on-tint` variant on `{colors.surface-soft}`) |
| Trust number that counts up | `{components.stat-counter}` |
| Progress toward a height goal | `{components.progress-ruler}` |
| Product tile with price + buy | `{components.product-card}` |
| Dosage / composition facts | `{components.ingredient-facts-table}` |
| Parent quote | `{components.testimonial-card}` |
| Doctor endorsement | `{components.expert-endorsement-card}` |
| Decorative delight | `{components.chip-nutrient}` cluster (one per section, one orange max) |
| Emotional state (error/empty/success) | MIGI pose per Mascot table + real text alongside |

#### Worked prompts

Copy-pasteable starting points — each names the components/tokens so the output stays on-system:

1. "Build a MIDU hero: `{components.hero-gradient}` slots in order — display-xl white headline left (~55%), `migi-hello.png` right at ≥120px, one bubble cluster, `{components.button-primary-on-gradient}` + `{components.button-secondary-on-gradient}`."
2. "Build a benefits band on white: three columns, each `{components.card}` with an icon-lg glyph, headline title, body copy, and a `{typography.caption}` source line under every efficacy claim."
3. "Add a stat row: three `{components.stat-counter}` on white — real Midu figures only, e.g. gần 20.000 chuyên gia đã đào tạo · 91+ khóa học toàn quốc · gần 300.000 phác đồ cá nhân hóa (nguồn: midu.vn) — tabular numerals. Never invent customer counts, %, or ratings."
4. "Build a product grid: `{components.product-grid}` of `{components.product-card}` — cards use `{components.button-secondary}`, the page keeps its single gradient CTA in the hero."
5. "Build a testimonial band on `{colors.surface-tint}`: three `{components.testimonial-card}` with avatar, name + tuổi con, 3-line excerpt; one `{components.expert-endorsement-card}` with credential + source line."
6. "Build an error state: `{components.empty-state}` with `migi-cry.png`, a soft never-blaming headline, real body text explaining the fix, and a `{components.button-secondary}` retry — no gradient CTA on error surfaces."

### Working rules

1. Reference components by token name (`{components.button-primary}`, `{components.progress-ruler}`) when asking for changes.
2. Choose the section ground first — `{colors.canvas}` or `{colors.surface-soft}` — before styling anything inside it.
3. Default text to `{typography.body}`; escalate to display sizes only for the one focal message per viewport.
4. New button variants must stay pill-shaped and must not invent new fills — derive from gradient, white+border, or sun.
5. When a screen feels flat, the fix order is: (a) add whitespace, (b) add one bubble cluster, (c) add a MIGI pose — never a new color.
6. Reference mascot poses by filename (`migi-hello.png`) — resolution/location is a build concern documented in the kit's README/skill, not a design one.
7. Validate token references and contrast after edits. Known traps: white text on `{colors.sun}` (always use `{colors.ink}`), `{colors.magenta}` eyebrows on `{colors.surface-soft}` (use `{components.eyebrow-badge-on-tint}`, now mandatory), white labels on `{colors.bubble-orange}` (decorative only — exempt from AA, but never make the orange bubble a text-bearing control), and a fixed `size`/`height` on any component that holds user-facing text (use `min-*` instead — see Accessibility).
8. New additive changes (a token, a component, a pose mapping) bump MINOR and get a Changelog entry; renaming/removing a token, or changing an *existing* token's value, bumps MAJOR and needs a grep-and-update pass — see Governance.

## Known Gaps

- **Font licensing** — FZ Rubik ships in `design-system/fonts/` from the company's font pack; confirm the license covers web embedding (`@font-face`) before public deployment. Do not substitute Google-Fonts Rubik for Vietnamese copy (it has no Vietnamese subset — diacritics would render in a mismatched fallback face mid-word).
- **`tnum` OpenType feature is unverified.** `{typography.display}` now declares `fontFeature: kern, tnum` for tabular stat-numeral alignment, but whether the bundled FZ Rubik 900 cut actually ships a `tnum` feature hasn't been checked against the font file. Verify before relying on it; if absent, digit alignment falls back to proportional (a cosmetic regression, not a breaking one).
- **The tagline script face is unidentified.** Quicksand approximates its thin rounded geometry; the original may be a Vietnamese foundry face (UTM/SVN family). Confirm before print work.
- **The guideline PDF documents only palette, logo variations, and font weights** — spacing, radii, elevation, components, breakpoints, motion, focus, and the tint/shade ramps in this file are *derived* from the brand's visual logic, not from an official spec. Treat them as the proposed system, adjustable as the brand team weighs in.
- **Dark mode: starting palette only, no component pass.** Canvas `{colors.indigo-900}`, surface `{colors.indigo-800}` — not `{colors.migi-deep}`, which is a saturated brand purple that would vibrate against gradient CTAs on a dark ground. Text/link accents: `{colors.indigo-300}`/`{colors.magenta-300}`; larger fills: `{colors.indigo-400}`/`{colors.magenta-400}`. `{colors.sun}`/`{colors.ink}` pairing (`button-sun`) is already dark-mode-agnostic — no change needed there. This commits only the palette; no component has an actual dark variant built yet.
- **Photography is out of scope for this round.** The system as specified is 100% illustrated (MIGI + nutrient bubbles); zero real-photo guidance exists. Before any real parent+child photography ships (testimonials, packaging, ads), this file needs a Photography section — color grade to sit next to the indigo/magenta palette, cropping against the shape system, and whether bubbles/gradient may overlay a photo.
- **Form controls beyond text-input and date-picker are backlog, not spec'd.** `select-dropdown`, `checkbox`/`radio`, `toggle-switch`, `textarea`, `inline-alert`, `tooltip`, `avatar`, `skeleton`/`loading`, `accordion`, `stepper`, `tag`/`badge` (non-nutrient), `breadcrumb`/`pagination` are all real, identified needs — see the component gap-analysis that produced this revision. (`table` shipped in v0.3.0 as `{components.ingredient-facts-table}`; the generic-`table` and remaining form controls stay backlog.) Track as a future round.
- **Legal disclaimer wording pending confirmation.** The footer `legal-band` ships the standard Ministry-of-Health supplement formula ("Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."); confirm the exact required wording with the brand/legal team before print or paid-media use.
- **MIGI mascot is official but not yet in the text knowledge base.** MIGI, the giraffe-doctor, is confirmed by the brand owner as MIDU's **official mascot** — treat it as canonical identity throughout this kit. It simply isn't documented in the company knowledge base (`Z:\DU LIEU MIDU\MIDU BRAIN`), which holds medical/training/brand-strategy knowledge rather than a complete visual-asset registry — so the strings "MIGI"/"hươu"/"giraffe" returning zero matches there is expected, not a provenance flag. Other KB-confirmed brand facts (Công ty CP Midu MenaQ7, founded 2022, first in Vietnam to pioneer Vitamin K2/MenaQ7 from Natto Pharma, Norway; product line 45/180/360 mcg) stand alongside it.
- **Print values**: the guideline lists CMYK equivalents (e.g. indigo 95/82/3/0, magenta 6/93/1/0); this file is screen-first and records hex only.
- **Vector sources are not in this kit.** The original `.ai`/`.pdf` files (mascot vectors, logo, guideline) live in the brand team's Drive folder; the kit ships rasterized PNGs (1871px mascot poses, 1224px logo), which cover web use but not large-format print. Request the vector files from the brand team for print work.

## Changelog

### 0.3.0 — this round
- Added: `stat-counter`, `product-card`, `ingredient-facts-table`, `testimonial-card`, `expert-endorsement-card`, `button-primary-on-gradient`, `button-secondary-on-gradient` components.
- Added: `colors.on-primary-soft` (contrast-verified 4.61:1 at the magenta pole) and `motion.duration-count` (1600ms, single-purpose) tokens.
- Added: Page Anatomy section (canonical landing order + density table); Motion scroll-reveal / card-hover-lift / stat-counter contracts; footer `legal-band` with the mandatory Vietnamese supplement disclaimer.
- Added: `cursor: pointer` rule for enabled interactive elements; explicit no-emoji-as-icons rule (Icons + Do/Don't).
- Added: mascot framing standard (~85% canvas-height, 54:46 margins) + `design-system/scripts/normalize_mascots.py`; all MIGI poses normalized (21 full-res masters + 19 skill-bundled copies).
- Added: Iteration Guide role→token lookup table and six worked prompts.
- Changed: `hero-gradient`, `empty-state`, `footer-gradient` rewritten as numbered slot lists; `table` need shipped as `ingredient-facts-table` (removed from backlog).

### 0.2.0 — this round
- Added: indigo/magenta/sun tint-shade ramps (50–900), `disabled-bg`/`disabled-text`, `hairline-strong`.
- Added: `breakpoints`, `container`, `motion`, `focus` token blocks; `spacing.touch-target-min(-decorative)`.
- Added: `typography.link`; fluid `clamp()` sizing for display-xl/display/headline; tabular-figure `fontFeature` on `display`.
- Added: `toast-snackbar`, `empty-state`, `modal-dialog`, `date-picker`, `tabs`, `product-grid` components.
- Added: Voice and Tone, Icons, Motion, Data Visualization, Accessibility, Governance sections.
- Changed: `text-input` border → `hairline-strong`; `chip-nutrient`/`top-nav` to `min-*` sizing (was fixed px); `caption`/`eyebrow`/`body`/`display-xl`/`headline` line-heights raised for Vietnamese diacritic safety and 4px-grid alignment.
- Changed: `eyebrow-badge-on-tint` is now mandatory on `{colors.surface-soft}` grounds (was "usually").

### 0.1.0 — alpha (previous)
- Initial system derived from the brand guideline PDF (palette, logo, font weights) plus derived spacing/radii/elevation/components/breakpoints.

## Governance and Change Proposals

- **Owner**: design-system owner — TBD. Until named, route proposals to the brand team lead.
- **How to propose a change**:
  1. State which token(s)/section(s) change and why.
  2. Tag **additive** (new token/component/pose) or **breaking** (renamed/removed token, or a value change to an *existing* token).
  3. Additive → one reviewer approves; bump MINOR; add a Changelog entry.
  4. Breaking, or anything touching colors/logo/core typography sourced from the official guideline PDF → requires brand-team sign-off; bump MAJOR; grep the codebase for the old token name before merging.
  5. Purely derived sections (spacing, radii, elevation, breakpoints, motion, focus, ramps) can be adjusted with design-team-only approval unless the change visibly shifts brand feel.
