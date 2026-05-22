# Day 19 · 医院走廊（带妈妈检查）

> 背景定稿：`BG_24_hospital_corridor_day.png`  
> 剧本行：2217、2225、2247（3 处连续使用）

---

## 场景要点

| 项目 | 说明 |
|------|------|
| 氛围 | 明亮、安静、希望、家庭温情；临床但不冰冷 |
| 画面 | 长走廊、候诊椅、远端窗光、浅蓝白；远处模糊人影 |
| 角色 | **妈妈 / 男主** 用立绘叠在 BG 上；长椅可台词中「坐下」 |

## 剧本摘录

```
lindao "妈，我们去医院看看吧。"
narrator "医院里人来人往。"
narrator "妈妈坐在长椅上，伸手摸了摸我的头。"
mother "没事的。妈妈身体好着呢。"
narrator "我看着她，心里默默发誓——这一次，绝不会再错过。"
```

## Ren'Py

```renpy
image bg hospital_corridor_day = "背景/BG_24_hospital_corridor_day.png"

label day19_hospital:
    scene bg hospital_corridor_day with dissolve
    "妈，我们去医院看看吧。"
    # show mother / protagonist on bench area
```

*2026-05-21*
