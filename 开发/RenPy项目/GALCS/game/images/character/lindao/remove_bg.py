from PIL import Image
import os

# 立绘目录
input_dir = os.path.dirname(os.path.abspath(__file__))

# 支持的文件格式
extensions = ['.png', '.jpg', '.jpeg', '.webp']

# 白色容差 (0-255)，值越大越宽容
threshold = 30

def remove_white_background(input_path, output_path):
    """移除白色背景，转为透明"""
    img = Image.open(input_path)

    # 转为 RGBA 模式
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # 获取像素数据
    data = img.getdata()

    new_data = []
    for item in data:
        r, g, b, a = item

        # 如果像素接近白色（RGB都大于 255-threshold），设为透明
        if r > (255 - threshold) and g > (255 - threshold) and b > (255 - threshold):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, 'PNG')
    print(f"处理完成: {os.path.basename(output_path)}")

# 处理所有图片
for filename in os.listdir(input_dir):
    if filename.lower().endswith(tuple(extensions)) and 'remove_bg' not in filename:
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(input_dir, filename)
        remove_white_background(input_path, output_path)

print("所有图片处理完成！")
