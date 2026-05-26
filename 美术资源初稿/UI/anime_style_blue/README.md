# UI · 二次元卡通风 · 晴空蓝定调（anime_style_blue）

与 `anime_style/`（樱粉）**文件名相同、尺寸相同**，仅配色不同，可整目录切换。  
**官方配色**：`../UI_THEME_COLORS.md` · **布局说明图**：`../UI_SAY_LAYOUT_GUIDE.md`

## 配色概要

| 用途 | Hex（定调） |
|------|-------------|
| 强调 / 默认外圈 | `#41B9FF` |
| Hover 外圈锚点 | `#73DCFF` |
| 描边 | `#5AC8FF` |

## 生成

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say.py" blue
# 同步生成预览 → ../previews/latest/UI_SAY_PREVIEW_sheet_blue_galcs.png
```

粉色版：

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say.py" pink
```

## Ren'Py

```renpy
define ui_folder = "UI/anime_style_blue/"
add ui_folder + "UI_DS_bar_dialogue.png" xalign 0.5 yalign 1.0
```

规格见 `UI_SPEC.md`（1920×360 底栏、780×76 选项等）。
