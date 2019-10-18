# coding=utf-8
import logging
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from PycharmProjects.Dingding_warning.warning import message

class Logger(object):
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.path.abspath('.')) + '\\Logs\\logs\\'
        log_name = log_path + rq + '.log'
        error_log_path = os.path.dirname(os.path.abspath('.')) + '\\Logs\\error_logs\\'
        error_log_name = error_log_path + rq + '.log'
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)
        eh = logging.FileHandler(error_log_name, encoding='utf-8')
        eh.setLevel(logging.ERROR)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        eh.setFormatter(error_formatter)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        self.logger.addHandler(eh)
    def getlog(self):
        return self.logger

mylogger = Logger(logger='百助').getlog()

# 定义标题判断方法
def title_judge(a, b):
    title = driver.title
    if title == a:
        mylogger.info("%s \n页面打开成功 " % b)
    else:
        mylogger.info("%s \n页面打开失败 " % b)


# 定义通过xpath鼠标点击接口，并后退
def testName(c, b, d):
    driver.find_element_by_xpath(c).click()
    time.sleep(3)
    title = driver.title
    if title == b:
        mylogger.info("%s \n页面打开成功 " % d)
    else:
        mylogger.info("%s \n页面打开失败 " % d)
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
                mylogger.info(b + "页面打开成功 ")
            else:
                mylogger.info(b + "页面打开失败 ")
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
                        mylogger.info(b + "页面打开成功 ")
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
    mylogger.info('百助官网的第%d次测试开始' % i)
    # message("自动化测试开始")
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
    mylogger.info('百助官网的第%d次测试结束' % i)
    # message("自动化测试结束")
    driver.quit()


