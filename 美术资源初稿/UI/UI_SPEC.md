# GAL 项目 · UI 规格书（UI_SPEC）

> **版本**：1.0 · 2026-05-19  
> **分辨率基准**：**1920×1080**（16:9）  
> **配套**：`UI_DESIGN_SYSTEM.md`（Token/色）· `UI_ASSET_MAP_FULL.md`（全量文件名）· `RENPY_GUI_SNIPPET.rpy`（gui 数值）

本文档为**尺寸与摆放的单一事实来源**。生成脚本、验收 PNG、写 Ren'Py `gui` 时以此为准。

---

## 1. 全局常量

| 项 | 规格 | 说明 |
|----|------|------|
| 游戏分辨率 | **1920×1080** | `config.screen_width/height` |
| 安全区（全宽 UI） | 宽 **1920** | 底栏、遮罩、菜单底 |
| 底栏高度 `bar.h` | **360** | ADV / NVL 共用 |
| 底栏锚点 | `xalign 0.5` · `yalign 1.0` | 贴屏幕底边 |
| 立绘区（逻辑） | x **0–360** | 立绘 **不在** 底栏 PNG 内 |
| 对话正文区 | x **400**，宽 **1420** | 底栏上叠字 |
| 旁白正文区 | x **360**，宽 **1200** | 居中栏（左右各 360） |
| 选项区 | 屏中 `vbox` · `xalign 0.5` · `yalign 0.5` | 不贴底 |
| 选项间距 | **14** | `choice_spacing` |
| 圆角 `radius.md` | **10** | 按钮、条带（脚本生成） |
| 图片格式 | **PNG-24/32**，带 Alpha | 勿 JPG |

---

## 2. 已交付资源（实测尺寸）

以下文件已存在于 `UI/`，尺寸经核对：

| 文件名 | 宽×高 (px) | 锚点 / 用法 | Ren'Py 对应 |
|--------|------------|-------------|-------------|
| `UI_DS_bar_dialogue.png` | **1920×360** | 底对齐全宽 | `gui.textbox_height = 360` |
| `UI_DS_bar_narration.png` | **1920×360** | 底对齐全宽 | 旁白分支 `say` |
| `UI_DS_nameplate.png` | **12×44** | 姓名左侧色条 only，x≈400、字从 x≈416 起 | `add` + `text who` |
| `UI_DS_choice_normal.png` | **780×76** | 选项底 | `gui.choice_button_width/height` |
| `UI_DS_choice_hover.png` | **780×76** | 悬停 | 同上 |
| `UI_DS_choice_selected.png` | **780×76** | 选中 | 同上 |
| `UI_DS_quick_bar.png` | **1920×56** | 顶对齐 `yalign 0.0` | `screen quick_menu` |
| `UI_DS_quick_{auto,skip,hide,history,save,load,settings,exit}_{default,hover}.png` | **48×48** | 快捷菜单图标 | `xsize/ysize 48` |
| `UI_DS_say_voice_{default,hover}.png` | **40×40** | 句内语音重播（可选） | say 屏角标 |

**底栏渐变**：PNG 顶缘近透明 → 底缘渐浓；**勿**与 `bar_narration` 叠在同屏。

### 2.1 风格变体（尺寸相同）

| 目录 | 风格 | 生成脚本 |
|------|------|----------|
| `UI/`（根） | 极简浅色 · 暖米白 | `scripts/build_ui_design_system.py` |
| `UI/anime_style/` | **二次元卡通 · 粉** | `scripts/build_ui_anime_say.py pink` |
| `UI/anime_style_blue/` | **二次元卡通 · 蓝** | `scripts/build_ui_anime_say.py blue` |

两套文件名均为 `UI_DS_*`，可整目录切换，无需改 Ren'Py 尺寸。

---

## 3. Ren'Py `gui` 与坐标（与 PNG 对齐）

粘贴自 `RENPY_GUI_SNIPPET.rpy`，改尺寸时**同步改本节 + 脚本常量**：

| gui 变量 | 值 | 对应规格 |
|----------|-----|----------|
| `gui.textbox_height` | **360** | 底栏高 |
| `gui.name_xpos` | **400** | 姓名 X |
| `gui.name_ypos` | **-330** | 相对底栏上缘（向上） |
| `gui.dialogue_xpos` | **400** | 正文 X |
| `gui.dialogue_ypos` | **-280** | 正文 Y |
| `gui.dialogue_width` | **1420** | 正文宽 |
| `gui.choice_button_width` | **780** | 选项宽 |
| `gui.choice_button_height` | **76** | 选项高 |
| `gui.name_text_size` | **26** | 姓名字号 |
| `gui.text_size` | **22** | 正文字号 |
| `gui.choice_button_text_size` | **22** | 选项字号 |

**立绘（非 gui）**：`xpos 72` · `yalign 1.0` · `zorder` 高于底栏。

---

## 4. 规划资源规格（按模块）

未交付项尺寸与 `UI_ASSET_MAP_FULL.md` 一致；制作时 **宽×高不得改列** 除非先改本表。

### 4.1 P0 · 游玩 / 确认

| 文件名 | 宽×高 | 备注 |
|--------|-------|------|
| `UI_DS_quick_bar.png` | **1920×56** | 快捷菜单底条 |
| `UI_DS_quick_*_default/hover.png` | **48×48** | 图标类统一方图 |
| `UI_DS_confirm_scrim.png` | **1920×1080** | 全屏 dim，α≈0.45 |
| `UI_DS_confirm_panel.png` | **720×360** | 居中窗 |
| `UI_DS_confirm_btn_default/hover.png` | **200×64** | 确认/取消钮 |
| `UI_DS_input_panel.png` | **720×280** | 输入框容器 |
| `UI_DS_say_voice_default/hover.png` | **40×40** | 句内语音（可选） |

### 4.2 P1 · 主菜单

| 文件名 | 宽×高 | 备注 |
|--------|-------|------|
| `UI_DS_title_bg_mask.png` | **1920×1080** | 暗角/渐隐，可全透明中心 |
| `UI_DS_title_btn_*_default/hover.png` | **520×72** | Start/Load/Prefs/Gallery/About/Quit |

### 4.3 P2 · 游戏菜单 / 存读

| 文件名 | 宽×高 | 备注 |
|--------|-------|------|
| `UI_DS_menu_bg.png` | **1920×1080** | 菜单半透明底 |
| `UI_DS_menu_tab_default/hover.png` | **280×48** | 侧栏/顶栏项 |
| `UI_DS_menu_icon_*` | **48×48** | 存读等图标 |
| `UI_DS_menu_heading_*.png` | **—** | 可选装饰字图，不强制 |
| `UI_DS_data_slot_default/hover.png` | **420×240** | 存档槽 |
| `UI_DS_data_slot_empty_default/hover.png` | **420×240** | 空槽 |
| `UI_DS_data_slot_label.png` | **400×56** | 槽内文字条 |
| `UI_DS_data_badge_new.png` | **64×64** | 新档角标 |
| `UI_DS_data_btn_delete_default/hover.png` | **120×48** | 删除 |
| `UI_DS_common_page_prev/next_*` | **64×64** | 翻页 |
| `UI_DS_common_dot_default/hover/selected.png` | **24×24** | 页码点 |
| `UI_DS_common_vthumb_default/hover.png` | **16×80** | 竖滚动拇指 |
| `UI_DS_common_vbar_top/bottom.png` | **12×40** | 轨道端 |
| `UI_DS_common_close_default/hover.png` | **48×48** | 关闭菜单 |

**存读布局建议**：`gui.file_slot_cols = 2` · `gui.file_slot_rows = 3` · 单页 6 槽。

### 4.4 P3 · 设置 / 历史 / 画廊

| 文件名 | 宽×高 | 备注 |
|--------|-------|------|
| `UI_DS_settings_section.png` | **600×40** | 分区标题底 |
| `UI_DS_settings_divider.png` | **600×2** | 分隔线 |
| `UI_DS_settings_hbar.png` | **400×8** | 滑轨（可九宫格） |
| `UI_DS_settings_hthumb_default/hover.png` | **120×24** | 滑块 |
| `UI_DS_settings_toggle_hover.png` | **32×32** | 开关指示 |
| `UI_DS_settings_preview_box.png` | **480×120** | 速度预览 |
| `UI_DS_history_avatar_frame.png` | **80×80** | 头像框 |
| `UI_DS_history_line_1.png` | **1600×48** | 单行历史条 |
| `UI_DS_history_line_2.png` | **1600×72** | 两行 |
| `UI_DS_history_line_3.png` | **1600×96** | 三行 |
| `UI_DS_history_voice_default/hover.png` | **40×40** | 语音回放 |
| `UI_DS_gallery_frame_default/hover.png` | **320×180** | 16:9 缩略框 |
| `UI_DS_gallery_locked.png` | **320×180** | 未解锁 |

### 4.5 可选

| 文件名 | 宽×高 |
|--------|-------|
| `UI_DS_notify_bg.png` | **480×64**（toast，待定） |

---

## 5. 脚本常量（生成端）

`scripts/build_ui_design_system.py` 顶部应与上表一致：

```python
W = 1920
BAR_H = 360
CHOICE_W, CHOICE_H = 780, 76
NAMEPLATE_W, NAMEPLATE_H = 320, 44
```

扩展 P1+ 时新增常量块，**禁止**硬编码 magic number  scattered 在脚本内。

---

## 6. 验收检查

```powershell
python -c "from PIL import Image; import os; p=r'J:\项目\GAL\美术资源初稿\UI';
spec={'UI_DS_bar_dialogue.png':(1920,360),'UI_DS_bar_narration.png':(1920,360),
'UI_DS_choice_normal.png':(780,76),'UI_DS_nameplate.png':(320,44)};
for f,s in spec.items():
 im=Image.open(os.path.join(p,f)); assert im.size==s, (f, im.size, s)"
```

新 PNG 入库前：核对宽×高、透明边、与 `UI_ASSET_MAP_FULL.md` 状态改为 `done`。

---

## 7. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-19 | 初版：全局 1920×1080、底栏 **1920×360**、选项 **780×76**、全模块规划尺寸 |
