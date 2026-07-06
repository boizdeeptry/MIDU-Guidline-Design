#!/usr/bin/env python3
"""Rebuild midu-landing.html from template.html. Requires: Pillow."""
import base64
import io
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "..", "design-system", "assets"))
FONTS_CSS = os.path.normpath(os.path.join(HERE, "..", "..", "design-system", "preview-src", "fonts.css"))

IMAGES = {  # placeholder -> (source in design-system/assets, max box px = 2x render size)
    "__IMG_logo__": ("logo-midu.png", 180),
    "__IMG_logowhite__": ("logo-midu-white.png", 180),
    "__IMG_hello__": ("migi-hello.png", 560),
    "__IMG_medicine__": ("migi-medicine.png", 560),
    "__IMG_love__": ("migi-love.png", 440),
}

html = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
html = html.replace("__FONT_CSS__", open(FONTS_CSS, encoding="utf-8").read())
for placeholder, (name, box) in IMAGES.items():
    im = Image.open(os.path.join(ASSETS, name))
    im.thumbnail((box, box), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    html = html.replace(placeholder, uri)

if "__IMG_" in html or "__FONT_CSS__" in html:
    raise SystemExit("unresolved placeholders remain — check IMAGES map")

out = os.path.join(HERE, "midu-landing.html")
open(out, "w", encoding="utf-8").write(html)
print(f"built {out} ({os.path.getsize(out) // 1024} KB)")
