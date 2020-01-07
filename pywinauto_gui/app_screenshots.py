import win32gui, sys, os, time

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *


hwnd_title = dict()
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
img.save(get_desktop + "\\" + "screen" + "\\" + rq + ".png")