# coding=utf-8
import sys
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
from PycharmProjects.Dingding_warning.warning import message


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
get_desk_p = os.path.join(os.path.expanduser('~'),"Desktop")
sys.stdout = Logger(get_desk_p + "\\bz_selenium_log.txt")


# 定义标题判断方法
def title_judge(a, b):
    title = driver.title
    if title == a:
        print("%s \n页面打开成功 " % b)
    else:
        print("%s \n页面打开失败 " % b)
    # 获取当前系统时间，并去除毫秒
    i = datetime.datetime.now().replace(microsecond=0)
    print("%s" % i)


# 定义获取当前系统时间
def datatime():
    i = datetime.datetime.now().replace(microsecond=0)
    print("%s" % i)


# 定义通过xpath鼠标点击接口，并后退
def testName(c, b, d):
    driver.find_element_by_xpath(c).click()
    time.sleep(3)
    title = driver.title
    if title == b:
        print("%s \n页面打开成功 " % d)
    else:
        print("%s \n页面打开失败 " % d)
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


for i in range(1, 2):
    print('百助官网的第%d次测试开始' % i, end="\n")
    message("自动化测试开始")
    datatime()
    driver = webdriver.Chrome()
    driver.get("http://www.bz.cn")
    time.sleep(2)
    driver.maximize_window()
    title_judge('百助_下载器_让下载更有价值', "百助官网")
    testName("//*[@id='nav']/ul/li[2]/a", "百助发展", "发展历程")
    testName("//*[@id='nav']/ul/li[3]/a", "百助新闻", "新闻动态")
    testName("//*[@id='nav']/ul/li[4]/a", "百助文化", "人在百助")
    testName("//*[@id='nav']/ul/li[5]/a", "百助招聘", "加入百助")
    testName("//*[@id='nav']/ul/li[6]/a", "管理团队百助_下载器_让下载更有价值", "管理团队")
    testName("//*[@id='nav']/ul/li[7]/a", "百助合作", "联系我们")
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[1]/div[1]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[1]/div[3]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[2]/div[1]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[2]/div[2]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[2]/div[3]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="intro"]/div[2]/div[4]/small')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    switchHandlee('//*[@id="home_tiniejr0"]/a/span')
    switchHandled('//*[@id="intro"]/div[2]/ul/li/div[1]/a')
    switchHandled('//*[@id="intro"]/div[2]/ul/li/div[2]/a')
    switchHandled('//*[@id="intro"]/div[2]/ul/li/div[3]/a')
    switchHandled('//*[@id="intro"]/div[2]/ul/li/div[4]/a')
    time.sleep(3)
    switchHandlee('//*[@id="features"]/div[2]/div[1]/ul/li/a/img')
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li/div[1]/span')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li/div[2]/span')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li/div[3]/span')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li/div[4]/span')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    testName('//*[@id="features"]/a', "百助招聘", "加入我们")
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li[1]/a/div[1]')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li[2]/a/div[1]')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    article = driver.find_element_by_xpath('//*[@id="features"]/ul/li[3]/a/div[1]')
    ActionChains(driver).move_to_element(article).perform()
    time.sleep(2)
    print('百助官网的第%d次测试结束' % i, end="\n")
    datatime()
    print(end='\n')
    message("自动化测试结束")
    driver.quit()


