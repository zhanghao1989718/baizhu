import pywinauto
from pywinauto import application
import os
import time


# os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
# pywinauto.Application(backend="uia").start("C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\软媒清理大师@133_39990.exe")
# time.sleep(5)
app = pywinauto.Application().start("notepad.exe")
time.sleep(1)
title_notepad = "无标题-记事本"
# app[title_notepad].menu_select("帮助->关于记事本")
# time.sleep(1)
#
# # 点击新弹出窗体的确定按钮
# out_note = "关于记事本"
# button_name_ok = "确定"
# app[out_note][button_name_ok].click()

# 输入一些文字
print(app[title_notepad].print_control_identifiers())
