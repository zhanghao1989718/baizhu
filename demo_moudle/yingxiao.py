from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "http://www.daque.cn/soft/655.html?tab=1745611"
# 隐形等待10秒时间
driver.implicitly_wait(10)
# 跳转网页
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(1)

driver.quit()
