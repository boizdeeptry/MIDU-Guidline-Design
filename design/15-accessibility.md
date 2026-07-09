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

