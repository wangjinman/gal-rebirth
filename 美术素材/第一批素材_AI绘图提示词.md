# 《重生·轻逆袭》美术素材AI提示词 - 专用文档

> **文档编号**：GAL-PROMPT-001
> **版本**：v1.3
> **日期**：2026-05-18
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
| **P0** | 最高 | 林晚棠立绘（6表情） | 6张 | Demo核心展示 | ⚠️ 已生成（需替换透明版） |
| **P0** | 最高 | 教室背景（日景） | 1张 | 序章+第一章 | ✅ 已完成 |
| **P0** | 最高 | 教室背景（窗外夕阳） | 1张 | 林晚棠关键场景 | ✅ 已完成 |
| **P0** | 最高 | 主角卧室背景 | 1张 | 日常场景 | ✅ 已完成 |
| **P0** | 高 | 学校天台（黄昏） | 1张 | 关键浪漫场景 | 🔲 待生成 |
| **P0** | 高 | 学校图书馆 | 1张 | 学习/安静对话 | 🔲 待生成 |
| **P0** | 高 | 学校走廊 | 1张 | 课间/转场 | 🔲 待生成 |
| **P0** | 高 | 公园长椅（黄昏） | 1张 | 约会场景 | 🔲 待生成 |
| **P0** | 高 | 咖啡馆内景 | 1张 | 苏念卿线/约会 | 🔲 待生成 |
| **P1** | 高 | 对话框底栏 | 1个 | 核心UI | 🔲 待生成 |
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
| 林晚棠立绘-01 | v1.2 | 2026-05-15 | — | ⚠️ 已生成 | 需替换透明背景版本 |
| 林晚棠立绘-02~06 | v1.2 | — | — | ⏳ 待生成 | 透明背景 |
| 背景-01 教室日景 | v1.0 | — | — | ✅ 已完成 | — |
| 背景-02 教室夕阳 | v1.0 | — | — | ✅ 已完成 | — |
| 背景-03 卧室 | v1.0 | — | — | ✅ 已完成 | — |
| 背景-04 天台 | v1.1 | — | — | 🔲 待生成 | — |
| 背景-05 图书馆 | v1.1 | — | — | 🔲 待生成 | — |
| 背景-06 走廊 | v1.1 | — | — | 🔲 待生成 | — |
| 背景-07 公园 | v1.1 | — | — | 🔲 待生成 | — |
| 背景-08 咖啡馆 | v1.1 | — | — | 🔲 待生成 | — |
| UI-01~12 | v1.1 | — | — | 🔲 待生成 | — |

---

## 九、后续素材预告

### P1批次（第一批后）
- 其他四位女主立绘各6表情
- 更多背景图（咖啡馆、天台、医院、便利店等）

### P2批次（正式开发）
- CG场景图（20-30张）
- 全套UI素材
- 差分立绘（服装/头发变化）

---

> **文档版本记录**：见上方"版本记录"表格
> **最后更新**：2026-05-18 by AI辅助
