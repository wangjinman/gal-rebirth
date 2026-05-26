# GAL Say UI · 协作规则（Agent / 人工）

> **版本**：2026-05-26 · Say 屏 UI 暂告一段落，字体待选。  
> 工作流详见 `UI_WORKFLOW.md` · 变更日志见 `UI_WORK_LOG.md`。

---

## 1. 目录与写入权限

| 规则 | 说明 |
|------|------|
| **唯一真源** | `J:\项目\GAL\美术资源初稿\UI\` |
| **Agent 可写** | 上述目录内脚本、PNG 输出、`previews/`、文档 |
| **禁止 Agent 写入** | `GALCS\game\images\UI\` 及整个 Ren'Py 工程（除非你明确要求改 `screens.rpy` / `gui.rpy`） |
| **进游戏** | 你手动复制 `UI_DS_*` → `GALCS\game\images\UI\`（常去掉 `UI_DS_` 前缀） |

---

## 2. 主题定调（勿擅自改）

### 粉套 `anime_style/`

| 分组 | 张数 | 风格 |
|------|------|------|
| 底栏 | 2 | 无色冷雾玻璃 `bar_colorless()` |
| 选项 | 3 | **浮岛 + 上亮下淡** `choice_colorless()` → 内部 `_choice_island_render(blue=False)` |
| 其余 | 20 | 樱粉（快捷栏、图标、姓名左条等） |

**禁止** 再做成「全套 25 张无色玻璃」（已撤回，灰条+粉钮违和）。

### 蓝套 `anime_style_blue/`

| 分组 | 风格 |
|------|------|
| 底栏、快捷、姓名等 | 全套晴空蓝 Token |
| 选项 | **与粉套同形状**（浮岛 + 上亮下淡），填充为天蓝雾 `choice_island_blue()` |

两套 **文件名相同**，只换目录。

---

## 3. 生成命令（固定流程）

```powershell
cd J:\项目\GAL\美术资源初稿\UI\scripts

# UI + 自动 UI 预览（latest + history）
python build_ui_anime_say.py pink
python build_ui_anime_say.py blue
python build_ui_anime_say.py all

# 不要预览
python build_ui_anime_say.py pink --no-preview

# 仅字体对比预览（不改 UI 时也可单独跑）
python build_say_font_preview.py
python build_say_font_preview.py --theme blue
```

| 产出 | 路径 |
|------|------|
| UI | `anime_style/` · `anime_style_blue/` |
| UI 预览 | `previews/latest/UI_SAY_PREVIEW_sheet_{theme}_galcs.png` |
| 字体预览 | `previews/latest/UI_SAY_FONT_PREVIEW_sheet_{theme}_galcs.png` |
| 历史 | `previews/history/YYYYMMDD_HHMMSS/` |

---

## 4. 选项按钮 · 技术规则（脚本内勿破坏）

当前定稿实现：`build_ui_anime_say.py` → `_choice_island_render()` + `_choice_island_finish()`。

| 要点 | 常量 / 行为 |
|------|-------------|
| 浮岛留白 | `CHOICE_ISLAND_W_FRAC=0.80` · `H_FRAC=0.62` |
| 渐变 | 顶 α≈0.28 → 底 α≈0.07（三态略增） |
| 顶缘 | numpy 补强 2–3px，**不用** 矢量 `outline`/`arc`（易顶缝缺色） |
| 超采样 | `CHOICE_SUPERSAMPLE=4` |
| 缩小后 | `_choice_island_finish()` 用 **软 mask**（高分辨率模糊再 Lanczos），避免硬切锯齿 |
| 已废弃 | 水光高光椭圆、底部水线、整圈灰雾填充 |

粉套：冷白 RGB `(250,252,255)`。蓝套：上白 → `BAR_BOTTOM`，边缘混 `ACCENT`。

---

## 5. 对话框底栏 · 技术规则

`bar_colorless()`：冷雾 tint、顶缘高光带、正文区略实；**不**加粉/蓝描边。  
黑屏与彩景无法完全一致；可选 Ren'Py 淡幕布（未默认写入 GALCS）。

---

## 6. 预览图规则

1. **出一版 UI → 必出一版 UI 预览**（除非 `--no-preview`）。  
2. 预览默认：`galcs` 布局，对齐 `GALCS/game/screens.rpy`（底栏 y=720、选项 800×90 拉伸、对话+选项同屏）。  
3. 字体方案用 `build_say_font_preview.py`，不混在 UI 构建里。  
4. 新字体试稿：字体文件放入 `GALCS/game/fonts/`，在 `build_say_font_preview.py` 的 `font_presets()` 增加条目后重跑。

---

## 7. 文案 / 字体（待定 · 推荐方向）

| 区域 | 推荐（预览已对照） |
|------|-------------------|
| 正文 | `#E8ECF2` + 2px 深色描边 |
| 姓名 | 樱粉 `#FF70A8` / 天蓝 `#41B9FF` |
| 选项字 | 白字 + 描边，约 28px |
| 字体族 | 思源黑 / 微软雅黑 / 霞鹜新晰黑（GitHub OFL） |

**不要** 在无色玻璃 UI 上继续用 `#2c3e50` 深灰字（GALCS 当前写死，待你确认后改引擎）。

Say **UI PNG 暂封版**；字体不进 `build_ui_anime_say.py`，只走字体预览 + 后续 `gui.rpy`。

---

## 8. Git / 基准

| 操作 | 命令 |
|------|------|
| 恢复 UI 基准 | `python scripts/restore_ui_baseline.py`（见 `UI_BASELINE.md`） |
| 提交 | **仅在你明确要求时** Agent 才 git commit |

---

## 9. 相关文档索引

| 文档 | 用途 |
|------|------|
| `UI_THEME_COLORS.md` | 配色 Token |
| `UI_SPEC.md` | 尺寸 |
| `UI_SAY_LAYOUT_GUIDE.md` | 引擎叠层坐标 |
| `UI_WORKFLOW.md` | 命令速查 |
| `UI_WORK_LOG.md` | 按日变更 |
| `previews/README.md` | 预览目录说明 |

*Rules ID: `gal-ui-rules-20260526`*
