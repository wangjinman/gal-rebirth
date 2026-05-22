# Galgame 美术风格规范（项目通用）

> **用途**：生成立绘 / CG / 背景 / UI 时，请让 AI 先阅读本文件，并引用「参考图」路径。  
> **主参考角色**：林晚棠（**两套穿搭**：新式蓝白校服 · 约 2000 年代中式运动服）  
> **最后更新**：2026-05-21（序章 BG_19～23 + **CG_P01 定稿** · 规则入档）  
> **备份目录**：`J:\项目\GAL\美术资源初稿\_规范文档备份\`  
> **序章专档**：`背景\PROLOGUE_BG_RULES.md` · `CG\CG_P01_FINAL.md`

### 统一输出目录（必遵）

```
J:\项目\GAL\美术资源初稿\
├── 立绘\     ← 角色立绘、表情差分、半身 bust
├── 背景\     ← BG_* 场景图
├── CG\       ← CG_* 事件插画（全幅场景，非透明抠图）
└── UI\       ← UI_* 界面素材
```

- 生成工具可能先写入 Cursor 临时 `assets\`；**完成后必须复制到上表路径**，并向用户只报告 **J: 路径**。
- 详细流程见 `.cursor/rules/gal-asset-output-path.mdc`。

---

## 一、素材规格

| 类型 | 分辨率 | 格式 | 用途 |
|------|--------|------|------|
| 角色立绘 | **800×1200** 竖版 | PNG RGBA 透明底 | 母版全身；**游戏内日常对话用半身** `立绘\bust\*-bust-feather.png` |
| 背景图 (BG) | **1920×1080** 16:9 | PNG/JPG | 场景背景，默认 **空镜无人** |
| 事件 CG | **1920×1080** 16:9 | PNG 全幅插画 | 关键剧情；**不用透明底** |
| UI | 视需求 | PNG RGBA | 对话框等 |

- 立绘透明流程：`立绘\SPRITE_TRANSPARENT_WORKFLOW.md`
- UI 对话底栏：`UI\DIALOGUE_UI_MINIMAL_SPEC.md`

### 背景 / 事件 CG · AI 构图（必写）

```
1920x1080, 16:9 aspect ratio, wide horizontal landscape composition,
cinematic widescreen framing, full environment visible within wide frame,
NOT square, NOT portrait, NOT 4:3
```

生成后若不恰好 16:9，优先 **居中裁切铺满**；仅用户明确要求时留边缩放。

### 背景命名

```
BG_{编号}_{英文场景名}_{光线/时段}.png
```

备份：`{文件名去掉扩展名}_original.png`

### 背景后期（制作约定）

| 项目 | 约定 |
|------|------|
| AI 常见尺寸 | **1536×1024**（3:2）→ 目标 **1920×1080** |
| 铺满裁切 | 居中裁切（`背景\_crop_to_1920x1080.ps1`） |
| 保全景 | 留边缩放（`fit_1920x1080.ps1`，仅用户要求时） |
| 安全区 | 重要元素避开上下约 **12%** 边距（3:2 转 16:9 易切钟表、前景书） |
| 交付 | 生成后 **必须** `Copy-Item` 到 J 盘；对用户只报告 **J:** 路径 |
| Cursor 规则 | `.cursor/rules/gal-asset-output-path.mdc`、`galgame-art-style.mdc` |

---

## 二、整体美术风格

| 维度 | 要求 |
|------|------|
| 画风 | 日系精致平涂，Key / Summer Pockets 系 |
| 气质 | 温暖柔和；暗色 UI 配亮色角色 |
| 色调 | 暖色为主，暗部偏蓝紫 |
| 线条 | 纤细流畅 |
| 光影 | 柔光、糖光边缘高光 |
| 背景 | 手绘场景，非照片非 3D；默认空镜 |

**背景负面词**：`photorealistic, photograph, 3D render`；空镜加 `people, crowd`（用户明确要求路人/剪影时除外）。

**立绘负面词（摘录）**：`low quality, bad anatomy, nsfw, action lines, speed lines, realistic 3D, chibi`

---

## 三、林晚棠 · 角色设定卡

| 项目 | 设定 |
|------|------|
| 姓名 | 林晚棠 |
| 年龄 | 18 岁 |
| 发色 | 棕黑色长发，齐刘海 |
| 瞳色 | 琥珀色 / 金色 |
| 眼睛高光 | 左眼 1 大光点 + 右眼 2 小光点 |

### 校服 A 套（立绘默认）

白短袖衬衫、藏青领袖口、蓝白格纹蝴蝶结、左胸圆校徽、藏青百褶裙 **两条白色横条**、白膝袜、黑乐福鞋。

**参考**：`J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-800x1200.png` 或项目 `assets\lin-wantang-standing-800x1200.png`

### 校服 B 套（约 2000 年代运动服）

蓝白条运动服、胸标「临海中学」、红白条；差分默认半开拉链露白 T。感动落泪 **泪少**，禁止流到脖子。

**参考**：`J:\项目\GAL\美术资源初稿\立绘\lin-wantang-standing-2000s-tracksuit.png`

**要点**：蓝衣身、**白袖**、袖上 **蓝条**、胸背「临海中学」、红白条；差分默认 **半开拉链露白 T**。

### B 套 · 差分文件（白底定稿，待透明流程时逐张重做）

| 表情 | 文件 |
|------|------|
| 站立 | `lin-wantang-standing-2000s-tracksuit.png` |
| 平常 | `lin-wantang-2000s-expr-normal.png` |
| 微笑 | `lin-wantang-2000s-expr-smile-v2.png` |
| 害羞 | `lin-wantang-2000s-expr-shy.png` |
| 忧虑 | `lin-wantang-2000s-expr-worried.png` |
| 哭泣 | `lin-wantang-2000s-expr-cry-v2.png` |
| 感动落泪 | `lin-wantang-2000s-expr-cry-moved-v3.png`（**泪少**，禁流到脖子） |
| 惊喜 | `lin-wantang-2000s-expr-surprised.png` |

### 表情差分要点（A 套）

| 表情 | 必守 |
|------|------|
| 害羞 | 红晕、食指相抵，≠ 伤心 |
| 忧虑 | 蹙眉、托下巴，无眼泪 |
| 哭泣 | 伤心、泪多 |
| 感动落泪 | 嘴角略扬、泪少，左眼几乎仅水光 |
| 惊喜 | 单手捂嘴，无惊吓线 |

---

## 四、立绘透明底 · 流程摘要

> 完整步骤：`J:\项目\GAL\美术资源初稿\立绘\SPRITE_TRANSPARENT_WORKFLOW.md`

1. AI 生成 **洋红幕 #FF00FF**（禁止假透明/白底）
2. `sprite_chroma_feather.py` → `*-transparent-v1-feather.png`
3. `sprite_crop_bust.py` → `bust\*-bust-feather.png`（**游戏内默认**）
4. 一张一张做，勿批量抠旧白底

### A 套 · 引擎推荐文件

| 表情 | 游戏内（半身） | 母版（全身羽化） |
|------|----------------|------------------|
| 站立 | `bust\lin-wantang-standing-transparent-v1-bust-feather.png` | `lin-wantang-standing-transparent-v1-feather.png` |
| 微笑 | `bust\lin-wantang-expr-smile-v3-transparent-v1-bust-feather.png` | `lin-wantang-expr-smile-v3-transparent-v1-feather.png` |
| 害羞 | `bust\lin-wantang-expr-shy-v3-transparent-v1-bust-feather.png` | `lin-wantang-expr-shy-v3-transparent-v1-feather.png` |
| 忧虑 | `bust\lin-wantang-expr-worried-v2-transparent-v1-bust-feather.png` | `lin-wantang-expr-worried-v2-transparent-v1-feather.png` |
| 哭泣 | `bust\lin-wantang-expr-crying-v2-transparent-v1-bust-feather.png` | `lin-wantang-expr-crying-v2-transparent-v1-feather.png` |
| 感动 | `bust\lin-wantang-expr-crying-moved-v3-transparent-v1-bust-feather.png` | `lin-wantang-expr-crying-moved-v3-transparent-v1-feather.png` |
| 惊喜 | `bust\lin-wantang-surprised-v4-transparent-v1-bust-feather.png` | `lin-wantang-surprised-v4-transparent-v1-feather.png` |

---

## 五、背景资源清单（J 盘定稿 · 推荐进引擎）

路径根目录：`J:\项目\GAL\美术资源初稿\背景\`

| 编号 | **推荐定稿** | 场景 / 用途 |
|------|-------------|-------------|
| 01 | `BG_01_classroom_day.png` | 教室日景 |
| 02 | `BG_02_classroom_sunset.png` | 教室夕阳 |
| 03 | `BG_03_bedroom.png` | 卧室（2008 中式） |
| 04 | `BG_04_rooftop_sunset_golden.png` | 天台夕阳（日景） |
| 05 | `BG_05_library_day.png` | 图书馆午后 · 空镜 |
| 06 | `BG_06_corridor_afternoon.png` | 走廊午后 |
| 07 | `BG_07_park_bench_sunset.png` | **银杏**公园长椅 · 夕阳 |
| 08 | `BG_08_cafe_sunset.png` | 咖啡馆宽景夕阳 |
| 09 | `BG_09_rainy_street_night.png` | 雨夜街道（同街区） |
| 10 | `BG_10_residential_street_morning.png` | 住宅区上学路 · 空镜 · 樱花少 |
| — | `BG_pending_girl_bedroom_day.png` | **待定编号** · 女孩卧室日景 |
| 11 | `BG_11_living_room_afternoon.png` | 林晚棠家客厅 · 窗外见阳台 · Day12 |
| 12 | `BG_12_balcony_succulents_afternoon.png` | 小阳台 · **站阳台向外** · Day12 |
| 13 | `BG_13_mahjong_parlor_interior_v2_distant_players.png` | 棋牌室 · 前景空桌 · 远处牌友 · Day16 |
| 14 | `BG_14_cafe_bar_evening_near_bar.png` | 晚星咖啡馆 · 近吧台 · 桌椅同 BG_08 · Day15 |
| 15 | `BG_15_basketball_court_night_stars.png` | 篮球场夜景 · Day21 |
| 16 | `BG_16_rooftop_night_stars.png` | 天台星空 · Day23 告白高潮 |
| 17 | `BG_17_urban_street_dusk.png` | 城南街道黄昏 · 去棋牌室路上 · Day16 |
| 18 | `BG_18_park_corner_afternoon.png` | **银杏**公园午后 · Day18 喜悦 |
| 19 | `BG_19_bedroom_night_overtime.png` | **序章** · 现代**卧室**昏暗夜景 · 凌晨加班 |
| 19 | `BG_19_office_night_overtime.png` | **序章** · 现代**办公室**昏暗夜景 · 凌晨加班（与卧室版二选一） |
| 20 | `BG_20_consciousness_fading_er.png` | **序章** · 急救室意识模糊 / 倒下后过渡（抽象） |
| 21 | `BG_21_home_entrance_morning.png` | **序章** · 重生后住宅玄关清晨 ·「妈，我去上学了」 |
| 22 | `BG_22_school_gate_morning.png` | **序章** · 滨海一中校门清晨 · **空镜定稿**（= `_empty` 同图） |
| 23 | `BG_23_memory_fragment_transition.png` | **序章** · 记忆碎片解锁过渡 · **RGBA 透明底** |

### 序章专用背景（4.2）

> 序章「死亡与重生」须用 **情绪化背景** 替代纯黑屏。  
> 时间线：**BG_19** → **BG_20** → **BG_03** → **BG_21** → **BG_22**（校门）→ **BG_10** / 教室等。

#### BG_19 · 昏暗夜景·凌晨加班（现代 · ≠ BG_03 2008）

两版氛围一致，按剧本选 **卧室** 或 **办公室**：

| 项目 | 卧室版 | 办公室版 |
|------|--------|----------|
| 定稿 | `BG_19_bedroom_night_overtime.png` | `BG_19_office_night_overtime.png` |
| 场景 | 居家卧室、凌乱床铺边书桌 | 开放式/工位办公室、多显示器工位 |
| 共通氛围 | 昏暗、压抑、孤独、深蓝紫；屏幕蓝光 + 台灯暖橙、钟 **3:00**、窗外城市夜景 |
| 备份 | `…_bedroom_…_original.png` | `…_office_…_original.png` |

**卧室 · 英文提示词**：

```
chinese style dimly lit bedroom at night, late night atmosphere
dark room, computer monitor glowing blue light, desk lamp warm orange
papers scattered, messy bedroom, overturned chair, empty coffee cup
clock 3:00 AM, window city lights, lonely suffocating adult overtime
dark blue purple tones, 1920x1080 16:9, empty scene, no people
```

**办公室 · 英文提示词**：

```
chinese style dimly lit modern office at night, late night overtime
dark open-plan office, multiple computer monitors blue glow
desk lamp warm orange, scattered documents, empty coffee cups
overturned office chair, clock showing 3:00 AM
floor-to-ceiling windows city night lights outside
exhausted melancholic lonely atmosphere, dark blue purple tones
1920x1080, 16:9, empty scene, no people
```

#### BG_20 · 急救室 / 意识模糊底图

| 项目 | 约定 |
|------|------|
| 定稿 | `BG_20_consciousness_fading_er.png` |
| 用途 | 主角倒下后、意识消散前 **过渡**；可叠 `dissolve` / 慢速 `vpunch` |
| 氛围 | **纯白闪回**、意识消散、高光过曝、轻淡蓝白边缘（非深重暗角） |
| 画面 | 大面积柔白、头顶光晕溶入白、极淡白灰同心涟漪（可选叠心跳音效） |
| 备份 | `BG_20_consciousness_fading_er_original.png` |
| 旧版对比 | `_v1_soft_pulse`（弱脉冲）· `_v2_strong_pulse`（红粉强脉冲） |

**英文提示词（生成用）**：

```
pure white flashback scene, overwhelming bright white light flooding frame
high key exposure, bleached ethereal white dominant, near-death white light
bright white overhead hospital lights dissolved into white bloom
soft focus blur, lights bleeding into white, minimal pale blue at far edges only
faint soft white-gray concentric heartbeat rings barely visible in white haze
consciousness fading, dreamlike soul leaving body, emotional VN transition
NOT heavy dark vignette, NOT dominant red pulse
1920x1080, 16:9, no visible characters
```

#### BG_21 · 住宅玄关 / 鞋柜（重生后清晨）

| 项目 | 约定 |
|------|------|
| 定稿 | `BG_21_home_entrance_morning.png` |
| 用途 | 重生后 2008 线 ·「妈，我去上学了」；**妈妈仅画外音**，空镜暗示家庭 |
| 氛围 | 清晨、温暖、怀旧、温馨家庭感 |
| 画面元素 | 玄关落差地板、鞋架球鞋、门边雨伞、带镜鞋柜、挂外套/书包、门外晨光 |
| 备份 | `BG_21_home_entrance_morning_original.png` |

**英文提示词（生成用）**：

```
chinese style home entrance genkan, morning light
apartment entrance wooden genkan floor, shoes on shoe rack
umbrellas by the door, shoe cabinet with mirror, jackets hanging
warm morning sunlight streaming in from outside
cozy familiar nostalgic family home warmth, mother's presence implied only
peaceful morning scene, soft warm lighting, heartwarming atmosphere
2008 chinese family apartment feel, 1920x1080 16:9, empty scene, no people
```

#### BG_22 · 校门·日景（滨海市第一中学）

| 项目 | 约定 |
|------|------|
| **定稿（空镜）** | `BG_22_school_gate_morning.png` / `BG_22_school_gate_morning_empty.png` |
| 备选（有人潮） | `BG_22_school_gate_morning_with_students.png` |
| 用途 | 序章进入校园前；校牌 **「滨海市第一中学」** |
| 氛围 | 清晨、青春、蓝白色调、温暖阳光、怀旧校园感 |
| 画面元素 | 校门牌坊/石柱、校徽、樱花道、飘瓣、明亮早晨天空 |
| 备份 | `BG_22_school_gate_morning_original.png` |

**空镜 · 英文提示词（推荐）**：

```
chinese style school gate entrance, morning sunlight, EMPTY scene no people
Chinese high school gate, sign "滨海市第一中学" clearly readable
cherry blossom trees along path, petals falling, bright morning sky
youthful nostalgic clean campus entrance, school emblem on pillars
1920x1080, 16:9, no students, no crowd
```

**人潮版 · 英文提示词（备选）**：

```
... distant students blue white uniforms morning rush, no close-up faces
```

#### BG_23 · 记忆碎片特效背景

| 项目 | 约定 |
|------|------|
| **定稿（叠层用）** | `BG_23_memory_fragment_transition.png` — **PNG RGBA**，暗部透明 |
| 不透明备选 | `BG_23_memory_fragment_transition_opaque.png` — 全屏 `scene` 时用 |
| 用途 | 序章「记忆碎片」解锁过渡；叠在教室/玄关等 BG 之上 |
| 氛围 | **整屏碎裂仍连片**；各碎片区嵌入**朦胧回忆画面**（玄关/校门/教室/卧室/加班/客厅） |
| 制作 | 在 `_v3_shattered_only` 基础上合成项目 BG 缩略模糊图；裂缝暗部 Alpha 透明 |
| 旧版对比 | `_v1_small_fragments` · `_v2_large_fragments` · `_v3_shattered_only`（无回忆图） |
| 备份 | `BG_23_memory_fragment_transition_original.png` |

**英文提示词（生成用）**：

```
chinese style ethereal memory fragment transition, high quality
ENTIRE SCREEN connected shattered glass one plane, cracked but pieces still edge-to-edge together NOT fallen apart
full frame fracture lines radiating, large polygon shards, dark crack gaps, warm gold cool blue glow on edges
NOT floating separated debris NOT scattered small particles
soft glowing orbs, abstract geometric shapes, memory visualization
dreamlike time passing, nostalgic warm gold mixed cool blue
soft radial light from center, magical surreal emotional VN effect
beautiful particle effects, 1920x1080 16:9, no characters
```

**Ren'Py 叠层示例**：

```renpy
image memory_frag = "背景/BG_23_memory_fragment_transition.png"
# show memory_frag onlayer overlay zorder 100 with dissolve
```

### 场景衔接备忘

| 日程 | 路线 / 说明 | 文档 |
|------|-------------|------|
| Day12 | 客厅 → 阳台 | `背景\DAY12_lin_home_scene.md` |
| Day16 | 黄昏街道 → 棋牌室 | BG_17 → BG_13 |
| Day15 | 咖啡馆吧台 | BG_14（`near_bar` / `customer_view` 备选） |
| 同地点 | 天台：BG_04 日 / BG_16 夜；公园：BG_07 夕 / BG_18 午后 | — |
| 同街区 | BG_09 雨夜 / BG_17 黄昏 | — |
| **序章** | 加班倒下 **CG_P01** → 消散 → 重生 → 入校 | BG_19 → **CG_P01** → BG_20 → … |

### 背景备选（对比用，非默认）

- `BG_10_residential_street_morning_with_figures.png` — 含背影双人
- `BG_13_mahjong_parlor_interior.png` — 前景有牌友
- `BG_14_cafe_bar_evening_customer_view.png` — 顾客卡座视角
- `BG_12_balcony_succulents_afternoon_v1_large_shelf.png` 等 — 旧阳台大架

### 教室多视角 · 历史稿（对比用，非引擎默认）

| 文件 | 说明 |
|------|------|
| `BG_01_classroom_sunset_golden_v2.png` | 教室金色夕阳 |
| `BG_01_classroom_sunset_window.png` | 夕阳 · 窗边（室内方向） |
| `BG_01_classroom_sunset_facing_window.png` | 夕阳 · 面向窗外 |
| `BG_01_classroom_day_v2_anime.png` | 日景 · 画风参考 |
| `BG_03_bedroom_2008.png` | 2008 卧室早期稿 → 定稿 `BG_03_bedroom.png` |

---

## 六、事件 CG 清单

路径：`J:\项目\GAL\美术资源初稿\CG\`

| 编号 | **推荐定稿** | 说明 |
|------|-------------|------|
| P01 | `CG_P01_overtime_life_end.png` | **序章 P0 已定稿** · v4 构图 + **咬牙**（见 `CG_P01_FINAL.md`） |
| 01 | `CG_01_starry_sky_confession.png` | 星空告白 · 白连衣裙 · 天台夜景 |
| 02 | `CG_02_rainy_umbrella_school_uniform.png` | 雨中撑伞 · 校服 · 娇羞 · 伞遮男主 |
| 03 | `CG_03_rooftop_embrace.png` | 天台拥抱 · 校服 · 夕阳金时刻 |

**备选**：`CG_01_*_school_uniform.png`、`CG_02_rainy_umbrella_casual.png`、`CG_02_rainy_umbrella.png`（白裙）等。

> 事件 CG 为 **完整场景 1920×1080 PNG（不透明全幅）**，与 BG 叠用；勿做洋红抠图。序章 CG 可与 `BG_19_bedroom` 氛围统一。

#### CG-P01 · 加班夜·生命终结（序章行 28–40）✅ 已定稿

> 完整规则与迭代史：`CG\CG_P01_FINAL.md`

| 项目 | 约定 |
|------|------|
| 定稿 | `CG_P01_overtime_life_end.png`（**用户确认 2026-05-21**） |
| 情绪 | 痛苦、挣扎、孤独、终结 ★★★★★ |
| 构图 | **v4 基线**：大侧脸、前倾栽桌、膝在椅/脚踩地、四肢自然 |
| 表情 | **咬牙**（禁止张嘴）；皱眉、冷汗可加 |
| 手机 | 下落中或触地碎屏，**禁止空中已碎** |
| 光线 | 显示器冷蓝光自下 vs 暖橙台灯 |
| 格式 | 1920×1080 **不透明**全幅 CG |
| 旧版 | `_v1`～`_v3`、`_v4`（张嘴）、`_v4b`（勿删） |
| 衔接 | `BG_19` → **CG_P01** → `BG_20` |

**续作 / 微调**：以 `_v4.png` 为参考，**仅改指定项**（如当初「只改张嘴→咬牙」）。

**英文提示词（定稿摘要）**：

```
side profile large face, slumping forward off chair toward desk, knees on seat feet on floor
clenched teeth NOT open mouth, hand on chest, phone falling to floor crack on impact
monitor blue light from below vs warm orange lamp, dim bedroom overtime, 1920x1080 VN CG
```

---

## 七、UI 资源（暂定）

| 文件 | 说明 |
|------|------|
| `UI_02_dialogue_minimal_wantang_posA_overflow_top.png` | 对话底栏 · 立绘头上探 · **1920×440** |
| `UI_02_narration_minimal_v2_left_weight.png` | 旁白 · 无立绘 · 左侧加重 |
| `UI_02_narration_minimal_v2_center.png` | 旁白 · 居中窄栏（对比） |
| `UI_01_dialogue_box.png` | 早期 Gal 对话框模板（已由 UI_02 取代） |

规范：`UI\DIALOGUE_UI_MINIMAL_SPEC.md`  
重建：`UI\scripts\build_dialogue_ui_minimal_posA.py` 等

**Ren'Py 底对齐**：`xalign 0.5`、`yalign 1.0`

---

## 八、后期脚本（J 盘 / 临时）

| 脚本 | 用途 |
|------|------|
| `立绘\scripts\sprite_chroma_feather.py` | 洋红幕色键 + 羽化 |
| `立绘\scripts\sprite_crop_bust.py` | 半身裁切 |
| `UI\scripts\build_dialogue_ui_minimal_posA.py` | 对话条 posA |
| `UI\scripts\build_dialogue_ui_narration_v2.py` | 旁白条对比稿 |
| `背景\_crop_to_1920x1080.ps1` | 裁切 1920×1080 |

PowerShell 中文路径失败时，可将脚本复制到 `C:\Users\wangjinman\AppData\Local\Temp\` 再运行。

---

## 九、给 AI 的使用说明

```
请阅读 assets/ART_STYLE_GUIDE.md，按林晚棠风格生成 [描述]。
参考图：assets/lin-wantang-standing-800x1200.png
```

**背景**：

```
请阅读 ART_STYLE_GUIDE 第一节构图要求，生成 1920x1080 横版空镜背景，命名 BG_xx_...
交付 J:\项目\GAL\美术资源初稿\背景\
```

**运动服套**：

```
参考 lin-wantang-standing-2000s-tracksuit.png，声明 B 套，勿与 A 套混穿。
```

---

## 十、工作记录与制作履历

> 原 `WORK_LOG_2026-05-18.md` 已合并入本节；旧文件保留为归档指针。

### 2026-05-18 · 基建

| 类别 | 完成项 |
|------|--------|
| 规范 | 统一 J 盘输出；`gal-asset-output-path.mdc`、`galgame-art-style.mdc` |
| 背景 | BG_01 教室多视角、BG_03～08、图书馆空镜等（见第五节「历史稿」） |
| B 套 | 运动服站立 + 6 表情白底差分；感动落泪 v3 定稿 |
| UI | `UI_01_dialogue_box.png` 首版对话框 |

### 2026-05-19 · 立绘 / UI / 场景扩展

| 类别 | 完成项 |
|------|--------|
| A 套透明 | `SPRITE_TRANSPARENT_WORKFLOW.md`；洋红幕 → 色键 → 羽化；7 张全身羽化；旧白底保留 |
| 半身 | `bust\*-bust-feather.png` 定为游戏内默认（`BUST_HEIGHT_RATIO=0.62`） |
| UI_02 | 对话条 posA 上探定稿；旁白 left_weight / center 对比稿 |
| 背景 | BG_08 咖啡馆；BG_09～18；林晚棠家 BG_11→12（`DAY12_lin_home_scene.md`） |
| CG | CG_01 星空告白、CG_02 雨中撑伞、CG_03 天台拥抱 |
| 文档 | 规范恢复；磁盘满导致 `ART_STYLE_GUIDE` 空文件后重建 |

### 2026-05-21 · 序章资产全日（BG_19～23 + CG_P01 定稿）

| 类别 | 完成项 |
|------|--------|
| 文档 | WORK_LOG 合并；`_规范文档备份\`；`PROLOGUE_BG_RULES.md`、`CG_P01_FINAL.md` |
| BG_19 | 卧室 + 办公室双版加班夜 |
| BG_20 | 意识消散；定稿纯白闪回 RGBA（`_v1`/`_v2` 脉冲备份） |
| BG_21 | 玄关清晨「去上学」 |
| BG_22 | 滨海一中校门；**空镜定稿**（`_with_students` 备选） |
| BG_23 | 整屏碎裂连片 + 碎片区回忆合成；RGBA 叠层 |
| **CG_P01** | **P0 定稿**：v4 前倾栽桌 + **咬牙**（弃 v3 扭肢、弃 v4b） |

---

## 十一、经验备忘

1. 背景默认 **空镜**；不要中央醒目角色（路人/剪影须用户明确要求）。
2. 3:2 裁 16:9 会切掉贴边钟表、前景书 → 构图内收或改用留边缩放。
3. 生成后必须复制到 **J 盘**；回复路径只写 `J:\项目\GAL\...`。
4. 背景若需 B 套运动服，必须 `@` 运动服参考并写清白袖蓝条。
5. **立绘勿用白底批量抠图 / rembg 定稿**；洋红幕 + 色键 + 羽化（见流程文档）。
6. `GenerateImage` 保存失败时缩短文件名（如 `s1.png`、`bg14.png`）。
7. PowerShell 中文路径失败 → 脚本放 `C:\Users\wangjinman\AppData\Local\Temp\` 用 Python 写 J 盘。
8. 规范大改后更新 `_规范文档备份\` 并追加 `ART_STYLE_GUIDE_YYYY-MM-DD.md` 快照。
9. **序章**：演出顺序见 `背景\PROLOGUE_BG_RULES.md`；**CG_P01** 已定稿，修改用 `_v4.png` 参考且尽量只改单项。
10. **事件 CG** 全幅不透明；**BG_23 / BG_20** 为 RGBA 叠层，裂缝暗部透明。
11. **CG 痛感** 提示词避免过激用语以防生成审核失败；构图优先「前倾栽桌 + 侧脸」。

---

## 十二、待办

| 状态 | 事项 |
|------|------|
| 待定 | 旁白条定稿：`left_weight` vs `center` |
| 待定 | 咖啡馆视角：`near_bar` vs `customer_view` |
| 待定 | B 套 7 张是否走洋红幕透明 + bust（与 A 套同流程） |
| 可选 | 批量同步 Cursor 临时 `assets\` → J 盘（`sync_from_cursor_assets.ps1`） |
| 可选 | 将备选 CG/BG 覆盖为唯一定稿文件名 |

---

## 十三、修订记录

| 日期 | 内容 |
|------|------|
| 2026-05-18 | 输出目录、Cursor 规则、B 套、教室/公园等早期 BG、UI_01 |
| 2026-05-19 | 立绘洋红幕色键 + A 套 7 张；半身 bust 定稿 |
| 2026-05-19 | UI_02 对话条 posA；旁白条 |
| 2026-05-19 | BG_09～18、CG_01～03、林晚棠家 Day12 衔接 |
| 2026-05-19 | **恢复本文档**（磁盘满导致空文件后的完整版重建） |
| 2026-05-21 | WORK_LOG 合并；J 盘 `_规范文档备份\` |
| 2026-05-21 | 序章 BG_19 昏暗现代卧室·加班夜 |
| 2026-05-21 | 序章 BG_19 办公室版 `BG_19_office_night_overtime.png` |
| 2026-05-21 | 序章 BG_21 住宅玄关清晨 `BG_21_home_entrance_morning.png` |
| 2026-05-21 | 序章 BG_22 滨海一中校门日景 `BG_22_school_gate_morning.png` |
| 2026-05-21 | BG_22 空镜定稿；人潮版备份 `_with_students` |
| 2026-05-21 | 序章 BG_23 记忆碎片 RGBA 透明过渡 |
| 2026-05-21 | BG_23 大块碎片定稿；v1 `_small_fragments` 备份 |
| 2026-05-21 | BG_23 整屏碎裂连片定稿；v2 `_large_fragments` 备份 |
| 2026-05-21 | BG_23 碎片区嵌入回忆场景（合成版） |
| 2026-05-21 | 序章 CG_P01 加班夜生命终结 |
| 2026-05-21 | CG_P01 v2：痛感加强、手机下落触地碎屏 |
| 2026-05-21 | CG_P01 v3：大侧脸 + 滑出椅子倒下 |
| 2026-05-21 | CG_P01 v4：前倾栽桌、四肢自然定稿 |
| 2026-05-21 | CG_P01 v4b：表情更狰狞、身体更多倒出椅子 |
| 2026-05-21 | 定稿回 v4 基线，仅改张嘴→咬牙 |
| 2026-05-21 | 序章 BG_20 急救室意识模糊过渡 |
| 2026-05-21 | BG_20 加强心跳脉冲；v1 备份为 `_v1_soft_pulse` |
| 2026-05-21 | BG_20 定稿改为纯白闪回；v2 备份 `_v2_strong_pulse` |
| 2026-05-21 | **CG_P01 用户确认定稿**；专档 `CG_P01_FINAL.md`、`PROLOGUE_BG_RULES.md` |

---

*维护：新增 BG/CG/立绘后更新第五节、第六节表格与第十节履历；序章见 PROLOGUE_BG_RULES；大改后执行备份。*
