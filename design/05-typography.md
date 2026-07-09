## Typography

### Font Family

The system pairs **two** faces (v0.4.0) — a characterful display face and a clean reading face — both with full Vietnamese:

- **FZ Rubik** (`{typography.*.fontFamily}` = display) — The brand's **display/title** face: `display-xl`, `display`, `headline`, `title`, `button`, `eyebrow`, and stat numerals. Bundled at `design-system/fonts/FzRubik/` (TTF, weights 400/500/700/900, full Vietnamese — verified; the scale never uses 300/600/800). Register with `design-system/fonts/fzrubik.css`, token `{colors...}` — use `var(--midu-font-display)` / stack `"Fz Rubik", system-ui, sans-serif`. **Never** substitute Google-Fonts Rubik (no Vietnamese subset); the bundled cut is the Vietnamese-adapted "Rubik MKT". Its rounded, friendly geometry carries brand personality but reads heavy in long paragraphs — which is why body copy moves to Lexend.
- **Lexend** (`{typography.body*/caption.fontFamily}`) — The **reading/body** face: `body-lg`, `body`, `body-sm`, `caption`, and link text. A Google Fonts (OFL) humanist sans **tuned for reading fluency**, with a full Vietnamese subset (verified). Bundled at `design-system/fonts/Lexend/` (woff2, weights 400/500/700, vietnamese+latin+latin-ext subsets); register with `design-system/fonts/lexend.css`, use `var(--midu-font-body)` / stack `"Lexend", "Fz Rubik", system-ui, sans-serif` (Rubik is the fallback so a load failure still renders Vietnamese correctly). The pairing rule: **Rubik for anything display-sized or a title; Lexend for anything you actually read.**
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

