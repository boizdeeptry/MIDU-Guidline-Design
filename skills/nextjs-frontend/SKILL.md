---
name: nextjs-frontend
description: React/Next.js engineering standard — performance rules (Vercel Engineering), Next.js framework conventions, and component-architecture patterns. Use whenever writing, reviewing, or refactoring React components, Next.js pages/routes, or client-side data fetching. Framework-agnostic of brand — pair with the midu-design-system skill for MIDU-branded UI, or use standalone on any React/Next.js codebase.
license: MIT (vercel-performance.md is Vercel Engineering, MIT-licensed; see file header)
---

# Next.js / React Frontend Engineering

Three reference bundles, loaded on demand — this file is the router, not the content.

| Reference | Use for |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/vercel-performance.md` | Performance rules: waterfalls, bundle size, server/client data fetching, re-renders, rendering, raw JS perf. **Read first** for any perf-sensitive change. |
| `${CLAUDE_SKILL_DIR}/references/nextjs/*.md` | Next.js framework conventions — see topic index below. |
| `${CLAUDE_SKILL_DIR}/references/component-patterns.md` | Component-API architecture: composition vs. inheritance, compound components, render props, custom hooks, context+reducer, error boundaries, forms, a11y. |

### `${CLAUDE_SKILL_DIR}/references/nextjs/` topic index

| File | Topic |
|---|---|
| `file-conventions.md` | Project structure, special files, route segments, parallel/intercepting routes, v16 middleware→proxy rename |
| `rsc-boundaries.md` | Valid/invalid Server-Component patterns, non-serializable props, Server Action exceptions |
| `async-patterns.md` | Next.js 15+ async `params`/`searchParams`/`cookies()`/`headers()`, migration codemod |
| `runtime-selection.md` | Node.js runtime by default; when Edge is actually appropriate |
| `directives.md` | `'use client'`, `'use server'`, `'use cache'` |
| `functions.md` | `useRouter`/`usePathname`/`useSearchParams`/`useParams`, `cookies`/`headers`/`draftMode`/`after`, `generateStaticParams`/`generateMetadata` |
| `error-handling.md` | `error.tsx`, `global-error.tsx`, `not-found.tsx`, `redirect`/`notFound`/`forbidden`/`unauthorized`, `unstable_rethrow` |
| `data-patterns.md` | Server Components vs. Server Actions vs. Route Handlers; avoiding waterfalls; client-side fetching |
| `route-handlers.md` | `route.ts` basics, conflicts with `page.tsx`, when to prefer Server Actions instead |
| `metadata.md` | Static/dynamic metadata, `generateMetadata`, OG images via `next/og` |
| `image.md` | `next/image` over `<img>`, remote config, `sizes`, blur placeholders, LCP priority |
| `font.md` | `next/font` setup (Google/local), Tailwind integration, subset preloading |
| `bundling.md` | Server-incompatible packages, CSS imports, ESM/CJS pitfalls, bundle analysis |
| `scripts.md` | `next/script` vs. native tags, loading strategies, `@next/third-parties` |
| `hydration-error.md` | Common causes (browser APIs, dates, invalid HTML) and fixes |
| `suspense-boundaries.md` | Which hooks force a CSR bailout and need a Suspense boundary |
| `parallel-routes.md` | `@slot` + `(.)` interceptor modal patterns, `default.tsx`, closing with `router.back()` |
| `self-hosting.md` | `output: 'standalone'`, cache handlers for multi-instance ISR |
| `debug-tricks.md` | MCP debug endpoint, `--debug-build-paths` |

## When to Activate

- Writing or reviewing any React component or Next.js page/layout
- Implementing data fetching (Server Components, Server Actions, Route Handlers, or client-side)
- Touching bundle size, load performance, or re-render behavior
- Anything under `app/` or `pages/` in a Next.js project

## Non-Negotiables (from `${CLAUDE_SKILL_DIR}/references/vercel-performance.md` — read the file for the full rule + example)

1. **No data waterfalls.** Independent fetches go through `Promise.all`; don't `await` sequentially when nothing depends on the prior result. Start promises early, await late in Route Handlers/Server Actions.
2. **No barrel-file imports** for anything non-trivial — import directly from the source module. Use `next/dynamic` for heavy/rarely-shown components.
3. **Cache server-side reads.** `React.cache()` for per-request dedup, an LRU cache for cross-request. Never re-fetch the same data twice in one render pass.
4. **Minimize what crosses the server→client boundary.** Serialize only what the client component actually needs.
5. **Don't subscribe to state you only read in a callback.** Read via ref/latest-value pattern instead of adding it to a dependency array that re-renders the tree.
6. **`next/image` and `next/font` are mandatory** — never a bare `<img>` or manual `@font-face` for anything `next/font` covers (see `${CLAUDE_SKILL_DIR}/references/nextjs/image.md`, `${CLAUDE_SKILL_DIR}/references/nextjs/font.md`).
7. **Ternary over `&&` for conditional rendering** — `cond && <Foo/>` renders a stray `0`/`NaN` when `cond` is a non-boolean falsy value.

## Workflow

1. Know the task shape first: perf fix → `${CLAUDE_SKILL_DIR}/references/vercel-performance.md`; "how does Next.js do X" → the matching `${CLAUDE_SKILL_DIR}/references/nextjs/*.md` file; "how should this component be structured" → `${CLAUDE_SKILL_DIR}/references/component-patterns.md`.
2. If the project also has the `midu-design-system` skill installed, brand tokens/components win for anything visual — this skill only governs *how* the React/Next.js code is written, not colors/spacing/typography.
3. Don't apply a performance rule speculatively — most of `vercel-performance.md` is impact-ranked (CRITICAL → LOW); fix waterfalls and bundle size before reaching for `js-*` micro-optimizations.
