#!/usr/bin/env python3
"""MIDU Vibecoder Kit — consistency lint. Run before every push; CI runs it too.

Catches the drift classes this kit has actually hit: references out of sync with
the canonical DESIGN.md/tokens.css, dangling {token} references, manifest version
mismatch, generated preview/example not rebuilt after a template edit, missing
fonts. Each check prints PASS/FAIL; the script exits non-zero if any FAIL.

Usage:  python scripts/check_kit.py
Requires: Python 3, Pillow (for the mascot self-test + build scripts).
The Next.js example build is a separate CI job (needs Node), not checked here.
"""
import io
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILS: list[str] = []
PASSES: list[str] = []


def ok(msg: str) -> None:
    PASSES.append(msg)
    print(f"  PASS  {msg}")


def fail(msg: str) -> None:
    FAILS.append(msg)
    print(f"  FAIL  {msg}")


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


# 0. DESIGN.md is the current concatenation of design/ parts -------------------
def check_design_built() -> None:
    print("[0] DESIGN.md built from design/ parts")
    r = subprocess.run([sys.executable, str(ROOT / "scripts/build_design.py"), "--check"],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0:
        ok("DESIGN.md matches design/ parts")
    else:
        fail(f"DESIGN.md stale vs design/ — run build_design.py: {(r.stdout + r.stderr).strip()[:160]}")


# 1. references byte-identical to canonical sources ---------------------------
def check_refs_in_sync() -> None:
    print("[1] references in sync")
    for rel in ("DESIGN.md", "design-system/tokens.css"):
        ref = f"skills/midu-design-system/references/{Path(rel).name}"
        if not (ROOT / ref).exists():
            fail(f"{ref} missing")
            continue
        if read(rel) == read(ref):
            ok(f"{rel} == {ref}")
        else:
            fail(f"{rel} != {ref} — re-copy into references/ after editing")


# 2. every {token} reference resolves to a defined frontmatter key ------------
def check_token_graph() -> None:
    print("[2] token graph resolves")
    txt = read("DESIGN.md")
    fm = txt.split("---", 2)[1]
    try:
        import yaml
        data = yaml.safe_load(fm)
    except Exception:
        # PyYAML absent — skip gracefully but say so (CI installs it)
        print("  SKIP  PyYAML not installed; token-graph check skipped")
        return
    groups = ("colors", "typography", "components", "motion", "rounded",
              "spacing", "focus", "breakpoints", "container", "elevation")
    defined = {g: set((data.get(g) or {}).keys()) for g in groups}
    dangling = []
    for g, key in re.findall(r"\{([a-z]+)\.([a-z0-9-]+)\}", txt):
        if g in defined and key not in defined[g]:
            # some are nested/derived (e.g. grad-brand-start under colors) — only
            # flag groups we fully enumerate
            dangling.append(f"{{{g}.{key}}}")
    dangling = sorted(set(dangling))
    if dangling:
        fail(f"dangling token refs: {', '.join(dangling[:12])}")
    else:
        ok("all enumerated {group.key} refs resolve")


# 3. manifests parse, versions agree, skill paths exist -----------------------
def check_manifests() -> None:
    print("[3] manifests parse + agree")
    try:
        plugin = json.loads(read(".claude-plugin/plugin.json"))
        mkt = json.loads(read(".claude-plugin/marketplace.json"))
    except Exception as e:
        fail(f"manifest JSON invalid: {e}")
        return
    ok("plugin.json + marketplace.json are valid JSON")
    entry = next((p for p in mkt.get("plugins", []) if p.get("name") == plugin["name"]), None)
    versions = {plugin.get("version"), mkt.get("metadata", {}).get("version")}
    if entry:
        versions.add(entry.get("version"))
    if len(versions) == 1 and None not in versions:
        ok(f"all version fields agree ({versions.pop()})")
    else:
        fail(f"version fields disagree: {versions}")
    for s in plugin.get("skills", []):
        if not (ROOT / s.lstrip("./")).exists():
            fail(f"skill path missing: {s}")
    else:
        if plugin.get("skills"):
            ok("all skill paths exist")


# 4. generated artifacts are current (template edited but not rebuilt?) -------
def check_generated_current() -> None:
    print("[4] generated artifacts current")
    builds = [
        ("design-system/preview.html", "design-system/preview-src/build-preview.py"),
        ("examples/midu-landing/midu-landing.html", "examples/midu-landing/build.py"),
    ]
    for out, script in builds:
        before = (ROOT / out).read_bytes() if (ROOT / out).exists() else None
        r = subprocess.run([sys.executable, str(ROOT / script)],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            fail(f"{script} errored: {r.stderr.strip()[:200]}")
            continue
        after = (ROOT / out).read_bytes()
        if before is None:
            fail(f"{out} did not exist; now built")
        elif before == after:
            ok(f"{out} up to date")
        else:
            fail(f"{out} was stale — rebuilt now differs; commit the rebuild")


# 5. mascot normalize self-test ----------------------------------------------
def check_mascot_selftest() -> None:
    print("[5] mascot script self-test")
    r = subprocess.run([sys.executable, str(ROOT / "design-system/scripts/normalize_mascots.py"), "--selftest"],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0 and "selftest OK" in (r.stdout + r.stderr):
        ok("normalize_mascots.py --selftest")
    else:
        fail(f"mascot selftest failed: {(r.stdout + r.stderr).strip()[:200]}")


# 6. fonts present + css references resolve ----------------------------------
def check_fonts() -> None:
    print("[6] fonts bundled")
    rubik = list((ROOT / "design-system/fonts/FzRubik").glob("*.ttf"))
    lexend = list((ROOT / "design-system/fonts/Lexend").glob("*.woff2"))
    ok(f"FZ Rubik TTF: {len(rubik)} files") if len(rubik) == 4 else fail(f"expected 4 FZ Rubik TTF, found {len(rubik)}")
    ok(f"Lexend woff2: {len(lexend)} files") if len(lexend) == 9 else fail(f"expected 9 Lexend woff2, found {len(lexend)}")
    for css in ("design-system/fonts/fzrubik.css", "design-system/fonts/lexend.css"):
        for url in re.findall(r'url\("([^"]+)"\)', read(css)):
            if url.startswith("data:"):
                continue
            if not (ROOT / "design-system/fonts" / url).exists():
                fail(f"{css} references missing file: {url}")
        else:
            ok(f"{css} references resolve")


def main() -> int:
    print("MIDU kit consistency check\n" + "=" * 34)
    for chk in (check_design_built, check_refs_in_sync, check_token_graph, check_manifests,
                check_generated_current, check_mascot_selftest, check_fonts):
        chk()
    print("=" * 34)
    print(f"{len(PASSES)} passed, {len(FAILS)} failed")
    if FAILS:
        print("\nFAILURES:")
        for f in FAILS:
            print(f"  - {f}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
