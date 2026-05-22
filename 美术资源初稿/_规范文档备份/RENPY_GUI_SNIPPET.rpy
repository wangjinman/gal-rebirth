# -*- coding: utf-8 -*-
# GAL · UI Design System v1 — paste into gui.rpy / screens.rpy
# Assets: UI/UI_DS_*.png  |  Spec: UI/UI_DESIGN_SYSTEM.md

## Sizes
define gui.textbox_height = 168
define gui.name_xpos = 400
define gui.name_ypos = -158
define gui.dialogue_xpos = 400
define gui.dialogue_ypos = -118
define gui.dialogue_width = 1420

define gui.choice_button_width = 780
define gui.choice_button_height = 76

## Colors (hex)
define gui.text_color = "#F4EFE8"
define gui.interface_text_color = "#F4EFE8"
define gui.accent_color = "#E8A05C"
define gui.idle_color = "#B8C0D4"

define gui.choice_button_text_idle_color = "#F4EFE8"
define gui.choice_button_text_hover_color = "#FFD9A8"
define gui.choice_button_text_insensitive_color = "#888898"

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
