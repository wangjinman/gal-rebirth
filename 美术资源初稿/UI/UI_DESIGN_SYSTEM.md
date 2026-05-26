# GAL 项目 · UI 设计系统（Design System v1）

> **状态**：2026-05-21 · **v1.1 浅色系**（Light）  
> **原则**：**立绘与底栏分离** · 一套 Token · Ren'Py `gui` 负责字，PNG 只负责「底」

---

## 1. 设计目标

| 目标 | 做法 |
|------|------|
| 统一 | 对话 / 旁白 / 选项共用颜色、圆角、透明度 |
| 轻盈 | 底栏 **360px**，顶缘渐隐透明 |
| 适配 Key 风 BG | 条带 **半透明暖白**，不抢立绘；亮场景可略提高 α |
| 可维护 | 单脚本 `build_ui_design_system.py` 重建全部 PNG |
| 可扩展 | 换角色只换 `show` 立绘，不换底栏图 |

---

## 2. Design Tokens

### 2.1 色彩（浅色系 · Light v1.1）

| Token | 值 | 用途 |
|-------|-----|------|
| `bar.bg` | RGB **(252, 250, 246)** 暖米白 · 峰值 α **~0.62** | 对话底栏 |
| `bar.bg.narration` | 同上 · 峰值 α **~0.50** | 旁白底栏（更透） |
| `bar.gradient` | **顶缘近透明 → 底缘渐浓**（`t^1.35`） | 叠在 BG 上自然融景 |
| `accent` | **#C97B35** | 强调、姓名、选项悬停（深一点保对比） |
| `accent.hover` | **#E8944A** | 选项悬停边框/光 |
| `accent.fill` | RGBA **(255, 210, 160, 0.55)** | 选项选中填充 |
| `text.primary` | **#3A4258** | 正文（深灰蓝，在浅色条上阅读） |
| `text.name` | **#B86A28** | 角色名 |
| `text.muted` | **#6B7589** | 旁白/次要 |
| `line.subtle` | RGBA **(255,255,255, 0.65)** | 顶缘高光 |
| `line.border` | RGBA **(50, 60, 80, 0.10)** | 底栏/按钮细描边 |
| `shadow` | RGBA **(40, 50, 70, 0.08)** | 轻阴影（底缘） |

### 2.2 尺寸与间距

> **完整规格表**（已交付实测 + 规划全模块宽×高）：见 **`UI_SPEC.md`**。  
> **官方双色**（樱粉 / 晴空蓝）：见 **`UI_THEME_COLORS.md`**（项目 UI 定调，仅此两套）。  
> **Say 屏布局说明图**（参考样张 × 已交付对照）：见 **`UI_SAY_LAYOUT_GUIDE.md`**。  
> **二次元 say 基准绘制**：见 **`UI_BASELINE.md`**；口令「回复到基准版」。

| Token | 值 |
|-------|-----|
| `screen` | **1920×1080** |
| `screen.w` | 1920 |
| `bar.size` | **1920×360**（对话/旁白底栏 PNG） |
| `bar.h` | **360** |
| `bar.pad.x` | 48 |
| `text.x.dialogue` | **400**（立绘区右侧起点） |
| `text.w.dialogue` | 1420 |
| `text.x.narration` | 360（居中栏左缘） |
| `text.w.narration` | 1200（宽约 62.5%） |
| `nameplate.size` | **320×44** |
| `portrait.x` | 72 |
| `portrait.yalign` | 1.0（脚底贴屏底） |
| `choice.size` | **780×76** |
| `choice.w` | **780** |
| `choice.h` | **76** |
| `choice.gap` | 14 |
| `radius.md` | **10** |

### 2.3 字体（Ren'Py `gui`，非 PNG）

| 角色 | 字号 | 字重 |
|------|------|------|
| 姓名 | 26 | 中等 |
| 正文 | 22 | 常规 |
| 旁白 | 22 | 常规，行距 1.38 |
| 选项 | 22 | 常规 |

推荐字体：思源黑体 / 微软雅黑 / 项目已嵌入字体。

---

## 3. 组件架构

```
┌────────────────────────────────── 1920 ──────────────────────────────────┐
│                         [ 场景 BG ]                                     │
│    ┌─────────┐                                                          │
│    │ 立绘    │  ← show bust/feather，x≈72, yalign 1.0（不在底栏 PNG 内） │
│    └─────────┘                                                          │
│  ┌─ 姓名条（gui frame 或 UI_DS_nameplate.png）──────────────────────────┐ │
│  │ 林晚棠                                                                 │ │
│  └──────────────────────────────────────────────────────────────────────┘ │
│  ┌─ UI_DS_bar_dialogue.png · 高 360 ────────────────────────────────────┐ │
│  │ 正文区 x≥400                                                           │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

**旁白**：无立绘 · `UI_DS_bar_narration.png` · 正文居中栏 1200px  
**选项**：屏幕中部 `vbox` · `UI_DS_choice_*.png` × 3

---

## 4. 交付文件清单

路径：`J:\项目\GAL\美术资源初稿\UI\`

**完整规划（跨项目复用）**：

| 文档 | 说明 |
|------|------|
| **`UI_SPEC.md`** | **宽×高规格书**（1920×360 等，单一事实来源） |
| `UI_ASSET_MAP_FULL.md` | 96 项参考包功能 → `UI_DS_*` 对标表（含进度） |
| `RENPY_UI_COMPLETE_CHECKLIST.md` | Ren'Py Gal 全量 UI 需求清单 |
| Cursor Skill `renpy-galgame-ui` | `~/.cursor/skills/renpy-galgame-ui/` |

| 文件 | 尺寸 (px) | 说明 |
|------|-----------|------|
| `UI_DS_bar_dialogue.png` | **1920×360** | 对话底栏，顶渐隐+左侧略重 |
| `UI_DS_bar_narration.png` | **1920×360** | 旁白底栏，更透对称 |
| `UI_DS_nameplate.png` | **320×44** | 姓名条底（可选，可用 gui 代替） |
| `UI_DS_choice_normal.png` | **780×76** | 选项·普通 |
| `UI_DS_choice_hover.png` | **780×76** | 选项·悬停 |
| `UI_DS_choice_selected.png` | **780×76** | 选项·选中 |

规划中的 P1–P3 尺寸见 `UI_SPEC.md` §4。

**二次元卡通风（say 全套第二版）**：`UI/anime_style/`，脚本 `scripts/build_ui_anime_say.py`，说明见 `anime_style/README.md`。

**旧版归档**（勿删）：`UI_02_*`、`UI_choice_*` → 目录 `_archive_UI02/`

重建：

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_design_system.py"
```

---

## 5. Ren'Py 集成（摘要）

完整片段见 `UI\RENPY_GUI_SNIPPET.rpy`。

```renpy
# 对话
screen say(who, what):
    if who:
        add "UI/UI_DS_bar_dialogue.png" xalign 0.5 yalign 1.0
        # show portrait separately
    else:
        add "UI/UI_DS_bar_narration.png" xalign 0.5 yalign 1.0
```

```renpy
# 选项
textbutton "[caption]":
    idle_background "UI/UI_DS_choice_normal.png"
    hover_background "UI/UI_DS_choice_hover.png"
    selected_idle_background "UI/UI_DS_choice_selected.png"
    xsize 780 ysize 76
```

---

## 6. 与旧 UI_02 对比

| 项目 | UI_02（弃用） | UI_DS v1 |
|------|---------------|----------|
| 画布高 | 440（含上探+立绘） | **360** 纯底栏 |
| 立绘 | 烤进 PNG | **独立 show** |
| 旁白 | 多张对比稿未决 | **一张** narration bar |
| 选项 | 800×90 扁平块 | **780×76** 玻璃感细条 |
| 维护 | 多脚本 | **单脚本** |

---

## 7. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-21 | UI 设计系统 v1 建立；全套 DS 资源脚本化生成 |
| 2026-05-21 | **v1.1 浅色系**：暖米白底栏 + 深色字 + 深橙强调 |
| 2026-05-21 | **v1.2**：顶缘渐隐更透、渐变加强 |
| 2026-05-21 | 底栏高度 **360px**（用户指定） |
| 2026-05-19 | 新增 **`UI_SPEC.md`** 集中记录 1920×360 等全模块宽×高 |

---

*维护：改尺寸先改 **`UI_SPEC.md`** + `build_ui_design_system.py` 常量，再重跑脚本。*
