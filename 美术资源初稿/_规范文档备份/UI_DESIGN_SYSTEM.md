# GAL 项目 · UI 设计系统（Design System v1）

> **状态**：2026-05-21 整体重做 · 取代 `UI_02` 拼贴方案  
> **原则**：**立绘与底栏分离** · 一套 Token · Ren'Py `gui` 负责字，PNG 只负责「底」

---

## 1. 设计目标

| 目标 | 做法 |
|------|------|
| 统一 | 对话 / 旁白 / 选项共用颜色、圆角、透明度 |
| 轻盈 | 底栏 **168px**（旧版 350+90 过重） |
| 适配 Key 风 BG | 条带 **半透明**，暗蓝紫，不抢立绘 |
| 可维护 | 单脚本 `build_ui_design_system.py` 重建全部 PNG |
| 可扩展 | 换角色只换 `show` 立绘，不换底栏图 |

---

## 2. Design Tokens

### 2.1 色彩

| Token | 值 | 用途 |
|-------|-----|------|
| `bar.bg` | RGB **(24, 32, 58)** · α **0.72** | 对话底栏 |
| `bar.bg.narration` | 同上 · α **0.58** | 旁白底栏（更淡） |
| `accent` | **#E8A05C** | 强调、姓名、选项悬停 |
| `accent.hover` | **#FFBC6E** | 选项悬停边框/光 |
| `accent.fill` | RGBA **(255, 188, 120, 0.38)** | 选项选中填充 |
| `text.primary` | **#F4EFE8** | 正文 |
| `text.name` | **#FFD9A8** | 角色名 |
| `text.muted` | **#B8C0D4** | 旁白/次要 |
| `line.subtle` | RGBA **(255,255,255, 0.14)** | 顶缘高光、分割线 |
| `line.accent` | RGBA **(255, 154, 77, 0.92)** | 选项悬停描边 |

### 2.2 尺寸与间距

| Token | 值 |
|-------|-----|
| `screen.w` | 1920 |
| `bar.h` | **168** |
| `bar.pad.x` | 48 |
| `text.x.dialogue` | **400**（立绘区右侧起点） |
| `text.w.dialogue` | 1420 |
| `text.x.narration` | 360（居中栏左缘） |
| `text.w.narration` | 1200（宽约 62.5%） |
| `portrait.x` | 72 |
| `portrait.yalign` | 1.0（脚底贴屏底） |
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
│  ┌─ UI_DS_bar_dialogue.png · 高 168 ────────────────────────────────────┐ │
│  │ 正文区 x≥400                                                           │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────┘
```

**旁白**：无立绘 · `UI_DS_bar_narration.png` · 正文居中栏 1200px  
**选项**：屏幕中部 `vbox` · `UI_DS_choice_*.png` × 3

---

## 4. 交付文件清单

路径：`J:\项目\GAL\美术资源初稿\UI\`

| 文件 | 尺寸 | 说明 |
|------|------|------|
| `UI_DS_bar_dialogue.png` | 1920×168 | 对话底栏，左侧略重 |
| `UI_DS_bar_narration.png` | 1920×168 | 旁白底栏，对称更淡 |
| `UI_DS_nameplate.png` | 320×44 | 姓名条底（可选，可用 gui 代替） |
| `UI_DS_choice_normal.png` | 780×76 | 选项·普通 |
| `UI_DS_choice_hover.png` | 780×76 | 选项·悬停 |
| `UI_DS_choice_selected.png` | 780×76 | 选项·选中 |

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
| 画布高 | 440（含上探+立绘） | **168** 纯底栏 |
| 立绘 | 烤进 PNG | **独立 show** |
| 旁白 | 多张对比稿未决 | **一张** narration bar |
| 选项 | 800×90 扁平块 | **780×76** 玻璃感细条 |
| 维护 | 多脚本 | **单脚本** |

---

## 7. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-21 | UI 设计系统 v1 建立；全套 DS 资源脚本化生成 |

---

*维护：改 Token 后只改 `build_ui_design_system.py` 顶部常量并重跑。*
