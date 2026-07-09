# MIDU MenaQ7 — Vibecoder Kit

**New here?** → [QUICKSTART.md](QUICKSTART.md) — up and running in 30 seconds.

A packaged standard that lets AI coding tools (Claude Code, Cursor, Windsurf…) build on-brand, well-engineered MIDU MenaQ7 web projects without a designer or a senior reviewer in every loop: brand tokens/mascot on one side, a Next.js/React frontend standard and a TypeScript backend standard on the other.

## Contents

| Path | Role |
|---|---|
| `DESIGN.md` | **The core** — design tokens (colors, typography, radius, spacing, components) + full spec in the [getdesign.md](https://getdesign.md) format. AI assistants read this one file before writing UI. **Generated** by `scripts/build_design.py` from the topic files in `design/` — edit those, not this. |
| `design/` | The maintainable source of `DESIGN.md`: one file per section (`00-frontmatter.md` … `19-governance.md`). Rebuild the single file with `python scripts/build_design.py`. |
| `design-system/tokens.css` | CSS custom properties — paste straight into any project. |
| `design-system/fonts/` | **FZ Rubik** (display/titles, TTF, weights 400/500/700/900, full Vietnamese) + `fzrubik.css`, and **Lexend** (body/reading text, woff2, weights 400/500/700, full Vietnamese) + `lexend.css` — each `.css` registers its own face. |
| `design-system/assets/` | Logo (color / white / tagline lockup) + 15 MIGI mascot poses, transparent full-res PNGs with semantic names. |
| `design-system/preview.html` | Self-contained visual style guide (build artifact — open in a browser). |
| `design-system/preview-src/` | Template + `build-preview.py` that generate `preview.html`. Edit here, then rebuild. |
| `examples/midu-landing/` | Example landing page as self-contained HTML (template + build script). |
| `examples/midu-landing-next/` | Production-grade example: Next.js 15 + Tailwind 4 + Supabase lead form, deploy-ready for Vercel. |
| `.claude-plugin/` | Plugin + marketplace manifests — makes this repo installable via `/plugin marketplace add`. |
| `skills/midu-design-system/` | **Claude skill** (brand) — auto-activates when building MIDU UI (rules digest + DESIGN.md + tokens.css + all assets at 560px). |
| `skills/midu-brand-review/` | **Claude skill** (brand) — audits UI against the brand with a 3-severity checklist (Blocker / Major / Minor). |
| `skills/nextjs-frontend/` | **Claude skill** (engineering) — Vercel Engineering's React/Next.js performance rules (MIT) + Next.js framework conventions + component-architecture patterns. Brand-agnostic, reusable on any React/Next.js codebase. |
| `skills/typescript-backend/` | **Claude skill** (engineering) — TypeScript code-style standard (errors, async, validation, types) + API/architecture patterns (repository, caching, auth, rate limiting), with a "Before You Build" checklist and this repo's own `api/leads` route as the reference implementation. |

## Usage

**Option 1 — Plugin marketplace (recommended for the whole company):** push this folder to a company Git repo, then everyone installs with two commands in Claude Code:

```
/plugin marketplace add boizdeeptry/MIDU-Guidline-Design
/plugin install midu-vibecoder-kit@midu-skills
```

One plugin ships all four skills — they auto-activate on matching work; invoke directly with `/midu-design-system`, `/midu-brand-review`, `/nextjs-frontend`, or `/typescript-backend`. Updates flow to everyone on `/plugin update`.

**Option 2 — manual copy (no Git):** copy the skill folders you need into a project or globally:

```powershell
# Into a specific project
Copy-Item -Recurse "skills\*" "<project>\.claude\skills\"

# Or globally for every project
Copy-Item -Recurse "skills\*" "$env:USERPROFILE\.claude\skills\"
```

**Option 3 — plain DESIGN.md (any AI tool):**
1. Copy `DESIGN.md` (plus `design-system/tokens.css` and `design-system/fonts/` as needed) into your project root.
2. Tell the AI assistant: **"Read DESIGN.md before writing any UI."**
3. Reference tokens by name when iterating: *"switch this button to `{components.button-sun}`"*.

## Maintenance

- **Source of truth & sync:** edit `DESIGN.md` via its parts in `design/` then rebuild (`python scripts/build_design.py`); `design-system/tokens.css` is edited directly. After either changes, re-copy both into the skill:

  ```powershell
  python scripts\build_design.py   # design\*.md -> DESIGN.md
  Copy-Item DESIGN.md, design-system\tokens.css "skills\midu-design-system\references\"
  ```

  Never edit `DESIGN.md` or the `references/` copies directly — edit `design/` and rebuild. `python scripts\check_kit.py` enforces both links. See CONTRIBUTING.md.
- **Preview:** `design-system/preview.html` is generated. Edit `design-system/preview-src/preview-template.html`, then run `python design-system/preview-src/build-preview.py`.
- **Fonts:** FZ Rubik comes from the company font pack — confirm the license covers web `@font-face` embedding before public deployment. Never substitute Google-Fonts Rubik for Vietnamese copy (it has no Vietnamese subset).
- **Vector sources:** the original `.ai`/`.pdf` brand files are not in this kit — they live in the brand team's Drive folder. The kit ships rasterized PNGs (web-sufficient); request vectors for large-format print.
