from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pywinauto.mouse import click
import time, os
import pyautogui as pa

url_rj = "http://www.33lc.com/soft/xtrj/xtyh/"
url_yx = "http://www.daque.cn/soft/82804.html?tab=2300491"
url_ob = "http://download.zol.com.cn/detail/43/429177.shtml"
save_button_path = os.path.abspath(".") +"\\png\\getdownloader\\"

class GetDownloader(object):

    def judge_programme(self):
        while True:
            input_programme = input("请输入方案，例如：软件、360营销、onebox")
            if input_programme == "软件":
                print("您输入的方案为:%s" % input_programme)
                self.programme_rj()
                break
            elif input_programme == "360营销":
                print("您输入的方案为:%s" % input_programme)
                self.programme_yx()
                break
            elif input_programme == "onebox":
                print("您输入的方案为:%s" % input_programme)
                self.programme_ob()
                break
            else:
                print("输入错误,请重新输入")
                
    @staticmethod
    def get_desktop():
        get_desktop = os.path.join(os.path.expanduser('~'), "Desktop")
        return get_desktop

    def programme_rj(self):
        # 实例化一个Options
        chrome_options = Options()
        # 用于定义下载不弹窗和默认下载地址（默认下载地址还要再后面的commands里启动，默认是不开启的）
        prefs = {"download.default_directory": self.get_desktop() + "\\", "download.prompt_for_download": False, }
        chrome_options.add_experimental_option("prefs", prefs)
        dr = webdriver.Chrome(options = chrome_options)
        dr.get(url_rj)
        dr.maximize_window()
        dr.find_element_by_xpath('//*[@id="pageList"]/div[9]/div[1]/a').click()
        while True:
            save_pixel = pa.locateOnScreen(save_button_path + "save_button.png")
            if save_pixel is not None:
                try:
                    x, y = pa.center(pa.locateOnScreen(save_button_path + "save_button.png"))
                    click(coords=(x, y))
                except Exception as result:
                    print(result)
                break
        dr.close()

    @staticmethod
    def programme_yx():
        dr = webdriver.Chrome()
        dr.get(url_yx)
        time.sleep(1)
        dr.close()

    @staticmethod
    def programme_ob():
        dr = webdriver.Chrome()
        dr.get(url_ob)
        time.sleep(1)
        dr.close()

    def main(self):
        self.judge_programme()

if __name__ == "__main__":
    gd = GetDownloader()
    gd.main()