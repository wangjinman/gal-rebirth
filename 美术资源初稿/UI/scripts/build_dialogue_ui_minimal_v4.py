#!/usr/bin/env python3
"""v4: portrait first, then veil gradient on top — reference VN blend."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 350
SPRITE = Path(r"J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-transparent-v1-feather.png")
OUT = Path(r"J:\项目\GAL\美术资源初稿\UI\UI_02_dialogue_minimal_wantang_v4.png")


def crop_bust(sprite: Image.Image) -> Image.Image:
    sprite = sprite.convert("RGBA")
    a = np.array(sprite.split()[3])
    ys, xs = np.where(a > 40)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    y1 = y0 + int((y1 - y0) * 0.64)
    bust = sprite.crop((x0, y0, x1, y1))
    th = int(H * 0.96)
    bw, bh = bust.size
    s = th / bh
    return bust.resize((max(1, int(bw * s)), th), Image.Resampling.LANCZOS)


def make_veil() -> Image.Image:
    """Dark gradient layer composited over entire UI including portrait."""
    arr = np.zeros((H, W, 4), dtype=np.uint8)
    for y in range(H):
        t = y / max(H - 1, 1)
        a = int(255 * min(0.94, t**0.7 * 0.82 + 0.1))
        for x in range(W):
            lx = max(0, 1.0 - x / (W * 0.5))
            aa = min(255, int(a * (0.88 + 0.12 * lx)))
            arr[y, x] = (10, 14, 28, aa)
    veil = Image.fromarray(arr, "RGBA")
    return veil.filter(ImageFilter.GaussianBlur(0.6))


def soften_feet(bust: Image.Image) -> Image.Image:
    arr = np.array(bust, dtype=np.float32)
    h, w = arr.shape[0], arr.shape[1]
    yy = np.arange(h, dtype=np.float32)[:, None]
    fade = np.clip((h - yy) / max(h * 0.22, 1), 0, 1) ** 1.3
    arr[..., 3] *= fade
    out = Image.fromarray(arr.astype(np.uint8), "RGBA")
    return out.filter(ImageFilter.GaussianBlur(0.5))


def main() -> None:
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    bust = soften_feet(crop_bust(Image.open(SPRITE)))
    px, py = 0, H - bust.size[1]
    canvas.paste(bust, (px, py), bust)
    veil = make_veil()
    canvas = Image.alpha_composite(canvas, veil)
    # whisper-thin text guides
    draw = ImageDraw.Draw(canvas)
    tx = bust.size[0] + 28
    draw.line((tx, 114, W - 36, 114), fill=(255, 255, 255, 48), width=1)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT, "PNG")
    print("saved", OUT)


if __name__ == "__main__":
    main()
