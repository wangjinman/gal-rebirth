# Day 14 · 送林晚棠回家（晴夜街道）

> 背景：`BG_27_residential_street_night_clear.png`  
> 剧本行：1546 · **晴天无雨**，不可用 `BG_09_rainy_street_night.png`

---

## 剧本摘录

```
hide cg rooftop_embrace with dissolve
scene black
narrator "送她回家的路上，我们谁都没有说话。"
narrator "但手一直牵在一起。"
narrator "今晚的月亮很亮。"
```

## 街区关系

| BG | 时段/天气 | 用途 |
|----|-----------|------|
| BG_10 | 早晨 | 上学路 |
| BG_17 | 黄昏 | 城南街道 |
| BG_09 | **雨夜** | 雨天剧情 |
| **BG_27** | **晴夜** | Day14 送归 · 满月、干路面 |

## Ren'Py

```renpy
image bg residential_night_clear = "背景/BG_27_residential_street_night_clear.png"

label day14_walk_home:
    hide cg rooftop_embrace with dissolve
    scene black with dissolve
    pause 0.5
    scene bg residential_night_clear with dissolve
    narrator "送她回家的路上，我们谁都没有说话。"
```

*2026-05-21*
