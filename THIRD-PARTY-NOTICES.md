# Third-Party Notices

This kit is proprietary to Midu Group (see [LICENSE](./LICENSE)). It bundles or
references the third-party open-source components listed below, each governed by
its own license. Those licenses apply **only** to their respective components —
not to MIDU's own brand content.

---

## ⚠️ Action required: proprietary font in a public repository

This repository is **currently public** and ships the proprietary **FZ Rubik**
TrueType files (`design-system/fonts/FzRubik/*.ttf`, plus web copies under
`examples/midu-landing-next/src/fonts/`). FZ Rubik is a company font pack, **not
open source**, and publicly redistributing it may not be permitted by its
license.

**The MIDU brand/legal owner must confirm the FZ Rubik license permits public
redistribution.** If it does not, the font must be moved out of the public tree
— for example into a private repository, a release asset behind access control,
or another access-gated location — before this repo remains or goes public.

---

## Bundled / referenced open-source components

### Lexend (font)
- **License:** SIL Open Font License, Version 1.1 (OFL-1.1)
- **Source:** Google Fonts — https://fonts.google.com/specimen/Lexend
- **Location:** `design-system/fonts/Lexend/` (woff2, weights 400/500/700;
  Vietnamese + Latin + Latin-Ext subsets). Also embedded in the examples.
- **Notice:** Copyright The Lexend Project Authors. The OFL permits bundling,
  embedding, and redistribution with the software, provided the font is not sold
  by itself and the license/copyright notice is retained. Full text:
  https://openfontlicense.org

### Lucide (icons)
- **License:** ISC
- **Source:** https://lucide.dev — https://github.com/lucide-icons/lucide
- **Usage:** Referenced by the icon system (see the Iconography section of
  `DESIGN.md`); Lucide is the required icon library for MIDU UI.
- **Notice:** Copyright Lucide Contributors. The ISC license permits use, copy,
  and redistribution with the copyright and permission notice retained. (Lucide
  originates as a fork of Feather Icons, MIT © Cole Bemis.)

### Vercel Engineering — React/Next.js performance rules
- **License:** MIT
- **Location:** `skills/nextjs-frontend/references/vercel-performance.md`
  (bundled verbatim; the file header credits "Vercel Engineering", v1.0.0,
  January 2026, and the skill's `SKILL.md` frontmatter records it as
  MIT-licensed).
- **Notice:** Copyright Vercel, Inc. The MIT license permits use, copy,
  modification, and redistribution with the copyright and permission notice
  retained.

### Next.js example app dependencies
- The `examples/midu-landing-next/` project installs npm packages (Next.js,
  React, Tailwind, the Supabase client, and their transitive dependencies), each
  under its own license as declared in `examples/midu-landing-next/package.json`
  and `package-lock.json` (predominantly MIT). Those packages are not vendored
  into this repository; their licenses ship with them under `node_modules/`.

---

## Proprietary MIDU assets — NOT open source, NOT redistributable

The following are proprietary MIDU assets, owned by Midu Group. They are **not
open source** and **must not be redistributed outside the company**, regardless
of the licenses above:

- **FZ Rubik font** — `design-system/fonts/FzRubik/*.ttf` and the web copies in
  `examples/midu-landing-next/src/fonts/*.woff2` (company font pack; see the
  action-required note above).
- **MIGI mascot artwork** — `design-system/assets/migi-*.png` (all poses).
- **MIDU logos** — `design-system/assets/logo-midu*.png` (color, white, tagline
  lockup) and the brand guideline images.
- **The MIDU MenaQ7 brand system itself** — colors, typography rules, and design
  tokens defined in `DESIGN.md` and `design-system/tokens.css`.

If any doubt exists about whether a file may be shared publicly, treat it as
proprietary and check with the MIDU brand team first.
