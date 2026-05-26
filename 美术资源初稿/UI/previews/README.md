# Say 屏合成预览

无需启动 Ren'Py：**背景 + 立绘 + UI** → 1920×1080 实机感效果图。  
规则与流程：`../UI_AGENT_RULES.md` · `../UI_WORKFLOW.md`

## 固定流程（与 UI 同发）

跑 `build_ui_anime_say.py` 时会**自动**生成本目录预览，无需单独记一步。

```powershell
python ..\scripts\build_ui_anime_say.py pink
```

## 目录结构

| 目录 | 说明 |
|------|------|
| `latest/` | **当前最新**预览，审图只看这里 |
| `history/<时间戳>/` | 每次出 UI 自动留档，便于对比旧版 |

主文件：`latest/UI_SAY_PREVIEW_sheet_pink_galcs.png`（樱粉 · 四宫格）

## 字体对比预览

```powershell
python build_say_font_preview.py
```

输出：`latest/UI_SAY_FONT_PREVIEW_sheet_pink_galcs.png`

## 仅重出预览（不改 UI 时）

```powershell
cd ..\scripts
python build_say_screen_preview.py --publish pink
python build_say_screen_preview.py --publish pink blue
```

## 单张自定义

```powershell
python build_say_screen_preview.py --mode say --bg BG_04
python build_say_screen_preview.py --mode black
python build_say_screen_preview.py --mode say --no-choices
```

详见 `../UI_WORKFLOW.md`。
