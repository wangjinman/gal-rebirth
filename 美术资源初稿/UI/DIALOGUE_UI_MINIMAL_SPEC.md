# UI_02 极简对话底栏 · 归档说明

> ⚠️ **已由 `UI_DESIGN_SYSTEM.md`（UI_DS v1）取代**（2026-05-21）。  
> 旧资源已移至 `UI\_archive_UI02\`。新工程请只用 `UI_DS_*` + 独立立绘 `show`。

---

# UI_02 极简对话底栏 · 历史规范（归档）

> **状态**：用户曾选定 **方案 A（立绘头部上探）** — 不再作为标准。

---

## 1. 方案概要

| 项目 | 约定 |
|------|------|
| 样式代号 | **UI_02 · minimal · posA_overflow_top** |
| 视觉 | 底部深色渐变条 + 左侧林晚棠半身立绘，**无**圆形头像框、**无**右侧功能图标 |
| 与旧版关系 | 基于 `v3` 自然融合（边缘羽化 + 底缘溶解），亮度参考 `v3_large_bright`；**不采用** `v4` 整层暗罩风格 |
| 弃用方案 | **方案 B**（整图缩进 350×1920 内露全头）— 仅作对比样，非标准 |

---

## 2. 画布与分区

```
┌──────────────────────────────────── 1920 ────────────────────────────────────┐
│  overflow 区（高 90px）— 立绘头部可进入游戏画面，条带以上多为透明/轻渐变      │
├──────────────────────────────────────────────────────────────────────────────┤
│  bar 区（高 350px，y = 90 … 439）— 对话渐变底、分割线、文本区                │
│  [立绘左]                    [姓名/正文预留区]                                  │
└──────────────────────────────────────────────────────────────────────────────┘
```

| 参数 | 值 |
|------|-----|
| 总画布 | **1920 × 440**（= 350 底栏 + **90** 上探） |
| `H_BAR` | 350（引擎对齐的「逻辑底栏高度」） |
| `OVERFLOW_TOP` | 90（头部上探区，可微调 ±10） |
| 格式 | PNG **RGBA**，全画布导出 |

**锚点规则**

- 立绘 **脚底对齐画布底边**（`py = canvas_h - portrait_h`）。
- 渐变条只画在 **bar 区**（`y_offset = OVERFLOW_TOP`，高度 `H_BAR`）。
- 上探区不强行铺不透明底，以便叠在场景上时头部自然「探出」底栏。

---

## 3. 立绘来源与裁剪

| 项目 | 约定 |
|------|------|
| 源文件 | `J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-transparent-v1-feather.png` |
| 裁剪 | 按 alpha  bbox 取半身，高度约为全身 bbox 的 **66%**（胸像～大腿） |
| 缩放 | `target_h = int(H_BAR * 1.14)`（约 **114%** 相对 350 栏高，保持大气） |
| 水平位置 | 左缘约 **x = 4px**，文本区分割线起始于立绘右缘 + **18px** |

其他角色复用本流程时：同一套裁剪比例与 scale，仅替换 feather 立绘路径。

---

## 4. 视觉参数（与 v3 一致）

| 参数 | 值 | 说明 |
|------|-----|------|
| 条带色调 `TINT` | RGB **(32, 42, 72)** | 比初版 v3 略亮，对齐 `v3_large_bright` |
| 渐变 | 自下而上透明度递增；左侧约 45% 宽度略加重，托住立绘 |
| 边缘融合 | `blend_mask`：下摆溶解 + 外轮廓羽化（Gaussian ~2.0）；核心 alpha > 0.55 保持清晰 |
| 色偏 | `harmonize_colors`：**仅外缘**向条带色偏，禁止整图染成条带色 |
| 分割线 | 栏内 y ≈ bar_top+112 / +128 两条 1px 白线（alpha 70 / 30） |

**禁止**

- 圆形/方形头像框、描边卡片
- 右侧齿轮/快进等图标（需另做 HUD）
- 将立绘整体缩进 350 内导致头被裁（那是方案 B）

---

## 5. 正式交付文件

| 用途 | 路径 |
|------|------|
| **暂定定稿** | `J:\项目\GAL\美术资源初稿\UI\UI_02_dialogue_minimal_wantang_posA_overflow_top.png` |
| 重建脚本 | `J:\项目\GAL\美术资源初稿\UI\scripts\build_dialogue_ui_minimal_posA.py` |
| 对比样（非标准） | `UI_02_dialogue_minimal_wantang_posB_shift_down.png` |

引擎若需短文件名，可在 Ren'Py `images/` 下建立同名软链或复制，**源规范仍以 J 盘全名为准**。

---

## 6. Ren'Py 对齐（必遵）

底栏贴屏幕底，**多出的 90px 向上进入画面**：

```renpy
screen dialogue_bar():
    add "UI/UI_02_dialogue_minimal_wantang_posA_overflow_top.png":
        xalign 0.5
        yalign 1.0
```

- **不要** `yalign 0.0` 或顶部对齐，否则上探区会被裁在屏幕外。
- 文本层建议仍在 **底部 350px** 安全区内排版（`ypos` 相对 `config.screen_height - 350`）。

---

## 7. 重建命令

```powershell
python "J:\项目\GAL\美术资源初稿\UI\scripts\build_dialogue_ui_minimal_posA.py"
```

修改 `OVERFLOW_TOP`、`PORTRAIT_SCALE` 或 `TINT` 后重跑即可；输出覆盖 `UI_02_dialogue_minimal_wantang_posA_overflow_top.png`。

---

## 8. 旁白条（无立绘）

旁白为全知叙述，**不应出现角色立绘**；与对话条共用底对齐，便于 Ren'Py 切换。

| 项目 | 约定 |
|------|------|
| 文件 | `UI\UI_02_narration_minimal.png` |
| 画布 | **1920×440**（与对话条相同，`OVERFLOW_TOP=90` 上区透明，仅对齐用） |
| 渐变 | 同 `TINT`，**左右对称**（取消对话条左侧加重） |
| 分割线 | 全宽，`x = 48 … 1920-48` |
| 脚本 | `UI\scripts\build_dialogue_ui_narration.py` |

```renpy
# 旁白
add "UI/UI_02_narration_minimal.png":
    xalign 0.5
    yalign 1.0
```

引擎侧建议：旁白用居中或略宽行距的正文样式，**不显示姓名框**；对话仍用 `UI_02_dialogue_minimal_wantang_posA_overflow_top.png`。

### 8.1 旁白布局对比稿（待选）

| 方案 | 文件 | 要点 | Ren'Py 文本区 |
|------|------|------|----------------|
| 原版 | `UI_02_narration_minimal.png` | 对称渐变，分割线全宽 | `x` 约 48 起 |
| **A 左侧加重** | `UI_02_narration_minimal_v2_left_weight.png` | 同对话条左区渐重 + 竖线分区；**无立绘** | 正文从 **x≈420** 起（与对话条对齐） |
| **B 居中窄栏** | `UI_02_narration_minimal_v2_center.png` | 中间略淡；分割线/竖引导在 **宽 62% 居中栏** | `text_align 0.5`，栏宽约 **1190px**（x 365～1555） |

重建：`UI\scripts\build_dialogue_ui_narration_v2.py`

---

## 9. 修订记录

| 日期 | 说明 |
|------|------|
| 2026-05-19 | 用户选定方案 A，本文档建立（暂定） |
| 2026-05-19 | 增加旁白条 `UI_02_narration_minimal.png` |
