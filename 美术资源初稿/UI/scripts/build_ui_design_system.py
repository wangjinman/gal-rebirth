#!/usr/bin/env python3
"""Build all UI_DS_* assets. Sizes: UI/UI_SPEC.md (1920x360 bar, 780x76 choice)."""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# --- Tokens (edit here; keep in sync with UI_SPEC.md) ---
W = 1920
BAR_H = 360
CHOICE_W, CHOICE_H = 780, 76
NAMEPLATE_W, NAMEPLATE_H = 320, 44
QUICK_BAR_H = 56
QUICK_ICON = 48
VOICE_ICON = 40

# Light theme v1.2 — 更高、更透、顶缘渐隐
TEXT_ICON = (58, 66, 88, 255)
TEXT_ICON_HOVER = (184, 106, 40, 255)
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


def quick_bar() -> Image.Image:
    """Top quick menu strip — 1920x56, lighter than dialogue bar."""
    arr = np.zeros((QUICK_BAR_H, W, 4), dtype=np.float32)
    for y in range(QUICK_BAR_H):
        t = y / max(QUICK_BAR_H - 1, 1)
        fade = t**1.1
        base_a = 0.38 * (0.15 + 0.85 * fade)
        for x in range(W):
            r, g, b = BAR_RGB
            arr[y, x, :3] = (r - 8, g - 8, b - 6)
            arr[y, x, 3] = base_a * 255
    img = Image.fromarray(arr.astype(np.uint8), "RGBA")
    draw = ImageDraw.Draw(img)
    draw.line([(0, QUICK_BAR_H - 1), (W, QUICK_BAR_H - 1)], fill=SHADOW_RGBA, width=1)
    draw.line([(0, 0), (W, 0)], fill=(255, 255, 255, 50), width=1)
    return img


def _icon_tile(size: int, hover: bool) -> Image.Image:
    pad = 4
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    mask = rounded_mask((size, size), 8)
    fill_a = 210 if hover else 185
    base = Image.new("RGBA", (size, size), (*BAR_RGB, fill_a))
    base.putalpha(mask)
    draw = ImageDraw.Draw(base)
    outline = ACCENT_HOVER if hover else BORDER_SUBTLE[:3] + (200,)
    width = 2 if hover else 1
    draw.rounded_rectangle(
        (pad, pad, size - pad - 1, size - pad - 1),
        radius=8,
        outline=outline,
        width=width,
    )
    if hover:
        glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.rounded_rectangle(
            (pad - 2, pad - 2, size - pad + 1, size - pad + 1),
            radius=10,
            outline=(*ACCENT_HOVER, 80),
            width=6,
        )
        glow = glow.filter(ImageFilter.GaussianBlur(5))
        base = Image.alpha_composite(glow, base)
    return base


def _draw_glyph(draw: ImageDraw.ImageDraw, name: str, ox: int, oy: int, color: tuple, scale: float = 1.0) -> None:
    s = scale
    cx, cy = ox, oy

    def line(pts, w=2):
        draw.line(
            [(cx + int(x * s), cy + int(y * s)) for x, y in pts],
            fill=color,
            width=max(1, int(w * s)),
        )

    def poly(pts, fill=None):
        draw.polygon(
            [(cx + int(x * s), cy + int(y * s)) for x, y in pts],
            fill=fill or color,
            outline=color,
        )

    if name == "auto":
        poly([(-6, -8), (10, 0), (-6, 8)])
        draw.arc((cx - 14, cy - 12, cx + 6, cy + 12), 200, 340, fill=color, width=2)
    elif name == "skip":
        poly([(-10, -9), (0, 0), (-10, 9)])
        poly([(-2, -9), (8, 0), (-2, 9)])
    elif name == "hide":
        draw.ellipse((cx - 12, cy - 6, cx + 12, cy + 6), outline=color, width=2)
        draw.ellipse((cx - 4, cy - 2, cx + 4, cy + 2), fill=color)
        line([(-14, 10), (14, -10)], 2)
    elif name == "history":
        draw.ellipse((cx - 10, cy - 10, cx + 10, cy + 10), outline=color, width=2)
        line([(0, 0), (0, -6)], 2)
        line([(0, 0), (5, 3)], 2)
    elif name == "save":
        draw.rounded_rectangle((cx - 10, cy - 8, cx + 10, cy + 10), radius=2, outline=color, width=2)
        draw.rectangle((cx - 6, cy - 12, cx + 6, cy - 6), fill=color)
        line([(-6, 2), (6, 2)], 1)
    elif name == "load":
        draw.rounded_rectangle((cx - 10, cy - 6, cx + 10, cy + 10), radius=2, outline=color, width=2)
        poly([(-4, -4), (0, -10), (4, -4)])
    elif name == "settings":
        for i in range(8):
            ang = i * 45
            rad = math.radians(ang)
            x1 = int(9 * math.cos(rad))
            y1 = int(9 * math.sin(rad))
            draw.ellipse((cx + x1 - 2, cy + y1 - 2, cx + x1 + 2, cy + y1 + 2), fill=color)
        draw.ellipse((cx - 5, cy - 5, cx + 5, cy + 5), outline=color, width=2)
    elif name == "exit":
        line([(-8, -8), (8, 8)], 2)
        line([(-8, 8), (8, -8)], 2)
        draw.arc((cx - 14, cy - 14, cx + 14, cy + 14), 30, 150, fill=color, width=2)
    elif name == "voice":
        poly([(-6, -6), (-6, 6), (2, 6), (8, 10), (8, -10), (2, -6)])
        line([(10, -4), (14, -8)], 2)
        line([(10, 4), (14, 8)], 2)


def quick_icon(name: str, hover: bool) -> Image.Image:
    size = QUICK_ICON
    base = _icon_tile(size, hover)
    draw = ImageDraw.Draw(base)
    color = TEXT_ICON_HOVER if hover else TEXT_ICON
    _draw_glyph(draw, name, size // 2, size // 2, color, scale=1.0)
    return base


def say_voice_icon(hover: bool) -> Image.Image:
    size = VOICE_ICON
    base = _icon_tile(size, hover)
    draw = ImageDraw.Draw(base)
    color = TEXT_ICON_HOVER if hover else TEXT_ICON
    _draw_glyph(draw, "voice", size // 2, size // 2, color, scale=0.85)
    return base


def build_say_quick() -> list[str]:
    """Generate all say-module quick_menu + voice assets."""
    written: list[str] = []
    quick_bar().save(OUT / "UI_DS_quick_bar.png", "PNG")
    written.append("UI_DS_quick_bar.png")

    icons = (
        "auto",
        "skip",
        "hide",
        "history",
        "save",
        "load",
        "settings",
        "exit",
    )
    for name in icons:
        for state in ("default", "hover"):
            img = quick_icon(name, hover=(state == "hover"))
            fname = f"UI_DS_quick_{name}_{state}.png"
            img.save(OUT / fname, "PNG")
            written.append(fname)

    for state in ("default", "hover"):
        img = say_voice_icon(hover=(state == "hover"))
        fname = f"UI_DS_say_voice_{state}.png"
        img.save(OUT / fname, "PNG")
        written.append(fname)

    return written


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

    say_files = build_say_quick()
    print("Say module (quick_menu + voice):", len(say_files), "files")

    print("UI Design System v1 built ->", OUT)
    for f in sorted(OUT.glob("UI_DS_*.png")):
        print(" ", f.name, f.stat().st_size)


if __name__ == "__main__":
    main()
