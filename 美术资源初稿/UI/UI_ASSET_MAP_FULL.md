# UI 功能对标表（完整版）

> **生成日期**：2026-05-19  
> **用途**：对照第三方 UI 包的**功能覆盖面**，映射到本项目原创 `UI_DS_*` 资源。  
> **参考包路径**（只读、非商用）：`J:\项目\GAL\美术素材\免费UI仓库\LLFs-FVNUIDP\[251207]青春校园类型 - Youth campus genre\english`  
> **交付路径**：`J:\项目\GAL\美术资源初稿\UI\`  
> **尺寸规格**：所有「尺寸」列与 **`UI_SPEC.md`** 同步；全局底栏 **1920×360**，选项 **780×76**，分辨率 **1920×1080**。

---

## 法律与制作原则

| 规则 | 说明 |
|------|------|
| 参考包 | **不得**放入 `game/`，**不得**作为 AI 参考图 |
| 参考文件名 | 仅用于查漏，不代表要画成一样 |
| 新资源 | 遵循 `UI_DESIGN_SYSTEM.md` |
| 商用 | 全部 `UI_DS_*` 须为原创或自有版权 |

---

## 进度总览

| 状态 | 数量 |
|------|------|
| done | 6 |
| pending | 91 |
| skip | 2 |
| optional | 1 |
| **合计** | 100 |

| 阶段 | 范围 |
|------|------|
| **P0** | 对话、旁白、选项、确认、快捷条、输入 |
| **P1** | 主菜单、quick 图标 |
| **P2** | 游戏菜单、存读档、翻页、滚动条 |
| **P3** | 设置、历史、画廊 |

---

## 命名规范

```
UI_DS_{域}_{部件}_{状态}.png
```

状态：`default` / `hover` / `selected` / `disabled`。

---

## 逐条对标表

| 模块 | 参考文件名 | Ren'Py 绑定 | 目标 `UI_DS_*` | 状态 | 阶段 | 尺寸 | 备注 |
|------|------------|-------------|----------------|------|------|------|------|
| say | `say_adv_say_window_llf.png` | screen say (who!=None) | `UI_DS_bar_dialogue.png` | **done** | P0 | 1920x360 | 已有；立绘独立 show |
| say | `say_adv_say_window_adornment_llf.png` | screen say 装饰层 | `—` | **skip** | P0 | — | 极简风不单独做角花 |
| say | `say_nvl_say_window_llf.png` | screen say (NVL) | `UI_DS_bar_narration.png` | **done** | P0 | 1920x360 | 已有 |
| say | `say_menu_box_default_llf.png` | screen choice | `UI_DS_choice_normal.png` | **done** | P0 | 780x76 | 已有 |
| say | `say_menu_box_hover_llf.png` | screen choice | `UI_DS_choice_hover.png` | **done** | P0 | 780x76 | 已有 |
| say | `say_auto_default_llf.png` | quick_menu auto | `UI_DS_quick_auto_default.png` | **pending** | P0 | 48x48 |  |
| say | `say_auto_hover_llf.png` | quick_menu auto | `UI_DS_quick_auto_hover.png` | **pending** | P0 | 48x48 |  |
| say | `say_skip_default_llf.png` | quick_menu skip | `UI_DS_quick_skip_default.png` | **pending** | P0 | 48x48 |  |
| say | `say_skip_hover_llf.png` | quick_menu skip | `UI_DS_quick_skip_hover.png` | **pending** | P0 | 48x48 |  |
| say | `say_hide_window_default_llf.png` | quick_menu hide | `UI_DS_quick_hide_default.png` | **pending** | P0 | 48x48 |  |
| say | `say_hide_window_hover_llf.png` | quick_menu hide | `UI_DS_quick_hide_hover.png` | **pending** | P0 | 48x48 |  |
| say | `say_history_default_llf.png` | quick_menu history | `UI_DS_quick_history_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_history_hover_llf.png` | quick_menu history | `UI_DS_quick_history_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_save_data_default_llf.png` | quick_menu save | `UI_DS_quick_save_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_save_data_hover_llf.png` | quick_menu save | `UI_DS_quick_save_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_load_data_default_llf.png` | quick_menu load | `UI_DS_quick_load_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_load_data_hover_llf.png` | quick_menu load | `UI_DS_quick_load_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_settings_default_llf.png` | quick_menu prefs | `UI_DS_quick_settings_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_settings_hover_llf.png` | quick_menu prefs | `UI_DS_quick_settings_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_exit_default_llf.png` | return main menu | `UI_DS_quick_exit_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_exit_hover_llf.png` | return main menu | `UI_DS_quick_exit_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_quick_menu_background_llf.png` | screen quick_menu | `UI_DS_quick_bar.png` | **pending** | P0 | 1920x56 | 横条半透明 |
| say | `say_quick_save_default_llf.png` | quick_menu | `UI_DS_quick_save_default.png` | **pending** | P1 | 48x48 | 与 save 合并风格 |
| say | `say_quick_save_hover_llf.png` | quick_menu | `UI_DS_quick_save_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_quick_load_default_llf.png` | quick_menu | `UI_DS_quick_load_default.png` | **pending** | P1 | 48x48 |  |
| say | `say_quick_load_hover_llf.png` | quick_menu | `UI_DS_quick_load_hover.png` | **pending** | P1 | 48x48 |  |
| say | `say_replay_voice_default_llf.png` | say voice replay | `UI_DS_say_voice_default.png` | **pending** | P3 | 40x40 |  |
| say | `say_replay_voice_hover_llf.png` | say voice replay | `UI_DS_say_voice_hover.png` | **pending** | P3 | 40x40 |  |
| say | `(derived)` | screen choice selected | `UI_DS_choice_selected.png` | **done** | P0 | 780x76 | 参考包无 selected；DS 已补 |
| title | `title_background_mask_llf.png` | screen main_menu | `UI_DS_title_bg_mask.png` | **pending** | P1 | 1920x1080 | 暗角渐隐 |
| title | `title_start_game_default_llf.png` | main_menu start | `UI_DS_title_btn_start_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_start_game_hover_llf.png` | main_menu start | `UI_DS_title_btn_start_hover.png` | **pending** | P1 | 520x72 |  |
| title | `title_load_data_default_llf.png` | main_menu load | `UI_DS_title_btn_load_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_load_data_hover_llf.png` | main_menu load | `UI_DS_title_btn_load_hover.png` | **pending** | P1 | 520x72 |  |
| title | `title_game_settings_default_llf.png` | main_menu prefs | `UI_DS_title_btn_prefs_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_game_settings_hover_llf.png` | main_menu prefs | `UI_DS_title_btn_prefs_hover.png` | **pending** | P1 | 520x72 |  |
| title | `title_art_gallery_default_llf.png` | main_menu gallery | `UI_DS_title_btn_gallery_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_art_gallery_hover_llf.png` | main_menu gallery | `UI_DS_title_btn_gallery_hover.png` | **pending** | P1 | 520x72 |  |
| title | `title_adout_game_default_llf.png` | main_menu about | `UI_DS_title_btn_about_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_adout_game_hover_llf.png` | main_menu about | `UI_DS_title_btn_about_hover.png` | **pending** | P1 | 520x72 |  |
| title | `title_exit_game_default_llf.png` | main_menu quit | `UI_DS_title_btn_quit_default.png` | **pending** | P1 | 520x72 |  |
| title | `title_exit_game_hover_llf.png` | main_menu quit | `UI_DS_title_btn_quit_hover.png` | **pending** | P1 | 520x72 |  |
| common | `common_screen_background_llf.png` | screen game_menu | `UI_DS_menu_bg.png` | **pending** | P2 | 1920x1080 |  |
| common | `common_title_screen_default_llf.png` | game_menu tab | `UI_DS_menu_tab_default.png` | **pending** | P2 | 280x48 |  |
| common | `common_title_screen_hover_llf.png` | game_menu tab | `UI_DS_menu_tab_hover.png` | **pending** | P2 | 280x48 |  |
| common | `common_save_data_default_llf.png` | navigation save | `UI_DS_menu_icon_save_default.png` | **pending** | P2 | 48x48 |  |
| common | `common_save_data_hover_llf.png` | navigation save | `UI_DS_menu_icon_save_hover.png` | **pending** | P2 | 48x48 |  |
| common | `common_load_data_default_llf.png` | navigation load | `UI_DS_menu_icon_load_default.png` | **pending** | P2 | 48x48 |  |
| common | `common_load_data_hover_llf.png` | navigation load | `UI_DS_menu_icon_load_hover.png` | **pending** | P2 | 48x48 |  |
| common | `common_title_save_data_llf.png` | menu heading | `UI_DS_menu_heading_save.png` | **pending** | P2 | — | 可选 |
| common | `common_title_load_data_llf.png` | menu heading | `UI_DS_menu_heading_load.png` | **pending** | P2 | — | 可选 |
| common | `common_title_game_settings_llf.png` | menu heading | `UI_DS_menu_heading_prefs.png` | **pending** | P2 | — | 可选 |
| common | `common_title_history_llf.png` | menu heading | `UI_DS_menu_heading_history.png` | **pending** | P2 | — | 可选 |
| common | `common_title_art_gallery_llf.png` | menu heading | `UI_DS_menu_heading_gallery.png` | **pending** | P2 | — | 可选 |
| common | `common_title_about_game_llf.png` | menu heading | `UI_DS_menu_heading_about.png` | **pending** | P2 | — | 可选 |
| common | `common_left_page_default_llf.png` | save/load page | `UI_DS_common_page_prev_default.png` | **pending** | P2 | 64x64 |  |
| common | `common_left_page_hover_llf.png` | save/load page | `UI_DS_common_page_prev_hover.png` | **pending** | P2 | 64x64 |  |
| common | `common_right_page_default_llf.png` | save/load page | `UI_DS_common_page_next_default.png` | **pending** | P2 | 64x64 |  |
| common | `common_right_page_hover_llf.png` | save/load page | `UI_DS_common_page_next_hover.png` | **pending** | P2 | 64x64 |  |
| common | `common_page_default_llf.png` | page dot | `UI_DS_common_dot_default.png` | **pending** | P2 | 24x24 |  |
| common | `common_page_hover_llf.png` | page dot | `UI_DS_common_dot_hover.png` | **pending** | P2 | 24x24 |  |
| common | `common_page_selected_llf.png` | page dot | `UI_DS_common_dot_selected.png` | **pending** | P2 | 24x24 |  |
| common | `common_slider_default_llf.png` | vbar thumb | `UI_DS_common_vthumb_default.png` | **pending** | P2 | 16x80 |  |
| common | `common_slider_hover_llf.png` | vbar thumb | `UI_DS_common_vthumb_hover.png` | **pending** | P2 | 16x80 |  |
| common | `common_vbar_top_llf.png` | vbar top | `UI_DS_common_vbar_top.png` | **pending** | P2 | 12x40 |  |
| common | `common_vbar_bottom_llf.png` | vbar bottom | `UI_DS_common_vbar_bottom.png` | **pending** | P2 | 12x40 |  |
| common | `common_close_screen_default_llf.png` | close menu | `UI_DS_common_close_default.png` | **pending** | P2 | 48x48 |  |
| common | `common_close_screen_hover_llf.png` | close menu | `UI_DS_common_close_hover.png` | **pending** | P2 | 48x48 |  |
| data | `data_data_box_default_llf.png` | screen save/load | `UI_DS_data_slot_default.png` | **pending** | P2 | 420x240 |  |
| data | `data_data_box_hover_llf.png` | screen save/load | `UI_DS_data_slot_hover.png` | **pending** | P2 | 420x240 |  |
| data | `data_data_message_box_llf.png` | slot label | `UI_DS_data_slot_label.png` | **pending** | P2 | 400x56 |  |
| data | `data_temporary_image_default_llf.png` | empty slot | `UI_DS_data_slot_empty_default.png` | **pending** | P2 | 420x240 |  |
| data | `data_temporary_image_hover_llf.png` | empty slot | `UI_DS_data_slot_empty_hover.png` | **pending** | P2 | 420x240 |  |
| data | `data_new_sign_llf.png` | new save badge | `UI_DS_data_badge_new.png` | **pending** | P2 | 64x64 |  |
| data | `data_delete_data_default_llf.png` | delete slot | `UI_DS_data_btn_delete_default.png` | **pending** | P2 | 120x48 |  |
| data | `data_delete_data_hover_llf.png` | delete slot | `UI_DS_data_btn_delete_hover.png` | **pending** | P2 | 120x48 |  |
| confirm | `confirm_background_llf.png` | screen confirm | `UI_DS_confirm_scrim.png` | **pending** | P0 | 1920x1080 |  |
| confirm | `confirm_confirm_window_llf.png` | screen confirm | `UI_DS_confirm_panel.png` | **pending** | P0 | 720x360 |  |
| confirm | `confirm_button_default_llf.png` | screen confirm | `UI_DS_confirm_btn_default.png` | **pending** | P0 | 200x64 |  |
| confirm | `confirm_button_hover_llf.png` | screen confirm | `UI_DS_confirm_btn_hover.png` | **pending** | P0 | 200x64 |  |
| settings | `settings_project_title_box_llf.png` | preferences | `UI_DS_settings_section.png` | **pending** | P3 | 600x40 |  |
| settings | `settings_divider_llf.png` | preferences | `UI_DS_settings_divider.png` | **pending** | P3 | 600x2 |  |
| settings | `settings_slider_default_llf.png` | preferences slider | `UI_DS_settings_hthumb_default.png` | **pending** | P3 | 120x24 |  |
| settings | `settings_slider_hover_llf.png` | preferences slider | `UI_DS_settings_hthumb_hover.png` | **pending** | P3 | 120x24 |  |
| settings | `settings_bar_top_llf.png` | slider track | `UI_DS_settings_hbar.png` | **pending** | P3 | 400x8 |  |
| settings | `settings_bar_bottom_llf.png` | slider track | `—` | **skip** | P3 | — | 与 top 合并 |
| settings | `settings_button_hover_sign_llf.png` | toggle hover | `UI_DS_settings_toggle_hover.png` | **pending** | P3 | 32x32 |  |
| settings | `settings_speed_alpha_test_box_llf.png` | speed preview | `UI_DS_settings_preview_box.png` | **pending** | P3 | 480x120 |  |
| history | `history_headshot_box_llf.png` | screen history | `UI_DS_history_avatar_frame.png` | **pending** | P3 | 80x80 |  |
| history | `history_replay_say_one_line_llf.png` | history line | `UI_DS_history_line_1.png` | **pending** | P3 | 1600x48 |  |
| history | `history_replay_say_two_line_llf.png` | history line | `UI_DS_history_line_2.png` | **pending** | P3 | 1600x72 |  |
| history | `history_replay_say_three_line_llf.png` | history line | `UI_DS_history_line_3.png` | **pending** | P3 | 1600x96 |  |
| history | `history_replay_voice_default_llf.png` | history voice | `UI_DS_history_voice_default.png` | **pending** | P3 | 40x40 |  |
| history | `history_replay_voice_hover_llf.png` | history voice | `UI_DS_history_voice_hover.png` | **pending** | P3 | 40x40 |  |
| gallery | `gallery_image_box_default_llf.png` | screen gallery | `UI_DS_gallery_frame_default.png` | **pending** | P3 | 320x180 |  |
| gallery | `gallery_image_box_hover_llf.png` | screen gallery | `UI_DS_gallery_frame_hover.png` | **pending** | P3 | 320x180 |  |
| gallery | `gallery_temporary_image_llf.png` | gallery locked | `UI_DS_gallery_locked.png` | **pending** | P3 | 320x180 |  |
| — | `(Ren'Py)` | screen input | `UI_DS_input_panel.png` | **pending** | P0 | 720x280 | 姓名输入 |
| — | `(Ren'Py)` | screen notify | `UI_DS_notify_bg.png` | **optional** | G | — | toast |
| — | `(Ren'Py)` | nameplate | `UI_DS_nameplate.png` | **done** | P0 | 320x44 | 已有 |

---

## 模块统计（参考包 96 PNG）

| 模块 | 参考包数量 |
|------|------------|
| say | 28 |
| title | 13 |
| common | 26 |
| data | 8 |
| confirm | 4 |
| settings | 8 |
| history | 6 |
| gallery | 3 |

---

*配套：`RENPY_UI_COMPLETE_CHECKLIST.md` · Skill `renpy-galgame-ui`*
