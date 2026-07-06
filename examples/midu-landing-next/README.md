# MIDU Landing — Next.js + Tailwind + Supabase

Production implementation of the MIDU MenaQ7 landing page, built with the MIDU Vibecoder Kit
(tokens from `DESIGN.md`, FZ Rubik, MIGI assets). Lead-capture form stores submissions in Supabase.

## Setup

```bash
npm install

# 1. Create a Supabase project → SQL Editor → run supabase/schema.sql
# 2. Copy env template and fill in Settings → API values
cp .env.example .env.local

npm run dev   # http://localhost:3000
```

## Deploy (Vercel)

1. Push this folder to a Git repo → **vercel.com → Add New Project** → import.
2. Add the two `NEXT_PUBLIC_SUPABASE_*` env vars in Project Settings → Environment Variables.
3. Deploy. Every push gets a preview URL; `main` goes to production.

## Structure

- `src/app/` — layout (FZ Rubik via `next/font/local`, `lang="vi"`), page, `api/leads` route
- `src/components/` — one section per file; `LeadForm` is the only client component
- `src/lib/leads.ts` — zod schema shared by client and API route
- `supabase/schema.sql` — `leads` table + INSERT-only RLS policy (anon key can write, never read)

## Brand notes

- Tokens live in `globals.css` `@theme` — do not introduce colors/shadows outside it.
- One gradient CTA per viewport: nav CTA is deliberately the secondary style.
- All figures/quotes are placeholders marked `*Thông tin minh họa` — replace with approved copy
  before public launch. Confirm FZ Rubik's license covers web embedding.
