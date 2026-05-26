# UI 基准版（Baseline v1）

> **锁定日期**：2026-05-19（绘制逻辑）· **配色定调**：见 **`UI_THEME_COLORS.md`**（樱粉 + 晴空蓝，项目唯一官方双色）  
> **用户约定**：说 **「回复到基准版」** = 用 `build_ui_anime_say_baseline.py` 覆盖主脚本并重生成两套 PNG（含已定调配色）。  
> **状态**：二次元 say 全套 · 粉/蓝各 25 张 · baseline 脚本已同步为 v2（含 theme-lock）。

---

## 1. 基准版包含什么

| 项 | 说明 |
|----|------|
| 风格 | 二次元 / 卡通 · 粉奶油 & 天蓝两套主题 |
| 范围 | say 全套 25 张 `UI_DS_*` / 主题（见下表） |
| 不含 | 全屏 `_apply_top_gloss`、`_blend_white` 提亮、对话底栏星星 |
| 已含修复 | 顶圆角底栏、双层选项/姓名条、3× 超采样圆角、skip+2 / voice-4.5 图标偏移 |

### 输出目录

| 主题 | 路径 |
|------|------|
| 粉 | `J:\项目\GAL\美术资源初稿\UI\anime_style\` |
| 蓝 | `J:\项目\GAL\美术资源初稿\UI\anime_style_blue\` |

### 文件清单（每套 25 张）

`UI_DS_bar_dialogue.png` · `UI_DS_bar_narration.png` · `UI_DS_nameplate.png`  
`UI_DS_choice_{normal,hover,selected}.png`  
`UI_DS_quick_bar.png` · `UI_DS_quick_{auto,skip,hide,history,save,load,settings,exit}_{default,hover}.png`  
`UI_DS_say_voice_{default,hover}.png`

---

## 2. 冻结的脚本（勿改 baseline 文件）

| 文件 | 用途 |
|------|------|
| **`scripts/build_ui_anime_say_baseline.py`** | 基准生成逻辑只读归档 |
| `scripts/build_ui_anime_say.py` | 日常调优改这个；回退时从 baseline 覆盖 |

---

## 3. 一键恢复基准版

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\restore_ui_baseline.py"
```

或手动：

```powershell
copy /Y "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say_baseline.py" "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say.py"
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say.py" all
```

---

## 4. 基准配色 Token（THEMES）

### pink · `anime_style`

| Token | 值 |
|-------|-----|
| BAR_TOP / BOTTOM | (255,252,255) → (255,228,238) |
| BAR_NVL | (255,250,252) → (255,235,245) |
| INNER_CREAM | (255,242,248) |
| OUTLINE | (200,110,145) |
| ACCENT / HOVER | (255,105,140) / (255,150,175) |
| BAR_A dialogue / nvl | **0.78** / **0.65** |

### blue · `anime_style_blue`

| Token | 值 |
|-------|-----|
| BAR_TOP / BOTTOM | (248,252,255) → (210,228,255) |
| BAR_NVL | (250,253,255) → (225,238,252) |
| INNER_CREAM | (242,248,255) |
| OUTLINE | (85,125,185) |
| ACCENT / HOVER | (70,140,220) / (110,175,245) |

---

## 5. 基准绘制规则（调优时不要破坏 unless  intentional）

- 底栏：顶圆角 mask + 手绘顶边描边，**无**顶光泽叠层  
- 选项/姓名条：外圈实心描边 + 内底，**3×** 超采样缩小  
- 图标：48×48，hover 外圈模糊光晕 + 顶弧高光（α≈100），**不用** `_apply_top_gloss`  
- 图标偏移：`skip` +2.0，`voice` -4.5（设计稿单位）

---

## 6. 调优分支（基准之后）

在 `build_ui_anime_say.py` 上实验；满意再更新 `build_ui_anime_say_baseline.py` 升版为 v2。  
实验记录建议写在 `UI_TUNING_LOG.md`（可选新建）。

---

## 7. 关联文档

- `UI_SPEC.md` — 尺寸  
- `UI_ASSET_MAP_FULL.md` — 功能对标与进度  
- `UI_DESIGN_SYSTEM.md` — 极简 `UI/` 根目录 DS（另一套）  
- Skill：`renpy-galgame-ui` — Agent 工作流  

---

*基准版 ID：`baseline-v1-20260519`*
