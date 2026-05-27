#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二次元 / 卡通风 say 全套 UI（独立目录，不覆盖 UI_DS_* 极简版）。
输出: UI/anime_style/ 或 UI/anime_style_blue/
用法: python build_ui_anime_say.py [pink|blue]
规格: 与 UI_SPEC.md 相同尺寸。
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# --- 尺寸（与 UI_SPEC 一致）---
W = 1920
BAR_H = 280  # 对话框高度（原 360；仅缩底栏试验）
LEFT_SLOT_W = 400  # 保留常量，当前底栏不启用左槽加厚
CHOICE_W, CHOICE_H = 780, 76
NAMEPLATE_W, NAMEPLATE_H = 12, 44  # 左侧强调色条
QUICK_BAR_H = 56
QUICK_ICON = 48
VOICE_ICON = 40

UI_ROOT = Path(r"J:\项目\GAL\美术资源初稿\UI")
UI_SUPERSAMPLE = 3  # nameplate 超采样
CHOICE_SUPERSAMPLE = 4  # 选项：更高采样 + 软 mask，圆弧更顺滑

# 主题色（由 apply_theme 写入）
BAR_TOP = (255, 255, 255)
BAR_BOTTOM = (255, 178, 200)
BAR_NVL_TOP = (255, 253, 255)
BAR_NVL_BOTTOM = (255, 205, 228)
INNER_CREAM = (255, 247, 252)
OUTLINE = (255, 158, 195, 255)
ACCENT = (255, 112, 168)
ACCENT_HOVER = (255, 178, 200)
ACCENT_DEEP = (248, 58, 125)
GLYPH = (205, 118, 158, 255)
GLYPH_HOVER = (255, 88, 148, 255)
GLYPH_OUTLINE = (248, 148, 188, 255)
CHOICE_GRAD_BASE = (255, 252, 254)
CHOICE_GRAD_DROP = (4, 18, 12)
ICON_FILL = (255, 252, 254)
ICON_FILL_HOVER = (255, 188, 212)
OUT = UI_ROOT / "anime_style"

BAR_A_DIALOGUE = 0.80
BAR_A_NARRATION = 0.67
# 无色对话框：冷雾 RGB + alpha；顶缘高光减轻黑屏发闷（与彩景观感拉近）
BAR_COLORLESS_TINT = (234, 240, 248)
BAR_COLORLESS_RGB_LIFT = 0.28
BAR_COLORLESS_A_DIALOGUE = 0.64
BAR_COLORLESS_A_NVL = 0.48
BAR_COLORLESS_SHEEN_A = 0.14
BAR_COLORLESS_RIM_A = 26
# 无色选项 · 浮岛 + 上亮下淡（粉套 choice）
CHOICE_ISLAND_W_FRAC = 0.80
CHOICE_ISLAND_H_FRAC = 0.62
CHOICE_ISLAND_RGB = (250, 252, 255)
CHOICE_ISLAND_A_TOP = {"normal": 0.28, "hover": 0.34, "selected": 0.31}
CHOICE_ISLAND_A_BOTTOM = {"normal": 0.07, "hover": 0.11, "selected": 0.10}
CHOICE_ISLAND_EDGE_A = {"normal": 0.50, "hover": 0.60, "selected": 0.54}
CHOICE_ISLAND_TOP_CAP = 0.08
CHOICE_ISLAND_GLOW_A = 48
CHOICE_ISLAND_RIM_BOOST = 1.12  # 顶缘折射边略加强（替代矢量顶弧，避免缺色缝）
RADIUS_BAR_TOP = 28
RADIUS_CHOICE = 22
RADIUS_NAME = 16

# 选项钮：透叠立绘；亮边+轻雾白，黑屏/彩景都能认（见 CHOICE_LIFT_*）
CHOICE_INNER_A = {"normal": 0.20, "hover": 0.30, "selected": 0.38}
CHOICE_RING_A = {"normal": 155, "hover": 190, "selected": 205}
CHOICE_TINT_A = {"hover": 55, "selected": 72}
CHOICE_GLOW_A = 80
CHOICE_LIFT_RGB = (255, 255, 255)  # 内底混一点雾白，避免纯黑底发闷
CHOICE_LIFT_MIX = 0.14
CHOICE_RIM_WHITE_A = 52  # 内沿细高光，黑屏轮廓
# 粉套 say 屏统一无色玻璃（含快捷栏/图标/姓名条，避免灰雾+粉钮违和）
QUICK_BAR_COLORLESS_A = 0.38
NAMEPLATE_COLORLESS_A = 175
ICON_COLORLESS_FILL = (255, 255, 255, 185)
ICON_COLORLESS_FILL_H = (255, 255, 255, 235)
ICON_COLORLESS_GLYPH = (95, 100, 112, 255)
ICON_COLORLESS_GLYPH_H = (60, 65, 78, 255)
ICON_COLORLESS_RING_A = 90
ICON_COLORLESS_GLOW_A = 40

# 官方双色定调 — 见 UI_THEME_COLORS.md（theme-lock-20260519）。勿擅自增删主题或改 Token。
# 粉套专用：仅底栏 + 选项用中性色（通篇叠 BG/立绘），其余仍樱粉
BAR_CHOICE_NEUTRAL: dict = {
    "BAR_TOP": (255, 255, 255),
    "BAR_BOTTOM": (228, 234, 244),
    "BAR_NVL_TOP": (255, 255, 255),
    "BAR_NVL_BOTTOM": (218, 226, 238),
    "INNER_CREAM": (248, 250, 253),
    "OUTLINE": (148, 168, 192, 255),
    "ACCENT": (88, 148, 210),
    "ACCENT_HOVER": (120, 178, 232),
    "ACCENT_DEEP": (62, 108, 168),
    "CHOICE_GRAD": ((252, 253, 255), (6, 10, 14)),
}

THEMES: dict[str, dict] = {
    "pink": {
        "dir": "anime_style",
        "BAR_TOP": (255, 255, 255),
        "BAR_BOTTOM": (255, 178, 200),
        "BAR_NVL_TOP": (255, 253, 255),
        "BAR_NVL_BOTTOM": (255, 205, 228),
        "INNER_CREAM": (255, 247, 252),
        "OUTLINE": (255, 158, 195, 255),
        "ACCENT": (255, 112, 168),
        "ACCENT_HOVER": (255, 178, 200),
        "ACCENT_DEEP": (248, 58, 125),
        "GLYPH": (205, 118, 158, 255),
        "GLYPH_HOVER": (255, 88, 148, 255),
        "GLYPH_OUTLINE": (248, 148, 188, 255),
        "CHOICE_GRAD": ((255, 252, 254), (4, 18, 12)),
        "ICON_FILL": (255, 252, 254),
        "ICON_FILL_HOVER": (255, 188, 212),
    },
    "blue": {
        "dir": "anime_style_blue",
        # 锚点：quick_exit_hover 外圈天蓝 (≈90,200,255)；默认态描边向其对齐
        "BAR_TOP": (255, 255, 255),
        "BAR_BOTTOM": (155, 215, 255),
        "BAR_NVL_TOP": (255, 254, 255),
        "BAR_NVL_BOTTOM": (195, 232, 255),
        "INNER_CREAM": (248, 252, 255),
        "OUTLINE": (90, 200, 255, 255),
        "ACCENT": (65, 185, 255),
        "ACCENT_HOVER": (115, 220, 255),
        "ACCENT_DEEP": (45, 150, 235),
        "GLYPH": (75, 165, 235, 255),
        "GLYPH_HOVER": (50, 190, 255, 255),
        "GLYPH_OUTLINE": (95, 190, 245, 255),
        "CHOICE_GRAD": ((248, 253, 255), (6, 16, 12)),
        "ICON_FILL": (248, 253, 255),
        "ICON_FILL_HOVER": (205, 235, 255),
    },
}


def apply_theme(name: str) -> None:
    global BAR_TOP, BAR_BOTTOM, BAR_NVL_TOP, BAR_NVL_BOTTOM, INNER_CREAM
    global OUTLINE, ACCENT, ACCENT_HOVER, ACCENT_DEEP
    global GLYPH, GLYPH_HOVER, GLYPH_OUTLINE
    global CHOICE_GRAD_BASE, CHOICE_GRAD_DROP, ICON_FILL, ICON_FILL_HOVER, OUT
    t = THEMES[name]
    BAR_TOP = t["BAR_TOP"]
    BAR_BOTTOM = t["BAR_BOTTOM"]
    BAR_NVL_TOP = t["BAR_NVL_TOP"]
    BAR_NVL_BOTTOM = t["BAR_NVL_BOTTOM"]
    INNER_CREAM = t["INNER_CREAM"]
    OUTLINE = t["OUTLINE"]
    ACCENT = t["ACCENT"]
    ACCENT_HOVER = t["ACCENT_HOVER"]
    ACCENT_DEEP = t["ACCENT_DEEP"]
    GLYPH = t["GLYPH"]
    GLYPH_HOVER = t["GLYPH_HOVER"]
    GLYPH_OUTLINE = t["GLYPH_OUTLINE"]
    CHOICE_GRAD_BASE = t["CHOICE_GRAD"][0]
    CHOICE_GRAD_DROP = t["CHOICE_GRAD"][1]
    ICON_FILL = t["ICON_FILL"]
    ICON_FILL_HOVER = t["ICON_FILL_HOVER"]
    OUT = UI_ROOT / t["dir"]


def apply_bar_choice_neutral() -> None:
    """仅覆盖底栏/选项绘制用到的 Token（快捷栏、图标、姓名条仍樱粉）。"""
    global BAR_TOP, BAR_BOTTOM, BAR_NVL_TOP, BAR_NVL_BOTTOM, INNER_CREAM
    global OUTLINE, ACCENT, ACCENT_HOVER, ACCENT_DEEP
    global CHOICE_GRAD_BASE, CHOICE_GRAD_DROP
    p = BAR_CHOICE_NEUTRAL
    BAR_TOP = p["BAR_TOP"]
    BAR_BOTTOM = p["BAR_BOTTOM"]
    BAR_NVL_TOP = p["BAR_NVL_TOP"]
    BAR_NVL_BOTTOM = p["BAR_NVL_BOTTOM"]
    INNER_CREAM = p["INNER_CREAM"]
    OUTLINE = p["OUTLINE"]
    ACCENT = p["ACCENT"]
    ACCENT_HOVER = p["ACCENT_HOVER"]
    ACCENT_DEEP = p["ACCENT_DEEP"]
    CHOICE_GRAD_BASE = p["CHOICE_GRAD"][0]
    CHOICE_GRAD_DROP = p["CHOICE_GRAD"][1]


def top_rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    """仅顶部圆角（选项等仍可用；底栏已改直角）。"""
    w, h = size
    r = min(radius, h // 2, w // 2)
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    if h > r:
        d.rectangle((0, r, w - 1, h - 1), fill=255)
    d.rounded_rectangle((0, 0, w - 1, min(h - 1, 2 * r + 2)), radius=r, fill=255)
    return m


def rect_bar_mask(size: tuple[int, int]) -> Image.Image:
    """底栏矩形 mask（顶边直角）。"""
    return Image.new("L", size, 255)


def _draw_bar_border_dialogue(
    draw: ImageDraw.ImageDraw, w: int, h: int, color: tuple, width: int
) -> None:
    """对话底栏：仅顶边横线，不画左右/底（避免贴屏缘与黑边叠缝）。"""
    ow = max(1, width)
    y = ow // 2
    draw.line([(0, y), (w - 1, y)], fill=color, width=ow)


def _draw_bar_border_rect(
    draw: ImageDraw.ImageDraw, w: int, h: int, color: tuple, width: int
) -> None:
    """四边直角描边（非对话底栏用）。"""
    ow = width
    inset = ow // 2 + 1
    draw.line(
        [(inset, h - inset - 1), (w - inset - 1, h - inset - 1)],
        fill=color,
        width=ow,
    )
    draw.line([(inset, inset), (inset, h - inset - 1)], fill=color, width=ow)
    draw.line([(w - inset - 1, inset), (w - inset - 1, h - inset - 1)], fill=color, width=ow)
    draw.line([(inset, inset), (w - inset - 1, inset)], fill=color, width=ow)


def _draw_bar_border_top_rounded(
    draw: ImageDraw.ImageDraw, w: int, h: int, radius: int, color: tuple, width: int
) -> None:
    """快捷栏等仍用顶圆角描边（对话底栏已改直角）。"""
    r = min(radius, h // 2, w // 2)
    ow = width
    inset = ow // 2 + 1
    draw.line(
        [(inset, h - inset - 1), (w - inset - 1, h - inset - 1)],
        fill=color,
        width=ow,
    )
    draw.line([(inset, r), (inset, h - inset - 1)], fill=color, width=ow)
    draw.line([(w - inset - 1, r), (w - inset - 1, h - inset - 1)], fill=color, width=ow)
    draw.line([(r, inset), (w - r - 1, inset)], fill=color, width=ow)
    draw.arc(
        (inset, inset, 2 * r - inset, 2 * r - inset),
        180,
        270,
        fill=color,
        width=ow,
    )
    draw.arc(
        (w - 2 * r + inset - 1, inset, w - inset - 1, 2 * r - inset),
        270,
        360,
        fill=color,
        width=ow,
    )


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle(
        (0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255
    )
    return m


def floating_island_mask(
    w: int,
    h: int,
    width_frac: float = CHOICE_ISLAND_W_FRAC,
    height_frac: float = CHOICE_ISLAND_H_FRAC,
) -> tuple[np.ndarray, tuple[int, int, int, int]]:
    """内缩浮岛 mask（药丸轮廓）+ 包围盒 (x0, y0, x1, y1)。"""
    iw = max(8, int(w * width_frac))
    ih = max(6, int(h * height_frac))
    x0 = (w - iw) // 2
    y0 = (h - ih) // 2
    x1 = x0 + iw - 1
    y1 = y0 + ih - 1
    r = max(2, ih // 2)
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((x0, y0, x1, y1), radius=r, fill=255)
    return np.array(m, dtype=np.float32) / 255.0, (x0, y0, x1, y1)


def soft_island_mask(w: int, h: int) -> np.ndarray:
    """终尺寸浮岛软边 mask（高分辨率绘制 → 轻模糊 → Lanczos 缩小）。"""
    s = CHOICE_SUPERSAMPLE
    big_m, _ = floating_island_mask(w * s, h * s)
    m = Image.fromarray((np.clip(big_m, 0, 1) * 255).astype(np.uint8), "L")
    m = m.filter(ImageFilter.GaussianBlur(max(1.0, 0.55 * s)))
    small = np.array(m.resize((w, h), Image.Resampling.LANCZOS), dtype=np.float32) / 255.0
    return np.clip(small, 0.0, 1.0)


def hard_rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    """硬边圆角 mask，避免顶缘抗锯齿造成窄条透明/缺色。"""
    w, h = size
    r = min(radius, w // 2, h // 2)
    yy, xx = np.mgrid[0:h, 0:w]
    body = (xx >= r) & (xx < w - r) & (yy >= r) & (yy < h - r)
    top = (yy < r) & (xx >= r) & (xx < w - r)
    bottom = (yy >= h - r) & (xx >= r) & (xx < w - r)
    left = (xx < r) & (yy >= r) & (yy < h - r)
    right = (xx >= w - r) & (yy >= r) & (yy < h - r)
    corners = np.zeros((h, w), dtype=bool)
    for cx, cy in ((r, r), (w - r - 1, r), (r, h - r - 1), (w - r - 1, h - r - 1)):
        corners |= (xx - cx) ** 2 + (yy - cy) ** 2 <= r**2
    inside = body | top | bottom | left | right | corners
    return Image.fromarray(np.where(inside, 255, 0).astype(np.uint8), mode="L")


def _sparkle(draw: ImageDraw.ImageDraw, x: int, y: int, r: int = 3) -> None:
    """仅用于大组件（底栏/选项）；小图标不用，避免色斑。"""
    for dx, dy, a in ((0, 0, 220), (-r, 0, 160), (r, 0, 160), (0, -r, 160), (0, r, 160)):
        draw.ellipse((x + dx - 2, y + dy - 2, x + dx + 2, y + dy + 2), fill=(*ACCENT[:3], a))


def _circle_alpha_mask(size: int, margin: int = 2) -> Image.Image:
    m = Image.new("L", (size, size), 0)
    ImageDraw.Draw(m).ellipse((margin, margin, size - margin - 1, size - margin - 1), fill=255)
    return m


def _apply_circle_clip(img: Image.Image, margin: int = 2) -> Image.Image:
    """裁掉圆外像素，消除描边/高光溢出的杂色块。"""
    w, h = img.size
    mask = np.array(_circle_alpha_mask(w, margin), dtype=np.float32) / 255.0
    a = np.array(img.split()[3], dtype=np.float32)
    a = (a * mask).astype(np.uint8)
    img = img.copy()
    img.putalpha(Image.fromarray(a))
    return img


def bar_anime(height: int, alpha: float, nvl: bool, left_weight: bool) -> Image.Image:
    top_c = BAR_NVL_TOP if nvl else BAR_TOP
    bot_c = BAR_NVL_BOTTOM if nvl else BAR_BOTTOM

    arr = np.zeros((height, W, 4), dtype=np.float32)
    for y in range(height):
        t = y / max(height - 1, 1)
        fade = t**1.35
        base_a = alpha * (0.06 + 0.94 * fade)
        for x in range(W):
            lw = 1.0
            if left_weight and not nvl:
                lw = 0.9 + 0.1 * (1.0 - min(1.0, x / (W * 0.38)))
            ri = int(top_c[0] + (bot_c[0] - top_c[0]) * t)
            gi = int(top_c[1] + (bot_c[1] - top_c[1]) * t)
            bi = int(top_c[2] + (bot_c[2] - top_c[2]) * t)
            a = min(0.92, base_a * lw)
            arr[y, x, :3] = (ri, gi, bi)
            arr[y, x, 3] = 255

    fill = Image.fromarray(arr.astype(np.uint8), "RGBA")
    shape = rect_bar_mask((W, height))
    img = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    img.paste(fill, (0, 0), shape)

    # 渐变透明度写在独立 alpha 通道，避免与 mask 相乘产生顶缘灰线
    grad_a = np.zeros((height, W), dtype=np.uint8)
    for y in range(height):
        t = y / max(height - 1, 1)
        fade = t**1.35
        base_a = alpha * (0.06 + 0.94 * fade)
        grad_a[y, :] = (np.minimum(255, base_a * 255)).astype(np.uint8)
    shape_a = np.array(shape, dtype=np.float32) / 255.0
    final_a = (grad_a.astype(np.float32) * shape_a).astype(np.uint8)
    img.putalpha(Image.fromarray(final_a))

    draw = ImageDraw.Draw(img)
    _draw_bar_border_dialogue(draw, W, height, OUTLINE, 2)
    return img


def bar_colorless(
    height: int, alpha: float, nvl: bool, *, left_slot: bool = False
) -> Image.Image:
    """无色对话框：冷雾玻璃 + 顶缘高光；正文区略实，黑屏/彩景观感更接近。"""
    arr = np.zeros((height, W, 4), dtype=np.float32)
    tint = np.array(BAR_COLORLESS_TINT, dtype=np.float32)
    rgb_lift = BAR_COLORLESS_RGB_LIFT
    peak = min(0.78, alpha * (0.92 if nvl else 1.0))
    slot_w = LEFT_SLOT_W if left_slot else 0

    for y in range(height):
        t = y / max(height - 1, 1)
        bell = math.sin(math.pi * t) ** 1.08
        text_zone = max(0.0, (t - 0.32) / 0.68) ** 0.82
        base_a = peak * (0.12 + 0.46 * bell + 0.30 * t + 0.18 * text_zone)
        base_a = min(0.78, base_a)
        mix = rgb_lift * (0.40 + 0.60 * (base_a / 0.78))
        rgb = 255.0 * (1.0 - mix) + tint * mix
        for x in range(W):
            a = base_a
            if slot_w and not nvl and x < slot_w:
                slot_t = max(0.0, (t - 0.25) / 0.75) ** 0.9
                edge = 1.0 - min(1.0, x / max(slot_w - 1, 1)) ** 1.6
                a = min(0.82, base_a + 0.06 * slot_t * (0.35 + 0.65 * edge))
            arr[y, x, 0] = rgb[0]
            arr[y, x, 1] = rgb[1]
            arr[y, x, 2] = rgb[2]
            arr[y, x, 3] = a * 255.0

    img = Image.fromarray(arr.astype(np.uint8), "RGBA")
    shape = rect_bar_mask((W, height))
    shape_a = np.array(shape, dtype=np.float32) / 255.0
    ca = np.array(img.split()[3], dtype=np.float32) * shape_a

    sheen_h = max(8, int(height * 0.14))
    for y in range(sheen_h):
        t = 1.0 - y / max(sheen_h - 1, 1)
        boost = BAR_COLORLESS_SHEEN_A * 255.0 * (t**1.4)
        ca[y, :] = np.minimum(255.0, ca[y, :] + boost * shape_a[y, :])

    img.putalpha(Image.fromarray(ca.astype(np.uint8)))
    draw = ImageDraw.Draw(img)
    draw.line(
        [(0, 1), (W - 1, 1)],
        fill=(255, 255, 255, BAR_COLORLESS_RIM_A),
        width=1,
    )
    return img


def _smooth_down(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.Resampling.LANCZOS)


def _choice_inner_gradient(w: int, h: int, border: int, inner_r: int, alpha_peak: float) -> Image.Image:
    """内底：与底栏同色系、半透明渐变（顶缘略实，避免与描边带之间露缝）。"""
    arr = np.zeros((h, w, 4), dtype=np.float32)
    y0, y1 = border, h - 1 - border
    for y in range(max(0, y0), min(h, y1 + 1)):
        t = (y - y0) / max(y1 - y0, 1)
        fade = t**1.1
        ri = int(BAR_TOP[0] + (BAR_BOTTOM[0] - BAR_TOP[0]) * t)
        gi = int(BAR_TOP[1] + (BAR_BOTTOM[1] - BAR_TOP[1]) * t)
        bi = int(BAR_TOP[2] + (BAR_BOTTOM[2] - BAR_TOP[2]) * t)
        lift = CHOICE_LIFT_MIX
        lr, lg, lb = CHOICE_LIFT_RGB
        ri = int(ri * (1 - lift) + lr * lift)
        gi = int(gi * (1 - lift) + lg * lift)
        bi = int(bi * (1 - lift) + lb * lift)
        a = alpha_peak * (0.32 + 0.68 * fade)
        arr[y, :, 0] = ri
        arr[y, :, 1] = gi
        arr[y, :, 2] = bi
        arr[y, :, 3] = np.minimum(255, a * 255)
    inner = Image.fromarray(arr.astype(np.uint8), "RGBA")
    mask = rounded_mask((w, h), max(1, inner_r))
    m = np.array(mask, dtype=np.float32) / 255.0
    ca = np.array(inner.split()[3], dtype=np.float32)
    inner.putalpha(Image.fromarray((ca * m).astype(np.uint8)))
    return inner


def _choice_anime_render(w: int, h: int, state: str) -> Image.Image:
    """选项钮：外圈+内底均半透明，叠在立绘上不挡景。"""
    scale = w / CHOICE_W
    r = max(4, int(RADIUS_CHOICE * scale))

    if state == "hover":
        border = max(4, int(5 * scale))
        ring = ACCENT[:3]
    elif state == "selected":
        border = max(3, int(4 * scale))
        ring = ACCENT[:3]
    else:
        border = max(2, int(2 * scale))
        ring = OUTLINE[:3]

    inner_a = CHOICE_INNER_A[state]
    ring_a = CHOICE_RING_A[state]
    inner_r = max(1, r - border)
    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))

    if state == "hover":
        glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.rounded_rectangle(
            (0, 0, w - 1, h - 1),
            radius=r + 3,
            fill=(*ACCENT_HOVER, CHOICE_GLOW_A),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(max(3, int(4 * scale))))
        layer = Image.alpha_composite(layer, glow)

    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=(*ring, ring_a))

    inner_fill = _choice_inner_gradient(w, h, border, inner_r, inner_a)
    layer = Image.alpha_composite(layer, inner_fill)

    rim = ImageDraw.Draw(layer)
    rim.rounded_rectangle(
        (border, border, w - 1 - border, h - 1 - border),
        radius=max(1, inner_r - 1),
        outline=(255, 255, 255, CHOICE_RIM_WHITE_A),
        width=max(1, int(1 * scale)),
    )

    if state == "hover":
        tint = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        td = ImageDraw.Draw(tint)
        td.rounded_rectangle(
            (border + 1, border, w - border - 2, h - border - 1),
            radius=max(1, inner_r - 2),
            fill=(*ACCENT_HOVER, CHOICE_TINT_A["hover"]),
        )
        layer = Image.alpha_composite(layer, tint)
    elif state == "selected":
        tint = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        td = ImageDraw.Draw(tint)
        td.rounded_rectangle(
            (border + 1, border, w - border - 2, h - border - 1),
            radius=max(1, inner_r - 2),
            fill=(*ACCENT, CHOICE_TINT_A["selected"]),
        )
        layer = Image.alpha_composite(layer, tint)

    shape = rounded_mask((w, h), r)
    sa = np.array(shape, dtype=np.float32) / 255.0
    ca = np.array(layer.split()[3], dtype=np.float32)
    layer.putalpha(Image.fromarray((ca * sa).astype(np.uint8)))
    return layer


def _choice_island_render(w: int, h: int, state: str, *, blue: bool = False) -> Image.Image:
    """浮岛 + 上亮下淡（粉套无色 / 蓝套淡天蓝雾，同形状）。"""
    scale = w / CHOICE_W
    island_m, (x0, y0, x1, y1) = floating_island_mask(w, h)
    ih = y1 - y0 + 1
    island_r = max(2, ih // 2)
    border_px = max(2, int(3 * scale))

    island_img = Image.fromarray((island_m * 255).astype(np.uint8), "L")
    erode_n = border_px * 2 + 1
    inner_m = (
        np.array(island_img.filter(ImageFilter.MinFilter(erode_n)), dtype=np.float32) / 255.0
    )
    edge_ring = np.clip(island_m - inner_m, 0.0, 1.0)

    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    t_y = np.clip((yy - y0) / max(ih - 1, 1), 0.0, 1.0)
    a_top = CHOICE_ISLAND_A_TOP[state]
    a_bot = CHOICE_ISLAND_A_BOTTOM[state]
    grad_a = a_top * (1.0 - t_y) ** 1.15 + a_bot * t_y**0.95
    top_cap = np.where(t_y < 0.22, (1.0 - t_y / 0.22) * CHOICE_ISLAND_TOP_CAP, 0.0)
    edge_top = np.where(t_y < 0.18, CHOICE_ISLAND_RIM_BOOST, 1.0)
    edge_a = CHOICE_ISLAND_EDGE_A[state] * edge_ring * edge_top
    a = (grad_a + top_cap + edge_a) * island_m

    top_band = yy <= y0 + max(2, int(2.5 * scale))
    seam = (island_m > 0.12) & top_band
    a = np.where(seam, np.maximum(a, a_top * 0.92), a)
    a = np.minimum(0.84, a)

    if blue:
        rgb_top = np.array((252, 253, 255), dtype=np.float32)
        rgb_bot = np.array(BAR_BOTTOM[:3], dtype=np.float32)
        glow_rgb = ACCENT_HOVER[:3]
        edge_mix = 0.32
    else:
        rgb_top = rgb_bot = np.array(CHOICE_ISLAND_RGB, dtype=np.float32)
        glow_rgb = (255, 255, 255)
        edge_mix = 0.0

    t3 = t_y[..., None]
    rgb = rgb_top * (1.0 - t3) + rgb_bot * t3
    if edge_mix > 0:
        accent = np.array(ACCENT[:3], dtype=np.float32)
        er3 = edge_ring[..., None]
        rgb = rgb * (1.0 - er3 * edge_mix) + accent * er3 * edge_mix

    arr = np.zeros((h, w, 4), dtype=np.uint8)
    arr[:, :, :3] = np.clip(rgb, 0, 255).astype(np.uint8)
    arr[:, :, 3] = (a * 255).astype(np.uint8)
    layer = Image.fromarray(arr, "RGBA")

    if state == "hover":
        glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.rounded_rectangle(
            (x0 - 4, y0 - 4, x1 + 4, y1 + 4),
            radius=island_r + 4,
            fill=(*glow_rgb, CHOICE_ISLAND_GLOW_A),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(max(3, int(3 * scale))))
        layer = Image.alpha_composite(glow, layer)

    return layer


def _choice_island_finish(img: Image.Image) -> Image.Image:
    """终尺寸套软浮岛 mask：保留留白，圆弧抗锯齿。"""
    w, h = img.size
    soft_m = soft_island_mask(w, h)
    ca = np.array(img.split()[3], dtype=np.float32)
    img.putalpha(Image.fromarray(np.clip(ca * soft_m, 0, 255).astype(np.uint8)))
    return img


def choice_colorless(state: str) -> Image.Image:
    s = CHOICE_SUPERSAMPLE
    big = _choice_island_render(CHOICE_W * s, CHOICE_H * s, state, blue=False)
    return _choice_island_finish(_smooth_down(big, (CHOICE_W, CHOICE_H)))


def choice_island_blue(state: str) -> Image.Image:
    s = CHOICE_SUPERSAMPLE
    big = _choice_island_render(CHOICE_W * s, CHOICE_H * s, state, blue=True)
    return _choice_island_finish(_smooth_down(big, (CHOICE_W, CHOICE_H)))


def choice_anime(state: str) -> Image.Image:
    s = UI_SUPERSAMPLE
    big = _choice_anime_render(CHOICE_W * s, CHOICE_H * s, state)
    return _smooth_down(big, (CHOICE_W, CHOICE_H))


def _nameplate_anime_render(nw: int, nh: int) -> Image.Image:
    """姓名区仅左侧竖条。"""
    layer = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    pad_y = max(2, nh // 10)
    r = max(2, nw // 3)
    draw.rounded_rectangle(
        (0, pad_y, nw - 1, nh - pad_y - 1),
        radius=r,
        fill=(*ACCENT, 255),
    )
    return layer


def nameplate_anime() -> Image.Image:
    s = UI_SUPERSAMPLE
    big = _nameplate_anime_render(NAMEPLATE_W * s, NAMEPLATE_H * s)
    return _smooth_down(big, (NAMEPLATE_W, NAMEPLATE_H))


def nameplate_colorless() -> Image.Image:
    layer = Image.new("RGBA", (NAMEPLATE_W, NAMEPLATE_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    pad_y = max(2, NAMEPLATE_H // 10)
    r = max(2, NAMEPLATE_W // 3)
    draw.rounded_rectangle(
        (0, pad_y, NAMEPLATE_W - 1, NAMEPLATE_H - pad_y - 1),
        radius=r,
        fill=(255, 255, 255, NAMEPLATE_COLORLESS_A),
    )
    return layer


def quick_bar_colorless() -> Image.Image:
    """无色快捷条，与底栏雾面一致。"""
    h = QUICK_BAR_H
    r_top = 16
    arr = np.zeros((h, W, 4), dtype=np.float32)
    for y in range(h):
        t = y / max(h - 1, 1)
        a = QUICK_BAR_COLORLESS_A * (0.12 + 0.88 * t)
        arr[y, :, 0] = 255.0
        arr[y, :, 1] = 255.0
        arr[y, :, 2] = 255.0
        arr[y, :, 3] = min(255.0, a * 255.0)
    img = Image.fromarray(arr.astype(np.uint8), "RGBA")
    shape = top_rounded_mask((W, h), r_top)
    shape_a = np.array(shape, dtype=np.float32) / 255.0
    ca = np.array(img.split()[3], dtype=np.float32)
    img.putalpha(Image.fromarray((ca * shape_a).astype(np.uint8)))
    return img


def quick_bar_anime() -> Image.Image:
    h = QUICK_BAR_H
    r_top = 16
    arr = np.zeros((h, W, 4), dtype=np.uint8)
    grad_a = np.zeros((h, W), dtype=np.uint8)
    for y in range(h):
        t = y / max(h - 1, 1)
        a = int(70 + 140 * t)
        grad_a[y, :] = a
        r = int(BAR_TOP[0] + (BAR_BOTTOM[0] - BAR_TOP[0]) * t)
        g = int(BAR_TOP[1] + (BAR_BOTTOM[1] - BAR_TOP[1]) * t)
        b = int(BAR_TOP[2] + (BAR_BOTTOM[2] - BAR_TOP[2]) * t)
        for x in range(W):
            arr[y, x] = (r, g, b, 255)
    fill = Image.fromarray(arr, "RGBA")
    shape = top_rounded_mask((W, h), r_top)
    img = Image.new("RGBA", (W, h), (0, 0, 0, 0))
    img.paste(fill, (0, 0), shape)
    shape_a = np.array(shape, dtype=np.float32) / 255.0
    img.putalpha(Image.fromarray((grad_a.astype(np.float32) * shape_a).astype(np.uint8)))
    draw = ImageDraw.Draw(img)
    _draw_bar_border_top_rounded(draw, W, h, r_top, OUTLINE, 2)
    return img


def _icon_k(size: int) -> float:
    """图标内部图形按画布等比缩放（基准 48px）。"""
    return size / 48.0


def _icon_circle_colorless(size: int, hover: bool) -> tuple[Image.Image, int, int, int, float, bool]:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    cx, cy = size // 2, size // 2
    k = _icon_k(size)
    r = int((size // 2 - 3) * 1.0)
    if hover:
        glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.ellipse(
            (cx - r - int(3 * k), cy - r - int(3 * k), cx + r + int(3 * k), cy + r + int(3 * k)),
            fill=(255, 255, 255, ICON_COLORLESS_GLOW_A),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(int(3 * k)))
        img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)
    fill = ICON_COLORLESS_FILL_H if hover else ICON_COLORLESS_FILL
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fill)
    draw.arc(
        (cx - r + 3, cy - r + 3, cx + r - 3, cy + r - 3),
        205,
        315,
        fill=(255, 255, 255, 80),
        width=max(1, int(2 * k)),
    )
    return img, r, cx, cy, k, hover


def _icon_circle(size: int, hover: bool) -> tuple[Image.Image, int, int, int, float, bool]:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    cx, cy = size // 2, size // 2
    k = _icon_k(size)
    r = int((size // 2 - 3) * 1.0)
    draw = ImageDraw.Draw(img)
    if hover:
        glow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.ellipse(
            (cx - r - int(3 * k), cy - r - int(3 * k), cx + r + int(3 * k), cy + r + int(3 * k)),
            fill=(*ACCENT_HOVER, 45),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(int(3 * k)))
        img = Image.alpha_composite(img, glow)
        draw = ImageDraw.Draw(img)
    draw.ellipse(
        (cx - r, cy - r, cx + r, cy + r),
        fill=(*ICON_FILL, 255) if not hover else (*ICON_FILL_HOVER, 255),
    )
    draw.arc(
        (cx - r + 3, cy - r + 3, cx + r - 3, cy + r - 3),
        205,
        315,
        fill=(255, 255, 255, 100),
        width=max(1, int(2 * k)),
    )
    return img, r, cx, cy, k, hover


def _draw_glyph_anime(
    draw: ImageDraw.ImageDraw, name: str, cx: int, cy: int, hover: bool, size: int
) -> None:
    fill = GLYPH_HOVER if hover else GLYPH
    edge = GLYPH_OUTLINE
    k = _icon_k(size)
    w = max(2, int((4 if hover else 3) * k))

    def poly(pts):
        draw.polygon(pts, fill=fill)

    def line(pts, width=None):
        draw.line(pts, fill=edge, width=width or w, joint="curve")

    # 相对 48px 设计稿的微调（修正视觉重心，非几何中心）
    glyph_ox, glyph_oy = {
        "skip": (2.0, 0.0),    # 双三角指向右，视觉重心偏左 → 右移
        "voice": (-4.5, 0.0),  # 喇叭+声波偏右 → 左移
    }.get(name, (0.0, 0.0))

    def R(x: float, y: float) -> tuple[int, int]:
        return (int(cx + (x + glyph_ox) * k), int(cy + (y + glyph_oy) * k))

    if name == "auto":
        # 约占内圆 70%：大三角 + 左侧弧（自动播放）
        poly([R(-7, -11), R(11, 0), R(-7, 11)])
        draw.arc(
            (R(-15, -13)[0], R(-15, -13)[1], R(2, 13)[0], R(2, 13)[1]),
            205,
            335,
            fill=edge,
            width=w,
        )
    elif name == "skip":
        # 双「快进」三角，x 范围 -12…12 对称
        poly([R(-12, -11), R(0, 0), R(-12, 11)])
        poly([R(-2, -11), R(12, 0), R(-2, 11)])
    elif name == "hide":
        draw.ellipse((*R(-15, -8), *R(15, 8)), outline=edge, width=w)
        draw.ellipse((*R(-6, -4), *R(6, 4)), fill=fill)
        line([R(-17, 12), R(17, -12)])
    elif name == "history":
        draw.ellipse((*R(-12, -12), *R(12, 12)), outline=edge, width=w)
        line([R(0, 0), R(0, -8)], w)
        line([R(0, 0), R(7, 5)], w)
    elif name == "save":
        rr = int(4 * k)
        draw.rounded_rectangle((*R(-12, -8), *R(12, 12)), radius=rr, outline=edge, width=w)
        draw.rounded_rectangle((*R(-8, -14), *R(8, -6)), radius=rr, fill=fill, outline=edge)
    elif name == "load":
        rr = int(4 * k)
        draw.rounded_rectangle((*R(-12, -6), *R(12, 12)), radius=rr, outline=edge, width=w)
        poly([R(-6, -4), R(0, -13), R(6, -4)])
    elif name == "settings":
        draw.ellipse((*R(-7, -7), *R(7, 7)), fill=fill, outline=edge, width=max(2, int(2 * k)))
        for i in range(6):
            ang = math.radians(i * 60)
            x1 = cx + int(13 * k * math.cos(ang))
            y1 = cy + int(13 * k * math.sin(ang))
            d = int(4 * k)
            draw.ellipse((x1 - d, y1 - d, x1 + d, y1 + d), fill=fill, outline=edge)
    elif name == "exit":
        draw.arc((*R(-16, -16), *R(16, 16)), 30, 150, fill=edge, width=w)
        line([R(-8, -8), R(8, 8)])
        line([R(-8, 8), R(8, -8)])
    elif name == "voice":
        poly([R(-8, -8), R(-8, 8), R(0, 8), R(10, 13), R(10, -13), R(0, -8)])
        draw.arc(
            (R(9, -11)[0], R(9, -11)[1], R(18, 0)[0], R(18, 0)[1]),
            300,
            60,
            fill=edge,
            width=max(2, int(2 * k)),
        )
        draw.arc(
            (R(9, 0)[0], R(9, 0)[1], R(18, 11)[0], R(18, 11)[1]),
            300,
            60,
            fill=edge,
            width=max(2, int(2 * k)),
        )


def _icon_outline_colorless(img: Image.Image, cx: int, cy: int, r: int, k: float, hover: bool) -> None:
    draw = ImageDraw.Draw(img)
    ow = max(2, int(3 * k)) if hover else max(2, int(2 * k))
    inset = max(1, ow // 2)
    draw.ellipse(
        (cx - r + inset, cy - r + inset, cx + r - inset, cy + r - inset),
        outline=(255, 255, 255, ICON_COLORLESS_RING_A + (40 if hover else 0)),
        width=ow,
    )


def _icon_outline(img: Image.Image, cx: int, cy: int, r: int, k: float, hover: bool) -> None:
    """描边画在填充内侧 1px，避免顶缘露底形成灰线。"""
    draw = ImageDraw.Draw(img)
    ow = max(2, int(3 * k)) if hover else max(2, int(2 * k))
    inset = max(1, ow // 2)
    # 默认 ACCENT、hover ACCENT_HOVER（粉/蓝同一逻辑，对齐各套 hover 外圈色）
    ring = ACCENT_HOVER if hover else ACCENT
    draw.ellipse(
        (cx - r + inset, cy - r + inset, cx + r - inset, cy + r - inset),
        outline=ring,
        width=ow,
    )


def _render_icon_at_size(size: int, name: str, hover: bool) -> Image.Image:
    base, r, cx, cy, k, hover = _icon_circle(size, hover)
    draw = ImageDraw.Draw(base)
    _draw_glyph_anime(draw, name, cx, cy, hover, size)
    _icon_outline(base, cx, cy, r, k, hover)
    return base


def _render_icon_colorless_at_size(size: int, name: str, hover: bool) -> Image.Image:
    global GLYPH, GLYPH_HOVER, GLYPH_OUTLINE
    base, r, cx, cy, k, hover = _icon_circle_colorless(size, hover)
    draw = ImageDraw.Draw(base)
    glyph = ICON_COLORLESS_GLYPH_H if hover else ICON_COLORLESS_GLYPH
    edge = ICON_COLORLESS_GLYPH
    old_g, old_gh, old_go = GLYPH, GLYPH_HOVER, GLYPH_OUTLINE
    GLYPH, GLYPH_HOVER, GLYPH_OUTLINE = glyph, glyph, edge
    try:
        _draw_glyph_anime(draw, name, cx, cy, hover, size)
    finally:
        GLYPH, GLYPH_HOVER, GLYPH_OUTLINE = old_g, old_gh, old_go
    _icon_outline_colorless(base, cx, cy, r, k, hover)
    return base


def quick_icon_anime(name: str, hover: bool) -> Image.Image:
    size = QUICK_ICON
    s = size * UI_SUPERSAMPLE
    big = _render_icon_at_size(s, name, hover)
    return big.resize((size, size), Image.Resampling.LANCZOS)


def quick_icon_colorless(name: str, hover: bool) -> Image.Image:
    size = QUICK_ICON
    s = size * UI_SUPERSAMPLE
    big = _render_icon_colorless_at_size(s, name, hover)
    return big.resize((size, size), Image.Resampling.LANCZOS)


def voice_icon_colorless(hover: bool) -> Image.Image:
    size = VOICE_ICON
    s = size * UI_SUPERSAMPLE
    big = _render_icon_colorless_at_size(s, "voice", hover)
    return big.resize((size, size), Image.Resampling.LANCZOS)


def voice_icon_anime(hover: bool) -> Image.Image:
    size = VOICE_ICON
    s = size * UI_SUPERSAMPLE
    big = _render_icon_at_size(s, "voice", hover)
    return big.resize((size, size), Image.Resampling.LANCZOS)


def main(theme: str = "pink") -> None:
    if theme not in THEMES:
        raise SystemExit(f"Unknown theme {theme!r}, use: {', '.join(THEMES)}")
    apply_theme(theme)
    OUT.mkdir(parents=True, exist_ok=True)
    written: list[str] = []

    def save(img: Image.Image, name: str) -> None:
        img.save(OUT / name, "PNG")
        written.append(name)

    if theme == "pink":
        save(
            bar_colorless(BAR_H, BAR_COLORLESS_A_DIALOGUE, False, left_slot=False),
            "UI_DS_bar_dialogue.png",
        )
        save(
            bar_colorless(BAR_H, BAR_COLORLESS_A_NVL, True, left_slot=False),
            "UI_DS_bar_narration.png",
        )
    else:
        save(bar_anime(BAR_H, BAR_A_DIALOGUE, False, True), "UI_DS_bar_dialogue.png")
        save(bar_anime(BAR_H, BAR_A_NARRATION, True, False), "UI_DS_bar_narration.png")

    for st in ("normal", "hover", "selected"):
        if theme == "pink":
            save(choice_colorless(st), f"UI_DS_choice_{st}.png")
        else:
            save(choice_island_blue(st), f"UI_DS_choice_{st}.png")

    if theme == "pink":
        apply_theme("pink")

    save(nameplate_anime(), "UI_DS_nameplate.png")
    save(quick_bar_anime(), "UI_DS_quick_bar.png")
    for name in ("auto", "skip", "hide", "history", "save", "load", "settings", "exit"):
        for state in ("default", "hover"):
            save(
                quick_icon_anime(name, state == "hover"),
                f"UI_DS_quick_{name}_{state}.png",
            )
    for state in ("default", "hover"):
        save(voice_icon_anime(state == "hover"), f"UI_DS_say_voice_{state}.png")

    print(f"Anime / cartoon say UI [{theme}] ->", OUT)
    print("Files:", len(written))
    for n in sorted(written):
        p = OUT / n
        im = Image.open(p)
        print(f"  {n}  {im.size[0]}x{im.size[1]}")
    return written


def _publish_say_previews(themes: list[str]) -> None:
    scripts_dir = Path(__file__).resolve().parent
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    from build_say_screen_preview import publish_previews

    print("--- Say screen previews ---")
    publish_previews(themes, triggered_by="build_ui_anime_say.py")


if __name__ == "__main__":
    argv = [a for a in sys.argv[1:] if a != "--no-preview"]
    skip_preview = "--no-preview" in sys.argv[1:]
    arg = argv[0] if argv else "pink"

    if arg == "all":
        for theme in ("pink", "blue"):
            main(theme)
        if not skip_preview:
            _publish_say_previews(["pink", "blue"])
    else:
        if arg not in THEMES:
            raise SystemExit(f"Unknown theme {arg!r}, use: {', '.join(THEMES)} or all")
        main(arg)
        if not skip_preview:
            _publish_say_previews([arg])
