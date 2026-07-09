## Page Anatomy

The default skeleton for a MIDU marketing/landing page — not a straitjacket, but the order an agent should reach for before inventing one. The white→`{colors.surface-soft}` alternation (see Layout) is what drives the rhythm; each band below flips the ground.

1. **`{components.top-nav}`** — white bar, logo left, one `{components.button-primary}` right.
2. **`{components.hero-gradient}`** — the gradient panel, ~55/45 copy|mascot split, one bubble cluster, on-gradient CTA pair. This surface holds the page's single gradient CTA.
3. **Benefits band (white)** — `{components.product-grid}` of `{components.card}`; **every efficacy/growth claim pairs with a stat or visual and a `{typography.caption}` source line** (Voice §2). Claims never float unsupported.
4. **Social-proof band (`{colors.surface-soft}`)** — `{components.testimonial-card}` grid + optional `{components.expert-endorsement-card}`.
5. **Stat/CTA row (white)** — `{components.stat-counter}` trust numbers, then the closing call to action.
6. **`{components.footer-gradient}`** — reversed gradient, link columns, and the mandatory `legal-band` disclaimer.

Sections may be added, removed, or reordered, but two rules always hold: **no two tinted sections are ever adjacent**, and **only one gradient CTA is visible per viewport**.

### Density

Section rhythm is not one-size-fits-all — a marketing page breathes, an in-app data screen packs tighter:

| Surface | Section gap | Card-grid gap |
|---|---|---|
| Marketing / landing | `{spacing.section}` (80px) | `{spacing.lg}` (24px) |
| App / height-tracker screens | 32–48px (`{spacing.xl}`–`{spacing.xxl}`) | `{spacing.md}` (16px) |

The 80px `{spacing.section}` rhythm is the landing-page default; app screens (growth charts, dose logs, settings) use the tighter scale so functional density doesn't force endless scrolling.

