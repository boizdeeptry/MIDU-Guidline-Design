# QUICKSTART — MIDU Vibecoder Kit

Up and running in 30 seconds. For the full story, see [README.md](README.md).

## 1. Install

Two commands in Claude Code:

```
/plugin marketplace add boizdeeptry/MIDU-Guidline-Design
/plugin install midu-vibecoder-kit@midu-skills
```

## 2. Verify

```
claude plugin details midu-vibecoder-kit@midu-skills
```

You should see **4 skills** (`midu-design-system`, `midu-brand-review`, `nextjs-frontend`, `typescript-backend`) and **2 hooks** (SessionStart, PostToolUse).

## 3. Use

Just ask for MIDU UI — *"build a MIDU landing page"*, *"style this MenaQ7 form"*. The `midu-design-system` skill auto-activates and runs its **brainstorm → brief → plan → build → review** pipeline.

> **HARD-GATE:** it writes no markup or CSS until it states a brief and you confirm (a simple "OK" counts).

Or invoke a skill directly:

- `/midu-design-system` — build MIDU-branded UI
- `/midu-brand-review` — audit UI against the brand (Blocker / Major / Minor)
- `/nextjs-frontend` — React/Next.js performance + conventions (brand-agnostic)
- `/typescript-backend` — TS backend code-style + API patterns (brand-agnostic)

## 4. Fonts & assets

- Fonts live in `design-system/fonts/`: **FZ Rubik** (display, TTF, proprietary MIDU) + **Lexend** (body, woff2, OFL) — full Vietnamese.
- Logos + 15 MIGI mascot poses live in `design-system/assets/` (transparent PNGs).
- **Self-contained page?** Inline `design-system/preview-src/fonts.css` — it already carries every face (FZ Rubik, Lexend, Quicksand, Patrick Hand) as base64 data URIs, so no path resolution or binary hunting. Embed the PNGs as data URIs too (see `examples/` build scripts).

## 5. No plugin? Fallbacks

- **Manual skill copy:** `Copy-Item -Recurse "skills\*" "$env:USERPROFILE\.claude\skills\"` (or into a project's `.claude\skills\`).
- **Other AI tools (Cursor, Windsurf…):** copy `DESIGN.md` (+ `design-system/tokens.css` and `fonts/` as needed) into the project, then tell the assistant *"Read DESIGN.md before writing any UI."*

See [README.md](README.md) → Usage for the detailed fallback steps.

## 6. Update

Everyone pulls the latest with:

```
/plugin marketplace update midu-skills
/plugin update
```
