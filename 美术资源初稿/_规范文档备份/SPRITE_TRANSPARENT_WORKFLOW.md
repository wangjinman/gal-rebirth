# 林晚棠 · 透明立绘制作流程（定稿）

> **确立日期**：2026-05-19  
> **适用范围**：角色立绘 / 表情差分（竖版 800×1200，RGBA 透明 PNG）  
> **不适用**：场景背景 BG（仍用 1920×1080，见 `ART_STYLE_GUIDE.md`）

---

## 一、结论（务必遵守）

| 做法 | 结论 |
|------|------|
| AI 直接生成「透明底 / 棋盘格」 | ❌ 无效：多为假透明或 RGB 白底/棋盘格画进像素 |
| 白底立绘 + 批量 floodfill 抠白 | ❌ 易误伤 **白衬衣、白袜**，发丝轮廓差 |
| **rembg / remove.bg 一键抠图** | ❌ 本项目实测不如色键；洋红底会溢色，白底会吃衣服 |
| **洋红幕生成 → 色键 → 边缘羽化** | ✅ **定稿流程**（2026-05-19 A 套 7 张） |

**游戏内展示（暂定定稿）**：`bust\*-bust-feather.png`（半身，由全身羽化版裁切）  
**母版 / 全身**：`*-transparent-v1-feather.png`（羽化全身；UI 底栏、重导半身、特殊全身镜头）  
**保留文件**：`*-transparent-v1.png`（色键未羽化，可对比）  
**源图备份**：`backup_gen\*_magenta-v1_rgb.png`（洋红幕 RGB，便于重导）

---

## 二、标准流程（一张一张做，不要批量脚本一口气跑完全部）

### 步骤 1 · AI 生成（洋红幕）

1. 阅读 `assets/ART_STYLE_GUIDE.md` 角色卡 + 对应表情表（动作/情绪要点）。
2. 用 **定稿白底图** 作 `reference_image_paths`（姿势、服装、表情）。
3. 提示词 **必须写**：
   - `solid flat chroma magenta #FF00FF background only`
   - `NO white background, NO checkerboard, NO shadow, NO scenery`
   - 校服 A 套细节、眼睛高光、负面词（无惊吓线等）。
4. 生成图先落在 Cursor 临时 `assets\`；文件名宜 **短**（如 `s1.png`），过长偶发保存失败。

**正向提示词骨架（立绘）**：

```
Japanese visual novel character sprite, vertical full-body,
Key / Summer Pockets galgame style, flat cel shading, soft sugar-light,
Lin Wantang, [表情与动作描述],
Uniform EXACT: white shirt navy collar/cuffs, blue-white bowtie,
blue chest badge, navy pleated skirt TWO white horizontal stripes,
white knee-high socks, black loafers,
solid flat magenta #FF00FF chroma background only,
NO white NO checkerboard NO action lines NOT 3D NOT nsfw
```

### 步骤 2 · 色键转透明（Python / Pillow）

1. 从洋红幕识别背景并写入 **真实 Alpha 通道**。
2. 按透明区域裁切 → 等比缩放到 **800×1200**。
3. **脚底对齐画布底边、水平居中**（所有表情统一，避免切换跳动）。

> 实现见：`立绘\scripts\sprite_chroma_feather.py`（仅色键加 `--no-feather`）

### 步骤 3 · 边缘羽化（仅 Alpha）

在色键结果上：

- `MaxFilter(3)` 略扩边 → `GaussianBlur(radius=1.2)` 柔化发丝外侧  
- 核心不透明区（`MinFilter(5)` 后 alpha > 0.92）**保持原 Alpha**，避免身体发虚  

参数为 2026-05-19 实机选定；勿随意加大 blur，否则整体糊。

### 步骤 4 · 交付到 J 盘

复制到：

```
J:\项目\GAL\美术资源初稿\立绘\
```

**命名约定**（以旧定稿文件名为基础）：

| 类型 | 命名示例 |
|------|----------|
| 色键透明 | `lin-wantang-expr-smile-v3-transparent-v1.png` |
| 羽化（进引擎） | `lin-wantang-expr-smile-v3-transparent-v1-feather.png` |
| 洋红源图备份 | `backup_gen\lin-wantang-expr-smile-magenta-v1_rgb.png` |

- **不要覆盖**旧白底定稿（如 `lin-wantang-expr-smile-v3.png`）。
- 回复协作者/用户时 **只写 J: 路径**。

### 步骤 5 · 目检（进引擎前）

叠在 **深色 + 复杂背景** 上看：

- [ ] 发丝、裙摆外缘无白边/紫边  
- [ ] 白衬衣、白袜无镂空  
- [ ] 校徽、蝴蝶结、裙摆双白条、黑乐福鞋  
- [ ] 与站立定稿 **肩宽/脚底** 大致一致（同画布 800×1200）

### 步骤 6 · 半身裁切（游戏内默认）

每完成一张全身 `*-feather.png` 后，运行 `sprite_crop_bust.py` 生成 `bust\` 下对应半身版（见第六节）。

---

## 三、林晚棠 A 套 · 已交付清单

| 表情 | 全身羽化（母版） | 半身（**游戏内推荐**） |
|------|------------------|------------------------|
| 站立 | `lin-wantang-standing-transparent-v1-feather.png` | `bust\lin-wantang-standing-transparent-v1-bust-feather.png` |
| 微笑 | `lin-wantang-expr-smile-v3-transparent-v1-feather.png` | `bust\lin-wantang-expr-smile-v3-transparent-v1-bust-feather.png` |
| 害羞 | `lin-wantang-expr-shy-v3-transparent-v1-feather.png` | `bust\lin-wantang-expr-shy-v3-transparent-v1-bust-feather.png` |
| 忧虑 | `lin-wantang-expr-worried-v2-transparent-v1-feather.png` | `bust\lin-wantang-expr-worried-v2-transparent-v1-bust-feather.png` |
| 哭泣 | `lin-wantang-expr-crying-v2-transparent-v1-feather.png` | `bust\lin-wantang-expr-crying-v2-transparent-v1-bust-feather.png` |
| 感动落泪 | `lin-wantang-expr-crying-moved-v3-transparent-v1-feather.png` | `bust\lin-wantang-expr-crying-moved-v3-transparent-v1-bust-feather.png` |
| 惊喜 | `lin-wantang-surprised-v4-transparent-v1-feather.png` | `bust\lin-wantang-surprised-v4-transparent-v1-bust-feather.png` |

---

## 四、表情生成要点（摘录）

| 表情 | 必守 |
|------|------|
| 害羞 | 红晕、食指相抵、腼腆笑，**≠ 伤心** |
| 忧虑 | 蹙眉、托下巴，**无眼泪** |
| 哭泣 | 伤心、泪多、拭泪 |
| 感动落泪 | 嘴角略扬、**泪少**，左眼几乎仅水光，**禁止流到脖子** |
| 惊喜 | **单手捂嘴**，无惊吓线/速度线 |

---

## 五、异常与备选

| 情况 | 处理 |
|------|------|
| `GenerateImage` 保存失败 | 缩短输出文件名重试（如 `m1.png`） |
| 无法生成洋红幕 | 临时：白底定稿四角 floodfill 改洋红再色键（质量略差，慎用） |
| 需下载 rembg 模型 | GitHub 超时时用镜像：`https://ghfast.top/https://github.com/.../u2net.onnx`；**本项目立绘仍不用 rembg 定稿** |
| 羽化过重/过轻 | 只改 `GaussianBlur radius`（建议 0.8–1.5），或出 `-feather-light` 副本对比 |

---

## 六、半身立绘 · 游戏内展示（暂定定稿）

> **确立**：2026-05-19 · 教室等透视背景实机对比，半身比全身更自然（避免脚线/比例违和）。

由全身羽化版 **程序化裁切**（非重画），画布仍为 **800×1200**，裁切下边对齐画布底，与全身版 **同一锚点**（`yalign 1.0` 可直接切换路径）。

| 项目 | 约定 |
|------|------|
| 源图 | `立绘\*-transparent-v1-feather.png` |
| 输出目录 | `立绘\bust\` |
| 命名 | `…-transparent-v1-bust-feather.png` |
| 裁切比例 | 透明 bbox 高度 × **`BUST_HEIGHT_RATIO = 0.62`**（约腰上～大腿中） |
| 脚本 | `立绘\scripts\sprite_crop_bust.py` |

```powershell
python 立绘\scripts\sprite_crop_bust.py
# PowerShell 中文路径失败时：python C:\Users\wangjinman\AppData\Local\Temp\sprite_crop_bust.py
```

**何时用哪套**

| 场景 | 文件 |
|------|------|
| **日常对话、教室/室内 BG** | `bust\*-bust-feather.png` |
| UI 底栏立绘、重导半身 | 全身 `*-feather.png`（脚本内裁切） |
| 走廊全身、刻意全身构图 | 全身 `*-feather.png` |

**Ren'Py**：`image` 指向 `立绘/bust/…-bust-feather.png`；可选 `zoom 0.85~0.92` 微调大小。

---

## 七、相关文件

| 文件 | 说明 |
|------|------|
| `assets/ART_STYLE_GUIDE.md` | 角色设定、表情表、提示词模板 |
| `.cursor/rules/galgame-art-style.mdc` | AI 作画自动规则 |
| `.cursor/rules/gal-asset-output-path.mdc` | J 盘输出目录 |
| `立绘\scripts\sprite_chroma_feather.py` | 色键 + 羽化脚本 |
| `立绘\scripts\sprite_crop_bust.py` | 半身裁切（见第六节） |

---

*维护：新增表情时：洋红幕 → 色键 → 羽化 → **裁半身** → 第三节表格补全身 + bust 两行。*

| 日期 | 修订 |
|------|------|
| 2026-05-19 | 透明色键流程、A 套 7 张全身 |
| 2026-05-19 | 半身 `bust\` 定为游戏内展示暂定标准 |
