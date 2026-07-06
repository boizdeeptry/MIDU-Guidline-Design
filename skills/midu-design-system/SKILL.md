---
name: midu-design-system
description: Design system for the MIDU MenaQ7 brand (Vietnamese children's height-supplement, mascot MIGI the giraffe doctor). Use whenever building, styling, or modifying ANY user-facing UI for MIDU — landing pages, web apps, emails, banners, components. Triggers on "MIDU", "MenaQ7", "MIGI", "chuyên gia chiều cao", or any UI work inside a MIDU project. Load BEFORE writing the first line of markup or CSS.
---

# MIDU MenaQ7 Design System

One signature gradient, one giraffe doctor, floating nutrient bubbles, everything rounded. Clinical credibility wrapped in cartoon warmth.

Full specification: `references/DESIGN.md` (token frontmatter + complete spec). Ready-to-paste CSS variables: `references/tokens.css`. Mascot art + logo lockup: `assets/`.

## When to Activate

- Building any MIDU-branded surface: landing page, app screen, email, ad banner, packaging mock
- Styling components (buttons, cards, forms, progress bars) in a MIDU project
- Choosing colors, fonts, spacing, or imagery for MIDU content
- Adding mascot/illustration to a MIDU screen

## Before You Build (required)

For any NEW page or app, do NOT write code yet. First resolve the points below — use the **AskUserQuestion** tool (one round, max 4 questions) when available, otherwise ask in chat. Skip anything the request already answers.

1. **Deliverable & stack** — static HTML (kit default for one-pagers) · Next.js + Tailwind · React SPA · email template?
2. **Deployment** — Vercel · Netlify · company server · files only? (decides font loading, analytics, form handling)
3. **Data & backend** — pure static · lead-capture form (submissions go where: Supabase, Google Sheets, existing API?) · CMS content?
4. **Content readiness** — approved copy/figures available, or build with placeholders? All placeholder claims MUST carry an `*Illustrative` caption; health copy needs the "not a medicine" disclaimer in the footer.

Defaults when the user says "up to you": static HTML for one-pagers; Next.js + Tailwind on Vercel for anything with routes/data; Supabase for form storage. State the chosen stack in one line before building.

### Stack notes

- **Static HTML**: self-contained page; embed FZ Rubik as woff2 data URIs or copy `design-system/fonts/`. Always start with `<meta charset="utf-8">` — Vietnamese text renders as mojibake without it when opened locally.
- **Tailwind**: map tokens into `theme.extend` (colors from the quick-reference table, `borderRadius: {pill:'999px'}`, `boxShadow` with the indigo-tinted values). Do not use default Tailwind grays/shadows.
- **Next.js**: load FZ Rubik via `next/font/local` (weights 400/500/700/900) from `design-system/fonts/FzRubik/`; expose as a CSS variable and wire it into Tailwind `fontFamily`.
- **Vercel/Netlify**: nothing brand-specific; confirm the FZ Rubik license covers public web embedding before deploying.
- **Supabase forms**: validate inputs client + server side; error states use `#C93A3A` with a helpful Vietnamese message, never a bare red banner — pair empty/error states with MIGI cry/sulk poses.

## Non-Negotiables

These rules are load-bearing. Violating any of them breaks the brand:

1. **One gradient pill per viewport.** Every primary CTA is the indigo→magenta gradient (`#384B98` → `#C1368D`, left→right). Never two gradient CTAs visible at once; never use the gradient on body text, icons, or borders. (Display headlines MAY use gradient text-fill on white grounds.)
2. **Ink on yellow, always.** Text on `#EFCA3D` (Sun) is `#221F1F` — white-on-yellow fails contrast at every size.
3. **No sharp corners anywhere.** Buttons = pill (999px). Cards ≥ 20px. Data tables minimum 8px. A square corner is off-brand.
4. **Black outlines belong to illustration only.** MIGI and stickers have comic outlines; UI chrome never gets black borders (use `#DDE2F0` hairline).
5. **Two yellows, never swapped.** UI yellow = `#EFCA3D` (Sun). Giraffe coat = `#FFDA69` (MIGI Yellow). Different temperatures on purpose.
6. **No new hues.** The palette is closed: indigo, magenta, sun/lime, the mascot's purple family, and two semantic tones.
7. **Vietnamese-safe typography.** The brand face is **FZ Rubik**, bundled in the kit at `design-system/fonts/FzRubik/` (weights 300–900, full Vietnamese) — register with `design-system/fonts/fzrubik.css`, stack `"Fz Rubik", system-ui, sans-serif`. NEVER substitute Google-Fonts Rubik (it has no Vietnamese subset — diacritics render in a mismatched fallback face mid-word). Body line-height ≥ 1.5 so stacked diacritics (ắ ễ ộ) don't clip. Test string: "Chuyên gia chiều cao".

## Token Quick Reference

<!-- Condensed from references/DESIGN.md frontmatter — when tokens change there, update these tables too. -->

### Colors

| Token | Hex | Role |
|---|---|---|
| primary (Indigo) | `#384B98` | Trust — headings, secondary-button text/border, links |
| magenta | `#C1368D` | Warm gradient pole — eyebrows, active states |
| grad-brand | `#384B98 → #C1368D` | Primary CTAs, hero panels, footer (reversed OK in footer only) |
| sun / lime | `#EFCA3D` / `#E4E254` | Energy accent, progress fill (as sun→lime gradient) |
| ink | `#221F1F` | Text on light surfaces |
| canvas | `#FFFFFF` | Default page ground |
| surface-soft | `#EEF1FA` | Alternating tinted sections |
| surface-tint | `#F7F4FB` | Mascot slots, testimonials |
| hairline | `#DDE2F0` | Borders (indigo-biased, never grey) |
| bubble-purple / bubble-orange | `#5F469B` / `#F68500` | Nutrient spheres (Arg is the only orange one) |
| success / error | `#2E7D46` / `#C93A3A` | AA-compliant on white |

### Typography (FZ Rubik)

| Role | Size/Weight | Notes |
|---|---|---|
| display-xl | 64px / 900 | Heroes; may wear gradient fill; lh 1.05 |
| display | 44px / 900 | Section openers, stat numbers |
| headline | 30px / 700 | Group titles |
| title | 22px / 700 | Card/modal titles |
| body-lg | 18px / 500 | Lead paragraphs |
| body | 16px / 400 | Default; lh 1.6 |
| button | 16px / 700 | All pills |
| eyebrow | 13px / 700 | UPPERCASE, +1.5px tracking, magenta, usually in a pill badge |
| caption | 12px / 500 | Sources, disclaimers |

Weights: 900 for moments, 700 for structure, 400–500 for reading. Skip 600.

### Shape & Space

- Radius: 8 / 12 / 20 / 28 / pill(999). Spacing: 4 / 8 / 12 / 16 / 24 / 32 / 48 / section 80. Base unit 8px.
- Max content width 1200px. Alternate white / surface-soft sections; never two tinted sections adjacent.
- Shadows are indigo-tinted: `0 8px 24px rgba(56,75,152,.10)` cards, `0 16px 40px rgba(56,75,152,.16)` floating. Never grey shadows.

## Component Recipes

Recipes use the variables from `references/tokens.css` — paste that file into the project first, so token values live in exactly one place.

```css
/* Primary CTA — the brand handshake */
.btn-primary {
  background: var(--midu-grad-brand);
  color: var(--midu-on-primary); font-weight: 700;
  border-radius: var(--midu-r-pill); padding: 14px 28px; border: 0;
}
/* Secondary partner */
.btn-secondary {
  background: var(--midu-canvas); color: var(--midu-primary);
  border: 2px solid var(--midu-primary); border-radius: var(--midu-r-pill); padding: 12px 26px;
}
/* Sun — promos/gamification only, max one per viewport */
.btn-sun { background: var(--midu-sun); color: var(--midu-ink); border-radius: var(--midu-r-pill); padding: 14px 28px; }

/* Nutrient bubble (decorative, 3–5 per cluster, one orange max) */
.bubble {
  border-radius: 50%; color: #fff; font-weight: 700;
  background: var(--midu-grad-bubble); /* orange variant: var(--midu-grad-bubble-orange) */
}

/* Progress "ruler" — the brand's measurement motif */
.ruler-track { height: 12px; border-radius: var(--midu-r-pill); background: var(--midu-surface-soft); }
.ruler-fill  { height: 100%; border-radius: var(--midu-r-pill); background: var(--midu-grad-sun); }
/* tick marks: repeating-linear-gradient(90deg, transparent 0 calc(10% - 1px), var(--midu-hairline) calc(10% - 1px) 10%) */
```

Full component specs (nav, footer, inputs, stat tiles, hero, mascot slots): `references/DESIGN.md` → Components.

## Logo

Files in `assets/`: `logo-midu.png` (color, light grounds), `logo-midu-white.png` (on gradient/dark imagery), `logo-midu-tagline.png` (lockup — prefer on first appearance per surface).

Rules: clearspace = height of the "m" on all sides · min width 96px · never stretch, rotate, outline, recolor, or detach the lightbulb/ruler/child elements from the wordmark.

## Mascot: MIGI

Transparent PNGs in `assets/` (560px; full-res 1871px lives in the source project's `design-system/assets/`). Map pose to UX moment:

<!-- Canonical table: references/DESIGN.md → "Mascot Usage (MIGI)". Keep in sync. -->

| File | Use for |
|---|---|
| `migi-hello.png` | Onboarding, welcome, chat greeting |
| `migi-measure.png` | Height input, growth-chart empty state |
| `migi-medicine.png` | Dose reminders, usage guide |
| `migi-cheer.png` / `migi-celebrate.png` | Goals reached, streaks |
| `migi-wow.png` | Achievements, feature reveals |
| `migi-love.png` / `migi-grin.png` | Reviews, thank-you |
| `migi-cry.png` / `migi-sulk.png` | Errors, empty results (soft, never blaming) |
| `migi-goodnight.png` | Evening reminders, sleep content |
| `migi-exercise.png` | Activity tips, challenges |
| `migi-birthday.png` | Birthday coupons |
| `migi-bye.png` / `migi-wave-fullbody.png` | Logout, order-complete send-off |

`-plain` variants = no floating elements, for tight layouts.

**Rules:** one MIGI per viewport · never mirror-flip (coat, tie, pocket badge break) · never recolor · min render height 120px (glasses must stay legible) · at icon sizes use the lightbulb dot or logo "m" instead · mascot may overflow its container edge by ≤15% (never `overflow:hidden` a mascot slot).

## Fix Order for Flat-Feeling Screens

(a) add whitespace → (b) add ONE nutrient-bubble cluster → (c) add a MIGI pose. **Never** a new color.

## Before Marking UI Done

- [ ] Exactly one gradient CTA visible per viewport
- [ ] No square corners, no black UI borders, no grey shadows
- [ ] Yellow surfaces carry ink text
- [ ] Vietnamese diacritics render in one face, nothing clips (test: "Chuyên gia chiều cao")
- [ ] Growth/health claims have a caption source line
- [ ] Mascot (if any): right pose for the moment, not flipped, not recolored
