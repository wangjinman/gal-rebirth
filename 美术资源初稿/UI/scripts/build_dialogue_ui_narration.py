#!/usr/bin/env python3
"""UI_02 narration bar — no portrait, same canvas/anchor as dialogue posA.

Spec: ../DIALOGUE_UI_MINIMAL_SPEC.md (narration section)
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

W = 1920
H_BAR = 350
OVERFLOW_TOP = 90
TEXT_MARGIN_X = 48

OUT = Path(r"J:\项目\GAL\美术资源初稿\UI\UI_02_narration_minimal.png")

TINT = np.array([32, 42, 72], dtype=np.float32)


def make_gradient_bar_narration(height: int, y_offset: int) -> np.ndarray:
    """Even gradient across width (no left portrait boost)."""
    arr = np.zeros((y_offset + height, W, 4), dtype=np.float32)
    for yi in range(height):
        y = y_offset + yi
        t = yi / max(height - 1, 1)
        base_a = min(0.76, t**0.82 * 0.58 + 0.05)
        for x in range(W):
            # very mild vignette at sides, center slightly calmer for long prose
            cx = abs(x - W * 0.5) / (W * 0.5)
            side = min(1.0, cx**1.2 * 0.04)
            a = min(0.80, base_a + side)
            arr[y, x, :3] = TINT
            arr[y, x, 3] = a * 255
    return arr


def draw_lines(base: np.ndarray, bar_top: int) -> None:
    overlay = Image.new("RGBA", (base.shape[1], base.shape[0]), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    y1, y2 = bar_top + 112, bar_top + 128
    for y, op in ((y1, 70), (y2, 30)):
        d.line((TEXT_MARGIN_X, y, W - TEXT_MARGIN_X, y), fill=(255, 255, 255, op), width=1)
    o = np.array(overlay, dtype=np.float32)
    a = o[..., 3:4] / 255.0
    base[..., :3] = o[..., :3] * a + base[..., :3] * (1.0 - a)


def build() -> Image.Image:
    canvas_h = H_BAR + OVERFLOW_TOP
    base = make_gradient_bar_narration(H_BAR, y_offset=OVERFLOW_TOP)
    draw_lines(base, bar_top=OVERFLOW_TOP)
    return Image.fromarray(base.astype(np.uint8), "RGBA")


def main() -> None:
    img = build()
    img.save(OUT, "PNG")
    print(OUT, img.size)


if __name__ == "__main__":
    main()
