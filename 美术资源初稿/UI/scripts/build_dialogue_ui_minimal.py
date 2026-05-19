#!/usr/bin/env python3
"""Build minimalist bottom dialogue UI: gradient + portrait (reference VN style)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 350
PORTRAIT_H = 300
PORTRAIT_X = 24
NAME_LINE_Y = 118
TEXT_TOP_Y = 132

SPRITE = Path(r"J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-transparent-v1-feather.png")
OUT = Path(r"J:\项目\GAL\美术资源初稿\UI\UI_02_dialogue_minimal_wantang_v2.png")


def make_gradient_bar() -> Image.Image:
    """Full-canvas bottom strip: transparent top -> dark navy bottom."""
    arr = np.zeros((H, W, 4), dtype=np.uint8)
    for y in range(H):
        t = y / max(H - 1, 1)
        # smooth fade: visible across full height, strongest at bottom
        alpha = int(255 * min(1.0, t**0.85 * 0.92 + 0.08))
        # dark blue-black like reference
        arr[y, :, 0] = 12
        arr[y, :, 1] = 16
        arr[y, :, 2] = 32
        arr[y, :, 3] = alpha
    return Image.fromarray(arr, "RGBA")


def crop_bust(sprite: Image.Image) -> Image.Image:
    """Upper-body crop for dialogue portrait."""
    sprite = sprite.convert("RGBA")
    a = np.array(sprite.split()[3])
    ys, xs = np.where(a > 40)
    if len(xs) == 0:
        return sprite
    x0, x1 = xs.min(), xs.max()
    y0, y1 = ys.min(), ys.max()
    body_h = y1 - y0
    # bust: top 58% of character bbox
    y1_bust = y0 + int(body_h * 0.58)
    bust = sprite.crop((x0, y0, x1, y1_bust))
    # scale to portrait height
    bw, bh = bust.size
    scale = PORTRAIT_H / bh
    nw = max(1, int(bw * scale))
    nh = PORTRAIT_H
    bust = bust.resize((nw, nh), Image.Resampling.LANCZOS)
    return bust


def soften_portrait_edges(bust: Image.Image) -> Image.Image:
    """Natural blend: keep sprite feather, soften bottom/outer edges into gradient."""
    arr = np.array(bust.convert("RGBA"), dtype=np.float32)
    h, w = arr.shape[0], arr.shape[1]
    a = arr[..., 3].copy()
    yy, xx = np.mgrid[0:h, 0:w]
    # gentle fade at bottom (legs cut) and far left outer edge
    bottom = np.clip((h - yy) / max(h * 0.22, 1), 0, 1)
    left = np.clip(xx / max(w * 0.15, 1), 0.35, 1.0)
    a *= bottom * left
    arr[..., 3] = np.clip(a, 0, 255)
    out = Image.fromarray(arr.astype(np.uint8), "RGBA")
    return out.filter(ImageFilter.GaussianBlur(0.4))


def paste_portrait(base: Image.Image, bust: Image.Image) -> Image.Image:
    bust = soften_portrait_edges(bust)
    bw, bh = bust.size
    px = PORTRAIT_X
    py = H - bh + 6
    # very soft shadow behind character (no circle frame)
    shadow = Image.new("RGBA", (bw + 40, bh + 20), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((8, 10, bw + 28, bh + 8), radius=24, fill=(0, 0, 0, 55))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    base.alpha_composite(shadow, (px - 12, py + 4))
    base.paste(bust, (px, py), bust)
    return base


def draw_ui_chrome(base: Image.Image, portrait_right: int) -> Image.Image:
    draw = ImageDraw.Draw(base)
    text_left = portrait_right + 32
    line_right = W - 48
    draw.line(
        (text_left, NAME_LINE_Y, line_right, NAME_LINE_Y),
        fill=(255, 255, 255, 200),
        width=1,
    )
    draw.line(
        (text_left, TEXT_TOP_Y, line_right, TEXT_TOP_Y),
        fill=(255, 255, 255, 35),
        width=1,
    )
    return base


def main() -> None:
    base = make_gradient_bar()
    sprite = Image.open(SPRITE)
    bust = crop_bust(sprite)
    base = paste_portrait(base, bust)
    pr = PORTRAIT_X + bust.size[0]
    base = draw_ui_chrome(base, pr)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    base.save(OUT, "PNG")
    a = np.array(base.split()[3])
    ys, xs = np.where(a > 8)
    print("saved", OUT)
    print("size", base.size, "alpha span", xs.max() - xs.min() + 1, ys.max() - ys.min() + 1)


if __name__ == "__main__":
    main()
