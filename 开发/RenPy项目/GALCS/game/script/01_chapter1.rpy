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

    player_thought "三十天。"

    player_thought "高考前最后的三十天。"

    player_thought "前世这时候，我在干什么来着……"

    narrator "想不起来了。"

    narrator "果然细节都模糊了。"

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

    player_thought "苏念卿……"

    player_thought "前世，她对我很好。"

    player_thought "但也仅此而已。"

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

    player_thought "前世这时候，我是怎么过的？"

    player_thought "每天浑浑噩噩，不知道自己想要什么。"

    player_thought "这次不一样了。"

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

    player_thought "前世我们是同桌，三年都没说破。"

    player_thought "这次，得找一个契机。"

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

    call chapter_title("日常推进中……", "Day 3 至 Day 7", 2.0)

    narrator "第三天。"

    narrator "高考倒计时：27天。"

    narrator "时间在一点点流逝。"

    narrator "但我没有之前那么焦虑了。"

    player_thought "重生给了我第二次机会。"

    player_thought "这次，一定要抓住。"

    if persistent.chapter1_day2_immigration_topic:
        call show_notification("命运改变", "留学出现转机", "#a29bfe")

    scene bg classroom_day with dissolve

    narrator "这几天，发生了很多小事。"

    narrator "和同学聊天。"

    narrator "听老师讲模拟考的事。"

    narrator "回家吃饭，和妈妈说说话。"

    narrator "平凡的日常。"

    narrator "但对我来说，每一刻都不平凡。"

    narrator "林晚棠……"

    narrator "这几天，我们的关系有了一些微妙的变化。"

    narrator "虽然还是普通的同桌交流。"

    narrator "但我能感觉到，她看我的眼神不一样了。"

    narrator "好奇，还有一丝……别的什么。"

    scene black

    call chapter_title("第一章 End", "", 1.5)

    narrator "第一章结束。"

    narrator "你已经认识了五位重要的女孩。"

    narrator "接下来的日子，你想和谁在一起？"

    jump route_menu
