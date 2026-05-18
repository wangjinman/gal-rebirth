# =============================================================================
# 02_lindao_route.rpy - 林晚棠线：这次，我不想再错过她
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

# =============================================================================
# 角色定义
# =============================================================================

define lindao = Character('林晚棠', color="#D4A574", what_color="#F5F5F5")
define lindao_thought = Character('陆鸣（内心）', color="#8ECAE6", what_color="#F5F5F5")

# =============================================================================
# Day 8：靠近期的开始
# =============================================================================

label lindao_day8:
    scene black

    centered "{b}—— 林晚棠线 ——{/b}"

    pause 1.5

    narrator "第一章结束后的第二天清晨。"

    narrator "我站在镜子前，看着十八岁的自己。"

    narrator "窗外的阳光很刺眼，和记忆中一模一样。"

    player_thought "这次，我不会犹豫了。"

    scene black

    centered "{b}—— Day 8 ——{/b}\n{w=0.5}靠近{w=0.5}"

    pause 1.0

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

    scene bg classroom_day with dissolve

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

    player_thought "她今天穿的是白色衬衫……"

    player_thought "前世我从来没注意过这种事。"

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

    narrator "她低头喝牛奶的样子，像只小仓鼠。"

    player_thought "我居然觉得有点可爱。"

    player_thought "前世我怎么没发现……"

    $ persistent.lindao_affection += 5

    narrator "这一幕被林远看到了。"

    narrator "「我靠，陆鸣你小子开窍了？」"

    player "……闭嘴。"

    narrator "林远在旁边挤眉弄眼。"

    narrator "林晚棠的脸红得更厉害了。"

    # 隐藏立绘
    hide lindao with dissolve

    scene black

    centered "{b}—— Day 8 End ——{/b}"

    pause 1.5

    jump lindao_day9

# =============================================================================
# Day 9：雨中送伞（小高潮1）
# =============================================================================

label lindao_day9:
    $ persistent.current_day = 9

    scene black

    centered "{b}—— Day 9 ——{/b}\n
{w=0.5}雨{w=0.5}"

    pause 1.0

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

    narrator "{b}{color=#FFD700}【记忆碎片 2/20 解锁】{/color}{/b}"
    narrator "{i}\"前世我也想过送她回家...但那天我退缩了。\"{/i}"

    pause 1.0

    scene bg street_rain with dissolve

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
    scene bg street_rain with dissolve

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
    centered "{b}{color=#FFD700}—— Day 9 End ——{/color}{/b}\n{w=0.5}小高潮1触发"

    # 根据选择类型显示不同反馈
    if persistent.lindao_day9_shared_umbrella:
        narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +18{/color}{/b}"
        narrator "{i}\"雨中一起撑伞……她的手好凉，但心是暖的。\"{/i}"
        narrator "{b}{color=#FFD700}遗憾弥补值 +15{/color}{/b}"
        narrator "{i}\"【记忆碎片 2/20 解锁】{/i}"
    elif persistent.lindao_day9_gentleman:
        narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +15{/color}{/b}"
        narrator "{i}\"他的肩膀很宽，靠着很有安全感……\"{/i}"
    elif persistent.lindao_day9_rational:
        narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +13{/color}{/b}"
        narrator "{i}\"明明是他把伞让给我……有点傻，但很温柔。\"{/i}"
    else:
        narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +10{/color}{/b}"

    pause 1.5

    jump lindao_day10

# =============================================================================
# Day 10：天台午餐
# =============================================================================

label lindao_day10:
    $ persistent.current_day = 10

    scene black

    centered "{b}—— Day 10 ——{/b}\n
{w=0.5}天台{w=0.5}"

    pause 1.0

    scene bg classroom_day with dissolve

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

    player "法医秦明，怎么了？"

    show lindao normal at LEFT with dissolve

    lindao "（皱眉）好重口味……"

    player "悬疑推理，有助于锻炼逻辑思维。"

    lindao "（想了想）那你能给我推荐一本吗？"

    player_thought "她主动找我聊天了。"

    player_thought "前世……从来没发生过这种事。"

    player "你想看什么类型的？"

    show lindao smile at LEFT with dissolve

    lindao "就……不那么吓人的，有意思的就行。"

    player "东野圭吾的《解忧杂货店》怎么样？"

    lindao "（眼睛亮了）好像听说过。"

    player "回头我把书借你。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）……谢谢。"

    narrator "她低头吃饭的样子，在阳光下显得格外温柔。"

    player_thought "她笑起来真好看。"

    player_thought "前世我怎么就没发现呢……"

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

    centered "{b}—— Day 10 End ——{/b}"

    pause 1.5

    jump lindao_day11

# =============================================================================
# Day 11：夕阳下的对话
# =============================================================================

label lindao_day11:
    $ persistent.current_day = 11

    scene black

    centered "{b}—— Day 11 ——{/b}\n
{w=0.5}夕阳{w=0.5}"

    pause 1.0

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

    narrator "这次的分别，没有遗憾。"

    hide lindao with dissolve

    scene black

    centered "{b}—— Day 11 End ——{/b}"

    pause 1.5

    jump lindao_day12

# =============================================================================
# Day 12：多肉植物的约定
# =============================================================================

label lindao_day12:
    $ persistent.current_day = 12

    scene black

    centered "{b}—— Day 12 ——{/b}\n
{w=0.5}多肉{w=0.5}"

    pause 1.0

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

    narrator "我站在林晚棠家门口，手里拿着《解忧杂货店》。"

    narrator "心跳有些快。"

    player_thought "前世我去过她家吗……好像没有。"

    player_thought "连她家长什么样都不知道。"

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

            narrator "{i}【发现：她的书架上有很多日本文学书籍】{/i}"

        "观察阳台的多肉植物":
            $ persistent.lindao_day12_observed_succulent = True

            narrator "阳台上有几盆多肉植物。"

            narrator "大部分都很精神……"

            narrator "但有一盆明显快枯萎了，叶子发黄发软。"

            player_thought "这盆……她应该很在意吧。"

            # 触发多肉约定前置
            $ persistent.lindao_succulent_hint = True

            narrator "{i}【发现：那盆快枯萎的多肉似乎对她很重要】{/i}"

        "看看墙上的全家福":
            $ persistent.lindao_day12_observed_photo = True

            narrator "墙上挂着一张全家福。"

            narrator "照片里是林晚棠小时候的样子。"

            narrator "旁边站着一个男人……是她父亲吧。"

            narrator "但照片上有一些划痕，像是被刻意刮过的。"

            player_thought "她和父亲的关系……"

            # 获得家庭背景信息
            $ persistent.lindao_family_background_hint = True

            narrator "{i}【发现：全家福上有被刮过的痕迹】{/i}"

        "静静坐着等她回来":
            $ persistent.lindao_day12_did_nothing = True

            narrator "我坐在沙发上，没有乱动。"

            narrator "这是她的家，我不该随便翻看。"

            narrator "……"

            narrator "厨房里传来水流声。"

            narrator "她很快就会出来。"

    # 继续剧情
    hide lindao with dissolve

    scene bg bedroom with dissolve

    narrator "她端着两杯水走出来。"

    narrator "看到我坐在沙发上，她的表情放松了一些。"

    narrator "但我注意到——"

    narrator "她的目光扫过我刚才'观察'的地方，似乎有一丝紧张。"

    show lindao normal at LEFT with dissolve

    lindao "久等了。"

    narrator "她把水递给我。"

    narrator "然后，走向阳台角落。"

    # 记忆碎片3触发（多肉观察后）
    if persistent.lindao_day12_observed_succulent:
        player_thought "她对那盆多肉……真的很在意。"

        player_thought "我记得前世……她也提过这件事。"

        narrator "一阵恍惚。"

        # 解锁记忆碎片3
        $ persistent.fragment_3 = True

        narrator "{b}{color=#FFD700}【记忆碎片 3/20 解锁】{/color}{/b}"
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

    centered "{b}—— Day 12 End ——{/b}"

    pause 1.5

    jump lindao_day13

# =============================================================================
# Day 13：移民风波（小高潮2）
# =============================================================================

label lindao_day13:
    $ persistent.current_day = 13

    scene black

    centered "{b}—— Day 13 ——{/b}\n
{w=0.5}图书馆{w=0.5}"

    pause 1.0

    scene bg classroom_day with dissolve

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

    narrator "{b}{color=#6B9FFF}♥ 林晚棠好感度 -10{/color}{/b}"

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

    narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +15{/color}{/b}"
    narrator "{i}\"解锁'说服林父'事件链（蝴蝶效应核心）\"{/i}"

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

    narrator "{b}{color=#FF6B6B}♥ 林晚棠好感度 +10{/color}{/b}"
    narrator "{i}\"解锁'说服林父'事件链（蝴蝶效应核心）\"{/i}"

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

    centered "{b}—— Day 13 End ——{/b}\n
{w=0.5}小高潮2触发"

    pause 1.5

    jump lindao_day14

# =============================================================================
# Day 14：多肉存活·承诺（小高潮3）
# =============================================================================

label lindao_day14:
    $ persistent.current_day = 14

    scene black

    centered "{b}—— Day 14 ——{/b}\n
{w=0.5}天台{w=0.5}"

    pause 1.0

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

    $ persistent.lindao_affection += 10
    $ persistent.lindao_day14_promise = True
    $ persistent.regret_value += 20

    hide lindao with dissolve

    scene black

    narrator "送她回家的路上，我们都没怎么说话。"

    narrator "但气氛很舒服。"

    narrator "像是两个人之间，已经有了某种默契。"

    scene black

    centered "{b}—— Day 14 End ——{/b}\n
{w=0.5}小高潮3触发\n
{w=0.5}承诺已许下"

    pause 1.5

    jump lindao_day15

# =============================================================================
# Day 15-16：寻找突破口
# =============================================================================

label lindao_day15:
    $ persistent.current_day = 15

    scene black

    centered "{b}—— Day 15 ——{/b}\n
{w=0.5}情报{w=0.5}"

    pause 1.0

    scene black

    narrator "为了林晚棠，我必须找到解决问题的办法。"

    narrator "前世……她爸爸好像戒赌了。"

    narrator "但我不记得具体是什么时候、怎么戒的。"

    narrator "我只知道结果。"

    narrator "这是重生者最大的优势，也是最大的限制。"

    scene black

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

    narrator "'让她妈妈有留下来的理由'……"

    narrator "前世的林晚棠家……"

    narrator "林父欠了很多赌债。"

    narrator "林母就是因为这个才想离开的。"

    player_thought "如果林父能戒赌……"

    player_thought "如果他能重新开始……"

    player_thought "林母就有留下来的理由了。"

    scene black

    centered "{b}—— Day 15 End ——{/b}"

    pause 1.5

    jump lindao_day16

label lindao_day16:
    $ persistent.current_day = 16

    scene black

    centered "{b}—— Day 16 ——{/b}\n
{w=0.5}父亲的真相{w=0.5}"

    pause 1.0

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

    player_thought "前世我只知道结果，不知道过程。"

    player_thought "原来是这样……"

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

    narrator "有人说在城南的棋牌室看到他。"

    narrator "我犹豫了很久。"

    narrator "去，还是不去？"

    player_thought "这不关我的事……"

    player_thought "但如果我不出手……"

    player_thought "她就会离开。"

    player_thought "这次，我不想再错过了。"

    scene black

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

    player "（直接）我知道您欠了很多钱。"

    narrator "他的脸色沉了下来。"

    lin_father "你……"

    player "我还知道，您太太要带晚棠去日本。"

    narrator "他没有说话。"

    player "我是来告诉您——如果您继续这样下去，晚棠就要走了。"

    player "以后您可能再也见不到她了。"

    narrator "他的身体微微一震。"

    player "我知道戒赌很难。"

    player "但您还有机会。"

    player "晚棠她……很需要父亲。"

    narrator "他沉默了很久。"

    narrator "然后，他低下了头。"

    lin_father "（声音沙哑）你一个小孩懂什么……"

    player "我不懂。"

    player "但我知道，如果您现在不改变，您会后悔一辈子。"

    narrator "他没有再说话。"

    narrator "我站起身，转身离开。"

    narrator "走到门口的时候——"

    lin_father "（叫住我）等一下。"

    narrator "我回过头。"

    lin_father "你……叫什么名字？"

    player "陆鸣。"

    lin_father "（沉默）……谢谢你。"

    scene black

    narrator "我不知道这次谈话有没有用。"

    narrator "但我做了我能做的事。"

    narrator "剩下的，就交给命运了。"

    narrator "这次，我不再后悔。"

    scene black

    centered "{b}—— Day 16 End ——{/b}"

    pause 1.5

    jump lindao_day17

# =============================================================================
# Day 17-18：蝴蝶效应（大高潮）
# =============================================================================

label lindao_day17:
    $ persistent.current_day = 17

    scene black

    centered "{b}—— Day 17 ——{/b}\n
{w=0.5}等待{w=0.5}"

    pause 1.0

    scene black

    narrator "三天过去了。"

    narrator "林父没有消息。"

    narrator "我不知道那天的谈话有没有用。"

    narrator "每天在学校看到林晚棠，她都在假装没事。"

    narrator "但我能感觉到她在担心。"

    player_thought "会不会失败了……"

    player_thought "蝴蝶效应……真的能改变命运吗？"

    scene black

    narrator "第三天。"

    narrator "林晚棠给我发消息。"

    narrator "'陆鸣，你在哪？'"

    narrator "'能出来一下吗？'"

    narrator "'有件事……我想当面告诉你。'"

    player_thought "……来了。"

    scene black

    centered "{b}—— Day 18 ——{/b}\n
{w=0.5}命运改变"

    pause 1.0

    scene bg classroom_sunset with dissolve

    narrator "学校后门的小公园。"

    narrator "林晚棠站在那里等我。"

    narrator "她的眼睛红红的，像是哭过。"

    narrator "但她的嘴角……在笑。"

    player "晚棠？"

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

    centered "{b}—— Day 18 End ——{/b}\n
{w=0.5}大高潮触发\n
{w=0.5}蝴蝶效应·MAX"

    pause 1.5

    jump lindao_day19

# =============================================================================
# Day 19-22：突破期
# =============================================================================

label lindao_day19:
    $ persistent.current_day = 19

    scene black

    centered "{b}—— Day 19 ——{/b}\n
{w=0.5}母亲的健康{w=0.5}"

    pause 1.0

    scene black

    narrator "移民风波平息后，我带妈妈去医院做了全面检查。"

    narrator "前世，她是三年后才发现病情。"

    narrator "这一次，我要提前预防。"

    scene black

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

    centered "{b}—— Day 19 End ——{/b}"

    pause 1.5

    jump lindao_day20

label lindao_day20:
    $ persistent.current_day = 20

    scene black

    centered "{b}—— Day 20 ——{/b}\n
{w=0.5}告白准备{w=0.5}"

    pause 1.0

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

    centered "{b}—— Day 20 End ——{/b}"

    pause 1.5

    jump lindao_day21

label lindao_day21:
    $ persistent.current_day = 21

    scene black

    centered "{b}—— Day 21 ——{/b}\n
{w=0.5}月下约定{w=0.5}"

    pause 1.0

    scene black

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

    show lindao normal at LEFT with dissolve

    lindao "（走过来）我……睡不着，出来走走。"

    narrator "她在我旁边坐下。"

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

    centered "{b}—— Day 21 End ——{/b}\n
{w=0.5}告白前夜"

    pause 1.5

    jump lindao_day23

# =============================================================================
# Day 23-25：告白成功与结局
# =============================================================================

label lindao_day23:
    $ persistent.current_day = 23

    scene black

    centered "{b}—— Day 23 ——{/b}\n
{w=0.5}告白"

    pause 1.0

    scene black

    narrator "高考倒计时：9天。"

    narrator "放学后。"

    narrator "我约林晚棠去天台。"

    narrator "这次，不是为了躲清静。"

    narrator "是为了——"

    player_thought "告诉她一切。"

    scene bg classroom_sunset with dissolve

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

    player "你可能觉得我很奇怪。"

    player "为什么突然对你好，为什么知道你家的事，为什么……"

    player "总是看着你发呆。"

    show lindao worried at LEFT with dissolve

    lindao "（小声）……"

    player "其实……我有些事一直没告诉你。"

    narrator "她没有说话，只是静静地看着我。"

    player "晚棠……我喜欢你。"

    narrator "话说出口的瞬间，世界仿佛安静了。"

    narrator "夕阳，晚风，远处的城市喧嚣——"

    narrator "一切都停了下来。"

    narrator "只剩下她的眼睛，和我的心跳声。"

    show lindao surprised at LEFT with dissolve

    player "不是最近才喜欢的。"

    player "是喜欢了很久。"

    player "久到……我自己都记不清是从什么时候开始的。"

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

    $ persistent.lindao_affection = 100
    $ persistent.lindao_confession_success = True
    $ persistent.regret_value += 50

    hide lindao with dissolve

    scene black

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

    scene black

    centered "{b}—— Day 23 End ——{/b}\n
{w=0.5}告白成功"

    pause 2.0

    jump lindao_day25

# =============================================================================
# Day 25：Happy Ending
# =============================================================================

label lindao_day25:
    $ persistent.current_day = 25

    scene black

    centered "{b}—— Day 25 ——{/b}\n
{w=0.5}高考结束"

    pause 1.0

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

    centered "{size=+8}{b}—— 林晚棠线 · Happy Ending ——{/b}{/size}\n
{w=0.5}这次，我不想再错过"

    pause 2.0

    scene black

    narrator "{b}【遗憾弥补值】{/b}"
    narrator "{font=simhei.ttf}{color=#FFD700}{u}198/200{/u}{/color}{/font}"

    narrator "{b}【记忆碎片】{/b}"
    narrator "{font=simhei.ttf}{color=#87CEEB}{u}12/20 解锁{/u}{/color}{/font}"

    narrator "{b}【成就解锁】{/b}"
    narrator "'不错过'—— 完成林晚棠线"

    narrator "'蝴蝶效应'—— 改变了命运的轨迹"

    narrator "'此生不换'—— 说出那句迟到了十七年的话"

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

    centered "{b}—— THE END ——{/b}"

    centered "{b}感谢游玩{/b}"

    pause 2.0

    return

# =============================================================================
# 林晚棠线结束
# =============================================================================
