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

    # 角色专属对话框映射
    # 林晚棠 - 暖橙边框专属UI
    DIALOGUE_BOXES = {
        "林晚棠": "images/UI/UI_02_lwt_dialogue_box.png",
    }

    # 获取对话背景图片
    def get_dialogue_bg(who):
        if who and who in DIALOGUE_BOXES:
            return DIALOGUE_BOXES[who]
        return "images/UI/UI_01_dialogue_box.png"

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
# 对话框样式覆盖 - 使用自定义UI组件
# 支持角色专属对话框
# =============================================================================
# 屏幕 1920x1080
# UI_01 尺寸 1920x350，内容从顶部开始
# UI_02 尺寸 1920x440，内容从 y=42 开始（顶部42px透明）

screen say(who, what):
    # 根据角色选择对话框背景
    $ bg_img = get_dialogue_bg(who)
    $ is_lwt = who and who in DIALOGUE_BOXES
    # 所有对话框高度统一为440px
    $ box_height = 440
    # 文字区域y坐标：UI_01内容从y=90开始，UI_02内容从y=42开始
    # 文字区域y坐标：UI_01内容从y=90(屏幕730)，UI_02内容从y=42(屏幕682)
    $ text_ypos = 960

    # 对话框图片 - 贴底显示
    add bg_img:
        xalign 0.5
        ypos 1080 - box_height

    # 文字内容窗口
    window:
        id "window"
        background None
        xfill True
        ypos text_ypos
        ymaximum 400
        padding (350, 60, 100, 50)

        has vbox
        spacing 10

        if who:
            text who id "who":
                size 26
                color "#2c3e50"
                font "fonts/SourceHanSansLite.ttf"
                yoffset -20

        text what id "what":
            size 32
            color "#2c3e50"
            font "fonts/SourceHanSansLite.ttf"

    use quick_menu

# =============================================================================
# 快速菜单（对话框下方的快捷操作）
# =============================================================================

screen quick_menu():
    if quick_menu:
        frame:
            style "quick_menu_frame"

            hbox:
                spacing 20

                textbutton _("回滚"):
                    action Rollback()
                    text_style "quick_menu_button"

                textbutton _("自动"):
                    action ui.callsinnewcontext("toggle_auto_forward")
                    text_style "quick_menu_button"

                textbutton _("跳过"):
                    action Skip()
                    text_style "quick_menu_button"

                textbutton _("保存"):
                    action ShowMenu('save')
                    text_style "quick_menu_button"

                textbutton _("读取"):
                    action ShowMenu('load')
                    text_style "quick_menu_button"

                textbutton _("设置"):
                    action ShowMenu('preferences')
                    text_style "quick_menu_button"

style quick_menu_frame:
    xalign 0.5
    yalign 1.0
    yoffset -60  # 调整到底栏上方
    padding (10, 10, 10, 10)
    background Solid("#1a1a2e")

style quick_menu_button:
    size 20
    color "#f5f5f5"
    hover_color "#e8a87c"
    insensitive_color "#606060"

# =============================================================================
# 选择菜单样式
# =============================================================================

screen choice(items):
    modal True
    zorder 100

    frame:
        background Solid("#2d2d4a")
        padding (40, 30, 40, 30)
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 20
            for caption, action, chosen in items:
                if action:
                    textbutton caption:
                        action action
                        text_size 28
                        text_color "#ffffff"
                        text_hover_color "#e8a87c"
                        text_bold False
                        xalign 0.5
                        padding (20, 15, 20, 15)
                        background Solid("#3d3d5c")
                        hover_background Solid("#e8a87c")
                else:
                    text caption:
                        size 28
                        color "#888888"

# =============================================================================
# 主菜单
# =============================================================================

screen main_menu():
    add Solid("#1a1a2e")

    vbox:
        align (0.5, 0.3)
        spacing 20

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
            spacing 20

            text "{b}游戏设置{/b}":
                size 32
                color "#f5f5f5"
                xalign 0.5

            null height 20

            hbox:
                spacing 20

                text "文字速度:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "text_cps", range=100)

            hbox:
                spacing 20

                text "自动播放:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "auto_forward_after", range=30)

            hbox:
                spacing 20

                text "音乐音量:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "music_volume")

            hbox:
                spacing 20

                text "音效音量:" size 24 color "#f5f5f5"
                bar value FieldValue(_preferences, "sound_volume")

            hbox:
                spacing 20

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
            spacing 20
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
            spacing 20
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
