---
name: midu-design-system
description: Design system + build workflow for the MIDU MenaQ7 brand (Vietnamese children's height-supplement, mascot MIGI the giraffe doctor). Use whenever building, styling, or modifying ANY user-facing UI for MIDU — landing pages, web apps, emails, banners, components. Runs a self-contained brainstorm → brief → plan → build → review pipeline (HARD-GATE: no code before the brief is confirmed). Triggers on "MIDU", "MenaQ7", "MIGI", "chuyên gia chiều cao", or any UI work inside a MIDU project. Load BEFORE writing the first line of markup or CSS.
---

# MIDU MenaQ7 Design System

One signature gradient, one giraffe doctor, floating nutrient bubbles, everything rounded. Clinical credibility wrapped in cartoon warmth.

Full specification: `${CLAUDE_SKILL_DIR}/references/DESIGN.md` (token frontmatter + complete spec). Ready-to-paste CSS variables: `${CLAUDE_SKILL_DIR}/references/tokens.css`. Mascot art + logo lockup: `${CLAUDE_SKILL_DIR}/assets/`.

**Locating bundled files (fonts, mascots, logos).** `${CLAUDE_SKILL_DIR}` and `${CLAUDE_PLUGIN_ROOT}` are auto-substituted to real paths when the plugin is installed — use them directly. **If you ever see the literal string `${CLAUDE_PLUGIN_ROOT}` unresolved** (older Claude Code, or you only have a copied `DESIGN.md`), don't go hunting blindly: the files are in the installed plugin cache at `~/.claude/plugins/cache/midu-skills/midu-vibecoder-kit/<version>/design-system/` (fonts under `fonts/`, art under `assets/`), or in the kit repo **https://github.com/boizdeeptry/MIDU-Guidline-Design**. Fonts: **FZ Rubik ships as TTF** (`fonts/FzRubik/*.ttf`), **Lexend as woff2** (`fonts/Lexend/*.woff2`) — for a self-contained page just inline the pre-built `design-system/preview-src/fonts.css` (every face, data-URI). For a self-contained page, mascot/logo PNGs must likewise be embedded as data URIs (see the build scripts in `examples/`), not linked by path.

## When to Activate

- Building any MIDU-branded surface: landing page, app screen, email, ad banner, packaging mock
- Styling components (buttons, cards, forms, progress bars) in a MIDU project
- Choosing colors, fonts, spacing, or imagery for MIDU content
- Adding mascot/illustration to a MIDU screen

## Build Workflow (required for any new page/app)

This skill runs a self-contained pipeline — **brainstorm → brief → plan → build → review** — the same shape as `/discuss → /plan → /execute → /ship`, but bundled in the plugin so it works for anyone, with no `.planning/` folder or external skill needed. Run the phases in order. The phases are lightweight (a small edit is one quick loop; a full site is a fuller one) but **none is skippable for a new surface**.

**HARD-GATE: do not write a single line of markup or CSS until (a) you've ASKED the user the deliverable/stack (Phase 1, item 2) and (b) you've stated the brief and the user has confirmed it (a simple "OK" counts).** The gate is on *the user choosing the stack and confirming the plan*, not on interrogating them about everything — the failure it prevents is silently auto-defaulting the deliverable (e.g. "it's a static HTML file so I'll just rebuild it") and shipping before anyone agreed to it. The stack is a real fork in the deliverable; it is asked, never assumed.

### Phase 1 — Brainstorm (infer first, ask only what's load-bearing)

Two opposite failures are in tension here — **interrogating** the user with questions you could answer yourself, and **silently auto-deciding** something material and burying it as a default. Resolve it with one rule: **infer everything you can, but ASK the deliverable/stack — always.**

**The deliverable/stack is the ONE required question. Ask it up front with a single AskUserQuestion, before you write the brief — never infer it, never fold it into the brief as a "default" for the user to rubber-stamp.** It changes the entire build (a share-and-view file vs a web-app with a real form/DB), so the user must actually choose it. Everything else you infer and state as assumptions in the brief for the user to correct.

The four things the brief must resolve:

1. **Goal & audience** — what the surface accomplishes and who it's for. **Infer** from the request/source; state it in the brief. Ask only if it genuinely flips the whole design.
2. **Deliverable & stack** — **ALWAYS ASK (do not infer, do not default).** Present the real options with their tradeoff so the choice is informed: **static self-contained HTML** (one file, opens/shares anywhere, no server — fits a stand-alone one-pager) · **Next.js + Tailwind** (real forms saved to a DB, SEO/analytics, part of a larger site — needs Node + deploy) · React SPA · email. You MAY mark a recommendation, but the user picks. (Even when a source `.html` or "just a one-pager" strongly implies static — still ask; confirming a strong inference costs one click, auto-defaulting it is the exact miss to avoid.)
3. **Deployment & data** — follows from the stack answer. If they picked a form-bearing stack, confirm where data goes; otherwise it's static, don't belabor it.
4. **Content & data source** — **non-negotiable to get right, usually answerable without asking:** real facts come from the user's provided material or the company KB (`Z:\DU LIEU MIDU\MIDU BRAIN` when present) — **never invented** (Non-Negotiable #13, DESIGN.md Voice §5). No real figure available → labelled placeholder, not a fabricated number.

Rule of thumb: **the stack question always fires** (item 2). Beyond it, a rebuild of provided content needs ~0 further questions (infer, state assumptions); a brand-new site from a one-line request maybe 1 more. Batch any extra into the **same** AskUserQuestion round as the stack — one round, never a barrage.

### Phase 2 — Brief (confirm before building)

Write back a short brief (5–8 lines) and get an explicit "yes": goal + audience · **the deliverable/stack the user picked in Phase 1** · the page sections in order (per DESIGN.md → Page Anatomy) · which components/tokens each uses · where every real fact/figure comes from (or which are labelled placeholders). This is the gate — wait for confirmation. For a genuinely tiny change (one component tweak), a one-line brief is enough, but still confirm.

### Phase 3 — Plan

Turn the brief into an ordered build list: section by section, top to bottom, naming the component per slot (use the "What Do I Use For…" table below) and the exact token values. Note the one gradient CTA's location up front so the rest stay secondary.

### Phase 4 — Build

Implement against the plan using the tokens/components/recipes below. Obey every Non-Negotiable. Pull real facts from the data source resolved in Phase 1 — **never fabricate** dosages, prices, stats, names, or citations. State the chosen goal/stack in one line as you start.

### Phase 5 — Review

Before calling it done, run the "Before Marking UI Done" checklist at the end of this skill, then audit against the **midu-brand-review** skill (or its checklist). Fix blockers before shipping.

### Stack notes

- **Static HTML** (self-contained single file): assemble it with a **Node** build script. Two hard rules learned the hard way:
  - **Use Node, not Python.** Node ships with Claude Code; many machines have **no Python** (`node build.mjs`, never `python build.py`, for a page you generate for a user).
  - **NEVER open `${CLAUDE_PLUGIN_ROOT}/design-system/preview-src/fonts.css` with the Read tool** — it's ~600KB (~600k tokens) and blows past the tool's 25k-token cap, so the read just fails. A build script reads it **from disk by path**; the bytes never enter your context.

  Pattern — a `template.html` with `__FONT_CSS__` and image placeholders, plus a tiny `build.mjs`:
  ```js
  // build.mjs — run: node build.mjs   (Node only; no Python, no Read-tool on fonts.css)
  import { readFileSync, writeFileSync } from "node:fs";
  const KIT = "${CLAUDE_PLUGIN_ROOT}/design-system"; // or a local copy of design-system/
  let html = readFileSync("template.html", "utf8")
    .replace("__FONT_CSS__", readFileSync(`${KIT}/preview-src/fonts.css`, "utf8"));
  for (const [token, file] of [["__LOGO_WHITE__", `${KIT}/assets/logo-midu-white.png`]]) {
    html = html.replaceAll(token, `data:image/png;base64,${readFileSync(file).toString("base64")}`);
  }
  writeFileSync("index.html", html);
  ```
  `fonts.css` already carries FZ Rubik + Lexend (+ Quicksand/Patrick Hand) as base64 — the script splices it in untouched. (Embedding by hand instead? Raw files are **FZ Rubik = TTF** in `fonts/FzRubik/`, **Lexend = woff2** in `fonts/Lexend/`.)
  - **Simpler, no-build option:** copy `design-system/fonts/` next to your HTML and `<link>` its `fzrubik.css` + `lexend.css` — a small portable folder, no script and no giant file at all.
  - Either way, start the HTML with `<meta charset="utf-8">` or Vietnamese renders as mojibake when opened locally.
- **Tailwind**: map tokens into the theme (Tailwind 4 `@theme` in CSS, or v3 `theme.extend`) — colors from the quick-reference table, `borderRadius: {pill:'999px'}`, indigo-tinted `boxShadow`; never default Tailwind grays/shadows. **Tailwind v4 gotcha:** Preflight removed `cursor:pointer` from `<button>`, so a `<button>` CTA shows the default arrow (breaks Non-Negotiable #11). Add once in your global CSS: `button:not(:disabled),[role="button"]:not(:disabled){cursor:pointer} button:disabled{cursor:not-allowed}`. (`<a>` links are unaffected.)
- **Next.js**: load FZ Rubik (display) via `next/font/local` (weights 400/500/700/900) from `${CLAUDE_PLUGIN_ROOT}/design-system/fonts/FzRubik/`, and Lexend (body) via `next/font/google` (`subsets: ["vietnamese","latin"]`, weights 400/500/700); expose both as CSS variables and wire into Tailwind — a display family (Rubik) and body family (Lexend). See `examples/midu-landing-next/` for the exact wiring.
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
7. **Vietnamese-safe typography — a two-face pairing.** Display/titles use **FZ Rubik**; reading text uses **Lexend** — BOTH carry a full Vietnamese subset. FZ Rubik is bundled at `${CLAUDE_PLUGIN_ROOT}/design-system/fonts/FzRubik/` (weights 400/500/700/900) — register with `${CLAUDE_PLUGIN_ROOT}/design-system/fonts/fzrubik.css`; use `var(--midu-font-display)` for display-xl/display/headline/title/button/eyebrow/stat numerals. Lexend is bundled at `${CLAUDE_PLUGIN_ROOT}/design-system/fonts/Lexend/` (weights 400/500/700) — register with `${CLAUDE_PLUGIN_ROOT}/design-system/fonts/lexend.css`; use `var(--midu-font-body)` (`"Lexend","Fz Rubik",system-ui,sans-serif`) for body/body-lg/body-sm/caption/links. NEVER substitute Google-Fonts Rubik (it has no Vietnamese subset — diacritics render in a mismatched fallback face mid-word); FZ Rubik stays the fallback in the body stack so Vietnamese never breaks even if Lexend fails to load. Body line-height ≥ 1.75, caption ≥ 1.667, eyebrow ≥ 1.54 so stacked diacritics (ắ ễ ộ, especially uppercase Ắ Ễ Ộ) don't clip. Test string: "Chuyên gia chiều cao".
8. **Focus rings are mandatory, not a brand-rule violation.** Every interactive element gets a `:focus-visible` ring (`#384B98`, 2px, swaps to white on gradient surfaces). This is a different pseudo-class/purpose than the "no black outline" rule — never suppress it to satisfy that rule.
9. **Disabled state ≠ opacity hack.** Use `#EBECEF` background / `#9C9FAB` text + `cursor: not-allowed` — a faded brand color reads as "still clickable," not "inert."
10. **Color is never the only signal.** Success/error always pair with a glyph or text, never a bare colored dot/pill. Mascot poses that communicate state (error, success, reminder) always ship with a real text string alongside — the illustration is reinforcement, never the sole carrier.
11. **`cursor: pointer` on every enabled interactive element.** Links, buttons, clickable cards/rows. Pairs with the disabled rule (`cursor: not-allowed`). A clickable surface with the default arrow cursor reads as broken — this is the most common miss when a `<div onClick>` is used instead of a real `<button>`.
12. **Emoji are never UI icons.** They render differently per platform and carry uncontrollable color — both break the closed palette. UI glyphs come from Lucide (see DESIGN.md → Icons); emoji are legal only inside `{typography.sticker}` caption copy.
13. **Never fabricate data.** Product names, ingredient dosages, prices, customer counts, %, ratings, doctor names, and citations come from a real Midu source (the company knowledge base `Z:\DU LIEU MIDU\MIDU BRAIN`, or material the user gives) — never invented, not even as "*illustrative". K2 (MenaQ7) ships only in 45/180/360 mcg; a made-up mg is a health-claim fabrication. No real figure available → omit it, use a clearly-labelled placeholder ("[nội dung minh họa]"), or drop the element. Real fallbacks: ~20.000 chuyên gia đào tạo · 91+ khóa học · ~300.000 phác đồ (midu.vn). See DESIGN.md Voice §5.

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
| success / error | `#2E7D46` / `#C93A3A` | AA-compliant on white — always pair with a glyph, never color-only |
| hairline-strong | `#8A8F9E` | Interactive borders (text-input) — plain hairline is only 1.3:1, fails WCAG 1.4.11 |
| disabled-bg / disabled-text | `#EBECEF` / `#9C9FAB` | Inert state for any button/input — pair with `cursor:not-allowed` |
| on-primary-soft | `rgba(255,255,255,.94)` | Subcopy/captions/links on the brand gradient — 4.61:1 at the magenta pole (AA). Never below this for on-gradient body text. |
| indigo/magenta/sun ramps (50–900) | see `${CLAUDE_SKILL_DIR}/references/DESIGN.md` | Lightness variants of the 3 base hues — hover fills (50), pressed states (700), dark surfaces (800–900). Not new colors. |

Motion adds `duration-count` (1600ms) for the stat count-up — single-purpose, not collapsed under reduced motion (the JS disables counting there instead).

Focus, motion, breakpoint, and container tokens (new in v0.2.0) live in `${CLAUDE_SKILL_DIR}/references/DESIGN.md` frontmatter — read it for exact values (`focus.ring-*`, `motion.duration-*`/`easing-*`, `breakpoints.*`, `container.*`).

### Typography (FZ Rubik + Lexend)

Two faces, one rule: **FZ Rubik** for display/titles (`var(--midu-font-display)`), **Lexend** for reading text (`var(--midu-font-body)`). Both are full-Vietnamese. The Font column below says which each role uses.

| Role | Font | Size/Weight | Notes |
|---|---|---|---|
| display-xl | FZ Rubik | 40–64px fluid / 900 | Heroes; may wear gradient fill; lh 1.125; `clamp(2.5rem, 2rem + 2.222vw, 4rem)` |
| display | FZ Rubik | 32–44px fluid / 900 | Section openers, stat numbers; tabular figures (`font-feature-settings: "tnum"`) |
| headline | FZ Rubik | 24–30px fluid / 700 | Group titles; lh 1.333 |
| title | FZ Rubik | 22px / 700 | Card/modal titles |
| body-lg | Lexend | 18px / 500 | Lead paragraphs |
| body | Lexend | 16px / 400 | Default; lh 1.75 (raised from 1.6 for Vietnamese diacritic safety) |
| body-sm | Lexend | 14px / 400 | Card body, meta text, footer links |
| button | FZ Rubik | 16px / 700 | All pills |
| eyebrow | FZ Rubik | 13px / 700 | UPPERCASE, +1.5px tracking, lh 1.54, magenta, usually in a pill badge |
| caption | Lexend | 12px / 500 | Sources, disclaimers; lh 1.667 — highest diacritic-clip risk in the scale |
| link | Lexend | inherits size | `color:#384B98`, underline at 40% opacity, hover → magenta, no visited state |

Weights: 900 for moments, 700 for structure, 400–500 for reading. Skip 600. Fluid sizes need no manual breakpoint — `clamp()` scales continuously from 360px to 1440px viewports.

### Shape & Space

- Radius: 8 / 12 / 20 / 28 / pill(999). Spacing: 4 / 8 / 12 / 16 / 24 / 32 / 48 / section 80. Base unit 8px.
- Max content width 1200px. Alternate white / surface-soft sections; never two tinted sections adjacent.
- Shadows are indigo-tinted: `0 8px 24px rgba(56,75,152,.10)` cards, `0 16px 40px rgba(56,75,152,.16)` floating. Never grey shadows.

## Component Recipes

Recipes use the variables from `${CLAUDE_SKILL_DIR}/references/tokens.css` — paste that file into the project first, so token values live in exactly one place.

**Tailwind 4 project?** Also ship `${CLAUDE_PLUGIN_ROOT}/design-system/midu-theme.css` — it lives at the plugin root beside `design-system/tokens.css` (NOT in this skill's `references/`; see "Locating bundled files"). Copy both files together, then `@import "tailwindcss"; @import "midu-theme.css";`. It aliases the tokens into `@theme` (`bg-primary`, `rounded-lg`, `shadow-card`, `font-display`). Don't hand-write the `@theme` block — the aliases are lint-checked against `tokens.css`.

```css
/* Global focus ring — the one outline permitted on UI chrome (not the "no black outline" rule) */
:focus-visible { outline: var(--midu-focus-ring-width) solid var(--midu-focus-ring-color); outline-offset: var(--midu-focus-ring-offset); }
.on-brand-gradient :focus-visible { outline-color: var(--midu-focus-ring-color-on-gradient); }

/* Primary CTA — the brand handshake */
.btn-primary {
  background: var(--midu-grad-brand);
  color: var(--midu-on-primary); font-weight: 700;
  border-radius: var(--midu-r-pill); padding: 14px 28px; border: 0;
  transition: transform var(--midu-duration-fast) var(--midu-easing-standard);
}
.btn-primary:active { background: linear-gradient(90deg, var(--midu-indigo-700), var(--midu-magenta-700)); }
.btn-primary:disabled { background: var(--midu-disabled-bg); color: var(--midu-disabled-text); cursor: not-allowed; }
/* Secondary partner */
.btn-secondary {
  background: var(--midu-canvas); color: var(--midu-primary);
  border: 2px solid var(--midu-primary); border-radius: var(--midu-r-pill); padding: 12px 26px;
}
.btn-secondary:hover { background: var(--midu-indigo-50); }
/* Sun — promos/gamification only, max one per viewport */
.btn-sun { background: var(--midu-sun); color: var(--midu-ink); border-radius: var(--midu-r-pill); padding: 14px 28px; }
.btn-sun:hover { background: var(--midu-sun-500); }

/* Nutrient bubble (decorative, 3–5 per cluster, one orange max) */
.bubble {
  border-radius: 50%; color: #fff; font-weight: 700;
  background: var(--midu-grad-bubble); /* orange variant: var(--midu-grad-bubble-orange) */
}

/* Progress "ruler" — the brand's measurement motif */
.ruler-track { height: 12px; border-radius: var(--midu-r-pill); background: var(--midu-surface-soft); }
.ruler-fill  { height: 100%; border-radius: var(--midu-r-pill); background: var(--midu-grad-sun); transition: width var(--midu-duration-slow) var(--midu-easing-standard); }
/* tick marks: repeating-linear-gradient(90deg, transparent 0 calc(10% - 1px), var(--midu-hairline) calc(10% - 1px) 10%) */

/* Toast/snackbar — new v0.2.0 */
.toast { background: var(--midu-indigo-800); color: #fff; border-radius: var(--midu-r-pill); padding: 12px 20px; box-shadow: var(--midu-shadow-float); }
.toast.success { background: var(--midu-success); } .toast.error { background: var(--midu-error); }

/* card-hover-lift — new v0.3.0. Doubled selector (0,2,0) so it owns the transition
   even next to a scroll-reveal rule. Apply alongside .card / any card surface. */
.card-hover-lift.card-hover-lift { transition: transform var(--midu-duration-fast) var(--midu-easing-standard), box-shadow var(--midu-duration-fast) var(--midu-easing-standard); }
.card-hover-lift:hover, .card-hover-lift:focus-visible { transform: translateY(-2px); box-shadow: var(--midu-shadow-float); }

/* on-gradient buttons — new v0.3.0. The primary/secondary pair for controls on a gradient panel. */
.btn-primary-on-gradient { background: var(--midu-on-primary); color: var(--midu-primary); border-radius: var(--midu-r-pill); padding: 14px 28px; font-weight: 700; }
.btn-secondary-on-gradient { background: transparent; color: var(--midu-on-primary); border: 2px solid var(--midu-on-primary); border-radius: var(--midu-r-pill); padding: 12px 26px; }
```

**stat-counter** (new v0.3.0) — count-up-on-scroll trust number. Markup: `<div class="stat-counter" role="img" data-target="10000" data-suffix="+" aria-label="10.000+ …"><span class="stat-counter__value" aria-hidden="true">0</span><span class="stat-counter__label">…</span></div>`. `role="img"` + `aria-label` carry the accessible name; format numbers with the **`vi-VN`** locale (never `en-US` — "10,000" misreads as a decimal in Vietnamese); counts once, snaps to final value under reduced motion. Full CSS+JS: `${CLAUDE_SKILL_DIR}/references/DESIGN.md` → Motion / Components.

Full component specs — v0.2.0 (`toast-snackbar`, `empty-state`, `modal-dialog`, `date-picker`, `tabs`, `product-grid`) and v0.3.0 (`stat-counter`, `product-card`, `ingredient-facts-table`, `testimonial-card`, `expert-endorsement-card`, `button-*-on-gradient`, `card-hover-lift`, `scroll-reveal`): `${CLAUDE_SKILL_DIR}/references/DESIGN.md` → Components / Motion.

## Logo

Files in `${CLAUDE_SKILL_DIR}/assets/`: `logo-midu.png` (color, light grounds), `logo-midu-white.png` (on gradient/dark imagery), `logo-midu-tagline.png` (lockup — prefer on first appearance per surface).

Rules: clearspace = height of the "m" on all sides · min width 96px · never stretch, rotate, outline, recolor, or detach the lightbulb/ruler/child elements from the wordmark.

## Mascot: MIGI

Transparent PNGs in `${CLAUDE_SKILL_DIR}/assets/` (560px; full-res 1871px lives in the kit's source repo at `design-system/assets/`, not bundled with the skill). Map pose to UX moment:

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
- [ ] Mascot (if any): right pose for the moment, not flipped, not recolored, and paired with real text if it communicates state
- [ ] Every interactive element shows a visible `:focus-visible` ring when tabbed to (white on gradient surfaces)
- [ ] Every button/input has a disabled state (`disabled-bg`/`disabled-text`), not just an opacity fade
- [ ] Success/error signaling pairs color with a glyph or text — never a bare colored dot/pill
- [ ] Every clickable element shows `cursor: pointer`; no emoji used as a UI icon
- [ ] Product-facing pages carry the legal disclaimer band in the footer ("Thực phẩm này không phải là thuốc…")
- [ ] Logo, mascot, and other brand assets use the **real files** from `assets/` (e.g. footer/nav shows `logo-midu-white.png` on the gradient, not a typed "Midu" text stand-in) — never a paraphrased look-alike
- [ ] `<html lang="vi">` set

## What Do I Use For…

| You want | Use |
|---|---|
| Primary CTA | `{components.button-primary}` (one/viewport; on gradient → `button-primary-on-gradient`) |
| Secondary action | `{components.button-secondary}` (`-on-gradient` on gradient grounds) |
| Promo / gamified action | `{components.button-sun}` (max one/viewport) |
| Section kicker / label | `{components.eyebrow-badge}` (`-on-tint` on surface-soft) |
| Trust number that counts up | `{components.stat-counter}` |
| Progress toward a height goal | `{components.progress-ruler}` |
| Product tile with price + buy | `{components.product-card}` |
| Dosage / composition facts | `{components.ingredient-facts-table}` |
| Parent quote | `{components.testimonial-card}` |
| Doctor endorsement | `{components.expert-endorsement-card}` |
| Decorative delight | `{components.chip-nutrient}` cluster (one/section, one orange max) |
| Emotional state (error/empty/success) | MIGI pose + real text alongside |
