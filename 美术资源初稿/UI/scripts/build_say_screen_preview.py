#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将 背景 + 立绘 + Say 屏 UI 合成为 1920×1080 实机感预览图。
无需启动 Ren'Py。

用法:
  python build_say_screen_preview.py
  python build_say_screen_preview.py --theme pink --layout galcs --mode say --bg BG_02
  python build_say_screen_preview.py --sheet
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

UI_ROOT = Path(r"J:\项目\GAL\美术资源初稿\UI")
ART_ROOT = Path(r"J:\项目\GAL\美术资源初稿")
BG_DIR = ART_ROOT / "背景"
SPRITE_DEFAULT = (
    ART_ROOT / "立绘" / "lin-wantang-expr-smile-v3-transparent-v1-feather.png"
)
SIDE_DEFAULT = (
    ART_ROOT / "立绘" / "bust" / "lin-wantang-expr-smile-v3-transparent-v1-bust-feather.png"
)
GALCS_LINDAO_NORMAL = Path(
    r"J:\项目\GAL\开发\RenPy项目\GALCS\game\images\character\lindao\LWT_01_normal.png"
)
BAR_H = 280
NAMEPLATE_W, NAMEPLATE_H = 12, 44
PREVIEW_DIR = UI_ROOT / "previews"
PREVIEW_LATEST = PREVIEW_DIR / "latest"
PREVIEW_HISTORY = PREVIEW_DIR / "history"
GALCS_FONTS = Path(r"J:\项目\GAL\开发\RenPy项目\GALCS\game\fonts")

W, H = 1920, 1080


@dataclass(frozen=True)
class SayFontProfile:
    """Say 屏字体方案（用于预览对比）。"""

    id: str
    title: str
    subtitle: str
    regular: Path
    bold: Path | None = None
    who_size: int = 42
    what_size: int = 38
    choice_size: int = 28
    who_color: str = "#FF70A8"
    what_color: str = "#E8ECF2"
    choice_color: str = "#ffffff"
    outline_w: int = 2
    outline: str = "#101820"
    line_spacing: int = 12
    use_outline: bool = True

THEME_DIRS = {
    "pink": UI_ROOT / "anime_style",
    "blue": UI_ROOT / "anime_style_blue",
}

# GALCS screens.rpy 对齐（底栏高 BAR_H，ypos = 1080 - BAR_H）
LAYOUT_GALCS = {
    "bar_y": H - BAR_H,
    "nameplate": (345, H - BAR_H + 26),
    "text_box": (370, H - BAR_H + 26, 1190, BAR_H - 36),
    "who_size": 42,
    "what_size": 38,
    "who_color": "#FF70A8",
    "what_color": "#E8ECF2",
    "quick_origin": (1460, 1016),
    "quick_spacing": 6,
    "quick_icons": (
        "UI_DS_quick_auto_default.png",
        "UI_DS_quick_skip_default.png",
        "UI_DS_quick_save_default.png",
        "UI_DS_quick_load_default.png",
        "UI_DS_quick_history_default.png",
        "UI_DS_quick_settings_default.png",
        "UI_DS_quick_hide_default.png",
        "UI_DS_quick_exit_default.png",
    ),
    "choice_box": (800, 90),  # screens.rpy xsize×ysize
    "choice_spacing": 15,  # vbox spacing
    "choice_text_size": 26,
}

# MO 式左侧槽：主角 / 角色+side / 旁白
LAYOUT_LEFT_SLOT = {
    "bar_y": H - BAR_H,
    "side": (18, H, 280),
    "nameplate_hero": (24, H - BAR_H + 18),
    "nameplate_npc": (196, H - BAR_H + 18),
    "text_box_hero": (292, H - BAR_H + 28, 1188, 268),
    "text_box_npc": (408, H - BAR_H + 28, 1072, 268),
    "text_box_nvl": (88, H - BAR_H + 28, 1352, 268),
    "who_size": 42,
    "what_size": 38,
    "who_color": "#FF70A8",
    "what_color": "#E8ECF2",
    "quick_origin": (1460, 1016),
    "quick_spacing": 6,
    "quick_icons": LAYOUT_GALCS["quick_icons"],
    "choice_box": (800, 90),
    "choice_spacing": 15,
    "choice_text_size": 26,
}

# UI_SAY_LAYOUT_GUIDE.md 推荐叠层
LAYOUT_SPEC = {
    "bar_y": H - BAR_H,
    "quick_bar_y": 664,
    "nameplate": (400, 688),
    "voice": (720, 708),
    "text_box": (496, 746, 1320, 300),
    "who_size": 42,
    "what_size": 38,
    "who_color": "#FF70A8",
    "what_color": "#E8ECF2",
    "quick_origin": (1460, 668),
    "quick_spacing": 8,
    "quick_icons": LAYOUT_GALCS["quick_icons"],
    "choice_box": (780, 76),
    "choice_spacing": 14,
    "choice_text_size": 26,
}

SAMPLE_WHO = "林晚棠"
SAMPLE_WHAT = (
    "夕阳把教室染成蜜色。她回头看我，睫毛在光里轻轻晃了一下。\n"
    "「明天……还会来吗？」"
)
SAMPLE_CHOICES = (
    ("当然会。", "normal"),
    ("……让我想想。", "hover"),
    ("今天先回去吧。", "normal"),
)


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        GALCS_FONTS / "simhei.ttf",
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
    ]
    for p in candidates:
        try:
            return ImageFont.truetype(str(p), size)
        except OSError:
            continue
    return ImageFont.load_default()


def _font_profile(
    profile: SayFontProfile, size: int, *, bold: bool = False
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    path = profile.bold if bold and profile.bold and profile.bold.is_file() else profile.regular
    try:
        return ImageFont.truetype(str(path), size)
    except OSError:
        return _font(size, bold=bold)


def _hex_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _text_outline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fill: str,
    outline: str = "#1a1a22",
    ow: int = 2,
    *,
    enabled: bool = True,
) -> None:
    if not enabled:
        draw.text(xy, text, font=font, fill=_hex_rgb(fill))
        return
    x, y = xy
    oc = _hex_rgb(outline)
    fc = _hex_rgb(fill)
    for dx in range(-ow, ow + 1):
        for dy in range(-ow, ow + 1):
            if dx == 0 and dy == 0:
                continue
            draw.text((x + dx, y + dy), text, font=font, fill=oc)
    draw.text((x, y), text, font=font, fill=fc)


def _load_ui(theme_dir: Path, name: str) -> Image.Image:
    p = theme_dir / name
    if not p.is_file():
        raise FileNotFoundError(p)
    return Image.open(p).convert("RGBA")


def _paste(canvas: Image.Image, layer: Image.Image, x: int, y: int) -> None:
    canvas.alpha_composite(layer, (int(x), int(y)))


def _cover_bg(path: Path, tw: int = W, th: int = H) -> Image.Image:
    bg = Image.open(path).convert("RGB")
    bw, bh = bg.size
    scale = max(tw / bw, th / bh)
    nw, nh = int(bw * scale), int(bh * scale)
    bg = bg.resize((nw, nh), Image.Resampling.LANCZOS)
    x0 = (nw - tw) // 2
    y0 = (nh - th) // 2
    return bg.crop((x0, y0, x0 + tw, y0 + th))


def _place_sprite(
    canvas: Image.Image,
    sprite_path: Path,
    x: int = 72,
    y_bottom: int = H,
    max_h: int = 920,
) -> None:
    if not sprite_path.is_file():
        return
    sp = Image.open(sprite_path).convert("RGBA")
    sw, sh = sp.size
    if sh > max_h:
        scale = max_h / sh
        sp = sp.resize((int(sw * scale), max_h), Image.Resampling.LANCZOS)
        sw, sh = sp.size
    _paste(canvas, sp, x, y_bottom - sh)


def _place_sprite_galcs(
    canvas: Image.Image,
    sprite_path: Path,
    *,
    zoom: float,
    xpos: float = 0.48,
    xanchor: float = 0.5,
    y_bottom: int = H,
) -> None:
    """对齐 Ren'Py：Transform(zoom) + Position(xpos, xanchor)，底对齐 yalign 1.0。"""
    if not sprite_path.is_file():
        return
    sp = Image.open(sprite_path).convert("RGBA")
    sw, sh = sp.size
    nw, nh = max(1, int(sw * zoom)), max(1, int(sh * zoom))
    if (nw, nh) != (sw, sh):
        sp = sp.resize((nw, nh), Image.Resampling.LANCZOS)
    x = int(W * xpos - nw * xanchor)
    _paste(canvas, sp, x, y_bottom - nh)


def _draw_multiline(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font,
    fill: str,
    line_spacing: int = 12,
    outline: bool = True,
    outline_color: str = "#101820",
    outline_w: int = 2,
) -> None:
    x, y, x1, y1 = box
    lines = text.split("\n")
    cy = y
    for line in lines:
        if outline:
            _text_outline(
                draw, (x, cy), line, font, fill, outline=outline_color, ow=outline_w, enabled=True
            )
        else:
            draw.text((x, cy), line, font=font, fill=_hex_rgb(fill))
        bb = draw.textbbox((x, cy), line, font=font)
        cy += bb[3] - bb[1] + line_spacing
        if cy > y1:
            break


def resolve_bg(name: str | None) -> Path | None:
    if not name or name.lower() in ("none", "black"):
        return None
    if Path(name).is_file():
        return Path(name)
    stem = name if name.startswith("BG_") else f"BG_{name}"
    for pat in (f"{stem}.png", f"{stem}_*.png"):
        hits = sorted(BG_DIR.glob(pat))
        if hits:
            return hits[0]
    direct = BG_DIR / f"{stem}.png"
    return direct if direct.is_file() else None


def _draw_choices(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    ui: Path,
    cfg: dict,
    font_profile: SayFontProfile | None = None,
) -> None:
    """屏中选项 vbox（对齐 choice screen yalign 0.5）。"""
    cw, ch = cfg["choice_box"]
    spacing = cfg["choice_spacing"]
    if font_profile:
        text_sz = font_profile.choice_size
        font = _font_profile(font_profile, text_sz)
        choice_fill = font_profile.choice_color
        ow = font_profile.outline_w
        ocolor = font_profile.outline
        use_o = font_profile.use_outline
    else:
        text_sz = cfg.get("choice_text_size", 26)
        font = _font(text_sz)
        choice_fill = "#ffffff"
        ow, ocolor, use_o = 2, "#101820", True

    n = len(SAMPLE_CHOICES)
    total_h = ch * n + spacing * (n - 1)
    y = int(H * 0.5 - total_h / 2)
    cx = (W - cw) // 2

    for caption, st in SAMPLE_CHOICES:
        fname = f"UI_DS_choice_{st}.png"
        btn = _load_ui(ui, fname)
        if btn.size != (cw, ch):
            btn = btn.resize((cw, ch), Image.Resampling.LANCZOS)
        _paste(canvas, btn, cx, y)
        bb = draw.textbbox((0, 0), caption, font=font)
        tw, th = bb[2] - bb[0], bb[3] - bb[1]
        _text_outline(
            draw,
            (cx + (cw - tw) // 2, y + (ch - th) // 2),
            caption,
            font,
            choice_fill,
            outline=ocolor,
            ow=ow,
            enabled=use_o,
        )
        y += ch + spacing


def _center_text_on_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    text: str,
    font,
    fill: str,
    *,
    outline: str = "#101820",
    ow: int = 2,
    enabled: bool = True,
) -> None:
    x0, y0, x1, y1 = box
    bb = draw.textbbox((0, 0), text, font=font)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    x = x0 + (x1 - x0 - tw) // 2
    y = y0 + (y1 - y0 - th) // 2
    _text_outline(draw, (x, y), text, font, fill, outline=outline, ow=ow, enabled=enabled)


def _nameplate_pos(cfg: dict, layout: str, role: str | None) -> tuple[int, int]:
    if layout == "left_slot":
        key = "nameplate_npc" if role == "npc" else "nameplate_hero"
        return cfg[key]
    return cfg["nameplate"]


def _draw_who_on_nameplate(
    canvas: Image.Image,
    ui: Path,
    nx: int,
    ny: int,
    who: str,
    font,
    *,
    fill: str = "#FF70A8",
    outline: str = "#FFFFFF",
    ow: int = 2,
    enabled: bool = True,
) -> None:
    """姓名叠在铭牌内（最后绘制，保证在条带之上）。"""
    np_img = _load_ui(ui, "UI_DS_nameplate.png")
    x0 = nx + 18
    x1 = nx + np_img.width - 10
    draw = ImageDraw.Draw(canvas)
    _center_text_on_box(
        draw,
        (x0, ny, x1, ny + np_img.height),
        who,
        font,
        fill,
        outline=outline,
        ow=ow,
        enabled=enabled,
    )


def build_frame(
    *,
    theme: str,
    layout: str,
    mode: str,
    bg: Path | None,
    sprite: Path,
    who: str | None,
    what: str,
    show_choices: bool = False,
    font_profile: SayFontProfile | None = None,
    sprite_zoom: float | None = None,
    sprite_xpos: float = 0.48,
    sprite_xanchor: float = 0.5,
    speak_role: str | None = None,
    side_sprite: Path | None = None,
) -> Image.Image:
    ui = THEME_DIRS[theme]
    if layout == "left_slot":
        cfg = LAYOUT_LEFT_SLOT
    elif layout == "galcs":
        cfg = LAYOUT_GALCS
    else:
        cfg = LAYOUT_SPEC
    accent = "#FF70A8" if theme == "pink" else "#41B9FF"

    if bg is None or mode == "black":
        base = Image.new("RGB", (W, H), (0, 0, 0))
        canvas = base.convert("RGBA")
    else:
        canvas = _cover_bg(bg).convert("RGBA")

    if mode != "black" and sprite.is_file():
        if sprite_zoom is not None:
            _place_sprite_galcs(
                canvas,
                sprite,
                zoom=sprite_zoom,
                xpos=sprite_xpos,
                xanchor=sprite_xanchor,
            )
        else:
            _place_sprite(canvas, sprite)

    draw_say = mode not in ("choice",)
    draw_choices = show_choices or mode == "choice"

    if draw_say:
        use_nvl_bar = mode == "narration" or not who
        if layout == "left_slot":
            role_probe = speak_role
            if role_probe is None:
                role_probe = "narration" if not who else ("npc" if side_sprite and side_sprite.is_file() else "hero")
            use_nvl_bar = role_probe == "narration"
        bar_name = "UI_DS_bar_narration.png" if use_nvl_bar else "UI_DS_bar_dialogue.png"
        bar = _load_ui(ui, bar_name)
        _paste(canvas, bar, (W - bar.width) // 2, cfg["bar_y"])

    draw = ImageDraw.Draw(canvas)

    if draw_say and layout == "spec" and mode not in ("black",) and who:
        qbar = _load_ui(ui, "UI_DS_quick_bar.png")
        _paste(canvas, qbar, (W - qbar.width) // 2, cfg["quick_bar_y"])

    role = speak_role
    if layout == "left_slot" and role is None:
        if not who or mode in ("narration",):
            role = "narration"
        elif side_sprite and side_sprite.is_file():
            role = "npc"
        else:
            role = "hero"

    if draw_say and layout == "left_slot" and role == "npc" and side_sprite and side_sprite.is_file():
        sx, y_bot, max_sh = cfg["side"]
        _place_sprite(canvas, side_sprite, x=sx, y_bottom=y_bot, max_h=max_sh)

    np_pos: tuple[int, int] | None = None
    if draw_say and who and mode not in ("black", "narration"):
        np_img = _load_ui(ui, "UI_DS_nameplate.png")
        nx, ny = _nameplate_pos(cfg, layout, role)
        np_pos = (nx, ny)
        _paste(canvas, np_img, nx, ny)
        if layout == "spec":
            voice = _load_ui(ui, "UI_DS_say_voice_default.png")
            vx, vy = cfg["voice"]
            _paste(canvas, voice, vx, vy)

    if draw_say and what:
        if layout == "left_slot":
            slot_key = {"hero": "hero", "npc": "npc", "narration": "nvl"}.get(role or "hero", "hero")
            tx, ty, tw, th = cfg[f"text_box_{slot_key}"]
        else:
            tx, ty, tw, th = cfg["text_box"]
        if font_profile:
            who_sz = font_profile.who_size
            what_sz = font_profile.what_size
            who_c = font_profile.who_color
            what_c = font_profile.what_color
            who_f = _font_profile(font_profile, who_sz, bold=True)
            what_f = _font_profile(font_profile, what_sz)
            ocolor = font_profile.outline
            ow = font_profile.outline_w
            use_o = font_profile.use_outline
            lsp = font_profile.line_spacing
        else:
            who_sz = cfg["who_size"]
            what_sz = cfg["what_size"]
            who_c = accent if theme == "pink" else cfg["who_color"]
            what_c = cfg["what_color"]
            who_f = _font(who_sz, bold=True)
            what_f = _font(what_sz)
            ocolor, ow, use_o, lsp = "#1a1020", 2, True, 12

        if who:
            _text_outline(
                draw,
                (tx, ty),
                who,
                who_f,
                who_c,
                outline=ocolor,
                ow=ow,
                enabled=use_o,
            )
            ty += who_sz + 28

        _draw_multiline(
            draw,
            (tx, ty, tx + tw, ty + th),
            what,
            what_f,
            what_c,
            line_spacing=lsp,
            outline=use_o,
            outline_color=ocolor,
            outline_w=ow,
        )

    if draw_say and mode not in ("black", "narration"):
        qx, qy = cfg["quick_origin"]
        for i, icon_name in enumerate(cfg["quick_icons"]):
            ic = _load_ui(ui, icon_name)
            _paste(canvas, ic, qx + i * (ic.width + cfg["quick_spacing"]), qy)

    # 选项叠在最上层（对齐 choice screen zorder）
    if draw_choices:
        _draw_choices(canvas, draw, ui, cfg, font_profile)

    return canvas.convert("RGB")


def _label_bar(img: Image.Image, title: str, sub: str) -> Image.Image:
    pad = 36
    bar_h = 72
    out = Image.new("RGB", (img.width, img.height + bar_h + pad), (248, 249, 252))
    out.paste(img, (0, 0))
    d = ImageDraw.Draw(out)
    d.text((24, img.height + 12), title, fill=(45, 55, 75), font=_font(22, bold=True))
    d.text((24, img.height + 40), sub, fill=(100, 110, 130), font=_font(15))
    return out


def build_sheet(theme: str = "pink", layout: str = "galcs") -> Image.Image:
    bg_class = resolve_bg("BG_02_classroom_sunset")
    bg_roof = resolve_bg("BG_04_rooftop_sunset_golden")
    panels = [
        (
            build_frame(
                theme=theme,
                layout=layout,
                mode="say",
                bg=bg_class,
                sprite=SPRITE_DEFAULT,
                who=SAMPLE_WHO,
                what=SAMPLE_WHAT,
                show_choices=True,
            ),
            "对话+选项 · 教室夕阳",
            f"{theme} / {layout} · 底栏+屏中三选项",
        ),
        (
            build_frame(
                theme=theme,
                layout=layout,
                mode="say",
                bg=None,
                sprite=SPRITE_DEFAULT,
                who=SAMPLE_WHO,
                what=SAMPLE_WHAT,
                show_choices=True,
            ),
            "对话+选项 · 纯黑底",
            "检查选项/底栏在黑场表现",
        ),
        (
            build_frame(
                theme=theme,
                layout=layout,
                mode="choice",
                bg=bg_roof or bg_class,
                sprite=SPRITE_DEFAULT,
                who=None,
                what="",
                show_choices=True,
            ),
            "仅选项 · 天台夕阳",
            "无底栏 · 中间 hover · 浮岛上亮下淡",
        ),
        (
            build_frame(
                theme=theme,
                layout=layout,
                mode="narration",
                bg=bg_class,
                sprite=SPRITE_DEFAULT,
                who=None,
                what="（旁白）雨停之后，走廊里只剩下球鞋摩擦地面的声音。",
            ),
            "旁白 · 无姓名",
            "bar_narration",
        ),
    ]
    gap = 24
    pw, ph = W, H
    sheet = Image.new("RGB", (pw * 2 + gap, ph * 2 + gap + 90), (235, 238, 245))
    d = ImageDraw.Draw(sheet)
    d.text((gap, 8), "GAL Say 屏合成预览（背景+立绘+UI）", fill=(45, 55, 75), font=_font(26, bold=True))
    d.text(
        (gap, 42),
        f"生成: build_say_screen_preview.py --sheet  ·  主题={theme}  布局={layout}",
        fill=(100, 110, 130),
        font=_font(14),
    )
    positions = [(0, 90), (pw + gap, 90), (0, 90 + ph + gap), (pw + gap, 90 + ph + gap)]
    for (img, title, sub), (ox, oy) in zip(panels, positions):
        tile = _label_bar(img, title, sub)
        sheet.paste(tile, (ox, oy))
    return sheet


def build_left_slot_sheet(theme: str = "pink") -> Image.Image:
    """MO 式左侧槽：主角 / 角色+side / 旁白 三态竖排。"""
    bg = resolve_bg("BG_02_classroom_sunset")
    what_hero = "但我知道。"
    what_nvl = "雨停之后，走廊里只剩下球鞋摩擦地面的声音。"
    panels = [
        (
            build_frame(
                theme=theme,
                layout="left_slot",
                mode="say",
                bg=bg,
                sprite=GALCS_LINDAO_NORMAL,
                sprite_zoom=0.85,
                who=SAMPLE_WHO,
                what=what_hero,
                speak_role="hero",
            ),
            "① 主角 · 仅姓名条",
            f"nameplate {NAMEPLATE_W}×{NAMEPLATE_H} · bar {BAR_H}px · 无 side",
        ),
        (
            build_frame(
                theme=theme,
                layout="left_slot",
                mode="say",
                bg=bg,
                sprite=GALCS_LINDAO_NORMAL,
                sprite_zoom=0.85,
                who=SAMPLE_WHO,
                what=what_hero,
                speak_role="npc",
                side_sprite=SIDE_DEFAULT,
            ),
            "② 角色 · side + 姓名 + 全屏立绘",
            "side 在底栏槽内 · 不隐藏全屏立绘",
        ),
        (
            build_frame(
                theme=theme,
                layout="left_slot",
                mode="narration",
                bg=bg,
                sprite=GALCS_LINDAO_NORMAL,
                sprite_zoom=0.85,
                who=None,
                what=what_nvl,
                speak_role="narration",
            ),
            "③ 旁白 · 左侧空",
            "bar_narration · 无 nameplate",
        ),
    ]
    gap = 20
    header_h = 78
    body_h = sum(H + 72 + 36 for _ in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (W, header_h + body_h), (235, 238, 245))
    d = ImageDraw.Draw(sheet)
    d.text(
        (24, 10),
        "左侧槽 Say UI · 三态预览（底栏 320 + 斜角姓名条）",
        fill=(45, 55, 75),
        font=_font(24, bold=True),
    )
    d.text(
        (24, 44),
        f"主题={theme} · build_ui_anime_say.py 后自动生成 · 叠层 layout=left_slot",
        fill=(100, 110, 130),
        font=_font(14),
    )
    y = header_h
    for img, title, sub in panels:
        tile = _label_bar(img, title, sub)
        sheet.paste(tile, (0, y))
        y += tile.height + gap
    return sheet


def publish_left_slot_previews(
    themes: list[str],
    *,
    archive: bool = True,
    triggered_by: str = "build_ui_anime_say.py",
) -> list[Path]:
    if not themes:
        return []
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    PREVIEW_LATEST.mkdir(parents=True, exist_ok=True)
    hist_dir = PREVIEW_HISTORY / ts if archive else None
    if hist_dir:
        hist_dir.mkdir(parents=True, exist_ok=True)
    saved: list[Path] = []
    for theme in themes:
        img = build_left_slot_sheet(theme)
        name = f"UI_LEFT_SLOT_PREVIEW_{theme}.png"
        for folder in (PREVIEW_LATEST, hist_dir) if hist_dir else (PREVIEW_LATEST,):
            out = folder / name
            img.save(out, "PNG", optimize=True)
            saved.append(out)
            print("Left-slot preview saved:", out, img.size)
    return saved


def build_sprite_zoom_sheet(
    *,
    theme: str = "pink",
    layout: str = "galcs",
    bg_name: str = "BG_02_classroom_sunset",
    sprite: Path = GALCS_LINDAO_NORMAL,
    zooms: tuple[float, ...] = (0.65, 0.75, 0.80),
    who: str = SAMPLE_WHO,
    what: str = "但我知道。",
) -> Image.Image:
    """竖排对比 GALCS 立绘 zoom（同背景、同 UI、同台词）。"""
    bg = resolve_bg(bg_name)
    if bg is None:
        raise FileNotFoundError(f"background not found: {bg_name}")

    labels: list[tuple[str, str]] = []
    for z in zooms:
        if z == 0.65:
            title = f"zoom={z:.2f}（GALCS 当前）"
        elif z in (0.75, 0.80):
            title = f"zoom={z:.2f}（建议试水）"
        else:
            title = f"zoom={z:.2f}"
        sw, sh = 800, 1200
        nw, nh = int(sw * z), int(sh * z)
        head_gap = max(0, H - nh)
        labels.append(
            (
                title,
                f"显示约 {nw}×{nh}px · LEFT xpos=0.48 · 头顶留白约 {head_gap * 100 // H}%",
            )
        )

    panels: list[Image.Image] = []
    for z, (title, sub) in zip(zooms, labels):
        frame = build_frame(
            theme=theme,
            layout=layout,
            mode="say",
            bg=bg,
            sprite=sprite,
            who=who,
            what=what,
            show_choices=False,
            sprite_zoom=z,
        )
        panels.append(_label_bar(frame, title, sub))

    gap = 20
    header_h = 78
    body_h = sum(p.height for p in panels) + gap * (len(panels) - 1)
    sheet = Image.new("RGB", (W, header_h + body_h), (235, 238, 245))
    d = ImageDraw.Draw(sheet)
    d.text(
        (24, 10),
        "立绘 zoom 对比 · 教室夕阳 + Say UI（GALCS 叠层规则）",
        fill=(45, 55, 75),
        font=_font(24, bold=True),
    )
    d.text(
        (24, 44),
        f"源图: {sprite.name} 800×1200  ·  build_say_screen_preview.py --sprite-zoom-sheet",
        fill=(100, 110, 130),
        font=_font(14),
    )
    y = header_h
    for tile in panels:
        sheet.paste(tile, (0, y))
        y += tile.height + gap
    return sheet


def publish_previews(
    themes: list[str],
    *,
    layout: str = "galcs",
    archive: bool = True,
    triggered_by: str = "build_ui_anime_say.py",
) -> list[Path]:
    """
    固定流程：UI 出一版 → 预览出一版。
    - previews/latest/  始终为当前最新
    - previews/history/<时间戳>/  每次构建留档
    """
    if not themes:
        return []

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    PREVIEW_LATEST.mkdir(parents=True, exist_ok=True)
    hist_dir = PREVIEW_HISTORY / ts if archive else None
    if hist_dir:
        hist_dir.mkdir(parents=True, exist_ok=True)

    saved: list[Path] = []
    for theme in themes:
        img = build_sheet(theme, layout)
        name = f"UI_SAY_PREVIEW_sheet_{theme}_{layout}.png"
        for folder in (PREVIEW_LATEST, hist_dir) if hist_dir else (PREVIEW_LATEST,):
            out = folder / name
            img.save(out, "PNG", optimize=True)
            saved.append(out)
            print("Preview saved:", out, img.size)

    info_lines = [
        f"built_at={datetime.now().isoformat(timespec='seconds')}",
        f"themes={','.join(themes)}",
        f"layout={layout}",
        f"triggered_by={triggered_by}",
        f"history_dir={hist_dir.name if hist_dir else ''}",
    ]
    for folder in (PREVIEW_LATEST, hist_dir) if hist_dir else (PREVIEW_LATEST,):
        (folder / "BUILD_INFO.txt").write_text("\n".join(info_lines) + "\n", encoding="utf-8")

    return saved


def main(argv: list[str] | None = None) -> None:
    ap = argparse.ArgumentParser(description="合成 Say 屏实机感预览图")
    ap.add_argument("--theme", choices=("pink", "blue"), default="pink")
    ap.add_argument("--layout", choices=("galcs", "spec"), default="galcs")
    ap.add_argument(
        "--mode",
        choices=("say", "narration", "choice", "black"),
        default="say",
    )
    ap.add_argument(
        "--choices",
        action=argparse.BooleanOptionalAction,
        default=None,
        help="叠屏中选项（say/black 默认开，narration 默认关）",
    )
    ap.add_argument("--bg", default="BG_02_classroom_sunset", help="BG_xx 名、路径或 black")
    ap.add_argument("--sprite", type=Path, default=None)
    ap.add_argument(
        "--galcs-sprite",
        action="store_true",
        help="使用 GALCS 林晚棠 LWT_01_normal（配合 --sprite-zoom）",
    )
    ap.add_argument(
        "--sprite-zoom",
        type=float,
        default=None,
        metavar="Z",
        help="Ren'Py zoom + LEFT 叠放；导出至 previews/latest/ 与 history/",
    )
    ap.add_argument("--who", default=SAMPLE_WHO)
    ap.add_argument("--what", default=SAMPLE_WHAT)
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--sheet", action="store_true", help="导出 2×2 对照拼图到 latest/ + history/")
    ap.add_argument(
        "--sprite-zoom-sheet",
        action="store_true",
        help="导出立绘 zoom 0.65/0.75/0.80 竖排对比（GALCS 立绘+LEFT）",
    )
    ap.add_argument(
        "--publish",
        nargs="*",
        metavar="THEME",
        help="仅发布预览（默认 pink；可传 pink blue）",
    )
    args = ap.parse_args(argv)

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    if args.publish is not None:
        themes = args.publish if args.publish else ["pink"]
        publish_previews(themes, layout=args.layout, triggered_by="build_say_screen_preview.py --publish")
        return

    if args.sheet:
        publish_previews([args.theme], layout=args.layout, triggered_by="build_say_screen_preview.py --sheet")
        return

    if args.sprite_zoom_sheet:
        img = build_sprite_zoom_sheet(theme=args.theme, layout=args.layout)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        PREVIEW_LATEST.mkdir(parents=True, exist_ok=True)
        name = f"UI_SPRITE_ZOOM_PREVIEW_{args.theme}_{args.layout}.png"
        out_latest = PREVIEW_LATEST / name
        img.save(out_latest, "PNG", optimize=True)
        hist = PREVIEW_HISTORY / ts
        hist.mkdir(parents=True, exist_ok=True)
        out_hist = hist / name
        img.save(out_hist, "PNG", optimize=True)
        print("Saved:", out_latest, img.size)
        print("Saved:", out_hist, img.size)
        return

    if args.sprite is not None:
        sprite_path = args.sprite
    elif args.galcs_sprite or args.sprite_zoom is not None:
        sprite_path = GALCS_LINDAO_NORMAL
    else:
        sprite_path = SPRITE_DEFAULT

    bg_path = resolve_bg(args.bg) if args.mode != "black" else None
    if (
        args.mode != "black"
        and args.bg
        and args.bg.lower() not in ("black", "none")
        and bg_path is None
    ):
        print("Warning: background not found:", args.bg, file=sys.stderr)

    who = None if args.mode in ("narration", "choice") else args.who
    what = args.what if args.mode not in ("choice",) else ""

    if args.choices is None:
        show_choices = args.mode in ("say", "black", "choice")
    else:
        show_choices = args.choices

    if args.sprite_zoom is not None and args.mode == "say" and show_choices:
        show_choices = False

    img = build_frame(
        theme=args.theme,
        layout=args.layout,
        mode=args.mode,
        bg=bg_path,
        sprite=sprite_path,
        who=who,
        what=what,
        show_choices=show_choices,
        sprite_zoom=args.sprite_zoom,
    )

    if args.sprite_zoom is not None:
        z_tag = f"{args.sprite_zoom:.2f}".replace(".", "")
        bg_tag = Path(args.bg).stem if bg_path else "black"
        name = f"UI_SPRITE_ZOOM_{z_tag}_{args.theme}_{args.layout}_{bg_tag}.png"
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        PREVIEW_LATEST.mkdir(parents=True, exist_ok=True)
        outs = [PREVIEW_LATEST / name]
        hist = PREVIEW_HISTORY / ts
        hist.mkdir(parents=True, exist_ok=True)
        outs.append(hist / name)
        if args.out:
            outs.insert(0, args.out)
        for out in outs:
            out.parent.mkdir(parents=True, exist_ok=True)
            img.save(out, "PNG", optimize=True)
            print("Saved:", out, img.size)
        return

    if args.out:
        out = args.out
    else:
        bg_tag = Path(args.bg).stem if bg_path else "black"
        out = PREVIEW_DIR / f"UI_SAY_PREVIEW_{args.theme}_{args.layout}_{args.mode}_{bg_tag}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG", optimize=True)
    print("Saved:", out, img.size)


if __name__ == "__main__":
    main()
