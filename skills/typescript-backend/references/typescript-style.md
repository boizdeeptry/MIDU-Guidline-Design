# TypeScript Code Style

Distilled from the team's global TypeScript standard (`~/.claude/rules/typescript/`). Targets TypeScript 5.x, Node/Next.js Route Handlers and Server Actions.

## Compiler Config

Start every project from `strict: true`, then add what `strict` doesn't cover:

```jsonc
{
  "compilerOptions": {
    "target": "es2022",
    "module": "nodenext",              // bundled apps (Next.js): "preserve" instead
    "moduleResolution": "nodenext",
    "strict": true,
    "noUncheckedIndexedAccess": true,  // adds `| undefined` to indexed access
    "exactOptionalPropertyTypes": true,
    "noPropertyAccessFromIndexSignature": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitReturns": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true
  }
}
```

**Why:** each flag rules out a whole bug class at the type-checker for free. Retrofitting `strict` onto an existing codebase is painful — start with it.

## Errors

- **Throw `Error` (or a subclass), never strings/plain objects.** Stack traces attach to `Error` instances only.
- **Subclass for distinct failure modes** callers will branch on (`HttpError`, `NotFoundError`); set `.name` in the constructor.
- **Wrap with `Error.cause`, not string concatenation:**
  ```ts
  throw new Error(`failed to load user ${id}`, { cause: err });
  ```
- **Catch `unknown`, narrow before use** — TypeScript already types the catch binding as `unknown` under `strict`; anything can be thrown.
- **Don't swallow errors.** Empty `catch {}` is a bug unless commented with why ignoring is correct.
- **Log or wrap-and-return — never both.** Logging at every layer produces duplicate noise; pick the boundary that owns the response.
- Result/Either types are optional, not default — only reach for them in library code with a small enumerable error set the caller will branch on.

## Async

- **`async/await`, not `.then()` chains** except trivial one-liners — stack traces stay usable, branching stays readable.
- **`Promise.all` for independent work.** Sequential `await` only when a later call genuinely depends on an earlier result. This is the #1 cause of "why is this endpoint slow."
- **Never `await` inside a `for` loop for independent items** — `Promise.all(items.map(fn))` instead.
- **No floating promises.** Every promise is `await`ed, returned, `.catch`-handled, or explicitly `void`-ed. Enforce with `@typescript-eslint/no-floating-promises`.
- **Pass `AbortSignal`** through any I/O that should be cancellable; wire it to `fetch`/timeouts.

## Types

- **`type` by default; `interface` only for declaration merging** (extending a library's ambient types) or class-like `extends` chains.
- **Never `any`. `unknown` at trust boundaries** (JSON.parse, third-party APIs, webhook payloads) — narrow before use.
- **Discriminated unions over optional-everywhere objects** when fields' presence depends on each other — makes illegal states unrepresentable:
  ```ts
  type Result = { ok: true; data: User } | { ok: false; error: string };
  ```
- **`as const` + `satisfies`** for literal lookup tables — `satisfies` validates shape without widening values.
- **No `enum`** — numeric enums ship a runtime inverse-mapping object; use `as const` objects or string-literal unions instead.
- **Validate everything crossing a system boundary with a schema library (zod)** — request bodies, query params, env vars, third-party responses. Parse once at the boundary, pass typed data inward.

## Null & Undefined

- **`undefined` for "absent" in your own code; `null` only where an external system already uses it** (DB rows, JSON APIs).
- **`?.` for safe deep access, `??` for defaults** — never `||` for defaults (it also replaces `0`, `""`, `false`).
- **Treat `!` as a smell.** Narrow with a real check or a helper that throws a real error instead of asserting.

## Modules

- **Named exports, not default** — consistent identifiers, better auto-import, grep-able.
- **No barrel files (`index.ts` re-exporting a directory)** in application code — they wreck tree-shaking and slow cold starts. Import the exact module.
- **`import type` for type-only imports** — required for transpile-only tools, guarantees no runtime side effect.

## Functions

- **Annotate return types on every exported function** — inference is convenient locally but forces readers (and future refactors) to walk the body.
- **Cap positional params at 3; an options object beyond that.**
- **Pure by default.** If a function mutates, name it so (`sortInPlace`, `pushAll`).

## Naming

| Kind | Convention |
|---|---|
| Variables, functions | `camelCase` |
| Types, interfaces, classes | `PascalCase` |
| Module-level constants | `CONSTANT_CASE` |
| Files | `kebab-case.ts` |
| Booleans | `is`/`has`/`can`/`should` prefix |

No Hungarian prefixes (`IUser`, `TResult`), no `Type`/`Interface` suffixes — the language already tells you what something is.

## Testing

- **One behavior per test.** `it("does X when Y")`, no conditional assertions.
- **Mock what you don't own** (network/filesystem boundary) — never mock your own modules; pass dependencies in instead.
- **Fake timers from the runner** (`vi.useFakeTimers()`), never real `setTimeout` waits in tests.
- **Wait on conditions (`findBy*`/`waitFor`), never on a fixed sleep.**

## Anti-Patterns (lint-enforced)

`any`, `@ts-ignore` (use `@ts-expect-error` + comment), floating promises, mutating function parameters, `console.log` in committed code, empty `catch {}`, `JSON.parse(JSON.stringify(x))` for deep copies (use `structuredClone`), non-null assertion `!`, `==` instead of `===`, commented-out code.

## Sources

- Full rule set with rationale and citations: `~/.claude/rules/typescript/` (tsconfig, errors, async, types, null-undefined, modules, functions, naming, testing, anti-patterns, generics, immutability, classes).
- [TypeScript Handbook](https://www.typescriptlang.org/docs/) · [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html) · [typescript-eslint rules](https://typescript-eslint.io/rules/) · [Effective TypeScript](https://effectivetypescript.com/)
