# coding = utf - 8
from selenium import webdriver
from yingxiaoluodiye.moudle_8.common.log import Logger
from yingxiaoluodiye.moudle_8.pages.basepage import BasePage


mylogger = Logger(logger = "营销8#模板首页").getlog()

class HomePage(BasePage):
    def tuijiankuang_test(self):
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[1]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[1]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[2]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[2]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[3]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[3]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[4]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[2]/span[4]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="next"]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[1]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[1]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[2]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[2]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[3]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[3]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[4]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[3]/span[4]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="next"]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[1]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[1]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[2]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[2]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[3]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[3]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[4]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="list"]/ul/li[4]/span[4]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[1]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[1]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[2]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[2]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[3]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[3]/a[2]')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[4]/a[1]/img')
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[3]/div/div[2]/div/div/ul/li/span[4]/a[2]')
        self.sleep(1)

    def tuijiankuang_close(self):
        self.click_by_xpath('//*[@id="bzPopBox"]/div/div[1]/a')

    def homepage_test(self):
        self.click_by_xpath('//*[@id="bzWrap"]/div[1]/div/img')
        self.tuijiankuang_test()
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[1]/img')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[1]/div')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/h1')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/ul/li[1]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/ul/li[2]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/ul/li[3]/span')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/ul/li[1]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/ul/li[2]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/p')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/h3')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[1]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[1]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[2]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[2]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[3]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[3]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[4]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[4]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[5]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[5]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[6]/span[1]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="history"]/ul/li[6]/span[2]')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[2]/div/div[2]/div/img')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[3]/div/h2')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[3]/div/p')
        self.tuijiankuang_close()
        self.sleep(1)
        self.click_by_xpath('//*[@id="bzWrap"]/div[3]/div/img')
        self.tuijiankuang_close()


if __name__ == "__main__":
    hpage = HomePage(driver=webdriver.Chrome(), showid=8)
    hpage.start_browser()
    hpage.sleep(2)
    hpage.homepage_test()
    hpage.sleep(2)
    hpage.quit_browser()