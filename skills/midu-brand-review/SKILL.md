---
name: midu-brand-review
description: Audit UI, pages, or components against the MIDU MenaQ7 brand system. Use when reviewing existing MIDU screens/code for brand compliance, when the user asks "đúng chuẩn brand chưa?", "review giao diện", "check brand", or before shipping any MIDU-facing surface. Pairs with the midu-design-system skill (which is for BUILDING; this one is for CHECKING).
---

# MIDU Brand Review

Audit a screen, page, or component against the MIDU MenaQ7 design system. Token source of truth: the `midu-design-system` skill (`${CLAUDE_PLUGIN_ROOT}/skills/midu-design-system/references/DESIGN.md`) — install both skills together. Hex values below are transcribed from DESIGN.md; re-verify them after any token change.

## How to Run a Review

1. Read the code/screenshot under review fully before judging.
2. Walk the checklist below; collect violations with file:line evidence.
3. Report by severity, most severe first. For each finding: what's wrong → which rule → the concrete fix (exact hex/token/value).
4. If nothing is wrong in a category, say so in one line — don't pad.

## Checklist

### 🔴 Blockers (break the brand or accessibility)

- **Gradient discipline:** more than one indigo→magenta gradient CTA per viewport; gradient on body text, icons, borders, or secondary buttons; gradient flowing the wrong way (must be indigo left/top → magenta right/bottom; only the footer may reverse).
- **Contrast traps:** white text on Sun `#EFCA3D` (must be ink `#221F1F`); magenta eyebrow directly on `#EEF1FA` tint (use the `eyebrow-badge-on-tint` component — white badge ground; bare magenta-on-tint is 4.45:1, fails AA); text-bearing controls on bubble-orange `#F68500`; semantic colors other than `#2E7D46` / `#C93A3A` for small text.
- **Foreign hues:** any color outside the system (indigo `#384B98`, magenta `#C1368D`, sun `#EFCA3D`, lime `#E4E254`, surfaces `#FFFFFF`/`#EEF1FA`/`#F7F4FB`, hairline `#DDE2F0`, ink `#221F1F`, mascot family, 2 semantic tones).
- **Vietnamese typography:** Google-Fonts Rubik used for Vietnamese copy (it has no Vietnamese subset — diacritics fall back to a mismatched face); body line-height < 1.5 clipping stacked diacritics. Correct face: FZ Rubik, bundled in the kit (`${CLAUDE_PLUGIN_ROOT}/design-system/fonts/`).
- **Logo misuse:** logo stretched, rotated, recolored, outlined, or with elements (lightbulb/ruler/child) detached; color logo on the gradient (must be the white version); rendered under 96px wide.
- **Mascot abuse:** MIGI mirror-flipped, recolored, rendered under 120px height, or more than one MIGI per viewport.
- **No focus indicator:** any interactive element with `outline: none`/`outline: 0` and no replacement `:focus-visible` style — this is a WCAG 2.4.7 failure, not a style choice. Check especially for the brand's "no black outline" rule being misapplied to suppress ALL outlines (it only bans decorative `#221F1F` comic strokes, not the `:focus-visible` ring).
- **Color-only signaling:** a bare colored dot/pill/row-highlight conveying success or error with no glyph, icon, or text alongside it. `#2E7D46`/`#C93A3A` have near-identical luminance and sit on the color-blind-hardest axis — color alone is not sufficient.
- **Mascot as sole state carrier:** an error/empty/success screen showing only a MIGI pose with no real, in-DOM text saying the same thing (`alt=""` decorative image + no text sibling = screen-reader user gets zero information).
- **Fixed-px containers clipping text:** `chip-nutrient`/`top-nav`/similar using a hard `size`/`height` instead of `min-*` + `aspect-ratio`/`overflow: visible` — clips labels at 200% zoom or large-text overrides.
- **Missing legal disclaimer:** any MIDU product-facing page whose footer lacks the mandatory Vietnamese supplement disclaimer band ("Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."). This is a regulatory requirement, not a style preference — its absence is a compliance liability.
- **Fabricated data:** any invented ingredient dosage, price, customer count, satisfaction %, rating, doctor name, or citation. K2 (MenaQ7) exists only in 45/180/360 mcg — a made-up mg value is a health-claim fabrication (the worst offender). Expert endorsements must name a real advisory-board doctor with a real cited source; testimonials must be real (Midu rule: "không bịa social proof") or a clearly-labelled placeholder. An "*illustrative" tag does NOT license an invented number — see DESIGN.md Voice §5.

### 🟠 Majors (visibly off-brand)

- Square corners anywhere (buttons must be pill 999px; cards ≥20px; tables ≥8px).
- Black borders/outlines on UI chrome (comic outlines are illustration-only; UI uses hairline `#DDE2F0`).
- Grey drop shadows (must be indigo-tinted: `rgba(56,75,152,.10)` / `.16`).
- Sun `#EFCA3D` and MIGI Yellow `#FFDA69` swapped (UI accent vs giraffe coat).
- Two adjacent tinted sections (rhythm is white → tint → white).
- Weight 600 text, or hierarchy built with mid-grey instead of weight (900 moments / 700 structure / 400–500 reading).
- More than one bubble cluster per section; more than one orange bubble per cluster.
- `button-sun` used for a primary action or appearing twice per viewport.

### 🟡 Minors (polish)

- Eyebrows not uppercase / missing +1.5px tracking / floating bare instead of in a pill badge.
- Growth or health claims without a 12px caption source line.
- Mascot slot with `overflow:hidden` cropping MIGI's overflow (allowed up to 15%).
- Wrong MIGI pose for the moment (e.g. cheerful pose on an error page — errors get `migi-cry`/`migi-sulk`, soft and never blaming).
- Missing hover states: primary pills lift 1px + deepen shadow on hover, darken to indigo-700/magenta-700 on press; secondary hover-fills indigo-50; sun hover swaps to sun-500.
- Missing disabled states on buttons/inputs (should be `disabled-bg` `#EBECEF` / `disabled-text` `#9C9FAB`, not a faded brand color).
- `text-input` border using plain `hairline` (`#DDE2F0`, 1.3:1) instead of `hairline-strong` (`#8A8F9E`, 3.2:1) — fails WCAG 1.4.11 for an interactive boundary.
- ALL-CAPS body copy (uppercase is eyebrow-only).
- Decorative animation (bubble float, mascot idle-loop, scroll-reveal entrance, stat count-up) not fully disabled under `prefers-reduced-motion: reduce` — partial slowdown isn't enough, it must stop. (A stat-counter that still animates its count-up under reduced motion is a violation — it should snap to the final value.)
- Voice/tone violations: fear or scarcity framing ("chỉ còn X suất", shortfall shaming), or mascot exclamations ("Wow!", "Cố lên!") used in body paragraphs or button labels instead of `{typography.sticker}` captions.
- Clickable element missing `cursor: pointer` (links, buttons, clickable cards/rows).
- Emoji used as a UI icon (platform-inconsistent, uncontrollable color) — glyphs come from Lucide; emoji only in `{typography.sticker}` captions.
- Testimonial without a name + child's age, or an expert-endorsement quote without a credential line and a `{typography.caption}` source — attribution is the trust mechanism; an unattributed quote is decoration.
- Stat number formatted with `en-US` grouping ("10,000") on Vietnamese copy — use `vi-VN` ("10.000") so the visible value matches the `aria-label`.

## Output Format

```
## Brand Review — <target>

### 🔴 Blockers (N)
1. <file:line> — <violation>. Rule: <rule>. Fix: <exact change>.

### 🟠 Majors (N)
...

### 🟡 Minors (N)
...

Verdict: SHIP / FIX BLOCKERS FIRST / NEEDS REWORK
```
