# Contributing — MIDU Vibecoder Kit

Internal MIDU project. This doc covers the maintenance discipline, the pre-push
gate, versioning, and how to cut a release.

## Golden rule: one source of truth

- **`DESIGN.md`** (repo root) is **generated** — author the small topic files under **`design/`** (`00-frontmatter.md`, `01-overview.md`, … `19-governance.md`), then rebuild:
  ```bash
  python scripts/build_design.py          # design/*.md  →  DESIGN.md
  ```
  The parts are exact slices, so the rebuild is byte-identical; the lint (`build_design.py --check`) fails if DESIGN.md is stale. Don't hand-edit DESIGN.md — edit the part, rebuild, then re-sync references (below).
- **`design-system/tokens.css`** is canonical (edit directly).
- After editing either, **re-copy BOTH into `skills/midu-design-system/references/`**:
  ```powershell
  Copy-Item DESIGN.md, design-system\tokens.css "skills\midu-design-system\references\"
  ```
  Never edit the `references/` copies directly — that forks the spec. The lint
  fails if they drift.
- `design-system/preview.html` and `examples/midu-landing/midu-landing.html` are
  **generated**. Edit the template (`preview-src/preview-template.html`, `examples/midu-landing/template.html`),
  then rebuild with the matching `build*.py`. The lint fails if a committed artifact
  is stale.
- **Never fabricate data** (dosages, prices, stats, doctors, citations). Pull real
  facts from the company knowledge base (`Z:\DU LIEU MIDU\MIDU BRAIN`) or use a
  clearly-labelled placeholder. See DESIGN.md → Voice §5 and Non-Negotiable #13.

## Pre-push gate

Run the consistency lint before every push (CI runs the same thing):

```bash
python scripts/check_kit.py
```

It checks: references in sync, token-graph resolves, manifests parse + versions
agree, generated preview/example current, mascot self-test, fonts present. It must
print **All checks passed** (exit 0). CI (`.github/workflows/ci.yml`) additionally
builds the Next.js example.

## Versioning

Two deliberate version lines:

- **Plugin version** (`plugin.json` + both `marketplace.json` fields) — SemVer, the
  release consumers pin, git-tagged. **This is the release of record.**
- **DESIGN.md spec version** (frontmatter) — tracks design-system maturity.

They move together at a release but mean different things; the CHANGELOG lists both
(e.g. plugin 1.3.0 ↔ spec 0.4.0). Bump MINOR for additive changes (new token/
component/section), PATCH for fixes/docs, MAJOR for a breaking token rename/removal.

## Cutting a release

1. Ensure `python scripts/check_kit.py` passes and the working tree is clean.
2. Bump the version in `plugin.json` and **both** `version` fields in `marketplace.json`
   (metadata + the plugin entry) to the new `X.Y.Z`.
3. Add a CHANGELOG.md entry (move items from `[Unreleased]`), noting the matching
   DESIGN.md spec version.
4. Commit, then tag with the plugin CLI (validates that the manifests agree):
   ```bash
   claude plugin tag
   ```
   This creates `midu-vibecoder-kit--vX.Y.Z`.
5. Push commits and the tag. Consumers update with:
   ```
   /plugin marketplace update midu-skills
   /plugin update midu-vibecoder-kit@midu-skills
   ```

## Fonts & assets

FZ Rubik and the MIGI/logo art are **proprietary MIDU** assets (see
THIRD-PARTY-NOTICES.md). Do not redistribute them outside the company. The repo's
public status vs the committed FZ Rubik font is an open compliance item — see
DESIGN.md → Known Gaps.
