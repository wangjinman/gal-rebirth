#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Say 屏 · 字体方案对比预览（背景 + 立绘 + UI + 文案）。

用法:
  python build_say_font_preview.py
  python build_say_font_preview.py --theme blue --bg BG_02
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw

UI_ROOT = Path(r"J:\项目\GAL\美术资源初稿\UI")
PREVIEW_LATEST = UI_ROOT / "previews" / "latest"
PREVIEW_HISTORY = UI_ROOT / "previews" / "history" / datetime.now().strftime("%Y%m%d_%H%M%S")
GALCS_FONTS = Path(r"J:\项目\GAL\开发\RenPy项目\GALCS\game\fonts")
WIN_FONTS = Path(r"C:\Windows\Fonts")

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from build_say_screen_preview import (  # noqa: E402
    SAMPLE_WHO,
    SAMPLE_WHAT,
    SPRITE_DEFAULT,
    W,
    H,
    SayFontProfile,
    _font,
    _label_bar,
    build_frame,
    resolve_bg,
)


def font_presets(theme: str = "pink") -> list[SayFontProfile]:
    simhei = GALCS_FONTS / "simhei.ttf"
    msyh = WIN_FONTS / "msyh.ttc"
    msyhbd = WIN_FONTS / "msyhbd.ttc"
    source = GALCS_FONTS / "SourceHanSansLite.ttf"
    who_accent = "#FF70A8" if theme == "pink" else "#41B9FF"

    presets = [
        SayFontProfile(
            id="simhei_old",
            title="① 黑体 · 当前游戏",
            subtitle="simhei · #2c3e50 深字无描边（对照）",
            regular=simhei,
            who_color="#2c3e50",
            what_color="#2c3e50",
            use_outline=False,
        ),
        SayFontProfile(
            id="simhei_glass",
            title="② 黑体 · 玻璃推荐",
            subtitle="simhei · 浅字 + 主题名色 + 2px 描边",
            regular=simhei,
            who_color=who_accent,
            what_color="#E8ECF2",
            use_outline=True,
        ),
        SayFontProfile(
            id="msyh_glass",
            title="③ 微软雅黑 · 玻璃推荐",
            subtitle="msyh / msyhbd · 浅字描边",
            regular=msyh,
            bold=msyhbd,
            who_color=who_accent,
            what_color="#E8ECF2",
            use_outline=True,
        ),
    ]
    if source.is_file():
        presets.append(
            SayFontProfile(
                id="source_glass",
                title="④ 思源黑 Lite",
                subtitle="SourceHanSansLite · 浅字描边",
                regular=source,
                who_color=who_accent,
                what_color="#E8ECF2",
                use_outline=True,
            )
        )
    else:
        presets.append(
            SayFontProfile(
                id="msyhl_glass",
                title="④ 微软雅黑 Light",
                subtitle="msyhl · 浅字描边（无思源时替补）",
                regular=WIN_FONTS / "msyhl.ttc",
                bold=msyh,
                who_color=who_accent,
                what_color="#E8ECF2",
                use_outline=True,
            )
        )

    ok: list[SayFontProfile] = []
    for p in presets:
        if p.regular.is_file():
            ok.append(p)
        else:
            print("Skip font preset (missing):", p.id, p.regular, file=sys.stderr)
    return ok


def build_font_sheet(
    *,
    theme: str = "pink",
    layout: str = "galcs",
    bg_name: str = "BG_02_classroom_sunset",
    black_panel: bool = True,
) -> Image.Image:
    bg = resolve_bg(bg_name)
    profiles = font_presets(theme)
    panels: list[tuple[Image.Image, str, str]] = []

    for p in profiles:
        img = build_frame(
            theme=theme,
            layout=layout,
            mode="say",
            bg=bg,
            sprite=SPRITE_DEFAULT,
            who=SAMPLE_WHO,
            what=SAMPLE_WHAT,
            show_choices=True,
            font_profile=p,
        )
        panels.append((img, p.title, p.subtitle))

    if black_panel and len(panels) < 4:
        p = next(x for x in profiles if x.id == "simhei_glass")
        img = build_frame(
            theme=theme,
            layout=layout,
            mode="say",
            bg=None,
            sprite=SPRITE_DEFAULT,
            who=SAMPLE_WHO,
            what=SAMPLE_WHAT,
            show_choices=True,
            font_profile=p,
        )
        panels.append((img, "⑤ 黑底 · 推荐字体验证", p.subtitle + " · 黑场"))

    while len(panels) < 4:
        panels.append(panels[-1])

    gap = 24
    cols, rows = 2, 2
    pw, ph = W, H
    header = 88
    sheet = Image.new("RGB", (pw * cols + gap, ph * rows + gap + header), (235, 238, 245))
    d = ImageDraw.Draw(sheet)
    accent = "#FF70A8" if theme == "pink" else "#41B9FF"
    d.text((gap, 10), "GAL Say 屏 · 字体方案对比", fill=(45, 55, 75), font=_font(26, bold=True))
    d.text(
        (gap, 44),
        f"UI={theme} · 布局={layout} · 背景={bg_name} · 生成=build_say_font_preview.py",
        fill=(100, 110, 130),
        font=_font(14),
    )
    d.text((gap, 66), f"强调色示例 {accent}", fill=accent, font=_font(14))

    positions = [
        (0, header),
        (pw + gap, header),
        (0, header + ph + gap),
        (pw + gap, header + ph + gap),
    ]
    for (img, title, sub), (ox, oy) in zip(panels[:4], positions):
        sheet.paste(_label_bar(img, title, sub), (ox, oy))
    return sheet


def publish(img: Image.Image, theme: str, layout: str) -> list[Path]:
    PREVIEW_LATEST.mkdir(parents=True, exist_ok=True)
    PREVIEW_HISTORY.mkdir(parents=True, exist_ok=True)
    name = f"UI_SAY_FONT_PREVIEW_sheet_{theme}_{layout}.png"
    saved = []
    for folder in (PREVIEW_LATEST, PREVIEW_HISTORY):
        out = folder / name
        img.save(out, "PNG", optimize=True)
        saved.append(out)
        print("Saved:", out, img.size)
    (PREVIEW_LATEST / "BUILD_INFO_FONTS.txt").write_text(
        f"built_at={datetime.now().isoformat(timespec='seconds')}\n"
        f"theme={theme}\nlayout={layout}\n",
        encoding="utf-8",
    )
    return saved


def main() -> None:
    ap = argparse.ArgumentParser(description="Say 屏字体对比预览")
    ap.add_argument("--theme", choices=("pink", "blue"), default="pink")
    ap.add_argument("--layout", choices=("galcs", "spec"), default="galcs")
    ap.add_argument("--bg", default="BG_02_classroom_sunset")
    ap.add_argument("--no-black", action="store_true", help="不追加黑底对照格")
    args = ap.parse_args()

    img = build_font_sheet(
        theme=args.theme,
        layout=args.layout,
        bg_name=args.bg,
        black_panel=not args.no_black,
    )
    publish(img, args.theme, args.layout)


if __name__ == "__main__":
    main()
