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
