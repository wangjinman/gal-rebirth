#!/usr/bin/env python3
"""Build all UI_DS_* assets. Sizes: UI/UI_SPEC.md (1920x360 bar, 780x76 choice)."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# --- Tokens (edit here; keep in sync with UI_SPEC.md) ---
W = 1920
BAR_H = 360
CHOICE_W, CHOICE_H = 780, 76
NAMEPLATE_W, NAMEPLATE_H = 320, 44

# Light theme v1.2 — 更高、更透、顶缘渐隐
BAR_RGB = (252, 250, 246)
BAR_A_DIALOGUE = 0.62
BAR_A_NARRATION = 0.50

ACCENT = (201, 123, 53)
ACCENT_HOVER = (232, 148, 74)
ACCENT_FILL = (255, 210, 160, 140)  # ~55% of 255

BORDER_SUBTLE = (50, 60, 80, 26)
SHADOW_RGBA = (40, 50, 70, 20)

RADIUS_BAR = 0  # full-width bar, square top
RADIUS_CHOICE = 10
RADIUS_NAME = 8

OUT = Path(r"J:\项目\GAL\美术资源初稿\UI")
ARCHIVE = OUT / "_archive_UI02"


def bar_gradient(height: int, alpha: float, left_weight: bool) -> Image.Image:
    """Top nearly transparent → bottom denser; soft color shift."""
    arr = np.zeros((height, W, 4), dtype=np.float32)
    for y in range(height):
        t = y / max(height - 1, 1)
        # strong vertical fade: top ~6% peak alpha, bottom full (readable text zone)
        fade = t**1.35
        base_a = alpha * (0.06 + 0.94 * fade)
        for x in range(W):
            lw = 1.0
            if left_weight:
                lw = 0.92 + 0.08 * (1.0 - min(1.0, x / (W * 0.40)))
            # warm → slightly cooler gray toward bottom
            r = BAR_RGB[0] - int(12 * t)
            g = BAR_RGB[1] - int(10 * t)
            b = BAR_RGB[2] - int(8 * t)
            a = min(0.88, base_a * lw)
            arr[y, x, :3] = (r, g, b)
            arr[y, x, 3] = a * 255
    img = Image.fromarray(arr.astype(np.uint8), "RGBA")
    # soften top edge into scene (extra blur band)
    top = img.crop((0, 0, W, min(48, height // 3)))
    top = top.filter(ImageFilter.GaussianBlur(4))
    img.paste(top, (0, 0))
    draw = ImageDraw.Draw(img)
    # top hairline only (no heavy border on top)
    for i, a in enumerate([80, 40, 15]):
        draw.line([(0, i), (W, i)], fill=(255, 255, 255, a), width=1)
    draw.line([(0, height - 1), (W, height - 1)], fill=SHADOW_RGBA, width=1)
    return img


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle(
        (0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255
    )
    return m


def choice_button(state: str) -> Image.Image:
    pad = 3
    img = Image.new("RGBA", (CHOICE_W, CHOICE_H), (0, 0, 0, 0))
    mask = rounded_mask((CHOICE_W, CHOICE_H), RADIUS_CHOICE)

    # base glass fill
    base = Image.new("RGBA", (CHOICE_W, CHOICE_H), (0, 0, 0, 0))
    arr = np.zeros((CHOICE_H, CHOICE_W, 4), dtype=np.uint8)
    for y in range(CHOICE_H):
        t = y / max(CHOICE_H - 1, 1)
        a = int(200 + (1 - t) * 40)
        for x in range(CHOICE_W):
            r = BAR_RGB[0] - int(6 * t)
            g = BAR_RGB[1] - int(6 * t)
            b = BAR_RGB[2] - int(4 * t)
            arr[y, x] = (r, g, b, a)
    base = Image.fromarray(arr, "RGBA")
    base.putalpha(mask)

    draw = ImageDraw.Draw(base)

    if state == "normal":
        draw.rounded_rectangle(
            (pad, pad, CHOICE_W - pad - 1, CHOICE_H - pad - 1),
            radius=RADIUS_CHOICE,
            outline=BORDER_SUBTLE,
            width=1,
        )
        draw.line(
            [(pad + 24, pad + 2), (CHOICE_W - pad - 24, pad + 2)],
            fill=(255, 255, 255, 120),
            width=1,
        )
    elif state == "hover":
        glow = Image.new("RGBA", (CHOICE_W, CHOICE_H), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.rounded_rectangle(
            (pad - 3, pad - 3, CHOICE_W - pad + 2, CHOICE_H - pad + 2),
            radius=RADIUS_CHOICE + 4,
            outline=(*ACCENT_HOVER, 100),
            width=8,
        )
        glow = glow.filter(ImageFilter.GaussianBlur(7))
        base = Image.alpha_composite(glow, base)
        draw = ImageDraw.Draw(base)
        draw.rounded_rectangle(
            (pad, pad, CHOICE_W - pad - 1, CHOICE_H - pad - 1),
            radius=RADIUS_CHOICE,
            outline=(*ACCENT_HOVER, 255),
            width=2,
        )
    elif state == "selected":
        sel = Image.new("RGBA", (CHOICE_W, CHOICE_H), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(sel)
        sdraw.rounded_rectangle(
            (pad, pad, CHOICE_W - pad - 1, CHOICE_H - pad - 1),
            radius=RADIUS_CHOICE,
            fill=ACCENT_FILL,
        )
        sel.putalpha(mask)
        base = Image.alpha_composite(base, sel)
        draw = ImageDraw.Draw(base)
        draw.rounded_rectangle(
            (pad, pad, CHOICE_W - pad - 1, CHOICE_H - pad - 1),
            radius=RADIUS_CHOICE,
            outline=(*ACCENT, 240),
            width=2,
        )

    img.paste(base, (0, 0), mask)
    return img


def nameplate() -> Image.Image:
    nw, nh = NAMEPLATE_W, NAMEPLATE_H
    img = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
    mask = rounded_mask((nw, nh), RADIUS_NAME)
    fill = Image.new("RGBA", (nw, nh), (*BAR_RGB, 230))
    fill.putalpha(mask)
    draw = ImageDraw.Draw(fill)
    draw.rounded_rectangle(
        (0, 0, nw - 1, nh - 1),
        radius=RADIUS_NAME,
        outline=(*ACCENT, 180),
        width=1,
    )
    # left accent bar
    draw.rectangle((0, 8, 4, nh - 8), fill=(*ACCENT, 255))
    return fill


def archive_old() -> None:
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    patterns = ("UI_02_", "UI_choice_", "UI_01_")
    for p in OUT.glob("*.png"):
        if any(p.name.startswith(x) for x in patterns):
            dest = ARCHIVE / p.name
            if not dest.exists():
                import shutil
                shutil.copy2(p, dest)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    archive_old()

    bar_gradient(BAR_H, BAR_A_DIALOGUE, left_weight=True).save(
        OUT / "UI_DS_bar_dialogue.png", "PNG"
    )
    bar_gradient(BAR_H, BAR_A_NARRATION, left_weight=False).save(
        OUT / "UI_DS_bar_narration.png", "PNG"
    )
    nameplate().save(OUT / "UI_DS_nameplate.png", "PNG")

    for st in ("normal", "hover", "selected"):
        choice_button(st).save(OUT / f"UI_DS_choice_{st}.png", "PNG")

    print("UI Design System v1 built ->", OUT)
    for f in sorted(OUT.glob("UI_DS_*.png")):
        print(" ", f.name, f.stat().st_size)


if __name__ == "__main__":
    main()
