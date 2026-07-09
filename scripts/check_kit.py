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
        fail(f"DESIGN.md stale vs design/ — run build_design.py: {(r.stdout + r.stderr).strip()[-600:]}")


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
def _norm_generated(raw: bytes) -> str:
    """Normalize away environment noise before comparing a rebuilt HTML artifact:
    - line endings (Windows-built vs Linux-CI), and
    - base64 data URIs — PNG re-encoding is NOT byte-stable across Pillow
      versions/platforms, so comparing embedded image/font bytes gives false
      'stale' hits. We only care that the markup/CSS/text is up to date."""
    s = raw.decode("utf-8", "replace").replace("\r\n", "\n")
    return re.sub(r"data:[a-z/;+-]*base64,[A-Za-z0-9+/=]+", "data:BASE64", s)


def check_generated_current() -> None:
    print("[4] generated artifacts current (markup/CSS, ignoring embedded-asset bytes)")
    builds = [
        ("design-system/preview.html", "design-system/preview-src/build-preview.py"),
        ("examples/midu-landing/midu-landing.html", "examples/midu-landing/build.py"),
    ]
    for out, script in builds:
        before = (ROOT / out).read_bytes() if (ROOT / out).exists() else None
        r = subprocess.run([sys.executable, str(ROOT / script)],
                           cwd=ROOT, capture_output=True, text=True)
        if r.returncode != 0:
            fail(f"{script} errored: {r.stderr.strip()[-400:]}")
            continue
        after = (ROOT / out).read_bytes()
        if before is None:
            fail(f"{out} did not exist; now built")
        elif _norm_generated(before) == _norm_generated(after):
            ok(f"{out} up to date")
        else:
            fail(f"{out} was stale — template changed but not rebuilt; run its build script and commit")


# 5. mascot normalize self-test ----------------------------------------------
def check_mascot_selftest() -> None:
    print("[5] mascot script self-test")
    r = subprocess.run([sys.executable, str(ROOT / "design-system/scripts/normalize_mascots.py"), "--selftest"],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode == 0 and "selftest OK" in (r.stdout + r.stderr):
        ok("normalize_mascots.py --selftest")
    else:
        fail(f"mascot selftest failed: {(r.stdout + r.stderr).strip()[-400:]}")


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


# 7. Tailwind theme file aliases resolve to real tokens ----------------------
def check_theme_aliases() -> None:
    print("[7] tailwind theme aliases resolve")
    theme = read("design-system/midu-theme.css")
    tokens = read("design-system/tokens.css")
    if '@import "./tokens.css"' not in theme and '@import "tokens.css"' not in theme:
        fail("midu-theme.css must @import tokens.css (values live there)")
    defined = set(re.findall(r"^\s*(--(?:midu|migi)-[a-z0-9-]+)\s*:", tokens, re.M))
    referenced = set(re.findall(r"var\((--midu-[a-z0-9-]+)\)", theme))
    missing = sorted(referenced - defined)
    if missing:
        fail(f"midu-theme.css references tokens not in tokens.css: {', '.join(missing)}")
    else:
        ok(f"all {len(referenced)} theme aliases map to defined tokens")


# 8. hooks.json valid + cross-platform (no dead per-OS fields) ---------------
def check_hooks() -> None:
    print("[8] hooks.json valid + portable")
    raw = read("hooks/hooks.json")
    try:
        data = json.loads(raw)
    except Exception as e:
        fail(f"hooks/hooks.json invalid JSON: {e}")
        return
    # commandWindows is NOT a real Claude Code hook field — it is silently dropped,
    # so relying on it (with `exec` in the POSIX command) breaks native Windows/PowerShell.
    if "commandWindows" in raw:
        fail("hooks.json uses `commandWindows` (not a valid field) — use exec form: command+args")
        return
    entries = [h for group in data.get("hooks", {}).values()
               for m in group for h in m.get("hooks", [])]
    missing = []
    for h in entries:
        for a in h.get("args", []):
            rel = a.replace("${CLAUDE_PLUGIN_ROOT}/", "")
            if rel.endswith(".js") and not (ROOT / rel).exists():
                missing.append(rel)
    if missing:
        fail(f"hooks.json points at missing scripts: {', '.join(missing)}")
    else:
        ok(f"hooks.json valid, exec form, {len(entries)} hooks resolve")


# 9. every ${CLAUDE_PLUGIN_ROOT}/${CLAUDE_SKILL_DIR} path in a SKILL.md resolves
#    on the installed tree (the kit's #1 recurring bug: "teammate can't find file")
def check_skill_paths() -> None:
    print("[9] skill file references resolve")
    pat = re.compile(r"\$\{CLAUDE_(PLUGIN_ROOT|SKILL_DIR)\}(/[^\s\"'`)\]<>]*)")
    keep = re.compile(r"[A-Za-z0-9._/*-]+")
    dangling = []
    checked = 0
    for skill_md in sorted(ROOT.glob("skills/*/SKILL.md")):
        base_skill = skill_md.parent
        for var, rest in pat.findall(read(str(skill_md.relative_to(ROOT)))):
            m = keep.match(rest.lstrip("/"))
            if not m:
                continue
            rel = m.group(0)
            base = ROOT if var == "PLUGIN_ROOT" else base_skill
            checked += 1
            if "*" in rel:
                if not list(base.glob(rel)):
                    dangling.append(f"{skill_md.parent.name}: ${{CLAUDE_{var}}}/{rel} (no glob match)")
            elif not (base / rel).exists():
                dangling.append(f"{skill_md.parent.name}: ${{CLAUDE_{var}}}/{rel}")
    if dangling:
        for d in dangling[:12]:
            fail(f"unresolved skill ref — {d}")
    else:
        ok(f"all {checked} ${{CLAUDE_*}} refs across skills resolve")


def main() -> int:
    print("MIDU kit consistency check\n" + "=" * 34)
    for chk in (check_design_built, check_refs_in_sync, check_token_graph, check_manifests,
                check_generated_current, check_mascot_selftest, check_fonts, check_theme_aliases,
                check_hooks, check_skill_paths):
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
