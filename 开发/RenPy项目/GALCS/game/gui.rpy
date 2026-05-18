# =============================================================================
# gui.rpy - GUI配置
# 《重生·轻逆袭》(Re: Second Chance)
# =============================================================================

# 使用黑体字体（支持中文）
define gui.font = "fonts/simhei.ttf"
define gui.small_font = "fonts/simhei.ttf"
define gui.name_font = "fonts/simhei.ttf"
define gui.interface_font = "fonts/simhei.ttf"

# 界面颜色
define gui.accent_color = '#e8a87c'
define gui.hover_color = '#f0b88c'
define gui.insensitive_color = '#606060'
define gui.text_color = '#f5f5f5'
define gui.idle_text_color = '#a0a0a0'
define gui.hover_text_color = '#f0b88c'
define gui.interface_color = '#f5f5f5'

# 对话框样式
init python:
    # 为默认样式设置中文字体
    style.default.font = "fonts/simhei.ttf"

# =============================================================================
# 菜单按钮样式（在 screens.rpy 中自定义，此处不覆盖）
# =============================================================================

# =============================================================================
# 文本框样式（确保在黑色背景上清晰可见）
# =============================================================================

# 文本框背景（半透明深色）
define gui.textbox_height = 160
define gui.name_xpos = 40
define gui.name_ypos = -30
define gui.name_yalign = 1.0

# 对话框窗口背景
define gui.window_background = "gui/textbox.png"

# 输入提示文字颜色
define gui.input_color = '#ffffff'

# 对话框文字样式
define gui.who_color = '#ffffff'
define gui.what_color = '#ffffff'

# 文本框位置
define gui.text_xpos = 40
define gui.text_ypos = 60
