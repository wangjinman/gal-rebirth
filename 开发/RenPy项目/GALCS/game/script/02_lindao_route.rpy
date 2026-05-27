# =============================================================================
# 02_lindao_route.rpy - 林晚棠线：这次，我不想再错过她
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

# =============================================================================
# 角色定义
# =============================================================================

define lindao = Character('林晚棠', color="#D4A574", what_color="#b08860")
define lindao_thought = Character('陆鸣（内心）', color="#8ECAE6", what_color="#6a9ac4")

# =============================================================================
# CG图片定义
# =============================================================================

# CG-01: 星空告白 (Day 23)
image cg_01_starry_sky_confession = "cg/CG_01_lwt_starry_sky_confession.png"

# CG-02: 雨中撑伞 (Day 9)
image cg_02_rainy_umbrella = "cg/CG_02_lwt_rainy_umbrella_school_uniform.png"

# CG-03: 天台拥抱 (Day 14)
image cg_03_rooftop_embrace = "cg/CG_03_lwt_rooftop_embrace.png"

# =============================================================================
# 背景图片定义
# =============================================================================

# BG-09: 雨夜街道 (Day 9 雨中场景)
image bg rainy_street_night = "backgrounds/BG_09_rainy_street_night.png"

# =============================================================================
# Day 8：靠近期的开始
# =============================================================================

label lindao_day8:
    scene black

    call chapter_title("林晚棠线", "", 1.5)

    narrator "第一章结束后的第二天清晨。"

    narrator "我站在镜子前，看着十八岁的自己。"

    narrator "窗外的阳光很刺眼，和记忆中一模一样。"

    player_thought "这次，我不会犹豫了。"

    scene black

    call chapter_title("靠近", "Day 8", 1.5)

label lindao_day8_morning:
    scene bg bedroom with dissolve

    narrator "从今天开始，我决定每天早起。"

    narrator "不是去晨读，而是——"

    player_thought "绕一点路，和她一起上学。"

    scene bg bedroom with dissolve

    narrator "林晚棠家和我家其实顺路。"

    narrator "前世我每天都是一个人走，从没想过要等她。"

    narrator "等我终于鼓起勇气的时候——"

    narrator "她已经去了日本。"

    # 站在她家楼下等她
    scene bg residential_street with dissolve

    narrator "今天，我站在她家楼下。"

    narrator "七点十五分，她准时从单元门走出来。"

    narrator "看到我，她明显愣了一下。"

    # 显示林晚棠立绘 - 惊讶表情
    show lindao surprised at LEFT with dissolve

    lindao "陆鸣？你怎么在这里？"

    player "早啊，刚好路过。"

    narrator "她的表情从惊讶变成了疑惑，然后是……一丝笑意。"

    # 切换到默认表情
    show lindao normal at LEFT with dissolve

    lindao "刚好路过？你家不是反方向吗？"

    player_thought "……"

    player_thought "被发现了。"

    player "呃……其实是特意等你的。"

    narrator "她的脸微微红了。"

    # 切换到害羞表情
    show lindao shy at LEFT with dissolve

    lindao "……你今天吃错药了？"

    player "怎么，不行吗？"

    lindao "（低下头）……走吧，别迟到了。"

    narrator "她加快脚步往前走。"

    narrator "但我注意到——"

    narrator "她的耳根，红红的。"

    # 隐藏立绘
    hide lindao with dissolve

    $ persistent.lindao_affection += 5
    $ persistent.lindao_day8_walked_together = True

    jump lindao_day8_classroom

label lindao_day8_classroom:
    scene bg classroom_day with dissolve

    narrator "早自习。"

    narrator "我坐在她旁边，假装看书。"

    narrator "其实余光一直在看她。"

    player_thought "她今天穿的是白色衬衫……很好看。"

    narrator "她似乎感受到了我的目光。"

    # 显示林晚棠立绘
    show lindao shy at LEFT with dissolve

    lindao "（小声）你今天怎么一直看我……"

    player "没什么，就是觉得你今天气色挺好的。"

    narrator "这句话，和第一章那天一模一样。"

    narrator "但这次——"

    show lindao normal at LEFT with dissolve

    lindao "（脸更红了）……你上次也这么说。"

    player "因为是真的啊。"

    narrator "她低下头，不再说话。"

    narrator "但嘴角，悄悄弯了起来。"

    $ persistent.lindao_affection += 3

    scene bg classroom_day with dissolve

    narrator "午休时间。"

    narrator "我去小卖部买了两盒牛奶。"

    narrator "然后……"

    player "林晚棠，给你。"

    narrator "我把一盒牛奶放在她桌上。"

    show lindao surprised at LEFT with dissolve

    lindao "（惊讶）给我的？"

    player "嗯，早餐奶。对身体好。"

    show lindao smile at LEFT with dissolve

    lindao "（接过，小声）……谢谢。"

    narrator "她低头喝牛奶的样子，很安静。"

    player_thought "突然觉得有点可爱。"

    $ persistent.lindao_affection += 5

    narrator "这一幕被林远看到了。"

    narrator "「我靠，陆鸣你小子开窍了？」"

    player "……闭嘴。"

    narrator "林远在旁边挤眉弄眼。"

    narrator "林晚棠的脸红得更厉害了。"

    # 隐藏立绘
    hide lindao with dissolve

    scene black

    call chapter_title("Day 8 End", "", 1.5)

    jump lindao_day9

# =============================================================================
# Day 9：雨中送伞（小高潮1）
# =============================================================================

label lindao_day9:
    $ persistent.current_day = 9

    scene black

    call chapter_title("雨", "Day 9", 1.5)

    scene bg classroom_day with dissolve

    narrator "天气预报说今天有雨。"

    narrator "早上出门的时候，我特意带了两把伞。"

    narrator "林远问我为什么，我说以防万一。"

    narrator "他看我的眼神，像在看一个恋爱脑。"

    player_thought "……他说得对。"

    scene bg classroom_sunset with dissolve

    narrator "放学的时候，雨下得很大。"

    narrator "教室里的同学陆续离开了。"

    narrator "林晚棠站在走廊尽头，看着雨幕发呆。"

    narrator "她没带伞。"

    player_thought "机会来了。"

    narrator "我走到她身边。"

    show lindao worried at LEFT with dissolve

    player "没带伞？"

    lindao "（回头）嗯……打算等雨停。"

    # ========================================
    # 【B型·态度表态型选择 - Day 9 雨中送伞】
    # ========================================

    menu lindao_day9_umbrella_choice:
        "「我送你回去吧。」":
            # 绅士型
            $ persistent.lindao_personality_impression = "reliable"
            $ persistent.lindao_affection += 5
            $ persistent.lindao_day9_gentleman = True

            narrator "我撑开伞，站在她旁边。"

            player "走吧，我送你。"

            show lindao shy at LEFT with dissolve

            lindao "（犹豫了一下）……那就麻烦你了。"

            narrator "她小心翼翼地靠近我。"

            narrator "肩膀和肩膀之间，隔着一把伞的距离。"

            jump lindao_day9_walking

        "「我们一起撑伞吧。」":
            # 浪漫型
            $ persistent.lindao_personality_impression = "romantic"
            $ persistent.lindao_affection += 8
            $ persistent.lindao_day9_shared_umbrella = True

            narrator "我把自己的伞收起来。"

            player "伞太小，一把就够。"

            show lindao surprised at LEFT with dissolve

            lindao "（脸红）这、这样不太好吧……"

            player "淋感冒了才不好。"

            narrator "我自然地走到她旁边。"

            narrator "伞下，两个人的距离近得能听到彼此的呼吸。"

            # 触发记忆碎片2
            jump memory_fragment_2_day9

        "「你先用伞，我跑回去就行。」":
            # 理性型
            $ persistent.lindao_personality_impression = "considerate"
            $ persistent.lindao_affection += 3
            $ persistent.lindao_day9_rational = True

            narrator "我把伞递给她。"

            player "你先用，我有书包挡一下就行。"

            show lindao worried at LEFT with dissolve

            lindao "可是你会淋湿的……"

            player "没关系，我家近。"

            narrator "她犹豫着接过伞。"

            narrator "离开时，她回头看了我好几眼。"

            $ persistent.lindao_day9_rain_scene = True
            $ persistent.lindao_affection += 3

            jump lindao_day9_end

# ========================================
# 【记忆碎片2 - Day 9触发】
# ========================================

label memory_fragment_2_day9:
    scene black with fade

    narrator "……"

    player_thought "这个场景……"

    player_thought "前世的我，也站在这里过。"

    player_thought "但那时候，我什么都没做。"

    player_thought "看着她一个人淋着雨离开……"

    narrator "一阵恍惚后，我回过神来。"

    # 解锁记忆碎片
    $ persistent.fragment_2 = True
    $ persistent.regret_value += 15

    call show_notification("记忆碎片", "雨中的温暖", "#FFD700")
    narrator "{i}\"前世我也想过送她回家...但那天我退缩了。\"{/i}"

    pause 1.0

    scene bg rainy_street_night with dissolve

    narrator "雨中的街道。"

    narrator "我们并肩走着。"

    narrator "伞很小，小到她靠近我的肩膀时，我能感受到她的体温。"

    narrator "雨水打在伞面上，滴滴答答，像是某种心跳的节奏。"

    narrator "她的发梢被雨水打湿，贴在脸颊上。"

    narrator "我侧过身挡在她前面——"

    player_thought "不知道是因为雨，还是因为她。"

    player_thought "这一刻，前世那个'我没敢追上去'的遗憾，终于被弥补了。"

    jump lindao_day9_talking

# ========================================
# 【雨中漫步 - 共同撑伞路线】
# ========================================

label lindao_day9_walking:
    scene bg rainy_street_night with dissolve

    narrator "雨中的街道。"

    narrator "我们并肩走着。"

    narrator "她小心翼翼地靠近我，保持着微妙的距离。"

    narrator "雨水打在伞面上，滴滴答答。"

    player_thought "她靠得越来越近……"

    player_thought "不知道是因为伞太小，还是因为别的。"

label lindao_day9_talking:
    show lindao worried at LEFT with dissolve

    lindao "（突然开口）陆鸣……"

    player "嗯？"

    lindao "你……好像变了。"

    player "是吗？变得更好了？"

    show lindao shy at LEFT with dissolve

    lindao "（低头）变得更……让人看不懂了。"

    narrator "她抬起头看我，眼睛里有光。"

    narrator "雨伞下，两个人的距离很近。"

    narrator "近到我能看清她睫毛上沾着的雨珠。"

    player "晚棠。"

    lindao "嗯？"

    player "你知道吗……我等这一天，等了很久。"

    narrator "她愣住了。"

    narrator "雨声很大，但我觉得心跳声更大。"

    player "（认真地看着她）因为，我不想再后悔了。"

    narrator "她的眼眶微微泛红。"

    show lindao crying at LEFT with dissolve

    lindao "……你说什么啊，我听不懂。"

    narrator "她低下头，加快了脚步。"

    narrator "但这次，她没有躲开。"

    narrator "她的手背，不经意地碰了碰我的手。"

    narrator "然后，缩了回去。"

    $ persistent.lindao_day9_rain_scene = True
    $ persistent.lindao_affection += 10
    $ persistent.regret_value += 15

    # 【CG-02 雨中撑伞】
    hide lindao
    scene black with dissolve
    show cg_02_rainy_umbrella with dissolve
    pause 2.0
    hide cg_02_rainy_umbrella with dissolve

    jump lindao_day9_home

label lindao_day9_home:
    scene black

    narrator "送她到家门口。"

    narrator "雨还在下，但似乎小了一些。"

    show lindao shy at LEFT with dissolve

    lindao "（接过伞）谢谢你……陆鸣。"

    player "不客气。明天见。"

    lindao "嗯。"

    narrator "她站在门口，目送我离开。"

    narrator "我回头看了一眼——"

    narrator "她还站在那里，手里握着伞。"

    narrator "雨雾中，她的身影有些模糊。"

    narrator "但我知道——"

    narrator "这一次，她不会消失在雨里了。"

    hide lindao with dissolve

    scene black

label lindao_day9_end:
    call chapter_title("Day 9 End", "", 1.5)

    # 根据选择类型显示不同反馈
    if persistent.lindao_day9_shared_umbrella:
        narrator "{i}\"雨中一起撑伞……她的手好凉，但心是暖的。\"{/i}"
        call show_notification("记忆碎片解锁", "雨中的温暖", "#FFD700")
    elif persistent.lindao_day9_gentleman:
        narrator "{i}\"他的肩膀很宽，靠着很有安全感……\"{/i}"
    elif persistent.lindao_day9_rational:
        narrator "{i}\"明明是他把伞让给我……有点傻，但很温柔。\"{/i}"
    else:
        pass

    pause 1.5

    jump lindao_day10

# =============================================================================
# Day 10：天台午餐
# =============================================================================

label lindao_day10:
    $ persistent.current_day = 10

    scene black

    call chapter_title("天台", "Day 10", 1.5)

    scene bg rooftop_sunset with dissolve

    narrator "午休时间。"

    narrator "我像往常一样在天台啃面包。"

    narrator "正要找个地方坐下的时候——"

    narrator "门口传来脚步声。"

    show lindao normal at LEFT with dissolve

    lindao "（出现在门口）……我可以进来吗？"

    player "！（惊讶）"

    player_thought "她怎么来了？"

    player "当、当然可以。"

    narrator "林晚棠拿着一个便当盒，有些局促地走进来。"

    show lindao smile at LEFT with dissolve

    lindao "这里风景挺好的……我能在这里吃吗？"

    player "当然可以。"

    narrator "她在我旁边坐下，铺开便当。"

    narrator "里面是精致的饭团和玉子烧。"

    player "（看着自己的面包）……"

    player_thought "突然觉得有点丢人。"

    show lindao smile at LEFT with dissolve

    lindao "（看了一眼我的面包）……你就吃这个？"

    player "面包怎么了，营养很全面的。"

    show lindao normal at LEFT with dissolve

    lindao "（嘴角微微上扬）你这是来野餐的还是来渡劫的？"

    player "……"

    player_thought "吐槽还是这么犀利。"

    narrator "她低下头，开始吃饭团。"

    narrator "气氛有些安静，但不尴尬。"

    narrator "风吹过天台，带来初夏的味道。"

    show lindao shy at LEFT with dissolve

    lindao "陆鸣。"

    player "嗯？"

    lindao "你最近在看什么书？"

    player "《福尔摩斯探案集》，怎么了？"
    show lindao normal at LEFT with dissolve

    lindao "（皱眉）好重口味……"

    player "悬疑推理，有助于锻炼逻辑思维。"

    lindao "（想了想）那你能给我推荐一本吗？"

    player_thought "她主动找我聊天了。这让我很开心。"

    player "你想看什么类型的？"

    show lindao smile at LEFT with dissolve

    lindao "就……不那么吓人的，有意思的就行。"

    player "东野圭吾的《白夜行》怎么样？"

    lindao "（眼睛亮了）好像听说过。"

    player "回头我把书借你。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）……谢谢。"

    narrator "她低头吃饭的样子，在阳光下显得格外温柔。"

    player_thought "她笑起来真好看。阳光落在她脸上。"

    $ persistent.lindao_affection += 6
    $ persistent.lindao_day10_rooftop_lunch = True

    scene black

    narrator "吃完饭，我们并肩坐着看天。"

    narrator "云很白，风很轻。"

    narrator "这一刻，时间仿佛静止了。"

    show lindao smile at LEFT with dissolve

    lindao "陆鸣……"

    player "嗯？"

    lindao "你为什么对我这么好？"

    player_thought "……"

    player "（微笑）因为你值得。"

    narrator "她没有说话。"

    narrator "但我看到她的嘴角，弯了弯。"

    hide lindao with dissolve

    scene black

    call chapter_title("Day 10 End", "", 1.5)

    jump lindao_day10_5

label lindao_day10_5:
    scene black

    call chapter_title("变数", "Day 10·傍晚", 1.5)

    scene bg classroom_sunset with dissolve

    narrator "天快黑的时候，我在教室门口看到了一个不认识的男生。"

    narrator "穿着干净的校服衬衫，头发梳得很整齐。"

    narrator "手里拿着一袋东西——看起来像是零食或者礼物。"

    narrator "他在等林晚棠。"

    show lindao surprised at LEFT with dissolve

    lindao "（走出教室）……赵轩然？"

    zhao_xuran "（微笑）晚棠！等你好久了。"

    narrator "他把手里的袋子递过去。"

    zhao_xuran "这是你上次说想吃的那个蛋糕，我特意去市里买的。"

    show lindao shy at LEFT with dissolve

    lindao "（愣住）啊……你不用这么麻烦的……"

    zhao_xuran "不麻烦。反正我也要去那边补习。"

    narrator "他的语气很自然。自然到让人觉得他们已经这样很久了。"

    player_thought "这个人是谁？"

    player_thought "这个人是谁？以前完全没注意到班里有这号人。"

    # 躲在一旁观察
    narrator "我站在走廊拐角，看着他们说话。"

    zhao_xuran "对了，你上次说的留学的事——"

    lindao "嗯……"

    zhao_xuran "如果真的要去日本的话，我可以帮你查一下那边的学校信息。"

    zhao_xuran "我表哥就在东京大学念书。"

    show lindao normal at LEFT with dissolve

    lindao "（眼睛亮了一下）真的吗？那就太好了！"

    zhao_xuran "（笑）小事一桩。"

    narrator "他们聊得很自然。"

    narrator "像是已经认识很久的朋友。"

    narrator "或者说……比朋友更多一点？"

    player_thought "他在帮她查日本学校的信息。"

    player_thought "这意味着——他是支持她离开的。"

    player_thought "和我完全相反。"

    # 林晚棠发现主角
    narrator "正想着的时候——"

    lindao "（突然转头）……陆鸣？"

    narrator "她看到了躲在拐角的我。"

    show lindao surprised at LEFT with dissolve

    lindao "你怎么在这里？"

    zhao_xuran "（看过来）这位是？"

    # 三人首次同框
    lindao "啊……这是我同桌，陆鸣。"

    lindao "陆鸣，这是赵轩然，以前……我们是一个初中的。"

    zhao_xuran "（礼貌地点头）你好。"

    narrator "他的笑容很标准。"

    narrator "标准的、挑不出任何毛病的、社交式的笑容。"

    player_thought "我不喜欢这个人。"

    player "（挤出笑容）你好。"

    zhao_xuran "（看了看手腕上的表）那我先走了，补习要迟到了。"

    zhao_xuran "晚棠，那个资料我晚上QQ上发给你。"

    lindao "嗯，谢谢。"

    narrator "他离开的时候，又看了我一眼。"

    narrator "不是敌意的眼神。"

    narrator "更像是——在确认一个竞争对手的存在。"

    hide lindao with dissolve

    scene bg corridor_window_sunset with dissolve

    narrator "走廊上只剩下我和林晚棠两个人。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）你……都看到了？"

    player "嗯。"

    lindao "他……是我初中同学。"

    lindao "之前帮过我一些忙……"

    player "（平静地）他喜欢你吧。"

    narrator "她愣住了。"

    show lindao worried at LEFT with dissolve

    lindao "什么？没有的事……"

    player "晚棠。"

    narrator "我没有追问。"

    player "不管他是谁，做什么，那是你的事。"

    player "我只是觉得……你应该知道我在意你。"

    narrator "她的表情复杂起来。"

    narrator "有惊讶，有慌乱，也有某种我说不清的东西。"

    show lindao normal at LEFT with dissolve

    lindao "陆鸣……你今天怎么怪怪的……"

    player "大概是因为看到有人给你送蛋糕，心里不太舒服吧。"

    narrator "话一出口我就后悔了——"

    narrator "这也太直白了。"

    narrator "但她的脸红了。"

    show lindao shy at LEFT with dissolve

    lindao "（低头，声音很小）……笨蛋。"

    narrator "然后她转身跑了。"

    narrator "但跑到楼梯口的时候——"

    narrator "她回过头来。"

    lindao "（大声）明天见！"

    narrator "声音大得整个走廊都能听到。"

    $ persistent.lindao_affection += 5
    $ persistent.lindao_day10_rival_met = True
    $ persistent.zhao_introduced = True

    hide lindao with dissolve

    scene black

    narrator "我站在原地。"

    narrator "心情很复杂。"

    player_thought "有一个条件比我更好的人也在追求她……"

    player_thought "而且他们认识得更久，关系看起来也更自然。"

    player_thought "但我不会放弃的。"

    player_thought "因为这次——我不会再逃了。"

    scene black

    jump lindao_day11

# =============================================================================
# Day 11：夕阳下的对话
# =============================================================================

label lindao_day11:
    $ persistent.current_day = 11

    scene black

    call chapter_title("夕阳", "Day 11", 1.5)

    scene bg classroom_sunset with dissolve

    narrator "放学后。"

    narrator "我故意留到最后。"

    narrator "林晚棠也在整理东西，似乎在等什么人。"

    narrator "教室里只剩下我们两个人。"

    narrator "夕阳从窗户照进来，把一切都染成金色。"

    narrator "她的侧脸，在光线下格外柔和。"

    player_thought "这个画面……前世也有过。"

    player_thought "但那时候，我只是坐在原位，什么都没说。"

    player_thought "等我想开口的时候，她已经走了。"

    show lindao normal at LEFT with dissolve

    player "晚棠。"

    lindao "（抬头）嗯？"

    player "放学后……能陪我聊会天吗？"

    narrator "她愣了一下，然后轻轻点头。"

    show lindao smile at LEFT with dissolve

    lindao "好啊，反正我也没什么事。"

    scene black

    narrator "夕阳西斜。"

    narrator "我们并肩站在窗边，看着天边的晚霞。"

    narrator "她的发丝被晚风轻轻吹起。"

    narrator "我伸出手，假装帮她拨开——"

    narrator "指尖碰到她的耳廓。"

    narrator "她的身体微微一颤。"

    show lindao shy at LEFT with dissolve

    lindao "（脸红）你……"

    player "头发挡到眼睛了。"

    narrator "她没有躲开。"

    narrator "只是低着头，任由我把她的头发别到耳后。"

    narrator "夕阳把她的耳朵染成了粉色。"

    player "晚棠。"

    show lindao normal at LEFT with dissolve

    lindao "嗯……？"

    player "你知道吗，这个场景我见过很多次。"

    show lindao surprised at LEFT with dissolve

    lindao "（疑惑）什么意思？"

    player "没什么……"

    player "（微笑）就是突然觉得，能和你一起看夕阳，挺好的。"

    narrator "她抬起头，看着我。"

    narrator "眼睛里有光，有疑惑，有……别的什么。"

    show lindao shy at LEFT with dissolve

    lindao "陆鸣……你到底想说什么？"

    player "（轻声）以后你就知道了。"

    narrator "她没有追问。"

    narrator "只是转过身，重新看向夕阳。"

    narrator "她的手，不经意地碰了碰我的手。"

    narrator "这次，她没有收回去。"

    $ persistent.lindao_affection += 10
    $ persistent.lindao_day11_sunset = True
    $ persistent.regret_value += 20

    scene black

    narrator "天色渐暗。"

    narrator "我们一起走出校门。"

    # 校门外·黄昏街道
    scene bg school_gate_dusk with dissolve

    narrator "这次的分别，没有遗憾。"

    hide lindao with dissolve

    scene black

    call chapter_title("Day 11 End", "", 1.5)

    jump lindao_day12

# =============================================================================
# Day 12：多肉植物的约定
# =============================================================================

label lindao_day12:
    $ persistent.current_day = 12

    scene black

    call chapter_title("多肉", "Day 12", 1.5)

    scene black

    narrator "林晚棠发来消息。"

    narrator "'你不是说有好书吗？什么时候借我？'"

    narrator "我回复：'周末有空吗？我去你家拿。'"

    narrator "她的回复来得很快。"

    narrator "'好啊，周六下午两点？'"

    player_thought "她答应了。"

    player_thought "这是……约会吗？"

    scene black

    narrator "周六下午。"

    narrator "我站在林晚棠家门口，手里拿着《白夜行》。"

    narrator "心跳有些快。"

    player_thought "心跳有些快。第一次去女生家。"

    player "（深呼吸，按门铃）"

    show lindao smile at LEFT with dissolve

    lindao "（开门）你来了！快进来。"

    narrator "她今天穿的是便装——一件淡黄色的连衣裙。"

    narrator "和平时在学校的样子不太一样。"

    narrator "更……温柔了。"

    player "（走进门）打扰了。"

    # ========================================
    # 【C型·细节观察型选择 - Day 12 参观房间】
    # ========================================

    show lindao smile at LEFT with dissolve

    lindao "你先坐，我去给你倒杯水。"

    narrator "她走进厨房。"

    narrator "我一个人留在客厅，环顾四周……"

    menu lindao_day12_observation:
        "仔细看看书架":
            $ persistent.lindao_day12_observed_bookshelf = True

            narrator "书架上摆满了书。"

            narrator "大多是文学类，还有一些日本文学……"

            narrator "《挪威的森林》《雪国》《1Q84》……"

            player_thought "原来她喜欢日本文学。"

            player_thought "难怪……会去日本留学。"

            # 获得"共同话题"信息
            $ persistent.lindao_common_topic_unlocked = True

            call show_notification("观察", "📚 书架上摆满了日本文学书籍", "#6B9FFF")

        "观察阳台的多肉植物":
            $ persistent.lindao_day12_observed_succulent = True

            narrator "阳台上有几盆多肉植物。"

            narrator "大部分都很精神……"

            narrator "但有一盆明显快枯萎了，叶子发黄发软。"

            player_thought "这盆……她应该很在意吧。"

            # 触发多肉约定前置
            $ persistent.lindao_succulent_hint = True

            call show_notification("观察", "🌱 一盆快枯萎的多肉……她似乎很在意它", "#6B9FFF")

        "看看墙上的全家福":
            $ persistent.lindao_day12_observed_photo = True

            narrator "墙上挂着一张全家福。"

            narrator "照片里是林晚棠小时候的样子。"

            narrator "旁边站着一个男人……是她父亲吧。"

            narrator "但照片上有一些划痕，像是被刻意刮过的。"

            player_thought "她和父亲的关系……"

            # 获得家庭背景信息
            $ persistent.lindao_family_background_hint = True

            call show_notification("观察", "🖼️ 全家福上……有人被刮掉了？", "#6B9FFF")

        "静静坐着等她回来":
            $ persistent.lindao_day12_did_nothing = True

            narrator "我坐在沙发上，没有乱动。"

            narrator "这是她的家，我不该随便翻看。"

            narrator "……"

            narrator "厨房里传来水流声。"

            narrator "她很快就会出来。"

    # 继续剧情
    hide lindao with dissolve

    # 客厅 - 她端水出来
    scene bg living_room with dissolve

    narrator "她端着两杯水走出来。"

    narrator "看到我坐在沙发上，她的表情放松了一些。"

    narrator "但我注意到——"

    narrator "她的目光扫过我刚才'观察'的地方，似乎有一丝紧张。"

    show lindao normal at LEFT with dissolve

    lindao "久等了。"

    narrator "她把水递给我。"

    narrator "然后，走向阳台角落。"

    # 阳台 - 多肉植物
    scene bg balcony with dissolve

    # 记忆碎片3触发（多肉观察后）
    if persistent.lindao_day12_observed_succulent:
        player_thought "她对那盆多肉……真的很在意。"

        player_thought "我记得前世……她也提过这件事。"

        narrator "一阵恍惚。"

        # 解锁记忆碎片3
        $ persistent.fragment_3 = True

        call show_notification("记忆碎片", "枯萎的多肉", "#FFD700")
        narrator "{i}\"我记得她提过，她最珍视的东西总养不活...\"{/i}"

        $ persistent.regret_value += 10

    show lindao normal at LEFT with dissolve

    lindao "那是我的宝贝！"

    player "宝贝？"

    lindao "（走到角落，蹲下来）嗯，我养的多肉。"

    narrator "我跟着走过去看。"

    narrator "她小心翼翼地照顾那些小植物的样子，很可爱。"

    player "你很喜欢植物？"

    show lindao smile at LEFT with dissolve

    lindao "（微笑）嗯，因为它们很安静。"

    player "安静？"

    lindao "不需要说很多话，只要好好照顾就好。"

    narrator "她的声音很轻，像是在说什么秘密。"

    player_thought "……"

    player_thought "她是不是觉得和其他人说话很困难？"

    narrator "我注意到有一株多肉快枯萎了。"

    player "这株……好像不太精神。"

    show lindao normal at LEFT with dissolve

    lindao "（叹气）是啊，已经救不活了……我总是养不好。"

    player "（拿起花盆）给我看看。"

    show lindao surprised at LEFT with dissolve

    lindao "（惊讶）你会养植物？"

    player "（检查）可能是浇水太多了……还有救。"

    narrator "她瞪大了眼睛。"

    player "你把枯叶摘掉，移到阳光充足的地方，三天浇一次水就好。"

    lindao "真的吗？"

    player "真的。你要是不信，我们打个赌。"

    lindao "打什么赌？"

    player "一周后它要是活了，你请我喝奶茶。"

    narrator "她愣了一下，然后笑了。"

    show lindao smile at LEFT with dissolve

    lindao "（接过花盆）好，一言为定。"

    narrator "她笑起来的样子，像是阳光突然照进了房间。"

    $ persistent.lindao_affection += 8
    $ persistent.lindao_day12_succulent = True

    hide lindao with dissolve

    scene black

    narrator "我在她家待了一下午。"

    narrator "我们一起看书，一起聊天。"

    narrator "她给我切了水果，我帮她把多肉移到阳台上。"

    narrator "很普通的下午。"

    narrator "但前世，我从来没有过这样的下午。"

    narrator "傍晚离开的时候，她送我到门口。"

    show lindao smile at LEFT with dissolve

    lindao "谢谢你今天来看我。"

    player "（微笑）下次再来的时候，那株多肉应该就活了。"

    show lindao shy at LEFT with dissolve

    lindao "（脸红）……那我等你的好消息。"

    hide lindao with dissolve

    scene black

    call chapter_title("Day 12 End", "", 1.5)

    jump lindao_day13

# =============================================================================
# Day 13：移民风波（小高潮2）
# =============================================================================

label lindao_day13:
    $ persistent.current_day = 13

    scene black

    call chapter_title("图书馆", "Day 13", 1.5)

    scene bg library with dissolve

    narrator "我和林晚棠约在图书馆一起复习。"

    narrator "但她一直心不在焉。"

    narrator "笔尖在纸上划来划去，却一个字也没写。"

    player "晚棠？"

    show lindao worried at LEFT with dissolve

    lindao "（回神）啊……什么？"

    player "你怎么了？看起来心事重重的样子。"

    narrator "她沉默了一会儿。"

    narrator "然后，轻轻开口。"

    lindao "陆鸣……我可以跟你说一件事吗？"

    player "当然。"

    narrator "她放下笔，看向窗外。"

    lindao "我爸……我妈……"

    narrator "她的声音有些颤抖。"

    show lindao crying at LEFT with dissolve

    lindao "他们可能要离婚了。"

    player "！"

    narrator "她继续说下去。"

    lindao "我妈今天打电话来说，她在办移民手续。"

    lindao "她要带我去日本。"

    narrator "——日本。"

    narrator "这两个字像一盆冷水，浇在我心上。"

    player_thought "前世……她真的去了日本。我再也见不到她了。"

    player_thought "毕业典礼那天，她笑着和所有人合影。"

    player_thought "然后就走了，再也没回来。"

    player_thought "这一世……不会了。"

    player "什么时候的事？"

    lindao "刚决定的。我妈说那边有更好的工作机会……"

    narrator "她的声音越来越小。"

    lindao "让我跟她一起去。"

    narrator "她低下头，肩膀微微颤抖。"

    player_thought "……"

    player_thought "这次，我不会让她一个人承受。"

    # ========================================
    # 【A型·命运转折型选择 - Day 13 移民话题】
    # ========================================

    menu lindao_day13_choice:
        "她应该有更好的选择……吧":
            # 错误选项 - 表达犹豫
            jump lindao_day13_choice_a
        "（鼓起勇气）我不想让你走":
            # 坦诚心意 - ★最佳选项
            jump lindao_day13_choice_b
        "别急着做决定，让我帮你想想办法":
            # 承诺解决问题 - ★正确选项
            jump lindao_day13_choice_c

label lindao_day13_choice_a:
    player "她应该有更好的选择……吧。"

    narrator "我说出这句话的时候，自己都觉得心虚。"

    narrator "这句话等于'我不在乎你去哪'。"

    narrator "她抬起头，看了我一眼。"

    narrator "眼睛里有失望。"

    show lindao worried at LEFT with dissolve

    lindao "……是吗。"

    narrator "她收回目光，重新看向窗外。"

    narrator "气氛变得有些沉重。"

    $ persistent.lindao_affection -= 10
    $ persistent.lindao_day13_wrong_choice = True
    $ persistent.lindao_long_distance_route = True

    hide lindao with dissolve

    jump lindao_day13_continue

label lindao_day13_choice_b:
    # ★最佳选项 - 坦诚表达心意
    player "（鼓起勇气）我不想让你走。"

    narrator "话说出口的瞬间，我自己都愣住了。"

    narrator "她的眼睛睁大了。"

    show lindao surprised at LEFT with dissolve

    lindao "你……说什么？"

    player "（认真地看着她）晚棠，你对我来说很重要。"

    player "我不想你离开。"

    show lindao crying at LEFT with dissolve

    lindao "（低下头）可是……我妈已经决定了……"

    player "那我们就一起想办法。"

    narrator "她抬起头，泪眼婆娑地看着我。"

    show lindao worried at LEFT with dissolve

    lindao "……真的吗？"

    player "真的。"

    $ persistent.lindao_affection += 15
    $ persistent.lindao_day13_confession_hint = True
    $ persistent.lindao_convince_father_event = True

    hide lindao with dissolve

    jump lindao_day13_continue

label lindao_day13_choice_c:
    # ★正确选项 - 承诺解决问题
    player "别急着做决定，让我帮你想想办法。"

    narrator "她抬起头，有些疑惑。"

    show lindao normal at LEFT with dissolve

    lindao "想办法？"

    player "（认真）晚棠，你先别急着做决定。"

    player "给我一点时间，让我弄清楚到底发生了什么。"

    narrator "她沉默了一会儿。"

    lindao "……你会帮我？"

    player "当然。"

    narrator "她轻轻点了点头。"

    show lindao smile at LEFT with dissolve

    lindao "……谢谢你，陆鸣。"

    $ persistent.lindao_affection += 10
    $ persistent.lindao_day13_promise = True
    $ persistent.lindao_convince_father_event = True

    hide lindao with dissolve

    jump lindao_day13_continue

label lindao_day13_continue:
    narrator "图书馆里很安静。"

    narrator "只有空调的嗡嗡声，和窗外偶尔传来的鸟鸣。"

    narrator "她坐在我对面，眼眶红红的。"

    show lindao worried at LEFT with dissolve

    narrator "我不知道该说什么。"

    narrator "但我知道——"

    narrator "这次，我不会让她一个人。"

    $ persistent.lindao_affection += 5
    $ persistent.lindao_day13_immigration_talk = True
    $ persistent.regret_value += 10

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "离开图书馆的时候，天已经黑了。"

    narrator "她走在我身边，比平时更沉默。"

    player "晚棠。"

    show lindao worried at LEFT with dissolve

    lindao "嗯？"

    player "不管发生什么，我都会站在你这边。"

    narrator "她没有说话。"

    narrator "但她加快了脚步，走到了我前面。"

    narrator "然后——"

    narrator "她回过头，对我笑了笑。"

    show lindao smile at LEFT with dissolve

    lindao "谢谢你，陆鸣。"

    narrator "路灯下，她的笑容很温暖。"

    narrator "但我看到了她眼角的泪光。"

    hide lindao with dissolve

    scene black

    call chapter_title("Day 13 End", "", 1.5)

    jump lindao_day14

# =============================================================================
# Day 14：多肉存活·承诺（小高潮3）
# =============================================================================

label lindao_day14:
    $ persistent.current_day = 14

    scene black

    call chapter_title("天台", "Day 14", 1.5)

    scene black

    narrator "一整周，我都在照顾那株多肉。"

    narrator "每天定时浇水，移到阳光下，观测土壤湿度。"

    narrator "室友问我怎么突然对植物感兴趣了。"

    narrator "我说是为了一个约定。"

    narrator "他看我的眼神，像在看一个恋爱脑。"

    player_thought "……他们说得对。"

    scene black

    narrator "周六。"

    narrator "我带着那株多肉，去找林晚棠。"

    narrator "一周前它还奄奄一息。"

    narrator "现在——"

    narrator "叶子已经挺立起来，泛着健康的光泽。"

    scene bg classroom_day with dissolve

    narrator "天台。"

    narrator "林晚棠已经在那里等着了。"

    narrator "我走过去，把多肉递给她。"

    player "我答应过你的。"

    narrator "她接过花盆，眼睛一下子亮了。"

    show lindao surprised at LEFT with dissolve

    lindao "（惊讶）真的活了！"

    player "（微笑）我说过有救的。"

    narrator "她小心翼翼地捧着花盆，像是捧着什么珍贵的宝物。"

    narrator "夕阳照在她身上，把一切都染成金色。"

    narrator "她的侧脸，在光线下格外柔和。"

    narrator "我忍不住伸出手——"

    narrator "帮她把垂落的发丝别到耳后。"

    show lindao shy at LEFT with dissolve

    lindao "（身体微微一颤）"

    narrator "她的耳朵瞬间红了。"

    narrator "我没有收回手。"

    narrator "指尖在她耳边停留了一秒。"

    narrator "心跳漏了一拍。"

    narrator "然后，我收回手。"

    narrator "假装什么都没发生。"

    $ persistent.lindao_affection += 8

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "我们并肩坐在天台边缘，看着夕阳西沉。"

    show lindao normal at LEFT with dissolve

    lindao "（轻声）陆鸣……谢谢你。"

    player "谢我什么？"

    lindao "谢谢你救活了我的多肉……还有……"

    narrator "她没有说下去。"

    player "还有什么？"

    show lindao worried at LEFT with dissolve

    lindao "（看向远方）谢谢你愿意听我说那些事。"

    player "……"

    player "晚棠，关于移民的事……"

    narrator "她沉默了一会儿。"

    hide lindao with dissolve
    show lindao worried at LEFT with dissolve

    lindao "我妈……已经办得差不多了。"

    lindao "估计高考之后就要走了。"

    narrator "我的心沉了下去。"

    player_thought "……前世就是这样。"

    player_thought "高考结束，她就走了。"

    player_thought "然后十年，再也没见过。"

    player "（轻声）你很想去吧？"

    show lindao normal at LEFT with dissolve

    lindao "（摇头）我不知道……"

    narrator "她的声音很轻。"

    lindao "我想去……因为我爸……"

    lindao "但我又有点……舍不得……"

    narrator "她没有说舍不得什么。"

    narrator "但我知道。"

    player "晚棠。"

    show lindao worried at LEFT with dissolve

    lindao "嗯？"

    player "你不用急着决定。"

    narrator "她抬起头看我。"

    player "在那之前——给我一点时间。"

    player "我想试试，能不能改变这件事。"

    narrator "她愣住了。"

    show lindao normal at LEFT with dissolve

    lindao "改变……？"

    player "（微笑）相信我。"

    narrator "她看着我，眼睛里有光。"

    narrator "有希望，有疑惑，也有……信任。"

    show lindao smile at LEFT with dissolve

    lindao "（轻轻点头）……好。"

    narrator "夕阳沉入地平线。"

    narrator "天边最后一抹红色渐渐消失。"

    narrator "但她的眼睛里，还有光。"

    narrator "这次，我会让那束光留在这里。"

    # 解锁记忆碎片4 - 她的眼泪
    $ persistent.fragment_count += 1
    $ persistent.fragments_collected.append("frag_008")
    $ persistent.lindao_day14_fragment_unlocked = True

    call show_notification("记忆碎片", "她的眼泪", "#FFD700")
    narrator "{i}\"前世，我从未见过她哭。\"{/i}"
    narrator "{i}\"这一世，我要亲手擦去她的眼泪。\"{/i}"

    $ persistent.lindao_affection += 10
    $ persistent.lindao_day14_promise = True
    $ persistent.regret_value += 20

    # 【CG-03 天台拥抱】
    hide lindao
    scene black with dissolve
    show cg_03_rooftop_embrace with dissolve
    pause 2.0
    hide cg_03_rooftop_embrace with dissolve

    scene black

    narrator "送她回家的路上，我们都没怎么说话。"

    # 住宅区街道·夜景（晴）
    scene bg residential_night_clear with dissolve

    narrator "但气氛很舒服。"

    narrator "像是两个人之间，已经有了某种默契。"

    scene black

    call chapter_title("承诺已许下", "Day 14 End", 1.5)

    jump lindao_day15

# =============================================================================
# Day 15-16：寻找突破口
# =============================================================================

label lindao_day15:
    $ persistent.current_day = 15

    scene black

    call chapter_title("情报", "Day 15", 1.5)

    scene black

    narrator "为了林晚棠，我必须找到解决问题的办法。"

    narrator "前世……她爸爸好像戒赌了。"

    narrator "但我不记得具体是什么时候、怎么戒的。"

    narrator "我只知道结果。"

    narrator "这是重生者最大的优势，也是最大的限制。"

    # 苏念卿的咖啡馆 - 获取情报
    scene bg cafe_bar with dissolve

    narrator "放学后，我去了一趟苏念卿的咖啡馆。"

    narrator "'晚星咖啡'——前世我经常来这里。"

    narrator "苏念卿正在吧台后面冲咖啡。"

    suni "哟，小弟弟来了。"

    player "念卿姐。"

    suni "（放下咖啡杯）怎么，有心事？"

    player "……我想问你一件事。"

    suni "（微笑）问吧。"

    player "你了解移民日本的事吗？"

    suni "（眉毛一挑）怎么，你朋友要移民？"

    player "嗯，她妈妈要去日本工作。"

    suni "工作签证的话……其实有另一种选择。"

    player "什么选择？"

    suni "你可以问问她妈妈具体情况。"

    suni "如果是派遣工作的话，有时候会因为公司变故取消。"

    suni "或者换到国内其他城市。这样的话，签证自然就作废了。"

    player "（若有所思）……"

    player "怎么才能让那边的工作黄掉……"

    suni "（笑）你想得可真多。"

    suni "其实，最关键的问题不是工作。"

    player "那是什么？"

    suni "是让她妈妈有留下来的理由。"

    narrator "我愣住了。"

    suni "一个女人决定带孩子远走他乡，通常是因为对现状失望了。"

    suni "如果她能看到留下来的希望……"

    suni "也许，她会改变主意。"

    $ persistent.lindao_day15_info_gained = True

    scene black

    narrator "我走出咖啡馆，脑海里翻涌着苏念卿的话。"

    # 咖啡馆外·黄昏街道
    scene bg cafe_street_evening with dissolve

    narrator "'让她妈妈有留下来的理由'……"

    narrator "前世的林晚棠家……"

    narrator "林父欠了很多赌债。"

    narrator "林母就是因为这个才想离开的。"

    player_thought "如果林父能戒赌……"

    player_thought "如果他能重新开始……"

    player_thought "林母就有留下来的理由了。"

    scene black

    call chapter_title("Day 15 End", "", 1.5)

    jump lindao_day16

label lindao_day16:
    $ persistent.current_day = 16

    scene black

    call chapter_title("父亲的真相", "Day 16", 1.5)

    scene bg classroom_day with dissolve

    narrator "第二天，我在学校找了个机会和林晚棠单独说话。"

    player "晚棠，你爸那边……是不是有什么问题？"

    narrator "她的表情变得有些警惕。"

    show lindao worried at LEFT with dissolve

    lindao "你怎么知道？"

    player "我猜的。你最近看起来心事重重……"

    narrator "她沉默了一会儿。"

    show lindao normal at LEFT with dissolve

    lindao "我爸……欠了很多钱。"

    narrator "果然。"

    lindao "我妈就是因为这个才想离开的。"

    narrator "她低下头，声音很轻。"

    show lindao worried at LEFT with dissolve

    lindao "他说会戒赌……但每次都食言。"

    lindao "我妈已经不相信他了。"

    player_thought "……"

    player_thought "原来背后还有这些我不知道的事。"

    player "晚棠。"

    show lindao surprised at LEFT with dissolve

    lindao "嗯？"

    player "我可以帮你想办法吗？"

    narrator "她抬起头，眼睛里有惊讶。"

    lindao "你……？"

    player "（认真）让我试试。"

    narrator "她犹豫了很久。"

    show lindao smile at LEFT with dissolve

    lindao "（轻声）……好。"

    $ persistent.lindao_affection += 5
    $ persistent.lindao_day16_dad_talk = True

    hide lindao with dissolve

    scene black

    narrator "放学后，我去打听了林父的下落。"

    # 放学后的走廊·夕阳窗边
    scene bg corridor_window_sunset with dissolve

    narrator "走廊里，夕阳透过窗户洒进来。"

    narrator "我的影子被拉得很长。"

    narrator "有人说在城南的棋牌室看到他。"

    narrator "我犹豫了很久。"

    scene black

    narrator "去，还是不去？"

    player_thought "这不关我的事……"

    player_thought "但如果我不出手……"

    player_thought "她就会离开。"

    player_thought "这次，我不想再错过了。"

    # 城南棋牌室 — 第一次尝试（失败）
    scene bg mahjong_parlor with dissolve

    narrator "城南棋牌室。"

    narrator "烟雾缭绕，空气浑浊。"

    narrator "角落里，一个中年男人正对着麻将发呆。"

    narrator "林父。"

    narrator "我走过去，在他对面坐下。"

    player "林叔叔。"

    narrator "他抬起头，眼神浑浊。"

    lin_father "你是谁？"

    player "我是晚棠的同学。"

    narrator "他的表情变了一下。"

    lin_father "……你来干什么？"

    player "我想跟您谈谈。"

    lin_father "（冷笑）谈什么？小孩子别管大人的事。"

    # ========== QTE说服林父（第一次尝试 - 失败线前置） ==========
    menu lindao_day16_persuasion_qte:
        "直接摊牌（理性说服）":
            jump lindao_day16_persuasion_rational
        "以情动人（情感打动）":
            jump lindao_day16_persuasion_emotional
        "给他压力（最后通牒）":
            jump lindao_day16_persuasion_ultimatum

    label lindao_day16_persuasion_rational:
        narrator "我决定直接切入正题。"

        player "（直接）我知道您欠了很多钱。"

        narrator "他的脸色沉了下来。"

        lin_father "你……"

        player "我还知道，您太太要带晚棠去日本。"

        narrator "他没有说话。"

        player "我是来告诉您——如果您继续这样下去，晚棠就要走了。"

        player "以后您可能再也见不到她了。"

        narrator "他的身体微微一震。"

        player "我知道戒赌很难。但您还有机会。"

        narrator "他沉默了很久。"

        $ persistent.lindao_day16_persuasion_result = "rational"
        $ persistent.lindao_day16_father_impressed = False

        jump lindao_day16_first_attempt_fail

    label lindao_day16_persuasion_emotional:
        narrator "我决定用真心打动他。"

        player "（放缓语速）林叔叔，我知道您现在很难。"

        narrator "他的表情微微一变。"

        player "但晚棠她……一直在担心您。"

        player "上次她跟我说，她很想念小时候您带她去公园的时候。"

        narrator "这是真的——前世我在整理她遗物时看到过那张照片。"

        lin_father "（沉默）……"

        player "我知道戒赌很难。"

        player "但您还有机会。"

        player "晚棠她……很需要父亲。"

        narrator "他的眼眶红了。"

        lin_father "（声音沙哑）你……你怎么知道……"

        player "因为我也曾是那个'差点失去一切'的人。"

        narrator "这句话是真的——前世的35年，我活成了最遗憾的样子。"

        narrator "他没有再说话，但眼睛里有了不一样的东西。"

        $ persistent.lindao_day16_persuasion_result = "emotional"
        $ persistent.lindao_day16_father_impressed = True

        # 情感路线：第一次没有完全失败，但也没完全成功
        jump lindao_day16_first_attempt_partial

    label lindao_day16_persuasion_ultimatum:
        narrator "我决定给他最后的压力。"

        player "（直接）我知道您欠了很多钱。"

        narrator "他的脸色沉了下来。"

        player "我还知道，您太太要带晚棠去日本。"

        player "（加重语气）如果您继续这样下去——"

        player "晚棠就会离开，这辈子您可能再也见不到她了。"

        narrator "他的身体微微一震。"

        player "林叔叔，您想好了吗？"

        narrator "他沉默了很久。"

        narrator "然后——"

        lin_father "（拍桌）你算什么东西！"

        narrator "他站起身，神色不善。"

        player_thought "糟糕，说得太过了……"

        lin_father "滚！"

        narrator "我被赶出了棋牌室。"

        $ persistent.lindao_day16_persuasion_result = "ultimatum"
        $ persistent.lindao_day16_father_impressed = False
        $ persistent.lindao_day16_persuasion_failed = True

        jump lindao_day16_first_attempt_fail

    # ========================================
    # 【关键冲突点 - 第一次尝试失败/部分失败】
    # ========================================

    label lindao_day16_first_attempt_fail:

        scene bg urban_street_dusk with dissolve

        narrator "被赶出来之后，我一个人走在城南的街道上。"

        narrator "天已经黑透了。"

        player_thought "失败了……"

        player_thought "不仅没说服他，还把事情搞砸了。"

        player_thought "如果林晚棠知道了……"

        # 第二天：林晚棠发现了 — 关系降至冰点
        scene black

        call chapter_title("裂痕", "Day 16·傍晚", 1.5)

        scene bg classroom_sunset with dissolve

        narrator "第二天放学后。"

        narrator "林晚棠堵在了教室门口。"

        show lindao crying at LEFT with dissolve

        lindao "你去找过我爸？"

        narrator "她的声音在发抖。"

        player "晚棠，听我说——"

        lindao "（提高音量）谁让你去的？！"

        narrator "教室里的同学都看了过来。"

        show lindao worried at LEFT with dissolve

        lindao "我爸爸回来大发脾气！他说有个'多事的小孩'去找过他！"

        lindao "你知道他被你刺激之后做了什么吗？"

        narrator "她的眼泪掉下来。"

        lindao "他又去打了！他说既然有人看不起他，那他就继续打！"

        player "……我不知道会变成这样。"

        lindao "（擦眼泪，声音变得很冷）陆鸣，我以为你是为了我好。"

        lindao "但你只是觉得自己了不起而已吧？觉得你能改变一切？"

        player "不是的——"

        lindao "（打断）别再来找我。"

        narrator "她转身跑了出去。"

        narrator "我想追——"

        narrator "但脚步像灌了铅一样沉重。"

        $ persistent.lindao_affection -= 20
        $ persistent.lindao_day16_ice_point = True
        $ persistent.lindao_relationship_iced = True

        hide lindao with dissolve

        scene black

        narrator "{b}{color=#FF6B6B}关系降至冰点{/color}{/b}"

        narrator "这一次，我真的搞砸了。"

        scene black

        call chapter_title("Day 16 End", "", 1.5)

        jump lindao_day17

    label lindao_day16_first_attempt_partial:

        # 情感路线：没有完全成功，但也触动了林父
        # 但林晚棠还是从侧面得知了，产生了矛盾（程度较轻）
        scene bg urban_street_dusk with dissolve

        narrator "走出棋牌室的时候——"

        lin_father "（叫住我）等一下。"

        narrator "我回过头。"

        lin_father "你……叫什么名字？"

        player "陆鸣。"

        lin_father "（沉默）……你让我想起了些事情。"

        narrator "他没有说下去。"

        narrator "但我能看出他的内心在挣扎。"

        player "林叔叔，我会再来的。"

        lin_father "（摇头）别来了。这是我自己的事。"

        narrator "他转身走进了棋牌室的深处。"

        # 但第二天：矛盾还是发生了（程度较轻）
        scene black

        call chapter_title("误会", "Day 16·次日", 1.5)

        scene bg school_gate_dusk with dissolve

        narrator "第二天早上。"

        narrator "林晚棠没有等我。"

        narrator "我一个人走到学校。"

        show lindao worried at LEFT with dissolve

        narrator "到了教室，我看到她在座位上。"

        narrator "但没有看我。"

        player "晚棠……"

        lindao "（低头翻书）我今天想安静一下。"

        narrator "她的声音很平静。"

        narrator "但那种平静比生气更让人不安。"

        player "是不是你爸说了什么？"

        show lindao normal at LEFT with dissolve

        lindao "（抬头，眼神复杂）他什么都没说。"

        lindao "但他昨晚喝了酒，一直在说'那个小孩说得对'。"

        lindao "（苦笑）你知道我最怕什么吗？不是他去赌博。"

        lindao "是给他希望之后，又让他失望。"

        narrator "我心里一紧。"

        lindao "陆鸣……你的出发点是好的。"

        lindao "但有些事情，不是一个高中生能解决的。"

        $ persistent.lindao_affection -= 8
        $ persistent.lindao_day16_partial_conflict = True

        hide lindao with dissolve

        scene black

        call chapter_title("Day 16 End", "", 1.5)

        jump lindao_day17

# =============================================================================
# Day 17：低谷期 / 冷战
# =============================================================================

label lindao_day17:
    $ persistent.current_day = 17

    scene black

    call chapter_title("沉默", "Day 17", 1.5)

    scene bg classroom_day with dissolve

    narrator "第三天。"

    narrator "林晚棠没有跟我说话。"

    narrator "不是故意不理我——"

    narrator "而是像我们之间竖了一道看不见的墙。"

    player_thought "她想安静。我应该尊重她。"

    # 冷战中的观察 — 赵轩然趁虚而入
    narrator "但有些事情，不想看到也会看到。"

    narrator "午休时间。我从教室后门进来——"

    narrator "赵轩然坐在林晚棠前面的座位上。"

    show lindao smile at LEFT_CENTER with dissolve

    zhao_xuran "（递过一张纸）这是东京大学的申请资料，我表哥发给我的。"

    lindao "（接过，眼睛亮了）哇……好详细……"

    zhao_xuran "你要是有什么不懂的随时问我，反正我表哥在那边。"

    narrator "他的语气很自然。自然到让人挑不出任何毛病。"

    narrator "而林晚棠笑得很放松。"

    narrator "是一种这几天她没有对我展现过的放松。"

    player_thought "他在帮她规划去日本的未来。"

    player_thought "而我……差点毁了她爸爸。"

    # 陈墨的意外介入 — 打破主角的孤独感
    narrator "我转身想走——"

    chen "陆鸣。"

    narrator "陈墨站在走廊上。"

    chen "你的表情很难看。"

    player "……被你看出来了。"

    chen "（沉默了两秒）……上次熨斗的事，谢了。"

    narrator "她说完就走了。"

    narrator "没有多问一句。"

    narrator "但这三个字，在今天的冷风里显得格外暖和。"

    $ persistent.chen_affection += 2

    # 下午的场景 — 尝试修复
    scene bg corridor_window_sunset with dissolve

    narrator "放学后。"

    narrator "我在楼梯口等她。"

    show lindao normal at LEFT with dissolve

    narrator "她看到了我。"

    narrator "脚步顿了一下——然后继续往下走。"

    player "晚棠！"

    narrator "她停下脚步。"

    narrator "但没有回头。"

    lindao "（背对着我）我今天要早点回去。"

    player "我知道错了。"

    narrator "她的肩膀微微一颤。"

    player "我不该擅自去找你爸。"

    player "我以为自己在帮你，但其实只是在满足自己的英雄主义。"

    narrator "很长的沉默。"

    lindao "（轻声）你知道就好。"

    narrator "她继续往前走了。"

    narrator "但走到楼梯拐角的时候——"

    lindao "（没有回头）……谢谢你没有追上来。"

    narrator "这句话比任何责骂都让我难受。"

    hide lindao with dissolve

    scene black

    narrator "{b}{color=#888888}距离告白还有6天{/color}{/b}"

    narrator "{b}{color=#888888}但我们之间，像是隔了一个世纪{/color}{/b}"

    $ persistent.lindao_day17_cold_war = True

    scene black

    call chapter_title("Day 17 End", "", 1.5)

    jump lindao_day18

label lindao_day18:
    $ persistent.current_day = 18

    scene black

    call chapter_title("转机", "Day 18", 1.5)

    scene black

    narrator "第四天。"

    narrator "冷战持续着。"

    narrator "我没有再试图去找她说话。"

    narrator "但我在做另一件事。"

    # 第二次尝试 — 换一个方法
    scene bg living_room with dissolve

    narrator "我去了林晚棠家。"

    narrator "不是去找她。"

    narrator "而是去找她妈妈。"

    player_thought "上次我只关注了林父的问题……"

    player_thought "但苏念卿说得对——关键不在于林父。"

    player_thought "而在于让林母有留下来的理由。"

    narrator "开门的是林晚棠。"

    show lindao surprised at LEFT with dissolve

    lindao "（惊讶）陆鸣？你怎么……"

    player "我不是来找你的。"

    lindao "（疑惑）那你是来……"

    player "我想跟你妈聊聊。"

    narrator "她的表情变得复杂起来。"

    show lindao worried at LEFT with dissolve

    lindao "你……还想管我们家的事？"

    player "（认真地看着她）晚棠，上一次是我太急了。"

    player "这次不一样。"

    narrator "她看了我很久。"

    lindao "……妈在厨房。你自己去说吧。"

    narrator "她让开了路。"

    narrator "没有阻止我。"

    # 和林母的对话 — 关键转折
    narrator "我在客厅等了大概十分钟。"

    narrator "林母从厨房出来，围裙还没摘。"

    lin_mom "听晚棠说你想找我？"

    narrator "她的语气客气但疏离。"

    player "阿姨好。我是晚棠的同学，叫陆鸣。"

    lin_mom "我知道你。晚棠提过你几次了。"

    player "阿姨，我知道您打算带晚棠去日本。"

    narrator "她的表情沉了下来。"

    lin_mom "是晚棠让你来的？"

    player "不是。是她不知道我来。"

    narrator "她坐了下来。"

    player "阿姨，我不谈晚棠爸的事。"

    player "那是你们大人的问题，我没资格插嘴。"

    lin_mom "那你来做什么？"

    player "我只是想告诉您一件事。"

    player "（深呼吸）晚棠不想走。"

    narrator "房间安静了几秒。"

    lin_mom "每个孩子都不想离开家。"

    player "这不是'不想离开家'。"

    player "她有舍不得的东西在这里。"

    player "有她养了很久的多肉植物，有她习惯走的上学路。"

    player "还有……她还没有跟喜欢的人好好说过话。"

    narrator "林母的眼神变了。"

    lin_mom "（轻声）……她跟你说的？"

    player "她什么都没跟我说。"

    player "但我看得出来。"

    player "阿姨，我不是来劝您改变主意的。"

    player "我只是想说——如果有一天您决定留下来……"

    player "不是因为日本的工作黄了，也不是因为签证出了问题。"

    player "而是因为您发现，其实这里也有值得留下的东西。"

    narrator "很长的沉默。"

    # 林母的反应
    lin_mom "（叹气）你这孩子……"

    lin_mom "你说得对。"

    narrator "我愣住了。"

    lin_mom "我确实是因为对他失望才想走的。"

    lin_mom "但如果他真的能改……"

    lin_mom "我也不是非要带着孩子跑到国外去。"

    player "阿姨。"

    lin_mom "（摇头）不过这些不是你能决定的。"

    lin_mom "要看他自己。"

    narrator "她站起身。"

    lin_mom "你回去吧。谢谢你愿意来说这些。"

    lin_mom "至少……让我重新想了一下。"

    $ persistent.lindao_day18_mom_talk = True
    $ persistent.lindao_affection += 5

    # 出门遇到林晚棠
    scene bg residential_street with dissolve

    narrator "走出楼道的时候。"

    narrator "林晚棠站在楼下。"

    narrator "像是在等我又不像是在等我。"

    show lindao shy at LEFT with dissolve

    lindao "你和我妈说了什么？"

    player "就是聊了聊天。"

    lindao "（低头）她很少会跟陌生人说这么多话的。"

    player "也许她只是需要一个理由留下来。"

    narrator "她沉默了一会儿。"

    show lindao normal at LEFT with dissolve

    lindao "（小声）陆鸣……"

    player "嗯？"

    lindao "（抬头看着我）谢谢你没有放弃。"

    narrator "她的眼眶有些红。"

    lindao "（快速低下头）但是！如果你再自作主张，我真的会生气的！"

    player "知道了。"

    narrator "她转身要上楼——"

    narrator "又回过头来。"

    lindao "明天见。"

    narrator "声音很小。"

    narrator "但足够让我笑出来了。"

    $ persistent.lindao_affection += 10
    $ persistent.lindao_relationship_iced = False
    $ persistent.lindao_day18_reconciled = True

    hide lindao with dissolve

    # 命运转折 — 更真实更艰难的成功
    call chapter_title("命运改变", "Day 18·傍晚", 1.5)

    # 学校后门小公园 - 命运转折
    scene bg park_corner with dissolve

    narrator "傍晚。"

    narrator "林晚棠发消息让我到学校后门的小公园。"

    narrator "看到她的瞬间我就知道——"

    narrator "有事发生了。"

    show lindao crying at LEFT with dissolve

    lindao "（跑过来）陆鸣！"

    narrator "她一把抱住了我。"

    narrator "我愣住了。"

    narrator "她在我怀里，声音断断续续。"

    lindao "我爸……他去自首了。"

    player "！"

    lindao "他说要重新开始。他去警局交代了一切。"

    narrator "她的眼泪落在我肩膀上。"

    lindao "还有……我妈决定再给他一次机会。"

    lindao "移民取消了……"

    narrator "我的大脑一片空白。"

    narrator "成功了。"

    narrator "真的成功了。"

    narrator "前世那个无能为力的遗憾——"

    narrator "这一世，被我改变了。"

    player_thought "……"

    player_thought "我做到了。"

    player_thought "这次，她的命运真的被改变了。"

    narrator "我伸出手，轻轻抱住她。"

    player "（轻声）太好了。"

    narrator "她在我怀里哭得更厉害了。"

    narrator "但这次，是喜悦的眼泪。"

    $ persistent.lindao_affection += 20
    $ persistent.lindao_day18_father_changed = True
    $ persistent.lindao_immigration_cancelled = True
    $ persistent.regret_value += 40
    $ persistent.butterfly_value = 100

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "不知道过了多久。"

    narrator "她终于从我怀里抬起头。"

    narrator "眼睛红红的，脸上全是泪痕。"

    narrator "但她在笑。"

    show lindao crying at LEFT with dissolve

    lindao "（擦眼泪）对不起……我失态了……"

    player "（微笑）没关系。"

    narrator "她不好意思地低下头。"

    show lindao smile at LEFT with dissolve

    lindao "陆鸣……谢谢你。"

    player "谢我什么？"

    lindao "谢谢你愿意帮我……"

    lindao "谢谢你那天去找我爸……"

    narrator "我愣了一下。"

    player "你怎么知道的？"

    lindao "（微笑）我爸告诉我的。"

    lindao "他说，那天有个叫陆鸣的男生来找过他。"

    lindao "是他这辈子见过的最好的小孩。"

    player "……"

    player_thought "原来他一直记得。"

    lindao "（看着我）陆鸣……你为什么对我这么好？"

    narrator "夕阳照在她脸上。"

    narrator "她的眼睛很亮，里面有泪光，也有光。"

    narrator "我想了很久。"

    narrator "然后，我开口了。"

    player "因为……"

    player "我不想再后悔了。"

    narrator "她愣了一下。"

    player "晚棠，有件事我一直想告诉你。"

    show lindao normal at LEFT with dissolve

    lindao "什么事？"

    player "（深吸一口气）等高考结束吧。"

    player "到时候，我会告诉你一切。"

    narrator "她没有追问。"

    narrator "只是轻轻点了点头。"

    show lindao smile at LEFT with dissolve

    lindao "好。我等你。"

    narrator "夕阳西下。"

    narrator "我们的影子在地上拉得很长。"

    narrator "这一刻，我感觉到——"

    narrator "命运的轨迹，真的被改变了。"

    hide lindao with dissolve

    scene black

    call chapter_title("Day 18 End", "", 1.5)

    jump lindao_day19

# =============================================================================
# Day 19-22：突破期
# =============================================================================

label lindao_day19:
    $ persistent.current_day = 19

    scene black

    call chapter_title("母亲的健康", "Day 19", 1.5)

    scene black

    narrator "移民风波平息后，我带妈妈去医院做了全面检查。"

    narrator "前世，她是三年后才发现病情。"

    narrator "这一次，我要提前预防。"

    # 医院走廊·白天
    scene bg hospital_corridor with dissolve

    narrator "医院。"

    narrator "我坐在走廊的椅子上，等待检查结果。"

    narrator "妈妈在旁边有些不耐烦。"

    mom "我身体好着呢，非要来医院浪费钱。"

    player "妈，就当是体检嘛。"

    narrator "她无奈地笑了笑。"

    mom "你这孩子，最近怎么老是大惊小怪的。"

    player "（微笑）因为想确认您身体好着呢。"

    narrator "她伸手摸了摸我的头。"

    mom "傻孩子。"

    scene black

    narrator "检查结果出来了。"

    narrator "一切正常。"

    narrator "我长舒一口气。"

    player_thought "还好……这次发现得早。"

    player_thought "妈妈，你不会有事的。"

    mom "（看着如释重负的我）你这孩子，怎么比我还紧张？"

    player "没什么，就是想确认一下您身体好着呢。"

    mom "（拍拍我脑袋）傻小子。"

    $ persistent.lindao_day19_mom_healthy = True
    $ persistent.regret_value += 20

    scene black

    call chapter_title("Day 19 End", "", 1.5)

    jump lindao_day20

label lindao_day20:
    $ persistent.current_day = 20

    scene black

    call chapter_title("告白准备", "Day 20", 1.5)

    scene black

    narrator "高考倒计时：12天。"

    narrator "我决定在高考前告白。"

    narrator "不能再拖了。"

    scene black

    narrator "放学后，我一个人来到天台。"

    narrator "拿出纸笔，开始写告白词。"

    player "（写）晚棠，我……"

    narrator "写了一半，觉得不对。"

    player "（撕掉）重来。"

    narrator "又写了一半。"

    narrator "还是不对。"

    player "（揉成团）"

    narrator "……"

    player_thought "前世我从来没告过白。"

    player_thought "现在要写了，反而不知道该说什么。"

    player "（深呼吸）冷静，冷静……"

    # ========== QTE告白准备 ==========
    menu lindao_day20_preparation_qte:
        "写一封情书":
            jump lindao_day20_prep_letter
        "准备一份礼物":
            jump lindao_day20_prep_gift
        "什么都不准备，真诚最重要":
            jump lindao_day20_prep_sincere

    label lindao_day20_prep_letter:
        narrator "我决定写一封情书。"

        narrator "情书是最传统的方式。"

        narrator "前世我在网上看过很多模板……"

        player_thought "但我不想用别人的模板。"

        narrator "我要写出自己的心声。"

        player "（深呼吸，开始写）"

        narrator "【晚棠，当你看到这封信的时候……】"

        narrator "……"

        narrator "一个小时后。"

        narrator "桌上散落着十几张废纸。"

        narrator "但最后一封，终于让我满意了。"

        $ persistent.lindao_day20_prepared = "letter"
        $ persistent.lindao_day20_letter_written = True

        narrator "{b}{color=#90EE90}准备好了告白信{/color}{/b}"

        jump lindao_day20_prep_continue

    label lindao_day20_prep_gift:
        narrator "我决定准备一份礼物。"

        player_thought "送什么好呢……"

        narrator "想起之前她说过喜欢多肉。"

        narrator "还有……她曾经提过想要一本绝版书。"

        menu lindao_day20_gift_choice:
            "去花店买一株精致的多肉":
                $ persistent.lindao_day20_gift = "succulent"
                narrator "我去了学校附近的花店。"

                narrator "挑了一株小巧精致的多肉，装在漂亮的盆里。"

                narrator "这让我想起当初救活她多肉的那天。"

            "去图书馆找那本绝版书":
                $ persistent.lindao_day20_gift = "book"
                narrator "我去了市里的图书馆。"

                narrator "花了大半天，终于找到了那本绝版书。"

                narrator "旧书散发着岁月的气息，和她很配。"

            "买一条简单的手链":
                $ persistent.lindao_day20_gift = "bracelet"
                narrator "我去了商场。"

                narrator "在饰品柜台看到一条简单精致的银手链。"

                narrator "不张扬，但很有质感——就像她一样。"

        $ persistent.lindao_day20_prepared = "gift"

        narrator "{b}{color=#90EE90}准备好了礼物{/color}{/b}"

        jump lindao_day20_prep_continue

    label lindao_day20_prep_sincere:
        narrator "我决定什么都不准备。"

        player_thought "不……有些东西不需要准备。"

        player_thought "真心就够了。"

        narrator "前世我就是因为想太多，才什么都没做。"

        narrator "这一世，我要用最真诚的方式——"

        narrator "直接告诉她。"

        $ persistent.lindao_day20_prepared = "sincere"
        $ persistent.lindao_day20_sincere_mode = True
        $ persistent.lindao_affection += 5

        jump lindao_day20_prep_continue

    label lindao_day20_prep_continue:
        pass

    scene bg classroom_day with dissolve

    narrator "正当我焦头烂额的时候——"

    narrator "身后传来脚步声。"

    show lindao surprised at LEFT with dissolve

    lindao "陆鸣？你在干什么？"

    narrator "我猛地回头。"

    narrator "林晚棠站在那里，手里拿着两瓶水。"

    narrator "她好奇地看向我脚边的纸团。"

    show lindao normal at LEFT with dissolve

    lindao "你在写什么啊？"

    player "（慌张地挡住）没、没什么！"

    narrator "她没听我的，绕过来看了一眼。"

    lindao "（看到纸上的字）……"

    narrator "她的脸瞬间红了。"

    narrator "我的心跳漏了一拍。"

    player_thought "完了，被看到了……"

    show lindao shy at LEFT with dissolve

    lindao "你、你、你……"

    player "（急忙解释）这是……草稿！草稿！"

    lindao "（脸红到耳根）你……"

    narrator "她把手里的水塞给我，转身就要走。"

    lindao "我先走了！"

    player "（叫住她）等一下！"

    narrator "她停下脚步，但没有回头。"

    player "晚棠。"

    show lindao shy at LEFT with dissolve

    lindao "……什么？"

    player "（深吸一口气）再等等。"

    player "到时候，我会好好告诉你的。"

    narrator "她沉默了一会儿。"

    show lindao shy at LEFT with dissolve

    lindao "……好。"

    narrator "然后快步离开了。"

    narrator "我站在原地，心跳如鼓。"

    narrator "手里的纸团被我攥得皱巴巴的。"

    $ persistent.lindao_affection += 8
    $ persistent.lindao_day20_confession_prepare = True

    hide lindao with dissolve

    scene black

    call chapter_title("Day 20 End", "", 1.5)

    jump lindao_day21

label lindao_day21:
    $ persistent.current_day = 21

    scene black

    call chapter_title("月下约定", "Day 21", 1.5)

    # 篮球场夜 - 告白前夜
    scene bg basketball_court with dissolve

    narrator "告白前夜。"

    narrator "我在篮球场边的长椅上坐着，看着天上的星星。"

    narrator "明天就是约定的时候了。"

    narrator "我在想该怎么开口。"

    player_thought "就说'我喜欢你'吗……太土了。"

    player_thought "还是含蓄一点……"

    player_thought "不对，她喜欢直接的……吧？"

    narrator "正当我纠结的时候——"

    narrator "身后传来脚步声。"

    show lindao surprised at LEFT with dissolve

    lindao "（小声）陆鸣？"

    narrator "我回过头。"

    player "晚棠？你怎么在这里？"

    hide lindao with dissolve
    show lindao normal at LEFT with dissolve

    lindao "（走过来）我……睡不着，出来走走。"

    narrator "她在我旁边坐下。"

    hide lindao with dissolve
    show lindao normal at LEFT with dissolve

    narrator "月光洒在她脸上，很柔和。"

    narrator "我们并肩坐着，谁也没有说话。"

    narrator "夜风吹过，带来初夏的味道。"

    narrator "她的发丝被风吹起，轻轻拂过我的肩膀。"

    scene black

    narrator "月亮很圆，星星很亮。"

    narrator "篮球场上空无一人，只有我们两个。"

    narrator "她突然开口。"

    show lindao worried at LEFT with dissolve

    lindao "陆鸣……"

    player "嗯？"

    hide lindao with dissolve
    show lindao worried at LEFT with dissolve

    lindao "你最近是不是有什么事瞒着我？"

    narrator "我愣了一下。"

    player "为什么这么问？"

    show lindao normal at LEFT with dissolve

    lindao "（看向远方）你最近怪怪的……"

    lindao "有时候看着我，会突然走神。"

    lindao "好像在想什么很远的事情。"

    player_thought "……"

    player_thought "她察觉到了。"

    player "晚棠……"

    narrator "她转过头，看着我。"

    show lindao shy at LEFT with dissolve

    player "（认真）明天，我会告诉你一切。"

    player "到时候……你就知道了。"

    narrator "她没有追问。"

    narrator "只是轻轻点了点头。"

    lindao "好。我等你。"

    narrator "月光下，她的眼睛很亮。"

    narrator "里面有期待，有信任，也有……别的什么。"

    scene black

    narrator "我们就这样坐着，看星星一颗一颗亮起来。"

    narrator "没有说话，但很舒服。"

    narrator "她的手放在长椅上，离我的手很近。"

    narrator "我没有动。"

    narrator "她也没有躲开。"

    narrator "夜风吹过，带来她身上淡淡的香味。"

    narrator "这一刻，时间仿佛静止了。"

    $ persistent.lindao_affection += 10

    scene black

    narrator "临走的时候，她突然停下脚步。"

    show lindao shy at LEFT with dissolve

    lindao "陆鸣。"

    player "嗯？"

    lindao "（回头）不管明天你要说什么……"

    narrator "她深吸一口气。"

    lindao "我都想听。"

    narrator "然后她转身，快步离开了。"

    narrator "月光下，我看着她的背影消失在夜色中。"

    narrator "嘴角不自觉地扬了起来。"

    player "……好。"

    hide lindao with dissolve

    scene black

    call chapter_title("告白前夜", "Day 21 End", 1.5)

    jump lindao_day23

# =============================================================================
# Day 23-25：告白成功与结局
# =============================================================================

label lindao_day23:
    $ persistent.current_day = 23

    scene black

    call chapter_title("告白", "Day 23", 1.5)

    scene black

    narrator "高考倒计时：9天。"

    narrator "放学后。"

    narrator "我约林晚棠去天台。"

    narrator "这次，不是为了躲清静。"

    narrator "是为了——"

    player_thought "告诉她一切。"

    # 天台 - 告白场景（夕阳版）
    scene bg rooftop_sunset with dissolve

    narrator "天台。"

    narrator "夕阳西下，把一切染成金色。"

    narrator "林晚棠已经在那里等着了。"

    narrator "她看到我，有些紧张地攥着衣角。"

    show lindao worried at LEFT with dissolve

    lindao "陆鸣……"

    player "晚棠。"

    narrator "我走过去，站在她面前。"

    narrator "夕阳照在她脸上，眼睛里有期待。"

    player "晚棠，我有话要对你说。"

    show lindao normal at LEFT with dissolve

    lindao "（点头）……我在听。"

    narrator "我深吸一口气。"

    # ========== 告白方式选择 ==========
    menu lindao_day23_confession_choice:
        "直接告白（勇敢型）":
            jump lindao_day23_confession_direct
        "含蓄表白（浪漫型）":
            jump lindao_day23_confession_romantic
        "用准备的礼物/信件表达心意":
            jump lindao_day23_confession_gift

    label lindao_day23_confession_direct:
        narrator "我决定直接说出来。"

        player "晚棠……我喜欢你。"

        narrator "话说出口的瞬间，世界仿佛安静了。"

        narrator "夕阳，晚风，远处的城市喧嚣——"

        narrator "一切都停了下来。"

        narrator "只剩下她的眼睛，和我的心跳声。"

        show lindao surprised at LEFT with dissolve

        player "不是最近才喜欢的。"

        player "是喜欢了很久。"

        player "久到……我自己都记不清是从什么时候开始的。"

        $ persistent.lindao_day23_confession_style = "direct"

        jump lindao_day23_confession_reaction

    label lindao_day23_confession_romantic:
        narrator "我决定换一种方式。"

        player "晚棠，你知道吗……"

        player "前世——"

        narrator "话说到一半，我停住了。"

        player_thought "不能告诉她重生的事……"

        player "……其实，我想问你一个问题。"

        narrator "她疑惑地看着我。"

        player "如果有一天，我突然对你很好很好……"

        player "不是因为突然，而是因为'一直'……"

        player "你会怎么想？"

        narrator "她沉默了一会儿。"

        show lindao shy at LEFT with dissolve

        lindao "……那我会很幸福。"

        narrator "我笑了。"

        player "那我现在告诉你——"

        player "晚棠，我喜欢你。"

        narrator "夕阳，晚风，远处的城市喧嚣——"

        narrator "一切都停了下来。"

        show lindao surprised at LEFT with dissolve

        player "不是最近才喜欢的。"

        player "是喜欢了很久。"

        player "久到……连我自己都忘了。"

        $ persistent.lindao_day23_confession_style = "romantic"
        $ persistent.lindao_affection += 5

        jump lindao_day23_confession_reaction

    label lindao_day23_confession_gift:
        narrator "我想起了之前准备的告白方式。"

        if persistent.lindao_day20_prepared == "letter":
            jump lindao_day23_confession_letter
        elif persistent.lindao_day20_prepared == "gift":
            jump lindao_day23_confession_present
        else:
            jump lindao_day23_confession_sincere

    label lindao_day23_confession_letter:
        narrator "我拿出那封写了很久的情书。"

        player "晚棠……这是我写给你的。"

        narrator "她愣了一下，接过信封。"

        narrator "夕阳下，她一个字一个字地读着。"

        narrator "我紧张地看着她。"

        narrator "她的眼睛渐渐红了。"

        show lindao crying at LEFT with dissolve

        lindao "（声音颤抖）这是……你写的？"

        player "（点头）嗯。"

        narrator "她把信贴在胸口。"

        lindao "……写得真好。"

        player "所以……"

        player "晚棠，我喜欢你。"

        $ persistent.lindao_day23_confession_style = "letter"
        $ persistent.lindao_affection += 8
        $ persistent.regret_value += 20

        call show_notification("记忆碎片解锁", "心意", "#FFD700")

        jump lindao_day23_confession_reaction

    label lindao_day23_confession_present:
        narrator "我拿出准备的礼物。"

        if persistent.lindao_day20_gift == "succulent":
            player "这是给你的……就像当初我救活的那株多肉一样。"

            narrator "她接过小巧精致的多肉盆栽。"

            narrator "夕阳照在透明的盆壁上，反射出温暖的光。"

            lindao "（惊讶）这株……好可爱……"

        elif persistent.lindao_day20_gift == "book":
            player "这是给你的……我记得你提过想要这本书。"

            narrator "她接过那本有些泛黄的绝版书。"

            narrator "眼睛一瞬间亮了。"

            lindao "（捂住嘴）这是……你怎么找到的？！"

        else:
            player "这是给你的……我看到它的时候，觉得很适合你。"

            narrator "她打开盒子，看到那条银手链。"

            narrator "夕阳下，手链闪着柔和的光。"

            lindao "（轻声）好漂亮……"

        show lindao shy at LEFT with dissolve

        lindao "谢谢你……陆鸣。"

        player "所以……晚棠，我喜欢你。"

        $ persistent.lindao_day23_confession_style = "gift"
        $ persistent.lindao_affection += 10
        $ persistent.regret_value += 15

        call show_notification("记忆碎片解锁", "心意", "#FFD700")

        jump lindao_day23_confession_reaction

    label lindao_day23_confession_sincere:
        narrator "我决定用最真诚的方式。"

        player "晚棠。"

        narrator "我看着她的眼睛。"

        player "其实我也不知道该怎么说……"

        player "但有些话，我憋了很久。"

        narrator "她静静地听着。"

        player "从第一次见到你的时候，我就觉得你很特别。"

        player "后来每天和你一起上学、放学……"

        player "我就知道，我喜欢你。"

        narrator "她的眼眶红了。"

        show lindao crying at LEFT with dissolve

        player "不是突然的喜欢，是一直的喜欢。"

        player "晚棠……我喜欢你。"

        $ persistent.lindao_day23_confession_style = "sincere"
        $ persistent.lindao_affection += 6

        jump lindao_day23_confession_reaction

    label lindao_day23_confession_reaction:
        narrator "她的眼眶红了。"

        show lindao crying at LEFT with dissolve

        lindao "（声音颤抖）你……"

        player "我知道这很突然。"

        player "我知道我们现在还在高三。"

        player "我知道我们有很多问题要面对。"

        player "但是——"

        narrator "我看着她的眼睛。"

        player "我不想再错过了。"

        player "这次，我不想给自己留下遗憾。"

        narrator "她低下头，肩膀微微颤抖。"

        narrator "我看到有泪水滴落在地上。"

        player "晚棠……？"

        narrator "她抬起头，泪眼婆娑地看着我。"

        hide lindao with dissolve
        show lindao crying at LEFT with dissolve

        lindao "（哽咽）你这个笨蛋……"

        player "……？"

        lindao "（用手背擦眼泪）你知道我等了多久吗……"

        player_thought "……"

        player_thought "她……等我？"

        show lindao crying at LEFT with dissolve

        lindao "（继续哭）我也喜欢你啊……"

        lindao "喜欢了好久好久……"

        narrator "我的大脑一片空白。"

        narrator "她……也喜欢我？"

        narrator "前世，我暗恋了她三年，什么都没说。"

        narrator "这一世——"

        narrator "原来，她也喜欢我。"

        narrator "我伸出手，把她拉进怀里。"

        player "（轻声）对不起……让你等了这么久。"

    narrator "她在我怀里哭得更厉害了。"

    narrator "但这次，是幸福的眼泪。"

    # 解锁记忆碎片10 - 星空下的约定
    $ persistent.fragment_count += 1
    $ persistent.fragments_collected.append("frag_010")

    call show_notification("记忆碎片", "星空下的约定", "#FFD700")
    narrator "{i}\"前世，我从未牵过她的手。\"{/i}"
    narrator "{i}\"这一世，星空下，我们终于在一起了。\"{/i}"

    $ persistent.lindao_affection = 100
    $ persistent.lindao_confession_success = True
    $ persistent.regret_value += 50

    hide lindao with dissolve

    # 时间流转：夕阳 → 星空
    scene bg rooftop_stars with dissolve

    narrator "夕阳完全沉入地平线。"

    narrator "天边的红色渐渐消退，取而代之的是深蓝色的夜幕。"

    narrator "星星一颗一颗亮起来。"

    narrator "我们并肩坐在天台上，手牵着手。"

    narrator "她靠在我肩膀上，眼睛红红的，但嘴角在笑。"

    show lindao smile at LEFT with dissolve

    lindao "（轻声）陆鸣……"

    player "嗯？"

    lindao "你说的是真的吗？"

    player "当然是真的。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）那你……从什么时候开始喜欢我的？"

    player_thought "这个问题……"

    player_thought "我怎么回答？说我前世就喜欢了三年？"

    player "（想了想）大概是……高一的时候吧。"

    show lindao surprised at LEFT with dissolve

    lindao "（惊讶）那么早？"

    player "嗯。第一次见到你的时候就觉得……"

    player "这个女生很特别。"

    show lindao shy at LEFT with dissolve

    lindao "（脸红）你骗人……那时候你都不怎么跟我说话……"

    player "（微笑）因为不敢。"

    lindao "不敢？"

    player "怕说了你会讨厌我。"

    lindao "（小声）笨蛋……"

    narrator "她把脸埋进我的肩膀。"

    narrator "我轻轻揽住她的腰。"

    narrator "星空下，我们就这样坐着。"

    narrator "像是世界上只剩下我们两个人。"

    show lindao smile at LEFT with dissolve

    scene black

    narrator "不知道过了多久。"

    narrator "她突然抬起头。"

    lindao "陆鸣。"

    player "嗯？"

    show lindao normal at LEFT with dissolve

    lindao "（认真地看着我）不管以后发生什么……"

    lindao "我都不会后悔今天。"

    narrator "她的眼睛很亮，里面有星光，也有我的倒影。"

    player "（微笑）我也是。"

    narrator "她笑了。"

    narrator "然后踮起脚尖——"

    show lindao shy at LEFT with dissolve

    narrator "轻轻在我脸颊上落下一个吻。"

    narrator "很快，像是蜻蜓点水。"

    narrator "然后她迅速低下头，脸红得像熟透的苹果。"

    lindao "（小声）这……这是定金。"

    player "……"

    narrator "我的脸也红了。"

    narrator "心跳漏了好几拍。"

    player "那……高考之后呢？"

    show lindao shy at LEFT with dissolve

    lindao "（抬起头）高考之后……"

    narrator "她看着我，眼睛里有光。"

    lindao "等你给我正式的答案。"

    narrator "我握紧她的手。"

    player "好。"

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "月亮升起来了。"

    narrator "我们一起看了很久的星星。"

    narrator "然后，一起回家。"

    narrator "路上，我们牵着手。"

    show lindao smile at LEFT with dissolve

    narrator "谁也没有说话。"

    narrator "但这沉默，比任何语言都更温暖。"

    hide lindao with dissolve

    # 【CG-01 星空告白】
    scene black with dissolve
    show cg_01_starry_sky_confession with dissolve
    pause 2.5
    hide cg_01_starry_sky_confession with dissolve

    call chapter_title("告白成功", "Day 23 End", 2.0)

    jump lindao_day25

# =============================================================================
# Day 24：结局判定与分支
# =============================================================================

label lindao_day24:
    $ persistent.current_day = 24

    scene black

    call chapter_title("命运的抉择", "Day 24", 1.5)

    # =================================================================
    # 结局类型判定
    # =================================================================

    # 判定顺序：BE → NE → HE → TE
    jump lindao_ending_judgment

label lindao_ending_judgment:
    # 判定1：告白是否成功
    if not persistent.lindao_confession_success:
        jump lindao_bad_ending_confession_failed
    # 判定2：是否打动林父
    elif not persistent.lindao_day16_father_impressed:
        jump lindao_normal_ending_family_issue
    # 判定3：是否触发移民取消蝴蝶效应
    elif persistent.butterfly_count < 3:
        jump lindao_normal_ending_butterfly
    # 判定4：记忆碎片收集是否足够
    elif persistent.fragment_count < 8:
        jump lindao_happy_ending
    # 判定5：遗憾值是否达标
    elif persistent.regret_value < 150:
        jump lindao_happy_ending
    # 判定6：True Ending条件检查
    elif persistent.te_routes_completed >= 2 and persistent.fragment_count >= 15:
        jump lindao_true_ending_unlock
    # 默认：Happy Ending
    else:
        jump lindao_happy_ending

# =============================================================================
# Bad Ending：告白失败
# =============================================================================

label lindao_bad_ending_confession_failed:
    $ persistent.lindao_ending_type = "BE"

    scene black

    narrator "那天晚上，我没有等到她。"

    narrator "林晚棠没有出现在天台。"

    narrator "我独自在那里坐了一整晚。"

    narrator "星星很亮，但我的心很冷。"

    scene bg classroom_sunset with dissolve

    narrator "第二天。"

    narrator "她没有看我。"

    narrator "我们之间的距离，仿佛比从前更远了。"

    show lindao worried at LEFT with dissolve

    narrator "我想问为什么。"

    narrator "但我不知道该怎么开口。"

    narrator "也许……这就是命运吧。"

    narrator "前世我没能说出口的话。"

    narrator "这一世，终于说了。"

    narrator "但结果……还是一样。"

    show lindao normal at LEFT with dissolve

    narrator "高考前一周。"

    narrator "林晚棠转学了。"

    narrator "移民手续提前办好了。"

    narrator "她甚至没有跟我说再见。"

    scene black

    narrator "我站在空荡荡的座位前。"

    narrator "她的东西已经全部搬走了。"

    narrator "只留下一张纸条。"

    narrator "\"[player_name]，谢谢你这段时间的陪伴。\""

    narrator "\"[player_name]，对不起。\""

    narrator "\"[player_name]，再见。\""

    narrator "就这么三行字。"

    narrator "连一个'朋友'的称呼都没有。"

    scene black

    narrator "高考结束了。"

    narrator "我考上了一所不好不差的大学。"

    narrator "林晚棠去了日本。"

    narrator "我们再也没有联系过。"

    narrator "这次重生——"

    narrator "好像什么都没改变。"

    narrator "不，改变了一点。"

    narrator "我终于知道——"

    narrator "有些事情，不是努力就能成功的。"

    narrator "有些人，注定会错过。"

    scene black

    call chapter_title("有些人，注定会错过", "林晚棠线 · Bad Ending", 2.5)

    scene black

    narrator "—— 结局回顾 ——"
    narrator "有些关键的选择，没能把握住"
    narrator "告白前准备不够充分"
    narrator "也没能打动她的父亲"
    narrator "命运的改变，还差一点点"

    narrator ""
    narrator "错过 —— 在最关键的时候，没能抓住机会"

    pause 2.0

    scene black

    narrator "感谢游玩林晚棠线。"

    narrator "如果你想重新挑战——"

    narrator "可以从Day 23重新开始。"

    jump lindao_route_ending_menu

# =============================================================================
# Normal Ending：家庭问题未解决
# =============================================================================

label lindao_normal_ending_family_issue:
    $ persistent.lindao_ending_type = "Normal"

    scene black

    narrator "告白成功了。"

    narrator "但问题才刚刚开始。"

    scene bg classroom_sunset with dissolve

    narrator "林父知道了我们的事。"

    narrator "他没有像之前那样激烈反对。"

    narrator "但也没有祝福。"

    narrator "只是沉默。"

    show lindao worried at LEFT with dissolve

    lindao "（担忧）陆鸣，我爸他……"

    player "（握紧她的手）没关系，我们会想办法的。"

    narrator "但我们都知道。"

    narrator "有些问题，不是有决心就能解决的。"

    narrator "林父的赌瘾还在。"

    narrator "家庭的裂痕还没有愈合。"

    scene black

    narrator "高考结束了。"

    narrator "我们都考得不错。"

    narrator "但林晚棠还是要去日本留学。"

    narrator "这次没有移民，但选择了留学。"

    narrator "她申请了一所日本大学的交换项目。"

    show lindao sad at LEFT with dissolve

    lindao "（不舍）陆鸣，我……"

    player "（微笑）没关系，我们可以异地。"

    narrator "但我们都知道。"

    narrator "异国恋……太难了。"

    scene black

    narrator "机场。"

    narrator "林晚棠抱着我哭。"

    show lindao crying at LEFT with dissolve

    lindao "（哽咽）对不起……我答应过你的……"

    player "（擦她的眼泪）不要道歉。"

    player "这是我们一起做的选择。"

    narrator "她点点头，但还是哭得很厉害。"

    narrator "飞机起飞了。"

    narrator "我站在机场，看着那架飞机消失在天际。"

    scene black

    narrator "后来。"

    narrator "我们的联系越来越少。"

    narrator "不是因为不爱了。"

    narrator "只是……太远了。"

    narrator "时差、距离、还有那些无法跨越的差异。"

    narrator "一年后，我们和平分手了。"

    narrator "没有争吵，没有背叛。"

    narrator "只是……走散了。"

    scene black

    call chapter_title("有些人注定只能陪你走一程", "林晚棠线 · Normal Ending", 2.5)

    scene black

    narrator "—— 结局回顾 ——"
    narrator "告白成功了，但根本问题没有解决"
    narrator "她父亲的态度依然没有改变"
    narrator "留学的阴影还在那里"
    narrator "有些东西，爱情也战胜不了"

    narrator ""
    narrator "走过 —— 你们曾经在一起过"
    narrator "异地 —— 跨越不了的距离"

    pause 2.0

    scene black

    narrator "感谢游玩林晚棠线。"

    narrator "如果想尝试更好的结局——"

    narrator "需要在Day 16说服林父时选择正确的策略。"

    jump lindao_route_ending_menu

# =============================================================================
# Normal Ending：蝴蝶效应不足
# =============================================================================

label lindao_normal_ending_butterfly:
    $ persistent.lindao_ending_type = "Normal"

    scene black

    narrator "告白成功了。"

    narrator "林父勉强接受了这个事实。"

    narrator "移民的问题暂时搁置。"

    narrator "高考结束了。"

    scene bg classroom_sunset with dissolve

    narrator "成绩出来了。"

    narrator "我们都考上了同一座城市的大学。"

    narrator "虽然不是最好的学校，但足以让我们在一起。"

    show lindao smile at LEFT with dissolve

    narrator "那个夏天。"

    narrator "是我们最快乐的时光。"

    narrator "没有考试的压力，没有移民的阴霾。"

    narrator "只有我们两个人。"

    narrator "和一份刚刚开始的爱情。"

    scene black

    narrator "但有时候。"

    narrator "我会想起前世的一些事情。"

    narrator "那些我没能改变的遗憾。"

    narrator "那些蝴蝶效应没能触及的角落。"

    narrator "母亲还是会生那场病。"

    narrator "虽然发现得早，但还是让我们担心了很久。"

    narrator "父亲还是会有一段时间的迷茫。"

    narrator "虽然后来走出来了，但那段日子很艰难。"

    narrator "我们改变了很多。"

    narrator "但不是全部。"

    scene black

    narrator "大学四年。"

    narrator "我们在一起，感情稳定。"

    narrator "毕业后，找到了还不错的工作。"

    narrator "没有大富大贵，但生活安稳。"

    narrator "偶尔会吵架，但很快就会和好。"

    narrator "这就是生活吧。"

    narrator "不是童话，但足够真实。"

    scene black

    call chapter_title("平凡的幸福，也是一种完美", "林晚棠线 · Normal Ending", 2.5)

    scene black

    narrator "—— 结局回顾 ——"
    narrator "告白成功了，生活也稳定下来"
    narrator "但有些遗憾，还是没能弥补"
    narrator "不是每一个转折都能改变"
    narrator "平凡的幸福，也是一种完美"

    narrator ""
    narrator "平凡 —— 不是每个人都需要轰轰烈烈"
    narrator "'在一起'—— 最重要的事"

    pause 2.0

    scene black

    narrator "感谢游玩林晚棠线。"

    narrator "如果你想体验更完整的改变——"

    narrator "可以在游戏中触发更多蝴蝶效应事件。"

    jump lindao_route_ending_menu

# =============================================================================
# Happy Ending（已有完整代码，这里做标记跳转）
# =============================================================================

label lindao_happy_ending:
    $ persistent.lindao_ending_type = "HE"
    $ persistent.lindao_route_completed = True
    $ persistent.te_routes_completed += 1

    # 更新遗憾值统计
    $ persistent.regret_value += 30

    # 标记完成
    $ renpy.save("lindao_ending_save")

    # 跳转到已有的Happy Ending代码
    jump lindao_day25

# =============================================================================
# True Ending 解锁
# =============================================================================

label lindao_true_ending_unlock:
    $ persistent.lindao_ending_type = "True"

    scene black

    call chapter_title("命运的重逢", "", 2.0)

    narrator "所有的选择，都在此刻交汇。"

    narrator "——这是属于你们的结局。"

    scene black

    narrator "你已经完成了至少2条女主线。"

    narrator "并且收集了15个以上的记忆碎片。"

    narrator "这意味着——"

    narrator "你理解了'重生'的真正含义。"

    narrator "不是简单地改变命运。"

    narrator "而是在每一次选择中，成为更好的自己。"

    pause 2.0

    narrator "True Ending将带给你一个完整的故事收尾。"

    narrator "所有女主的命运都会在这里交汇。"

    narrator "所有的遗憾都会得到最终的解答。"

    scene black

    narrator "继续吗？"

    menu lindao_true_ending_choice:
        "继续 True Ending 路线":
            jump lindao_true_ending_route
        "先保存，返回标题画面":
            jump lindao_save_and_return

label lindao_true_ending_route:
    $ persistent.lindao_route_completed = True
    $ persistent.te_routes_completed += 1
    $ persistent.true_ending_unlocked = True

    # 跳转到Day 25 True Ending版本
    jump lindao_day25_true_ending

label lindao_save_and_return:
    narrator "游戏已保存。"

    narrator "可以在标题画面读取'林晚棠线结局存档'继续。"

    jump lindao_route_ending_menu

# =============================================================================
# 林晚棠线 · True Ending Day 25
# =============================================================================

label lindao_day25_true_ending:
    $ persistent.current_day = 25

    scene black

    call chapter_title("命运的交汇", "Day 25 · True Ending", 2.0)

    scene black

    narrator "高考结束了。"

    narrator "走出考场的那一刻，我感觉整个人都轻松了。"

    narrator "不管结果如何——"

    narrator "这一次，我没有遗憾。"

    narrator "林父戒赌了，重新找了工作。"

    narrator "林母留了下来，一家人重新开始。"

    narrator "母亲的身体很健康。"

    narrator "而林晚棠——"

    narrator "她还在我身边。"

    scene bg classroom_sunset with dissolve

    narrator "校门口。"

    narrator "她站在那里等我。"

    narrator "阳光洒在她身上，像是镀了一层金边。"

    show lindao smile at LEFT with dissolve

    lindao "（跑过来）陆鸣！"

    player "（张开双臂）过来。"

    narrator "她扑进我怀里。"

    narrator "我紧紧抱住她。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）这里是学校门口……"

    player "（微笑）我知道。"

    narrator "我低下头，在她额头上轻轻一吻。"

    narrator "周围有同学起哄。"

    narrator "但我不在乎。"

    narrator "这一次，我什么都不在乎了。"

    narrator "只想和她在一起。"

    hide lindao with dissolve

    scene black

    narrator "成绩出来的那天。"

    narrator "我们都考得不错。"

    narrator "可以上同一所城市的大学。"

    narrator "林父这次是真正地接受了我们。"

    narrator "他甚至主动找我谈话。"

    show lindao normal at LEFT with dissolve

    lin_father "小伙子，好好对她。"

    player "（认真）我会的，叔叔。"

    narrator "林母在一旁笑着。"

    scene black

    narrator "那个夏天。"

    # 公园场景 - 约会（夕阳）
    scene bg park_sunset with dissolve

    narrator "夕阳下，我们走在公园的小路上。"

    narrator "她牵着气球，笑得很开心。"

    show lindao smile at LEFT with dissolve

    lindao "陆鸣，你说我们会一直在一起吗？"

    player "（握紧她的手）会的，一定会的。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）那你要说话算话哦。"

    narrator "晚风轻轻吹过，带来夏天的气息。"

    narrator "这一刻，我觉得自己是世界上最幸福的人。"

    hide lindao with dissolve

    scene black

    narrator "后来有一天。"

    # 咖啡馆场景 - 庆祝（夕阳）
    scene bg cafe_sunset with dissolve

    narrator "我们约在常去的那家咖啡馆。"

    narrator "这里有我们太多回忆。"

    narrator "我在这里向她告白过。"

    narrator "也在这里等过她很多次。"

    show lindao smile at LEFT with dissolve

    lindao "（放下咖啡杯）陆鸣，你在发什么呆？"

    player "（微笑）在想我们第一次在这里见面的场景。"

    show lindao shy at LEFT with dissolve

    lindao "那时候你还很害羞呢……"

    player "（笑）是啊，现在也是。"

    narrator "她笑了。"

    narrator "咖啡的香气，温暖的灯光，还有她的笑容。"

    narrator "一切都是刚刚好的样子。"

    hide lindao with dissolve

    scene black

    narrator "九月份。"

    narrator "大学开学的第一天。"

    narrator "我站在校门口，等她。"

    narrator "她穿着白裙子，从远处跑过来。"

    show lindao smile at LEFT with dissolve

    lindao "（扑进我怀里）等很久了吗？"

    player "（揉她的头发）没有，刚好。"

    narrator "阳光很暖，风很轻。"

    narrator "她的笑容，比阳光更耀眼。"

    player "走吧，去报到。"

    lindao "嗯！"

    narrator "我们牵着手，走进校园。"

    narrator "身后是十八岁的夏天。"

    narrator "面前是全新的人生。"

    narrator "这一次——"

    narrator "我没有错过。"

    narrator "而且，我拥有了最好的一切。"

    scene black

    call chapter_title("这次，我抓住了命运", "林晚棠线 · True Ending", 2.5)

    scene black

    narrator "—— True Ending 统计 ——"
    narrator "遗憾弥补值：[persistent.regret_value]/300"
    narrator "记忆碎片：[persistent.fragment_count]/20"
    narrator "命运改变次数：[persistent.butterfly_count]"

    narrator ""
    narrator "不错过 —— 完成林晚棠线"
    narrator "命运的轨迹 —— 你改变了未来"
    narrator "迟到了十七年的话 —— 终于说出口"
    narrator "完美 —— 达成 True Ending"

    pause 2.0

    scene black

    narrator "你已完成林晚棠线的True Ending。"

    narrator "感谢你陪伴陆鸣走完这段旅程。"

    narrator "他曾经是一个懦弱的人。"

    narrator "错过喜欢的人，错过重要的人，错过想要珍惜的时光。"

    narrator "但这一世——"

    narrator "他终于抓住了命运的咽喉。"

    narrator "成为了那个不会被命运打败的人。"

    jump lindao_route_ending_menu

# =============================================================================
# 结局菜单
# =============================================================================

label lindao_route_ending_menu:
    scene black

    call chapter_title("林晚棠线 · 结局菜单", "", 2.0)

    menu lindao_ending_menu_choice:
        "查看结局总结":
            jump lindao_ending_summary
        "读取存档（重新体验其他路线）":
            jump lindao_load_save
        "返回标题画面":
            jump lindao_return_to_title
        "结束游戏":
            jump lindao_exit_game

label lindao_ending_summary:
    scene black

    narrator "{i}—— 旅程总结 ——{/i}"

    if persistent.lindao_ending_type == "BE":
        narrator "结局类型：Bad Ending"
        narrator "告白失败，未能挽回林晚棠"
    elif persistent.lindao_ending_type == "Normal":
        narrator "结局类型：Normal Ending"
        narrator "告白成功，但未能解决所有问题"
    elif persistent.lindao_ending_type == "HE":
        narrator "结局类型：Happy Ending"
        narrator "达成幸福的结局"
    elif persistent.lindao_ending_type == "True":
        narrator "结局类型：True Ending"
        narrator "达成最完美的结局"

    narrator ""
    narrator "{i}—— 这一次的数据 ——{/i}"
    narrator "记忆碎片：[persistent.fragment_count]/20"
    narrator "遗憾弥补值：[persistent.regret_value]/300"
    narrator "蝴蝶效应：[persistent.butterfly_count]次"
    narrator "已攻略角色：林晚棠"

    if persistent.te_routes_completed >= 2:
        narrator ""
        narrator "{color=#FFD700}{i}—— 提示 ——{/i}{/color}"
        narrator "你已完成[persistent.te_routes_completed]条女主线"
        narrator "当完成2条以上女主线且收集足够记忆碎片时"
        narrator "可以解锁True Ending"

    pause 2.0

    jump lindao_route_ending_menu

label lindao_load_save:
    narrator "请在标题画面选择'读取存档'。"

    jump lindao_return_to_title

label lindao_return_to_title:
    scene black

    narrator "正在返回标题画面……"

    pause 1.0

    jump start

label lindao_exit_game:
    scene black

    centered "{b}感谢游玩{/b}"
    centered "{b}《重生·轻逆袭》{/b}"

    pause 2.0

    return

# =============================================================================
# Day 25：Happy Ending（原代码保留）
# =============================================================================

label lindao_day25:
    $ persistent.current_day = 25

    scene black

    call chapter_title("高考结束", "Day 25", 1.5)

    scene black

    narrator "高考结束了。"

    narrator "走出考场的那一刻，我感觉整个人都轻松了。"

    narrator "不管结果如何——"

    narrator "这一次，我没有遗憾。"

    scene black

    scene bg classroom_sunset with dissolve

    narrator "校门口。"

    narrator "林晚棠站在那里等我。"

    narrator "她看到我，眼睛一下子亮了。"

    show lindao smile at LEFT with dissolve

    lindao "（跑过来）陆鸣！"

    player "（微笑）考得怎么样？"

    show lindao smile at LEFT with dissolve

    lindao "（笑着）应该还行吧……你呢？"

    player "（牵起她的手）不管成绩怎样，我们先去庆祝。"

    narrator "她没有挣脱。"

    narrator "反而握紧了我的手。"

    show lindao smile at LEFT with dissolve

    lindao "好。"

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "学校后山。"

    narrator "这里是我们第一次告白的地方。"

    narrator "也是我们约定'高考后给正式答案'的地方。"

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "星空下。"

    narrator "我看着她的眼睛。"

    player "晚棠。"

    show lindao normal at LEFT with dissolve

    lindao "嗯？"

    player "高考结束了。"

    narrator "她点头，眼睛里满是期待。"

    player "我来兑现承诺了。"

    narrator "我深吸一口气。"

    player "林晚棠。"

    player "我喜欢你。"

    player "不是'想跟你做朋友'的那种喜欢。"

    player "是想跟你在一起、一辈子、不分开的那种喜欢。"

    show lindao crying at LEFT with dissolve

    narrator "她的眼眶红了。"

    player "你愿意……做我的女朋友吗？"

    narrator "星空下，她看着我。"

    narrator "眼泪落下来，但嘴角在笑。"

    show lindao smile at LEFT with dissolve

    lindao "（点头）我愿意。"

    narrator "她扑进我怀里。"

    narrator "我紧紧抱住她。"

    narrator "这一刻，星空、晚风、虫鸣——"

    narrator "一切都刚刚好。"

    narrator "前世那个没说出口的告白——"

    narrator "这一世，终于说出来了。"

    narrator "而且，她答应了。"

    $ persistent.lindao_happy_ending = True

    hide lindao with dissolve

    scene black

    narrator "高考成绩出来的那天。"

    narrator "我们都考得不错。"

    narrator "可以上同一所城市的大学。"

    narrator "林父戒赌了，重新找了工作。"

    narrator "林母留了下来，一家人重新开始。"

    narrator "妈妈的身体很健康，每天都在念叨'我儿子有女朋友了'。"

    narrator "林远虽然没当兵，但选择了自己喜欢的专业。"

    narrator "而我——"

    narrator "终于不再是那个'差不多先生'了。"

    scene black

    narrator "那个夏天。"

    # 公园场景 - 约会（夕阳）
    scene bg park_sunset with dissolve

    narrator "夕阳下，我们走在公园的小路上。"

    narrator "她牵着气球，笑得很开心。"

    show lindao smile at LEFT with dissolve

    lindao "陆鸣，你说我们会一直在一起吗？"

    player "（握紧她的手）会的，一定会的。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）那你要说话算话哦。"

    narrator "晚风轻轻吹过，带来夏天的气息。"

    narrator "这一刻，我觉得自己是世界上最幸福的人。"

    hide lindao with dissolve

    scene black

    narrator "后来有一天。"

    # 咖啡馆场景 - 庆祝（夕阳）
    scene bg cafe_sunset with dissolve

    narrator "我们约在常去的那家咖啡馆。"

    narrator "这里有我们太多回忆。"

    narrator "我在这里向她告白过。"

    narrator "也在这里等过她很多次。"

    show lindao smile at LEFT with dissolve

    lindao "（放下咖啡杯）陆鸣，你在发什么呆？"

    player "（微笑）在想我们第一次在这里见面的场景。"

    show lindao shy at LEFT with dissolve

    lindao "那时候你还很害羞呢……"

    player "（笑）是啊，现在也是。"

    narrator "她笑了。"

    narrator "咖啡的香气，温暖的灯光，还有她的笑容。"

    narrator "一切都是刚刚好的样子。"

    hide lindao with dissolve

    scene black

    narrator "九月份。"

    narrator "大学开学的第一天。"

    narrator "我站在校门口，等她。"

    narrator "她穿着白裙子，从远处跑过来。"

    lindao "（扑进我怀里）等很久了吗？"

    player "（揉她的头发）没有，刚好。"

    narrator "阳光很暖，风很轻。"

    narrator "她的笑容，比阳光更耀眼。"

    player "走吧，去报到。"

    lindao "嗯！"

    narrator "我们牵着手，走进校园。"

    narrator "身后是十八岁的夏天。"

    narrator "面前是全新的人生。"

    narrator "这一次——"

    narrator "我没有错过。"

    scene black

    call chapter_title("这次，我不想再错过", "林晚棠线 · Happy Ending", 2.5)

    scene black

    narrator "—— 旅程总结 ——"

    narrator "这一世，你没有再留下遗憾。"

    narrator "记忆碎片：12 / 20"

    narrator ""

    narrator "不错过 —— 完成林晚棠线"

    narrator "命运的轨迹 —— 你改变了彼此的未来"

    narrator "迟到了十七年的话 —— 终于说出口"

    pause 2.0

    scene black

    narrator "谢谢你陪陆鸣走完这段旅程。"

    narrator "他曾经是一个懦弱的人。"

    narrator "错过喜欢的人，错过重要的人，错过想要珍惜的时光。"

    narrator "但这一世——"

    narrator "他终于学会了勇敢。"

    narrator "学会了不再犹豫。"

    narrator "学会了珍惜眼前人。"

    scene black

    narrator "如果你还想体验其他女主的路线——"

    narrator "可以返回标题画面，选择'读取存档'。"

    narrator "重玩第一章，选择不同的路线。"

    narrator "每一条线，都有不同的故事。"

    narrator "每一个选择，都会改变命运。"

    scene black

    call chapter_title("THE END", "", 2.5)

    centered "{b}感谢游玩{/b}"

    pause 2.0

    return

# =============================================================================
# 林晚棠线结束
# =============================================================================
