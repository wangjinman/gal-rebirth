# GAL UI 工作记录

> 按日期追加。Agent 只改 `美术资源初稿/UI/`；游戏内资源由你手动复制到 GALCS。

---

## 2026-05-26 · Say UI 封版 + 预览流程 + 选项定稿

### 状态

- **Say 屏 UI（粉/蓝）**：用户确认选项形状 OK，暂不再改 PNG。  
- **字体**：未进游戏；已建字体预览脚本，引擎 `gui.rpy` / `screens.rpy` 待你确认后再改。

---

### 选项按钮 · 最终定稿（浮岛 + 上亮下淡）

| 项目 | 值 |
|------|-----|
| 形状 | 内缩浮岛 **80%×62%**，药丸圆角（`floating_island_mask`） |
| 渐变 | 上亮下淡：顶 α≈0.28 → 底 ≈0.07；顶缘 2–3px 补强 |
| 三态 | normal / hover（外晕）/ selected（略实） |
| 粉套 | 冷白雾，无色相 |
| 蓝套 | 同形状，`choice_island_blue()`，天蓝雾 |
| 技术 | `CHOICE_SUPERSAMPLE=4` + `soft_island_mask` + `_choice_island_finish` |

**迭代摘要（勿回退）：**

1. 药丸+亮芯雾 → 用户嫌呆板/偏暗  
2. 浮岛+上亮下淡 → 形状认可  
3. 顶缘缺色 → 去掉矢量顶弧/外描边，改 numpy 顶带  
4. 蓝套「看不出形状」→ 缩小后硬 mask 被 Lanczos 晕满；改终尺寸软 mask  
5. 圆弧锯齿 → 软 mask + 4× 超采样  

**废弃：** 全套无色玻璃 25 张；水光高光；左侧大椭圆「白圈」。

---

### 对话框底栏（粉套 · 仍有效）

`bar_colorless()`：冷雾 RGB、顶缘高光、正文区略实（见 `UI_THEME_COLORS.md`）。用户未再提底栏问题。

---

### 新增工具与流程

| 脚本 | 作用 |
|------|------|
| `build_say_screen_preview.py` | 背景+立绘+UI 合成 1920×1080；`publish_previews()` |
| `build_say_font_preview.py` | 多套字体四宫格对比 |
| `build_ui_anime_say.py` | 末尾自动调用 UI 预览 |

规则写入：`UI_AGENT_RULES.md` · `UI_WORKFLOW.md`。

---

### 预览输出（当前）

| 文件 | 说明 |
|------|------|
| `previews/latest/UI_SAY_PREVIEW_sheet_pink_galcs.png` | UI 四宫格（樱粉） |
| `previews/latest/UI_SAY_PREVIEW_sheet_blue_galcs.png` | UI 四宫格（蓝） |
| `previews/latest/UI_SAY_FONT_PREVIEW_sheet_pink_galcs.png` | 字体四宫格 |
| `previews/history/<时间戳>/` | 每次构建留档 |

---

## 2026-05-19 · Say 屏底栏/选项（樱粉拆分主题）

### 定调摘要

粉套：仅底栏+选项无色；快捷/姓名樱粉。蓝套原全套蓝，后选项改为与粉同形。

详见当日条目；以 **2026-05-26** 选项实现为准。

---

*最后更新：2026-05-26*
