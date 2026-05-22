# UI_02 · 选择菜单按钮

> 与 `UI_02_dialogue_minimal` 同系：深色条带 RGB(32,42,72) + 暖橙强调色  
> **2026-05-21**

---

## 规格

| 项目 | 值 |
|------|-----|
| 单按钮画布 | **800 × 90** px |
| 格式 | PNG **RGBA** 透明底 |
| 圆角 | 约 14px |
| 可裁剪 | 宽度可按 Ren'Py `xsize` 缩放，建议保持比例 |

## 交付文件

| 状态 | 文件 |
|------|------|
| 普通 | `UI_choice_normal.png` |
| 悬停 | `UI_choice_hover.png`（橙框 + 外光晕） |
| 选中 | `UI_choice_selected.png`（淡橙填充 + 橙边） |

路径：`J:\项目\GAL\美术资源初稿\UI\`

## 重建

```powershell
python J:\项目\GAL\美术资源初稿\UI\scripts\build_choice_buttons.py
```

## Ren'Py 示例

```renpy
image choice normal = "UI/UI_choice_normal.png"
image choice hover = "UI/UI_choice_hover.png"
image choice selected = "UI/UI_choice_selected.png"

# 或使用 gui 绘制减少素材依赖：
# define gui.choice_button_borders = Borders(14, 14, 14, 14)
# define gui.choice_button_tile = False
```

```renpy
screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12
        for i in items:
            textbutton i.caption:
                action i.action
                idle_background "UI/UI_choice_normal.png"
                hover_background "UI/UI_choice_hover.png"
                selected_idle_background "UI/UI_choice_selected.png"
                selected_hover_background "UI/UI_choice_selected.png"
                xsize 800
                ysize 90
```

---

*与对话条 `DIALOGUE_UI_MINIMAL_SPEC.md` 配套使用。*
