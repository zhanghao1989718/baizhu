# coding = utf - 8
from selenium import webdriver
from softjiegeng.common.log import Logger
from softjiegeng.pages.basepage import BasePage

mylogger = Logger(logger = "桔梗软件站详情页").getlog()

class DetailsPage(BasePage):

    def detailspage(self):
        self.click_by_xpath('/html/body/div[3]/div/div[1]/h1/a/img')
        self.back()
        self.inputkeys_by_xpath('//*[@id="keyword"]', '腾讯视频')
        self.click_by_xpath('//*[@id="search_button"]')
        windows_2 = self.driver.window_handles
        self.driver.switch_to.window(windows_2[1])
        self.driver.close()
        self.driver.switch_to.window(windows_2[0])
        self.check_click('/html/body/div[3]/div/div/a')
        self.action_chains_check_click('/html/body/div[3]/div/div/p/i', '/html/body/div[3]/div/div/p/span/a')
        self.click_by_xpath('/html/body/div[6]/div/div[1]/div/div[1]/div')
        self.tuijiankuang_test()
        self.tuijiankuang_close()
        self.click_by_xpath('/html/body/div[6]/div/div[1]/div/div[2]/span[1]/b')
        self.tuijiankuang_close()
        self.click_by_xpath('/html/body/div[6]/div/div[1]/div/div[2]/span[2]/b')
        self.tuijiankuang_close()
        self.clicks_by_xpath('/html/body/div[6]/div/div[2]/ul/li/a')
        self.clicks_by_xpath('//*[@id="mtab"]')
        mylogger.info('id="mtab"点击成功')
        self.clicks_by_xpath('//*[@id="jrgx"]/li/p/span/a')
        mylogger.info('id="jrgx"点击成功')
        self.clicks_by_xpath('//*[@id="download"]/div/div[2]/div/span')
        mylogger.info('id="download"点击成功')
        self.clicks_by_xpath('//*[@id="xgd"]/div[2]/ul/li/p/a')
        mylogger.info('id="xgd"点击成功')
        self.clicks_by_xpath('//*[@id="reci"]/div/div/span')
        mylogger.info('id="reci"点击成功')
        self.clicks_by_xpath('//*[@id="recomc"]/ul/li/a')
        mylogger.info('id="recomc"点击成功')
        self.driver.back()



if __name__ == "__main__":
    dpage = DetailsPage(webdriver.Chrome())
    dpage.start_browser()
    dpage.click_by_xpath('//*[@id="focus1"]/ul/li/a/img')
    dpage.sleep(2)
    dpage.detailspage()
    dpage.quit_browser()