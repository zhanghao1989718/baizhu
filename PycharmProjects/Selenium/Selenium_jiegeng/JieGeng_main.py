# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import datetime
from PycharmProjects.Dingding_warning.warning import message
from PycharmProjects.LOG.logger import Logger




# def title_judge(a): # 定义标题判断方法
#     title = driver.title
#     if title == a:
#         mylogger.info(a + "页面打开成功 ")
#         message(a + "页面打开成功 ")
#     else:
#         mylogger.info(a + "页面打开失败 ")
#     # 获取当前系统时间，并去除毫秒
#     i = datetime.datetime.now().replace(microsecond=0)
#     mylogger.info("%s" % i)


# # 定义获取当前系统时间
# def datatime():
#     i = datetime.datetime.now().replace(microsecond=0)
#     mylogger.info("%s" % i)


# 定义通过xpath鼠标点击接口，并后退
# def testName(c, b):
#     driver.find_element_by_xpath(c).click()
#     time.sleep(3)
#     title = driver.title
#     if title == b:
#         mylogger.info(b + "页面打开成功 ")
#         message(b + "页面打开成功 ")
#     else:
#         mylogger.info(b + "页面打开失败 ")
#     i = datetime.datetime.now().replace(microsecond=0)
#     mylogger.info("%s" % i)
#     driver.back()
#     time.sleep(3)


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
                message(b + "页面打开成功 ")
            else:
                mylogger.info(b + "页面打开失败 ")
            i = datetime.datetime.now().replace(microsecond=0)
            mylogger.info("%s" % i)
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


def switchHandle_Dianshiju(a):
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1 and current_window != window_first:
            driver.switch_to.window(current_window)
            driver.close()
            driver.switch_to.window(window_1)
    time.sleep(3)


def switchHandle_Dianshiju_Panduan(a, b, c):
    driver.find_element_by_xpath(a).click()
    window_1 = driver.current_window_handle
    windows = driver.window_handles
    time.sleep(3)
    for current_window in windows:
        if current_window != window_1 and current_window != window_first:
            driver.switch_to.window(current_window)
            title = driver.title
            if title == b:
                mylogger.info(c + "打开成功 ")
                message(b + "页面打开成功 ")
            else:
                mylogger.info(c + "打开失败 ")
            i = datetime.datetime.now().replace(microsecond=0)
            mylogger.info("%s" % i)
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
                    mylogger.info(c + "页面打开成功 ")
                    message(c + "页面打开成功 ")
                    i = datetime.datetime.now().replace(microsecond=0)
                    mylogger.info("%s" % i)
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


def switchHandle_Remenyouxi_CheckBoxs(a):
    checkboxs = driver.find_elements_by_xpath(a)
    for k in checkboxs:
        k.click()
        window_1 = driver.current_window_handle
        windows = driver.window_handles
        time.sleep(3)
        for current_window in windows:
            if current_window != window_1 and current_window != window_remenyouxi:
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
                        message(b + "页面打开成功 ")
                        i = datetime.datetime.now().replace(microsecond=0)
                        mylogger.info("%s" % i)
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
    mylogger = Logger(logger='桔梗网').getlog()
    mylogger.info('桔梗网的第%d次测试开始' % i)
    message('桔梗网的第%d次测试开始' % i)
    # driver实列化
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    mylogger.info("打开浏览器")
    message("打开浏览器")
    # 浏览器运行到指定网址
    driver.get('http://www.jiegeng.com/')
    # 等待3秒
    time.sleep(3)
    # 窗口最大化
    driver.maximize_window()
    # 调用判断标题的方法
    title_judge('桔梗导航[www.jiegeng.com]_最实用的上网主页_上网就上桔梗网！')
    mylogger.info('桔梗网页正确打开')
    switchHandle('//*[@id="indexLogo"]/a/img', '桔梗导航[www.jiegeng.com]_最实用的上网主页_上网就上桔梗网！')
    mylogger.info('左上角网站图标点击成功')
    switchHandle('//*[@id="weaoo_container"]/div[1]/div[1]/div[1]/span/a',
                 '安徽马鞍山天气，马鞍山天气预报一周以及24小时实况查询 - 围观天气')
    switchHandle('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[1]',
                 '马鞍山PM2.5,马鞍山空气质量指数24小时实时查询 - 围观天气')
    driver.find_element_by_xpath('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[2]').click()
    mylogger.info('切换点击成功')
    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    switchHandlea('//*[@id="weaoo_container"]/div[1]/div[2]/div[1]/a/div[2]')
    mylogger.info('今日天气点击成功')
    switchHandlea('//*[@id="weaoo_container"]/div[1]/div[2]/div[2]/a/div[2]')
    mylogger.info('明日天气点击成功')
    switchHandle('//*[@id="calendar"]/div/span[1]/a[1]', '日历_百度搜索')
    switchHandle('//*[@id="calendar"]/div/span[1]/a[2]', '日历_百度搜索')
    switchHandle('//*[@id="calendar"]/div/span[1]/a[3]', '生肖查询_百度搜索')
    switchHandle('//*[@id="calendar"]/div/span[2]/a[1]', '日历_百度搜索')
    switchHandle('//*[@id="calendar"]/div/span[2]/a[2]', '星座运势_百度搜索')
    switchHandlea('//*[@id="headJoke"]/a/span')
    mylogger.info('顶部游戏推荐栏遍历成功')
    switchHandlea('//*[@id="header"]/div[1]/div/div[4]/div/div/a/img')
    mylogger.info('顶部游戏图片遍历成功')
    switchHandle('//*[@id="eng-logo"]', '360搜索，SO靠谱')
    driver.find_element_by_xpath('//*[@id="g-toggle"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="search-input"]').send_keys('下载器')
    time.sleep(3)
    switchHandle('//*[@id="search-form"]/div[3]/input', '下载器_360搜索')
    driver.find_element_by_xpath('//*[@id="menus"]/li[1]/a/span').click()
    time.sleep(3)

    # 电视剧模块
    driver.find_element_by_xpath('//*[@id="menus"]/li[2]/a/span').click()
    window_first = driver.current_window_handle
    windows = driver.window_handles
    for current_window in windows:
        if current_window != window_first:
            time.sleep(2)
            driver.switch_to.window(current_window)
            title = driver.title
            if title == "桔梗电视剧大全 - 更新更全更好看的电视剧网站在线观看 - 2019新电视剧":
                mylogger.info("电视剧页面打开成功 ")
            else:
                mylogger.info("电视剧页面打开失败 ")
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="vheader"]/div[1]/div/a').click()
            time.sleep(3)
            article = driver.find_element_by_xpath('//*[@id="vheader"]/div[1]/div/div[1]/a/em')
            ActionChains(driver).move_to_element(article).perform()
            time.sleep(3)
            article = driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/input')
            ActionChains(driver).move_to_element(article).perform()
            driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/input').send_keys("诛仙")
            time.sleep(3)
            switchHandle_Dianshiju('//*[@id="search"]')
            driver.back()
            time.sleep(2)
            switchHandle_Dianshiju_Panduan('//*[@id="left_1"]/span',
                                   '桔梗导航[www.jiegeng.com]_最实用的上网主页_上网就上桔梗网！',
                                   '桔梗网首页')
            driver.find_element_by_xpath('//*[@id="main_menu"]/div/p/a[3]/span').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="left_4"]/span').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="main_menu"]/div/p/a[5]/span').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="main_menu"]/div/p/a[3]/span').click()
            time.sleep(2)
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[1]/dd/span/a')
            mylogger.info("地区复选框遍历完毕，无异常")
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[1]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[2]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[3]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[4]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[5]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[6]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[7]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[8]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[9]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[10]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[11]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[12]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[13]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[14]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[15]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[16]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[17]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[18]/a')
            mylogger.info('类型复选框遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[3]/dd/span/a')
            mylogger.info('年代复选框遍历完毕，无异常')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[1]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[2]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[3]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[4]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[5]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[6]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[7]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[8]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[9]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[11]/a')
            switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[12]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[3]/div[1]/div/div[2]/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('同步追剧遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li/a')
            mylogger.info('本周最热遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="neidi"]/div/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('内地剧遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/ul/li')
            mylogger.info('内地剧搜视榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="wangluoju"]/div/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('网络剧遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[3]/div[2]/div/div[2]/div/ul/li/a')
            mylogger.info('网络剧搜视榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="hanguo"]/div/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('浪漫日韩遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[4]/div[2]/div/div[2]/div/ul/li/a')
            mylogger.info('韩剧好评榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="meiguo"]/div/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('美剧热播遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[6]/div[2]/div/div[2]/div/ul/li/a')
            mylogger.info('美剧强档榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="taiwan"]/div/div[2]/div/ul/li/div[1]/a/i')
            mylogger.info('风情·港台泰榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[7]/div[2]/div/div[2]/div/ul/li/a')
            mylogger.info('台剧人气榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[1]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[2]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[3]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[4]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[5]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[6]/div[1]/a/i')
            mylogger.info('谍战剧 PK 抗战剧遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[1]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[2]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[3]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[4]')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[5]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[6]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[7]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[8]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[9]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[10]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[11]/a')
            mylogger.info('谍战剧热播榜遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[1]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[2]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[3]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[4]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[5]/div[1]/a/i')
            switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[6]/div[1]/a/i')
            mylogger.info('唯美古风吹遍历完毕，无异常')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[1]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[2]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[3]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[4]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[5]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[6]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[7]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[8]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[9]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[10]/a')
            switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[11]/a')
            mylogger.info('古装剧热播榜遍历完毕，无异常')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[1]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '战争抗日')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[2]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '古装武侠')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[3]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '警匪谍战')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[4]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '言情偶像')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[5]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '朴实农村')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[6]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '都市生活')
            switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[7]',
                                           '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                           '全部分类')
            driver.close()
            driver.switch_to.window(window_first)


    switchHandle('//*[@id="menus"]/li[3]/a/span', '软件下载中心、最安全的软件资源下载')
    driver.find_element_by_xpath('//*[@id="menus"]/li[4]/a/span').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="menus"]/li[5]/a/span').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="menus"]/li[6]/a/span').click()
    time.sleep(3)


    #热门游戏模块
    driver.find_element_by_xpath('//*[@id="menus"]/li[7]/a/span').click()
    window_remenyouxi = driver.current_window_handle
    windows_remenyouxi = driver.window_handles
    for current_window in windows_remenyouxi:
        if current_window != window_remenyouxi:
            time.sleep(2)
            driver.switch_to.window(current_window)
            title = driver.title
            if title == "2019网页游戏大全,更新好玩的网页游戏开服表-桔梗网页游戏":
                mylogger.info("电视剧页面打开成功 ")
            else:
                mylogger.info("电视剧页面打开失败 ")
            time2 = datetime.datetime.now().replace(microsecond=0)
            mylogger.info("%s" % time2)
            time.sleep(3)
            switchHandle_Remenyouxi_CheckBoxs('//*[@id="view3"]/div/a/img')
            switchHandle_Remenyouxi_CheckBoxs('//*[@id="view2"]/li/span')
            switchHandle_Remenyouxi_CheckBoxs('//*[@id="view3"]/div/a/img')

            driver.close()
            driver.switch_to.window(window_remenyouxi)
    switchHandle('//*[@id="menus"]/li[8]/a/span', '在线小游戏,单机小游戏大全-桔梗小游戏')
    switchHandle('//*[@id="menus"]/li[9]/a/span', '爱淘宝-淘宝网购物分享平台')
    switchHandle('//*[@id="menus"]/li[10]/a/span', '携程旅行网官网:酒店预订,机票预订查询,旅游度假,商旅管理')
    switchHandlea('//*[@id="menus"]/li[11]/a/span')
    driver.find_element_by_xpath('//*[@id="menus"]/li[1]/a/span').click()
    time.sleep(3)



    switchHandlea('//*[@id="layout-side"]/div[1]/div/ul/li[1]/a/img')
    switchHandlee('//*[@id="box-starbar"]/div/a')
    switchHandled('//*[@id="site"]/div[1]/ul/li[1]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[2]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[3]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[4]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[5]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[6]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[7]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[8]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[9]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[10]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[11]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[12]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[13]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[14]/a[1]')
    switchHandlee('//*[@id="site"]/div[1]/ul/li[15]/a[2]/img')
    switchHandled('//*[@id="site"]/div[1]/ul/li[16]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[17]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[18]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[19]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[20]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[21]/a[1]')
    switchHandlee('//*[@id="site"]/div[1]/ul/li[22]/a[2]/img')
    switchHandled('//*[@id="site"]/div[1]/ul/li[23]/a[1]')
    switchHandled('//*[@id="site"]/div[1]/ul/li[24]/a[1]')
    mylogger.info('id="site"遍历成功')
    switchHandled('//*[@id="box-famoussite"]/div/ul/li/a')
    mylogger.info('id="box-famoussite"遍历成功')
    switchHandlee('// *[ @ id = "hlbar"] / span')
    mylogger.info('id = "hlbar"遍历成功')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[1] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[2] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[3] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[4] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[5] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[6] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[7] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[8] / a / span')
    switchHandlea('// *[ @ id = "topzixun-over"] / div / p[9] / a / span')
    mylogger.info('id = topzixun-over遍历成功')
    switchHandlee('//*[@id="infoflow-list"]/div/div[1]/a/img')
    time.sleep(3)
    switchHandlea('//*[@id="topzixun-over"]/div/p[1]/a[@data-id = "10466"]')
    switchHandlea('//*[@id="topzixun-over"]/div/p[2]/a[@data-id = "10467"]')
    switchHandlea('//*[@id="topzixun-over"]/div/p[3]/a[@data-id = "10468"]')
    switchHandlee('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div/p[1]/a/span')
    switchHandlee('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div[2]/p/a/span')



    switchframe('//*[@id="wrapper"]/div[1]/ul/li[1]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[2]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[3]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[4]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[5]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[6]/a')
    switchframe('//*[@id="wrapper"]/div[1]/ul/li[7]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[1]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[2]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[3]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[4]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[5]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[6]/a')
    switchframe('//*[@id="wrapper"]/div[2]/ul/li[7]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[1]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[2]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[3]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[4]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[5]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[6]/a')
    switchframe('//*[@id="wrapper"]/div[3]/ul/li[7]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[1]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[2]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[3]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[4]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[5]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[6]/a')
    switchframe('//*[@id="wrapper"]/div[4]/ul/li[7]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[1]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[2]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[3]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[4]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[5]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[6]/a')
    switchframe('//*[@id="wrapper"]/div[5]/ul/li[7]/a')
    switchHandlec('//*[@id="toplist-soft"]/div/div/div[2]/div/p/a',
                  ['Microsoft Office Visio 2016',
                   '极速PDF转Word 免费下载_极速PDF转Word 免费版_极速PDF转Word -桔梗下载站',
                   '腾讯QQ 轻聊版',
                   '天气网天气预报',
                   '花椒直播免费下载_花椒直播免费版_花椒直播-桔梗下载站'
                   '微信电脑版',
                   '酷狗音乐',
                   '爱奇艺PPS影音',
                   '万能数据恢复大师',
                   '腾讯视频',
                   'YY语音（中国最大的视频直播软件）',
                   'QQ浏览器免费下载_QQ浏览器免费版_QQ浏览器-桔梗下载站', ])
    switchHandlec('//*[@id="navigate"]/a/span',
                  ['桔梗电视剧大全 - 更新更全更好看的电视剧网站在线观看 - 2019新电视剧',
                   '桔梗电影大全 - 更新电影_电影天堂_好看的电影排行榜_高清在线观看',
                   '头条新闻_东方新闻',
                   '娱乐新闻_东方资讯网',
                   '军事头条_东方军事网'
                   '在线小游戏,单机小游戏大全-桔梗小游戏',
                   '2019网页游戏大全,更新好玩的网页游戏开服表-桔梗网页游戏',
                   '淘抢购首页- 淘抢购',
                   '爱淘宝-淘宝网购物分享平台',
                   '桔梗综艺大全-最新综艺节目,更全更新好看的综艺节目在线观看',
                   '软件下载中心、最安全的软件资源下载',
                   '宜人贷借款,快捷、简单、无抵押无担保_宜人贷', ])
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[1]/span[8]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[2]/span[8]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[3]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[5]/span[8]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[6]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[2]/a[1]')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[2]/a[2]')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[2]/a[3]')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[6]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[7]/span[7]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[2]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[3]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[4]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[5]/a')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[6]/a[1]')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[6]/a[2]')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[6]/a[3]')
    switchHandlea('//*[@id="coolsite-group0"]/div[8]/span[7]/a')
    mylogger.info('id="coolsite-group0"遍历成功')
    switchHandlec('//*[@id="coolsite-group1"]/div[1]/a',
                  ['软件下载中心、最安全的软件资源下载',
                   '彩票_福利彩票发行管理中心指定网络信息发布媒体-中彩网',
                   '考试_桔梗上网导航',
                   '爱淘宝-淘宝网购物分享平台',
                   '没有找到站点'
                   '东方体育新闻_NBA直播吧|足球直播吧|中超直播吧_体育直播吧',
                   '东方体育新闻_NBA直播吧|足球直播吧|中超直播吧_体育直播吧',
                   '娱乐新闻_东方资讯网',
                   '头条新闻_东方新闻',
                   '在线小游戏,单机小游戏大全-桔梗小游戏',
                   '桔梗理财 – 专业互联网理财平台',
                   '桔梗小说网', ])
    switchHandlee('//*[@id="coolsite-group1"]/div/span/a')
    mylogger.info('id="coolsite-group1"遍历成功')
    switchHandlea('//*[@id="gimgl2"]/a[1]/img')
    switchHandlea('//*[@id="gimgl2"]/a[2]/img')
    switchHandlea('//*[@id="gimgl2"]/a[3]/img')
    switchHandlea('//*[@id="gimgl2"]/a[4]/img')
    switchHandlea('//*[@id="gimgl2"]/a[5]/img')
    switchHandlea('//*[@id="gimgl2"]/a[6]/img')
    switchHandlea('//*[@id="gimgl2"]/a[7]/img')
    switchHandlea('//*[@id="gimgl2"]/a[8]/img')
    switchHandlea('//*[@id="gimgl2"]/a[9]/img')
    switchHandlea('//*[@id="gimgl2"]/a[10]/img')
    switchHandlea('//*[@id="gimgl2"]/a[11]/img')
    switchHandlea('//*[@id="gimgl2"]/a[12]/img')
    switchHandlea('//*[@id="gimgl2"]/a[13]/img')
    switchHandlea('//*[@id="gimgl2"]/a[14]/img')
    switchHandlea('//*[@id="gimgl2"]/a[15]/img')
    switchHandlea('//*[@id="gimgl2"]/a[16]/img')
    switchHandlea('//*[@id="gimgl2"]/a[17]/img')
    switchHandlea('//*[@id="gimgl2"]/a[18]/img')
    switchHandlea('//*[@id="gimgl2"]/a[19]/img')
    switchHandlea('//*[@id="gimgl2"]/a[20]/img')
    switchHandlea('//*[@id="gimgl2"]/a[21]/img')
    switchHandlea('//*[@id="gimgl2"]/a[22]/img')
    switchHandlea('//*[@id="gimgl2"]/a[23]/img')
    switchHandlea('//*[@id="gimgl2"]/a[24]/img')
    mylogger.info('id="gimgl2"遍历成功')
    switchHandlea('//*[@id="shortvideo_slider1"]/div/div/ul/li[1]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[1]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[2]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[3]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[4]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[5]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[6]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[7]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[8]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[9]/a/img')
    switchHandlea('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[10]/a/img')
    mylogger.info('id="shortvideo_slider2遍历成功')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[1]/a/img')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[2]/a/img')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[3]/a/img')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[4]/a/img')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[5]/a/img')
    switchHandlea('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[6]/a/img')
    mylogger.info('id="hao123-shortvideo"遍历成功')
    switchHandlee('//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/ul/li/a')
    mylogger.info('id="slider_597985e4ce882遍历成功')
    time.sleep(3)
    mylogger.info('桔梗网的第%d次测试结束' % i)
    time.sleep(2)
    print(driver.capabilities['version'])  # 打印浏览器version的值
    driver.quit()
