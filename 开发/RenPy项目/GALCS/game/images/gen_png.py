# -*- coding: utf-8 -*-
"""
生成简单的PNG占位符图片
"""
import zlib
import struct
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
bg_dir = os.path.join(script_dir, 'backgrounds')
char_dir = os.path.join(script_dir, 'characters')

os.makedirs(bg_dir, exist_ok=True)
os.makedirs(char_dir, exist_ok=True)

def create_png(width, height, color_rgb, filepath):
    """创建一个简单的纯色PNG图片"""
    r, g, b = color_rgb
    
    def png_chunk(chunk_type, data):
        chunk = chunk_type + data
        crc = zlib.crc32(chunk) & 0xffffffff
        return struct.pack('>I', len(data)) + chunk + struct.pack('>I', crc)
    
    signature = b'\x89PNG\r\n\x1a\n'
    ihdr_data = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    ihdr = png_chunk(b'IHDR', ihdr_data)
    
    raw_data = b''
    for y in range(height):
        raw_data += b'\x00'
        for x in range(width):
            raw_data += bytes([r, g, b])
    
    compressed = zlib.compress(raw_data, 9)
    idat = png_chunk(b'IDAT', compressed)
    iend = png_chunk(b'IEND', b'')
    
    with open(filepath, 'wb') as f:
        f.write(signature + ihdr + idat + iend)
    
    print(f"Created: {os.path.basename(filepath)} ({width}x{height})")

print("Creating backgrounds...")
create_png(1920, 1080, (26, 26, 46), os.path.join(bg_dir, 'main_menu.png'))
create_png(1920, 1080, (0, 0, 0), os.path.join(bg_dir, 'black.png'))
create_png(1920, 1080, (45, 58, 74), os.path.join(bg_dir, 'classroom.png'))
create_png(1920, 1080, (58, 58, 74), os.path.join(bg_dir, 'room.png'))
create_png(1920, 1080, (74, 74, 90), os.path.join(bg_dir, 'hallway.png'))

print("\nCreating characters...")
create_png(800, 1200, (232, 168, 124), os.path.join(char_dir, 'lindao_normal.png'))
create_png(800, 1200, (192, 133, 155), os.path.join(char_dir, 'suni_normal.png'))
create_png(800, 1200, (125, 216, 125), os.path.join(char_dir, 'zhou_normal.png'))
create_png(800, 1200, (107, 107, 171), os.path.join(char_dir, 'chen_normal.png'))
create_png(800, 1200, (155, 155, 203), os.path.join(char_dir, 'shen_normal.png'))

print("\nDone!")
