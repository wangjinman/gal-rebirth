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

define narrator = Character(None, what_color="#3a3a4e")

define player = Character("[player_name]",
    color="#6c9bd1",
    what_color="#b8c8e0",
    who_bold=True
)

# 内心独白（玩家视角）
define player_thought = Character("[player_name]",
    color="#8ec8e8",
    what_color="#6a9ac4",
    what_italic=True
)

# =============================================================================
# 林晚棠（女一）
# =============================================================================

define lindao = Character("林晚棠",
    color="#e8a87c",           # 暖橙色
    what_color="#b08860",      # 深暖棕（亮背景可读）
    who_bold=False,
    who_italic=False
)

# 林晚棠的不同语气/状态
define lindao_shy = Character("林晚棠",
    color="#e8b88c",
    what_color="#a07850",
    who_italic=True
)

define lindao_happy = Character("林晚棠",
    color="#f0b87c",
    what_color="#c09050",
    who_bold=True
)

define lindao_sad = Character("林晚棠",
    color="#d89868",
    what_color="#a06848",
    who_italic=True
)

define lindao_angry = Character("林晚棠",
    color="#e87858",
    what_color="#a04830",
    who_bold=True
)

# =============================================================================
# 苏念卿（女二）
# =============================================================================

define suni = Character("苏念卿",
    color="#c0859b",           # 优雅紫
    what_color="#8a5a6a",      # 深玫粉棕
    who_bold=False,
    who_italic=False
)

define suni_gentle = Character("苏念卿",
    color="#c095ab",
    what_color="#9a6a7a"
)

define suni_sad = Character("苏念卿",
    color="#a0657b",
    what_color="#7a4055",
    who_italic=True
)

define suni_happy = Character("苏念卿",
    color="#d0a5bb",
    what_color="#a07090",
    who_bold=True
)

define suni_reminisce = Character("苏念卿",
    color="#b0758b",
    what_color="#804a62",
    who_italic=True,
    what_italic=True
)

# =============================================================================
# 周芷晴（女三）
# =============================================================================

define zhou = Character("周芷晴",
    color="#7dd87d",           # 元气绿
    what_color="#3a8040",      # 深森林绿（亮背景可读）
    who_bold=False
)

define zhou_energetic = Character("周芷晴",
    color="#8de88d",
    what_color="#4a9050",
    who_bold=True
)

define zhou_shy = Character("周芷晴",
    color="#6dc86d",
    what_color="#387838",
    who_italic=True
)

define zhou_serious = Character("周芷晴",
    color="#5db85d",
    what_color="#408040"
)

# =============================================================================
# 陈墨（女四）
# =============================================================================

define chen = Character("陈墨",
    color="#6b6bab",           # 冷傲紫蓝
    what_color="#4a4a78",      # 深靛蓝灰
    who_bold=False
)

define chen_cold = Character("陈墨",
    color="#5b5b9b",
    what_color="#3a3a6a"
)

define chen_vulnerable = Character("陈墨",
    color="#8b8bdb",
    what_color="#6a6a98",
    who_italic=True
)

define chen_teasing = Character("陈墨",
    color="#7b7bcb",
    what_color="#5a5a88",
    who_bold=True
)

# =============================================================================
# 沈听雨（女五/隐藏角色）
# =============================================================================

define shen = Character("沈听雨",
    color="#9b9bcb",           # 神秘灰紫
    what_color="#5a5a82",      # 深岩灰紫
    who_bold=False
)

define shen_mysterious = Character("沈听雨",
    color="#8b8bbb",
    what_color="#4a4a72",
    who_italic=True
)

define shen_smile = Character("沈听雨",
    color="#ababdb",
    what_color="#6a6a92",
    who_bold=True
)

define shen_sad = Character("沈听雨",
    color="#7b7bab",
    what_color="#3a3a62",
    who_italic=True
)

define shen_reveal = Character("沈听雨",
    color="#cbcbff",
    what_color="#7a7ab2",
    who_bold=True
)

# =============================================================================
# 男配角
# =============================================================================

# 好兄弟 - 林远
define lin = Character("林远",
    color="#5ba3d0",           # 兄弟蓝
    what_color="#3a7098"       # 深钢蓝
)

define lin_happy = Character("林远",
    color="#6bb3e0",
    what_color="#4a80a8",
    who_bold=True
)

define lin_sad = Character("林远",
    color="#4b93c0",
    what_color="#3a6088",
    who_italic=True
)

define lin_angry = Character("林远",
    color="#3b83b0",
    what_color="#8a3030",
    who_bold=True
)

# 情敌/竞争对手
define rival = Character("???",
    color="#808080",
    what_color="#6a6a72"
)

# =============================================================================
# 家人
# =============================================================================

# 母亲
define mom = Character("妈妈",
    color="#e8a0a0",           # 温柔红
    what_color="#a05858"       # 暗砖红
)

define mom_worried = Character("妈妈",
    color="#d89090",
    what_color="#904848",
    who_italic=True
)

define mom_happy = Character("妈妈",
    color="#f0b0b0",
    what_color="#b06868",
    who_bold=True
)

# 父亲
define dad = Character("爸爸",
    color="#a0a0a0",
    what_color="#5a5a5e"
)

define dad_worried = Character("爸爸",
    color="#909090",
    what_color="#4a4a4e"
)

define dad_happy = Character("爸爸",
    color="#b0b0b0",
    what_color="#6a6a6e"
)

# 林晚棠的父亲（出现在林晚棠线）
define lin_father = Character("林父",
    color="#708090",           # 石板灰（深沉/有故事感）
    what_color="#4a5a68"       # 深石板色
)

define lin_father_angry = Character("林父",
    color="#505050",
    what_color="#8a2828",
    who_bold=True
)

define lin_father_sad = Character("林父",
    color="#606060",
    what_color="#3a3a42",
    who_italic=True
)

# 林晚棠的母亲（出现在林晚棠线 Day 18）
define lin_mom = Character("林母",
    color="#A08070",           # 温暖棕色
    what_color="#6a5040"       # 深咖啡色
)

# 妹妹（提及）
define sister = Character("妹妹",
    color="#d8a0d8",
    what_color="#8a5a8a"
)

# =============================================================================
# 老师/其他NPC
# =============================================================================

# 班主任
define teacher = Character("班主任",
    color="#808080",
    what_color="#5a5a5e"
)

# 路人/旁白风格
define npc_generic = Character("???",
    color="#909090",
    what_color="#6a6a6e"
)

# 医生（前世记忆）
define doctor = Character("医生",
    color="#ffffff",
    what_color="#888890"
)

# 赵轩然 — 情敌/竞争者（林晚棠线 Day 7-11 出现）
define zhao_xuran = Character("赵轩然",
    color="#5B8C8C",           # 青灰色（斯文败类感）
    what_color="#3a6068"       # 深青灰色
)

# 通用学生NPC
define male_student_1 = Character("男生",
    color="#888888",
    what_color="#5a5a5e"
)
define female_student_1 = Character("女生A",
    color="#CC88AA",
    what_color="#8a5570"
)
define female_student_2 = Character("女生B",
    color="#BB99BB",
    what_color="#7a5580"
)

# =============================================================================
# 旁白/系统
# =============================================================================

# 记忆闪回旁白
define memory_narration = Character(None,
    color="#a29bfe",
    what_color="#6858a8",      # 深紫靛（亮背景可读）
    what_italic=True
)

# 蝴蝶效应旁白
define butterfly_narration = Character(None,
    color="#ffeaa7",
    what_color="#a08830",      # 暗金色
    what_bold=True
)

# 记忆碎片收集提示
define fragment_prompt = Character(None,
    color="#a29bfe",
    what_color="#5848a0",      # 深紫色
    what_bold=True
)

# =============================================================================
# 角色立绘定义
# =============================================================================

# 林晚棠立绘（10表情）- zoom=0.85 适配1080p屏幕
image lindao normal = Transform("images/character/lindao/LWT_01_normal.png", zoom=0.85)
image lindao smile = Transform("images/character/lindao/LWT_02_smile.png", zoom=0.85)
image lindao shy = Transform("images/character/lindao/LWT_03_shy.png", zoom=0.85)
image lindao worried = Transform("images/character/lindao/LWT_04_worried.png", zoom=0.85)
image lindao crying = Transform("images/character/lindao/LWT_05_crying.png", zoom=0.85)
image lindao surprised = Transform("images/character/lindao/LWT_06_surprised.png", zoom=0.85)

# 新增4表情（括号表情清理后补充）
image lindao angry = Transform("images/character/lindao/LWT_07_angry.png", zoom=0.85)
image lindao gentle = Transform("images/character/lindao/LWT_08_gentle.png", zoom=0.85)
image lindao sad = Transform("images/character/lindao/LWT_09_sad.png", zoom=0.85)
image lindao thinking = Transform("images/character/lindao/LWT_10_thinking.png", zoom=0.85)

# 角色位置定义（用于立绘显示）
# =============================================================================
# 屏幕位置常量 - 调整后更居中（再往右移动0.2）
define LEFT = Position(xpos=0.48, xanchor=0.5)
define LEFT_CENTER = Position(xpos=0.58, xanchor=0.5)
define CENTER = Position(xpos=0.5, xanchor=0.5)
define RIGHT_CENTER = Position(xpos=0.82, xanchor=0.5)
define RIGHT = Position(xpos=0.92, xanchor=0.5)
define FAR_LEFT = Position(xpos=0.35, xanchor=0.5)
define FAR_RIGHT = Position(xpos=0.95, xanchor=0.5)

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

# 公园长椅 - 夕阳（日常/约会场景）
image bg park_sunset = "images/backgrounds/BG_07_park_bench_sunset.png"

# 咖啡馆 - 夕阳（苏念卿线/约会场景）
image bg cafe_sunset = "images/backgrounds/BG_08_cafe_sunset.png"

# 雨夜街道（林晚棠Day 9雨中场景）
image bg rainy_street = "images/backgrounds/BG_09_rainy_street_night.png"

# =============================================================================
# 林晚棠线背景图（BG-10 ~ BG-18）
# =============================================================================

# 住宅区街道 - 清晨（Day 8 上学同行/等她下楼）
image bg residential_street = "images/backgrounds/BG_10_residential_street_morning.png"

# 住宅客厅 - 下午（Day 12 家访/参观房间）
image bg living_room = "images/backgrounds/BG_11_living_room_afternoon.png"

# 住宅阳台 - 下午（Day 12 多肉植物场景）
image bg balcony = "images/backgrounds/BG_12_balcony_succulents_afternoon.png"

# 棋牌室 - 内景（Day 16 说服林父场景）
image bg mahjong_parlor = "images/backgrounds/BG_13_mahjong_parlor_interior.png"

# 咖啡馆吧台 - 傍晚（Day 15 苏念卿咖啡馆获取情报）
image bg cafe_bar = "images/backgrounds/BG_14_cafe_bar_evening.png"

# 篮球场 - 夜景（Day 21 告白前夜月下约定）
image bg basketball_court = "images/backgrounds/BG_15_basketball_court_night.png"

# 天台 - 星空夜景（Day 23 夜晚告白/告白后）
image bg rooftop_stars = "images/backgrounds/BG_16_rooftop_night_stars.png"

# 城南街道 - 黄昏（Day 16 过渡/寻找林父途中）
image bg urban_street_dusk = "images/backgrounds/BG_17_urban_street_dusk.png"

# 公园角落 - 下午（Day 18 喜悦/放松场景）
image bg park_corner = "images/backgrounds/BG_18_park_corner_afternoon.png"

# =============================================================================
# 序章专用背景图
# =============================================================================

# 卧室·昏暗夜景 - 加班夜（序章·第一幕：死亡场景）
image bg bedroom_late_night = "images/backgrounds/BG_19_bedroom_night_overtime.png"

# 意识消散过渡（序章·第二幕：意识流过渡场景）
image bg consciousness_fading = "images/backgrounds/BG_20_consciousness_fading.png"

# 家中玄关 - 清晨（序章·第三幕：出门上学场景）
image bg home_entrance = "images/backgrounds/BG_21_home_entrance_morning.png"

# 清晨高中校门（序章·第四幕：重生后第一天到校）
image bg school_gate_morning = "images/backgrounds/BG_22_school_gate_morning.png"

# 记忆碎片过渡特效（序章·第三幕/各章节转场用）
image bg memory_fragment = "images/backgrounds/BG_23_memory_fragment_transition.png"

# =============================================================================
# 序章CG图
# =============================================================================

# CG-P01 - 【加班夜·生命终结】35岁男人深夜加班倒下瞬间（序章情绪高潮★5）
image cg death_overtime = "images/cg/CG_P01_overtime_life_end.png"

# CG-P02 - 【意识消散·沉入深海】抽象意识消散过渡（意识流场景）
image cg consciousness_fade = "images/cg/CG_P02_consciousness_deep_sea_opaque.png"

# =============================================================================
# 林晚棠线补充背景（BG-24~28）
# =============================================================================

# 医院走廊·白天 - Day19 带妈妈检查
image bg hospital_corridor = "images/backgrounds/BG_24_corridor_hospital_day.png"

# 走廊窗边·夕阳 - Day11 并肩看晚霞
image bg corridor_window_sunset = "images/backgrounds/BG_25_corridor_window_sunset.png"

# 校门外·黄昏街道 - Day11 走出校门告别
image bg school_gate_dusk = "images/backgrounds/BG_26_school_gate_street_dusk.png"

# 住宅区街道·夜景(晴) - Day14 天台CG后送回家
image bg residential_night_clear = "images/backgrounds/BG_27_residential_street_night.png"

# 咖啡馆外街道·黄昏 - Day15 走出咖啡馆
image bg cafe_street_evening = "images/backgrounds/BG_28_cafe_exterior_street_evening.png"

# =============================================================================
# UI素材 - 选择菜单按钮（3态差分）
# =============================================================================

# 普通状态 - 深蓝紫底 + 白色边框
image ui_choice_normal = "images/UI/UI_choice_normal.png"

# 悬停状态 - 橙色边框 + 光晕
image ui_choice_hover = "images/UI/UI_choice_hover.png"

# 选中状态 - 淡橙色填充
image ui_choice_selected = "images/UI/UI_choice_selected.png"
