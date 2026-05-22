# Day 15 · 咖啡馆外街道（黄昏）

> 背景：`BG_28_cafe_exterior_street_evening.png`  
> 剧本行：1647 · 从 **晚星咖啡馆** 走出，承接 `BG_14` / `BG_08` 室内

---

## 剧本摘录

```
narrator "走出咖啡馆的时候，脑子里还在想着她说的话。"
player_thought ""如果真的喜欢她的话……""
player_thought ""现在就是最好的时机。""
narrator "苏念卿说得对。"
narrator "不能再等了。"
```

## 与咖啡馆 BG 关系

| 场景 | 文件 |
|------|------|
| 室内宽景 | `BG_08_cafe_sunset.png` |
| 室内吧台 | `BG_14_cafe_bar_evening_near_bar.png` |
| **室外街道** | `BG_28_cafe_exterior_street_evening.png` |

店面灯光、户外桌椅风格应与室内绿皮沙发、暖光咖啡馆统一。

## Ren'Py

```renpy
image bg cafe_exterior_evening = "背景/BG_28_cafe_exterior_street_evening.png"

label day15_leave_cafe:
    scene bg cafe_exterior_evening with dissolve
    narrator "走出咖啡馆的时候，脑子里还在想着她说的话。"
```

*2026-05-21*
