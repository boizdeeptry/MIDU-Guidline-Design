## Responsive Behavior

### Breakpoints

| Name | Token | Width | Key Changes |
|---|---|---|---|
| Desktop-XL | `{breakpoints.desktop-xl}` | 1440px | Content holds 1200px; gutters widen |
| Desktop | `{breakpoints.desktop}` | 1200px | Default 3-up card grids |
| Tablet | `{breakpoints.tablet}` | 960px | Grids 3-up → 2-up; nav collapses to hamburger |
| Mobile-L | `{breakpoints.mobile-l}` | 768px | Hero/tint panels go full-bleed (corners removed); MIGI moves below headline; fluid type is now continuous through this band instead of jumping |
| Mobile | `{breakpoints.mobile}` | 560px | display-xl reaches its 40px floor; pills go full-width; bubble clusters thin to 3 |
| Mobile-S | `{breakpoints.mobile-s}` | 400px | Stat tiles stack 1-up; footer columns collapse |

Reference these by token in new code, not raw pixel values — two undocumented breakpoints (860px, 700px) had already crept into shipped example code before these tokens existed.

### Touch Targets

- All pills ≥ `{spacing.touch-target-min}` (48px) tall on touch viewports (padding already guarantees this).
- Nutrient chips are decorative — if made tappable (ingredient info), enforce `{spacing.touch-target-min-decorative}` (44px) minimum and add the tap-bounce pressed state (see Motion).
- Inputs ≥ 48px tall.
- FAQ/accordion rows: the entire question row is the tappable trigger, min-height 48px, full-width — never just the disclosure icon.
- `top-nav` and `footer-gradient` text links: 44px hit area via `inline-flex` + `padding-inline`, even at body-sm visible text size.

### Collapsing Strategy

- **Hero**: two-column (copy | mascot) → stacked with mascot at 60% scale below the CTA pair. Never crop MIGI's head.
- **Nav**: links fold into a full-canvas overlay; logo and `button-primary` stay visible.
- **Stat rows**: 3-up → horizontal scroll snap at Mobile-L rather than stacking, keeping numbers comparable.
- **Progress-ruler**: tick labels drop to every 25% below 560px; the track never shrinks below 8px.

