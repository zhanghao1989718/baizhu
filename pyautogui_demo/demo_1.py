# coding = utf-8
import pyautogui

# # 获取屏幕尺寸
# pyautogui.size()
# # 把屏幕尺寸赋予变量（宽，高）
# width, height = pyautogui.size()
# # 打印屏幕尺寸
# print(width,height)



# 鼠标顺时针移动，并划10次方框
# for i in range(10):
#     pyautogui.moveTo(300, 300, duration=0.25)
#     pyautogui.moveTo(400, 300, duration=0.25)
#     pyautogui.moveTo(400, 400, duration=0.25)
#     pyautogui.moveTo(300, 400, duration=0.25)


# 画圆
# from mpmath import math2
# width, height = pyautogui.size()
# r = 250 # 圆的半径
# # 圆心
# o_x = width/2
# o_y = height/2
# pi = 3.1415926
# for i in range(10):  # 转10圈
#     for angle in range(0, 360, 5): # 利用圆的参数方程
#         X = o_x + r * math2.sin(angle*pi/180)
#         Y = o_y + r * math2.cos(angle*pi/180)
#         pyautogui.moveTo(X, Y, duration=0.1)



# 以当前鼠标所在位置为基点
# for i in range(10):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)
#     pyautogui.moveRel(-100, 0, duration=0.25)
#     pyautogui.moveRel(0, -100, duration=0.25)


# # 获得鼠标位置
# x, y = pyautogui.position()
# print(x, y)


# 实时获得鼠标位置
# try:
#     while True:
#         x, y = pyautogui.position()
#         print(x, y)
# except KeyboardInterrupt:
#     print('\nExit.')

# cur_x = 519
# cur_y = 41
# pyautogui.click(x=cur_x, y=cur_y, button='left')
# # x，y是要点击的位置，默认是鼠标当前位置
# # button是要点击的按键，有三个可选值：‘left', ‘middle',  ‘right'。
#
# # 要在当前位置点击右键：
# pyautogui.click(button='right')
#
# # 要在指定位置点击左键：
# pyautogui.click(100, 100)

# 滚轮,使用函数scroll()，它只接受一个整数。如果值为正往上滚，值为负往下滚。
# pyautogui.scroll(1000)

# 截屏判断所在位置的元素，或者截屏判断
# 获得某个坐标的像素
# im = pyautogui.screenshot()
# print(im)
# b = im.getpixel((517, 43))
# print(b)
# # 判断屏幕坐标的像素是不是等于某个值
# a = pyautogui.pixelMatchesColor(517, 43, (165, 186, 186))
# print(a)
# 获取button.png的像素
c = pyautogui.locateOnScreen('button.png')
print(c)
# # 通过像素还原中心点的坐标
# x, y = pyautogui.center((482, 24, 71, 31)) # 获得中心点
# pyautogui.click(x, y)


# d = pyautogui.locateOnScreen('txt.png')
# print(d)
# x, y = pyautogui.center((197, 1035, 42, 41))
# pyautogui.click(x, y)
# pyautogui.click(200, 200)
# pyautogui.typewrite('Hello world!')
# pyautogui.typewrite('Good Bye', 0.25)
# pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], '0.25')


# d = pyautogui.locateOnScreen('txt.png')
# print(d)
# x, y = pyautogui.center((197, 1035, 42, 41))
# pyautogui.click(x, y)
# pyautogui.click(200, 200)
# # 模拟alt＋F4：
# # pyautogui.keyDown('altleft')
# # pyautogui.press('f4')
# # pyautogui.keyUp('altleft')
# # # 也可以直接使用热键函数：hotkey()
# pyautogui.hotkey('altleft', 'f4')