#!/usr/bin/env python3
"""UI_02 choice buttons — normal / hover / selected (800x90 RGBA).

Spec: ../UI_CHOICE_BUTTON_SPEC.md
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 800, 90
OUT_DIR = Path(r"J:\项目\GAL\美术资源初稿\UI")

TINT = (32, 42, 72)
ORANGE = (255, 148, 72)
ORANGE_SOFT = (255, 190, 130)
RADIUS = 14
PAD = 4


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return m


def gradient_fill() -> Image.Image:
    arr = np.zeros((H, W, 4), dtype=np.uint8)
    for y in range(H):
        t = y / max(H - 1, 1)
        a = int(175 + (1 - t) * 45)
        for x in range(W):
            lx = 0.92 + 0.08 * (x / max(W - 1, 1))
            arr[y, x] = (
                int(TINT[0] * lx),
                int(TINT[1] * lx),
                int(TINT[2] * lx),
                a,
            )
    return Image.fromarray(arr, "RGBA")


def draw_button(state: str) -> Image.Image:
    mask = rounded_mask((W, H), RADIUS)
    base = gradient_fill()
    base.putalpha(Image.new("L", (W, H), 0))
    base.putalpha(mask)
    draw = ImageDraw.Draw(base)

    if state == "normal":
        draw.rounded_rectangle(
            (PAD, PAD, W - PAD - 1, H - PAD - 1),
            radius=RADIUS,
            outline=(255, 255, 255, 70),
            width=1,
        )
        draw.line([(PAD + 18, PAD + 3), (W - PAD - 18, PAD + 3)], fill=(255, 255, 255, 35), width=1)
    elif state == "hover":
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.rounded_rectangle(
            (PAD - 4, PAD - 4, W - PAD + 3, H - PAD + 3),
            radius=RADIUS + 6,
            outline=(*ORANGE, 120),
            width=10,
        )
        glow = glow.filter(ImageFilter.GaussianBlur(8))
        layer = gradient_fill()
        layer.putalpha(mask)
        base = Image.alpha_composite(glow, layer)
        draw = ImageDraw.Draw(base)
        draw.rounded_rectangle(
            (PAD, PAD, W - PAD - 1, H - PAD - 1),
            radius=RADIUS,
            outline=(*ORANGE, 255),
            width=3,
        )
    elif state == "selected":
        sel = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(sel)
        sdraw.rounded_rectangle(
            (PAD, PAD, W - PAD - 1, H - PAD - 1),
            radius=RADIUS,
            fill=(*ORANGE_SOFT, 200),
        )
        sel.putalpha(mask)
        tint = gradient_fill()
        tint.putalpha(mask)
        base = Image.alpha_composite(tint, sel)
        draw = ImageDraw.Draw(base)
        draw.rounded_rectangle(
            (PAD, PAD, W - PAD - 1, H - PAD - 1),
            radius=RADIUS,
            outline=(*ORANGE, 240),
            width=2,
        )

    return base


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for state in ("normal", "hover", "selected"):
        path = OUT_DIR / f"UI_choice_{state}.png"
        draw_button(state).save(path, "PNG")
        print("saved", path, path.stat().st_size)


if __name__ == "__main__":
    main()
