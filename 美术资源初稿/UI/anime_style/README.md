# UI · 二次元 / 卡通风（anime_style · 樱粉 + 底栏/选项无色）

> **仅底栏 + 选项** 无色气泡；**快捷栏、图标、姓名条** 樱粉。  
> **配色**：`../UI_THEME_COLORS.md` · **规则**：`../UI_AGENT_RULES.md`  
> **生成**：`python ../scripts/build_ui_anime_say.py pink`（含自动预览 → `../previews/latest/`）

## 风格特征

- 底栏/选项：无色玻璃 · 快捷/姓名：樱粉 `#FF70A8`
- 底栏 / 快捷条 **顶圆角**；对话底栏无星星点缀
- 选项：**浮岛药丸** + 上亮下淡 + 4× 超采样（见 `UI_CHOICE_BUTTON_SPEC.md`）
- 快捷钮：**圆形** + `ACCENT` / `ACCENT_HOVER` 外圈
- 姓名条：独立 PNG + 左侧色块

## 生成

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_ui_anime_say.py" pink
```

## Ren'Py 使用

将本目录下 PNG 复制到 `game/UI/`，或改路径前缀：

```renpy
define ui_style = "UI/anime_style/"
add ui_style + "UI_DS_bar_dialogue.png"
```

## 规格（与 UI_SPEC.md 一致）

| 资源 | 尺寸 |
|------|------|
| 对话/旁白底栏 | 1920×360 |
| 姓名条 | 320×44 |
| 选项 | 780×76 |
| 快捷条 | 1920×56 |
| 快捷图标 | 48×48 |
| 语音钮 | 40×40 |
