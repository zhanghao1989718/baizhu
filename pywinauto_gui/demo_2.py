import pywinauto as pw
import pyautogui as pa
import os
import time
import shutil
from pywinauto.mouse import move, click
from PIL import ImageGrab

def get_desktop():
    get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
    return get_desktop

def make_dir():
    try:
        os.makedirs(os.path.join(get_desktop()) + '\\screen')
    except:
        shutil.rmtree(os.path.join(get_desktop()) + '\\screen')
        os.makedirs(os.path.join(get_desktop()) + '\\screen')

def get_screen():
    make_dir()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    time.sleep(3)
    im = ImageGrab.grab()
    im.save(get_desktop() + "\\" + "screen" + "\\" + rq + ".png")

def start_download(soft_name):
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})
    app = pw.Application(backend="uia").start(get_desktop() + "\\" + soft_name)
    return app


def click_button(pic_name, soft_name):
    try:
        button_down_pixel = pa.locateOnScreen(pic_name)
        x, y = pa.center(button_down_pixel)
        move(coords=(x, y))
        click(coords=(x, y))
    except:
        pw.Application(backend="uia").connect\
            (path=(get_desktop() + "\\" + soft_name)).kill(soft=True)
        start_download(soft_name)
        time.sleep(10)
        button_down_pixel = pa.locateOnScreen(pic_name)
        x, y = pa.center(button_down_pixel)
        move(coords=(x, y))
        click(coords=(x, y))

def main(soft_name=None):
    # start_download(soft_name)
    # time.sleep(10)
    # click_button("install.png",soft_name)
    # get_screen()
    pw.Application(backend="uia").connect \
        (path=(get_desktop() + "\\" + "软媒清理大师@133_39990.exe")).kill(soft=True)

if __name__ == "__main__":
    main()