#!/usr/bin/env python3
"""UI_02 minimal dialogue bar — Scheme A (portrait head overflow above bar).

Spec: ../DIALOGUE_UI_MINIMAL_SPEC.md
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W = 1920
H_BAR = 350
OVERFLOW_TOP = 90

SPRITE = Path(r"J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-transparent-v1-feather.png")
OUT = Path(r"J:\项目\GAL\美术资源初稿\UI\UI_02_dialogue_minimal_wantang_posA_overflow_top.png")

TINT = np.array([32, 42, 72], dtype=np.float32)
PORTRAIT_SCALE = 1.14


def make_gradient_bar(height: int, y_offset: int) -> np.ndarray:
    arr = np.zeros((y_offset + height, W, 4), dtype=np.float32)
    for yi in range(height):
        y = y_offset + yi
        t = yi / max(height - 1, 1)
        base_a = min(0.78, t**0.8 * 0.62 + 0.04)
        for x in range(W):
            lx = 1.0 - min(1.0, x / (W * 0.45))
            boost = (1.0 - t) * 0.07 * lx
            a = min(0.82, base_a + boost)
            arr[y, x, :3] = TINT
            arr[y, x, 3] = a * 255
    return arr


def crop_bust(sprite: Image.Image) -> Image.Image:
    sprite = sprite.convert("RGBA")
    a = np.array(sprite.split()[3])
    ys, xs = np.where(a > 40)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    y1_bust = y0 + int((y1 - y0) * 0.66)
    bust = sprite.crop((x0, y0, x1, y1_bust))
    target_h = int(H_BAR * PORTRAIT_SCALE)
    s = target_h / bust.size[1]
    return bust.resize((max(1, int(bust.size[0] * s)), target_h), Image.Resampling.LANCZOS)


def blend_mask(alpha: np.ndarray) -> np.ndarray:
    h, w = alpha.shape
    a = np.clip(alpha.astype(np.float32), 0, 1)
    yy = np.arange(h, dtype=np.float32)[:, None]
    bottom = np.clip((h - yy) / max(h * 0.26, 1), 0, 1) ** 1.05
    core = a > 0.55
    edge_zone = np.clip((1.0 - a) * 2.0, 0, 1)
    a = a * bottom
    a = np.where(core, a, a * (1.0 - edge_zone * 0.55))
    am = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), "L")
    am = am.filter(ImageFilter.GaussianBlur(2.0))
    return np.array(am, dtype=np.float32) / 255.0


def harmonize_colors(rgb: np.ndarray, mask: np.ndarray) -> np.ndarray:
    out = rgb.astype(np.float32)
    edge = np.clip((1.0 - mask) * 2.2, 0, 1)[..., None]
    return np.clip(out * (1.0 - edge * 0.18) + TINT * (edge * 0.18), 0, 255)


def paste_portrait(base: np.ndarray, bust: Image.Image, px: int, py: int) -> int:
    b = np.array(bust.convert("RGBA"), dtype=np.float32)
    bh, bw = int(b.shape[0]), int(b.shape[1])
    mask = blend_mask(b[..., 3] / 255.0)[..., None]
    src_rgb = harmonize_colors(b[..., :3], mask[..., 0])

    canvas_h, canvas_w = base.shape[0], base.shape[1]
    y0, y1 = max(0, py), min(canvas_h, py + bh)
    x0, x1 = max(0, px), min(canvas_w, px + bw)
    sy0, sy1 = y0 - py, y1 - py
    sx0, sx1 = x0 - px, x1 - px

    dst = base[y0:y1, x0:x1]
    sa = mask[sy0:sy1, sx0:sx1]
    da = dst[..., 3:4] / 255.0
    out_a = sa + da * (1.0 - sa)
    out_rgb = (src_rgb[sy0:sy1, sx0:sx1] * sa + dst[..., :3] * da * (1.0 - sa)) / np.maximum(
        out_a, 1e-6
    )
    dst[..., :3] = out_rgb
    dst[..., 3:4] = out_a * 255.0
    base[y0:y1, x0:x1] = dst
    return x1


def draw_lines(base: np.ndarray, text_x: int, bar_top: int) -> None:
    overlay = Image.new("RGBA", (base.shape[1], base.shape[0]), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    y1, y2 = bar_top + 112, bar_top + 128
    for y, op in ((y1, 70), (y2, 30)):
        d.line((text_x, y, W - 40, y), fill=(255, 255, 255, op), width=1)
    o = np.array(overlay, dtype=np.float32)
    a = o[..., 3:4] / 255.0
    base[..., :3] = o[..., :3] * a + base[..., :3] * (1.0 - a)


def build() -> Image.Image:
    canvas_h = H_BAR + OVERFLOW_TOP
    base = make_gradient_bar(H_BAR, y_offset=OVERFLOW_TOP)
    bust = crop_bust(Image.open(SPRITE))
    px = 4
    py = canvas_h - bust.size[1]
    text_x = paste_portrait(base, bust, px, py) + 18
    draw_lines(base, text_x, bar_top=OVERFLOW_TOP)
    return Image.fromarray(base.astype(np.uint8), "RGBA")


def main() -> None:
    img = build()
    img.save(OUT, "PNG")
    print(OUT, img.size, "bar_top_y", OVERFLOW_TOP)


if __name__ == "__main__":
    main()
