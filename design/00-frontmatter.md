---
version: 0.4.0
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
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: 0
    fontFeature: kern
  body:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
    fontFeature: kern
  body-sm:
    fontFamily: Lexend
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
    fontFamily: Lexend
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

