#!/usr/bin/env python
# -*- coding: utf-8 -*-
import struct
import os
import sys

def create_bmp_fast(width, height, color_hex):
    """高效创建纯色BMP图片"""
    color_hex = color_hex.lstrip('#')
    r = int(color_hex[0:2], 16)
    g = int(color_hex[2:4], 16)
    b = int(color_hex[4:6], 16)
    
    row_size = (width * 3 + 3) & ~3
    padding = row_size - width * 3
    
    # 创建一行像素数据
    row = struct.pack('BBB', b, g, r) * width + b'\x00' * padding
    # 复制所有行
    pixel_data = row * height
    
    file_size = 54 + len(pixel_data)
    header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, 54)
    dib_header = struct.pack('<IiiHHIIiiII', 40, width, height, 1, 24, 0, len(pixel_data), 2835, 2835, 0, 0)
    
    return header + dib_header + pixel_data

def save_bmp(data, filepath):
    with open(filepath, 'wb') as f:
        f.write(data)
    print(f"Created: {filepath}")

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = script_dir

# 创建目录
os.makedirs(f'{base_dir}/backgrounds', exist_ok=True)
os.makedirs(f'{base_dir}/characters', exist_ok=True)
os.makedirs(f'{base_dir}/cg', exist_ok=True)

print("Generating placeholder images...")

# 背景图片 (1920x1080)
save_bmp(create_bmp_fast(1920, 1080, '1a1a2e'), f'{base_dir}/backgrounds/main_menu.png')
save_bmp(create_bmp_fast(1920, 1080, '000000'), f'{base_dir}/backgrounds/black.png')
save_bmp(create_bmp_fast(1920, 1080, '2d3a4a'), f'{base_dir}/backgrounds/classroom.png')
save_bmp(create_bmp_fast(1920, 1080, '3a3a4a'), f'{base_dir}/backgrounds/room.png')
save_bmp(create_bmp_fast(1920, 1080, '4a4a5a'), f'{base_dir}/backgrounds/hallway.png')

# 角色立绘 (800x1200)
save_bmp(create_bmp_fast(800, 1200, 'e8a87c'), f'{base_dir}/characters/lindao_normal.png')
save_bmp(create_bmp_fast(800, 1200, 'c0859b'), f'{base_dir}/characters/suni_normal.png')
save_bmp(create_bmp_fast(800, 1200, '7dd87d'), f'{base_dir}/characters/zhou_normal.png')
save_bmp(create_bmp_fast(800, 1200, '6b6bab'), f'{base_dir}/characters/chen_normal.png')
save_bmp(create_bmp_fast(800, 1200, '9b9bcb'), f'{base_dir}/characters/shen_normal.png')

print("\nAll placeholder images created successfully!")
