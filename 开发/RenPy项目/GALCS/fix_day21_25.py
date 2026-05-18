# -*- coding: utf-8 -*-
with open(r'J:\项目\GAL\开发\RenPy项目\GALCS\game\script\02_lindao_route.rpy', 'r', encoding='utf-8') as f:
    content = f.read()

# Day 21 - basketball court moonlight scene
old_day21 = '''    narrator "正当我纠结的时候——"

    narrator "身后传来脚步声。"

    lindao "（小声）陆鸣？"

    narrator "我回过头。"

    player "晚棠？你怎么在这里？"

    lindao "（走过来）我……睡不着，出来走走。"

    narrator "她在我旁边坐下。"

    narrator "月光洒在她脸上，很柔和。"

    narrator "我们并肩坐着，谁也没有说话。"

    narrator "夜风吹过，带来初夏的味道。"

    narrator "她的发丝被风吹起，轻轻拂过我的肩膀。"

    scene black

    narrator "月亮很圆，星星很亮。"

    narrator "篮球场上空无一人，只有我们两个。"

    narrator "她突然开口。"

    lindao "陆鸣……"

    player "嗯？"

    lindao "你最近是不是有什么事瞒着我？"

    narrator "我愣了一下。"

    player "为什么这么问？"

    lindao "（看向远方）你最近怪怪的……"

    lindao "有时候看着我，会突然走神。"

    lindao "好像在想什么很远的事情。"

    player_thought "……"

    player_thought "她察觉到了。"

    player "晚棠……"

    narrator "她转过头，看着我。"

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

    lindao "陆鸣。"

    player "嗯？"

    lindao "（回头）不管明天你要说什么……"

    narrator "她深吸一口气。"

    lindao "我都想听。"

    narrator "然后她转身，快步离开了。"

    narrator "月光下，我看着她的背影消失在夜色中。"

    narrator "嘴角不自觉地扬了起来。"

    player "……好。"

    scene black

    centered "{b}—— Day 21 End ——{/b}
{w=0.5}告白前夜{/w=0.5}"'''

new_day21 = '''    scene bg classroom_sunset with dissolve

    narrator "正当我纠结的时候——"

    narrator "身后传来脚步声。"

    show lindao normal at LEFT with dissolve

    lindao "（小声）陆鸣？"

    narrator "我回过头。"

    player "晚棠？你怎么在这里？"

    show lindao smile at LEFT with dissolve

    lindao "（走过来）我……睡不着，出来走走。"

    narrator "她在我旁边坐下。"

    narrator "月光洒在她脸上，很柔和。"

    narrator "我们并肩坐着，谁也没有说话。"

    narrator "夜风吹过，带来初夏的味道。"

    narrator "她的发丝被风吹起，轻轻拂过我的肩膀。"

    hide lindao with dissolve

    scene black

    narrator "月亮很圆，星星很亮。"

    narrator "篮球场上空无一人，只有我们两个。"

    narrator "她突然开口。"

    show lindao normal at LEFT with dissolve

    lindao "陆鸣……"

    player "嗯？"

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

    player "（认真）明天，我会告诉你一切。"

    player "到时候……你就知道了。"

    narrator "她没有追问。"

    narrator "只是轻轻点了点头。"

    show lindao smile at LEFT with dissolve

    lindao "好。我等你。"

    narrator "月光下，她的眼睛很亮。"

    narrator "里面有期待，有信任，也有……别的什么。"

    hide lindao with dissolve

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

    show lindao normal at LEFT with dissolve

    lindao "陆鸣。"

    player "嗯？"

    lindao "（回头）不管明天你要说什么……"

    narrator "她深吸一口气。"

    show lindao shy at LEFT with dissolve

    lindao "我都想听。"

    narrator "然后她转身，快步离开了。"

    narrator "月光下，我看着她的背影消失在夜色中。"

    narrator "嘴角不自觉地扬了起来。"

    player "……好。"

    hide lindao with dissolve

    scene black

    centered "{b}—— Day 21 End ——{/b}
{w=0.5}告白前夜{/w=0.5}"'''

if old_day21 in content:
    content = content.replace(old_day21, new_day21)
    print('Day 21 替换成功!')
else:
    print('Day 21 模式未找到，跳过')

# Day 23 - 天台告白
old_day23 = '''    narrator "天台。"

    narrator "夕阳西下，把一切染成金色。"

    narrator "林晚棠已经在那里等着了。"

    narrator "她看到我，有些紧张地攥着衣角。"

    lindao "陆鸣……"

    player "晚棠。"

    narrator "我走过去，站在她面前。"

    narrator "夕阳照在她脸上，眼睛里有期待。"

    player "晚棠，我有话要对你说。"

    lindao "（点头）……我在听。"

    narrator "我深吸一口气。"

    player "你可能觉得我很奇怪。"

    player "为什么突然对你好，为什么知道你家的事，为什么……"

    player "总是看着你发呆。"

    lindao "（小声）……"

    player "其实……我有些事一直没告诉你。"

    narrator "她没有说话，只是静静地看着我。"

    player "晚棠……我喜欢你。"

    narrator "话说出口的瞬间，世界仿佛安静了。"

    narrator "夕阳，晚风，远处的城市喧嚣——"

    narrator "一切都停了下来。"

    narrator "只剩下她的眼睛，和我的心跳声。"

    player "不是最近才喜欢的。"

    player "是喜欢了很久。"

    player "久到……我自己都记不清是从什么时候开始的。"

    narrator "她的眼眶红了。"

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

    lindao "（哽咽）你这个笨蛋……"

    player "……？"

    lindao "（用手背擦眼泪）你知道我等了多久吗……"

    player_thought "……"

    player_thought "她……等我？"

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

    scene black

    narrator "夕阳完全沉入地平线。"

    narrator "天边的红色渐渐消退，取而代之的是深蓝色的夜幕。"

    narrator "星星一颗一颗亮起来。"

    narrator "我们并肩坐在天台上，手牵着手。"

    narrator "她靠在我肩膀上，眼睛红红的，但嘴角在笑。"

    lindao "（轻声）陆鸣……"

    player "嗯？"

    lindao "你说的是真的吗？"

    player "当然是真的。"

    lindao "（小声）那你……从什么时候开始喜欢我的？"

    player_thought "这个问题……"

    player_thought "我怎么回答？说我前世就喜欢了三年？"

    player "（想了想）大概是……高一的时候吧。"

    lindao "（惊讶）那么早？"

    player "嗯。第一次见到你的时候就觉得……"

    player "这个女生很特别。"

    lindao "（脸红）你骗人……那时候你都不怎么跟我说话……"

    player "（微笑）因为不敢。"

    lindao "不敢？"

    player "怕说了你会讨厌我。"

    lindao "（小声）笨蛋……"

    narrator "她把脸埋进我的肩膀。"

    narrator "我轻轻揽住她的腰。"

    narrator "星空下，我们就这样坐着。"

    narrator "像是世界上只剩下我们两个人。"

    scene black

    narrator "不知道过了多久。"

    narrator "她突然抬起头。"

    lindao "陆鸣。"

    player "嗯？"

    lindao "（认真地看着我）不管以后发生什么……"

    lindao "我都不会后悔今天。"

    narrator "她的眼睛很亮，里面有星光，也有我的倒影。"

    player "（微笑）我也是。"

    narrator "她笑了。"

    narrator "然后踮起脚尖——"

    narrator "轻轻在我脸颊上落下一个吻。"

    narrator "很快，像是蜻蜓点水。"

    narrator "然后她迅速低下头，脸红得像熟透的苹果。"

    lindao "（小声）这……这是定金。"

    player "……"

    narrator "我的脸也红了。"

    narrator "心跳漏了好几拍。"

    player "那……高考之后呢？"

    lindao "（抬起头）高考之后……"

    narrator "她看着我，眼睛里有光。"

    lindao "等你给我正式的答案。"

    narrator "我握紧她的手。"

    player "好。"

    scene black

    narrator "月亮升起来了。"

    narrator "我们一起看了很久的星星。"

    narrator "然后，一起回家。"

    narrator "路上，我们牵着手。"

    narrator "谁也没有说话。"

    narrator "但这沉默，比任何语言都更温暖。"

    scene black

    centered "{b}—— Day 23 End ——{/b}
{w=0.5}告白成功{/w=0.5}"'''

new_day23 = '''    scene bg classroom_sunset with dissolve

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

    player "不是最近才喜欢的。"

    player "是喜欢了很久。"

    player "久到……我自己都记不清是从什么时候开始的。"

    show lindao crying at LEFT with dissolve

    narrator "她的眼眶红了。"

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

    scene bg classroom_sunset with dissolve

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

    show lindao shy at LEFT with dissolve

    lindao "（小声）笨蛋……"

    narrator "她把脸埋进我的肩膀。"

    narrator "我轻轻揽住她的腰。"

    narrator "星空下，我们就这样坐着。"

    narrator "像是世界上只剩下我们两个人。"

    hide lindao with dissolve

    scene bg classroom_sunset with dissolve

    narrator "不知道过了多久。"

    narrator "她突然抬起头。"

    show lindao smile at LEFT with dissolve

    lindao "陆鸣。"

    player "嗯？"

    lindao "（认真地看着我）不管以后发生什么……"

    lindao "我都不会后悔今天。"

    narrator "她的眼睛很亮，里面有星光，也有我的倒影。"

    player "（微笑）我也是。"

    narrator "她笑了。"

    narrator "然后踮起脚尖——"

    narrator "轻轻在我脸颊上落下一个吻。"

    narrator "很快，像是蜻蜓点水。"

    narrator "然后她迅速低下头，脸红得像熟透的苹果。"

    show lindao shy at LEFT with dissolve

    lindao "（小声）这……这是定金。"

    player "……"

    narrator "我的脸也红了。"

    narrator "心跳漏了好几拍。"

    player "那……高考之后呢？"

    show lindao normal at LEFT with dissolve

    lindao "（抬起头）高考之后……"

    narrator "她看着我，眼睛里有光。"

    lindao "等你给我正式的答案。"

    narrator "我握紧她的手。"

    player "好。"

    hide lindao with dissolve

    scene black

    narrator "月亮升起来了。"

    narrator "我们一起看了很久的星星。"

    narrator "然后，一起回家。"

    narrator "路上，我们牵着手。"

    narrator "谁也没有说话。"

    narrator "但这沉默，比任何语言都更温暖。"

    scene black

    centered "{b}—— Day 23 End ——{/b}
{w=0.5}告白成功{/w=0.5}"'''

if old_day23 in content:
    content = content.replace(old_day23, new_day23)
    print('Day 23 替换成功!')
else:
    print('Day 23 模式未找到，跳过')

# Day 25 - Happy Ending
old_day25 = '''    narrator "校门口。"

    narrator "林晚棠站在那里等我。"

    narrator "她看到我，眼睛一下子亮了。"

    lindao "（跑过来）陆鸣！"

    player "（微笑）考得怎么样？"

    lindao "（笑着）应该还行吧……你呢？"

    player "（牵起她的手）不管成绩怎样，我们先去庆祝。"

    narrator "她没有挣脱。"

    narrator "反而握紧了我的手。"

    lindao "好。"

    scene black

    narrator "学校后山。"

    narrator "这里是我们第一次告白的地方。"

    narrator "也是我们约定'高考后给正式答案'的地方。"

    scene black

    narrator "星空下。"

    narrator "我看着她的眼睛。"

    player "晚棠。"

    lindao "嗯？"

    player "高考结束了。"

    narrator "她点头，眼睛里满是期待。"

    player "我来兑现承诺了。"

    narrator "我深吸一口气。"

    player "林晚棠。"

    player "我喜欢你。"

    player "不是'想跟你做朋友'的那种喜欢。"

    player "是想跟你在一起、一辈子、不分开的那种喜欢。"

    narrator "她的眼眶红了。"

    player "你愿意……做我的女朋友吗？"

    narrator "星空下，她看着我。"

    narrator "眼泪落下来，但嘴角在笑。"

    lindao "（点头）我愿意。"

    narrator "她扑进我怀里。"

    narrator "我紧紧抱住她。"

    narrator "这一刻，星空、晚风、虫鸣——"

    narrator "一切都刚刚好。"

    narrator "前世那个没说出口的告白——"

    narrator "这一世，终于说出来了。"

    narrator "而且，她答应了。"

    $ persistent.lindao_happy_ending = True

    scene black'''

new_day25 = '''    scene bg classroom_sunset with dissolve

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

    scene black'''

if old_day25 in content:
    content = content.replace(old_day25, new_day25)
    print('Day 25 替换成功!')
else:
    print('Day 25 模式未找到，跳过')

with open(r'J:\项目\GAL\开发\RenPy项目\GALCS\game\script\02_lindao_route.rpy', 'w', encoding='utf-8') as f:
    f.write(content)

print('全部完成!')
