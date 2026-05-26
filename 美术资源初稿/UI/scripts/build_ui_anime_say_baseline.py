#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
【基准版 v2 · 冻结 2026-05-19 — 含樱粉/晴空蓝定调 · 勿日常改】
配色: UI_THEME_COLORS.md · 恢复: python restore_ui_baseline.py

二次元 / 卡通风 say 全套 UI（独立目录，不覆盖 UI_DS_* 极简版）。
输出: UI/anime_style/ 或 UI/anime_style_blue/
用法: python build_ui_anime_say_baseline.py [pink|blue|all]（仅归档/对比）
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
BAR_H = 360
CHOICE_W, CHOICE_H = 780, 76
NAMEPLATE_W, NAMEPLATE_H = 320, 44
QUICK_BAR_H = 56
QUICK_ICON = 48
VOICE_ICON = 40

UI_ROOT = Path(r"J:\项目\GAL\美术资源初稿\UI")
UI_SUPERSAMPLE = 3  # choice / nameplate 超采样后缩小，圆角更光滑

# 主题色（由 apply_theme 写入）
BAR_TOP = (255, 252, 255)
BAR_BOTTOM = (255, 228, 238)
BAR_NVL_TOP = (255, 250, 252)
BAR_NVL_BOTTOM = (255, 235, 245)
INNER_CREAM = (255, 242, 248)
OUTLINE = (200, 110, 145, 255)
ACCENT = (255, 105, 140)
ACCENT_HOVER = (255, 150, 175)
ACCENT_DEEP = (220, 80, 120)
GLYPH = (120, 70, 100, 255)
GLYPH_HOVER = (255, 90, 130, 255)
GLYPH_OUTLINE = (180, 90, 120, 255)
CHOICE_GRAD_BASE = (255, 248, 252)
CHOICE_GRAD_DROP = (8, 18, 10)
ICON_FILL = (255, 248, 252)
ICON_FILL_HOVER = (255, 228, 238)
OUT = UI_ROOT / "anime_style"

BAR_A_DIALOGUE = 0.78
BAR_A_NARRATION = 0.65
RADIUS_BAR_TOP = 28
RADIUS_CHOICE = 22
RADIUS_NAME = 16

THEMES: dict[str, dict] = {
    "pink": {
        "dir": "anime_style",
        "BAR_TOP": (255, 252, 255),
        "BAR_BOTTOM": (255, 228, 238),
        "BAR_NVL_TOP": (255, 250, 252),
        "BAR_NVL_BOTTOM": (255, 235, 245),
        "INNER_CREAM": (255, 242, 248),
        "OUTLINE": (200, 110, 145, 255),
        "ACCENT": (255, 105, 140),
        "ACCENT_HOVER": (255, 150, 175),
        "ACCENT_DEEP": (220, 80, 120),
        "GLYPH": (120, 70, 100, 255),
        "GLYPH_HOVER": (255, 90, 130, 255),
        "GLYPH_OUTLINE": (180, 90, 120, 255),
        "CHOICE_GRAD": ((255, 248, 252), (8, 18, 10)),
        "ICON_FILL": (255, 248, 252),
        "ICON_FILL_HOVER": (255, 228, 238),
    },
    "blue": {
        "dir": "anime_style_blue",
        "BAR_TOP": (248, 252, 255),
        "BAR_BOTTOM": (210, 228, 255),
        "BAR_NVL_TOP": (250, 253, 255),
        "BAR_NVL_BOTTOM": (225, 238, 252),
        "INNER_CREAM": (242, 248, 255),
        "OUTLINE": (85, 125, 185, 255),
        "ACCENT": (70, 140, 220),
        "ACCENT_HOVER": (110, 175, 245),
        "ACCENT_DEEP": (50, 95, 165),
        "GLYPH": (55, 85, 125, 255),
        "GLYPH_HOVER": (90, 155, 235, 255),
        "GLYPH_OUTLINE": (65, 105, 155, 255),
        "CHOICE_GRAD": ((242, 248, 255), (10, 20, 8)),
        "ICON_FILL": (242, 248, 255),
        "ICON_FILL_HOVER": (218, 232, 255),
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


def top_rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    """仅顶部圆角；避免整图圆角 + 底矩形拼接产生接缝横线。"""
    w, h = size
    r = min(radius, h // 2, w // 2)
    m = Image.new("L", size, 0)
    d = ImageDraw.Draw(m)
    if h > r:
        d.rectangle((0, r, w - 1, h - 1), fill=255)
    d.rounded_rectangle((0, 0, w - 1, min(h - 1, 2 * r + 2)), radius=r, fill=255)
    return m


def _draw_bar_border_top_rounded(
    draw: ImageDraw.ImageDraw, w: int, h: int, radius: int, color: tuple, width: int
) -> None:
    """只画上圆角 + 直底边，不用整圈 rounded_rectangle（避免底角多余线段）。"""
    r = min(radius, h // 2, w // 2)
    ow = width
    inset = ow // 2 + 1
    # 底边
    draw.line(
        [(inset, h - inset - 1), (w - inset - 1, h - inset - 1)],
        fill=color,
        width=ow,
    )
    # 左右竖边（从圆角下端到距底 inset）
    draw.line([(inset, r), (inset, h - inset - 1)], fill=color, width=ow)
    draw.line([(w - inset - 1, r), (w - inset - 1, h - inset - 1)], fill=color, width=ow)
    # 顶边直线（两角之间）
    draw.line([(r, inset), (w - r - 1, inset)], fill=color, width=ow)
    # 左上、右上圆角弧
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
    r_top = RADIUS_BAR_TOP

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
    shape = top_rounded_mask((W, height), r_top)
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
    _draw_bar_border_top_rounded(draw, W, height, r_top, OUTLINE, 2)
    return img


def _smooth_down(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    return img.resize(size, Image.Resampling.LANCZOS)


def _choice_anime_render(w: int, h: int, state: str) -> Image.Image:
    """在目标尺寸绘制选项钮（供超采样调用）。"""
    scale = w / CHOICE_W
    r = max(4, int(RADIUS_CHOICE * scale))
    border = max(2, int(2 * scale))
    cream_top = INNER_CREAM

    if state == "selected":
        ring = ACCENT[:3]
    elif state == "hover":
        ring = ACCENT_HOVER[:3]
    else:
        ring = OUTLINE[:3]

    rgb = np.zeros((h, w, 3), dtype=np.uint8)
    gb, gd = CHOICE_GRAD_BASE, CHOICE_GRAD_DROP
    for y in range(h):
        t = y / max(h - 1, 1)
        rgb[y, :, 0] = gb[0] - int(gd[0] * t)
        rgb[y, :, 1] = gb[1] - int(gd[1] * t)
        rgb[y, :, 2] = gb[2] - int(gd[2] * t)

    layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=(*ring, 255))
    inner_r = max(1, r - border)
    draw.rounded_rectangle(
        (border, border - 1, w - 1 - border, h - 1 - border),
        radius=inner_r,
        fill=(*cream_top, 255),
    )
    flat_l, flat_r = border + inner_r, w - 1 - border - inner_r
    if flat_r > flat_l:
        draw.rectangle((flat_l, border - 1, flat_r, border + 1), fill=(*cream_top, 255))

    # 渐变叠在内区
    inner = Image.fromarray(rgb, mode="RGB").convert("RGBA")
    inner_mask = rounded_mask((w, h), max(1, inner_r))
    layer.paste(inner, (0, 0), inner_mask)

    if state == "selected":
        tint = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        td = ImageDraw.Draw(tint)
        td.rounded_rectangle(
            (border + 1, border, w - border - 2, h - border - 1),
            radius=max(1, inner_r - 2),
            fill=(*ACCENT, 45),
        )
        layer = Image.alpha_composite(layer, tint)

    if state == "hover":
        glow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        g = ImageDraw.Draw(glow)
        g.rounded_rectangle(
            (0, 0, w - 1, h - 1),
            radius=r + 2,
            outline=(*ACCENT_HOVER, 100),
            width=max(3, int(4 * scale)),
        )
        glow = glow.filter(ImageFilter.GaussianBlur(max(2, int(3 * scale))))
        layer = Image.alpha_composite(glow, layer)

    layer.putalpha(rounded_mask((w, h), r))
    return layer


def choice_anime(state: str) -> Image.Image:
    s = UI_SUPERSAMPLE
    big = _choice_anime_render(CHOICE_W * s, CHOICE_H * s, state)
    return _smooth_down(big, (CHOICE_W, CHOICE_H))


def _nameplate_anime_render(nw: int, nh: int) -> Image.Image:
    scale = nw / NAMEPLATE_W
    r = max(4, int(RADIUS_NAME * scale))
    border = max(2, int(2 * scale))
    pink = OUTLINE[:3]
    cream = INNER_CREAM

    layer = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.rounded_rectangle((0, 0, nw - 1, nh - 1), radius=r, fill=(*pink, 255))
    inner_r = max(1, r - border)
    draw.rounded_rectangle(
        (border, border - 1, nw - 1 - border, nh - 1 - border),
        radius=inner_r,
        fill=(*cream, 255),
    )
    flat_l, flat_r = border + inner_r, nw - 1 - border - inner_r
    if flat_r > flat_l:
        draw.rectangle((flat_l, border - 1, flat_r, border + 1), fill=(*cream, 255))
    bx = int(5 * scale)
    bw = int(6 * scale)
    draw.rounded_rectangle(
        (bx, int(8 * scale), bx + bw, nh - int(9 * scale)),
        radius=max(2, int(3 * scale)),
        fill=(*ACCENT, 255),
    )
    layer.putalpha(rounded_mask((nw, nh), r))
    return layer


def nameplate_anime() -> Image.Image:
    s = UI_SUPERSAMPLE
    big = _nameplate_anime_render(NAMEPLATE_W * s, NAMEPLATE_H * s)
    return _smooth_down(big, (NAMEPLATE_W, NAMEPLATE_H))


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


def _icon_outline(img: Image.Image, cx: int, cy: int, r: int, k: float, hover: bool) -> None:
    """描边画在填充内侧 1px，避免顶缘露底形成灰线。"""
    draw = ImageDraw.Draw(img)
    ow = max(2, int(3 * k)) if hover else max(2, int(2 * k))
    inset = max(1, ow // 2)
    draw.ellipse(
        (cx - r + inset, cy - r + inset, cx + r - inset, cy + r - inset),
        outline=ACCENT_HOVER if hover else OUTLINE,
        width=ow,
    )


def _render_icon_at_size(size: int, name: str, hover: bool) -> Image.Image:
    base, r, cx, cy, k, hover = _icon_circle(size, hover)
    draw = ImageDraw.Draw(base)
    _draw_glyph_anime(draw, name, cx, cy, hover, size)
    _icon_outline(base, cx, cy, r, k, hover)
    return base


def quick_icon_anime(name: str, hover: bool) -> Image.Image:
    size = QUICK_ICON
    s = size * UI_SUPERSAMPLE
    big = _render_icon_at_size(s, name, hover)
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

    save(bar_anime(BAR_H, BAR_A_DIALOGUE, False, True), "UI_DS_bar_dialogue.png")
    save(bar_anime(BAR_H, BAR_A_NARRATION, True, False), "UI_DS_bar_narration.png")
    save(nameplate_anime(), "UI_DS_nameplate.png")

    for st in ("normal", "hover", "selected"):
        save(choice_anime(st), f"UI_DS_choice_{st}.png")

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


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "pink"
    if arg == "all":
        for theme in ("pink", "blue"):
            main(theme)
    else:
        main(arg)
