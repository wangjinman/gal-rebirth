#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导出 Say 屏 UI 对照示意图 → UI/UI_SAY_LAYOUT_DIAGRAM.png"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

UI = Path(r"J:\项目\GAL\美术资源初稿\UI")
OUT = UI / "UI_SAY_LAYOUT_DIAGRAM.png"

W, H = 1920, 2200
MARGIN = 48
PANEL_H = 980
GAP = 40

# 定调色
PINK = (255, 178, 200)
PINK_ACC = (255, 112, 168)
BLUE = (115, 220, 255)
BLUE_ACC = (65, 185, 255)
YELLOW = (255, 210, 80)
GRAY_BG = (248, 249, 252)
GRAY_LINE = (180, 190, 210)
GRAY_TEXT = (55, 65, 85)
WHITE = (255, 255, 255)


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _rounded_rect(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    radius: int,
    fill=None,
    outline=None,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def _center_text(draw, box, text, font, fill):
    x0, y0, x1, y1 = box
    bb = draw.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    draw.text((x0 + (x1 - x0 - tw) // 2, y0 + (y1 - y0 - th) // 2), text, fill=fill, font=font)


def _draw_screen_wireframe(
    draw: ImageDraw.ImageDraw,
    ox: int,
    oy: int,
    pw: int,
    ph: int,
    mode: str,
) -> None:
    """mode: ref | ours_pink | ours_blue"""
    _rounded_rect(draw, (ox, oy, ox + pw, oy + ph), 16, fill=WHITE, outline=GRAY_LINE, width=2)
    # 背景区
    bg = (ox + 16, oy + 56, ox + pw - 16, oy + ph - 400)
    draw.rectangle(bg, fill=(235, 242, 250))
    draw.text((bg[0] + 12, bg[1] + 8), "背景 + 立绘区", fill=GRAY_TEXT, font=_font(18))

    cx = ox + pw // 2
    cy_choices = oy + 320

    if mode == "ref":
        for i, border in enumerate([BLUE_ACC, PINK_ACC, BLUE_ACC]):
            y = cy_choices + i * 92
            box = (cx - 390, y, cx + 390, y + 76)
            _rounded_rect(draw, box, 22, outline=border, width=3, fill=(255, 255, 255, 200))
            draw.ellipse((box[0] + 12, y + 18, box[0] + 52, y + 58), fill=(255, 90, 110))
            draw.text((box[0] + 70, y + 24), "这是选项框的文本", fill=GRAY_TEXT, font=_font(17))
            draw.line((box[2] - 48, y + 20, box[2] - 20, y + 48), fill=YELLOW, width=4)
        draw.text((ox + 24, oy + ph - 430), "═ 黄色装饰条（独立图层，非底栏 α）═", fill=YELLOW, font=_font(16))
        bar_y = oy + ph - 360
        bar = (ox + 16, bar_y, ox + pw - 16, oy + ph - 24)
        _rounded_rect(draw, bar, 12, fill=(255, 255, 255, 190), outline=GRAY_LINE, width=2)
        draw.text((bar[0] + 20, bar_y + 16), "角色名字", fill=YELLOW, font=_font(22, bold=True))
        draw.text((bar[0] + 130, bar_y + 18), "🔊", fill=BLUE_ACC, font=_font(20))
        draw.text(
            (bar[0] + 20, bar_y + 56),
            "正文区域（样张建议约三行上限）",
            fill=GRAY_TEXT,
            font=_font(17),
        )
        draw.text((bar[2] - 420, bar_y + 280), "Q.LOAD  Q.SAVE  [图标…]  [X]", fill=BLUE_ACC, font=_font(15))
        draw.text((ox + 24, oy + ph - 52), "左下 LOGO → 换游戏 Logo", fill=GRAY_TEXT, font=_font(14))
    else:
        accent = PINK_ACC if mode == "ours_pink" else BLUE_ACC
        hover = PINK if mode == "ours_pink" else BLUE
        theme = "樱粉 anime_style/" if mode == "ours_pink" else "晴空蓝 anime_style_blue/"
        for i in range(3):
            y = cy_choices + i * 92
            box = (cx - 390, y, cx + 390, y + 76)
            _rounded_rect(draw, box, 22, outline=accent if i != 1 else hover, width=3, fill=(255, 252, 254))
            _center_text(draw, (box[0], y, box[2], y + 76), "UI_DS_choice_*.png", _font(16), GRAY_TEXT)
        draw.text((ox + 24, oy + ph - 430), f"主题：{theme}", fill=accent, font=_font(16))
        bar_y = oy + ph - 360
        bar = (ox + 16, bar_y, ox + pw - 16, oy + ph - 24)
        _rounded_rect(draw, bar, 28, fill=(255, 255, 255, 200), outline=accent, width=2)
        np = (bar[0] + 20, bar_y - 36, bar[0] + 340, bar_y - 4)
        _rounded_rect(draw, np, 12, fill=(255, 250, 253), outline=accent, width=2)
        draw.text((np[0] + 48, bar_y - 32), "UI_DS_nameplate.png", fill=accent, font=_font(15))
        draw.ellipse((bar[0] + 360, bar_y - 34, bar[0] + 400, bar_y + 2), outline=accent, width=2)
        draw.text((bar[0] + 368, bar_y - 30), "♪", fill=accent, font=_font(14))
        draw.text((bar[0] + 20, bar_y + 20), "gui 正文 x=400  w=1420", fill=GRAY_TEXT, font=_font(17))
        qbar = (ox + 16, bar_y - 56, ox + pw - 16, bar_y - 8)
        _rounded_rect(draw, qbar, 10, fill=(248, 252, 255), outline=accent, width=1)
        draw.text((qbar[0] + 12, bar_y - 48), "UI_DS_quick_bar.png 1920×56", fill=GRAY_TEXT, font=_font(14))
        ix = bar[2] - 420
        for j in range(6):
            draw.ellipse((ix + j * 52, bar_y + 268, ix + j * 52 + 40, bar_y + 308), outline=accent, width=2)
        draw.text((bar[2] - 400, bar_y + 318), "quick_* 48×48", fill=GRAY_TEXT, font=_font(13))
        alpha = "α≈0.80" if mode == "ours_pink" else "α≈0.80"
        draw.text((bar[0] + 20, bar_y + 300), f"UI_DS_bar_dialogue.png  1920×360  {alpha}", fill=accent, font=_font(15))


def main() -> None:
    img = Image.new("RGB", (W, H), GRAY_BG)
    draw = ImageDraw.Draw(img)
    title_f = _font(32, bold=True)
    sub_f = _font(20)
    small_f = _font(16)

    draw.text((MARGIN, 28), "GAL · Say 屏 UI 对照示意图", fill=GRAY_TEXT, font=title_f)
    draw.text(
        (MARGIN, 72),
        "上：参考样张（功能示意）  下：已交付拼装（1920×1080 · 详见 UI_SAY_LAYOUT_GUIDE.md）",
        fill=GRAY_TEXT,
        font=sub_f,
    )

    pw = W - 2 * MARGIN
    y0 = 120

    # --- 参考 ---
    draw.text((MARGIN, y0), "① 参考样张 · ADV 预览", fill=GRAY_TEXT, font=_font(22, bold=True))
    _draw_screen_wireframe(draw, MARGIN, y0 + 36, pw, PANEL_H, "ref")

    y1 = y0 + 36 + PANEL_H + GAP
    draw.text((MARGIN, y1), "② 已交付 · 晴空蓝线（anime_style_blue/）", fill=BLUE_ACC, font=_font(22, bold=True))
    _draw_screen_wireframe(draw, MARGIN, y1 + 36, pw, PANEL_H, "ours_blue")

    # 图例
    ly = y1 + 36 + PANEL_H + 24
    draw.text((MARGIN, ly), "图例", fill=GRAY_TEXT, font=_font(18, bold=True))
    items = [
        (BLUE_ACC, "晴空蓝强调 #41B9FF"),
        (BLUE, "Hover 外圈 #73DCFF"),
        (PINK_ACC, "樱粉强调 #FF70A8（粉套同布局，见 anime_style/）"),
        (YELLOW, "样张专用：黄字/黄装饰（本项目未做进 PNG）"),
    ]
    for i, (col, lab) in enumerate(items):
        y = ly + 32 + i * 28
        draw.rectangle((MARGIN, y, MARGIN + 22, y + 18), fill=col)
        draw.text((MARGIN + 32, y - 2), lab, fill=GRAY_TEXT, font=small_f)

    draw.text(
        (MARGIN, H - 36),
        "生成: scripts/build_ui_say_layout_diagram.py  ·  配色: UI_THEME_COLORS.md",
        fill=GRAY_TEXT,
        font=small_f,
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("Saved:", OUT, img.size)


if __name__ == "__main__":
    main()
