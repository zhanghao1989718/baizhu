# coding=utf-8
from selenium import webdriver
from jiegengwang.pages.basepage import BasePage
from jiegengwang.common.log import Logger

mylogger = Logger(logger="桔梗网热门游戏模块").getlog()


class ReMenYouXi_Moudle(BasePage):

    def switchHandle_remenyouxi(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.close()
        self.driver.switch_to.window(windows[1])

    def switchHandle_remenyouxi_CheckBoxs(self, xpath):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            self.driver.close()
            self.driver.switch_to.window(windows[1])

    def remenyouxi_moudle(self):
        self.click_by_xpath('//*[@id="menus"]/li[7]/a/span')
        window_first = self.driver.current_window_handle
        windows = self.driver.window_handles
        for current_window in windows:
            if current_window != window_first:
                self.driver.switch_to.window(current_window)
                title = self.driver.title
                if title == "2019网页游戏大全,更新好玩的网页游戏开服表-桔梗网页游戏":
                    mylogger.info("热门游戏页面打开成功 ")
                else:
                    mylogger.error("热门游戏页面打开失败 ")
                self.switchHandle_remenyouxi('//*[@id="view2"]/li[1]/a')
                self.switchHandle_remenyouxi('//*[@id="view2"]/li[2]/a')
                self.switchHandle_remenyouxi('//*[@id="view2"]/li[3]/a')
                self.switchHandle_remenyouxi('//*[@id="view2"]/li[4]/a')
                self.switchHandle_remenyouxi('//*[@id="view2"]/li[5]/a')
                self.switchHandle_remenyouxi_CheckBoxs('//*[@id="view3"]/div/a/img')
                self.switchHandle_remenyouxi_CheckBoxs('//*[@id="view5"]/li/a/span[2]')
                self.switchHandle_remenyouxi_CheckBoxs('//*[@id="view4"]/li/a/img')
                self.driver.close()
                self.driver.switch_to.window(window_first)


if __name__ == '__main__':
    dpage = ReMenYouXi_Moudle(webdriver.Chrome())
    dpage.start_browser()
    dpage.remenyouxi_moudle()
    dpage.quit_browser()