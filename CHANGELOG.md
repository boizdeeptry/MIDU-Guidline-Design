# Changelog

All notable changes to the MIDU Vibecoder Kit are recorded here. Format follows
[Keep a Changelog](https://keepachangelog.com/); the kit uses [SemVer](https://semver.org/).

Each release lists the **plugin version** (the release you pin / that gets git-tagged)
and, in parentheses, the matching **DESIGN.md spec version** (design-system maturity).
See CONTRIBUTING.md → Versioning.

## [Unreleased]

## [1.4.2] — 2026-07-09  (DESIGN.md 0.4.0)

### Fixed
- **Tailwind `<button>` cursor.** Tailwind v4's Preflight removed `cursor:pointer` from `<button>`, so button CTAs (e.g. the example's form submit) showed the default arrow — a Non-Negotiable #11 miss on the primary conversion control. Added `button:not(:disabled){cursor:pointer}` / `button:disabled{cursor:not-allowed}` to `examples/midu-landing-next` global CSS, and documented the gotcha + fix in the `midu-design-system` skill's Tailwind stack note so every Tailwind build carries it. (`<a>` links were unaffected.)

## [1.4.1] — 2026-07-09  (DESIGN.md 0.4.0)

### Fixed
- **Static-HTML build path unblocked for teammates.** The skill said "inline `fonts.css`," which led the model to `Read` the ~600KB file (≈600k tokens) and hit the Read tool's 25k-token cap, and the build scripts assumed Python (absent on many machines — the build errored with "Python was not found"). The `midu-design-system` skill + QUICKSTART now: (1) build self-contained pages with a **Node** script (`node build.mjs` — Node ships with Claude Code; no Python), (2) **never** open `fonts.css` with the Read tool — a build script reads it from disk by path so the bytes never enter context, and (3) offer a no-build fallback (copy `design-system/fonts/` + `<link>` its CSS). Includes a copy-paste `build.mjs`.

## [1.4.0] — 2026-07-09  (DESIGN.md 0.4.0)

### Changed
- **`midu-design-system` build workflow now ASKS the deliverable/stack up front** — one AskUserQuestion (static self-contained HTML · Next.js + Tailwind · React SPA · email) *before* the brief, instead of inferring it and folding a default into the brief for the user to rubber-stamp. The stack is the one material fork in a build (a share-and-view file vs a web-app with a real form/DB), so it is an explicit choice, never an assumption. Everything else is still inferred and stated as assumptions — no interrogation.

### Added
- `design-system/midu-theme.css` — a **Tailwind 4** drop-in that aliases the `--midu-*` tokens into Tailwind's `@theme` namespaces (`bg-primary`, `rounded-lg`, `shadow-card`, `font-display`, …). It `@import`s `tokens.css`, so hex/values stay single-sourced; verified to compile on Tailwind 4.3, and `check_kit.py` fails if any alias points at a token missing from `tokens.css`. Beginners on Tailwind now `@import` one file instead of hand-mapping `@theme`.
- `DESIGN.md` is now **generated** from per-section source files in `design/` (`00-frontmatter.md` … `19-governance.md`) via `scripts/build_design.py` — small files to maintain, one file for AI to read. The lint enforces DESIGN.md == the rebuild.
- `QUICKSTART.md` — 30-second onboarding, linked from the top of README.
- `scripts/check_kit.py` — consistency lint (references-in-sync, token-graph resolves, manifests parse + versions agree, generated preview/example current, mascot self-test, fonts present, tailwind theme aliases resolve, hooks.json valid + portable, every skill's ${CLAUDE_*} file reference resolves on the installed tree). Run before every push.
- `.github/workflows/ci.yml` — CI running the lint (Python + Pillow + PyYAML) and the Next.js example build (Node 22, on Node-24 action runtimes).
- `LICENSE` (proprietary, internal MIDU use) + `THIRD-PARTY-NOTICES.md` (Lexend OFL, Lucide ISC, Vercel MIT; FZ Rubik / MIGI / logos flagged proprietary).
- `CONTRIBUTING.md` — release process, pre-push gate, references-sync discipline, versioning policy.

### Fixed
- **Hooks now run cross-platform.** `hooks/hooks.json` used `exec node …` plus a `commandWindows` field that isn't a real Claude Code hook field (silently dropped) — so on native Windows without Git Bash both hooks errored on every session start and every edit (PowerShell has no `exec`). Switched to the docs-blessed **exec form** (`"command": "node"`, `"args": ["${CLAUDE_PLUGIN_ROOT}/hooks/…"]`) — no shell, works on macOS/Linux/Windows. New lint check `[8]` guards against reintroducing `commandWindows`.
- Fresh-install UX: documented Node.js as a prerequisite (hooks) and the 0-hooks→`/plugin update` fix in QUICKSTART; added a macOS/Linux `cp -r` manual-copy path (was Windows-only `Copy-Item`); added the "can't find a bundled file" fallback note to all four skills (was only in `midu-design-system`); corrected the `midu-theme.css` locating hint (it ships at plugin root beside `design-system/tokens.css`, not in `references/`).
- Font/asset findability: corrected "FZ Rubik as woff2" → TTF; added the repo URL to DESIGN.md + README; added a `${CLAUDE_PLUGIN_ROOT}` fallback note.

### Known risk
- The proprietary FZ Rubik TTF ships in the repo. **Owner decision (2026-07-09): internal-only distribution** — the install link is shared with Midu teammates only, not promoted publicly. The repo is kept public for friction-free install; the owner accepts that the bundled font is then technically discoverable by anyone who finds the repo. Setting the repo private would close that exposure (install unchanged for teammates) but is not being done. Do not actively publish/promote the repo or marketplace publicly until the FZ Rubik license is cleared. See THIRD-PARTY-NOTICES.md and DESIGN.md → Known Gaps.

## [1.3.0] — 2026-07-08  (DESIGN.md 0.4.0)

### Changed
- Typography is now a **two-font pairing**: FZ Rubik for display/titles, **Lexend** for reading text (body, body-lg, body-sm, caption, links). Both carry full Vietnamese.

### Added
- Lexend bundled at `design-system/fonts/Lexend/` (woff2, weights 400/500/700, vietnamese+latin+latin-ext) + `lexend.css`; tokens `--midu-font-display` / `--midu-font-body`.
- Applied across all surfaces: preview, both examples (Next.js via `next/font/google`), skills, README.

## [1.2.0] — 2026-07-08  (DESIGN.md 0.3.0)

### Added
- Components: `stat-counter` (count-up), `product-card`, `ingredient-facts-table`, `testimonial-card`, `expert-endorsement-card`, `button-primary-on-gradient`, `button-secondary-on-gradient`.
- Motion contracts: `scroll-reveal`, `card-hover-lift`, and the `stat-counter` count-up.
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
- Design-director review pass: tint/shade ramps (50–900), disabled/hairline-strong tokens, breakpoints/container/motion/focus token blocks, fluid `clamp()` type, global `:focus-visible` ring, 6 v0.2.0 components (`toast-snackbar`, `empty-state`, `modal-dialog`, `date-picker`, `tabs`, `product-grid`), Voice/Icons/Motion/Accessibility/Governance sections.

### Fixed
- Anchored all skill-internal / plugin-root file references with `${CLAUDE_SKILL_DIR}` / `${CLAUDE_PLUGIN_ROOT}` so they resolve regardless of install location.

## [1.0.0] — 2026-07-06  (DESIGN.md 0.1.0)

### Added
- Initial MIDU MenaQ7 design system: DESIGN.md (getdesign.md format) + `tokens.css`, FZ Rubik font, MIGI mascot poses + logos, self-contained `preview.html`, static + Next.js landing examples.
- Skills `midu-design-system` (build) and `midu-brand-review` (audit); packaged as a Claude Code plugin installable via marketplace.

[Unreleased]: https://github.com/boizdeeptry/MIDU-Guidline-Design/compare/midu-vibecoder-kit--v1.4.2...HEAD
[1.4.2]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.4.2
[1.4.1]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.4.1
[1.4.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.4.0
[1.3.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.3.0
[1.2.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.2.0
[1.1.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.1.0
[1.0.0]: https://github.com/boizdeeptry/MIDU-Guidline-Design/releases/tag/midu-vibecoder-kit--v1.0.0
