import autoit
import time
import pyautogui as pa
from pywinauto.mouse import move, click

autoit.run("notepad.exe")
# time.sleep(3)
# autoit.win_wait_active("[CLASS:Notepad]", 3)
# time.sleep(3)
# autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
# time.sleep(3)
# autoit.win_close("[CLASS:Notepad]")
# time.sleep(3)
# autoit.control_click("[Class:#32770]", "Button2")

a = pa.locateOnScreen("install_success.png")
print(a)
print(type(a))
x, y = pa.center(a)
move(coords=(x, y))
click(coords=(x, y))