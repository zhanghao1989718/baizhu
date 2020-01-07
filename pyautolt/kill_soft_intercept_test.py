import autoit, os, time, psutil
import pywinauto as pw
import pyautogui as pa
from pywinauto.mouse import move, click, double_click
from pyautolt.wincontrol import WinControl
from pyautolt.mousecontrol import MouseControl
from pyautolt.processcontrol import ProcessControl


soft_name = "软媒清理大师@133_39990.exe"
title_name = "软媒清理大师"
process_name = "软媒清理大师@133_39990.exe"
xiazaiqi_anniu_path = os.path.abspath(".") +"\\png\\xiazaiqi_anniu\\"
jietu360_path = os.path.abspath(".") +"\\png\\360_jietu\\"
jietu360_name = "360截图"
cl360_pos = [604, 315, 713, 400]
jh360_pos = [1516, 412, 410, 630]
cl360jxyx = []

class DownloaderInstall(object):

    def get_desktop(self):
        get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
        return get_desktop

    # 获取权限
    def get_system_permissions(self):
        os.environ.update({"__COMPAT_LAYER": "RUnAsInvoker"})

    # 启动下载器
    def start_app(self):
        self.get_system_permissions()
        soft_path = self.get_desktop() + "\\" + soft_name
        autoit.run(soft_path)

    # 创建文件夹
    def make_dir(self):
        try:
            os.makedirs(os.path.join(self.get_desktop()) + '\\screen')
        except:
            pass

    # 截屏
    def get_screen(self, pos, name):
        img = pa.screenshot(region = pos)
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        img.save(self.get_desktop() + "\\" + "screen" + "\\" + rq + name + ".png")

    # 下载器截屏
    def get_xiazaiqi_screen(self, name, title_app_name):
        x, y, x1, y1 = WinControl(title_app_name).getPos()
        w = x1 - x
        h = y1 - y
        pos = [x, y, w, h]
        self.get_screen(pos, name)
        # img = pa.screenshot(region = pos)
        # rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        # img.save(self.get_desktop() + "\\" + "screen" + "\\" + rq + name + ".png")

    # 点击第一页安装按钮
    def first_button_click(self, pic_name, pic_zh_name, title_app_name):
        WinControl(title_app_name).activate()
        # 截屏第一页
        self.get_xiazaiqi_screen("第一页", title_name)
        time.sleep(1)
        try:
            button_down_pixel = pa.locateOnScreen(pic_name)
            x, y = pa.center(button_down_pixel)
            # move(coords=(x, y))
            click(coords=(x, y))
        except:
            button_down_pixel = pa.locateOnScreen(pic_zh_name)
            x, y = pa.center(button_down_pixel)
            # move(coords=(x, y))
            click(coords=(x, y))

    # 判断安装按钮是否出现
    def install_button_click(self, pic_name, pic_zh_name, title_app_name):
        while True:
           # 激活软件窗口
           WinControl(title_app_name).activate()
           if pa.locateOnScreen(pic_name) is not None:
               x, y = pa.center(pa.locateOnScreen(pic_name))
               # move(coords=(x, y))
               # 截屏第三页
               self.get_xiazaiqi_screen("第三页", title_name)
               click(coords=(x, y))
               break
           elif pa.locateOnScreen(pic_zh_name) is not None:
               x, y = pa.center(pa.locateOnScreen(pic_zh_name))
               # move(coords=(x, y))
               # 截屏第三页
               self.get_xiazaiqi_screen("第三页", title_name)
               click(coords=(x, y))
               break

    # 关闭下载器
    def close_app(self, title_app_name):
        WinControl(title_app_name).kill()

    def main(self):
        # 判断杀软环境

        # 360环境
        # 启动下载器程序
        self.start_app()
        WinControl(title_name).wait(60)
        self.make_dir()

        # 点击一键安装
        self.first_button_click(xiazaiqi_anniu_path + "install.png", xiazaiqi_anniu_path + "install_bs.png", title_name)
        time.sleep(2)

        # 判断第三页按钮是否出现并点击安装完成
        self.install_button_click(xiazaiqi_anniu_path + "install_success.png", xiazaiqi_anniu_path + "install_success_bs.png", title_name)
        time.sleep(3)

        # 杀软拦截截屏

        # 判断第三页是否有软件

        # 有软件，等待进程结束继续重复以上步骤

        # 无软件，结束任务

        self.close_app(title_name)

if __name__ == "__main__":
    di = DownloaderInstall()
    # di.main()
    di.make_dir()
    while True:
        if pa.locateOnScreen(jietu360_path + "cl_button.png") is not None:
            di.get_screen(cl360_pos, jietu360_name)
            x, y = pa.center(pa.locateOnScreen(jietu360_path + "cl_button.png"))
            move(coords=(x, y))
            double_click(coords=(x, y))
            time.sleep(1)
            break
        elif pa.locateOnScreen(jietu360_path + "cl_button_bs.png") is not None:
            di.get_screen(cl360_pos, jietu360_name)
            x, y = pa.center(pa.locateOnScreen(jietu360_path + "cl_button_bs.png"))
            move(coords=(x, y))
            double_click(coords=(x, y))
            time.sleep(1)
            break
        elif pa.locateOnScreen(jietu360_path + "cl_jxyx.png") is not None:
            di.get_screen(cl360_pos, jietu360_name)
            x, y = pa.center(pa.locateOnScreen(jietu360_path + "cl_jxyx.png"))
            move(coords=(x, y))
            double_click(coords=(x, y))
            time.sleep(1)
            break
        elif pa.locateOnScreen(jietu360_path + "jh_button.png") is not None:
            di.get_screen(jh360_pos, jietu360_name)
            x, y = pa.center(pa.locateOnScreen(jietu360_path + "jh_button.png"))
            move(coords=(x, y))
            double_click(coords=(x, y))
            time.sleep(1)
            break

