# =============================================================================
# script.rpy - 主脚本入口
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

# 启动时执行
label start:
    # 初始化游戏
    call init_game from _call_init_game

    # 显示标题画面（可选跳过）
    $ quick_menu = False
    scene black with fade
    pause 1.0

    # 跳转到序章
    jump prologue

# =============================================================================
# 游戏初始化
# =============================================================================

label init_game:
    # 设置主角名称
    $ player_name = "陆鸣"

    # 初始化当前章节
    $ current_chapter = "prologue"

    # 重置所有Flag（开始新游戏）
    call reset_all_flags from _call_reset_flags

    return

# =============================================================================
# Flag重置
# =============================================================================

label reset_all_flags:
    # 系统Flag重置
    $ persistent.current_day = 1
    $ persistent.current_chapter = "prologue"
    $ persistent.fragment_count = 0
    $ persistent.fragments_collected = []
    $ persistent.regret_value = 0
    $ persistent.butterfly_count = 0

    # 好感度重置
    $ persistent.lindao_affection = 0
    $ persistent.suni_affection = 0
    $ persistent.zhou_affection = 0
    $ persistent.chen_affection = 0
    $ persistent.shen_affection = 0

    # 结局Flag重置
    $ persistent.lindao_route_completed = False
    $ persistent.suni_route_completed = False
    $ persistent.zhou_route_completed = False
    $ persistent.chen_route_completed = False
    $ persistent.shen_route_completed = False
    $ persistent.true_ending_unlocked = False

    # 序章Flag重置
    $ prologue_woke_up = False
    $ prologue_memory_fragment_1 = False
    $ prologue_memory_fragment_2 = False
    $ prologue_butterfly_1 = False

    return

# =============================================================================
# 序章
# =============================================================================

label prologue:
    # 更新当前章节
    $ persistent.current_chapter = "prologue"

    # 显示序章标题
    scene black with fade
    centered "{size=+10}{b}序章{/b}{/size}\n{w=0.5}死亡与重生{w=0.5}"

    pause 2.0

    # 跳转到序章脚本
    jump prologue_part1

# =============================================================================
# 第一章
# =============================================================================

label chapter1:
    # 更新当前章节
    $ persistent.current_chapter = "chapter1"

    scene black with fade
    centered "{size=+10}{b}第一章{/b}{/size}\n{w=0.5}熟悉的陌生{w=0.5}"

    pause 2.0

    jump chapter1_day1

# =============================================================================
# 各女主线入口（通过菜单选择）
# =============================================================================

label route_menu:
    # 显示路线选择菜单
    menu:
        "林晚棠线" if persistent.chapter1_day1_school:
            jump lindao_route_start

        "苏念卿线" if persistent.chapter1_day1_school:
            jump suni_route_start

        "周芷晴线" if persistent.chapter1_day1_school:
            jump zhou_route_start

        "陈墨线" if persistent.chapter1_day1_school:
            jump chen_route_start

        "沈听雨线" if persistent.chapter1_day1_school and persistent.shen_met:
            jump shen_route_start

        "继续游戏":
            jump .continue

    label .continue:
        return

# =============================================================================
# 林晚棠线入口
# =============================================================================

label lindao_route_start:
    $ persistent.current_chapter = "lindao"
    $ persistent.lindao_affection = 42  # 继承第一章好感度
    $ renpy.movie_cutscene("fadeblack.webm") if renpy.exists("fadeblack.webm") else None
    jump lindao_day8

# =============================================================================
# 苏念卿线入口
# =============================================================================

label suni_route_start:
    $ persistent.current_chapter = "suni"
    scene black with fade
    centered "{size=+8}{b}苏念卿线{/b}{/size}\n{w=0.5}年岁的温柔{w=0.5}"
    pause 2.0
    jump suni_day8

# =============================================================================
# 周芷晴线入口
# =============================================================================

label zhou_route_start:
    $ persistent.current_chapter = "zhou"
    scene black with fade
    centered "{size=+8}{b}周芷晴线{/b}{/size}\n{w=0.5}阳光下的心动{w=0.5}"
    pause 2.0
    jump zhou_day4

# =============================================================================
# 陈墨线入口
# =============================================================================

label chen_route_start:
    $ persistent.current_chapter = "chen"
    scene black with fade
    centered "{size=+8}{b}陈墨线{/b}{/size}\n{w=0.5}完美与真实{w=0.5}"
    pause 2.0
    jump chen_day3

# =============================================================================
# 沈听雨线入口（隐藏线）
# =============================================================================

label shen_route_start:
    $ persistent.current_chapter = "shen"
    scene black with fade
    centered "{size=+8}{b}沈听雨线{/b}{/size}\n{w=0.5}命运的重逢{w=0.5}"
    pause 2.0
    jump shen_day5

# =============================================================================
# True Ending
# =============================================================================

label true_ending:
    $ persistent.current_chapter = "true_ending"
    scene black with fade
    centered "{size=+10}{b}True Ending{/b}{/size}\n{w=0.5}重生后的选择{w=0.5}"
    pause 2.0
    jump te_start

# =============================================================================
# 记忆碎片收集提示
# =============================================================================

label collect_fragment(fragment_id, fragment_name):
    # 检查是否已收集
    if fragment_id in persistent.fragments_collected:
        return

    # 添加到已收集列表
    $ persistent.fragments_collected.append(fragment_id)
    $ persistent.fragment_count += 1

    # 显示收集提示
    scene black with dissolve
    centered "{size=+6}{color=#a29bfe}✧ 记忆碎片收集 ✧{/color}{/size}\n\n{size=+4}[fragment_name]{/size}"

    pause 2.0

    # 返回到之前的场景（使用 scene black 恢复）
    scene black with dissolve

    return

# =============================================================================
# 好感度变化提示
# =============================================================================

label affection_change(heroine, change, show_bar=True):
    if show_bar:
        $ affection_name = ""
        if heroine == "lindao":
            $ affection_name = "林晚棠"
        elif heroine == "suni":
            $ affection_name = "苏念卿"
        elif heroine == "zhou":
            $ affection_name = "周芷晴"
        elif heroine == "chen":
            $ affection_name = "陈墨"
        elif heroine == "shen":
            $ heroine_name = "沈听雨"

        if change > 0:
            show screen affection_popup(affection_name, "+" + str(change), "#ff6b6b")
        else:
            show screen affection_popup(affection_name, str(change), "#54a0ff")

        pause 1.5
        hide screen affection_popup

    return

# =============================================================================
# 蝴蝶效应提示
# =============================================================================

label butterfly_effect(description):
    $ persistent.butterfly_count += 1

    butterfly_narration "{b}【蝴蝶效应】{/b}\n{description}"

    return

# =============================================================================
# 游戏结束
# =============================================================================

label game_over:
    scene black with fade
    centered "{size=+10}{b}Game Over{/b}{/size}"

    menu:
        "回到标题":
            jump _return_to_title
        "结束游戏":
            return

label _return_to_title:
    jump start

# =============================================================================
# 标题画面（从Ren'Py模板调用）
# =============================================================================

label before_main_menu:
    return

label main_menu:
    return
