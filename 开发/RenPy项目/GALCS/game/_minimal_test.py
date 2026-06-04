import sys

with open("J:/项目/GAL/开发/RenPy项目/GALCS/game/screens.rpy", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 找 load_save_screen 范围
start = None
end = None
for i, line in enumerate(lines):
    if start is None and 'screen load_save_screen(which):' in line:
        start = i
    elif start is not None and end is None:
        stripped = line.strip()
        if stripped.startswith('screen ') or stripped.startswith('init '):
            end = i
            break

if start is None:
    print("ERROR: 找不到 load_save_screen")
    sys.exit(1)
if end is None:
    end = len(lines)

print(f"load_save_screen: 行{start+1} ~ 行{end}")

new_screen = '''screen load_save_screen(which):
    modal True
    tag menu
    zorder 150

    vbox:
        spacing 0

        # 标题栏
        frame:
            xfill True
            ysize 72
            background Solid("#00000088")
            padding (100, 0, 40, 0)
            hbox:
                yalign 0.5
                textbutton "← 返回":
                    action Hide("load_save_screen")
                    text_style "data_back_button"
                text "[which]":
                    size 32
                    color "#f0f0f0"
                    xpos 30

    # 存档槽区域（简化测试：不用 grid，直接 vbox）
    frame:
        xalign 0.5
        xsize 1350
        ysize 980
        background None
        padding (40, 30, 40, 30)

        vbox:
            xalign 0.5
            spacing 28

            # 只显示第一个槽做测试
            $ slot_num = 1

            if FileLoadable(slot_num):
                # 有存档：imagebutton + Solid 色
                imagebutton:
                    xsize 380
                    ysize 228
                    idle FileScreenshot(slot_num, empty=Null())
                    hover Fixed(FileScreenshot(slot_num, empty=Null()), Solid((255, 100, 100, 160)))
                    action FileAction(slot_num)
                    # 信息条叠在截图上
                    vbox:
                        yalign 1.0
                        frame:
                            xfill True
                            background Solid("#00000099")
                            padding (14, 6, 14, 6)
                            vbox:
                                spacing 2
                                text FileSaveName(slot_num, empty=""):
                                    size 20
                                    color "#f0f0f0"
                                text FileTime(slot_num, format="%Y/%m/%d %H:%M", empty=""):
                                    size 15
                                    color "#cccccc"
            else:
                # 空槽测试
                imagebutton:
                    xsize 380
                    ysize 228
                    idle Solid("#3a3a5e")
                    hover Solid("#e8a87c")
                    action FileAction(slot_num)
                    text "空槽测试":
                        size 28
                        color "#ffffff"
                        xalign 0.5
                        yalign 0.5

'''

lines[start:end] = new_screen.splitlines(keepends=True)

with open("J:/项目/GAL/开发/RenPy项目/GALCS/game/screens.rpy", "w", encoding="utf-8") as f:
    f.writelines(lines)

print(f"写入成功，新行数：{len(new_screen.splitlines())}")
print("验证：")
with open("J:/项目/GAL/开发/RenPy项目/GALCS/game/screens.rpy", "r", encoding="utf-8") as f:
    c = f.read()
print("  imagebutton 存在：", "imagebutton:" in c)
print("  Solid 存在：", "Solid(" in c)
print("  FileScreenshot 存在：", "FileScreenshot" in c)
