# Changelog

All notable changes to the MIDU Vibecoder Kit are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/); the kit uses [SemVer](https://semver.org/).

Each release lists the **plugin version** (the release you pin / that gets git-tagged)
and, in parentheses, the matching **DESIGN.md spec version** (design-system maturity).
See CONTRIBUTING.md → Versioning.

## [Unreleased]

### Added
- `QUICKSTART.md` — 30-second onboarding, linked from the top of README.
- `scripts/check_kit.py` — consistency lint (references-in-sync, token-graph resolves, manifests parse + versions agree, generated preview/example current, mascot self-test, fonts present). Run before every push.
- `.github/workflows/ci.yml` — CI running the lint (Python + Pillow + PyYAML) and the Next.js example build (Node 20).
- `LICENSE` (proprietary, internal MIDU use) + `THIRD-PARTY-NOTICES.md` (Lexend OFL, Lucide ISC, Vercel MIT; FZ Rubik / MIGI / logos flagged proprietary).
- `CONTRIBUTING.md` — release process, pre-push gate, references-sync discipline, versioning policy.

### Fixed
- Font/asset findability: corrected "FZ Rubik as woff2" → TTF; added the repo URL to DESIGN.md + README; added a `${CLAUDE_PLUGIN_ROOT}` fallback note.

### Known risk
- The proprietary FZ Rubik TTF is committed to a public repo — pending brand/legal confirmation or relocation (see DESIGN.md → Known Gaps and THIRD-PARTY-NOTICES.md).

## [1.3.0] — 2026-07-08  (DESIGN.md 0.4.0)

### Changed
- Typography is now a **two-font pairing**: FZ Rubik for display/titles, **Lexend** for reading text (body, body-lg, body-sm, caption, links). Both carry full Vietnamese.

### Added
- Lexend bundled at `design-system/fonts/Lexend/` (woff2, weights 400/500/700, vietnamese+latin+latin-ext) + `lexend.css`; tokens `--midu-font-display` / `--midu-font-body`.
- Applied across all surfaces: preview, both examples (Next.js via `next/font/google`), skills, README.

## [1.2.0] — 2026-07-08  (DESIGN.md 0.3.0)

### Added
- Components: `stat-counter` (count-up), `product-card`, `ingredient-facts-table`, `testimonial-card`, `expert-endorsement-card`, `button-primary-on-gradient`, `button-secondary-on-gradient`, `card-hover-lift`, `scroll-reveal`.
- Sections: Page Anatomy (canonical landing order + density), footer `legal-band` with the mandatory supplement disclaimer.
- Tokens: `on-primary-soft` (contrast-verified 4.61:1), `duration-count` (1600ms).
- Mascot framing standard + `design-system/scripts/normalize_mascots.py`; all MIGI poses normalized to ~85% frame height.
- Interaction rules: `cursor: pointer` non-negotiable; no emoji as UI icons.
- `midu-design-system` gained a self-contained brainstorm → brief → plan → build → review workflow (HARD-GATE before code); Non-Negotiable #13 "never fabricate data".

### Fixed
- Replaced fabricated demo data (dosages, price, doctor, testimonial, stats) with real Midu facts / clearly-labelled placeholders, verified against the company knowledge base.
- Hero CTA uses the on-gradient white pill (was a gradient pill on a gradient ground → two gradient CTAs per viewport).

## [1.1.0] — 2026-07-07  (DESIGN.md 0.2.0)

### Added
- Engineering skills: `nextjs-frontend` (Vercel performance rules + Next.js conventions + component patterns) and `typescript-backend` (code-style + API/architecture patterns).
- Plugin renamed to `midu-vibecoder-kit`; `displayName` "MIDU Vibecoder Kit"; SessionStart + PostToolUse hooks.
- Design-director review pass: tint/shade ramps (50–900), disabled/hairline-strong tokens, breakpoints/container/motion/focus token blocks, fluid `clamp()` type, global `:focus-visible` ring, 5 v0.2.0 components (toast, empty-state, modal, date-picker, tabs), Voice/Icons/Motion/Accessibility/Governance sections.

### Fixed
- Anchored all skill-internal / plugin-root file references with `${CLAUDE_SKILL_DIR}` / `${CLAUDE_PLUGIN_ROOT}` so they resolve regardless of install location.

## [1.0.0] — 2026-07-06  (DESIGN.md 0.1.0)

### Added
- Initial MIDU MenaQ7 design system: DESIGN.md (getdesign.md format) + `tokens.css`, FZ Rubik font, MIGI mascot poses + logos, self-contained `preview.html`, static + Next.js landing examples.
- Skills `midu-design-system` (build) and `midu-brand-review` (audit); packaged as a Claude Code plugin installable via marketplace.

[Unreleased]: https://github.com/boizdeeptry/MIDU-Guidline-Design/compare/midu-vibecoder-kit--v1.3.0...HEAD
[1.3.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.3.0
[1.2.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.2.0
[1.1.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.1.0
[1.0.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.0.0
