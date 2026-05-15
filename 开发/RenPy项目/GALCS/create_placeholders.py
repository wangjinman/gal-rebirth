#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
生成占位图片 - 使用纯Python创建BMP图片（无需Pillow）
"""

import struct
import os

def create_bmp(width, height, color_hex):
    """创建纯色BMP图片"""
    # 解析颜色
    color_hex = color_hex.lstrip('#')
    r = int(color_hex[0:2], 16)
    g = int(color_hex[2:4], 16)
    b = int(color_hex[4:6], 16)
    
    # BMP格式：每行必须是4字节对齐
    row_size = (width * 3 + 3) & ~3
    padding = row_size - width * 3
    
    # 像素数据
    pixel_data = b''
    for y in range(height):
        for x in range(width):
            pixel_data += struct.pack('BBB', b, g, r)
        pixel_data += b'\x00' * padding
    
    # BMP文件头
    file_size = 54 + len(pixel_data)
    header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)
    
    # DIB头 (BITMAPINFOHEADER)
    dib_header = struct.pack('<IiiHHIIiiII',
        40,         # DIB头大小
        width,      # 宽度
        height,     # 高度
        1,          # 颜色平面数
        24,         # 每像素位数
        0,          # 压缩方式
        len(pixel_data),  # 图像大小
        2835,       # 水平分辨率
        2835,       # 垂直分辨率
        0,          # 颜色数
        0           # 重要颜色数
    )
    
    return header + dib_header + pixel_data

def create_gradient_bmp(width, height, color1, color2):
    """创建渐变BMP图片"""
    r1, g1, b1 = int(color1[0:2], 16), int(color1[2:4], 16), int(color1[4:6], 16)
    r2, g2, b2 = int(color2[0:2], 16), int(color2[2:4], 16), int(color2[4:6], 16)
    
    row_size = (width * 3 + 3) & ~3
    padding = row_size - width * 3
    
    pixel_data = b''
    for y in range(height):
        t = y / height
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        
        for x in range(width):
            pixel_data += struct.pack('BBB', b, g, r)
        pixel_data += b'\x00' * padding
    
    file_size = 54 + len(pixel_data)
    header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)
    dib_header = struct.pack('<IiiHHIIiiII', 40, width, height, 1, 24, 0, len(pixel_data), 2835, 2835, 0, 0)
    
    return header + dib_header + pixel_data

def save_bmp(data, filepath):
    """保存BMP文件"""
    with open(filepath, 'wb') as f:
        f.write(data)
    print(f"Created: {filepath}")

# 创建目录
base_dir = '/j/项目/GAL/开发/RenPy项目/GALCS/game/images'
os.makedirs(f'{base_dir}/backgrounds', exist_ok=True)
os.makedirs(f'{base_dir}/characters', exist_ok=True)
os.makedirs(f'{base_dir}/cg', exist_ok=True)

# 1. 主菜单背景 - 深蓝渐变
save_bmp(create_gradient_bmp(1920, 1080, '1a1a2e', '2d4a6f'), 
         f'{base_dir}/backgrounds/main_menu.png')

# 2. 黑色背景
save_bmp(create_bmp(1920, 1080, '000000'), 
         f'{base_dir}/backgrounds/black.png')

# 3. 教室背景
save_bmp(create_bmp(1920, 1080, '2d3a4a'), 
         f'{base_dir}/backgrounds/classroom.png')

# 4. 房间背景
save_bmp(create_bmp(1920, 1080, '3a3a4a'), 
         f'{base_dir}/backgrounds/room.png')

# 5. 走廊背景
save_bmp(create_bmp(1920, 1080, '4a4a5a'), 
         f'{base_dir}/backgrounds/hallway.png')

# 6. 林晚棠立绘占位 (暖橙色)
save_bmp(create_bmp(800, 1200, 'e8a87c'), 
         f'{base_dir}/characters/lindao_normal.png')

# 7. 苏念卿立绘占位 (优雅紫)
save_bmp(create_bmp(800, 1200, 'c0859b'), 
         f'{base_dir}/characters/suni_normal.png')

# 8. 周芷晴立绘占位 (元气绿)
save_bmp(create_bmp(800, 1200, '7dd87d'), 
         f'{base_dir}/characters/zhou_normal.png')

# 9. 陈墨立绘占位 (冷傲紫蓝)
save_bmp(create_bmp(800, 1200, '6b6bab'), 
         f'{base_dir}/characters/chen_normal.png')

# 10. 沈听雨立绘占位 (神秘灰紫)
save_bmp(create_bmp(800, 1200, '9b9bcb'), 
         f'{base_dir}/characters/shen_normal.png')

print("\n✅ 所有占位图片创建完成！")
