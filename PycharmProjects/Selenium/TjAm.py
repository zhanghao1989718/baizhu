# # coding=utf-8
# import sys
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
# import datetime
#
#
# # 定义日志集合
# class Logger(object):
#     def __init__(self, fileN="Default.log"):
#         self.terminal = sys.stdout
#         self.log = open(fileN, "a")
#
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
#
#     def flush(self):
#         pass
#
#
# # 输出日志到桌面文档
# sys.stdout = Logger("C:\\Users\\80649.LAPTOP-T3EKEB7M\\Desktop\\天津安美log.txt")
#
#
# # 定义获取当前系统时间
# def datatime():
#     i = datetime.datetime.now().replace(microsecond=0)
#     print("%s" % i)
#
#
# # 定义标题判断方法
# def title_judge(a):
#     title = driver.title
#     if title == a:
#         print(a, end="\n" + "页面打开成功 ")
#     else:
#         print(a, end="\n" + "页面打开失败 ")
#     # 获取当前系统时间，并去除毫秒
#     i = datetime.datetime.now().replace(microsecond=0)
#     print("%s" % i)
#
#
# # 定义通过xpath鼠标点击接口，并后退
# def testName(c, b):
#     driver.find_element_by_xpath(c).click()
#     time.sleep(2)
#     title = driver.title
#     if title == b:
#         print(b, end="\n" + "页面打开成功 ")
#     else:
#         print(b, end="\n" + "页面打开失败 ")
#     i = datetime.datetime.now().replace(microsecond=0)
#     print("%s" % i)
#     driver.back()
#     time.sleep(2)
#
#
# # 定义通过xpath鼠标点击接口，切换窗口到新窗口后
# # 判断跳转页面是否正确，再切换回之前窗口
# def switchHandle(a, b):
#     driver.find_element_by_xpath(a).click()
#     window_1 = driver.current_window_handle
#     windows = driver.window_handles
#     time.sleep(2)
#     for current_window in windows:
#         if current_window != window_1:
#             driver.switch_to.window(current_window)
#             title = driver.title
#             if title == b:
#                 print(b, end="\n" + "页面打开成功 ")
#             else:
#                 print(b, end="\n" + "页面打开失败 ")
#             i = datetime.datetime.now().replace(microsecond=0)
#             print("%s" % i)
#             driver.close()
#             driver.switch_to.window(window_1)
#
#
# # 定义通过linktext鼠标点击接口，切换窗口到新窗口后，在切换回之前窗口
# def switchHandleb(b):
#     driver.find_element_by_partial_link_text(b).click()
#     window_1 = driver.current_window_handle
#     windows = driver.window_handles
#     time.sleep(2)
#     for current_window in windows:
#         if current_window != window_1:
#             driver.switch_to.window(current_window)
#             driver.close()
#             driver.switch_to.window(window_1)
#
#
# # 定义通过xpath鼠标点击接口，切换窗口到新窗口后，在切换回之前窗口
# # 复选框循环点击,复选框内定义了列表a，在列表a内寻找title
# def switchHandlec(c, a):
#     checkboxs = driver.find_elements_by_xpath(c)
#     for k in checkboxs:
#         k.click()
#         time.sleep(2)
#         window_1 = driver.current_window_handle
#         windows = driver.window_handles
#         time.sleep(2)
#         for current_window in windows:
#             if current_window != window_1:
#                 driver.switch_to.window(current_window)
#                 title = driver.title
#                 title_name = a
#                 for b in title_name:
#                     if title == b:
#                         print(b, end="\n" + "页面打开成功 ")
#                         i = datetime.datetime.now().replace(microsecond=0)
#                         print("%s" % i, end="\n")
#                         break
#                 driver.close()
#                 driver.switch_to.window(window_1)
#
#
# # 定义定义通过xpath键盘回车点击接口，切换窗口到新窗口后，在切换回之前窗口
# def switchHandled(d):
#     driver.find_element_by_xpath(d).send_keys(Keys.ENTER)
#     window_1 = driver.current_window_handle
#     windows = driver.window_handles
#     time.sleep(2)
#     for current_window in windows:
#         if current_window != window_1:
#             driver.switch_to.window(current_window)
#             driver.close()
#             driver.switch_to.window(window_1)
#
#
# def switchHandlee(e):
#     checkboxs = driver.find_elements_by_xpath(e)
#     for k in checkboxs:
#         k.click()
#         time.sleep(2)
#         window_1 = driver.current_window_handle
#         windows = driver.window_handles
#         time.sleep(2)
#         for current_window in windows:
#             if current_window != window_1:
#                 driver.switch_to.window(current_window)
#                 driver.close()
#                 driver.switch_to.window(window_1)
#
#
# for i in range(1, 3):
#     print('安美网的第%d次测试开始' % i, end="\n")
#     datatime()
#     # driver实列化
#     driver = webdriver.Chrome()
#     # 浏览器运行到指定网址
#     driver.get('http://tjamjh.com/')
#     # 等待2秒
#     time.sleep(2)
#     # 窗口最大化
#     driver.maximize_window()
#     # 调用判断标题的方法
#     title_judge('传递窗_高效过滤器_净化板_净化复合板_库板_彩钢夹芯净化复合板-天津市安美空调净化设备有限公司')
#     print('天津安美页面正确打开')
#     switchHandle('/html/body/table[1]/tbody/tr/td[1]/a/img',
#                  '传递窗_高效过滤器_净化板_净化复合板_库板_彩钢夹芯净化复合板-天津市安美空调净化设备有限公司')
#     print('左上角图标点击成功')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[1]/a').click()
#     title_judge('传递窗_高效过滤器_净化板_净化复合板_库板_彩钢夹芯净化复合板-天津市安美空调净化设备有限公司')
#     print('首页点击成功')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[2]/a').click()
#     title_judge('公司简介-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[3]/a').click()
#     title_judge('新闻中心-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[4]/a').click()
#     title_judge('净化产品-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[5]/a').click()
#     title_judge('招聘信息-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[6]/a').click()
#     title_judge('公司相册-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[7]/a').click()
#     title_judge('在线留言-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[8]/a').click()
#     title_judge('业绩展示-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[9]/a').click()
#     title_judge('联系我们-天津市安美空调净化设备有限公司')
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="navigation"]/li[1]/a').click()
#     time.sleep(2)
#     driver.find_element_by_xpath('/html/body/table[4]/tbody/tr/td[2]/table[2]/'
#                                  'tbody/tr[1]/td/table/tbody/tr/td[1]/a/img').click()
#     time.sleep(2)
#     driver.back()
#     time.sleep(2)
#     switchHandlee('/html/body/table[4]/tbody/tr/td[3]/table/tbody/'
#                   'tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr/td[2]/a')
#     print('公司新闻浏览成功')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[1]'
#              '/tbody/tr[2]/td[2]/a', '复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[2]'
#              '/tbody/tr[2]/td[2]/a', '高效过滤器-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[3]'
#              '/tbody/tr[2]/td[2]/a', '风淋室-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[4]'
#              '/tbody/tr[2]/td[2]/a', '传递窗-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[5]'
#              '/tbody/tr[2]/td[2]/a', '工作台-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[6]'
#              '/tbody/tr[2]/td[2]/a', '净化门窗-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[7]'
#              '/tbody/tr[2]/td[2]/a', '送风口-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[1]/table/tbody/tr[2]/td/table[8]'
#              '/tbody/tr[2]/td[2]/a', '其他净化产品-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table'
#              '/tbody/tr/td/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '彩钢复合板-复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table'
#              '/tbody/tr/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '岩棉复合板-复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[1]/tbody/tr/td/table'
#              '/tbody/tr/td/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '聚氨酯复合板-复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '不锈钢复合板-复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '净化板衔接-复合板-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[2]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '风淋室及传递窗-风淋室-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '高效过滤器-高效过滤器-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '活性炭过滤器-高效过滤器-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[3]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '空气过滤器-高效过滤器-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[4]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '风淋传递窗-传递窗-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[4]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[2]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '洁净传递窗-传递窗-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[5]/tbody/tr/td[2]/table/tbody/tr[2]/td/table[4]/tbody/tr[2]/td/table'
#              '/tbody/tr/td/table/tbody/tr/td/div[3]/table/tbody/tr[1]/td/table/tbody/tr/td/div/a/img',
#              '普通传递窗-传递窗-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[1]',
#              '公司简介-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[2]',
#              '新闻中心-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[3]',
#              '净化产品-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[4]',
#              '招聘信息-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[5]',
#              '公司相册-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[6]',
#              '在线留言-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[7]',
#              '业绩展示-天津市安美空调净化设备有限公司')
#     testName('/html/body/table[6]/tbody/tr/td[2]/table/tbody/tr/td[3]/table/tbody/tr[1]/td/a[8]',
#              '联系我们-天津市安美空调净化设备有限公司')
#     switchHandlec('/html/body/table[7]/tbody/tr/td/a',
#                   ['复合板-天津市安美空调净化设备有限公司',
#                    '复合板-天津市安美空调净化设备有限公司',
#                    '传递窗-天津市安美空调净化设备有限公司',
#                    '风淋室-天津市安美空调净化设备有限公司',
#                    '高效过滤器-天津市安美空调净化设备有限公司'])
#     print('安美网的第%d次测试结束' % i, end="\n")
#     datatime()
#     print(end='\n')
#     driver.quit()