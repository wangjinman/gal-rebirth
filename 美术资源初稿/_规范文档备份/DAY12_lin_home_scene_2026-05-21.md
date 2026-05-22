# Day 12 · 林晚棠家（室内 → 阳台）

> 背景：`BG_11_living_room_afternoon.png` → `BG_12_balcony_succulents_afternoon.png`  
> 用途：做客、客厅对话 → 阳台照顾多肉

---

## 场景衔接关系

| 顺序 | 背景 | 剧情用途 |
|------|------|----------|
| 1 | `BG_11_living_room_afternoon.png` | 进门、客厅落座、喝茶对话 |
| 2 | `BG_12_balcony_succulents_afternoon.png` | 去阳台看/浇多肉、更私密或治愈向台词 |

**视觉连贯点（已定稿图）：**

- 同一时段：**午后暖光**；家境 **普通**，阳台 **窄小**（非大露台）
- 客厅落地窗望见：栏杆边 **简易木层架 + 多肉**（与 BG_12 同一布局）
- **BG_12 机位**：站在阳台地砖上向外看（栏杆 + 花架在前方），左侧仅露推拉门框；**非**从室内透过门洞望出去

---

## Ren'Py 示例

```renpy
# Day 12 — 林晚棠家
label day12_lin_home:
    scene bg living_room_afternoon with dissolve
    "门铃响过，林晚棠把你让进客厅。茶香和阳光一起漫过来。"

    # 客厅对话：立绘半身 + UI_02 对话条
    show lin smile at center
    lin "你先坐，我去泡茶。"
    # ...

    "她指了指通向阳台的门。"
    lin "顺便来看看我那些多肉，最近长了不少。"

    # 转阳台：短 dissolve 或 slide
    scene bg balcony_succulents_afternoon with dissolve
    "推开门，午后的风带着一点潮气。架子上挤满小小的绿。"

    show lin smile at center
    lin "这一盆是上周才分出来的……"
    # 照顾多肉 / 治愈对话
    return
```

**image 定义：**

```renpy
image bg living_room_afternoon = "背景/BG_11_living_room_afternoon.png"
image bg balcony_succulents_afternoon = "背景/BG_12_balcony_succulents_afternoon.png"
```

---

## 演出建议

| 项目 | 建议 |
|------|------|
| 转场 | `dissolve` 1.0～1.5s；可加一句台词交代「走向阳台」 |
| 立绘 | 两景均用 `bust\` 半身；`yalign 1.0` |
| UI | 对话 `UI_02_dialogue_minimal_wantang_posA_overflow_top`；旁白可用 `UI_02_narration_minimal_v2_left_weight` |
| BGM | 客厅偏温馨日常；阳台可略清、更静 |

---

## 文件路径（J 盘）

```
J:\项目\GAL\美术资源初稿\背景\
  BG_11_living_room_afternoon.png
  BG_12_balcony_succulents_afternoon.png
```

*2026-05-19*
