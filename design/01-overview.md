## Overview

> **Source & assets.** This kit lives at **https://github.com/boizdeeptry/MIDU-Guidline-Design**. Fonts, mascot art, and logos ship alongside this file: fonts in `design-system/fonts/` (**FZ Rubik = TTF** in `FzRubik/` + `fzrubik.css`; **Lexend = woff2** in `Lexend/` + `lexend.css`), mascot/logo PNGs in `design-system/assets/`. For a **self-contained** page, inline `design-system/preview-src/fonts.css` — it already carries every face (FZ Rubik, Lexend, Quicksand, Patrick Hand) as base64 data URIs, so no binary hunting or path resolution is needed. If you only have this `DESIGN.md` and not the rest of the kit, fetch the fonts/assets from the repo above.

MIDU MenaQ7 is a Vietnamese children's height-growth supplement ("Chuyên gia chiều cao" — *the height expert*), and its design system fuses two registers that usually repel each other: **clinical credibility** and **cartoon warmth**. The credibility layer is white canvas, generous spacing, Rubik set in confident heavy weights, and a restrained two-hue brand core. The warmth layer is MIGI — a giraffe doctor with round glasses, a white lab coat, and a purple-striped tie — plus a floating cloud of nutrient bubbles (Ca+, D3, K2, Mg, Arg) that turns ingredient science into toy-like decoration.

The system's signature move is the **brand gradient**: indigo `{colors.grad-brand-start}` flowing into magenta `{colors.grad-brand-end}`. It appears in the wordmark letterforms, on hero panels, on every primary CTA, and in full-bleed footer bands. It always flows in one direction per surface (indigo → magenta, left to right or top-left to bottom-right) and it is the *only* gradient allowed on interactive chrome. A second, supporting gradient — sunshine `{colors.grad-sun-start}` → lime `{colors.grad-sun-end}` — is reserved for illustrative highlights and progress fills, never for buttons.

The third pillar is the **ruler motif**. The logo hides a ruler inside the "I", a lightbulb dot above it, and a reaching child inside the "U". Measurement is the product promise, so height charts, growth trackers, and tick-marked progress bars are first-class citizens, not afterthoughts.

**Key Characteristics:**
- One signature gradient (`{colors.grad-brand-start}` → `{colors.grad-brand-end}`) owns all primary actions and hero moments.
- Sunshine yellow `{colors.sun}` is the energy accent — badges, highlights, progress fill, MIGI's own body color echoes it.
- White `{colors.canvas}` dominates; lavender-tinted `{colors.surface-soft}` sections give rhythm without competing with the gradient.
- Everything is round: pill buttons, circular nutrient chips, `{rounded.lg}`+ cards. There are no sharp corners anywhere in the brand.
- MIGI the giraffe doctor carries emotional states across the product — 15+ named poses map to UX moments (onboarding, success, errors, reminders, bedtime) — but the illustration always travels with real text; see Accessibility.
- Bold black comic outlines (`{colors.ink}`) belong to *illustration only* — UI chrome never uses black borders. The one exception is the indigo `:focus-visible` ring, which is a different color, purpose, and pseudo-class — see Accessibility.
- Rubik at weights 400 / 500 / 700 / 900 is the single UI voice; the round, thin Quicksand tagline face appears only next to the logo lockup.
- Every hue in this system — including the new tint/shade ramps below — is a lightness variant of an already-approved brand color. The palette is still closed: no new hues were introduced in this revision.

