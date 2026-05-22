# 《重生·轻逆袭》美术素材AI提示词 - 专用文档

> **文档编号**：GAL-PROMPT-001
> **版本**：v1.7
> **日期**：2026-05-20
> **状态**：正式使用中
> **用途**：所有美术素材AI生成提示词的统一管理文档
> **生成工具建议**：Midjourney / Stable Diffusion XL / DALL-E 3
>
> ⚠️ **重要声明**：本文档为美术素材AI提示词专用文档，今后所有美术素材生成的提示词都应记录在本文件中，并在更新时递增版本号。

---

## 版本记录

| 版本 | 日期 | 更新内容 | 负责人 |
|------|------|----------|--------|
| v1.0 | 2026-05-15 | 初始版本，包含第一批Demo素材提示词 | AI辅助 |
| v1.1 | 2026-05-18 | 扩充背景素材（+5张天台/图书馆/走廊/公园/咖啡馆），完善UI素材（12个组件） | AI辅助 |
| v1.2 | 2026-05-18 | 添加透明背景核心关键词，所有立绘提示词更新 | AI辅助 |
| v1.3 | 2026-05-18 | 融合桌面版v1.1与现有v1.2，完善素材清单状态追踪、背景+UI提示词完整性 | AI辅助 |
| v1.4 | 2026-05-20 | 批量更新素材状态（林晚棠6立绘+8背景+UI-01均已完成），新增雨夜街道背景提示词 | AI辅助 |
| v1.5 | 2026-05-20 | 新增9张背景图提示词（住宅3张+棋牌室+咖啡馆+篮球场+天台星空夜景等），完善素材清单状态追踪 | AI辅助 |
| v1.6 | 2026-05-20 | 新增5张序章背景图提示词（卧室夜景+急救室+玄关+校门日景+记忆碎片特效） | AI辅助 |
| v1.7 | 2026-05-20 | 新增2张序章CG提示词（加班猝死+意识消散），完善序章素材优先级分析 | AI辅助 |

---

## 一、美术风格指南

### 1.1 整体风格定位

| 维度 | 要求 |
|------|------|
| **画风** | 日系精致平涂风格，柔和光影 |
| **色调** | 暖色调为主（橙/粉/米色），暗部偏蓝紫 |
| **线条** | 纤细流畅，轮廓清晰 |
| **光影** | 柔光，日系常用"糖光"效果 |
| **质感** | 皮肤通透，眼神有光点 |

### 1.2 统一视觉规范

```
【必须统一】
✓ 人物面部比例：日系三庭五眼
✓ 瞳色：每角色固定色系（见角色设定）
✓ 发色：每角色固定色系（见角色设定）
✓ 眼睛高光：左眼1个大光点+右眼2个小光点（增强灵动）
✓ 服装：校服（林晚棠/周芷晴/陈墨）、便装（苏念卿）、病服（沈听雨）

【禁止出现】
✗ 成人化/暴露服装
✗ 过度美式写实风格
✗ 动漫过度简化（蛋卷头+大眼睛）
✗ 过度液化/失真的"网红脸"
```

### 1.3 配色方案

| 角色 | 发色 | 瞳色 | 主色调 | 辅助色 |
|------|------|------|--------|--------|
| 林晚棠 | 棕黑色长发 | 琥珀色 | 暖橙 | 米白、淡粉 |
| 苏念卿 | 深栗色中长发 | 灰蓝色 | 咖啡棕 | 奶白、酒红 |
| 周芷晴 | 橙黄色高马尾 | 翠绿色 | 阳光黄 | 活力橙、白色 |
| 陈墨 | 黑色齐肩短发 | 银灰色 | 冷灰 | 靛蓝、纯白 |
| 沈听雨 | 银白色长发 | 淡紫色 | 神秘紫 | 烟灰、月白 |

---

## 二、第一批素材清单（Demo用）

### 2.1 优先级说明

| 批次 | 优先级 | 素材类型 | 数量 | 用途 | 状态 |
|------|--------|---------|------|------|------|
| **P0** | 最高 | 林晚棠立绘（6表情） | 6张 | Demo核心展示 | ✅ 已完成 |
| **P0** | 最高 | 教室背景（日景） | 1张 | 序章+第一章 | ✅ 已完成 |
| **P0** | 最高 | 教室背景（窗外夕阳） | 1张 | 林晚棠关键场景 | ✅ 已完成 |
| **P0** | 最高 | 主角卧室背景 | 1张 | 日常场景 | ✅ 已完成 |
| **P0** | 高 | 学校天台（黄昏） | 1张 | 关键浪漫场景 | ✅ 已完成 |
| **P0** | 高 | 学校图书馆 | 1张 | 学习/安静对话 | ✅ 已完成 |
| **P0** | 高 | 学校走廊 | 1张 | 课间/转场 | ✅ 已完成 |
| **P0** | 高 | 公园长椅（黄昏） | 1张 | 约会场景 | ✅ 已完成 |
| **P0** | 高 | 咖啡馆内景 | 1张 | 苏念卿线/约会 | ✅ 已完成 |
| **P0** | 高 | 住宅门口/上学路 | 1张 | Day 8上学同行 | 🔲 待生成 |
| **P0** | 高 | 住宅室内客厅 | 1张 | Day 12 去林晚棠家 | 🔲 待生成 |
| **P0** | 高 | 住宅阳台(多肉) | 1张 | Day 12 照顾多肉 | 🔲 待生成 |
| **P0** | 高 | 棋牌室 | 1张 | Day 16 说服林父 | 🔲 待生成 |
| **P0** | 高 | 卧室·昏暗夜景 | 1张 | 序章"加班夜" | 🔲 待生成 |
| **P0** | 高 | 急救室/意识模糊底图 | 1张 | 序章死亡过渡 | 🔲 待生成 |
| **P1** | 高 | 咖啡馆内景(Day15剧情) | 1张 | Day 15 获取情报 | 🔲 待生成 |
| **P1** | 高 | 玄关/鞋柜 | 1张 | 序章"妈，我去上学了" | 🔲 待生成 |
| **P1** | 高 | 校门·日景 | 1张 | 序章进入校园 | 🔲 待生成 |
| **P1** | 高 | 篮球场夜景/星空 | 1张 | Day 21 告白前夜 | 🔲 待生成 |
| **P1** | 高 | 天台星空夜景 | 1张 | Day 23 告白场景 | 🔲 待生成 |
| **P1** | 高 | 对话框底栏 | 1个 | 核心UI | ✅ 已完成 |
| **P1** | 高 | 选择菜单按钮 | 3状态 | 选项UI | 🔲 待生成 |
| **P1** | 高 | 主菜单背景 | 1张 | 启动界面 | 🔲 待生成 |
| **P1** | 高 | 存档/读档槽位 | 2个 | 存档界面 | 🔲 待生成 |
| **P1** | 高 | 快捷菜单图标组 | 6个 | 对话框上方 | 🔲 待生成 |
| **P1** | 高 | 好感度浮动提示 | 2个 | HUD动态 | 🔲 待生成 |
| **P2** | 中 | 章节标题卡片 | 若干 | 过渡效果 | 🔲 待生成 |
| **P2** | 中 | 设置面板 | 1个 | 选项界面 | 🔲 待生成 |
| **P2** | 中 | 历史记录面板 | 1个 | 回看功能 | 🔲 待生成 |
| **P2** | 中 | 确认对话框 | 1个 | 确认弹窗 | 🔲 待生成 |
| **P2** | 中 | 游戏标题Logo | 1个 | 主菜单 | 🔲 待生成 |

---

## 三、核心提示词规范

### 3.1 ⚠️ 透明背景要求（必读）

> **重要**：立绘必须使用透明背景，否则游戏显示会有白色方块！

#### 透明背景核心关键词（立绘必加）

| 关键词 | 作用 |
|--------|------|
| `transparent background` | 透明背景，PNG格式 |
| `no background` | 无背景 |
| `PNG` | 确保输出PNG格式 |
| `alpha channel` | 保留透明度通道 |
| `properly transparent` | 正确透明处理 |

#### 透明背景完整示例

```
beautiful anime girl, long dark brown hair, amber eyes
school uniform, upper body portrait
transparent background, PNG, properly transparent, alpha channel
clean lineart, soft warm lighting, Japanese anime style
best quality, masterpiece
negative prompt: white background, black background, solid background, watermark, cropped, worst quality
```

### 3.2 负面提示词（所有素材必用）

```
low quality, bad anatomy, extra limbs, missing fingers, extra fingers
ugly, disfigured, mutated, blurry, blurry eyes, empty eyes
bad proportions, cropped, worst feet, mutation hands
nsfw, nake, adult, sexy, revealing clothes
realistic style, 3D render, photo
western cartoon style, chibi
white background, black background, solid background, watermark
```

---

## 四、AI绘图提示词

### 4.1 林晚棠立绘（6表情）

---

#### 【晚棠-01】标准立绘（默认表情）

**用途**：游戏开始、对话默认展示

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair, sitting at a desk
her hair is flowing naturally, with soft highlights
amber/golden eyes, gentle expression, slight smile
wearing a standard Chinese high school uniform (blue and white), crisp and clean
looking slightly forward, gentle and soft atmosphere
warm lighting from the left side, soft shadows
transparent background, PNG, properly transparent, alpha channel
clean lineart, detailed face, sparkling eyes with highlight, translucent skin
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发，坐在书桌前
头发自然垂落，带有柔和的高光
琥珀色眼睛，温柔的表情，嘴角微微上扬
穿着标准中式高中校服（蓝白色），整洁干净
微微向前看，温柔柔和的氛围
左侧暖光照射，柔和阴影
透明背景，PNG格式，正确透明处理，保留透明度通道
干净的线稿，精细的面部描写，闪亮的眼睛带高光，通透的皮肤
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：标准、平静、温和、默认

**规格要求**：
- 分辨率：800×1200px（竖版立绘比例）
- 格式：PNG透明背景
- 精度：300DPI

---

#### 【晚棠-02】微笑表情（开心/认可时）

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair
bright happy smile, eyes slightly closed in happiness, genuine warm smile
amber/golden eyes, sparkling with joy
wearing a standard Chinese high school uniform (blue and white)
warm golden hour lighting, cheerful atmosphere
transparent background, PNG, properly transparent, alpha channel
clean lineart, flushed cheeks from happiness, delicate features
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发
灿烂的笑容，眼睛因开心微微眯起，真诚温暖的笑容
琥珀色眼睛，因喜悦而闪烁
穿着标准中式高中校服（蓝白色）
金色时刻的暖光照射，欢快的气氛
透明背景，PNG格式，正确透明处理
干净的线稿，因开心而泛红的脸颊，精致五官
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：开心、感动、温暖微笑

---

#### 【晚棠-03】害羞表情（心动/告白场景）

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair
embarrassed expression, slightly blushing cheeks, shy smile, eyes looking away
amber/golden eyes with soft blush on cheeks, shyly averting gaze
wearing a standard Chinese high school uniform (blue and white)
heartbeat atmosphere, romantic soft pink lighting
transparent background, PNG, properly transparent, alpha channel
clean lineart, hand near chest in shy gesture, delicate features, translucent skin
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发
害羞的表情，脸颊微微泛红，羞涩的微笑，眼神看向别处
琥珀色眼睛，脸颊泛红，羞涩地避开视线
穿着标准中式高中校服（蓝白色）
心跳加速的氛围，浪漫的柔和粉色光线
透明背景，PNG格式，正确透明处理
干净的线稿，手放在胸口做害羞姿势，精致五官，通透皮肤
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：害羞、心动、温馨、脸红、紧张又幸福

---

#### 【晚棠-04】忧虑表情（担忧/纠结时）

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair
worried expression, slightly furrowed brows, melancholic smile, contemplative eyes
amber/golden eyes, eyes looking down slightly, vulnerable feeling
wearing a standard Chinese high school uniform (blue and white)
soft blue and purple ambient lighting, somber atmosphere
transparent background, PNG, properly transparent, alpha channel
clean lineart, hands clasped together nervously, delicate features
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发
忧虑的表情，眉心微蹙，忧郁的微笑，沉思的眼神
琥珀色眼睛，眼神微微下垂，脆弱感
穿着标准中式高中校服（蓝白色）
柔和的蓝紫色环境光，忧郁的氛围
透明背景，PNG格式，正确透明处理
干净的线稿，双手紧张地交握，精致五官
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：担忧、纠结、焦虑、脆弱、忧郁微笑

---

#### 【晚棠-05】哭泣表情（伤心/感动时）

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair
tears welling up in eyes, crying softly, emotional expression
amber/golden eyes, crystal teardrops on cheeks, heartbreaking beauty
wearing a standard Chinese high school uniform (blue and white)
soft blue lighting, emotional and touching atmosphere
transparent background, PNG, properly transparent, alpha channel
clean lineart, tears streaming down, trembling lips, vulnerable and delicate
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发
眼眶泛泪，轻轻哭泣，情绪化的表情
琥珀色眼睛，晶莹的泪珠滑落脸颊，令人心碎的美
穿着标准中式高中校服（蓝白色）
柔和的蓝色光线，情绪化和感人的氛围
透明背景，PNG格式，正确透明处理
干净的线稿，泪水滑落，嘴唇颤抖，脆弱而精致
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：哭泣、泪眼婆娑、情绪化、心碎、感动落泪

---

#### 【晚棠-06】惊喜表情（震惊/重大发现时）

**英文正向提示词**：
```
anime style illustration, high quality, detailed, Japanese visual novel art style
a beautiful 18-year-old Chinese girl with long dark brown hair
shocked expression, eyes wide open, surprised and stunned
amber/golden eyes, pupils dilated from surprise, mouth slightly open
wearing a standard Chinese high school uniform (blue and white)
dramatic lighting from below, intense atmosphere
transparent background, PNG, properly transparent, alpha channel
clean lineart, hands raised to cheeks in shock, dramatic moment
masterpiece, best quality, 2D game sprite, visual novel character sprite
```

**中文参考**：
```
日系动漫风格插画，高质量，精细，视觉小说艺术风格
一位美丽的18岁中国女孩，长长的棕黑色头发
震惊的表情，眼睛睁大，惊讶和惊呆
琥珀色眼睛，因惊讶而瞳孔放大，嘴巴微微张开
穿着标准中式高中校服（蓝白色）
底部戏剧性光线，紧张的氛围
透明背景，PNG格式，正确透明处理
干净的线稿，双手举起放在脸颊边做震惊姿势，戏剧性时刻
杰作，最高品质，2D游戏立绘，视觉小说角色立绘
```

**角色表情**：震惊、惊讶、惊呆、惊叹、目瞪口呆

---

### 4.2 背景素材（Demo用）

---

#### 【背景-01】普通教室（日景）

**英文正向提示词**：
```
Japanese style classroom interior, anime background, high quality
daytime, bright sunlight streaming through windows, warm lighting
20+ wooden desks and chairs arranged neatly in rows
blackboard in front with "Class 3" written on it, classroom poster on wall
bulletin board with student work displayed
slightly messy teacher's desk, textbooks stacked
students' bags and water bottles on desks
wide shot, showing the whole classroom
cinematic composition, detailed environment
clean and bright atmosphere, nostalgic school feeling
```

**中文参考**：
```
日式风格教室内部，动漫背景，高质量
白天，明亮的阳光透过窗户洒入，暖色调光线
20多张整齐排列的木制课桌椅
前方黑板写着"高三三班"，墙上有教室海报
公告板展示着学生的作品
稍微凌乱的讲台，书堆叠在一起
学生书包和水瓶放在桌上
宽镜头，展示整个教室
电影感构图，精细的环境细节
干净明亮的氛围，怀旧的校园感
```

**规格要求**：
- 分辨率：1920×1080px（16:9宽屏）
- 格式：PNG/JPG
- 精度：300DPI

---

#### 【背景-02】教室窗边（夕阳场景）

**英文正向提示词**：
```
Japanese style classroom, anime background, high quality
golden sunset hour, beautiful orange and pink gradient sky outside window
long school desk near the window, student chair beside it
warm golden hour light streaming in, dramatic shadows
窗外夕阳西下，橙粉色渐变天空
窗外可见操场和远处的城市天际线
dust particles floating in the golden sunlight beam
bokeh effect in background, dreamy atmosphere
romantic and nostalgic feeling, pivotal scene moment
cinematic composition, soft focus foreground
beautiful light and shadow play, emotional scene
```

**中文参考**：
```
日式风格教室，动漫背景，高质量
金色夕阳时分，窗外美丽的橙粉色渐变天空
靠窗的长书桌，旁边是学生椅
暖金色光线洒入，戏剧性的光影
窗外可见操场和远处的城市天际线
金色阳光光束中漂浮的尘埃粒子
背景散景效果，梦幻般的氛围
浪漫怀旧的感觉，关键场景时刻
电影感构图，柔和对焦前景
美丽的光影交织，情绪化的场景
```

**用途**：林晚棠关键场景（前世最遗憾的瞬间复现）

---

#### 【背景-03】主角卧室

**英文正向提示词**：
```
Japanese style bedroom interior, anime background, high quality
small but cozy bedroom, afternoon soft light
single bed with blue quilt, neat and simple
wooden desk with computer monitor, textbooks and notebooks
small bookshelf filled with books, manga on shelf
window with light curtains, afternoon sun streaming in
wall poster of some anime or band (subtle)
closet door slightly open, clothes hanging outside
messy but lived-in feeling, realistic details
clean floor, houseplant on windowsill
nostalgic teenage bedroom atmosphere
```

**中文参考**：
```
日式风格卧室内部，动漫背景，高质量
小巧温馨的卧室，下午柔和的光线
铺着蓝色被子的单人床，简洁整齐
带电脑显示器的木书桌，课本和笔记本
装满书籍的小书架，架子上有漫画
带轻纱的窗户，下午阳光洒入
墙上贴着动漫或乐队的海报（低调）
衣柜门微开，衣服挂在外面
有点凌乱但有生活感，真实的细节
干净的地板，窗台上有绿植
怀旧的青少年卧室氛围
```

---

#### 【背景-04】学校天台（黄昏）

**用途**：关键浪漫场景、谈心、告白预备

**英文正向提示词**：
```
anime style school rooftop background, high quality
golden sunset hour, beautiful orange and pink gradient sky
chain-link fence at the edge, rooftop water tank in distance
city skyline visible in the far background, silhouette buildings
warm golden hour lighting, dramatic shadows on concrete floor
clothes poles with white shirts fluttering in wind
dramatic and romantic atmosphere, cinematic composition
emotional scene location, vast sky occupying upper half
```

**中文参考**：
```
日式风格学校天台背景，动漫背景，高质量
金色夕阳时分，美丽的橙粉色渐变天空
边缘有铁丝网围栏，远处天台水箱
远景可见城市天际线，建筑剪影
暖金色光线，混凝土地面上的戏剧性阴影
晾衣杆上白衬衫在风中飘动
戏剧性和浪漫的氛围，电影感构图
情绪化场景地点，上半部分是大片天空
```

**规格要求**：
- 分辨率：1920×1080px（16:9宽屏）
- 格式：PNG/JPG

---

#### 【背景-05】学校图书馆

**用途**：一起学习、安静对话场景

**英文正向提示词**：
```
anime style school library background, high quality
rows of bookshelves filled with books, warm reading lamps
large windows with soft daylight streaming in
wooden study tables with students studying quietly
"Silence" sign on wall, clock on pillar
soft warm lighting, quiet and studious atmosphere
detailed environment, cinematic composition
depth of field, foreground books slightly blurred
```

**中文参考**：
```
日式风格学校图书馆背景，动漫背景，高质量
一排排满书的书架，暖色阅读灯
大窗户透入柔和日光
木质自习桌，学生们安静地学习
墙上"静"字标识，柱子上的时钟
柔和暖光，安静而好学的故事氛围
精细环境，电影感构图
景深效果，前景书籍轻微模糊
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-06】学校走廊

**用途**：课间对话、偶遇、转场

**英文正向提示词**：
```
anime style school corridor background, high quality
long corridor with classroom doors on both sides
lockers along the wall, afternoon sun through windows
shadows of window frames on floor, dust particles in light beams
notice board on wall with papers pinned
shallow depth of field, school life atmosphere
clean and bright, nostalgic feeling
```

**中文参考**：
```
日式风格学校走廊背景，动漫背景，高质量
两侧有教室门的长走廊
墙边储物柜，下午阳光透过窗户
窗框影子落在地板上，光柱中的尘埃粒子
墙上公告板贴着纸张
浅景深，校园生活氛围
干净明亮，怀旧感
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-07】公园长椅（黄昏）

**用途**：约会场景、关键对话

**英文正向提示词**：
```
anime style park bench background, high quality
wooden bench under a large cherry blossom tree (or ginkgo tree)
sunset lighting, golden hour, warm orange and pink sky
cherry blossom petals floating in the air (or ginkgo leaves)
pathway in background, street lamp starting to glow
romantic atmosphere, bokeh effect on background foliage
cinematic composition, emotional scene location
```

**中文参考**：
```
日式风格公园长椅背景，动漫背景，高质量
大樱花树下（或银杏树）的木制长椅
夕阳光线，金色时刻，暖橙粉天空
樱花花瓣在空中飘舞（或银杏叶）
背景是小径，街灯开始发光
浪漫氛围，背景树叶散景效果
电影感构图，情绪化场景地点
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-08】咖啡馆内景

**用途**：苏念卿线关键场景，也可用于林晚棠约会

**英文正向提示词**：
```
anime style cozy cafe interior background, high quality
wooden counter with coffee machine, shelves with mugs and books
warm amber lighting, pendant lamps hanging from ceiling
round tables with chairs, some occupied by customers (silhouettes)
large windows with sunset visible outside
cozy and warm atmosphere, detailed environment
cinematic composition, depth of field
```

**中文参考**：
```
中式风格温馨咖啡馆内景背景，动漫背景，高质量
木质柜台配咖啡机，架子上的马克杯和书籍
暖琥珀色灯光，吊灯从天花板垂下
圆桌配椅子，一些被顾客（剪影）占用
大窗户可见外面夕阳
温馨舒适的氛围，精细环境
电影感构图，景深效果
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-09】雨夜街道

**用途**：林晚棠线Day 10关键场景，雨中对话

**英文正向提示词**：
```
anime style rainy night street background, high quality
heavy rain, wet pavement reflecting street lights
orange and yellow light pools from street lamps
umbrellas scattered on street, silhouettes in rain
night atmosphere, melancholic and emotional mood
rain droplets on camera lens effect, bokeh lights
distant buildings with warm windows, cold blue tones
romantic but sad atmosphere, anime visual novel style
cinematic composition, dramatic lighting contrast
```

**中文参考**：
```
日系风格雨夜街道背景，高质量
大雨倾盆，湿润的地面反射路灯灯光
橙黄色光斑从路灯洒下
街道上散落的雨伞，雨中的身影剪影
夜晚氛围，忧郁情绪化的氛围
镜头雨滴效果，散景灯光
远处建筑透着温暖灯光，冷蓝色调
浪漫但伤感的氛围，动漫视觉小说风格
电影感构图，戏剧性光线对比
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-10】住宅区街道（上学路上）

**用途**：Day 8 早晨和女生一起上学的场景

**英文正向提示词**：
```
anime style residential neighborhood street, morning sunlight
quiet suburban area, Japanese style apartment buildings
morning golden sunlight through cherry blossom trees
boy and girl walking together to school, back view
blue and white school uniforms, gentle morning breeze
cherry blossom petals on the path, nostalgic atmosphere
clean street with subtle shadows, cinematic composition
warm and peaceful morning scene, anime visual novel background
```

**中文参考**：
```
日系住宅区街道，清晨阳光
安静的郊区，日式公寓楼
晨间金色阳光透过樱花树
男生女生一起上学，背影
蓝白色校服，柔和晨风
道路上的樱花花瓣，怀旧氛围
干净的街道，微妙的阴影，电影感构图
温暖平和的清晨场景，动漫视觉小说背景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-11】住宅室内客厅

**用途**：Day 12 去林晚棠家做客，室内对话场景

**英文正向提示词**：
```
anime style cozy living room interior, afternoon soft light
Japanese style apartment, wooden furniture
warm afternoon sunlight through curtains
comfortable sofa, small茶几 with tea cups
green plants in corner, bookshelf with books
neat and tidy, homey atmosphere
heartwarming family living room, anime background
soft bokeh effect, nostalgic and peaceful feeling
```

**中文参考**：
```
日系温馨客厅内部，下午柔和光线
日式公寓，木质家具
温暖的下午阳光透过窗帘
舒适的沙发，放着茶杯的小茶几
角落的绿植，装满书籍的书架
整洁干净，温馨的家庭氛围
令人心暖的家庭客厅，动漫背景
柔和散景效果，怀旧平和的感觉
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-12】住宅阳台（多肉植物）

**用途**：Day 12 在林晚棠家阳台照顾多肉植物

**英文正向提示词**：
```
anime style apartment balcony, bright sunlight
wooden plant shelf with colorful succulents and small potted plants
small green plants in various cute pots
sunny balcony atmosphere, Japanese apartment style
soft shadows, warm afternoon lighting
green plants and flowers on wooden shelf
peaceful and healing atmosphere, anime visual novel background
detailed succulent plants, cute potted flowers
```

**中文参考**：
```
日系公寓阳台，明亮阳光
木质花架上摆满颜色的多肉和小盆栽
小绿植装在各种可爱的花盆里
阳光明媚的阳台氛围，日式公寓风格
柔和阴影，温暖的下午光线
木质架子上绿植和花朵
平和治愈的氛围，动漫视觉小说背景
精细的多肉植物，可爱的盆栽
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-13】棋牌室内部

**用途**：Day 16 城南棋牌室，说服林父的关键场景

**英文正向提示词**：
```
anime style mahjong parlor interior, dim lighting
smoky atmosphere, cigarette smoke haze
mahjong tables with players, middle-aged men playing
old and worn interior, yellowish ceiling lights
warm but gloomy feeling, retro Chinese mahjong hall
dusty environment, cluttered space
dramatic shadows, melancholic atmosphere
anime visual novel background, serious emotional scene
```

**中文参考**：
```
日系风格麻将馆内部，昏暗灯光
烟雾缭绕的氛围，香烟烟雾弥漫
麻将桌旁有玩家，中年男子在打牌
老旧破败的内部，泛黄的顶灯
温暖但阴郁的感觉，复古中式麻将馆
灰尘环境，杂乱的空間
戏剧性的阴影，忧郁的氛围
动漫视觉小说背景，严肃情绪化的场景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 注意：此场景较为阴暗，与其他明亮场景形成对比

---

#### 【背景-14】咖啡馆吧台（偏内景）

**用途**：Day 15 在晚星咖啡馆与苏念卿对话，获取关键情报

**英文正向提示词**：
```
anime style cozy cafe interior, warm amber lighting
wooden counter with espresso machine, coffee cups on shelf
round mirrors on wall, vintage decorations
cafe interior with soft warm light, pendant lamps
barista area visible, steam rising from coffee
comfortable booth seats in background
cozy and relaxing atmosphere, anime visual novel
romantic evening ambiance, detailed cafe environment
```

**中文参考**：
```
日系温馨咖啡馆内部，暖琥珀色灯光
木质吧台配浓缩咖啡机，架子上咖啡杯
墙上圆形镜子，复古装饰
咖啡馆内部，柔和暖光，吊灯
可见咖啡师区域，咖啡升起蒸汽
背景有舒适卡座
温馨放松的氛围，动漫视觉小说
浪漫夜晚氛围，精细的咖啡馆环境
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-15】篮球场夜景（星空）

**用途**：Day 21 告白前夜，月下约定场景

**英文正向提示词**：
```
anime style basketball court at night, starry sky
wooden bench beside basketball court, night scene
countless stars in dark blue sky, full moon bright
empty basketball court, soft moonlight on court
peaceful and romantic night atmosphere, anime background
city skyline in far distance, warm window lights
quiet nighttime, emotional scene location
dreamy and nostalgic feeling, visual novel CG background
```

**中文参考**：
```
日系篮球场夜景，满天星空
篮球场旁的木质长椅，夜间场景
深蓝色天空中无数星星，皎洁明月
空无一人的篮球场，月光洒在球场
平和浪漫的夜晚氛围，动漫背景
远处城市天际线，温暖的窗户灯光
寂静的夜晚，情绪化场景地点
梦幻怀旧感，视觉小说CG背景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-16】天台夜景（星空）

**用途**：Day 23 告白大高潮场景，星空下的告白

**英文正向提示词**：
```
anime style school rooftop at night, starry night sky
countless bright stars, Milky Way visible
romantic stargazing atmosphere, vast open sky
school rooftop with chain-link fence, night scene
city lights glowing in the distance, warm atmosphere
magical starry night, emotional confession scene
peaceful and beautiful, anime visual novel background
cinematic composition, romantic and dreamy
```

**中文参考**：
```
日系学校天台夜景，满天星空
无数明亮的星星，可见银河
浪漫观星氛围，广阔开放的天空
学校天台有铁丝网围栏，夜间场景
远处城市灯光闪烁，温暖的氛围
神奇的星空夜晚，情绪化告白场景
平和美丽，动漫视觉小说背景
电影感构图，浪漫梦幻
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-17】城南街道夜景

**用途**：Day 16 傍晚去棋牌室的路上

**英文正向提示词**：
```
anime style urban street at dusk, evening atmosphere
Chinese neighborhood street, small shops closing
orange and purple gradient sunset in sky
street lamps starting to light up, warm glow
residential area with local shops, quiet evening
nostalgic Chinese urban scene, anime background
peaceful evening mood, soft shadows
cinematic composition, emotional transitional scene
```

**中文参考**：
```
日系城郊街道黄昏，傍晚氛围
中国住宅区街道，小店即将打烊
天空中橙紫色渐变夕阳
路灯开始亮起，温暖光芒
住宅区有小店，安静的傍晚
怀旧中式城市场景，动漫背景
平和傍晚情绪，柔和阴影
电影感构图，情绪化过渡场景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

#### 【背景-18】公园角落（日景）

**用途**：Day 18 命运改变后的公园，喜悦场景

**英文正向提示词**：
```
anime style small park corner, afternoon sunlight
peaceful park with wooden bench under tree
green grass and flowers, gentle breeze
soft warm lighting, cheerful and hopeful atmosphere
park in afternoon, nature surrounding
comfortable and healing environment, anime background
beautiful natural lighting, emotional positive scene
nostalgic and warm feeling, visual novel scene
```

**中文参考**：
```
日系小公园角落，下午阳光
树下有木质长椅的宁静公园
绿草和花朵，柔和微风
柔和温暖光线，欢快充满希望的氛围
下午的公园，自然环绕
舒适治愈的环境，动漫背景
美丽自然光，情绪化正面场景
怀旧温暖感，视觉小说场景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG

---

### 4.2 序章专用背景素材

> ⚠️ **特别说明**：序章"死亡与重生"的氛围营造至关重要，需要昏暗、情绪化的背景来替代纯黑屏，增强沉浸感。

---

#### 【背景-19】卧室·昏暗夜景（加班夜）

**用途**：序章开头，35岁主角加班到凌晨三点的场景

**英文正向提示词**：
```
anime style dimly lit bedroom at night, late night atmosphere
dark room, computer monitor glowing blue light
desk lamp with warm orange light, papers scattered on desk
window showing city lights at night, darkness outside
messy bedroom, exhausted atmosphere, melancholic mood
overturned chair, empty cup of coffee on desk
clock showing 3:00 AM, time passing feeling
lonely and suffocating atmosphere, adult working late
cinematic composition, emotional visual novel background
dark blue and purple tones, single light source from monitor
```

**中文参考**：
```
日系风格昏暗卧室，夜晚氛围
漆黑的房间，电脑显示器发出蓝色光芒
台灯发出暖橙色光线，桌上散落文件
窗户可见城市夜景，外面一片漆黑
凌乱的卧室，疲惫的氛围，忧郁的情绪
椅子翻倒，桌上空咖啡杯
时钟显示凌晨3点，时间流逝感
孤独压抑的氛围，成年人深夜加班
电影感构图，情绪化视觉小说背景
深蓝紫色调，唯一光源来自显示器
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：昏暗、压抑、孤独、深夜加班

---

#### 【背景-20】急救室/意识模糊底图

**用途**：序章主角倒下后、意识消散前的过渡场景

**英文正向提示词**：
```
anime style abstract consciousness fading scene, high quality
blurred vision effect, lights bleeding together
bright white overhead lights, hospital emergency room feel
swirling abstract pattern, consciousness dissolving
darkness creeping from edges, tunnel vision effect
heartbeat pulse visual effect, dramatic lighting
emotional and surreal atmosphere, visual novel transition
dreamlike quality, soul leaving body feeling
cinematic composition, emotional death scene
soft focus, ethereal white and blue tones
```

**中文参考**：
```
日系风格抽象意识消散场景，高质量
模糊视觉效果，灯光交融在一起
头顶明亮白色灯光，医院急救室感觉
漩涡般抽象图案，意识消融
黑暗从边缘蔓延，隧道视觉效应
心跳脉冲视觉效果，戏剧性光线
情绪化超现实氛围，视觉小说过渡
梦幻般的质感，灵魂离体感
电影感构图，情绪化死亡场景
柔焦效果， ethereal 白色蓝色调
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：意识模糊、消散、白光、深蓝渐变、梦幻

---

#### 【背景-21】住宅玄关/鞋柜

**用途**：序章重生后"妈，我去上学了"的场景，妈妈声音来源

**英文正向提示词**：
```
anime style home entrance genkan, morning light
Japanese style apartment entrance, wooden genkan floor
shoes on shoe rack, umbrellas by the door
warm morning sunlight streaming in from outside
cozy and familiar atmosphere, nostalgic feeling
family home warmth, mother's presence implied
shoe cabinet with mirror, jackets hanging
peaceful morning scene, anime background
soft warm lighting, heartwarming atmosphere
```

**中文参考**：
```
日系风格住宅玄关，清晨光线
日式公寓入口，木质玄关地板
鞋架上的鞋子，门边的雨伞
温暖的清晨阳光从外面洒入
温馨熟悉的氛围，怀旧感
家庭温暖，暗示妈妈的存在
带镜子的鞋柜，挂着的外套
宁静的清晨场景，动漫背景
柔和暖光，温馨的家庭氛围
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：清晨、温暖、家庭、怀旧

---

#### 【背景-22】校门·日景

**用途**：序章进入校园前的场景，"滨海市第一中学"校门

**英文正向提示词**：
```
anime style school gate entrance, morning sunlight
Chinese high school gate, "滨海市第一中学" sign
students walking through gate in uniforms
blue and white school uniforms, morning rush
cherry blossom trees along the path, petals falling
bright morning sky, warm sunshine
youthful and energetic atmosphere
school pillar with school emblem
clean campus entrance, nostalgic school feeling
cinematic composition, emotional scene transition
```

**中文参考**：
```
日系风格校门入口，清晨阳光
中式高中校门，"滨海市第一中学"校牌
穿校服的学生走过校门
蓝白色校服，清晨人潮
道路两旁的樱花树，花瓣飘落
明亮的早晨天空，温暖阳光
青春洋溢的氛围
校门柱子上的校徽
干净的校园入口，怀旧的校园感
电影感构图，情绪化场景过渡
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：清晨、青春、校园、蓝白色调

---

#### 【背景-23】记忆碎片特效背景

**用途**：序章"记忆碎片"解锁时的过渡背景

**英文正向提示词**：
```
anime style ethereal memory fragment transition, high quality
floating light particles, shimmering fragments
dark background with soft glowing orbs
abstract geometric shapes, memory visualization
dreamlike quality, time passing feeling
nostalgic warm tones mixed with cool blue
soft radial light from center, magical atmosphere
emotional and surreal, visual novel effect
cinematic composition, transition scene
beautiful particle effects, heart-touching moment
```

**中文参考**：
```
日系风格空灵记忆碎片过渡，高质量
漂浮光粒子，闪烁的碎片
深色背景配柔和发光球体
抽象几何形状，记忆可视化
梦幻般的质感，时间流逝感
怀旧暖色调与冷蓝色混合
中心柔和径向光，魔法般的氛围
情绪化超现实，视觉小说效果
电影感构图，过渡场景
美丽粒子效果，触动心弦的时刻
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG（透明背景效果更好）
- 氛围关键词：空灵、碎片、记忆、怀旧、魔法

---

---

### 4.2.2 林晚棠线补充背景素材

> ⚠️ **说明**：以下5张背景为林晚棠线（02_lindao_route.rpy）审查后确认缺失的场景背景，用于替换当前的黑屏段落，提升画面饱满度和沉浸感。

---

#### 【背景-24】医院走廊·白天

**用途**：Day 19，带妈妈去医院检查——"拯救妈妈"前世遗憾的关键场景

**出现位置**：行2217、2225、2247（3处连续使用）

**优先级**：🔴 P0（有对话+情绪+角色互动，黑屏体验极差）

**剧本上下文**：
```
lindao "妈，我们去医院看看吧。"
narrator "医院里人来人往。"
narrator "妈妈坐在长椅上，伸手摸了摸我的头。"
mother "没事的。妈妈身体好着呢。"
narrator "我看着她，心里默默发誓——这一次，绝不会再错过。"
```

**英文正向提示词**：
```
anime style hospital corridor, daytime, bright atmosphere
long white corridor with fluorescent ceiling lights
waiting benches along the wall, clean tiled floor
people walking in distance, blurred background figures
windows at far end letting in natural daylight
soft white and light blue tones, clinical but not cold
information desk visible in background, hospital signage
calm and peaceful atmosphere, emotional family scene
cinematic composition, visual novel background
warm natural lighting from windows, hopeful mood
clean modern Chinese hospital interior
```

**中文参考**：
```
日系风格医院走廊，白天，明亮氛围
长长的白色走廊，天花板的荧光灯
墙边等候长椅，干净瓷砖地面
远处走动的人影，模糊的背景人物
远端窗户透入自然日光
柔和白色和浅蓝色调，临床感但不冰冷
可见背景中的服务台和医院标识
平静安详的氛围，情绪化家庭场景
电影感构图，视觉小说背景
窗户透入温暖自然光线，充满希望的情绪
干净的现代中式医院内部
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：明亮、安静、希望、家庭温情、医院

---

#### 【背景-25】走廊窗边·夕阳

**用途**：Day 11傍晚，夕阳西斜，主角与林晚棠并肩站在窗边看晚霞——高浪漫感场景

**出现位置**：行718（1次）

**优先级**：🟡 P1（浪漫氛围场景，窗边空间与教室完全不同）

**剧本上下文**：
```
narrator "夕阳西斜。"
narrator "我们并肩站在窗边，看着外面的晚霞。"
lindao "你看，今天的晚霞好像特别好看。"
player "嗯……确实很好看。"
narrator "她的侧脸被夕阳染成了暖色。"
```

**英文正向提示词**：
```
anime style school hallway by window, sunset golden hour
large window frame on right side, showing beautiful evening sky
orange and pink gradient sunset sky, soft clouds
window sill with small potted plant, warm light streaming in
school corridor perspective, lockers faintly visible on left
dust particles dancing in golden sunlight beam
romantic and peaceful atmosphere, youth moment
warm orange and amber tones dominating the scene
empty quiet hallway, after school hours feeling
cinematic composition, emotional visual novel background
beautiful lighting, nostalgic school memory scene
```

**中文参考**：
```
日系风格学校走廊窗边，夕阳金色时刻
右侧大窗框，展示美丽的黄昏天空
橙粉渐变晚霞天空，柔和云朵
窗台有小盆栽，温暖阳光倾泻而入
学校走廊透视感，左侧隐约可见储物柜
金色阳光束中飞舞的尘埃粒子
浪漫宁静的氛围，青春时刻
温暖橙色琥珀色调主导画面
空旷安静的走廊，放学后的感觉
电影感构图，情绪化视觉小说背景
美丽的光线，怀旧校园记忆场景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：夕阳、浪漫、校园、青春、温馨

---

#### 【背景-26】校门外·黄昏街道

**用途**：Day 11傍晚，天色渐暗，一起走出校门告别的场景

**出现位置**：行782（1次）

**优先级**：🟡 P1（告别场景，校门外街道与住宅区街道语境完全不同）

**剧本上下文**：
```
narrator "天色渐渐暗了下来。"
narrator "我们一起走出校门。"
lindao "那我先回去了。"
player "路上小心。"
narrator "她点点头，转身离开。"
narrator "夕阳把她的影子拉得很长。"
```

**英文正向提示词**：
```
anime style street outside school gate, dusk twilight
school gate visible in background, slightly out of focus
urban street stretching into distance, evening atmosphere
street lamps just starting to glow warm orange
long shadows cast by setting sun, golden hour remaining
few students walking home in distance, silhouettes
trees lining the sidewalk, leaves rustling in evening breeze
peaceful end-of-day atmosphere, farewell moment
warm orange and purple dusk sky gradient
quiet city street, suburban school area feeling
cinematic composition, emotional visual novel background
nostalgic youth farewell scene, gentle mood
```

**中文参考**：
```
日系风格校门外街道，黄昏暮色
背景中可见校门，略微虚焦
城市街道向远方延伸，傍晚氛围
街灯刚开始发出温暖的橙色光芒
落日投下长长的影子，残留的金色时刻
远处几个回家的学生身影，剪影
人行道旁的树木，晚风中树叶摇曳
平静的一日终了氛围，告别时刻
温暖橙色紫色黄昏天空渐变
安静的城市街道，郊区学校区域感觉
电影感构图，情绪化视觉小说背景
怀旧青春告别场景，温柔的情绪
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：黄昏、告别、街道、温柔、青春

---

#### 【背景-27】住宅区街道·夜景（晴天）

**用途**：Day 14晚上，天台拥抱CG结束后送林晚棠回家的路途——晴夜无雨版

**出现位置**：行1546（1次）

**优先级**：🟡 P1（Day 14非雨天，不能用BG-09雨夜街道）

**剧本上下文**：
```
hide cg rooftop_embrace with dissolve
scene black
narrator "送她回家的路上，我们谁都没有说话。"
narrator "但手一直牵在一起。"
narrator "今晚的月亮很亮。"
```

**英文正向提示词**：
```
anime style residential street at night, clear weather no rain
quiet neighborhood street, apartment buildings on both sides
bright full moon in night sky, moonlight casting soft shadows
street lamps glowing warm orange, illuminating the path
no people around, intimate private atmosphere
clean dry pavement reflecting moonlight gently
balconies with faint indoor lights from apartments
peaceful late evening, romantic walking-home scene
deep blue night sky with stars visible
safe and quiet residential area, Chinese urban housing
cinematic composition, visual novel background
warm orange lamp light vs cool blue moonlight contrast
```

**中文参考**：
```
日系风格住宅区街道夜晚，晴天无雨
安静的社区街道，两侧公寓楼
明亮的满月在夜空中，月光洒下柔和阴影
街灯发出温暖橙色光芒，照亮道路
周围无人，私密亲密的氛围
干净干燥的地面，轻柔反射月光
阳台透出公寓内微弱的室内灯光
安宁的深夜，浪漫的回家路途
深蓝色夜空，星星清晰可见
安全安静的居民区，中式城市住宅
电影感构图，视觉小说背景
温暖橙色路灯光 vs 冷蓝色月光对比
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：晴夜、安静、浪漫、月光、温馨

---

#### 【背景-28】咖啡馆外街道·黄昏

**用途**：Day 15傍晚，从咖啡馆走出来，脑海中翻涌苏念卿话语的独白场景

**出现位置**：行1647（1次）

**优先级**：🟡 P1（咖啡馆外景视角，承接室内咖啡馆场景）

**剧本上下文**：
```
narrator "走出咖啡馆的时候，脑子里还在想着她说的话。"
player_thought ""如果真的喜欢她的话……""
player_thought ""现在就是最好的时机。""
narrator "苏念卿说得对。"
narrator "不能再等了。"
```

**英文正向提示词**：
```
anime style cafe exterior street view, evening sunset
cafe storefront visible on one side, warm interior lights through glass door
outdoor seating area with empty tables and chairs
evening street, pedestrian zone or quiet side street
sunset sky with warm orange and soft purple hues
street lamps beginning to glow, transitional day-to-night
cozy commercial district atmosphere, urban evening scene
glass windows reflecting sunset colors, inviting ambiance
a few pedestrians in distance, unhurried pace
introspective and thoughtful mood, decision-making moment
cinematic composition, visual novel background
warm color palette, emotionally charged transition scene
```

**中文参考**：
```
日系风格咖啡馆外景街道视角，傍晚夕阳
一侧可见咖啡馆店面，玻璃门透出温暖室内灯光
户外座区，空着的桌椅
傍晚的街道，步行区或安静的侧街
夕阳天空，温暖橙色和柔和紫色的色调
街灯开始亮起，昼夜交替的时刻
舒适的商业区氛围，城市傍晚场景
窗户玻璃反射出夕阳色彩，诱人的氛围
远处零星行人，不紧不慢的节奏
内省沉思的氛围，做决定的关键时刻
电影感构图，视觉小说背景
暖色调，充满情绪张力的过渡场景
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG/JPG
- 氛围关键词：傍晚、沉思、都市、温暖、过渡

---

### 4.4 CG场景素材

> ⚠️ **CG vs 背景的选择原则**：
> - **CG**：关键情绪点、需要角色参与的名场面、玩家第一眼的震撼点
> - **背景**：过渡场景、纯描述性场景、内心独白场景
>
> 📍 **序章CG优先级**：
> - 🔴 CG-P01（加班猝死）= 必须做，玩家第一眼震撼
> - 🟡 CG-P02（意识消散）= 建议做，死亡仪式感

---

#### 【CG-P01】加班夜·生命终结（序章）

**用途**：序章行28-40，主角倒下瞬间——游戏第一个情绪高潮点

**优先级**：🔴 最高（P0）

**情绪峰值**：★★★★★

**剧本位置**：
```
narrator "胃部传来一阵剧烈的绞痛。"
narrator "像是有什么东西在内部撕裂。"
player "……哈……"
narrator "手机从指间滑落。"
narrator "屏幕碎裂的声音，像是某种终结的号角。"
```

**画面描述**：
```
昏暗卧室，一个35岁男人的背影坐在电脑前
- 电脑屏幕发出惨淡蓝光，照亮他疲惫的脸
- 一只手捂住胸口，表情痛苦扭曲
- 手机从手中滑落，屏幕碎裂的瞬间
- 暖橙色台灯 vs 冷蓝色屏幕光的强烈对比
- 孤独、压抑、挣扎的氛围
```

**英文正向提示词**：
```
anime style dramatic scene, high quality, detailed
adult man sitting at desk, 35 years old, suffering expression, back view
computer monitor blue light illuminating face from below
one hand clutching chest in pain, other hand dropping phone
phone screen cracking mid-air, glass shards visible in flash
warm desk lamp orange glow vs cold monitor blue light contrast
dim dark bedroom, late night atmosphere, papers scattered on desk
empty coffee cup beside computer, overturned feeling
dramatic tension building, life ending moment
cinematic composition, emotional visual novel CG art
dark blue purple tones with orange accent, melancholic mood
```

**中文参考**：
```
日系戏剧性场景，高质量，精细
35岁成年男人坐在书桌前，痛苦的表情，背影
电脑显示器蓝光从下方照亮他的脸
一只手因疼痛捂住胸口，另一只手正在松开手机
手机在空中滑落，屏幕碎裂的瞬间，闪光中可见玻璃碎片
暖橙色台灯光芒 vs 冷蓝色显示器光的强烈对比
昏暗漆黑的卧室，深夜氛围，桌上散落文件
电脑旁有空咖啡杯，一种被压垮的感觉
戏剧性张力积聚，生命终结时刻
电影感构图，情绪化视觉小说CG艺术
深蓝紫色调配橙色点缀，忧郁情绪
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG透明背景
- 情绪关键词：痛苦、挣扎、孤独、终结
- Ren'Py使用：`show cg death_moment with fade`

---

#### 【CG-P02】意识消散·沉入深海（序章）

**用途**：序章行50-66，主角意识消散的过渡场景

**优先级**：🟡 建议（P1）

**情绪峰值**：★★★★☆

**剧本位置**：
```
narrator "视野越来越暗。"
narrator "就像……沉入深海。"
player_thought "就这样……结束了吗……"
player_thought "那些……没说出口的话……"
narrator "意识，在这一刻，彻底消散。"
scene black with fade
pause 3.0
```

**画面描述**：
```
抽象意识视角，从中心向外模糊消散
- 画面从中心向外模糊，白色光点逐渐消散
- 深蓝色"深海"感从边缘蔓延
- 隐约可见过去的画面碎片飘过（林晚棠的笑容、妈妈的身影）
- 空灵、告别、沉静的氛围
```

**英文正向提示词**：
```
anime style ethereal consciousness fading scene, high quality
white light particles dissolving into darkness from center
tunnel vision effect, edges darkening with deep blue
ghostly memory fragments floating in void, translucent silhouettes
past scenes fading: a girl's smile, a mother's figure
soul leaving body visualization, spirit rising upward
deep ocean blue darkness creeping in from edges
peaceful but melancholic atmosphere, accepting death
surreal dreamlike quality, transition between life and death
cinematic composition, emotional visual novel CG art
soft focus, ethereal white to deep blue radial gradient
```

**中文参考**：
```
日系空灵意识消散场景，高质量
白色光粒子从中心向黑暗中消融
隧道视觉效应，边缘渐暗呈深蓝色
幽灵般的记忆碎片在虚空中飘浮，半透明剪影
过去的画面渐渐消散：女孩的笑容、母亲的身影
灵魂离体可视化，精神向上飘升
深蓝色海洋般的黑暗从边缘蔓延
平和但忧郁的氛围，接受死亡
超现实梦幻般的质感，生命与死亡的过渡
电影感构图，情绪化视觉小说CG艺术
柔焦效果， ethereal 白色到深蓝色径向渐变
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG透明背景
- 氛围关键词：空灵、消散、深海、告别
- Ren'Py使用：`show cg consciousness_fade with dissolve`

---

#### 【CG-01】星空告白

**用途**：林晚棠线告白名场面

**英文正向提示词**：
```
anime style romantic scene illustration, high quality
two high school students on school rooftop at night
starry sky with countless stars, romantic atmosphere
boy confessing to girl, emotional moment
warm golden lighting from city below, moonlight on faces
tears of joy in girl's eyes, heartfelt confession
cinematic composition, emotional visual novel CG art
transparent background, PNG, alpha channel
```

**中文参考**：
```
日系浪漫场景插画，高质量
两个高中生夜晚在学校天台
满天星星的夜空，浪漫氛围
男孩向女孩告白，情绪化时刻
城市温暖的灯光从下方照射，月光洒在脸上
女孩眼中喜悦的泪水，真诚的告白
电影感构图，情绪化视觉小说CG艺术
透明背景，PNG格式，保留透明度通道
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG透明背景

---

#### 【CG-02】雨中撑伞

**用途**：林晚棠线Day 10雨夜场景

**英文正向提示词**：
```
anime style romantic rainy scene, high quality
couple sharing one umbrella on rainy night street
rain falling heavily around them, warm street lamp glow
girl slightly leaning toward boy, intimate atmosphere
wet pavement reflecting orange lights, romantic mood
cinematic composition, emotional visual novel CG art
transparent background, PNG, alpha channel
```

**中文参考**：
```
日系浪漫雨景，高质量
情侣雨夜共撑一把伞
周围大雨倾盆，温暖的街灯光芒
女孩微微靠近男孩，亲密氛围
湿润地面反射橙色灯光，浪漫情绪
电影感构图，情绪化视觉小说CG艺术
透明背景，PNG格式，保留透明度通道
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG透明背景

---

#### 【CG-03】天台拥抱

**用途**：告白成功后甜蜜场景

**英文正向提示词**：
```
anime style tender embrace scene, high quality
two high school students hugging on rooftop at sunset
warm golden hour lighting, romantic atmosphere
girl's head on boy's shoulder, peaceful happy expression
vast sky with orange and pink gradient
cinematic composition, visual novel CG art
transparent background, PNG, alpha channel
```

**中文参考**：
```
日系温馨拥抱场景，高质量
两个高中生夕阳时分在天台相拥
温暖的金色时刻光线，浪漫氛围
女孩的头靠在男孩肩上，平静幸福的表情
广阔天空，橙粉渐变
电影感构图，视觉小说CG艺术
透明背景，PNG格式，保留透明度通道
```

**规格要求**：
- 分辨率：1920×1080px
- 格式：PNG透明背景

---

### 4.3 UI素材（全套界面元素）

---

#### 【UI-01】对话框底栏（核心组件）

**用途**：对话显示，屏幕底部，承载角色名 + 对话文本

**英文正向提示词**：
```
visual novel dialogue box template, anime style
semi-transparent dark purple/blue background with blur/bokeh effect
elegant rounded corners (16px radius), thin warm-orange border line (2px)
bottom 300px of the screen, horizontal layout
clean minimalist design, modern visual novel UI
subtle gradient from dark purple to transparent blue
glassmorphism style with 70% opacity
left 280px reserved for character name area (rounded pill shape)
right area for dialogue text (multi-line capable)
speaker name tag: small rounded rectangle, warm orange background
thin white inner stroke on border, premium feel
game title accent: subtle warm glow on border
```

**中文参考**：
```
视觉小说对话框模板，日系动漫风格
半透明深紫/蓝色背景，带模糊/散景效果
优雅圆角（16px圆角），细暖橙色边框线（2px宽）
屏幕下方300px高度，横版布局
简洁极简设计，现代视觉小说UI
从深紫到透明蓝的微妙渐变
玻璃拟态风格，70%透明度
左侧280px预留角色名区域（圆角矩形）
右侧区域承载对话文本（多行）
角色名标签：小圆角矩形，暖橙色背景
白色内描边，白金质感
游戏标题强调：边框细微暖色光晕
```

**规格要求**：
- 尺寸：1920×350px（横版，底部对齐，宽度全屏）
- 格式：PNG透明背景
- 精度：72DPI（UI素材不需要打印精度）
- 风格色值：主色 #2d2d44（深紫蓝），强调色 #e8a87c（暖橙），边框 #ffffff（白）
- PNG图层要求：主体底栏、角色名标签分别独立导出，方便 Ren'Py 代码控制显隐

**Ren'Py 集成说明**：
- 对话框整体尺寸建议 1920×320，角色名区域左对齐
- 若使用代码绘制（gui.rpy），只需背景素材；若使用图片叠加，提供透明PNG

---

#### 【UI-02】选择菜单按钮

**用途**：选项分支（游戏中的 A/B/C 选项）

**英文正向提示词**：
```
visual novel choice button, anime UI style
rounded rectangle button (height 90px, variable width 600-900px)
semi-transparent dark purple background (#2d2d44, 75% opacity)
thin white border (2px), warm orange border on hover state
elegant minimalist design, text centered
soft glow effect on hover, subtle scale-up animation feel
clean flat design, no excessive shadow
transparent rounded corners matching dialogue box
```

**中文参考**：
```
视觉小说选择按钮，日系UI风格
圆角矩形按钮（高90px，宽600-900px可变）
半透明深紫色背景（#2d2d44，75%不透明度）
白色细边框（2px），悬停时边框变为暖橙色
优雅简洁设计，文字居中
悬停时有柔和光晕效果，微妙的放大动画感
简洁扁平设计，不过度阴影
透明圆角，与对话框风格统一
```

**规格要求**：
- 单个按钮尺寸：800×90px（宽度可裁剪）
- 格式：PNG透明背景
- 状态差分（需生成3种）：
  - UI_choice_normal.png（普通状态）
  - UI_choice_hover.png（悬停状态，橙色边框+光晕）
  - UI_choice_selected.png（选中状态，淡橙色填充）
- Ren'Py 建议：也可用代码绘制按钮（gui.choice_button 属性），减少素材依赖

---

#### 【UI-03】主菜单背景

**用途**：游戏启动后的标题界面背景

**英文正向提示词**：
```
visual novel main menu background, anime style illustration
beautiful romantic atmosphere, warm sunset lighting
school rooftop viewpoint, golden hour, vast sky
silhouette of cherry blossom tree in foreground, petals floating
warm orange to soft pink gradient sky, dramatic clouds
distant city skyline, nostalgic and emotional atmosphere
cinematic composition, wide aspect, emotional and dreamy
high quality background art, masterpiece
no text, no UI elements, purely scenic background
```

**中文参考**：
```
视觉小说主菜单背景，动漫风格插画
美丽浪漫氛围，暖夕阳光线
学校天台视角，金色时刻，广阔天空
前景樱花树剪影，花瓣飘落
暖橙色到柔粉色渐变天空，戏剧性云层
远景城市天际线，怀旧情绪化氛围
电影感构图，宽幅比例，情绪化梦幻
高质量背景艺术，杰作
无文字，无UI元素，纯风景背景
```

**规格要求**：
- 尺寸：1920×1080px（全屏）
- 格式：JPG（主背景）或 PNG（若要透明效果）
- 注意：预留顶部200px区域给游戏标题文字（避免文字与天空融为一体）
- 另一种做法：提供不带文字的纯风景底图，标题用 Ren'Py 代码叠加

---

#### 【UI-04】存档/读档槽位

**用途**：Save/Load 界面的每个存档格

**英文正向提示词**：
```
visual novel save slot frame, anime UI style
rounded rectangle frame (width 380px, height 260px)
semi-transparent dark purple background (#2d2d44, 80% opacity)
thin white border (1.5px)
left 38% area: screenshot preview (rounded, with placeholder gradient)
right 58% area: text info (save name, chapter, date/time stacked)
minimalist design, clean layout
warm accent elements matching dialogue box style
transparent background for overlay use
```

**中文参考**：
```
视觉小说存档槽位框架，动漫UI风格
圆角矩形框架（宽380px，高260px）
半透明深紫色背景（#2d2d44，80%不透明度）
白色细边框（1.5px）
左侧38%区域：截图预览区（圆角，带占位渐变）
右侧58%区域：文字信息（存档名、章节、日期时间纵向排列）
简洁设计，干净布局
与对话框风格统一的暖强调元素
透明背景用于叠加
```

**规格要求**：
- 单槽尺寸：380×260px
- 格式：PNG透明背景
- 提供两种状态：
  - UI_save_slot_empty.png（空槽，带虚线/渐变占位）
  - UI_save_slot_filled.png（已有存档，正常边框）
- Ren'Py 集成：截图区域由 Ren'Py 自动填充，只需框架底图

---

#### 【UI-05】设置面板

**用途**：Preferences 界面（音量、文字速度、跳过模式等）

**英文正向提示词**：
```
visual novel preferences panel, anime UI style
centered popup panel (width 1000px, height 700px)
semi-transparent dark purple background (#2d2d44, 90% opacity)
rounded corners (20px), thin white border (1.5px)
title bar at top with "设置" text area
slider bar elements: thin horizontal track, circular thumb
toggle switch elements: rounded pill shape, on/off state indicator
minimalist design, clean layout, vertical stacked sections
warm accent color for active/selected states
back button at bottom center
```

**中文参考**：
```
视觉小说设置面板，动漫UI风格
居中弹出面板（宽1000px，高700px）
半透明深紫色背景（#2d2d44，90%不透明度）
大圆角（20px），白色细边框（1.5px）
顶部标题栏带"设置"文字区域
滑块元素：细长横向轨道，圆形滑块
开关元素：圆角胶囊形状，开/关状态指示
简洁设计，干净布局，垂直排列各设置项
暖强调色用于激活/选中状态
底部居中有返回按钮
```

**规格要求**：
- 面板整体：1000×700px（居中于 1920×1080 屏幕）
- 格式：PNG透明背景
- 组件拆分（可选）：
  - UI_pref_panel.png（面板框架）
  - UI_pref_slider_track.png（滑轨背景）
  - UI_pref_slider_thumb.png（滑块圆点）
  - UI_pref_toggle_on.png / UI_pref_toggle_off.png（开关状态）
  - UI_pref_back_btn.png（返回按钮）
- Ren'Py 建议：大部分用代码绘制（gui.preference 样式），只提供面板背景图

---

#### 【UI-06】快捷菜单图标组

**用途**：对话框上方常驻快捷按钮（快进、自动、存档、读取、回滚）

**英文正向提示词**：
```
visual novel quick menu icon set, anime UI style
6 small rounded square icons (48×48px each)
semi-transparent dark background pill shape container
white monochrome icon symbols: skip (>>), auto (A), save (floppy), load (folder), rollback (left arrow), history (book)
hover state: warm orange tint on icon
minimalist flat design, no gradient, solid fills only
thin white border on container, transparent background
```

**中文参考**：
```
视觉小说快捷菜单图标组，动漫UI风格
6个小型圆角方形图标（每个48×48px）
半透明深色背景的胶囊形容器
白色单色图标符号：快进(>>)、自动(A)、存档(软盘)、读档(文件夹)、回滚(左箭头)、历史(书本)
悬停状态：图标有暖橙色色调
简洁扁平设计，无渐变，纯色填充
容器白色细边框，透明背景
```

**规格要求**：
- 单个图标：48×48px
- 格式：PNG透明背景，白色图标（悬停时橙色由 Ren'Py CSS 控制）
- 图标列表：快进(skip)、自动(auto)、存档(save)、读档(load)、回滚(rollback)、历史(history)
- Ren'Py 集成：提供单色图标 PNG，Ren'Py 通过 tint/hover 效果处理颜色变化

---

#### 【UI-07】好感度浮动提示（弹窗）

**用途**：好感度增减时屏幕中央弹出的浮动提示（如 "+10 好感度 ↑"）

**英文正向提示词**：
```
visual novel affection popup notification, anime UI style
small floating rounded bubble (width 300px, height 80px)
warm orange to pink gradient background
heart icon on left side, text in center
floating upward animation feel, soft glow effect
gentle fade-in and rise animation
minimalist cute design, semi-transparent
centered on screen, unobtrusive
```

**中文参考**：
```
视觉小说好感度弹窗提示，动漫UI风格
小型浮动圆角气泡（宽300px，高80px）
暖橙色到粉色渐变背景
左侧心形图标，中心文字
向上漂浮动画感，柔和光晕效果
温和的淡入上升动画
简洁可爱设计，半透明
屏幕居中，不遮挡主要视线
```

**规格要求**：
- 单个提示框：300×80px
- 格式：PNG透明背景（文字内容由代码绘制，好感度数值动态变化）
- 变化版本：
  - UI_affection_up.png（好感度上升，橙色渐变+上箭头）
  - UI_affection_down.png（好感度下降，蓝色渐变+下箭头）

---

#### 【UI-08】好感度进度条（侧边HUD）

**用途**：游戏过程中显示当前攻略角色的好感度等级

**英文正向提示词**：
```
visual novel affection meter bar, anime UI style
vertical or horizontal rounded progress bar
warm gradient fill (orange to pink), glowing effect on fill
heart icon at end or start of bar
clean minimalist frame, semi-transparent dark background
level indicator text area beside bar
soft elegant design, unobtrusive
```

**中文参考**：
```
视觉小说好感度条，动漫UI风格
垂直或水平圆角进度条
暖渐变填充（橙色到粉色），填充区域光晕效果
进度条末端或起始处有心形图标
简洁框架，半透明深色背景
进度条旁边有等级文字区域
柔和优雅设计，不遮挡视线
```

**规格要求**：
- 水平进度条：600×60px
- 垂直进度条：80×400px
- 格式：PNG透明背景
- Ren'Py 集成建议：用代码绘制进度条（fill 用动态图片或 tint 处理），只提供框架和心形图标素材

---

#### 【UI-09】章节标题卡片

**用途**：章节开始前的过渡标题（"序章"、"第一章"、"林晚棠线"等）

**英文正向提示词**：
```
visual novel chapter title card, anime UI style
centered elegant card (width 1000px, height 500px)
dark semi-transparent background with radial gradient
decorative thin frame, warm orange accent line
chapter number in large elegant font
chapter title in smaller font below
cherry blossom or star decorative elements at corners
dramatic cinematic feel, fade-in animation ready
romantic warm atmosphere, centered text composition
```

**中文参考**：
```
视觉小说章节标题卡，动漫UI风格
居中的优雅卡片（宽1000px，高500px）
深色半透明背景，径向渐变
装饰性细边框，暖橙色强调线
大号优雅字体章节编号
下方稍小字号的章节标题
四角樱花或星星装饰元素
戏剧性电影感，淡入动画准备
浪漫温暖氛围，居中文字构图
```

**规格要求**：
- 卡片尺寸：1000×500px（居中于全屏）
- 格式：PNG透明背景（章节文字由代码绘制）
- Ren'Py 集成：提供框架背景 PNG，"{b}第一章{/b}\n熟悉的陌生" 等文字由 Ren'Py text 显示

---

#### 【UI-10】确认对话框

**用途**：存档确认、退出确认、"是否保存"等二选一弹窗

**英文正向提示词**：
```
visual novel confirm dialog box, anime UI style
centered rounded rectangle (width 700px, height 400px)
semi-transparent dark purple background (#2d2d44, 90% opacity)
white border (2px), rounded corners (16px)
title text area at top center
message text area in middle
two buttons side by side at bottom: "是/Yes" and "否/No"
minimalist design, warm accent color on yes button
```

**中文参考**：
```
视觉小说确认对话框，动漫UI风格
居中圆角矩形（宽700px，高400px）
半透明深紫色背景（#2d2d44，90%不透明度）
白色边框（2px），圆角（16px）
顶部居中标题文字区域
中部提示文字区域
底部并排两个按钮："是/Yes" 和 "否/No"
简洁设计，"是"按钮用暖强调色
```

**规格要求**：
- 对话框整体：700×400px
- 格式：PNG透明背景
- 组件拆分：
  - UI_confirm_panel.png（面板框架）
  - UI_confirm_yes_btn.png / UI_confirm_no_btn.png（两个按钮，80×60px）
- Ren'Py 集成：框架背景 + 代码绘制按钮文字，Yes 按钮边框用暖橙色

---

#### 【UI-11】历史记录（回览）界面

**用途**：回看已读对话记录的文字回溯功能

**英文正向提示词**：
```
visual novel history log panel, anime UI style
full-height side panel (width 500px, height 1080px)
semi-transparent dark purple background (#2d2d44, 88% opacity)
white left border line (3px accent)
scrollable text area, character names in accent color
close button (X) at top right corner
minimalist clean layout, easy to read
```

**中文参考**：
```
视觉小说历史记录面板，动漫UI风格
全高度侧边面板（宽500px，高1080px）
半透明深紫色背景（#2d2d44，88%不透明度）
左侧白色强调边框线（3px）
可滚动文字区域，角色名用强调色
右上角关闭按钮(X)
简洁干净布局，易于阅读
```

**规格要求**：
- 面板整体：500×1080px（从屏幕右侧滑出）
- 格式：PNG透明背景
- Ren'Py 集成：提供侧边框架 PNG，文字由 Ren'Py history 屏幕自动填充

---

#### 【UI-12】游戏标题Logo

**用途**：主菜单屏幕的游戏标题文字

**英文正向提示词**：
```
visual novel game title logo text, anime style
stylized elegant typography for Chinese text "重生·轻逆袭"
subtitle "Re: Second Chance" in modern sans-serif font
warm golden-orange gradient text, slight glow effect
cherry blossom petals decorative elements around text
romantic and nostalgic feeling, cinematic title card style
transparent background, centered composition
```

**中文参考**：
```
视觉小说游戏标题Logo，动漫风格
优雅风格化字体呈现中文"重生·轻逆袭"
副标题"Re: Second Chance"用现代无衬线字体
暖金橙色渐变文字，微弱光晕效果
文字周围樱花花瓣装饰元素
浪漫怀旧感，电影感标题卡风格
透明背景，居中构图
```

**规格要求**：
- 整体尺寸：800×300px（根据字体大小调整）
- 格式：PNG透明背景（白色/金色文字）
- 也可提供 AI 生成的整张标题卡（含背景风景 + 叠加文字），省去字体依赖
- 推荐：提供纯文字透明背景 PNG，背景用单独的 UI-03 主菜单风景图

---

## 五、生成参数建议

### 5.1 Midjourney 参数

```
--ar 2:3 --niji 6 --style raw --q 2 --v 6.1
```

### 5.2 Stable Diffusion 参数

| 参数 | 推荐值 |
|------|--------|
| **采样器** | DPM++ 2M Karras |
| **步数** | 25-35 |
| **CFG Scale** | 7-9 |
| **分辨率** | 768×1152（立绘）/ 1920×1080（背景）/ 按UI组件实际尺寸 |
| **重绘幅度** | 0.3-0.5（保持风格一致性） |

### 5.3 批处理建议

```
1. 先用标准提示词生成1张，确认风格正确
2. 风格确认后，批量生成同类型素材
3. 每批生成5-8张，从中挑选最优
4. 需要人工精修的PNG素材，建议额外生成2-3个变体备选
```

---

## 六、素材文件命名规范

```
【立绘命名】
{角色缩写}_{表情编号}_{表情名称}.png
示例：LWT_01_normal.png (林晚棠_01_标准.png)
      LWT_03_shy.png   (林晚棠_03_害羞.png)

【背景命名】
BG_{场景编号}_{场景名称}_{光线}.png
示例：BG_01_classroom_day.png    (背景_01_教室_日景.png)
      BG_02_classroom_sunset.png (背景_02_教室_夕阳.png)
      BG_03_bedroom.png          (背景_03_卧室.png)

【UI命名】
UI_{组件类型}_{状态}.png
示例：UI_dialogue_base.png  (UI_对话框_底栏.png)
```

---

## 七、提示词更新规范

### 7.1 更新流程

```
1. 在对应素材类别下添加新的提示词
2. 同步更新"版本记录"表格
3. 版本号规则：
   - 小幅调整（关键词优化）：v1.x → v1.x+0.1
   - 中等更新（新增素材类型）：v2.0
   - 大幅更新（重构/重写）：v3.0
4. 提交时注明：feat: 更新AI提示词文档至vX.X
```

### 7.2 新增提示词模板

```markdown
---

#### 【类别-编号】素材名称

**用途**：描述使用场景

**英文正向提示词**：
```
在此处填写英文提示词
```

**中文参考**：
```
在此处填写中文参考
```

**规格要求**：
- 分辨率：XXXX×XXXXpx
- 格式：PNG透明背景 / JPG
- 精度：300DPI
```

---

## 八、素材生成记录

| 素材名称 | 提示词版本 | 生成日期 | 使用模型 | 状态 | 备注 |
|---------|-----------|----------|---------|------|------|
| 林晚棠立绘-01~06 | v1.4 | 2026-05-20 | — | ✅ 已完成 | 透明背景PNG |
| 背景-01 教室日景 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-02 教室夕阳 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-03 卧室 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-04 天台 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-05 图书馆 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-06 走廊 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-07 公园 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-08 咖啡馆 | v1.4 | 2026-05-18 | — | ✅ 已完成 | — |
| 背景-09 雨夜街道 | v1.4 | — | — | ✅ 已完成 | Day 9 雨中场景 |
| 背景-10 住宅区街道 | v1.5 | — | — | 🔲 待生成 | Day 8 上学同行 |
| 背景-11 住宅客厅 | v1.5 | — | — | 🔲 待生成 | Day 12 家访 |
| 背景-12 住宅阳台 | v1.5 | — | — | 🔲 待生成 | Day 12 多肉 |
| 背景-13 棋牌室 | v1.5 | — | — | 🔲 待生成 | Day 16 说服林父 |
| 背景-14 咖啡馆吧台 | v1.5 | — | — | 🔲 待生成 | Day 15 情报 |
| 背景-15 篮球场夜景 | v1.5 | — | — | 🔲 待生成 | Day 21 告白前夜 |
| 背景-16 天台星空夜景 | v1.5 | — | — | 🔲 待生成 | Day 23 告白 |
| 背景-17 城南街道夜景 | v1.5 | — | — | 🔲 待生成 | Day 16 过渡 |
| 背景-18 公园角落日景 | v1.5 | — | — | 🔲 待生成 | Day 18 喜悦场景 |
| 背景-19 卧室·昏暗夜景 | v1.6 | — | — | 🔲 待生成 | 序章"加班夜" |
| 背景-20 急救室/意识模糊 | v1.6 | — | — | 🔲 待生成 | 序章死亡过渡 |
| 背景-21 住宅玄关 | v1.6 | — | — | 🔲 待生成 | 序章"妈，我去上学了" |
| 背景-22 校门·日景 | v1.6 | — | — | 🔲 待生成 | 序章进入校园 |
| 背景-23 记忆碎片特效 | v1.6 | — | — | 🔲 待生成 | 序章记忆解锁 |
| CG-01 星空告白 | v1.4 | 2026-05-20 | — | ✅ 已完成 | — |
| CG-02 雨中撑伞 | v1.4 | — | — | 🔲 待生成 | 新增 |
| CG-03 天台拥抱 | v1.4 | — | — | 🔲 待生成 | 新增 |
| CG-P01 加班猝死 | v1.7 | — | — | 🔲 待生成 | 序章情绪高潮 |
| CG-P02 意识消散 | v1.7 | — | — | 🔲 待生成 | 序章死亡过渡 |
| UI-01 对话框 | v1.4 | 2026-05-19 | — | ✅ 已完成 | — |
| UI-02~12 | v1.1 | — | — | 🔲 待生成 | — |

---

## 九、林晚棠线完整素材清单

### 9.1 已完成素材 ✅

| 素材类型 | 文件名 | 用途 | 状态 |
|---------|--------|------|------|
| 林晚棠立绘×6 | LWT_01~06_*.png | 全部6种表情 | ✅ |
| 背景-01 | BG_01_classroom_day.png | 教室日景 | ✅ |
| 背景-02 | BG_02_classroom_sunset.png | 教室夕阳 | ✅ |
| 背景-03 | BG_03_bedroom.png | 卧室 | ✅ |
| 背景-04 | BG_04_rooftop_sunset_golden.png | 天台黄昏 | ✅ |
| 背景-05 | BG_05_library_day.png | 图书馆 | ✅ |
| 背景-06 | BG_06_corridor_afternoon.png | 走廊 | ✅ |
| 背景-07 | BG_07_park_bench_sunset.png | 公园长椅 | ✅ |
| 背景-08 | BG_08_cafe_sunset.png | 咖啡馆 | ✅ |
| 背景-09 | BG_09_rainy_street_night.png | 雨夜街道 | ✅ |
| 背景-10 | 待生成 | 住宅区街道 | 🔲 |
| 背景-11 | 待生成 | 住宅客厅 | 🔲 |
| 背景-12 | 待生成 | 住宅阳台 | 🔲 |
| 背景-13 | 待生成 | 棋牌室 | 🔲 |
| 背景-14 | 待生成 | 咖啡馆吧台 | 🔲 |
| 背景-15 | 待生成 | 篮球场夜景 | 🔲 |
| 背景-16 | 待生成 | 天台星空夜景 | 🔲 |
| 背景-17 | 待生成 | 城南街道夜景 | 🔲 |
| 背景-18 | 待生成 | 公园角落日景 | 🔲 |
| UI-01 | UI_01_dialogue_box.png | 对话框 | ✅ |

### 9.2 序章完整素材清单 🔲

#### 9.2.1 序章CG（关键情绪点）

| 素材类型 | 提示词状态 | 优先级 | 备注 |
|---------|-----------|--------|------|
| **CG-P01 加班猝死** | ✅ 文档中新增 | 🔴 P0 | 玩家第一眼震撼，情绪高潮 |
| **CG-P02 意识消散** | ✅ 文档中新增 | 🟡 P1 | 死亡仪式感，过渡场景 |

#### 9.2.2 序章背景图

| 素材类型 | 提示词状态 | 优先级 | 备注 |
|---------|-----------|--------|------|
| **背景-19 卧室·昏暗夜景** | ✅ 文档中已有 | 🔴 P0 | 序章"加班夜" |
| **背景-20 急救室/意识模糊** | ✅ 文档中已有 | 🔴 P0 | 序章死亡过渡 |
| **背景-21 住宅玄关** | ✅ 文档中已有 | 🟡 P1 | 序章"妈，我去上学了" |
| **背景-22 校门·日景** | ✅ 文档中已有 | 🟡 P1 | 序章进入校园 |
| **背景-23 记忆碎片特效** | ✅ 文档中已有 | 🟢 P2 | 序章记忆解锁 |

#### 9.2.3 序章黑屏→素材对照表

| 行号 | 原代码 | 建议类型 | 素材编号 | 说明 |
|------|--------|----------|----------|------|
| 7 | `scene black` | ✅ 保持黑屏 | - | 标题页用黑底白字更有仪式感 |
| 22 | 内心独白 | 🖼️ 背景 | BG-19 | 需要看到"手机屏幕光" |
| 28 | `vpunch`倒下 | 🎬 CG | CG-P01 | 倒下瞬间，关键情绪点 |
| 40 | 手机滑落后 | 🖼️ 背景 | BG-19 | 手机碎裂的视觉暗示 |
| 50 | 意识消散 | 🎬 CG | CG-P02 | "意识消散"是名场面 |
| 66 | 重生过渡 | 🖼️ 背景 | BG-19 | 渐变到清醒 |
| 113 | 重生醒来 | 🖼️ 背景 | BG-19 | 同一背景，淡入效果 |
| 131 | 震惊确认 | 🖼️ 背景 | BG-19 | 确认重生的震惊 |
| 179 | 坐床边发呆 | 🖼️ 背景 | BG-19 | 情绪过渡 |
| 319 | 上学出发 | 🖼️ 背景 | BG-21 | 玄关场景 |
| 335 | 章节标题 | ✅ 保持黑屏 | - | 章节过渡页 |
| 344 | 进入校门 | 🖼️ 背景 | BG-22 | 校门日景 |
| 375 | 章节标题 | ✅ 保持黑屏 | - | 正式章节标题 |

### 9.3 林晚棠线补充素材 🔲

| 素材类型 | 提示词状态 | 优先级 | 备注 |
|---------|-----------|--------|------|
| **背景-09 雨夜街道** | ✅ 文档中已有 | P0 | ~~林晚棠线Day 9~~ ✅ 已完成 |
| **背景-10 住宅区街道** | ✅ 文档中新增 | P0 | Day 8 上学同行 |
| **背景-11 住宅客厅** | ✅ 文档中新增 | P0 | Day 12 去林晚棠家 |
| **背景-12 住宅阳台** | ✅ 文档中新增 | P0 | Day 12 照顾多肉 |
| **背景-13 棋牌室** | ✅ 文档中新增 | P0 | Day 16 说服林父 |
| **背景-14 咖啡馆吧台** | ✅ 文档中新增 | P1 | Day 15 获取情报 |
| **背景-15 篮球场夜景** | ✅ 文档中新增 | P1 | Day 21 告白前夜 |
| **背景-16 天台星空夜景** | ✅ 文档中新增 | P1 | Day 23 告白场景 |
| **背景-17 城南街道夜景** | ✅ 文档中新增 | P2 | Day 16 过渡场景 |
| **背景-18 公园角落日景** | ✅ 文档中新增 | P2 | Day 18 喜悦场景 |
| CG-01 星空告白 | ✅ 已在文档中新增 | P1 | 告白名场面 |
| CG-02 雨中撑伞 | ✅ 已在文档中新增 | P1 | Day 10场景 |
| CG-03 天台拥抱 | ✅ 已在文档中新增 | P2 | 告白后甜蜜 |
| UI-02 选择菜单按钮 | ✅ 已有提示词 | P1 | 3种状态 |
| UI-03 主菜单背景 | ✅ 已有提示词 | P1 | - |
| UI-04 存档/读档槽位 | ✅ 已有提示词 | P1 | 2种状态 |
| UI-05 设置面板 | ✅ 已有提示词 | P2 | - |
| UI-06 快捷菜单图标组 | ✅ 已有提示词 | P1 | 6个图标 |
| UI-07 好感度浮动提示 | ✅ 已有提示词 | P1 | 2种状态 |
| UI-08 好感度进度条 | ✅ 已有提示词 | P2 | - |
| UI-09 章节标题卡片 | ✅ 已有提示词 | P2 | - |
| UI-10 确认对话框 | ✅ 已有提示词 | P2 | - |
| UI-11 历史记录面板 | ✅ 已有提示词 | P2 | - |
| UI-12 游戏标题Logo | ✅ 已有提示词 | P2 | - |

---

## 十、后续素材预告

### P1批次（第一批后）
- 其他四位女主立绘各6表情
- 更多背景图（咖啡馆、天台、医院、便利店等）

### P2批次（正式开发）
- CG场景图（20-30张）
- 全套UI素材
- 差分立绘（服装/头发变化）

---

## 十一、后续素材预告

### P1批次（第二批）
- 其他四位女主立绘各6表情
- 更多背景图（咖啡馆、天台、医院、便利店等）

### P2批次（正式开发）
- CG场景图（20-30张）
- 全套UI素材
- 差分立绘（服装/头发变化）

---

> **文档版本记录**：见上方"版本记录"表格
> **最后更新**：2026-05-20 v1.7 by AI辅助
