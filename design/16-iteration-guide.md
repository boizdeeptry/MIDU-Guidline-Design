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

