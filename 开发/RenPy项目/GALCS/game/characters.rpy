# =============================================================================
# characters.rpy - 角色定义
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

init python:
    # 导入角色模块（Character已内置，DynamicCharacter用于动态名字）
    from store import DynamicCharacter

# =============================================================================
# 主角
# =============================================================================

define narrator = Character(None, what_color="#f5f5f5")

define player = Character("[player_name]",
    color="#6c9bd1",
    what_color="#f5f5f5",
    who_bold=True
)

# 内心独白（玩家视角）
define player_thought = Character("[player_name]",
    color="#8ec8e8",
    what_color="#b8d4e8",
    what_italic=True
)

# =============================================================================
# 林晚棠（女一）
# =============================================================================

define lindao = Character("林晚棠",
    color="#e8a87c",           # 暖橙色
    what_color="#fff5ee",
    who_bold=False,
    who_italic=False
)

# 林晚棠的不同语气/状态
define lindao_shy = Character("林晚棠",
    color="#e8b88c",
    what_color="#fff0e8",
    who_italic=True
)

define lindao_happy = Character("林晚棠",
    color="#f0b87c",
    what_color="#fff8f0",
    who_bold=True
)

define lindao_sad = Character("林晚棠",
    color="#d89868",
    what_color="#fff0f0",
    who_italic=True
)

define lindao_angry = Character("林晚棠",
    color="#e87858",
    what_color="#ffe8e8",
    who_bold=True
)

# =============================================================================
# 苏念卿（女二）
# =============================================================================

define suni = Character("苏念卿",
    color="#c0859b",           # 优雅紫
    what_color="#faf0f5",
    who_bold=False,
    who_italic=False
)

define suni_gentle = Character("苏念卿",
    color="#c095ab",
    what_color="#fff5fa"
)

define suni_sad = Character("苏念卿",
    color="#a0657b",
    what_color="#fff0f5",
    who_italic=True
)

define suni_happy = Character("苏念卿",
    color="#d0a5bb",
    what_color="#fffaf8",
    who_bold=True
)

define suni_reminisce = Character("苏念卿",
    color="#b0758b",
    what_color="#fff0f8",
    who_italic=True,
    what_italic=True
)

# =============================================================================
# 周芷晴（女三）
# =============================================================================

define zhou = Character("周芷晴",
    color="#7dd87d",           # 元气绿
    what_color="#f0fff0",
    who_bold=False
)

define zhou_energetic = Character("周芷晴",
    color="#8de88d",
    what_color="#f8fff8",
    who_bold=True
)

define zhou_shy = Character("周芷晴",
    color="#6dc86d",
    what_color="#f0fff0",
    who_italic=True
)

define zhou_serious = Character("周芷晴",
    color="#5db85d",
    what_color="#f8fff8"
)

# =============================================================================
# 陈墨（女四）
# =============================================================================

define chen = Character("陈墨",
    color="#6b6bab",           # 冷傲紫蓝
    what_color="#f5f5fa",
    who_bold=False
)

define chen_cold = Character("陈墨",
    color="#5b5b9b",
    what_color="#f0f0fa"
)

define chen_vulnerable = Character("陈墨",
    color="#8b8bdb",
    what_color="#fafaff",
    who_italic=True
)

define chen_teasing = Character("陈墨",
    color="#7b7bcb",
    what_color="#f8f8ff",
    who_bold=True
)

# =============================================================================
# 沈听雨（女五/隐藏角色）
# =============================================================================

define shen = Character("沈听雨",
    color="#9b9bcb",           # 神秘灰紫
    what_color="#f8f8ff",
    who_bold=False
)

define shen_mysterious = Character("沈听雨",
    color="#8b8bbb",
    what_color="#f5f5fa",
    who_italic=True
)

define shen_smile = Character("沈听雨",
    color="#ababdb",
    what_color="#fafaff",
    who_bold=True
)

define shen_sad = Character("沈听雨",
    color="#7b7bab",
    what_color="#f0f0fa",
    who_italic=True
)

define shen_reveal = Character("沈听雨",
    color="#cbcbff",
    what_color="#ffffff",
    who_bold=True
)

# =============================================================================
# 男配角
# =============================================================================

# 好兄弟 - 林远
define lin = Character("林远",
    color="#5ba3d0",           # 兄弟蓝
    what_color="#f0f8ff"
)

define lin_happy = Character("林远",
    color="#6bb3e0",
    what_color="#f5faff",
    who_bold=True
)

define lin_sad = Character("林远",
    color="#4b93c0",
    what_color="#f0f8ff",
    who_italic=True
)

define lin_angry = Character("林远",
    color="#3b83b0",
    what_color="#ffe8e8",
    who_bold=True
)

# 情敌/竞争对手
define rival = Character("???",
    color="#808080",
    what_color="#f5f5f5"
)

# =============================================================================
# 家人
# =============================================================================

# 母亲
define mom = Character("妈妈",
    color="#e8a0a0",           # 温柔红
    what_color="#fff5f5"
)

define mom_worried = Character("妈妈",
    color="#d89090",
    what_color="#fff0f0",
    who_italic=True
)

define mom_happy = Character("妈妈",
    color="#f0b0b0",
    what_color="#fff8f8",
    who_bold=True
)

# 父亲
define dad = Character("爸爸",
    color="#a0a0a0",
    what_color="#f5f5f5"
)

define dad_worried = Character("爸爸",
    color="#909090",
    what_color="#f0f0f0"
)

define dad_happy = Character("爸爸",
    color="#b0b0b0",
    what_color="#f8f8f8"
)

# 林晚棠的父亲（出现在林晚棠线）
define lin_father = Character("林父",
    color="#708090",           # 石板灰（深沉/有故事感）
    what_color="#f0f0f0"
)

define lin_father_angry = Character("林父",
    color="#505050",
    what_color="#ffe0e0",
    who_bold=True
)

define lin_father_sad = Character("林父",
    color="#606060",
    what_color="#f0f0f0",
    who_italic=True
)

# 妹妹（提及）
define sister = Character("妹妹",
    color="#d8a0d8",
    what_color="#faf0fa"
)

# =============================================================================
# 老师/其他NPC
# =============================================================================

# 班主任
define teacher = Character("班主任",
    color="#808080",
    what_color="#f5f5f5"
)

# 路人/旁白风格
define npc_generic = Character("???",
    color="#909090",
    what_color="#f5f5f5"
)

# 医生（前世记忆）
define doctor = Character("医生",
    color="#ffffff",
    what_color="#f5f5f5"
)

# =============================================================================
# 旁白/系统
# =============================================================================

# 记忆闪回旁白
define memory_narration = Character(None,
    color="#a29bfe",
    what_color="#e8e0ff",
    what_italic=True
)

# 蝴蝶效应旁白
define butterfly_narration = Character(None,
    color="#ffeaa7",
    what_color="#fffef0",
    what_bold=True
)

# 记忆碎片收集提示
define fragment_prompt = Character(None,
    color="#a29bfe",
    what_color="#f0ebff",
    what_bold=True
)

# =============================================================================
# 角色立绘定义
# =============================================================================

# 林晚棠立绘（6表情）- zoom=0.65 适配1080p屏幕
image lindao normal = Transform("images/character/lindao/LWT_01_normal.png", zoom=0.65)
image lindao smile = Transform("images/character/lindao/LWT_02_smile.png", zoom=0.65)
image lindao shy = Transform("images/character/lindao/LWT_03_shy.png", zoom=0.65)
image lindao worried = Transform("images/character/lindao/LWT_04_worried.png", zoom=0.65)
image lindao crying = Transform("images/character/lindao/LWT_05_crying.png", zoom=0.65)
image lindao surprised = Transform("images/character/lindao/LWT_06_surprised.png", zoom=0.65)

# 角色位置定义（用于立绘显示）
# =============================================================================
# 屏幕位置常量
define LEFT = Position(xpos=0.15, xanchor=0.5)
define LEFT_CENTER = Position(xpos=0.3, xanchor=0.5)
define CENTER = Position(xpos=0.5, xanchor=0.5)
define RIGHT_CENTER = Position(xpos=0.7, xanchor=0.5)
define RIGHT = Position(xpos=0.85, xanchor=0.5)
define FAR_LEFT = Position(xpos=0.0, xanchor=0.5)
define FAR_RIGHT = Position(xpos=1.0, xanchor=0.5)

# 角色叠加顺序
define ADVANCE_SPRITE_ORDER = 0
define NORMAL_SPRITE_ORDER = 1
define BACKGROUND_SPRITE_ORDER = 2

# =============================================================================
# 好感度显示配置
# =============================================================================

init python:
    # 好感度阈值
    AFFECTION_TIER_LOW = 30
    AFFECTION_TIER_MED = 60
    AFFECTION_TIER_HIGH = 80

    # 好感度描述
    AFFECTION_TIER_NAMES = {
        0: "陌生",
        1: "初识",
        2: "好感",
        3: "心动",
        4: "喜欢",
        5: "深爱"
    }

    def get_affection_tier(affection):
        """根据好感度获取等级"""
        if affection < 15:
            return 0
        elif affection < 30:
            return 1
        elif affection < 50:
            return 2
        elif affection < 70:
            return 3
        elif affection < 90:
            return 4
        else:
            return 5

    def get_affection_color(affection):
        """根据好感度获取颜色"""
        if affection >= 70:
            return "#ff6b6b"  # 高好感 - 红色
        elif affection >= 40:
            return "#feca57"  # 中好感 - 黄色
        else:
            return "#54a0ff"  # 低好感 - 蓝色

# =============================================================================
# 背景图定义
# =============================================================================

# 教室 - 日景（序章、第一章常用）
image bg classroom_day = "images/backgrounds/BG_01_classroom_day.png"

# 教室 - 夕阳（林晚棠关键场景：告白前、放学后谈话）
image bg classroom_sunset = "images/backgrounds/BG_02_classroom_sunset.png"

# 主角卧室（日常独白、夜晚回忆场景）
image bg bedroom = "images/backgrounds/BG_03_bedroom.png"

# 学校天台 - 夕阳（林晚棠Day 10天台午餐、周芷晴线关键场景）
image bg rooftop_sunset = "images/backgrounds/BG_04_rooftop_sunset_golden.png"

# 学校图书馆 - 日景（林晚棠Day 13图书馆、苏念卿线）
image bg library = "images/backgrounds/BG_05_library_day.png"

# 学校走廊 - 下午（日常转场、课间场景）
image bg corridor = "images/backgrounds/BG_06_corridor_afternoon.png"
