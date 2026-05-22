#!/usr/bin/env python3
"""Crop full-body feather sprites to bust (waist-up) on 800x1200, feet line at canvas bottom.

Usage:
  python sprite_crop_bust.py                    # all *-feather.png in 立绘\\
  python sprite_crop_bust.py lin-wantang-standing-transparent-v1-feather.png

Output: 立绘\\bust\\{name-with-feather-suffix}-bust.png
  e.g. lin-wantang-standing-transparent-v1-feather.png
    -> bust\\lin-wantang-standing-transparent-v1-bust-feather.png
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image

SRC_DIR = Path(r"J:\项目\GAL\美术资源初稿\立绘")
OUT_DIR = SRC_DIR / "bust"
TARGET_W, TARGET_H = 800, 1200
# top of bbox -> cut (0.62 ≈ 腰上～大腿中，比 UI 0.66 略紧一点更像半身)
BUST_HEIGHT_RATIO = 0.62
ALPHA_THRESH = 40


def crop_bust_canvas(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    a = np.array(im.split()[3])
    ys, xs = np.where(a > ALPHA_THRESH)
    if ys.size == 0:
        return im
    x0, x1 = int(xs.min()), int(xs.max())
    y0, y1 = int(ys.min()), int(ys.max())
    y1_bust = y0 + int((y1 - y0) * BUST_HEIGHT_RATIO)
    bust = im.crop((x0, y0, x1, y1_bust))

    bw, bh = bust.size
    scale = min(TARGET_W / bw, TARGET_H / bh)
    nw, nh = max(1, int(bw * scale)), max(1, int(bh * scale))
    bust = bust.resize((nw, nh), Image.Resampling.LANCZOS)

    canvas = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
    canvas.paste(bust, ((TARGET_W - nw) // 2, TARGET_H - nh), bust)
    return canvas


def out_name(src: Path) -> str:
    stem = src.stem  # ...-feather
    if stem.endswith("-feather"):
        return stem[:- len("-feather")] + "-bust-feather.png"
    return stem + "-bust.png"


def process_one(src: Path) -> Path:
    out = OUT_DIR / out_name(src)
    img = crop_bust_canvas(Image.open(src))
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    return out


def main() -> None:
    if len(sys.argv) > 1:
        sources = [SRC_DIR / sys.argv[1]]
    else:
        sources = sorted(SRC_DIR.glob("*-transparent-*-feather.png"))
        sources = [p for p in sources if p.is_file() and "bust" not in p.stem]

    if not sources:
        print("No source sprites found.")
        sys.exit(1)

    for src in sources:
        if not src.exists():
            print("skip missing", src)
            continue
        out = process_one(src)
        print(src.name, "->", out.relative_to(SRC_DIR))


if __name__ == "__main__":
    main()
