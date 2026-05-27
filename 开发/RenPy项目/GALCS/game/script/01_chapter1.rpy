# =============================================================================
# 01_chapter1.rpy - 第一章：熟悉的陌生
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

label chapter1_day1:
    $ persistent.chapter1_day1_school = True
    $ persistent.current_day = 1

    scene black

    call chapter_title("Day 1", "", 1.5)

    scene bg classroom_day with dissolve

    narrator "早自习的铃声响起。"

    narrator "教室里响起稀稀拉拉的读书声。"

    narrator "我坐在座位上，假装看书。"

    narrator "实际上，视线一直飘向旁边。"

    narrator "林晚棠正认真地朗读着英语课文。"

    narrator "阳光从窗户斜照进来，在她发丝上镀了一层金边。"

    player_thought "十七年了……"

    player_thought "这个画面，我以为早就忘了。"

    player_thought "原来还记得这么清楚。"

    narrator "她似乎感受到了我的目光。"

    narrator "她抬起头，对我微微一笑。"

    narrator "那个笑容，和记忆中一模一样。"

    narrator "——和十七年后，那个日本街头匆匆而过的身影，重叠在一起。"

    narrator "「早上好，陆鸣。」"

    player_thought "……"

    player_thought "和十七年前一模一样。"

    player_thought "但是这一次——"

    player_thought "我不会让它只是「记忆」了。"

    $ persistent.lindao_affection += 2

    narrator "班主任李老师走进来。"

    narrator "「好了好了，都安静一下！」"

    narrator "李老师看向门口。"

    narrator "「我们班来了一位转学生。」"

    narrator "来了。"

    narrator "周芷晴。"

    scene bg classroom_day with dissolve

    narrator "她站在讲台上，笑得像个小太阳。"

    narrator "元气满满，和林晚棠完全是两个类型。"

    player_thought "前世……"

    player_thought "我和她几乎没什么交集。"

    player_thought "她是我妹妹的好朋友。"

    player_thought "但因为妹妹在外地上学，我们基本上没见过面。"

    narrator "周芷晴背着书包往后排走。"

    narrator "经过我身边时，她的目光扫过来——"

    narrator "她多看了我一眼。"

    narrator "然后继续往后走了。"

    narrator "只是一个小小的对视。"

    narrator "但我不知道的是——"

    narrator "这一点小小的注意，在未来会改变很多事。"

    $ persistent.zhou_affection += 2

    narrator "早自习继续。"

    narrator "我翻开了课本。"

    narrator "上面的笔记，陌生又熟悉。"

    narrator "是十八岁的我写的。"

    narrator "字迹潦草，内容杂乱。"

    player_thought "十七年没看过高中课本了……"

    player_thought "这些知识，我现在应该还能辅导高中生吧。"

    narrator "——正当我出神的时候，有人敲了敲我的桌子。"

    narrator "「陆鸣，老师叫你去办公室拿作业。」"

    narrator "陈墨。"

    narrator "我们班的班长，也是年级第一。"

    narrator "冷傲，完美主义，是所有人眼中「别人家的孩子」。"

    narrator "前世，我们几乎没有交集。"

    narrator "但我知道她——"

    narrator "完美主义的外表下，藏着巨大的压力。"

    player "啊……好的，谢谢。"

    narrator "她转身离开。"

    narrator "马尾辫轻轻晃动。"

    $ persistent.chen_affection += 1

    narrator "这只是一个小插曲。"

    narrator "我没有多想。"

    scene black

    narrator "去办公室的路上。"

    narrator "路过窗户，可以看到操场。"

    narrator "有班级在上体育课。"

    narrator "青春的喧嚣声，从窗外传进来。"

    narrator "突然有些恍惚。"

    player_thought "这是真的。"

    player_thought "我真的回来了。"

    menu:
        "顺便去洗手间整理一下思绪":
            jump chapter1_day1_restroom
        "直接去办公室":
            jump chapter1_day1_office

label chapter1_day1_restroom:
    scene black

    narrator "我站在洗手间的镜子前。"

    narrator "看着镜子里那张年轻的脸。"

    player_thought "十八岁……"

    player_thought "皮肤真好。"

    player_thought "头发也没秃。"

    player_thought "肚子也没中年人的啤酒肚。"

    narrator "苦笑。"

    player_thought "重生回来的第一件事，居然是在意自己的颜值。"

    player_thought "果然是个俗人。"

    narrator "但笑着笑着，又有些感慨。"

    player_thought "年轻真好。"

    player_thought "三十天。高考前最后的三十天。"

    jump chapter1_day1_office

label chapter1_day1_office:
    scene black

    narrator "我沿着走廊往办公室走。"

    narrator "——正当我发呆的时候。"

    narrator "撞到了一个人。"

    narrator "是个女人。"

    narrator "二十多岁的样子，穿着咖啡色的长裙。"

    narrator "——等等。"

    narrator "这个身影……"

    player_thought "苏念卿？！"

    narrator "她不是住在我们家隔壁吗？"

    narrator "前世，她是我为数不多的朋友。"

    narrator "咖啡馆的老板，总是在深夜阳台上喝酒看星星。"

    narrator "但现在……"

    narrator "她怎么会出现在学校里？"

    narrator "「没事没事，是我走路不看路。」"

    narrator "她的笑容很温柔。"

    narrator "但眼神里有一丝我看不懂的东西。"

    narrator "「我是苏念卿，是来学校办事的。」"

    narrator "「你叫什么名字？」"

    player "我……我叫陆鸣。"

    narrator "她重复了一遍我的名字。"

    narrator "像是在记住什么。"

    narrator "「好名字。」"

    narrator "「那，陆鸣同学，去忙你的吧。」"

    narrator "「小心别再撞到人了哦。」"

    player "……好。"

    narrator "我看着她的背影消失在走廊尽头。"

    narrator "心里有一丝奇怪的预感。"

    player_thought "苏念卿……她对我很好。但我也仅此而已。"

    player_thought "这次……"

    $ persistent.suni_affection += 3
    $ persistent.chapter1_met_suni = True

    scene bg classroom_sunset with dissolve

    narrator "一天的时间，过得很快。"

    narrator "或者说，太快了。"

    narrator "像是怕这一切只是一场梦。"

    narrator "放学铃响起。"

    narrator "林晚棠收拾好书包。"

    narrator "「陆鸣，你今天……」"

    narrator "她欲言又止。"

    player "怎么了？"

    narrator "「没什么……就是觉得你今天有点奇怪。」"

    player "……奇怪？"

    narrator "「嗯……感觉你一直看着我。」"

    narrator "我心里一惊。"

    player_thought "被发现了？！"

    narrator "「不过……」"

    narrator "她微微一笑。"

    narrator "「也没什么啦。」"

    narrator "「可能是高考太紧张了吧。」"

    narrator "「早点回家休息哦。」"

    narrator "她收拾好书包，站起身。"

    $ persistent.lindao_affection += 3
    $ persistent.chapter1_day1_lindao_curious = True

    narrator "我也站起身。"

    narrator "林远在旁边等着我。"

    narrator "「陆鸣！走啦！打篮球去！」"

    player "来了。"

    narrator "我看了林晚棠一眼。"

    narrator "她也正好回头。"

    narrator "四目相对。"

    narrator "然后她微微一笑，转身离开了。"

    narrator "重生后的第一天，就这样过去了。"

    scene black

    call chapter_title("Day 1 End", "", 1.5)

    jump chapter1_day2

label chapter1_day2:
    $ persistent.current_day = 2

    scene black

    call chapter_title("Day 2", "", 1.5)

    pause 1.0

    scene black

    narrator "第二天。"

    narrator "闹钟响起的时候，我已经醒了。"

    narrator "或者说，根本没怎么睡着。"

    player_thought "重生后的第二天……"

    player_thought "还是会觉得不真实。"

    narrator "但该做的事，还是得做。"

    player "妈，我去上学了。"

    scene black

    narrator "走在路上，我开始思考。"

    player_thought "每天浑浑噩噩，不知道自己想要什么。这次必须不一样。"

    player_thought "我有一个月的时间。"

    player_thought "改变命运。"

    menu:
        "主动找林晚棠说话":
            jump chapter1_day2_lindao
        "先观察一下情况":
            jump chapter1_day2_observe

label chapter1_day2_lindao:
    scene bg classroom_day with dissolve

    narrator "一进教室，我就看到林晚棠已经在座位上了。"

    narrator "她正低头看着什么。"

    narrator "走近一看——是一本日本留学的资料。"

    player_thought "……"

    player_thought "她已经在看这个了。"

    player_thought "前世我也见过这本资料。"

    player_thought "但那时候，我只是默默看着，什么都没说。"

    narrator "深吸一口气。"

    player "早上好。"

    narrator "她抬起头。"

    narrator "「啊，陆鸣，早上好。」"

    narrator "「今天来得比我还早呢。」"

    player "嗯……那个……"

    narrator "我在她旁边的座位坐下。"

    player "你在看什么？"

    narrator "明知故问。"

    narrator "她犹豫了一下。"

    narrator "「啊，这个……」"

    narrator "「没什么，就是一些……资料。」"

    narrator "但我看到了封面上的字——"

    narrator "「日本语能力试验N2」"

    player "你想去日本留学？"

    narrator "她的身体微微一僵。"

    narrator "「……你怎么知道？」"

    player "资料上写着呢。"

    narrator "她沉默了一会儿。"

    narrator "「嗯……是有这个打算。」"

    narrator "「我爸爸在日本工作。」"

    narrator "「妈妈想让我过去，一家人团聚。」"

    narrator "前世我也听说过这件事。"

    narrator "但当时只是当成普通的消息听过。"

    narrator "从来没想过要挽留什么。"

    player "……那你很想去吗？"

    narrator "她犹豫了。"

    narrator "那一刻，我看到了她眼底的迷茫。"

    narrator "「我……」"

    narrator "「我也不知道。」"

    narrator "「妈妈说去日本好，可是……」"

    narrator "「这里也有我舍不得的东西。」"

    player_thought "舍不得的东西……"

    player_thought "是什么呢？"

    narrator "我没有问出口。"

    narrator "但我记住了她此刻的表情。"

    $ persistent.lindao_affection += 5
    $ persistent.chapter1_day2_immigration_topic = True

    narrator "上课铃响了。"

    narrator "她收回目光，重新翻开课本。"

    narrator "「上课了，先不聊了。」"

    player "嗯。"

    narrator "但我知道——"

    narrator "有些东西，已经开始不一样了。"

    jump chapter1_day2_continue

label chapter1_day2_observe:
    scene bg classroom_day with dissolve

    narrator "我没有急着行动。"

    narrator "观察。"

    narrator "这是重生者最大的优势。"

    narrator "我知道未来会发生什么。"

    narrator "至少知道大方向。"

    narrator "只需要找到切入点。"

    player_thought "林晚棠……"

    player_thought "这次，得找一个契机。一个不会太突兀的方式。"

    narrator "一上午过去了。"

    narrator "我没有找到合适的机会。"

    narrator "但我注意到了另一件事——"

    narrator "周芷晴在教室里走来走去，和各种人聊天。"

    narrator "她似乎很快就融入了新环境。"

    narrator "和林晚棠完全是两个类型。"

    narrator "一个像向日葵，一个像栀子花。"

    player_thought "前世……"

    player_thought "我好像在高考前都没和她说过几句话。"

    player_thought "这次，是不是可以改变一下？"

    narrator "但现在还不是时候。"

    narrator "先处理最重要的事。"

label chapter1_day2_continue:
    scene black

    narrator "午休时间。"

    narrator "我和林远坐在操场的台阶上。"

    narrator "「你最近怎么了？感觉魂不守舍的。」"

    player "没什么，就是……在想一些事。"

    narrator "「什么事？高考的事？」"

    player "……算是吧。"

    narrator "「别想太多啦，你成绩又不差。」"

    narrator "「考个一本没问题。」"

    narrator "我没有说话。"

    narrator "林远不知道的是——"

    narrator "六年后，我们会因为一个误会决裂。"

    narrator "整整十年没有联系。"

    player_thought "这次不一样了。"

    player_thought "林远，你是我最好的兄弟。"

    player_thought "我不会让那个误会发生的。"

    $ persistent.bro_friendship = (persistent.bro_friendship or 0) + 5

    scene black

    call chapter_title("Day 2 End", "", 1.5)

    jump chapter1_day3

label chapter1_day3:
    $ persistent.current_day = 3

    scene black

    call chapter_title("模拟考", "Day 3", 1.5)

    scene bg classroom_day with dissolve

    narrator "第三天。"

    narrator "高考倒计时：27天。"

    narrator "早自习还没开始，教室里已经弥漫着一股紧张的气息。"

    narrator "——因为今天要发模拟考成绩。"

    player_thought "这次模考我必须考好。重生者总得有点优势吧。"

    # 模拟考成绩发布场景 — 先用旁白铺垫群像

    narrator "李老师抱着一摞试卷走进教室。"

    narrator "「这次考试，整体情况不太理想。」"

    narrator "「但我们班有两位同学进了年级前十。」"

    narrator "全班安静下来。"

    narrator "「第一名，陈墨，692分。第二名，周芷晴，685分。」"

    $ persistent.chen_affection += 1
    $ persistent.zhou_affection += 1

    # 周芷晴的反应 — 展示她"元气"表象下的一面
    narrator "周芷晴从后排跳起来，挥了拳头。"

    narrator "「耶！谢谢老师！」"

    narrator "她笑得像刚中了彩票。"

    narrator "周围的同学都在鼓掌。"

    player_thought "转学才两天就考了年级第二……"

    player_thought "这个人不简单。"

    # 陈墨的反应 — 完美主义者的"不够好"
    narrator "而陈墨面无表情地接过试卷。"

    narrator "坐回座位后，我瞥了一眼——"

    narrator "她在最后一道大题旁边用红笔写了三个字：'再算一遍'。"

    narrator "692分。年级第一。"

    narrator "她的表情像是不及格一样。"

    player_thought "……这就是'别人家的孩子'吗？"

    # 林晚棠的成绩 — 引入她的学业压力
    narrator "「林晚棠，581分。」"

    narrator "「比上次有进步，继续保持。」"

    show lindao shy at LEFT_CENTER with dissolve

    narrator "林晚棠接过试卷，低声说了一句'谢谢老师'。"

    narrator "但我注意到——她把试卷折了起来。"

    narrator "没有像其他人那样互相比分。"

    player_thought "581分……在她那个层次算中等偏上吧。"

    player_thought "但她好像不太在意分数的样子。"

    hide lindao with dissolve

    scene bg corridor with dissolve

    narrator "课间休息。"

    narrator "我在走廊上遇到了周芷晴。"

    narrator "她正靠在窗边喝酸奶。"

    zhou "（看到我）嗨！你是……陆鸣对吧？"

    player "嗯。恭喜你考第二。"

    zhou "（摆手）哎呀运气啦运气啦！"

    narrator "她笑得太自然了，自然到让人觉得她在表演。"

    zhou "不过说真的，你那天一直盯着林晚棠看诶——"

    narrator "她突然凑近了一点，压低声音。"

    zhou "（小声）你喜欢她？"

    player "（被噎住）啊？！没有！"

    zhou "（眨眼）放心啦，我不会说的~"

    narrator "她转身离开的时候，回头看了我一眼。"

    narrator "不是好奇的眼神。"

    narrator "更像是——在确认什么。"

    $ persistent.zhou_affection += 3
    $ persistent.chapter1_day3_zhou_noticed = True

    scene black

    call chapter_title("Day 3 End", "", 1.5)

    jump chapter1_day4

label chapter1_day4:
    $ persistent.current_day = 4

    scene black

    call chapter_title("裂缝", "Day 4", 1.5)

    scene bg corridor with dissolve

    narrator "第四天。"

    narrator "中午去食堂的路上。"

    narrator "我听到了一阵不大不小的骚动。"

    # 陈墨的完美主义裂缝
    narrator "走廊拐角处，陈墨正站在一个男生面前。"

    narrator "那个男生手里拿着一张皱巴巴的班级卫生检查表。"

    chen "（声音不大但很冷）我说过很多次，检查表要平整地交上来。"

    narrator "那个男生涨红了脸。"

    male_student_1 "不就是张纸吗……差不多就行了啊……"

    chen "'差不多'？"

    narrator "陈墨的声音依然平静，但那种平静让人害怕。"

    chen "如果每个人都觉得'差不多就行'，那我们班的量化考核永远拿不到优秀。"

    chen "你知不知道因为这张表被扣了0.5分，我们和二班就拉开了差距？"

    narrator "周围的空气凝固了。"

    narrator "没有人敢出声。"

    player_thought "这已经不是认真了……"

    player_thought "这是在逼自己，也在逼所有人。"

    # 主角的介入 — 展示"和前世不一样"
    narrator "陈墨转身要走——"

    narrator "她的目光扫过我。"

    narrator "那一瞬间，我看到了她眼底的一丝疲惫。"

    player "（鬼使神差地）陈墨。"

    narrator "她停下脚步，回头看我。"

    chen "什么事？"

    player "那张表……如果用熨斗烫一下，应该能恢复平整。"

    narrator "她愣了一下。"

    chen "……熨斗？"

    player "办公室里有。以前李老师教过我们这个方法。"

    narrator "沉默了两秒。"

    chen "（语气稍微缓和）……我知道了。"

    narrator "她没说谢谢，也没道歉。"

    narrator "只是拿着那张表往办公室走去。"

    narrator "经过我身边时，脚步顿了一下。"

    narrator "很轻。如果不是刻意注意根本不会发现。"

    $ persistent.chen_affection += 3
    $ persistent.chapter1_day4_chen_crack = True

    # 林晚棠的小细节 — 她注意到了主角的行为
    scene bg classroom_day with dissolve

    narrator "回到教室后。"

    narrator "林晚棠正在整理桌上的书本。"

    show lindao normal at LEFT_CENTER with dissolve

    lindao "刚才……你在帮陈墨解围？"

    player "不算解围吧，就是提了个建议。"

    show lindao smile at LEFT_CENTER with dissolve

    lindao "（轻声）你好像和前几天不太一样了。"

    player "哪里不一样？"

    lindao "（想了想）……说不上来。"

    narrator "她低下头继续整理书。"

    narrator "嘴角却微微弯了弯。"

    $ persistent.lindao_affection += 2

    hide lindao with dissolve

    scene black

    call chapter_title("Day 4 End", "", 1.5)

    jump chapter1_day5

label chapter1_day5:
    $ persistent.current_day = 5

    scene black

    call chapter_title("咖啡馆", "Day 5", 1.5)

    scene bg school_gate_dusk with dissolve

    narrator "第五天。"

    narrator "放学后，我没有直接回家。"

    narrator "苏念卿的咖啡馆就在学校附近。"

    narrator "'晚星咖啡'——前世我经常来这里。"

    narrator "但那时候是三十多岁的大叔来借酒消愁的。"

    player_thought "现在我是十八岁的高中生……"

    player_thought "以这个身份走进去，会是什么感觉？"

    # 苏念卿的神秘感场景
    scene bg cafe_bar with dissolve

    narrator "推开门，风铃响了。"

    narrator "店里没什么人。"

    narrator "苏念卿坐在角落的位置，面前放着一杯已经凉了的黑咖啡。"

    narrator "她看着窗外，不知道在想什么。"

    suni "（没有回头）欢迎光临~要喝点什么？"

    player "……一杯柠檬水就好。"

    narrator "她回过头。"

    narrator "看到是我之后，表情有一丝微妙的变化。"

    suni "（微笑）是你啊，陆鸣同学。"

    suni "放学后来咖啡馆……你家长知道吗？"

    player "我都十八了。"

    suni "（笑）十八岁也是未成年人哦。"

    narrator "她起身去调饮料。"

    narrator "我注意到她走路时有些迟疑——像是左脚不太舒服。"

    player_thought "她脚受伤了吗？前世从来没注意到这件事……"

    narrator "她端着柠檬水过来。"

    suni "（放下杯子）五块钱。"

    narrator "我刚要掏钱——"

    suni "算了，请你的。"

    narrator "她在我对面坐下。"

    suni "（看着窗外）你最近……过得还好吗？"

    player "还好吧。就是高考有点压力。"

    suni "（轻笑）压力好啊。"

    suni "有压力说明你还活着，还有想要的东西。"

    player_thought "这句话……听起来不像是随口说的。"

    player "念卿姐，你呢？最近怎么样？"

    narrator "她的笑容停顿了一瞬。"

    narrator "很短，短到可能只有0.1秒。"

    suni "我？老样子呗。"

    suni "开店，冲咖啡，看人进进出出。"

    suni "（站起身）柠檬水喝完了就早点回去。"

    suni "别让你妈妈等急了。"

    narrator "她走回吧台后面。"

    narrator "背影看起来比那天在学校里更单薄了一些。"

    player_thought "苏念卿……她看起来好像过得不太好。"

    $ persistent.suni_affection += 3
    $ persistent.chapter1_day5_cafe_talk = True

    scene black

    call chapter_title("Day 5 End", "", 1.5)

    jump chapter1_day6

label chapter1_day6:
    $ persistent.current_day = 6

    scene black

    call chapter_title("群体", "Day 6", 1.5)

    scene bg classroom_day with dissolve

    narrator "第六天。"

    narrator "周五下午最后一节课是班会。"

    narrator "李老师说下周要重新排座位。"

    narrator "教室里顿时炸开了锅。"

    narrator "「我不想换！」「我想坐窗边！」「能不能和XXX同桌？」"

    # 群像场景 — 展示班级生态
    narrator "在一片嘈杂中，我注意到了几个画面。"

    narrator "周芷晴已经被三四个人围着了——有人想和她同桌，有人问她题。"

    narrator "她应对自如，每个人都能照顾到。"

    narrator "但她的笑容里有一种……熟练感。"

    player_thought "像是早就习惯了被人围绕。"

    # 林晚棠在群体中的状态 — 核心：受欢迎但孤独
    narrator "另一边。"

    narrator "林晚棠坐在座位上，安静地收拾书包。"

    narrator "有两个女生过来找她说话。"

    show lindao smile at LEFT_CENTER with dissolve

    female_student_1 "晚棠，周末一起去逛街嘛？"

    lindao "（笑着）不好意思啊，我这周末有事。"

    narrator "温柔地拒绝了。"

    narrator "脸上带着恰到好处的歉意的笑。"

    female_student_2 "那下次咯！"

    lindao "嗯，下次一定。"

    narrator "两个女生离开后。"

    narrator "她脸上的笑意淡了下去。"

    narrator "不是不开心，而是……松了一口气的感觉。"

    show lindao normal at LEFT_CENTER with dissolve

    player_thought "她总是这样。对谁都温柔，但对谁都不敞开。"

    # 主角的小行动 — 不是为了攻略，而是真的在意
    player "林晚棠。"

    show lindao surprised at LEFT_CENTER with dissolve

    lindao "嗯？"

    player "你这周末真有事？还是不想去？"

    narrator "她愣了一下。"

    show lindao shy at LEFT_CENTER with dissolve

    lindao "（小声）……都被你看穿了啊。"

    player "不想去就不去嘛。"

    lindao "（低头）嗯……我只是觉得……"

    narrator "她没有说完。"

    narrator "但我知道她想说什么。"

    narrator "——有时候待在人堆里，比一个人待着还累。"

    $ persistent.lindao_affection += 3
    $ persistent.chapter1_day6_lindao_defense = True

    # 配角互动 — 周芷晴观察主角
    narrator "散会后。"

    narrator "我正要离开——"

    narrator "周芷晴挡在了门口。"

    zhou "（双手背在身后，歪头看着我）陆鸣同学~"

    player "……怎么了？"

    zhou "你和林晚棠关系很好嘛。"

    player "还行吧。"

    zhou "（眯眼笑）只是'还行'？"

    zhou "那我怎么看你跟她说话的时候，表情都不一样了呢？"

    player "……你想说什么？"

    zhou "（突然收起笑容，认真脸）没什么。"

    narrator "她又变回了元气满满的样子。"

    zhou "就是觉得挺有意思的~毕竟她平时很少跟男生那么自然地聊天。"

    narrator "她从我身边走过。"

    narrator "肩膀撞了我一下——"

    narrator "不重，但绝对是有意的。"

    zhou "（回头）加油哦，陆鸣同学~"

    narrator "她的背影消失在楼梯口。"

    player_thought "这个女生……"

    player_thought "到底在看什么？"

    $ persistent.zhou_affection += 2

    hide lindao with dissolve

    scene black

    call chapter_title("Day 6 End", "", 1.5)

    jump chapter1_day7

label chapter1_day7:
    $ persistent.current_day = 7

    scene black

    call chapter_title("前夕", "Day 7", 1.5)

    scene bg bedroom with dissolve

    narrator "第七天。周六。"

    narrator "明天就是决定性的一天了。"

    player_thought "按照计划，明天早上我要站在她家楼下等她。"

    player_thought "然后一起上学。"

    player_thought "说起来简单……做起来真的好紧张。"

    # 前夜的心理建设 — 减少前世独白，增加当下感
    narrator "我躺在床上，盯着天花板。"

    narrator "桌上的诺基亚闪了两下灯。"

    narrator "是林远发来的短信。"

    narrator "'明天出来打篮球？'"

    player "（回复）明天有事，改天吧。"

    narrator "林远秒回了三个问号。"

    narrator "'？？？你有事？什么事？难道是——'"

    narrator "后面跟了一串QQ表情。"

    player "（回复）滚。"

    narrator "我把手机扔到一边。"

    narrator "心里却在想——"

    player "明天……该穿什么好呢？"

    player_thought "等等，我在想什么？"

    player_thought "我又不是去约会……"

    player_thought "……只是送个同学上学而已。"

    player "（翻了个身）睡觉！"

    narrator "但我清楚地听到自己的心跳很快。"

    # 小冲突伏笔 — 引入不确定性
    narrator "临睡前，我打开电脑看了一眼班级QQ群。"

    narrator "有人在讨论明天的安排。"

    narrator "一个我不熟悉的名字跳了出来——"

    narrator "'林晚棠同学，明天有空吗？想请你帮个忙。'"

    narrator "发消息的人：赵轩然。"

    narrator "群里安静了两秒。"

    player_thought "赵轩然……班里有这个人吗？完全没印象。"

    narrator "过了大概五分钟。"

    narrator "林晚棠回了一个QQ表情。"

    narrator "是一个点头的小猫。"

    narrator "——答应了？"

    player_thought "……"

    narrator "我关掉QQ，合上电脑。"

    narrator "闭上眼睛。"

    narrator "但这一夜，睡得并不安稳。"

    $ persistent.chapter1_day7_zhao_appeared = True

    scene black

    call chapter_title("Day 7 End", "", 1.5)

    jump chapter1_day8_preview

# =============================================================================
# Day 8 前置过渡（衔接原林晚棠线）
# =============================================================================

label chapter1_day8_preview:
    $ persistent.current_day = 8

    scene black

    call chapter_title("靠近", "Day 8", 1.5)

    narrator "第八天。清晨。"

    narrator "闹钟响之前我就醒了。"

    narrator "或者说——根本没怎么睡着。"

    player_thought "昨晚那个赵轩然的事……"

    player_thought "别多想。先做好今天的再说。"

    narrator "我站在镜子前，看着自己。"

    narrator "深呼吸。"

    player "好了。出发。"

    # 跳转到林晚棠线 Day 8
    jump lindao_day8_morning
