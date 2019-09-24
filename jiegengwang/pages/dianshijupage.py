# coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from jiegengwang.pages.basepage import BasePage
from jiegengwang.common.log import Logger

mylogger = Logger(logger = "桔梗网电视剧模块").getlog()
class DianShiJu_Moudle(BasePage):

    def switchHandle_Dianshiju(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.close()
        self.driver.switch_to.window(windows[1])

    def switchHandle_Dianshiju_Panduan(self, xpath, titname, pagename):
        self.driver.find_element_by_xpath(xpath).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        title = self.driver.title
        if title == titname:
            mylogger.info(pagename + "打开成功 ")
        else:
            mylogger.info(pagename + "打开失败 ")
        self.driver.close()
        self.driver.switch_to.window(windows[1])

    def switchHandle_DianShiJu_XunHuanPanDuan(self, xpath, title_name):
        self.driver.find_element_by_xpath(xpath).click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        title = self.driver.title
        for c in title_name:
            if title == c:
                mylogger.info(c + "页面打开成功 ")
                break
        self.driver.close()
        self.driver.switch_to.window(windows[1])

    def switchHandle_DianShiJu_CheckBoxs(self, xpath):
        checkboxs = self.driver.find_elements_by_xpath(xpath)
        for k in checkboxs:
            k.click()
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])
            self.driver.close()
            self.driver.switch_to.window(windows[1])
    
    def dianshiju_moudle(self):
        self.click_by_xpath('//*[@id="menus"]/li[2]/a/span')
        window_first = self.driver.current_window_handle
        windows = self.driver.window_handles
        for current_window in windows:
            if current_window != window_first:
                self.driver.switch_to.window(current_window)
                title = self.driver.title
                if title == "桔梗电视剧大全 - 更新更全更好看的电视剧网站在线观看 - 2019新电视剧":
                    mylogger.info("电视剧页面打开成功 ")
                else:
                    mylogger.error("电视剧页面打开失败 ")
                self.driver.find_element_by_xpath('//*[@id="vheader"]/div[1]/div/a').click()
                self.sleep(3)
                article = self.driver.find_element_by_xpath('//*[@id="vheader"]/div[1]/div/div[1]/a/em')
                ActionChains(self.driver).move_to_element(article).perform()
                self.sleep(3)
                article = self.driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/input')
                ActionChains(self.driver).move_to_element(article).perform()
                self.inputkeys_by_xpath('//*[@id="searchForm"]/div[2]/input', "诛仙")
                self.click_by_xpath('//*[@id="search"]')
                self.driver.back()
                self.switchHandle_Dianshiju_Panduan('//*[@id="left_1"]/span',
                                                        '桔梗导航[www.jiegeng.com]_最实用的上网主页_上网就上桔梗网！',
                                                        '桔梗网首页')
                self.click_by_xpath('//*[@id="main_menu"]/div/p/a[3]/span')
                self.click_by_xpath('//*[@id="left_4"]/span')
                self.click_by_xpath('//*[@id="main_menu"]/div/p/a[5]/span')
                self.click_by_xpath('//*[@id="main_menu"]/div/p/a[3]/span')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[1]/dd/span/a')
                mylogger.info("地区复选框遍历完毕，无异常")
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[1]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[2]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[3]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[4]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[5]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[6]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[7]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[8]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[9]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[10]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[11]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[12]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[13]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[14]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[15]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[16]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[17]/a')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[2]/dd/span[18]/a')
                mylogger.info('类型复选框遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[1]/div[2]/dl[3]/dd/span/a')
                mylogger.info('年代复选框遍历完毕，无异常')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[1]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[2]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[3]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[4]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[5]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[6]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[7]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[8]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[9]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[11]/a')
                self.switchHandle_Dianshiju('//*[@id="mCSB_1_container"]/dl/dd/span[12]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[1]/div[3]/div[1]/div/div[2]/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('同步追剧遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[1]/div[4]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('本周最热遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="neidi"]/div/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('内地剧遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('/html/body/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('内地剧搜视榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="wangluoju"]/div/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('网络剧遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[3]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('网络剧搜视榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="hanguo"]/div/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('浪漫日韩遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[4]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('韩剧好评榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="meiguo"]/div/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('美剧热播遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[6]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('美剧强档榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="taiwan"]/div/div[2]/div/ul/li/div[1]/a/i')
                mylogger.info('风情·港台泰榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[7]/div[2]/div/div[2]/div/ul/li/a')
                mylogger.info('台剧人气榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[1]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[2]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[3]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[4]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[5]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="diezhan"]/div/div[2]/div/ul/li[6]/div[1]/a/i')
                mylogger.info('谍战剧 PK 抗战剧遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[1]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[2]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[3]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[4]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[5]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[6]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[7]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[8]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[9]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[10]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[9]/div[2]/div/div[2]/div/ul/li[11]/a')
                mylogger.info('谍战剧热播榜遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[1]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[2]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[3]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[4]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[5]/div[1]/a/i')
                self.switchHandle_DianShiJu_CheckBoxs('//*[@id="guzhuang"]/div/div[2]/div/ul/li[6]/div[1]/a/i')
                mylogger.info('唯美古风吹遍历完毕，无异常')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[1]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[2]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[3]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[4]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[5]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[6]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[7]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[8]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[9]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[10]/a')
                self.switchHandle_DianShiJu_CheckBoxs(
                    '/html/body/div[3]/div[3]/div[10]/div[2]/div/div[2]/div/ul/li[11]/a')
                mylogger.info('古装剧热播榜遍历完毕，无异常')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[1]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '战争抗日')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[2]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '古装武侠')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[3]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '警匪谍战')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[4]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '言情偶像')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[5]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '朴实农村')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[6]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '都市生活')
                self.switchHandle_Dianshiju_Panduan('/html/body/div[3]/div[3]/div[14]/p/a[7]',
                                                        '热播电视剧大全_收视率最高的连续剧推荐_好看的连续剧【桔梗电视剧】',
                                                        '全部分类')
                self.driver.close()
                self.driver.switch_to.window(window_first)

if __name__ == '__main__':
    dpage = DianShiJu_Moudle(webdriver.Chrome())
    dpage.start_browser()
    dpage.dianshiju_moudle()
    dpage.quit_browser()