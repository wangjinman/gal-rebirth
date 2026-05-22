# CG-P02 · 意识消散·沉入深海 — 定稿

> **状态**：初稿入库（2026-05-21）  
> **优先级**：P1 · 情绪 ★★★★☆

---

## 剧本位置（序章行 50–66）

```
narrator "视野越来越暗。"
narrator "就像……沉入深海。"
player_thought "就这样……结束了吗……"
player_thought "那些……没说出口的话……"
narrator "意识，在这一刻，彻底消散。"
scene black with fade
pause 3.0
```

---

## 定稿文件

| 用途 | 文件 |
|------|------|
| **叠层 / dissolve（推荐）** | `CG_P02_consciousness_deep_sea.png`（RGBA，边缘深蓝透明） |
| 全屏不透明 | `CG_P02_consciousness_deep_sea_opaque.png` |
| 原图 | `CG_P02_consciousness_deep_sea_original.png` |

路径：`J:\项目\GAL\美术资源初稿\CG\`

---

## 画面规则

| 项目 | 约定 |
|------|------|
| 构图 | 中心亮白渐向外模糊；**隧道视野**；边缘 **深海深蓝** 侵入 |
| 粒子 | 白色光点从中心向暗处消融 |
| 回忆 | **中央**：女主（女孩）微笑；**两侧**：母亲剪影 + **童年男主（男孩）**剪影（濒死男主回忆母与己与女主） |
| 旧版 | `_v1` / `_v1_opaque`（两侧曾为两女剪影） |
| 气质 | 空灵、告别、沉静；平和而忧郁 |
| 规格 | 1920×1080；叠层用 RGBA，后可 `scene black` |

---

## Ren'Py

```renpy
image cg consciousness_deep_sea = "CG/CG_P02_consciousness_deep_sea.png"

label prologue_fade_away:
    scene cg overtime_end
    show cg consciousness_deep_sea with Dissolve(2.5)
    narrator "视野越来越暗。"
    narrator "就像……沉入深海。"
    # ...
    hide cg consciousness_deep_sea with Dissolve(2.0)
    scene black with Dissolve(3.0)
    pause 3.0
```

---

## 衔接

- 前：`CG_P01` 或 `BG_20`（白闪回）之后
- 后：`scene black` → 重生线 `BG_03` / `BG_21`

与 **BG_20** 区别：P02 为 **CG 事件插画**（含回忆剪影、深海隐喻更强）；BG_20 为碎屏闪回叠层素材。

---

## 英文提示词（生成用）

```
ethereal consciousness fading, white light center dissolving to deep ocean blue edges
tunnel vision, CENTER girl smile unchanged, LEFT RIGHT mother silhouette and young boy child silhouette (protagonist childhood)
spirit rising peaceful melancholic surreal VN CG 1920x1080
```

*2026-05-21*
