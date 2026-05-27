# GAL 项目 · 官方 UI 配色定调（Locked）

> **定稿（进游戏）**：**`anime_style_blue/`** 晴空蓝全套 · Lock `say-ui-final-blue-20260527`  
> **备选**：`anime_style/` 粉套（底栏/选项无色玻璃 + 樱粉快捷/姓名条）

---

## 1. 使用规则

| 规则 | 说明 |
|------|------|
| 生成 | `python scripts/build_ui_anime_say.py pink` / `blue` / `all` |
| 复制 | 只从 `美术资源初稿/UI/` 手动复制进 GALCS |

---

## 2. 粉套 · 拆分配色

### 2.1 无色玻璃（仅这 5 张 · 叠 BG/立绘）

| 文件 | 函数 |
|------|------|
| `UI_DS_bar_dialogue.png` | `bar_colorless()` |
| `UI_DS_bar_narration.png` | `bar_colorless()` |
| `UI_DS_choice_normal/hover/selected.png` | `choice_colorless()` |

- 底栏：冷雾 RGB + 顶缘高光 + 正文区略实（黑屏/彩景观感拉近）  
- 选项：**浮岛 + 上亮下淡**（岛 80%×62%、顶 α≈0.28→底 α≈0.07；numpy 描边，无矢量顶弧），三态靠渐变/外晕区分  

### 2.2 樱粉（其余 20 张）

快捷条、8×快捷图标、语音钮、姓名左条 → `THEMES["pink"]` 樱粉 Token（`#FF70A8` / `#FFB2C8` 等）。

```renpy
define gui.accent_color = "#FF70A8"
define gui.name_text_color = "#FF70A8"
# 选项/底栏文字建议白字+描边（与无色 PNG 一致）
```

---

## 3. 晴空蓝 · `anime_style_blue/`（**定稿**）

| 项 | 说明 |
|----|------|
| 底栏 | `bar_anime()` · 1920×**280** · 顶直角 · **无左右描边** |
| 快捷/姓名 | 天蓝 Token · 姓名条 12×44 左竖条 |
| 选项 | 浮岛 + 上亮下淡 · `choice_island_blue()` |

```renpy
define gui.accent_color = "#41B9FF"
define gui.name_text_color = "#41B9FF"
```

---

*Theme lock ID: `say-ui-final-blue-20260527`*
