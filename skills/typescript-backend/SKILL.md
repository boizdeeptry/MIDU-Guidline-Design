---
name: typescript-backend
description: TypeScript backend engineering standard — code-style rules (errors, async, types, validation) and API/architecture patterns (repository, service layer, caching, auth, rate limiting). Use whenever writing or reviewing Next.js Route Handlers, Server Actions, or any Node/TypeScript backend code. Framework-agnostic of brand — pair with midu-design-system for MIDU-specific request/response copy, or use standalone.
license: MIT (api-patterns.md adapted from an internal claude-skills collection; typescript-style.md distilled from the team's global TypeScript rules)
---

# TypeScript Backend Engineering

Two reference files, loaded on demand.

| Reference | Use for |
|---|---|
| `${CLAUDE_SKILL_DIR}/references/typescript-style.md` | Code-level rules: error handling, async/await, type safety, validation, null-handling, module structure, naming, testing. Read this for "is this idiomatic" questions. |
| `${CLAUDE_SKILL_DIR}/references/api-patterns.md` | Architecture-level patterns: REST structure, repository/service layers, middleware, N+1 prevention, transactions, caching (Redis/in-memory/cache-aside), JWT + RBAC, rate limiting, background jobs, structured logging. Read this for "how should this be structured" questions. |

## Before You Build (required for a new endpoint/service)

Don't write code before resolving these — ask via **AskUserQuestion** if not already answered by the request:

1. **Purpose & contract** — what business action does this perform, and what request/response shape does it promise callers? Decides whether it's a thin CRUD passthrough or needs real domain logic worth its own layer — the "why" a stack question alone won't surface.
2. **Runtime & data store** — Next.js Route Handler / Server Action / standalone Node service / serverless function — and Supabase/Postgres / another DB / external API? Changes error-response shape, cold-start concerns, and whether the repository pattern in `${CLAUDE_SKILL_DIR}/references/api-patterns.md` is worth the layer or overkill for a single query.
3. **Who calls this?** Public internet (needs rate limiting + input validation at the boundary) vs. internal-only (still validate, but auth/rate-limit needs differ).
4. **What's the failure mode users see?** A friendly message + logged detail (see `${CLAUDE_SKILL_DIR}/references/typescript-style.md` → Errors), never a raw stack trace or raw DB error to the client.

## Non-Negotiables

1. **Validate at every boundary with zod (or equivalent).** Request body, query params, env vars, third-party responses — parse once, pass typed data inward. Never trust `JSON.parse(...)` output as typed without a schema check.
2. **Never leak internals in error responses.** Log the real error server-side (`console.error`/structured logger) with enough context to debug; return a short, user-facing message with no stack trace, SQL, or internal field names.
3. **One shared schema between client and server validation** when both exist (e.g. a form that pre-validates before hitting the API) — import from one module, don't hand-roll the same rules twice.
4. **No floating promises, no sequential `await` for independent work** — see `${CLAUDE_SKILL_DIR}/references/typescript-style.md` → Async. This is the most common source of slow endpoints.
5. **Module-level singletons for expensive clients** (DB client, third-party SDK client) — construct once, reuse across warm invocations. Don't instantiate inside the request handler.
6. **RLS/authorization at the data layer, not just the API layer** — if the DB supports row-level security (Supabase/Postgres), turn it on for anything the client can reach directly; the API-layer check is a second line of defense, not the only one.

## Reference Implementation in This Repo

`${CLAUDE_PLUGIN_ROOT}/examples/midu-landing-next/src/app/api/leads/route.ts` + `${CLAUDE_PLUGIN_ROOT}/examples/midu-landing-next/src/lib/leads.ts` demonstrate: shared zod schema for client+server validation, module-level Supabase singleton, boundary error messages that never leak DB detail, and INSERT-only RLS (`${CLAUDE_PLUGIN_ROOT}/examples/midu-landing-next/supabase/schema.sql`). Use it as the template for new endpoints in this stack before inventing a new pattern.
