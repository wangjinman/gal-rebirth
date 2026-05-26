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
# 文本框样式（由 screens.rpy 自定义 say screen 完全接管）
# 此处仅保留最小值避免冲突
# =============================================================================

# 文本框高度（设为0，由自定义say screen控制布局）
define gui.textbox_height = 0

# 对话框窗口背景（设为透明，不覆盖自定义对话框图片）
define gui.window_background = None

# 角色名位置（由自定义say screen控制）
define gui.name_xpos = 0
define gui.name_ypos = 0
define gui.name_yalign = 0.0

# 输入提示文字颜色
define gui.input_color = '#ffffff'

# 对话框文字颜色
define gui.who_color = '#2c3e50'
define gui.what_color = '#2c3e50'

# 文本框位置偏移（设为0，由自定义say screen的绝对坐标控制）
define gui.text_xpos = 0
define gui.text_ypos = 0
