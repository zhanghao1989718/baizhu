import os, time
import pyautogui

def get_desktop():
    get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
    return get_desktop

# 创建文件夹
def make_dir():
    try:
        os.makedirs(os.path.join(get_desktop()) + '\\screen')
    except:
        pass

def get_screen(name):
    img = pyautogui.screenshot(region=[468, 212, 600, 400])
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    img.save(get_desktop() + "\\" + "screen" + "\\" + rq + name + ".png")



def main():
    make_dir()
    get_screen("第一页")


main()


