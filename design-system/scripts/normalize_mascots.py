#!/usr/bin/env python3
"""
mascot_normalize.py - Normalize MIGI mascot PNG framing for consistent grid display.

Problem: MIGI mascot PNGs share a transparent canvas (~560x560) but the
character's visual footprint varies a lot by pose (full-body vs close-up).
Shown at a fixed box size with CSS object-fit:contain, poses look
inconsistently zoomed relative to each other even though every source PNG
has the same canvas dimensions.

Fix: measure the alpha-channel bounding box of the character in each PNG,
then re-compose the image onto a fresh square transparent canvas so the
character bbox HEIGHT is always the same fraction of canvas height,
horizontally centered, with slightly more headroom than footroom (standard
portrait framing - a subject with its feet near the bottom edge and a bit
of open space above reads as "grounded", not "floating" or "cut off").

Usage:
    python mascot_normalize.py INPUT.png OUTPUT.png
    python mascot_normalize.py --all SRC_DIR OUT_DIR      # batch: every migi-*.png
    python mascot_normalize.py --selftest                 # runs the built-in check

Requires: Pillow (pip install Pillow)
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

# --- Tunable framing parameters --------------------------------------------
# Target height %: how much of the canvas height the character bbox fills.
# 85% picked as the midpoint of the requested 82-88% band: high enough that
# close-up poses (migi-cry) don't float in a sea of empty canvas, low enough
# that full-body poses (migi-measure) keep breathing room and don't touch
# the frame edge (matters once a card border/shadow is layered on top in
# the style guide grid).
TARGET_HEIGHT_PCT = 0.85

# Uniform margin added around the tight alpha bbox before scaling, as a
# fraction of the bbox's own size. Anti-aliased edge pixels sit just below
# full opacity and a pixel-perfect bbox can shave them; this pads them back
# in so soft outlines/shadows don't look clipped.
CROP_MARGIN_PCT = 0.03

# Headroom/footroom split of the leftover vertical space after scaling.
# >0.5 means more empty space above the character than below it.
TOP_MARGIN_SHARE = 0.54

# Safety clamp: if scaling to TARGET_HEIGHT_PCT would push the bbox wider
# than this fraction of canvas width (e.g. an arm-wave pose that's wide
# relative to its height), scale by width instead so nothing clips off
# the sides.
MAX_WIDTH_PCT = 0.92

# --canvas-size defaults to the INPUT image's own largest dimension (see
# main()), so running the script without the flag preserves resolution and
# can never silently downscale a full-res master.
# ----------------------------------------------------------------------------


def measure_bbox(img: Image.Image) -> tuple[int, int, int, int]:
    """Return (left, top, right, bottom) of non-transparent pixels."""
    alpha = img.getchannel("A") if img.mode == "RGBA" else img.convert("RGBA").getchannel("A")
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("image is fully transparent - no visible content to bound")
    return bbox


def normalize_mascot(
    src_path: Path,
    dst_path: Path,
    canvas_size: int | None = None,
    target_height_pct: float = TARGET_HEIGHT_PCT,
    crop_margin_pct: float = CROP_MARGIN_PCT,
    top_margin_share: float = TOP_MARGIN_SHARE,
) -> dict:
    """Normalize one mascot PNG's framing. Returns before/after measurements.

    canvas_size=None (the default) preserves the input's own resolution by
    using its largest dimension — so the script never downscales a master.
    """
    img = Image.open(src_path).convert("RGBA")
    orig_size = img.size
    if canvas_size is None:
        canvas_size = max(orig_size)

    left, top, right, bottom = measure_bbox(img)
    bbox_w, bbox_h = right - left, bottom - top

    # Expand the crop by a uniform margin so we don't shave anti-aliased edges.
    margin = int(round(max(bbox_w, bbox_h) * crop_margin_pct))
    crop_box = (
        max(left - margin, 0),
        max(top - margin, 0),
        min(right + margin, orig_size[0]),
        min(bottom + margin, orig_size[1]),
    )
    cropped = img.crop(crop_box)

    # Scale so the CHARACTER bbox (not the padded crop) hits target_height_pct
    # of the new canvas, clamped so it never overflows canvas width either.
    scale = (canvas_size * target_height_pct) / bbox_h
    if bbox_w * scale > canvas_size * MAX_WIDTH_PCT:
        scale = (canvas_size * MAX_WIDTH_PCT) / bbox_w

    new_crop_w = max(1, round(cropped.width * scale))
    new_crop_h = max(1, round(cropped.height * scale))
    resized = cropped.resize((new_crop_w, new_crop_h), Image.LANCZOS)

    # Character bbox top-left within `cropped` was (left - crop_box[0], top - crop_box[1]).
    # Scale that offset too, so we know where the *character* (not the padded
    # crop) needs to land on the new canvas.
    char_off_x = (left - crop_box[0]) * scale
    char_off_y = (top - crop_box[1]) * scale
    new_bbox_h = bbox_h * scale
    new_bbox_w = bbox_w * scale

    # Vertical placement: split leftover space top/bottom per top_margin_share.
    leftover_v = canvas_size - new_bbox_h
    bbox_target_top = leftover_v * top_margin_share

    # Horizontal placement: center the character bbox.
    leftover_h = canvas_size - new_bbox_w
    bbox_target_left = leftover_h / 2

    paste_x = round(bbox_target_left - char_off_x)
    paste_y = round(bbox_target_top - char_off_y)

    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    canvas.paste(resized, (paste_x, paste_y), resized)

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dst_path)

    # Re-measure the actual output for reporting/verification.
    out_left, out_top, out_right, out_bottom = measure_bbox(canvas)
    out_bbox_h = out_bottom - out_top
    out_bbox_w = out_right - out_left

    return {
        "file": src_path.name,
        "orig_canvas": orig_size,
        "orig_bbox": (bbox_w, bbox_h),
        "orig_bbox_height_pct": bbox_h / orig_size[1],
        "new_canvas": (canvas_size, canvas_size),
        "new_bbox": (out_bbox_w, out_bbox_h),
        "new_bbox_height_pct": out_bbox_h / canvas_size,
        "new_bbox_top": out_top,
        "new_bbox_bottom_margin": canvas_size - out_bottom,
    }


def _selftest() -> None:
    """
    ponytail: smallest thing that fails if the geometry logic breaks.
    Draws two synthetic shapes at different scales/positions on different
    canvas sizes (standing in for a full-body vs close-up pose) and asserts
    both come out at the same target bbox-height ratio, centered, with more
    headroom than footroom.
    """
    import tempfile

    tmpdir = Path(tempfile.mkdtemp())

    # "full-body": a tall thin rect filling most of a 560x560 canvas.
    a = Image.new("RGBA", (560, 560), (0, 0, 0, 0))
    ImageDraw.Draw(a).rectangle([220, 40, 340, 520], fill=(255, 0, 0, 255))
    a_path = tmpdir / "a.png"
    a.save(a_path)

    # "close-up": a small square stuck in one corner of a differently-sized canvas.
    b = Image.new("RGBA", (500, 640), (0, 0, 0, 0))
    ImageDraw.Draw(b).rectangle([50, 50, 200, 200], fill=(0, 255, 0, 255))
    b_path = tmpdir / "b.png"
    b.save(b_path)

    out_a = normalize_mascot(a_path, tmpdir / "a_out.png")
    out_b = normalize_mascot(b_path, tmpdir / "b_out.png")

    for r in (out_a, out_b):
        ratio = r["new_bbox_height_pct"]
        assert abs(ratio - TARGET_HEIGHT_PCT) < 0.01, (
            f"{r['file']}: bbox height ratio {ratio:.3f} != target {TARGET_HEIGHT_PCT}"
        )
        assert r["new_bbox_top"] < r["new_bbox_bottom_margin"] * 1.3, (
            f"{r['file']}: expected top margin >= bottom margin (headroom), "
            f"got top={r['new_bbox_top']} bottom={r['new_bbox_bottom_margin']}"
        )
        assert r["new_bbox_top"] > r["new_bbox_bottom_margin"] * 0.9, (
            f"{r['file']}: top margin suspiciously small vs bottom, "
            f"got top={r['new_bbox_top']} bottom={r['new_bbox_bottom_margin']}"
        )

    # Both differently-shaped/sized source canvases must converge on the
    # same output bbox ratio - this is the whole point of the script.
    assert abs(out_a["new_bbox_height_pct"] - out_b["new_bbox_height_pct"]) < 0.005

    # "wide pose": a short wide rect that would exceed MAX_WIDTH_PCT if scaled
    # to the height target — the clamp must kick in, so its bbox height lands
    # BELOW target (never at 85%) and its width must not exceed the clamp.
    c = Image.new("RGBA", (600, 600), (0, 0, 0, 0))
    ImageDraw.Draw(c).rectangle([30, 250, 570, 360], fill=(0, 0, 255, 255))  # very wide, short
    c_path = tmpdir / "c.png"
    c.save(c_path)
    out_c = normalize_mascot(c_path, tmpdir / "c_out.png")
    cw, ch = out_c["new_bbox"]
    assert cw <= out_c["new_canvas"][0] * MAX_WIDTH_PCT + 1, (
        f"wide pose: width {cw} exceeded clamp {out_c['new_canvas'][0] * MAX_WIDTH_PCT}"
    )
    assert out_c["new_bbox_height_pct"] < TARGET_HEIGHT_PCT, (
        f"wide pose: height ratio {out_c['new_bbox_height_pct']:.3f} should be BELOW "
        f"target {TARGET_HEIGHT_PCT} when the width clamp triggers"
    )

    print("selftest OK:", out_a["new_bbox_height_pct"], out_b["new_bbox_height_pct"],
          "wide-clamp:", round(out_c["new_bbox_height_pct"], 3))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src", type=Path, nargs="?", help="source PNG, or source directory with --all")
    parser.add_argument("dst", type=Path, nargs="?", help="output PNG, or output directory with --all")
    parser.add_argument("--all", action="store_true", help="batch mode: process every migi-*.png in src dir")
    parser.add_argument("--canvas-size", type=int, default=None,
                        help="output square canvas px; default = input image's own largest dimension (preserves resolution)")
    parser.add_argument("--target-height-pct", type=float, default=TARGET_HEIGHT_PCT)
    parser.add_argument("--selftest", action="store_true", help="run the built-in geometry self-check and exit")
    args = parser.parse_args()

    if args.selftest:
        _selftest()
        return

    if args.src is None or args.dst is None:
        parser.error("src and dst are required unless --selftest is given")

    if args.all:
        args.dst.mkdir(parents=True, exist_ok=True)
        results = [
            normalize_mascot(f, args.dst / f.name, args.canvas_size, args.target_height_pct)
            for f in sorted(args.src.glob("migi-*.png"))
        ]
    else:
        results = [normalize_mascot(args.src, args.dst, args.canvas_size, args.target_height_pct)]

    for r in results:
        print(
            f"{r['file']}: orig {r['orig_canvas']} bbox {r['orig_bbox']} "
            f"({r['orig_bbox_height_pct']:.1%} h) -> new {r['new_canvas']} bbox {r['new_bbox']} "
            f"({r['new_bbox_height_pct']:.1%} h)"
        )


if __name__ == "__main__":
    main()
