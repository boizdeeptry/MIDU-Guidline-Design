#!/usr/bin/env python3
"""Rebuild ../preview.html from preview-template.html.

Inlines fonts.css (FZ Rubik subsets + Quicksand + Patrick Hand as data URIs)
and base64-embeds images resized from ../assets full-res sources.
Requires: Pillow.  Usage: python build-preview.py
"""
import base64
import functools
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
OUT = os.path.normpath(os.path.join(HERE, "..", "preview.html"))

# placeholder -> (source file in ../assets, max box px)
# Sizes = 2x the largest CSS render size, so retina stays sharp without waste.
IMAGES = {
    "__IMG_logo__": ("logo-midu.png", 180),              # nav, h34 (bare logo — tagline illegible at nav size)
    "__IMG_logofull__": ("logo-midu.png", 440),          # logo card, 220px
    "__IMG_logowhite__": ("logo-midu-white.png", 440),
    "__IMG_logotagline__": ("logo-midu-tagline.png", 440),
    "__IMG_hello__": ("migi-hello.png", 560),            # hero, renders ~340px
    "__IMG_measure__": ("migi-measure.png", 260),        # mascot grid, 130px
    "__IMG_medicine__": ("migi-medicine.png", 260),
    "__IMG_cheer__": ("migi-cheer.png", 260),
    "__IMG_wow__": ("migi-wow.png", 260),
    "__IMG_love__": ("migi-love.png", 260),
    "__IMG_cry__": ("migi-cry.png", 260),
    "__IMG_goodnight__": ("migi-goodnight.png", 260),
    "__IMG_exercise__": ("migi-exercise.png", 260),
}


@functools.lru_cache(maxsize=None)
def _load(name: str) -> Image.Image:
    return Image.open(os.path.join(ASSETS, name))


def image_data_uri(name: str, box: int) -> str:
    im = _load(name).copy()  # two placeholders can share one source (e.g. the logo)
    im.thumbnail((box, box), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


with open(os.path.join(HERE, "preview-template.html"), encoding="utf-8") as f:
    html = f.read()
with open(os.path.join(HERE, "fonts.css"), encoding="utf-8") as f:
    html = html.replace("__FONT_CSS__", f.read())
for placeholder, (name, box) in IMAGES.items():
    html = html.replace(placeholder, image_data_uri(name, box))

if "__IMG_" in html or "__FONT_CSS__" in html:
    raise SystemExit("unresolved placeholders remain — check IMAGES map")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"built {OUT} ({os.path.getsize(OUT) // 1024} KB)")
