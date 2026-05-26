# =============================================================================
# 00_prologue.rpy - 序章：死亡与重生
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

label prologue_part1:
    scene bg bedroom_late_night with fade

    call chapter_title("终焉", "序章·第一幕", 2.0)

    narrator "..."

    narrator "我是谁来着？"

    narrator "……陆鸣。陆鸣。"

    narrator "我叫陆鸣。"

    narrator "手机屏幕的光，在黑暗中刺痛眼睛。"

    narrator "加班到凌晨三点的第七天。"

    narrator "三十五岁的身体，好像真的撑不住了。"

    # CG-01: 生命终结时刻（情绪最高潮）
    show cg death_overtime with vpunch
    pause 2.0
    hide cg death_overtime

    narrator "胃部传来一阵剧烈的绞痛。"

    narrator "像是有什么东西在内部撕裂。"

    player "……哈……"

    narrator "手机从指间滑落。"

    narrator "屏幕碎裂的声音，像是某种终结的号角。"

    scene black

    player_thought "这种感觉……"

    player_thought "好像……要死了……"

    player_thought "不……还没……"

    call memory_fragment_death

    # 意识流过渡背景 + CG-02叠加
    scene bg consciousness_fading with dissolve
    # CG-02: 意识消散 - 沉入深海（抽象意识流过渡）
    show cg consciousness_fade with dissolve
    pause 2.5

    narrator "视野越来越暗。"

    narrator "就像……沉入深海。"

    player_thought "就这样……结束了吗……"

    player_thought "那些……没说出口的话……"

    player_thought "那些……没做到的事……"

    player_thought "……"

    narrator "意识，在这一刻，彻底消散。"

    hide cg consciousness_fade with fade
    scene black with fade
    pause 3.0

    jump prologue_part2

label memory_fragment_death:
    narrator "{i}—— 她的笑容 ——{/i}"

    narrator "她的笑容，干净得像夏天的风。"

    narrator "三年同桌，我却从未对她说一句——"

    narrator "「我喜欢你」。"

    narrator "后来听说她去了日本。"

    narrator "再后来，就再也没有后来了。"

    narrator "{i}—— 兄弟 ——{/i}"

    narrator "林远。我最好的兄弟。"

    narrator "因为一个误会，我们再也没有说过话。"

    narrator "整整十年。"

    narrator "直到他结婚的消息传来，我才知道——"

    narrator "那个误会，从未解开过。"

    narrator "{i}—— 最后的遗憾 ——{/i}"

    narrator "妈妈走的那天。"

    narrator "我甚至没能见到她最后一面。"

    narrator "我总说「以后还来得及」。"

    narrator "可是「以后」，是最不可靠的承诺。"

    narrator "我甚至没来得及，好好陪她。"

    call collect_fragment("frag_001", "死亡的记忆")

    return

label prologue_part2:
    scene black

    narrator "……"

    narrator "嗯……？"

    narrator "什么声音……"

    narrator "好吵……"

    player "再睡五分钟……"

    narrator "闹钟还在不知疲倦地叫着。"

    narrator "但我已经无暇顾及。"

    narrator "双手颤抖。"

    narrator "猛地坐起身，心跳剧烈加速。"

    # 坐起身来，看清房间 —— 卧室日景淡入
    scene bg bedroom with fade

    narrator "这是……"

    narrator "我的房间？"

    narrator "不对。"

    narrator "这是……高考前那个家？！"

    player "怎么可能……"

    narrator "环顾四周——"

    narrator "墙上的日历。"

    narrator "桌上的课本。"

    narrator "窗外的蝉鸣。"

    narrator "颤抖着拿起手机——"

    narrator "2024年5月8日。"

    narrator "高考倒计时：30天。"

    player "！！！！！！"

    player "……疼。"

    narrator "不是梦。"

    narrator "这一切，都是真的。"

    player_thought "我……重生了？"

    player_thought "回到了高考前一个月？"

    player_thought "回到了……十八岁？"

    scene black

    narrator "我坐在床边。"

    narrator "不知道过了多久。"

    narrator "也许是几秒。"

    narrator "也许是几分钟。"

    narrator "然后——"

    player "哈……哈哈哈哈……"

    narrator "我笑了。"

    narrator "笑着笑着，眼泪就流了下来。"

    player "回来了……"

    player "真的回来了……"

    player "这一次……"

    player "这一次，我不会再错过了。"

    narrator "三十五年的记忆。"

    narrator "三十五年的遗憾。"

    narrator "全都涌入脑海。"

    call prologue_memory_reconstruction

    # === 时空跳跃：死亡 → 重生 ===
    # 记忆碎片过渡特效（纯画面展示，无文字干扰）
    scene bg memory_fragment with dissolve
    window hide
    pause 2.5
    window show

    jump prologue_part3

label prologue_memory_reconstruction:
    narrator "{i}—— 重生 ——{/i}"

    narrator "你回到了2024年5月8日。"

    narrator "高考倒计时：30天。"

    pause 1.5

    call collect_fragment("frag_002", "重生觉醒")

    narrator "深吸一口气。"

    player_thought "好。冷静。"

    player_thought "整理一下我知道的事。"

    narrator "高考……是6月7日。"

    player_thought "前世我考了什么成绩来着……"

    call show_notification("记忆碎片", "高考的遗憾", "#FFD700")

    narrator "高考成绩：理科487分"

    narrator "志愿滑档，最终进入三本院校"

    player_thought "报志愿的时候太保守了……结果还是滑档。"

    player_thought "算了，大学的事之后再说。"

    player_thought "现在最重要的是——"

    narrator "林晚棠。"

    call show_notification("记忆碎片", "她要走了", "#FFD700")

    narrator "林晚棠将在高考后前往日本留学"

    narrator "此后十年，再未相见"

    player_thought "她毕业就要去日本了。"

    player_thought "三十天。只有三十天。"

    player_thought "这一次，我不能再错过。"

    player_thought "还有……"

    call show_notification("记忆碎片", "兄弟", "#FFD700")

    narrator "林远——你最好的兄弟"

    narrator "三年后将因误会决裂"

    player_thought "林远……"

    player_thought "这次，不能再让那个误会发生了。"

    call show_notification("记忆碎片", "最后的遗憾", "#FFD700")

    narrator "母亲将在你28岁时因病去世"

    player_thought "妈妈……"

    player_thought "还有六年的时间。"

    player_thought "这次，一定要多陪陪她。"

    player_thought "还有……"

    player_thought "等等，有些事情我想不起来了……"

    narrator "{i}—— 模糊的记忆 ——{/i}"

    narrator "你只能记住关键人生节点的结果"

    narrator "细节随着时间推移会逐渐模糊"

    narrator "原来重生有代价的。"

    narrator "细节性的东西，想不起来了。"

    player_thought "没关系。"

    player_thought "知道结果就够了。"

    player_thought "这次，我会让结果不一样。"

    return

label prologue_part3:
    # 重生后醒来 - 卧室日景
    scene bg bedroom with fade

    narrator "看向时钟——"

    narrator "七点十分。"

    narrator "再不走就迟到了。"

    narrator "虽然昨晚的加班仿佛还在眼前——"

    narrator "但那是十七年后的昨晚了。"

    narrator "得赶紧准备出门了。"

    # 家中玄关 - 出门前的早晨
    scene bg home_entrance with dissolve

    narrator "餐桌上，妈妈絮絮叨叨说着什么。"

    narrator "我有一搭没一搭地应着。"

    narrator "但心里却在想着别的事。"

    player_thought "今天去学校……"

    player_thought "林晚棠……就坐在我旁边。"

    player_thought "这次，该怎么做？"

    player "妈！我去上学了！"

    scene black

    call chapter_title("重生后的第一天", "第一章 · 熟悉的陌生", 2.0)

    jump prologue_part4

label prologue_part4:
    # 清晨高中校门 - 重生后第一天到校
    scene bg school_gate_morning with dissolve

    narrator "「滨海市第一中学」"

    narrator "熟悉的校门，熟悉的石狮子。"

    narrator "门口熙熙攘攘的学生，穿着熟悉的蓝色校服。"

    narrator "一切都和记忆中一样。"

    narrator "又不一样。"

    player_thought "十七年了……"

    player_thought "突然看到这么多年轻的脸庞。"

    player_thought "有种说不出的感觉。"

    scene bg classroom_day with dissolve

    narrator "深吸一口气。"

    player_thought "好。"

    player_thought "准备好了吗？"

    player_thought "……"

    player_thought "准备好了。"

    scene black

    call chapter_title("—— 第一章 · 熟悉的陌生 ——", "", 1.5)

    jump chapter1_day1
