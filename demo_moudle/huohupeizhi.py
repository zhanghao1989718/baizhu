# encoding=utf-8
from selenium import webdriver
import unittest, time
import os

# 定义桌面路径的方法
def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")

class TestDemo(unittest.TestCase):
    def setUp(self):
        # self.driver= webdriver.Firefox()
        # 创建一个FirefoxProfile的实例，用于存放自定义配置
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', get_desk_p() + '\\iDownload')
        # 将browser.download.folderList设置成2，表示将文件下载到指定路径
        # 设置成0表示下载到桌面；设置为1表示下载到默认路径
        profile.set_preference('browser.download.folderList', 2)
        # browser.helpApps.alwaysAsk.force对于未知的MIME类型文件会弹出窗口
        # 让用户处理，默认值为True,设定为False表示不会记录打开未知MIME类型
        # 文件方式
        profile.set_preference('browser.helpApps.alwaysAsk.force', False)
        # 在开始下载时是否显示下载管理器
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        # 设定为False会把下载框进行隐藏
        profile.set_preference('browser.download.manager.useWindow', False)
        # 默认值为True设置为false表示不获取焦点
        profile.set_preference('browser.download.manager.focusWhenStarting', False)
        # 下载exe文件弹出警告，默认值为True ，设置为False则不会弹出警告框
        profile.set_preference('browser.download.manager.alertOnEXEOpen', False)
        # browser.helperApps.neverAsk.openFile表示直接打开下载文件，不显示确认框
        # 默认值为空字符串，下行代码设定了多种文件的MIME类型
        # 例如 application/exe,表示.exe文件
        # application/execl 表示Excel类型的文件
        profile.set_preference('browser.helperApps.neverAsk.openFile', "application/pdf")
        # 对所给出的文件类型不在弹出提示框进行询问，直接保存在本地盘
        profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
                               'application/zip,application/octet-stream')
        # browser.download.manager.showAlertOnComplete设定下载文件结束后是否
        # 提示下载完成提示框
        profile.set_preference('browser.download.manager.showAlertOnComplete', False)
        # browser.download.manager.closeWhenDone 设定结束后是否自动关闭关闭下载框
        # 默认值是 True,设置为False表示不关闭下载管理器
        profile.set_preference("browser.download.manager.closeWhenDone", False)

        # 启动浏览器时，通过firefox_profile参数
        # 将自动配置添加到FirefoxProfile对象中
        self.driver = webdriver.Firefox(firefox_profile=profile)

    def test_dataPicker(self):
        # 访问webDriver驱动Firefox的驱动文件下载网址
        url = "http://soft.jiegeng.com/86/92365.html"
        self.driver.get(url)
        # 选择下载ZIP类型文件，使用application/zip指代此类型文件
        self.driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/div/div[2]/span[1]/i").click()
        # 等待加载下载文件
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
