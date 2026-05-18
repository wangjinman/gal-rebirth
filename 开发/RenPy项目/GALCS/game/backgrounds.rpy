# =============================================================================
# backgrounds.rpy - 背景图定义与别名
# 《重生·轻逆袭》(Re: Second Chance)
#
# 定义背景图别名，让剧本中的引用更清晰
# =============================================================================

# Ren'Py会自动将 images/ 目录下的文件映射为场景标签
# 例如: images/backgrounds/BG_01_classroom_day.png → scene bg classroom_day
#
# 这里定义一些别名，让代码更易读

# =============================================================================
# 第一章常用背景
# =============================================================================

# 教室 - 日间
define bg classroom_day = "bg classroom_day"

# 教室 - 黄昏
define bg classroom_sunset = "bg classroom_sunset"

# 卧室
define bg bedroom = "bg bedroom"

# 街道 - 雨天
define bg street_rain = "bg street_rain"

# 天台 - 金色黄昏
define bg rooftop_sunset = "bg rooftop_sunset"

# =============================================================================
# 林晚棠线背景
# =============================================================================

# 图书馆 - 日间
define bg library = "bg library"

# 走廊 - 午后
define bg corridor = "bg corridor"

# 公园长椅 - 黄昏
define bg park = "bg park_bench_sunset"

# 咖啡馆 - 黄昏
define bg cafe = "bg cafe_sunset"

# =============================================================================
# 背景图对照表
# =============================================================================
#
# 文件名 → 代码引用
# ----------------------------------------
# BG_01_classroom_day.png    → bg classroom_day
# BG_02_classroom_sunset.png → bg classroom_sunset
# BG_03_bedroom.png          → bg bedroom
# BG_04_rooftop_sunset_golden.png → bg rooftop_sunset
# BG_05_library_day.png      → bg library
# BG_06_corridor_afternoon.png → bg corridor
# BG_07_park_bench_sunset.png → bg park
# BG_08_cafe_sunset.png      → bg cafe
#
