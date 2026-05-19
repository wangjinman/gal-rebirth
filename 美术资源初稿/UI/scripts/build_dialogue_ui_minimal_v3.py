#!/usr/bin/env python3
"""Minimal dialogue UI v3 — portrait fully blended into gradient bar."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 1920, 350
SPRITE = Path(r"J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-transparent-v1-feather.png")
OUT = Path(r"J:\项目\GAL\美术资源初稿\UI\UI_02_dialogue_minimal_wantang_v3.png")

# bar tint (matches gradient)
TINT = np.array([12, 18, 38], dtype=np.float32)


def make_gradient_bar() -> np.ndarray:
    """RGBA float32, full canvas — darker behind left portrait zone."""
    arr = np.zeros((H, W, 4), dtype=np.float32)
    for y in range(H):
        t = y / max(H - 1, 1)
        base_a = min(1.0, t**0.75 * 0.88 + 0.06)
        for x in range(W):
            # extra density under portrait / left third
            lx = 1.0 - min(1.0, x / (W * 0.42))
            boost = (1.0 - t) * 0.12 * lx
            a = min(1.0, base_a + boost)
            arr[y, x, :3] = TINT
            arr[y, x, 3] = a * 255
    return arr


def crop_bust(sprite: Image.Image) -> Image.Image:
    sprite = sprite.convert("RGBA")
    a = np.array(sprite.split()[3])
    ys, xs = np.where(a > 40)
    x0, x1 = xs.min(), xs.max()
    y0, y1 = ys.min(), ys.max()
    body_h = y1 - y0
    y1_bust = y0 + int(body_h * 0.62)
    bust = sprite.crop((x0, y0, x1, y1_bust))
    target_h = int(H * 0.94)
    bw, bh = bust.size
    scale = target_h / bh
    return bust.resize((max(1, int(bw * scale)), target_h), Image.Resampling.LANCZOS)


def blend_mask(alpha: np.ndarray) -> np.ndarray:
    """Soft natural mask: long bottom fade, feathered edges only."""
    h, w = alpha.shape
    a = np.clip(alpha.astype(np.float32), 0, 1)
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)

    # bottom dissolve into bar (skirt/feet)
    bottom_start = h * 0.72
    bottom = np.clip((h - yy) / max(h - bottom_start, 1), 0, 1)
    bottom = bottom**1.1

    # soft outer silhouette only (keep face/body solid)
    core = a > 0.55
    edge_zone = np.clip(1.0 - a, 0, 1) * 2.2
    edge_zone = np.clip(edge_zone, 0, 1)

    a = a * bottom
    a = np.where(core, a, a * (1.0 - edge_zone * 0.65))

    am = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), "L")
    am = am.filter(ImageFilter.GaussianBlur(2.2))
    return np.array(am, dtype=np.float32) / 255.0


def harmonize_colors(rgb: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """Tint only outer fringe toward bar color — keep face/clothes readable."""
    out = rgb.astype(np.float32)
    edge = np.clip((1.0 - mask) * 2.5, 0, 1)[..., None]
    out = out * (1.0 - edge * 0.28) + TINT * (edge * 0.28)
    return np.clip(out, 0, 255)


def composite_portrait(base: np.ndarray, bust: Image.Image) -> np.ndarray:
    b = np.array(bust.convert("RGBA"), dtype=np.float32)
    bh, bw = b.shape[0], b.shape[1]
    px, py = max(0, 8), H - bh

    mask = blend_mask(b[..., 3] / 255.0)[..., None]
    src_rgb = harmonize_colors(b[..., :3], mask[..., 0])

    dst = base[py : py + bh, px : px + bw]
    sa = mask
    da = dst[..., 3:4] / 255.0
    out_a = sa + da * (1.0 - sa)
    out_rgb = (src_rgb * sa + dst[..., :3] * da * (1.0 - sa)) / np.maximum(out_a, 1e-6)
    dst[..., :3] = out_rgb
    dst[..., 3:4] = out_a * 255.0
    base[py : py + bh, px : px + bw] = dst
    return base


def draw_subtle_lines(base: np.ndarray, text_x: int) -> None:
    """Very soft separators — not cutting the UI."""
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    y1, y2 = 112, 128
    for y, op in ((y1, 55), (y2, 22)):
        d.line((text_x, y, W - 40, y), fill=(255, 255, 255, op), width=1)
    o = np.array(overlay, dtype=np.float32)
    for y in range(H):
        for x in range(W):
            a = o[y, x, 3] / 255.0
            if a < 0.01:
                continue
            for c in range(3):
                base[y, x, c] = o[y, x, c] * a + base[y, x, c] * (1 - a)


def main() -> None:
    base = make_gradient_bar()
    sprite = Image.open(SPRITE)
    bust = crop_bust(sprite)
    base = composite_portrait(base, bust)
    text_x = 8 + bust.size[0] + 20
    draw_subtle_lines(base, text_x)
    out = Image.fromarray(base.astype(np.uint8), "RGBA")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    out.save(OUT, "PNG")
    print("saved", OUT, out.size)


if __name__ == "__main__":
    main()
