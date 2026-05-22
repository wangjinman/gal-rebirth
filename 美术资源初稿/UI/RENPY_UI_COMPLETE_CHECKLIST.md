# Ren'Py 视觉小说 · UI 完整需求清单

> **版本**：1.0 · 2026-05-19  
> **适用**：Key 风 / 现代校园 / 日常系 ADV（1920×1080）  
> **配套**：`UI_SPEC.md`（宽×高）· `UI_DESIGN_SYSTEM.md` · `UI_ASSET_MAP_FULL.md` · Skill `renpy-galgame-ui`

本清单回答：**做一个可发行的 Ren'Py Gal，UI 层面至少要有什么**。与具体美术包解耦，新项目可整表复制后删减。

---

## 1. 必做 vs 可选

| 级别 | 含义 |
|------|------|
| **MUST** | 无则无法正常游玩 |
| **SHOULD** | 玩家预期标配 |
| **MAY** | 按剧本需要 |

---

## 2. 屏幕与资源对照（总表）

### 2.1 游玩中（MUST · P0）

| # | Ren'Py | 说明 | 资源 |
|---|--------|------|------|
| 1 | `screen say` ADV | 角色对话 | `UI_DS_bar_dialogue` + 立绘 |
| 2 | `screen say` NVL | 旁白 | `UI_DS_bar_narration` |
| 3 | `screen choice` | 分支 | `UI_DS_choice_*` |
| 4 | 姓名 | `who` | `UI_DS_nameplate` 或 gui |
| 5 | `screen confirm` | 二次确认 | confirm 系列 |
| 6 | `screen quick_menu` | 右键菜单 | quick 系列 |
| 7 | Skip / Auto | 快进自动 | 小图标 |
| 8 | `screen input` | 起名 | input panel |

### 2.2 流程与菜单（SHOULD · P1–P2）

| # | Ren'Py | 说明 |
|---|--------|------|
| 9 | `screen main_menu` | 标题 |
| 10 | `screen navigation` | 菜单导航 |
| 11 | `screen game_menu` | 菜单容器 |
| 12 | `screen save` / `load` | 存读档 |
| 13 | `screen preferences` | 设置 |
| 14 | Return / Quit | 返回退出 |

### 2.3 回顾（SHOULD · P3）

| # | Ren'Py | 说明 |
|---|--------|------|
| 15 | `screen history` | 对话历史 |
| 16 | `screen gallery` | CG 回想 |
| 17 | `screen about` | Staff 授权 |

### 2.4 可选（MAY）

| # | 场景 |
|---|------|
| 18 | 地图选点 |
| 19 | 好感/参数面板 |
| 20 | 手机聊天 UI |
| 21 | 音乐鉴赏 |
| 22 | 成就 / 结局列表 |

---

## 3. 制作工单（按类型）

### P0 底栏与选项
- [ ] ADV / NVL 底栏 **1920×360**（见 `UI_SPEC.md` §2）
- [ ] 姓名条 **320×44**（可选）
- [ ] 选项三态 **780×76**，间距 14
- [ ] `gui.textbox_height=360` 等与 `UI_SPEC.md` §3 一致

### P1 主菜单与快捷
- [ ] Start Load Prefs Gallery About Quit
- [ ] quick_menu 底条 + 图标

### P2 存读与框架
- [ ] menu 半透明底
- [ ] 槽位 / 空槽 / 删除 / 翻页

### P3 设置历史画廊
- [ ] 滑条、分区标题
- [ ] history 行条、gallery 框

---

## 4. Ren'Py 必配 gui 项

- `gui.textbox_height` · `gui.dialogue_*` · `gui.name_*`
- `gui.choice_*` · `gui.file_slot_cols/rows`
- `config.screen_width/height` · `config.overlay_screens`

---

## 5. 新项目启动

1. 复制 `UI/` 四件套（DESIGN_SYSTEM、MAP、CHECKLIST、SNIPPET）
2. 改 Token，跑 `build_ui_design_system.py`
3. 按 `UI_ASSET_MAP_FULL.md` 更新状态
4. Cursor 使用 skill **renpy-galgame-ui**

---

| 日期 | 说明 |
|------|------|
| 2026-05-19 | 初版 |
