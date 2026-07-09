## Layout

### Spacing System

- **Base unit**: 8px, halved to 4px for chip and badge interiors.
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 80px · `{spacing.touch-target-min}` 48px · `{spacing.touch-target-min-decorative}` 44px.
- Section rhythm: `{spacing.section}` (80px) vertical between major blocks; hero and footer panels get `{spacing.xxl}` interior padding.
- Card interiors: `{spacing.lg}` (24px). Inputs: 12px vertical · 16px horizontal.
- Grids: `{components.product-grid}` formalizes gap at `{spacing.lg}` (24px) — replaces the ad hoc 14–48px gap values that had crept into shipped code with no token backing them.

### Breakpoints

Tokenized as `{breakpoints.*}` (see frontmatter) so implementers reference `@media (max-width: {breakpoints.tablet})` instead of re-typing raw pixel values — two undocumented breakpoints (860px, 700px) had already appeared in shipped code before these tokens existed. Values map 1:1 to the Responsive Behavior table below.

### Grid & Container

- Max content width `{container.max-width}` (1200px), gutters `{spacing.lg}` mobile → `{spacing.xxl}` desktop.
- `{container.reading-width}` (760px) — the second real max-width in this system, for FAQ lists, lead-capture forms, and other single-column reading content. Previously a repeated magic number with no token; use it instead of inventing 720/780/800px on the next narrow-content component.
- Product/benefit grids run `{components.product-grid}`: 3-up desktop, 2-up tablet, 1-up mobile, `{spacing.lg}` gap.
- **The mascot breaks the grid.** MIGI overlaps section edges — a hand over the hero boundary, a head poking above a card — always by design. Reserve overflow room; never `overflow: hidden` a mascot slot.

### Whitespace Philosophy

White space is the credibility layer. The gradient and the mascot are loud, so everything between them must be quiet: white canvas, one focal point per viewport, decoration budget of one bubble cluster per section. When a section feels empty, add breathing room or one nutrient bubble — not another color.

