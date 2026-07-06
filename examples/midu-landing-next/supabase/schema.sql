-- MIDU landing: lead-capture table. Run in Supabase SQL Editor.
create table if not exists public.leads (
  id uuid primary key default gen_random_uuid(),
  created_at timestamptz not null default now(),
  parent_name text not null check (char_length(parent_name) between 1 and 120),
  phone text not null check (phone ~ '^[0-9+ ().-]{8,20}$'),
  child_age smallint check (child_age between 0 and 18),
  note text check (char_length(note) <= 1000)
);

alter table public.leads enable row level security;

-- Public visitors may only INSERT; nobody reads via the anon key.
create policy "anon can insert leads"
  on public.leads for insert
  to anon
  with check (true);
