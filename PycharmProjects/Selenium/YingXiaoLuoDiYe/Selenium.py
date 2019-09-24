# coding=utf-8
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


# 定义日志集合
class Logger(object):
    def __init__(self, fileN="Default.log"):
        self.terminal = sys.stdout
        self.log = open(fileN, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


# 输出日志到桌面文档
sys.stdout = Logger("C:\\Users\\80649\\Desktop\\营销落地页log.txt")


# 定义标题判断方法
def title_judge(a):
    title = driver.title
    if title == a:
        print(a, end="\n" + "页面打开成功 ")
    else:
        print(a, end="\n" + "页面打开失败 ")
    # 获取当前系统时间，并去除毫秒
    i = datetime.datetime.now().replace(microsecond=0)
    print("%s" % i)


# 定义获取当前系统时间
def datatime():
    i = datetime.datetime.now().replace(microsecond=0)
    print("%s" % i)


# 定义通过xpath鼠标点击接口，并后退
def testName(c, b):
    driver.find_element_by_xpath(c).click()
    time.sleep(3)
    title = driver.title
    if title == b:
        print(b, end="\n" + "页面打开成功 ")
    else:
        print(b, end="\n" + "页面打开失败 ")
    i = datetime.datetime.now().replace(microsecond=0)
    print("%s" % i)
    driver.back()
    time.sleep(3)


# 定义通过xpath鼠标点击接口，切换窗口到新窗口后
# 判断跳转页面是否正确，再切换回之前窗口
def switchHandle(a, b):
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)
            title = driver.title
            if title == b:
                print(b, end="\n" + "页面打开成功 ")
            else:
                print(b, end="\n" + "页面打开失败 ")
            i = datetime.datetime.now().replace(microsecond=0)
            print("%s" % i)
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)


def switchHandlea(a):
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)


def switchHandle_DianShiJu_XunHuanPanDuan(a, b):
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1 and current_window != window_first:
            driver.switch_to.window(current_window)
            title = driver.title
            title_name = b
            for c in title_name:
                if title == c:
                    print(c, end="\n" + "页面打开成功 ")
                    i = datetime.datetime.now().replace(microsecond=0)
                    print("%s" % i, end="\n")
                    break
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)


def switchHandle_DianShiJu_CheckBoxs(a):
    checkboxs = driver.find_elements_by_xpath(a)
    for k in checkboxs:
        k.click()
        window_1 = driver.current_window_handle
        windows = driver.window_handles
        time.sleep(3)
        for current_window in windows:
            if current_window != window_1 and current_window != window_first:
                driver.switch_to.window(current_window)
                driver.close()
                driver.switch_to.window(window_1)
        time.sleep(3)


# 定义通过linktext鼠标点击接口，切换窗口到新窗口后，在切换回之前窗口
def switchHandleb(b):
    driver.find_element_by_partial_link_text(b).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)


# 定义通过xpath鼠标点击接口，切换窗口到新窗口后，在切换回之前窗口
# 复选框循环点击,复选框内定义了列表a，在列表a内寻找title
def switchHandlec(c, a):
    checkboxs = driver.find_elements_by_xpath(c)
    for k in checkboxs:
        k.click()
        window_1 = driver.current_window_handle
        windows = driver.window_handles
        time.sleep(3)
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
                title = driver.title
                title_name = a
                for b in title_name:
                    if title == b:
                        print(b, end="\n" + "页面打开成功 ")
                        i = datetime.datetime.now().replace(microsecond=0)
                        print("%s" % i, end="\n")
                        break
                driver.close()
                driver.switch_to.window(window_1)
        time.sleep(3)


# 定义定义通过xpath键盘回车点击接口，切换窗口到新窗口后，在切换回之前窗口
def switchHandled(d):
    checkboxs = driver.find_elements_by_xpath(d)
    for k in checkboxs:
        k.send_keys(Keys.ENTER)
        window_1 = driver.current_window_handle
        windows = driver.window_handles
        time.sleep(3)
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
                driver.close()
                driver.switch_to.window(window_1)
        time.sleep(3)


def switchHandlee(e):
    checkboxs = driver.find_elements_by_xpath(e)
    for k in checkboxs:
        k.click()
        window_1 = driver.current_window_handle
        windows = driver.window_handles
        time.sleep(3)
        for current_window in windows:
            if current_window != window_1:
                driver.switch_to.window(current_window)
                driver.close()
                driver.switch_to.window(window_1)
        time.sleep(3)


def switchframe(a):
    driver.switch_to.frame('myFrame')
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)
    driver.switch_to.default_content()


for i in range(1, 2):
    print('营销落地页的第%d次测试开始' % i, end="\n")
    datatime()
    # driver实列化
    driver = webdriver.Chrome()
    # 浏览器运行到指定网址
    driver.get('http://www.daque.cn/18/43553.html?tab=639827')
    # 等待2秒
    time.sleep(3)
    # 窗口最大化
    driver.maximize_window()




    print('营销落地页的第%d次测试结束' % i, end="\n")
    datatime()
    print(end='\n')
    time.sleep(2)
    driver.quit()
