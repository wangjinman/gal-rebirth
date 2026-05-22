# Day 11 · 走廊窗边·夕阳（林晚棠）

> 背景：`BG_25_corridor_window_sunset.png`  
> **与 `BG_06_corridor_afternoon.png` 为同一条学校走廊**（午后 / 傍晚窗边）  
> **中式校园**：班牌「高二(x)班」、公告栏汉字；**禁止日语**（与 BG_06 一致）  
> 剧本行：718

---

## 氛围

夕阳、浪漫、校园青春、温馨；橙粉晚霞、窗光、尘埃微粒。

## 剧本摘录

```
narrator "夕阳西斜。"
narrator "我们并肩站在窗边，看着外面的晚霞。"
lindao "你看，今天的晚霞好像特别好看。"
player "嗯……确实很好看。"
narrator "她的侧脸被夕阳染成了暖色。"
```

## Ren'Py

```renpy
image bg corridor_window_sunset = "背景/BG_25_corridor_window_sunset.png"

label day11_sunset_window:
    scene bg corridor_window_sunset with dissolve
    "夕阳西斜。"
    show lin smile at right   # 并肩靠窗，站位按立绘微调
    show protagonist at left
```

## 备注

- 旧版：`BG_25_corridor_window_sunset_v1.png`（与 BG_06 细节不符 / 含日式元素）
- 备选：`BG_25_corridor_window_sunset_composite_BG06.png`（程序化拼窗备份）

---

## Day 11 · 校门外告别（行 782）

> 背景：`BG_26_school_gate_street_dusk.png`  
> 与 **BG_22** 同一校门（滨海市第一中学），**黄昏门外街道**，≠ BG_10 住宅区早晨

```
narrator "天色渐渐暗了下来。"
narrator "我们一起走出校门。"
lindao "那我先回去了。"
player "路上小心。"
narrator "她点点头，转身离开。"
narrator "夕阳把她的影子拉得很长。"
```

```renpy
image bg school_gate_street_dusk = "背景/BG_26_school_gate_street_dusk.png"
scene bg school_gate_street_dusk with dissolve
```

*2026-05-21*
