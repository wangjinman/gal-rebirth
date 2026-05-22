#!/usr/bin/env python3
"""Narration bar comparison: v2_left_weight / v2_center.

See DIALOGUE_UI_MINIMAL_SPEC.md §8.1
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

W = 1920
H_BAR = 350
OVERFLOW_TOP = 90
TINT = np.array([32, 42, 72], dtype=np.float32)

OUT_DIR = Path(r"J:\项目\GAL\美术资源初稿\UI")
TEXT_COL_LEFT = 420
MARGIN_R = 48
CENTER_COL_W = int(W * 0.62)


def make_gradient_left_weight(height: int, y_offset: int) -> np.ndarray:
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


def make_gradient_center_calm(height: int, y_offset: int) -> np.ndarray:
    arr = np.zeros((y_offset + height, W, 4), dtype=np.float32)
    for yi in range(height):
        y = y_offset + yi
        t = yi / max(height - 1, 1)
        base_a = min(0.76, t**0.82 * 0.58 + 0.05)
        for x in range(W):
            cx = abs(x - W * 0.5) / (W * 0.5)
            side = min(1.0, cx**1.1 * 0.05)
            mid = max(0.0, 1.0 - cx * 1.4) * 0.03
            a = min(0.80, base_a + side - mid)
            arr[y, x, :3] = TINT
            arr[y, x, 3] = a * 255
    return arr


def composite_overlay(base: np.ndarray, overlay: Image.Image) -> None:
    o = np.array(overlay, dtype=np.float32)
    a = o[..., 3:4] / 255.0
    base[..., :3] = o[..., :3] * a + base[..., :3] * (1.0 - a)


def build_left_weight() -> Image.Image:
    bar_top = OVERFLOW_TOP
    base = make_gradient_left_weight(H_BAR, y_offset=bar_top)
    overlay = Image.new("RGBA", (W, H_BAR + OVERFLOW_TOP), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    x_div = TEXT_COL_LEFT - 20
    d.line((x_div, bar_top + 72, x_div, bar_top + H_BAR - 8), fill=(255, 255, 255, 38), width=1)
    for y, op in ((bar_top + 112, 70), (bar_top + 128, 30)):
        d.line((TEXT_COL_LEFT, y, W - MARGIN_R, y), fill=(255, 255, 255, op), width=1)
    composite_overlay(base, overlay)
    return Image.fromarray(base.astype(np.uint8), "RGBA")


def build_center() -> Image.Image:
    bar_top = OVERFLOW_TOP
    base = make_gradient_center_calm(H_BAR, y_offset=bar_top)
    overlay = Image.new("RGBA", (W, H_BAR + OVERFLOW_TOP), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    cx0 = (W - CENTER_COL_W) // 2
    cx1 = cx0 + CENTER_COL_W
    d.line((cx0, bar_top + 80, cx0, bar_top + H_BAR - 12), fill=(255, 255, 255, 22), width=1)
    d.line((cx1, bar_top + 80, cx1, bar_top + H_BAR - 12), fill=(255, 255, 255, 22), width=1)
    for y, op in ((bar_top + 112, 70), (bar_top + 128, 30)):
        d.line((cx0, y, cx1, y), fill=(255, 255, 255, op), width=1)
    composite_overlay(base, overlay)
    return Image.fromarray(base.astype(np.uint8), "RGBA")


def main() -> None:
    build_left_weight().save(OUT_DIR / "UI_02_narration_minimal_v2_left_weight.png", "PNG")
    build_center().save(OUT_DIR / "UI_02_narration_minimal_v2_center.png", "PNG")
    print("done", OUT_DIR)


if __name__ == "__main__":
    main()
