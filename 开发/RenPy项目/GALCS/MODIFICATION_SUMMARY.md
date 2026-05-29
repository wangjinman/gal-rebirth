# 修改总结报告（汇总）

**项目**: 《重生·轻逆袭》(Re: Second Chance)
**引擎**: Ren'Py 8.5.2
**路径**: `J:\项目\GAL\开发\RenPy项目\GALCS\`

---

## 一、历次修改总览

| 日期 | 修改主题 | 关键结果 |
|------|---------|---------|
| 05-15 | 项目框架搭建 + 林晚棠立绘Day8-11 | 基础可运行 ✅ |
| 05-18 | 扩充背景图 BG-04~09 | 6张新增 |
| 05-21 | 林晚棠线Day12-15 + CG-01~02 | 剧情推进 ✅ |
| 05-22 | 林晚棠线Day16-18 + CG-03 | 情敌冲突 ✅ |
| 05-25 | 林晚棠线Day19-22 + 4新表情(angry/gentle/sad/thinking) | 10表情集齐 ✅ |
| 05-26 | 林晚棠线Day23-25 + BG-20~28 | 剧本完结 ✅ |
| 05-27 | 风格修复（括号205处+时代用语5处）+ 黑屏审计文档 | v1.9提示词完成 ✅ |
| 05-28 | 黑屏审计分类完成 + 待生成素材P0/P1确认 | 审计就绪 ✅ |
| **05-29** | **阶段二（10处复用背景）+ 阶段一（BG-29~34+CG-04~07集成）** | **21处黑屏消除 ✅** |

---

## 二、黑屏审计执行记录（05-29，最重要）

### 阶段二：10处复用已有背景

**01_chapter1.rpy（4处）**
| 行号 | 场景 | 替换背景 |
|------|------|---------|
| 138 | 走廊去办公室 | `bg corridor` (BG-06) |
| 190 | 走廊撞见苏念卿 | `bg corridor` (BG-06) |
| 329 | Day2卧室早晨 | `bg bedroom` (BG-03) |
| 509 | 操场午休 | `bg playground_bleachers` (BG-30) |

**02_lindao_route.rpy（6处）**
| 行号 | 场景 | 替换背景 |
|------|------|---------|
| 935 | 雨夜门口 | `bg apartment_entrance_rain` (BG-34，阶段一更新) |
| 1250 | 天台午休 | `bg rooftop_day` (BG-31，阶段一更新) |
| 1662 | 校门外送别 | `bg school_gate_dusk` (BG-26) |
| 1790 | 教室窗边晚霞 | `bg corridor_window_sunset` (BG-25) |
| 1978 | 卧室收消息 | `bg bedroom` (BG-03) |
| 2430 | 林晚棠家一下午 | `bg living_room` (BG-11) |

### 阶段一：BG-29~34 + CG-04~07 集成

**characters.rpy 新增10行定义**（BG-29~34 + CG-04~07）

**剧本代码改动（11处）**
| 文件 | 行号 | 改动 |
|------|------|------|
| 01_chapter1.rpy | 161 | `scene black` → `bg restroom_mirror` (BG-29) |
| 01_chapter1.rpy | 509 | `bg park_corner` → `bg playground_bleachers` (BG-30) |
| 02_lindao_route.rpy | 935 | `bg rainy_street` → `bg apartment_entrance_rain` (BG-34) |
| 02_lindao_route.rpy | 1250 | `bg rooftop_sunset` → `bg rooftop_day` (BG-31) |
| 02_lindao_route.rpy | Day16(4264) | `scene black` → `show cg day16_freezing with fade` + hide |
| 02_lindao_route.rpy | Day18(5069) | "谢谢你没有放弃"后插入 `show/hide cg day18_note` |
| 02_lindao_route.rpy | Day20(5590) | `scene black` → `bg rooftop_day` (BG-31) |
| 02_lindao_route.rpy | Day20(5606) | 去掉多余 `scene black` |
| 02_lindao_route.rpy | BE(7492) | `scene black` → `show cg be_empty_seat with fade` + pause 3.0 + hide |
| 02_lindao_route.rpy | TE(8376) | `scene black` → `bg living_room_warm` (BG-32) |
| 02_lindao_route.rpy | TE(8541) | `scene black` → `bg university_gate` (BG-33) |
| 02_lindao_route.rpy | TE(8612后) | 插入 `show cg te_reunion with fade` + pause 4.0 + hide |

**验证**: 16/16 全部 ✅

---

## 三、素材集成现状

| 类型 | 总数 | 详情 |
|------|------|------|
| 背景 BG | **34张** | BG-01~34（含阶段一新增BG-29~34） |
| CG | **7张** | CG-01~07（含阶段一新增CG-04~07） |
| 林晚棠立绘 | **10表情** | zoom=0.85，全部集成 ✅ |
| 其他女主立绘 | 0 | 待制作 |

---

## 四、待处理事项

### P1
- [ ] 时代错位用语剩余（~3处）
- [ ] 其他女主立绘+剧本

### P2
- [ ] Day16冰点特效屏/倒计时特效（代码实现 or 图片）
- [ ] UI素材（存档槽/设置面板）
- [ ] 行9254 另一路线TE是否同步改`university_gate`（待确认）
- [ ] Git提交（累积大量改动未提交）

---

## 五、Ren'Py 8.5 踩坑记录

| 问题 | 错误写法 | 正确写法 |
|------|---------|---------|
| 窗口隐藏 | `WindowHide()` | `_window_hide` |
| 屏幕变换 | `show screen X with transform` | `show screen X at transform_name` |
| 通知调用 | `$ show_notification(...)` | `call show_notification` |
| 特殊符号 | ✦ ✧ | 方框，需替换 |

---

*最后更新：2026-05-29*
