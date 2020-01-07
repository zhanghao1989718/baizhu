import pywinauto as pw
import pyautogui as pa
import os, time, psutil, shutil
from pywinauto.mouse import move, click
from PIL import ImageGrab

# 获取桌面
def get_desktop():
    get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
    return get_desktop

# 创建文件夹
def make_dir():
    try:
        os.makedirs(os.path.join(get_desktop()) + '\\screen')
    except:
        print("桌面已有screen文件夹")
        # 删除非空文件夹
        # shutil.rmtree(os.path.join(get_desktop()) + '\\screen')
        # os.makedirs(os.path.join(get_desktop()) + '\\screen')

# 截屏
def get_screen():
    make_dir()
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    time.sleep(3)
    im = ImageGrab.grab()
    im.save(get_desktop() + "\\" + "screen" + "\\" + rq + ".png")

# 获取权限
def get_system_permissions():
    os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})

# 启动下载器
def start_download(soft_name):
    get_system_permissions()
    path_soft = get_desktop() + "\\" + soft_name
    app = pw.Application(backend="uia").start(path_soft)
    return app

def close_download(soft_name):
    app_connect = start_download(soft_name).connect(path=(get_desktop() + "\\" +soft_name))
    app_connect.kill(soft=True)

# 模拟鼠标点击
def click_button(pic_name):
    button_down_pixel = pa.locateOnScreen(pic_name)
    x, y = pa.center(button_down_pixel)
    move(coords=(x, y))
    click(coords=(x, y))

def get_process_name():
    pids = psutil.pids()
    list_pro_name = []
    for pid in pids:
        p = psutil.Process(pid)
        process_name = p.name()
        list_pro_name.append(process_name)
    return list_pro_name

def main():
    soft_name = "软媒清理大师@133_39990.exe"
    start_download(soft_name)
    time.sleep(10)
    get_screen()
    click_button("install.png") 
    time.sleep(3)
    get_screen()
    click_button("install_success.png")


if __name__ == "__main__":
    main()