## Changelog

### 0.4.0 — this round
- Changed: typography is now a **two-font pairing** — FZ Rubik for display/titles (`display-xl`/`display`/`headline`/`title`/`button`/`eyebrow` + stat numerals), **Lexend** for reading text (`body-lg`/`body`/`body-sm`/`caption`/link). Both carry full Vietnamese.
- Added: Lexend bundled at `design-system/fonts/Lexend/` (woff2, weights 400/500/700, vietnamese+latin+latin-ext) + `design-system/fonts/lexend.css`; tokens `--midu-font-display` / `--midu-font-body` (`--midu-font-ui` kept as a back-compat alias of display).

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

