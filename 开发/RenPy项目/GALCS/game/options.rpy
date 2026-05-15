# =============================================================================
# options.rpy - 游戏配置选项
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

# 基础信息
define config.name = _("重生·轻逆袭")
define config.version = "0.1.0"

define gui.show_name = True

# 窗口设置
define config.window_title = "重生·轻逆袭"

# 存档设置
define config.save_directory = "ReSecondChance"

# 自动存档
define config.autosave_on_quit = True
define config.autosave_slots = 3

# 回滚设置
define config.rollback_enabled = True
define config.rollback_length = 200

# 跳过设置
define config.skip_indicator = True

# 性能设置
define config.image_cache_size = 64

# 默认设置
define config.default_afm_enable = False
define config.default_afm_time = 15

# 屏幕布局
define config.screen_width = 1920
define config.screen_height = 1080
