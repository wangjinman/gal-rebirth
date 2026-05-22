# CG-P01 · 加班夜·生命终结 — 定稿记录

> **状态**：✅ 用户确认定稿（2026-05-21）  
> **文件**：`J:\项目\GAL\美术资源初稿\CG\CG_P01_overtime_life_end.png`

---

## 剧本位置

序章行 28–40 · 第一个情绪高潮（P0）

```
narrator "胃部传来一阵剧烈的绞痛。"
narrator "像是有什么东西在内部撕裂。"
player "……哈……"
narrator "手机从指间滑落。"
narrator "屏幕碎裂的声音，像是某种终结的号角。"
```

---

## 定稿画面规则（续作 / 重绘必守）

| 项目 | 约定 |
|------|------|
| 构图基线 | **v4**：前倾栽向桌沿，**非**侧滑扭肢 |
| 侧脸 | 轮廓占比较大，显示器**蓝光自下**打亮 |
| 表情 | **咬牙**（唇紧闭、齿可见），**禁止**大张张嘴；可皱眉、冷汗 |
| 上身 | 从椅上前倾，肩/胸将触或已触桌沿 |
| 下肢 | 膝在椅面、双脚平踩地，比例自然 |
| 手机 | 脱手**下落**，**触地/触桌瞬间**碎屏；**空中不碎** |
| 光线 | 冷蓝屏幕光 vs 暖橙台灯，深蓝紫环境 |
| 道具 | 凌乱文稿、空咖啡杯 |
| 规格 | 1920×1080 全幅 **不透明 PNG**（事件 CG，非透明底） |

---

## 迭代历程（勿删备份）

| 版本 | 说明 | 备份文件 |
|------|------|----------|
| v1 | 初版 | `CG_P01_overtime_life_end_v1.png` |
| v2 | 痛感、手机触地 | `_v2.png` |
| v3 | 大侧脸滑出椅子（四肢不协调，弃用） | `_v3.png` |
| v4 | 前倾栽桌、四肢自然（**构图定稿**） | `_v4.png`（张嘴） |
| v4b | 更狰狞、更多倒出椅子（弃用） | `_v4b_preview.png` |
| **定稿** | v4 构图 + **咬牙** | `CG_P01_overtime_life_end.png` |

修改 v4 时：用 `_v4.png` 作参考图，**仅改嘴型**，其余保持不变。

---

## Ren'Py

```renpy
image cg overtime_end = "CG/CG_P01_overtime_life_end.png"

label prologue_collapse:
    scene bg bedroom_night_overtime   # 或 BG_19_office
    scene cg overtime_end with vpunch
    play sound "phone_drop.ogg"
    pause 0.2
    play sound "glass_crack.ogg"
    scene bg consciousness_fading with Dissolve(2.0)  # BG_20
```

---

## 衔接 BG

- 前：`BG_19_bedroom_night_overtime.png` 或 `BG_19_office_night_overtime.png`
- 后：`BG_20_consciousness_fading_er.png`（纯白闪回意识消散）

*2026-05-21*
