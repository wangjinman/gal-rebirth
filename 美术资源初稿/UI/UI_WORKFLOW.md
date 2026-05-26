# GAL Say UI · 固定工作流

> 出一版 UI PNG → **自动**出一版合成预览图。无需进游戏。  
> **协作规则全文**：`UI_AGENT_RULES.md` · **变更日志**：`UI_WORK_LOG.md`

## 标准命令（推荐）

```powershell
cd J:\项目\GAL\美术资源初稿\UI\scripts

# 樱粉（含 25 张 UI + 四宫格预览）
python build_ui_anime_say.py pink

# 晴空蓝
python build_ui_anime_say.py blue

# 两套 UI + 两套预览
python build_ui_anime_say.py all
```

仅生成 UI、不要预览时：

```powershell
python build_ui_anime_say.py pink --no-preview
```

## 输出位置

| 产物 | 路径 |
|------|------|
| UI 零件 | `anime_style/` 或 `anime_style_blue/` · `UI_DS_*.png` |
| **最新预览** | `previews/latest/UI_SAY_PREVIEW_sheet_{theme}_galcs.png` |
| **历史留档** | `previews/history/YYYYMMDD_HHMMSS/`（同文件名 + `BUILD_INFO.txt`） |

预览内容（2×2）：教室对话+选项 · 黑底对话+选项 · 仅选项 · 旁白。  
布局默认对齐 `GALCS/game/screens.rpy`（`galcs`）。

## 字体对比预览（Say 文案）

与 UI 预览相同思路：**背景 + 立绘 + 当前 UI + 多套字体** 拼成四宫格。

```powershell
python build_say_font_preview.py
python build_say_font_preview.py --theme blue --bg BG_04
```

输出：`previews/latest/UI_SAY_FONT_PREVIEW_sheet_{theme}_galcs.png`

对比项默认：游戏当前黑体深字 → 黑体/雅黑/思源（或雅黑 Light）+ 浅字描边。

## 单独补预览（UI 已存在时）

```powershell
python build_say_screen_preview.py --publish pink
python build_say_screen_preview.py --publish pink blue
python build_say_screen_preview.py --sheet   # 等同 --publish pink
```

## 复制进游戏

手动将 `UI_DS_*` 复制到 `GALCS\game\images\UI\`（Agent 不写游戏目录）。

## 相关文档

- `UI_THEME_COLORS.md` · `UI_SAY_LAYOUT_GUIDE.md` · `previews/README.md` · `UI_WORK_LOG.md`
