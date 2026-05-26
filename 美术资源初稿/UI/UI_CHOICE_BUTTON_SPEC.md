# 选项按钮 · anime_style（当前定稿）

> **2026-05-26 封版** · 粉套无色浮岛 / 蓝套同形天蓝雾  
> 旧版 `UI_choice_*.png`（800×90 橙框系）见文末；新资源在 `anime_style*/UI_DS_choice_*.png`。

---

## 规格

| 项目 | 值 |
|------|-----|
| 资源画布 | **780 × 76** px（RGBA） |
| Ren'Py（GALCS） | `xsize 800` · `ysize 90`（会横向略拉宽） |
| 形状 | 浮岛 **80%×62%**，上亮下淡渐变 |
| 圆角 | 药丸（`radius = 岛高/2`） |

## 交付文件（每主题 3 张）

| 状态 | 文件 |
|------|------|
| 普通 | `UI_DS_choice_normal.png` |
| 悬停 | `UI_DS_choice_hover.png` |
| 选中 | `UI_DS_choice_selected.png` |

路径：

- 樱粉：`anime_style/`
- 晴空蓝：`anime_style_blue/`

## 重建

```powershell
cd J:\项目\GAL\美术资源初稿\UI\scripts
python build_ui_anime_say.py pink   # 或 blue / all
```

自动生成 UI 预览：`previews/latest/UI_SAY_PREVIEW_sheet_*_galcs.png`

## 实现要点（改脚本时必读）

- 函数：`_choice_island_render()` · `_choice_island_finish()` · `soft_island_mask()`
- **禁止** 恢复：矢量顶弧、双高光椭圆、整条灰雾底
- **禁止** 缩小后仅用硬 `floating_island_mask` 裁切（会糊满画布）

详见 `UI_AGENT_RULES.md` §4。

## Ren'Py 示例（GALCS 现状）

```renpy
# 资产 780×76，屏幕 800×90
background "images/UI/UI_choice_normal.png"
hover_background "images/UI/UI_choice_hover.png"
text caption:
    size 26   # 预览建议可试 28
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]
```

文案颜色与描边见 `UI_AGENT_RULES.md` §7。

---

## 附录 · 旧版 UI_02 橙框按钮（已 superseded）

| 项目 | 值 |
|------|-----|
| 画布 | 800 × 90 |
| 脚本 | `build_choice_buttons.py` |
| 文件 | `UI/UI_choice_*.png` |

仅作历史参考，与当前 Say 屏 `UI_DS_*` 不是同一套。
