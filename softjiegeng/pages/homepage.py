# coding = utf - 8
from selenium.webdriver import ActionChains
from selenium import webdriver
from softjiegeng.common.log import Logger
from softjiegeng.pages.basepage import BasePage
from softjiegeng.pages.detailspage import DetailsPage

mylogger = Logger(logger = "桔梗软件站首页").getlog()

class HomePage(DetailsPage, BasePage):

    def homepage_tuijian(self):
        self.click_by_xpath("/html/body/div/div[1]/div/a/img")
        self.sleep(1)
        article = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/a/em')
        ActionChains(self.driver).move_to_element(article).perform()
        self.inputkeys_by_xpath('//*[@id="searchkey"]',"加速器")
        self.sleep(1)
        self.click_by_xpath('/html/body/div/div[1]/div/div[2]/form/input[5]')
        self.sleep(1)
        self.back()
        self.click_by_xpath('//*[@id="fixbar"]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[1]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[2]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[3]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[4]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[5]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[6]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[7]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[8]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[9]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[10]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[11]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[12]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[13]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[14]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[15]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[16]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[17]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[18]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[19]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[20]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[21]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/dl/dd[22]/a')
        self.sleep(1)
        self.click_by_xpath('//*[@id="fixbar"]/a')
        self.sleep(1)
        self.radio_click('//*[@id="focus1"]/ul/li/a/img')

    def homepage_xiazai_01(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[1]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_02(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[2]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_03(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[3]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_04(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[4]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_05(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[5]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_06(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[6]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_07(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[7]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_08(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[8]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_09(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[9]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_10(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[10]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_11(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[11]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_12(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[12]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_13(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[13]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_14(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[14]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_15(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[15]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_16(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[16]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_17(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[17]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_18(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[18]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_19(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[19]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_20(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[20]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_21(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[21]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_22(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[22]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_23(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[23]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_24(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[24]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_25(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[25]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_26(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[26]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_27(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[27]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_28(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[28]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_29(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[29]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_30(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[3]/div[2]/ul/li[30]/a[1]/img')
        self.detailspage()

    def homepage_xiazai_31(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[1]/a[1]/span')
        self.detailspage()

    def homepage_xiazai_32(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[2]/a[1]/span')
        self.detailspage()

    def homepage_xiazai_33(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[3]/a[1]/span')
        self.detailspage()

    def homepage_xiazai_34(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[4]/a')
        self.detailspage()

    def homepage_xiazai_35(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[5]/a')
        self.detailspage()

    def homepage_xiazai_36(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[6]/a')
        self.detailspage()

    def homepage_xiazai_37(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[7]/a')
        self.detailspage()

    def homepage_xiazai_38(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[8]/a')
        self.detailspage()

    def homepage_xiazai_39(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[9]/a')
        self.detailspage()

    def homepage_xiazai_40(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[10]/a')
        self.detailspage()

    def homepage_xiazai_41(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[11]/a')
        self.detailspage()

    def homepage_xiazai_42(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[12]/a')
        self.detailspage()

    def homepage_xiazai_43(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[13]/a')
        self.detailspage()

    def homepage_xiazai_44(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[14]/a')
        self.detailspage()

    def homepage_xiazai_45(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[15]/a')
        self.detailspage()

    def homepage_xiazai_46(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[16]/a')
        self.detailspage()

    def homepage_xiazai_47(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[17]/a')
        self.detailspage()

    def homepage_xiazai_48(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[18]/a')
        self.detailspage()

    def homepage_xiazai_49(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[19]/a')
        self.detailspage()

    def homepage_xiazai_50(self):
        self.click_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div[2]/ol/li[20]/a')
        self.detailspage()

if __name__ == "__main__":
    hpage = HomePage(webdriver.Chrome())
    hpage.start_browser()
    hpage.homepage_tuijian()
    hpage.homepage_xiazai_01()
    hpage.quit_browser()