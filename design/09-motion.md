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

