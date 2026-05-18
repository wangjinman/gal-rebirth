# =============================================================================
# definitions.rpy - 全局变量与Flag定义
# 《重生·轻逆袭》(Re: Second Chance)
#
# 所有游戏状态变量、好感Flag、剧情Flag都在此定义
# =============================================================================

# =============================================================================
# 游戏基础状态
# =============================================================================

# 当前日期（游戏内天数，Day 1-30）
default persistent.current_day = 1

# 当前章节标识
default persistent.current_chapter = "prologue"

# 游戏完成标志
default persistent.game_completed = False

# =============================================================================
# 系统Flag（记录游戏进度）
# =============================================================================

# 记忆碎片系统
default persistent.fragment_count = 0          # 已收集记忆碎片数量
default persistent.fragments_collected = []    # 已收集的碎片ID列表

# 遗憾值系统
default persistent.regret_value = 0            # 当前遗憾弥补值
default persistent.max_regret_value = 300     # 最大遗憾值

# 蝴蝶效应计数
default persistent.butterfly_count = 0        # 蝴蝶效应触发次数

# =============================================================================
# 各女主好感度
# =============================================================================

# 林晚棠 - 好感度 (0-100)
default persistent.lindao_affection = 0
default persistent.lindao_heart_events = 0    # 心仪事件触发数
default persistent.lindao_confession = False  # 是否已告白

# 苏念卿 - 好感度 (0-100)
default persistent.suni_affection = 0
default persistent.suni_heart_events = 0
default persistent.suni_confession = False

# 周芷晴 - 好感度 (0-100)
default persistent.zhou_affection = 0
default persistent.zhou_heart_events = 0
default persistent.zhou_confession = False

# 陈墨 - 好感度 (0-100)
default persistent.chen_affection = 0
default persistent.chen_heart_events = 0
default persistent.chen_confession = False

# 沈听雨 - 好感度 (0-100)
default persistent.shen_affection = 0
default persistent.shen_heart_events = 0
default persistent.shen_revelation = False     # 是否发现其身份

# =============================================================================
# 各女主线Flag（标记已完成的线）
# =============================================================================

default persistent.lindao_route_completed = False
default persistent.suni_route_completed = False
default persistent.zhou_route_completed = False
default persistent.chen_route_completed = False
default persistent.shen_route_completed = False

# True Ending解锁条件
default persistent.true_ending_unlocked = False

# =============================================================================
# 序章Flag
# =============================================================================

default prologue_woke_up = False               # 是否已醒来
default prologue_memory_fragment_1 = False      # 记忆碎片1 - 死亡
default prologue_memory_fragment_2 = False      # 记忆碎片2 - 遗憾
default prologue_butterfly_1 = False           # 蝴蝶效应1

# =============================================================================
# 第一章Flag
# =============================================================================

default chapter1_day1_school = False           # Day 1 到校
default chapter1_met_lindao = False             # 遇见林晚棠
default chapter1_met_chen = False              # 遇见陈墨
default chapter1_met_zhou = False              # 遇见周芷晴
default chapter1_met_suni = False              # 遇见苏念卿
default chapter1_butterfly_lindao = False      # 林晚棠蝴蝶效应
default chapter1_butterfly_family = False      # 家庭蝴蝶效应

# =============================================================================
# 林晚棠线Flag（按场景编号）
# =============================================================================

# Day 8-10 初期接触
default lindao_day8_first_talk = False
default lindao_day9_lunch = False
default lindao_day10_homework = False

# Day 11-13 感情升温
default lindao_day11_library = False
default lindao_day12_rain = False
default lindao_day13_immigration = False       # 移民话题关键Flag

# Day 14-16 深入了解
default lindao_day14_secret = False
default lindao_day14_fragment_unlocked = False    # 记忆碎片4解锁
default lindao_day15_family_visit = False
default lindao_day16_cherry_blossom = False

# Day 16-17 说服林父QTE
default lindao_day16_persuasion_result = None    # "rational" / "emotional" / "ultimatum"
default lindao_day16_father_impressed = False    # 是否打动林父
default lindao_day16_persuasion_failed = False   # 说服是否失败

# Day 17-18 最终抉择
default lindao_day17_confession_prep = False
default lindao_day17_father_conflict = False   # 父亲冲突Flag
default lindao_day18_confession = False        # 告白Flag
default lindao_day18_result = False            # 告白结果

# Day 20 告白准备QTE
default lindao_day20_prepared = None          # "letter" / "gift" / "sincere"
default lindao_day20_letter_written = False   # 是否写了情书
default lindao_day20_sincere_mode = False      # 是否选择真诚模式
default lindao_day20_gift = None               # "succulent" / "book" / "bracelet"

# Day 23 告白分支
default lindao_day23_confession_style = None   # "direct" / "romantic" / "letter" / "gift" / "sincere"
default lindao_confession_success = False       # 告白是否成功

# 林晚棠结局Flag
default lindao_ending_type = None              # "HE" / "Normal" / "BE"

# =============================================================================
# 苏念卿线Flag
# =============================================================================

default suni_day8_first_meet = False
default suni_day10_cafe = False
default suni_day11_scar = False                # 疤痕话题Flag
default suni_day12_ex_boyfriend = False       # 前男友Flag
default suni_day14_truth = False
default suni_day15_healing = False
default suni_day18_confession = False
default suni_ending_type = None

# =============================================================================
# 周芷晴线Flag
# =============================================================================

default zhou_day4_first_meet = False           # Day 4初遇
default zhou_day8_basketball = False
default zhou_day12_game_center = False
default zhou_day15_secret = False
default zhou_day18_rain_night = False          # 雨夜关键Flag
default zhou_day19_confession = False
default zhou_ending_type = None

# =============================================================================
# 陈墨线Flag
# =============================================================================

default chen_day3_first_notice = False
default chen_day7_study = False
default chen_day9_exam = False                 # 考试Flag
default chen_day11_cry = False                # 哭泣Flag
default chen_day15_pressure = False
default chen_day18_confession = False
default chen_day20_final = False
default chen_ending_type = None

# =============================================================================
# 沈听雨线Flag（隐藏线）
# =============================================================================

default shen_day5_first_see = False
default shen_day10_mysterious = False
default shen_day12_hint = False
default shen_day15_truth = False               # 真相Flag
default shen_day20_choice = False
default shen_day24_final = False
default shen_ending_type = None                # "HE" / "BE" / "True"
default shen_identity_revealed = False

# =============================================================================
# True EndingFlag
# =============================================================================

default te_routes_completed = 0                # 已完成女主线数量
default te_fragment_bonus = False              # 记忆碎片额外加成
default te_choice_made = None                  # 最终选择: "A" / "B" / "C"

# =============================================================================
# 男配Flag（兄弟/情敌）
# =============================================================================

default bro_friendship = 50                    # 兄弟情谊值 (0-100)
default bro_conflict_triggered = False         # 是否触发冲突
default bro_reconciliation = False             # 是否和解

default rival_chen_detected = False            # 是否察觉陈墨的感情
default rival_zhou_detected = False           # 是否察觉周芷晴的感情

# =============================================================================
# 家庭关系Flag
# =============================================================================

default family_dad_gambling = False            # 父亲赌博问题
default family_dad_improved = False           # 父亲改善
default family_mom_health = True              # 母亲健康
default family_mom_care = False               # 是否开始关心母亲

# =============================================================================
# 学业Flag
# =============================================================================

default academic_exam_score = 0               # 模拟考成绩
default academic_studied = False               # 是否努力学习
default academic_improved = False              # 是否有进步

# =============================================================================
# 记忆碎片定义
# =============================================================================

# 碎片ID列表（用于追踪收集）
default ALL_FRAGMENTS = [
    # 序章碎片
    ("frag_001", "死亡的记忆"),
    ("frag_002", "遗憾清单"),
    ("frag_003", "她的笑容"),
    # 第一章碎片
    ("frag_004", "高考成绩"),
    ("frag_005", "母亲的病"),
    # 林晚棠线碎片
    ("frag_006", "错过的告白"),
    ("frag_007", "日本的方向"),
    ("frag_008", "她的眼泪"),          # Day 14解锁
    ("frag_009", "父亲的背影"),        # Day 16解锁
    ("frag_010", "星空下的约定"),      # Day 23解锁
    # ... 其他碎片
]

# =============================================================================
# 临时变量（每次游戏重置）
# =============================================================================

# 非持久化的临时状态
default temp_choice_made = None
default temp_scene_count = 0
