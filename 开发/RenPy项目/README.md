# 《重生·轻逆袭》(Re: Second Chance)

> 一款基于 Ren'Py 引擎开发的视觉小说 / 恋爱模拟游戏

## 游戏简介

**《重生·轻逆袭》** 是一款重生穿越题材的GAL游戏。玩家将扮演35岁的社畜陆鸣，在一次意外中重生回到高考前一个月，带着前世35年的记忆碎片，重新面对人生中的遗憾与抉择。

- **游戏时长**：约10小时（单周目4-5小时，全女主+TE约10小时）
- **定价**：¥28（早鸟¥18）
- **目标平台**：Steam
- **目标上线**：2026-11-14

## 项目结构

```
RenPy项目/
├── game/                          # Ren'Py 游戏主目录
│   ├── script/                    # 剧本脚本
│   │   ├── 00_prologue.rpy       # 序章：死亡与重生
│   │   ├── 01_chapter1.rpy       # 第一章：熟悉的陌生
│   │   ├── 02_lindao.rpy         # 林晚棠线（待创作）
│   │   ├── 03_suni.rpy           # 苏念卿线（待创作）
│   │   ├── 04_zhou.rpy           # 周芷晴线（待创作）
│   │   ├── 05_chen.rpy            # 陈墨线（待创作）
│   │   ├── 06_shen.rpy            # 沈听雨线（待创作）
│   │   └── 07_true_ending.rpy     # True Ending（待创作）
│   │
│   ├── images/                    # 图片资源
│   │   ├── backgrounds/           # 背景图
│   │   ├── characters/            # 角色立绘
│   │   └── cg/                    # CG图
│   │
│   ├── audio/                     # 音频资源
│   │   ├── bgm/                   # 背景音乐
│   │   └── se/                    # 音效
│   │
│   ├── saves/                     # 存档目录
│   │
│   ├── script.rpy                 # 主脚本入口
│   ├── definitions.rpy            # 全局变量与Flag定义
│   ├── characters.rpy             # 角色定义
│   ├── options.rpy                # 游戏配置
│   ├── gui.rpy                    # GUI界面配置
│   └── screens.rpy                # 界面屏幕
│
├── README.md                       # 项目说明
└── TODO.md                         # 开发待办事项
```

## 已完成内容

### ✅ 基础框架
- [x] 项目目录结构创建
- [x] `options.rpy` - 游戏配置
- [x] `gui.rpy` - GUI界面配置
- [x] `definitions.rpy` - 全局Flag定义
- [x] `characters.rpy` - 角色定义
- [x] `screens.rpy` - 界面屏幕
- [x] `script.rpy` - 主脚本入口

### ✅ 剧本
- [x] `00_prologue.rpy` - 序章（完整，4+1场景，约30分钟）
- [x] `01_chapter1.rpy` - 第一章（基础版本，7天时间线，约60分钟）

### ⬜ 待创作剧本
- [ ] 林晚棠线（18场景，约90分钟）
- [ ] 苏念卿线（12场景，约120分钟）
- [ ] 周芷晴线（10场景，约90分钟）
- [ ] 陈墨线（14场景，约150分钟）
- [ ] 沈听雨线（8场景，约60分钟）
- [ ] True Ending（6场景，约60分钟）

### ⬜ 待制作资源
- [ ] 背景图片（学校、街道、家等）
- [ ] 角色立绘（5位女主 × 6表情）
- [ ] CG图（关键场景）
- [ ] BGM音乐
- [ ] 音效

## 运行游戏

### 方法1：使用 Ren'Py Launcher
1. 安装 [Ren'Py](https://www.renpy.org/latest.html) 8.0+
2. 打开 Ren'Py Launcher
3. 点击 "Open Directory" 选择 `J:\项目\GAL\开发\RenPy项目`
4. 点击 "Launch Project"

### 方法2：命令行运行
```bash
# 安装 Ren'Py SDK 后
renpy.exe "J:\项目\GAL\开发\RenPy项目"
```

## 开发规范

### 角色命名
- 主角：`player` / `player_name`
- 林晚棠：`lindao` / `lindao_shy` / `lindao_happy` 等（按情绪）
- 苏念卿：`suni` / `suni_gentle` / `suni_sad` 等
- 周芷晴：`zhou` / `zhou_energetic` / `zhou_shy` 等
- 陈墨：`chen` / `chen_cold` / `chen_vulnerable` 等
- 沈听雨：`shen` / `shen_mysterious` / `shen_reveal` 等

### Flag命名规范
```
章节_flag名 = True/False
示例：
- prologue_woke_up = False
- chapter1_day1_school = True
- lindao_confession = False
```

### 好感度命名
```
persistent.xxx_affection = 0-100
示例：
- persistent.lindao_affection = 50
- persistent.suni_affection = 30
```

### 剧本注释规范
```
# 【剧情意义】
# ☑ 好感绑定：xxx好感+N
# ☑ Flag绑定：xxx = True
# ☑ 伏笔绑定：xxx（伏笔编号）
# ☑ 蝴蝶效应植入：xxx描述
# ☑ 凡人感植入：xxx描述
```

## 技术栈

- **游戏引擎**：Ren'Py 8.0+
- **开发语言**：Ren'Py Script + Python
- **版本控制**：Git
- **美术工具**：AI生成（待定）

## 剧本大纲

详见：`J:\项目\GAL\剧本\00_剧本大纲.md`（v1.2）

## 联系方式

- **制作人**：wangjinman
- **邮箱**：wangjinman_2008@126.com
- **GitHub**：https://github.com/wangjinman/gal-rebirth

---

*「这一次，我要让人生重来。」*
