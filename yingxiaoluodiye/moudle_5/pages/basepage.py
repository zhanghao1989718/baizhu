# coding=utf-8
import time
from yingxiaoluodiye.moudle_5.common.cappic import Cappic
from yingxiaoluodiye.moudle_5.common.log import Logger
import requests,json

mylogger = Logger(logger='basepage').getlog()

class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """
    def __init__(self, driver, showid):
        self.driver = driver
        self.showid = showid

    def get_keywordId(self):
        url = "http://zone.bz.cn/sem/keyword/index"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "keep-alive",
                   "Content-Length": "30",
                   "Host": "zone.bz.cn",
                   "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_221)"
                   }

        request_param = {
            "urrPage": "1",
            "pageSize": "20",
            "showId": self.showid
        }
        # response=requests.post(url,data=json.dumps(request_param), headers=headers)
        response = requests.post(url, data=request_param, headers=headers)

        get_text = response.text
        # json.loads把json格式转换为python识别的格式
        # print(json.loads(get_text)["content"]["pageContent"][1]["keywordId"])
        # print(get_text)
        # print(json.loads(get_text)["content"]["pageContent"][1]["showId"])
        # print("=" * 50)
        return json.loads(get_text)["content"]["pageContent"][1]["keywordId"]

    def get_url(self):
        url = "http://zone.bz.cn/sem/keyword/show"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "keep-alive",
                   "Content-Length": "30",
                   "Host": "zone.bz.cn",
                   "User-Agent": "Apache-HttpClient/4.5.2 (Java/1.8.0_221)"
                   }

        request_param = {
            "keywordId": self.get_keywordId()

        }
        response = requests.post(url, data=request_param, headers=headers)

        get_text = response.text
        # print(json.loads(get_text)["data"]["keyword"]["destinationUrl"])
        return json.loads(get_text)["data"]["keyword"]["destinationUrl"]

    def start_browser(self):
        mylogger.info("营销5#模板自动化测试开始")
        url = self.get_url()
        # 隐形等待10秒时间
        self.wait(10)
        # 跳转网页
        self.driver.get(url)
        mylogger.info("跳转至%s" % url)
        # 窗口最大化
        self.driver.maximize_window()
        mylogger.info("窗口已经最大化")
        #调用截屏方法
        Cappic(self.driver)
        self.sleep(1)

    def quit_browser(self):
        self.driver.quit()

    # 模拟鼠标左键点击
    def click_by_xpath(self, xpath):
        try:
            click_text = self.driver.find_element_by_xpath(xpath).text
            self.driver.find_element_by_xpath(xpath).click()
            mylogger.info("%s点击成功" % click_text)
        except Exception as result:
            mylogger.info(result)

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        mylogger.info("隐性等待%d秒" % seconds)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        # mylogger.info("强制等待 %d 秒" % seconds)

