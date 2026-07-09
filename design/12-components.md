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

