# -*- coding: utf-8 -*-
# GAL · UI Design System v1 — paste into gui.rpy / screens.rpy
# Assets: UI/UI_DS_*.png
# Spec: UI/UI_SPEC.md (1920x360 bar, 780x76 choice) + UI_DESIGN_SYSTEM.md

## Sizes — must match UI_SPEC.md
define gui.textbox_height = 360
define gui.name_xpos = 400
define gui.name_ypos = -330
define gui.dialogue_xpos = 400
define gui.dialogue_ypos = -280
define gui.dialogue_width = 1420

define gui.choice_button_width = 780
define gui.choice_button_height = 76

## Colors (hex) — Light theme v1.1
define gui.text_color = "#3A4258"
define gui.interface_text_color = "#3A4258"
define gui.accent_color = "#C97B35"
define gui.idle_color = "#6B7589"

define gui.choice_button_text_idle_color = "#3A4258"
define gui.choice_button_text_hover_color = "#B86A28"
define gui.choice_button_text_insensitive_color = "#9AA3B5"

## Fonts — adjust to your bundled font
define gui.text_font = "SourceHanSansCN-Regular.otf"
define gui.name_text_font = gui.text_font
define gui.interface_text_font = gui.text_font
define gui.choice_button_text_font = gui.text_font

define gui.name_text_size = 26
define gui.text_size = 22
define gui.choice_button_text_size = 22

## Choice screen example
# screen choice(items):
#     style_prefix "choice"
#     vbox:
#         xalign 0.5
#         yalign 0.5
#         spacing 14
#         for i in items:
#             textbutton i.caption:
#                 action i.action
#                 idle_background "UI/UI_DS_choice_normal.png"
#                 hover_background "UI/UI_DS_choice_hover.png"
#                 selected_idle_background "UI_DS_choice_selected.png"
#                 selected_hover_background "UI_DS_choice_selected.png"
#                 xsize 780
#                 ysize 76

## Say screen — use bar + separate portrait (not baked UI_02)
# screen say(who, what):
#     if who:
#         add "UI/UI_DS_bar_dialogue.png" xalign 0.5 yalign 1.0
#         # show lin at portrait position
#     else:
#         add "UI/UI_DS_bar_narration.png" xalign 0.5 yalign 1.0

## Quick menu (say 模块) — 1920x56 顶条 + 48x48 图标
# screen quick_menu():
#     zorder 100
#     if quick_menu:
#         add "UI/UI_DS_quick_bar.png" xalign 0.5 yalign 0.0
#         hbox:
#             xalign 0.98
#             yalign 0.0
#             yoffset 4
#             spacing 6
#             textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True):
#                 style "quick_button"
#                 idle_background "UI/UI_DS_quick_skip_default.png"
#                 hover_background "UI/UI_DS_quick_skip_hover.png"
#                 xsize 48 ysize 48
#             textbutton _("Auto") action Preference("auto-forward", "toggle"):
#                 style "quick_button"
#                 idle_background "UI/UI_DS_quick_auto_default.png"
#                 hover_background "UI/UI_DS_quick_auto_hover.png"
#                 xsize 48 ysize 48
#             # history / save / load / settings / hide / exit 同理
