# =============================================================================
# screens.rpy - 界面屏幕
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

init python:
    # 好感度弹窗样式
    style.affection_popup = Style(style.default)
    style.affection_popup.xalign = 0.5
    style.affection_popup.yalign = 0.3
    style.affection_popup.background = Solid("#2d4a6f")
    style.affection_popup.padding = (20, 15, 20, 15)

    # 对话框映射
    # bar_narration = 旁白/内心独白/多女主通用框（上方可叠放立绘或头像）
    DIALOGUE_BOXES = {
        "旁白": "images/UI/UI_bar_narration.png",
        "独白": "images/UI/UI_bar_narration.png",
        "???": "images/UI/UI_bar_narration.png",
        "内心": "images/UI/UI_bar_narration.png",
    }

    # 获取对话背景图片
    def get_dialogue_bg(who):
        if who and who in DIALOGUE_BOXES:
            return DIALOGUE_BOXES[who]
        return "images/UI/UI_dialogue_box.png"

# =============================================================================
# 好感度变化弹窗（Screen）
# =============================================================================

screen affection_popup(name, change, color):
    frame:
        at popup_appear
        background Solid("#2d4a6f")
        padding (20, 15, 20, 15)

        vbox:
            text "{b}{name}{/b}" size 28 color "#f5f5f5"
            text "{color=[color]}{b}{change}{/b}{/color}" size 36

# 弹窗动画
transform popup_appear:
    easein 0.3 alpha 1.0
    pause 1.2
    easeout 0.3 alpha 0.0

# =============================================================================
# 好感度条（游戏内显示）
# =============================================================================

screen affection_bar(heroine_name, affection_value, max_value=100):
    frame:
        xalign 0.98
        yalign 0.02
        padding (15, 10, 15, 10)
        background Solid("#1a1a2e")

        vbox:
            spacing 5

            text "{b}{heroine_name}{/b}" size 20 color "#f5f5f5"

            bar:
                value AnimatedValue(affection_value, max_value, 0.5)
                range max_value
                xmaximum 150
                left_gutter 0
                right_gutter 0
                thumb None
                left_bar Solid("#e8a87c")
                right_bar Solid("#3a3a4a")

            text "{affection_value}/{max_value}" size 16 color "#a0a0a0"

# =============================================================================
# HUD显示（游戏过程中）
# =============================================================================

screen hud():
    frame:
        xalign 0.02
        yalign 0.02
        padding (15, 10, 15, 10)
        background Solid("#1a1a2e")

        vbox:
            text "Day [persistent.current_day]" size 24 color "#f5f5f5"

            if persistent.current_chapter == "prologue":
                text "序章" size 16 color "#a29bfe"
            elif persistent.current_chapter == "chapter1":
                text "第一章" size 16 color "#6c9bd1"

# =============================================================================
# =============================================================================
# 对话框 - 自定义UI完全接管
# 布局（1920x1080 屏幕）：
#   y=800~1080  对话框 (280px, 贴屏幕底边，含内嵌按钮)
# =============================================================================

screen say(who, what):
    # 根据角色选择对话框背景
    $ bg_img = get_dialogue_bg(who)

    # ── 层1：对话框背景图 (280px, 直接贴屏幕底边) ──
    add bg_img:
        xalign 0.5
        ypos 800

    # ── 层2：名字背景牌 (320×44) ──
    if who:
        add "images/UI/UI_nameplate.png":
            xpos 345
            ypos 826

    # ── 层3：文字内容 ──
    # 无论有无角色名，都预留名字行高度（32px），避免正文位置跳动
    fixed:
        xpos 370
        ypos 826
        xsize 1190
        ysize 220

        vbox:
            spacing 28

            # 名字行：有名字显示名字，无名字时留空（保持高度一致）
            if who:
                text who id "who":
                    size 42
                    color "#1a1a2e"
                    font "fonts/simhei.ttf"
            else:
                null height 44

            text what id "what":
                size 38
                color "#1a1a2e"
                font "fonts/simhei.ttf"
                line_spacing 12
                outlines [(1, "#ffffff", 0, 0)]

    # ── 层4：快捷按钮（内嵌在对话框右下角，单排显示）──
    if quick_menu:
        hbox:
            xpos 1460
            ypos 1016
            spacing 6

            imagebutton:
                idle "images/UI/UI_quick_auto_default.png"
                hover "images/UI/UI_quick_auto_hover.png"
                action ui.callsinnewcontext("toggle_auto_forward")
            imagebutton:
                idle "images/UI/UI_quick_skip_default.png"
                hover "images/UI/UI_quick_skip_hover.png"
                action Skip()
            imagebutton:
                idle "images/UI/UI_quick_save_default.png"
                hover "images/UI/UI_quick_save_hover.png"
                action ShowMenu('save')
            imagebutton:
                idle "images/UI/UI_quick_load_default.png"
                hover "images/UI/UI_quick_load_hover.png"
                action ShowMenu('load')
            imagebutton:
                idle "images/UI/UI_quick_history_default.png"
                hover "images/UI/UI_quick_history_hover.png"
                action ShowMenu('history')
            imagebutton:
                idle "images/UI/UI_quick_settings_default.png"
                hover "images/UI/UI_quick_settings_hover.png"
                action ShowMenu('preferences')
            imagebutton:
                idle "images/UI/UI_quick_hide_default.png"
                hover "images/UI/UI_quick_hide_hover.png"
                action _window_hide
            imagebutton:
                idle "images/UI/UI_quick_exit_default.png"
                hover "images/UI/UI_quick_exit_hover.png"
                action MainMenu()

# =============================================================================
# 快速菜单（保留定义，不再被 say screen use）
# =============================================================================

screen quick_menu():
    if quick_menu:
        hbox:
            xpos 1460
            ypos 1016
            spacing 6

            imagebutton:
                idle "images/UI/UI_quick_auto_default.png"
                hover "images/UI/UI_quick_auto_hover.png"
                action ui.callsinnewcontext("toggle_auto_forward")
            imagebutton:
                idle "images/UI/UI_quick_skip_default.png"
                hover "images/UI/UI_quick_skip_hover.png"
                action Skip()
            imagebutton:
                idle "images/UI/UI_quick_save_default.png"
                hover "images/UI/UI_quick_save_hover.png"
                action ShowMenu('save')
            imagebutton:
                idle "images/UI/UI_quick_load_default.png"
                hover "images/UI/UI_quick_load_hover.png"
                action ShowMenu('load')
            imagebutton:
                idle "images/UI/UI_quick_history_default.png"
                hover "images/UI/UI_quick_history_hover.png"
                action ShowMenu('history')
            imagebutton:
                idle "images/UI/UI_quick_settings_default.png"
                hover "images/UI/UI_quick_settings_hover.png"
                action ShowMenu('preferences')
            imagebutton:
                idle "images/UI/UI_quick_hide_default.png"
                hover "images/UI/UI_quick_hide_hover.png"
                action _window_hide
            imagebutton:
                idle "images/UI/UI_quick_exit_default.png"
                hover "images/UI/UI_quick_exit_hover.png"
                action MainMenu()

# =============================================================================
# 选择菜单样式
# =============================================================================

transform choice_hover:
    on hovered, showed:
        easein 0.1 zoom 1.03 yoffset -2
    on idle:
        easeout 0.1 zoom 1.0 yoffset 0

screen choice(items):
    modal True
    zorder 100

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15

        for caption, action, chosen in items:
            if action:
                button:
                    at choice_hover
                    action action
                    xsize 800
                    ysize 90
                    background "images/UI/UI_choice_normal.png"
                    hover_background "images/UI/UI_choice_hover.png"

                    text caption:
                        xalign 0.5
                        yalign 0.35
                        size 26
                        color "#ffffff"
                        outlines [(1, "#000000", 0, 0)]

            else:
                text caption:
                    xalign 0.5
                    size 26
                    color "#666666"


# =============================================================================
# 章节标题（全屏居中 + 淡入/停留/淡出）
# 用法: call chapter_title("终焉", "序章·第一幕", 2.0)
#   title    = 主标题（大字）
#   subtitle = 副标题（小字，可选，传 "" 则不显示）
#   hold     = 居中停留秒数（默认2.0）
# 总时长 = 0.8(dissolve) + hold(停留) + 1.0(淡出dissolve) = 默认3.8秒
# =============================================================================
label chapter_title(title, subtitle="", hold=2.0):
    $ _ct_title = title
    $ _ct_subtitle = subtitle
    window hide
    show screen _chapter_title_display with dissolve
    $ renpy.pause(0.8 + hold + 1.0)
    hide screen _chapter_title_display with dissolve
    window show
    return

screen _chapter_title_display:
    zorder 200
    frame:
        background Solid("#000000aa")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.45
            spacing 20

            if _ct_subtitle:
                text _ct_subtitle:
                    xalign 0.5
                    size 28
                    color "#a0a0a0"
                    outlines [(1, "#000000", 0, 0)]

            text _ct_title:
                xalign 0.5
                size 64
                color "#ffffff"
                outlines [(2, "#000000", 0, 0)]


# =============================================================================
# 悬浮通知（Toast）— 记忆碎片解锁 / 细节发现 等提示
# 屏幕右上角淡入 → 停留 → 上飘淡出
# 用法: $ show_notification("记忆碎片解锁", "✦ 雨中的温暖 ✦", "#FFD700")
#   title   = 标题文字（小字）
#   message = 主内容（大字）
#   color   = 主题色（十六进制，默认金色）
# =============================================================================

init python:
    _toast_title = ""
    _toast_message = ""
    _toast_color = "#FFD700"

label show_notification(title, message, color="#FFD700"):
    $ _toast_title = title
    $ _toast_message = message
    $ _toast_color = color
    show screen _toast_display
    $ renpy.pause(2.0)
    hide screen _toast_display
    return

screen _toast_display:
    zorder 300
    # 居中偏上显示，无背景框
    frame:
        at toast_anim
        xalign 0.5
        ypos 80
        background None
        xpadding 0
        ypadding 0
        vbox:
            xalign 0.5
            spacing 12
            if _toast_title:
                text _toast_title:
                    xalign 0.5
                    size 26
                    color _toast_color
            text _toast_message:
                xalign 0.5
                size 42
                color "#ffffff"

transform toast_anim:
    on show:
        alpha 0.0
        yoffset 15
        easein 0.4 alpha 1.0 yoffset 0
        pause 2.2
        easeout 0.5 alpha 0.0 yoffset -20


# =============================================================================
# Day16 冰点特效屏
# 用法: call show_ice_point
# 在 CG-05 图片之上叠加蓝冰色文字 + 颤动动画，模拟关系冻结感
# 总时长约 3.5 秒
# =============================================================================

init python:
    _ice_point_initialized = True

label show_ice_point:
    window hide
    show screen _ice_point_screen
    $ renpy.pause(3.5)
    hide screen _ice_point_screen with dissolve
    window show
    return

screen _ice_point_screen:
    zorder 250

    # 全屏半透明蓝黑遮罩
    frame:
        background Solid("#00001acc")
        xfill True
        yfill True

    # 冰裂线条装饰（模拟冻裂感，使用文字排版）
    vbox:
        xalign 0.5
        yalign 0.42
        spacing 18

        # 主文字：关系降至冰点（用 ATL 颤动动画）
        text "{b}关系降至冰点{/b}":
            at ice_shake
            xalign 0.5
            size 72
            color "#7ec8e3"
            outlines [(3, "#003a5c", 1, 1), (1, "#b0e0f0", 0, 0)]

        # 副文字：英文对照，增加质感
        text "RELATIONSHIP — FROZEN":
            at ice_fade_in
            xalign 0.5
            size 22
            color "#4a8fa8"
            outlines [(1, "#001a2e", 0, 0)]

        # 提示符：强调数值下降
        null height 8

        text "好感度 {color=#FF4444}-20{/color}":
            at ice_fade_in
            xalign 0.5
            size 28
            color "#c0d8e8"
            outlines [(1, "#001020", 0, 0)]

# 主标题：轻微颤动 + 蓝光脉冲感
transform ice_shake:
    alpha 0.0
    easein 0.4 alpha 1.0
    # 颤动循环（模拟冰裂震动）
    block:
        linear 0.06 xoffset -3
        linear 0.06 xoffset 3
        linear 0.06 xoffset -2
        linear 0.06 xoffset 0
        repeat 4
    pause 0.5
    # 颤动结束，稳定
    pause 1.2
    easeout 0.5 alpha 0.0

# 副文字/数值：延迟淡入
transform ice_fade_in:
    alpha 0.0
    pause 0.6
    easein 0.5 alpha 1.0
    pause 1.5
    easeout 0.5 alpha 0.0


# =============================================================================
# 高考倒计时特效屏
# 用法: call show_countdown(days)
#   days = 剩余天数（整数）
# 在当前背景之上叠加倒计时，红色数字脉冲缩放，约 2.8 秒
# =============================================================================

init python:
    _countdown_days = 0

label show_countdown(days=0):
    $ _countdown_days = days
    window hide
    show screen _countdown_screen
    $ renpy.pause(2.8)
    hide screen _countdown_screen with dissolve
    window show
    return

screen _countdown_screen:
    zorder 250

    # 顶部居中显示，不遮挡背景
    frame:
        at countdown_slide_in
        xalign 0.5
        ypos 60
        background Solid("#1a000099")
        xpadding 50
        ypadding 20

        hbox:
            xalign 0.5
            spacing 12

            text "高考倒计时":
                size 32
                color "#cccccc"
                yalign 0.5

            text "{b}[_countdown_days]{/b}":
                at countdown_pulse
                size 60
                color "#FF4444"
                yalign 0.5

            text "天":
                size 32
                color "#cccccc"
                yalign 0.5

# 整体从上方滑入
transform countdown_slide_in:
    yoffset -80
    alpha 0.0
    easein 0.35 yoffset 0 alpha 1.0
    pause 1.8
    easeout 0.45 yoffset -30 alpha 0.0

# 数字心跳脉冲
transform countdown_pulse:
    zoom 1.0
    # 入场时放大一次
    pause 0.3
    linear 0.15 zoom 1.25
    linear 0.15 zoom 1.0
    # 等待
    pause 0.6
    # 再跳一次
    linear 0.12 zoom 1.18
    linear 0.12 zoom 1.0


# =============================================================================
# 主菜单
# =============================================================================

screen main_menu():
    add Solid("#1a1a2e")

    vbox:
        align (0.5, 0.3)
        spacing 60

        text "{b}{size=+20}重生·轻逆袭{/size}{/b}":
            color "#f5f5f5"
            text_align 0.5

        text "{size=-5}Re: Second Chance{/size}":
            color "#a0a0a0"
            text_align 0.5

    frame:
        align (0.5, 0.65)
        background Solid("#16213e")
        padding (40, 30, 40, 30)

        vbox:
            spacing 15

            textbutton _("开始游戏"):
                action Start()
                text_style "main_menu_button"

            textbutton _("继续游戏"):
                action ShowMenu("load")
                text_style "main_menu_button"

            textbutton _("读取游戏"):
                action ShowMenu("load")
                text_style "main_menu_button"

            textbutton _("游戏设置"):
                action ShowMenu("preferences")
                text_style "main_menu_button"

            textbutton _("制作人员"):
                action ShowMenu("about")
                text_style "main_menu_button"

            textbutton _("退出游戏"):
                action Quit()
                text_style "main_menu_button"

style main_menu_button:
    size 28
    color "#f5f5f5"
    hover_color "#e8a87c"
    text_align 0.5
    xalign 0.5

# =============================================================================
# 加载/保存界面
# =============================================================================

screen load_save_screen(which):
    modal True
    tag menu

    add Solid("#000000")

    text "{b}{which}{/b}":
        size 36
        color "#f5f5f5"
        align (0.5, 0.1)

    frame:
        align (0.5, 0.5)
        background Solid("#16213e")
        padding (30, 20, 30, 20)

        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                for i in range(config.quicksave_slots if which == "Quick Save" else 10):
                    $ slot_name = "quicksave" if which == "Quick Save" else str(i + 1)

                    textbutton _("{b}存档 {slot_name}{/b}"):
                        action FileAction(slot_name)
                        text_style "save_slot_button"

style save_slot_button:
    size 24
    color "#f5f5f5"
    hover_color "#e8a87c"

# =============================================================================
# 游戏设置界面
# =============================================================================

screen preferences():
    modal True
    tag menu

    add Solid("#000000")

    frame:
        align (0.5, 0.5)
        background Solid("#16213e")
        padding (40, 30, 40, 30)

        vbox:
            spacing 60

            text "{b}游戏设置{/b}":
                size 32
                color "#f5f5f5"
                xalign 0.5

            null height 20

            hbox:
                spacing 60

                text "文字速度:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "text_cps", range=100)

            hbox:
                spacing 60

                text "自动播放:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "auto_forward_after", range=30)

            hbox:
                spacing 60

                text "音乐音量:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "music_volume")

            hbox:
                spacing 60

                text "音效音量:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "sound_volume")

            hbox:
                spacing 60

                text "全屏模式:" size 24 color "#f5f5f5"
                textbutton _("切换"):
                    action ToggleField(_preferences, "fullscreen")
                    text_style "preferences_button"

            null height 20

            textbutton _("返回"):
                action Return()
                text_style "preferences_button"

style preferences_button:
    size 24
    color "#f5f5f5"
    hover_color "#e8a87c"

# =============================================================================
# 制作人员界面
# =============================================================================

screen about():
    modal True
    tag menu

    add Solid("#000000")

    frame:
        align (0.5, 0.5)
        background Solid("#16213e")
        padding (50, 40, 50, 40)

        vbox:
            spacing 15
            align (0.5, 0.5)

            text "{b}{size=+10}重生·轻逆袭{/size}{/b}":
                color "#f5f5f5"
                text_align 0.5

            text "{size=-5}Re: Second Chance{/size}":
                color "#a0a0a0"
                text_align 0.5

            null height 20

            text "{b}制作团队{/b}":
                size 24
                color "#e8a87c"
                text_align 0.5

            text "制作人: wangjinman":
                size 20
                color "#f5f5f5"
                text_align 0.5

            text "使用 Ren'Py 引擎开发":
                size 18
                color "#a0a0a0"
                text_align 0.5

            null height 30

            textbutton _("返回"):
                action Return()
                text_style "preferences_button"

# =============================================================================
# Yes/No 确认对话框（必须定义）
# =============================================================================

screen yesno_prompt:
    modal True

    frame:
        at popup_appear
        align (0.5, 0.5)
        background Solid("#1a1a2e")
        padding (40, 30, 40, 30)

        vbox:
            spacing 60
            align (0.5, 0.5)

            text "{b}[yesno_prompt_title]{/b}":
                size 28
                color "#f5f5f5"
                text_align 0.5

            text "[yesno_prompt_message]":
                size 22
                color "#a0a0a0"
                text_align 0.5

            null height 15

            hbox:
                spacing 30
                align (0.5, 0.5)

                textbutton _("是"):
                    action yesno_action
                    text_style "yesno_button"

                textbutton _("否"):
                    action Return()
                    text_style "yesno_button"

style yesno_button:
    size 24
    color "#f5f5f5"
    hover_color "#e8a87c"
    text_align 0.5

# =============================================================================
# 确认对话框（用于退出等操作）
# =============================================================================

screen confirm(message, yes_action, no_action):
    modal True

    frame:
        align (0.5, 0.5)
        background Solid("#1a1a2e")
        padding (40, 30, 40, 30)

        vbox:
            spacing 60
            align (0.5, 0.5)

            text "{b}[message]{/b}":
                size 28
                color "#f5f5f5"
                text_align 0.5

            null height 15

            hbox:
                spacing 30
                align (0.5, 0.5)

                textbutton _("是"):
                    action yes_action
                    text_style "yesno_button"

                textbutton _("否"):
                    action no_action
                    text_style "yesno_button"
