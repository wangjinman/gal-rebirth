# 2026-05-15 工作日志

## GAL项目进度归档

### 项目路径
`J:\项目\GAL\开发\RenPy项目\GALCS\`

### 当前版本状态

#### ✅ 已完成
- **游戏框架搭建** - Ren'Py 8.5.2 项目结构完成
- **核心脚本** - script.rpy, characters.rpy, definitions.rpy, screens.rpy
- **字体配置** - 使用 simhei.ttf 解决中文显示问题
- **序章剧本** - 00_prologue.rpy 完整（死亡与重生场景）
- **第一章剧本** - 01_chapter1.rpy 框架完成

#### ⚠️ 缺少资源
- **图片素材** - 无背景图、无角色立绘、无CG图
- **音效/音乐** - 无BGM、无SE

### 修复的问题列表

| 日期 | 问题 | 修复方案 |
|------|------|---------|
| 05-15 | current_background未定义 | 改为 scene black |
| 05-15 | yesno_prompt缺失 | 添加确认对话框屏幕 |
| 05-15 | 字体方框 | 改用simhei.ttf |
| 05-15 | config.font无效(Ren'Py8) | 改用gui.font |
| 05-15 | 未知style名称 | 删除无效样式 |

### 项目文件结构

```
GALCS/
├── game/
│   ├── characters.rpy      # 角色定义（5女主+配角）
│   ├── definitions.rpy     # 变量/Flag定义
│   ├── gui.rpy            # GUI配置+字体
│   ├── options.rpy        # 游戏配置
│   ├── screens.rpy        # 界面屏幕
│   ├── script.rpy         # 主脚本+通用label
│   ├── script/
│   │   ├── 00_prologue.rpy   # 序章
│   │   └── 01_chapter1.rpy  # 第一章
│   ├── fonts/
│   │   ├── simhei.ttf        # 黑体（已验证支持中文）
│   │   └── SourceHanSansLite.ttf
│   ├── gui/               # GUI图片资源
│   ├── images/            # 背景/立绘/CG
│   ├── audio/             # 音乐/音效
│   └── cache/             # 编译缓存
├── README.md
├── TODO.md
└── errors.txt
```

### 剧情进度

- **序章** ✅ 完成 - 死亡场景、重生觉醒、记忆碎片
- **第一章** 🔄 进行中 - 回到学校第一天
- **林晚棠线** ⬜ 未开始
- **苏念卿线** ⬜ 未开始
- **周芷晴线** ⬜ 未开始
- **陈墨线** ⬜ 未开始
- **沈听雨线** ⬜ 未开始
- **True Ending** ⬜ 未开始

### Git提交记录

| 提交 | 内容 |
|------|------|
| 初始化 | 项目框架、基础脚本 |
| 修复1 | current_background、yesno_prompt |
| 修复2 | 字体配置、中文显示 |
| 归档1 | 进度记录、美术需求清单 |

---

*最后更新：2026-05-15*
