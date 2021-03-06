# coding=utf-8
from selenium import webdriver
from jiegengwang.common.log import Logger
from jiegengwang.pages.basepage import BasePage
from jiegengwang.pages.dianshijupage import DianShiJu_Moudle
from jiegengwang.pages.loginpage import Login_Jiegeng
from jiegengwang.pages.remenyouxipage import ReMenYouXi_Moudle

mylogger = Logger(logger="桔梗网首页").getlog()
class JgHome(Login_Jiegeng, ReMenYouXi_Moudle, DianShiJu_Moudle, BasePage):

    def top_moudle(self):
        self.titpd("桔梗导航")
        self.radio_click_pd('//*[@id="weaoo_container"]/div[1]/div[1]/div[1]/span/a', '围观天气')
        self.radio_click_pd('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[1]', '围观天气')
        self.click_by_xpath('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[2]')
        self.refresh()
        self.radio_click('//*[@id="weaoo_container"]/div[1]/div[2]/div[1]/a/div[2]')
        mylogger.info('今日天气点击成功')
        self.radio_click('//*[@id="weaoo_container"]/div[1]/div[2]/div[2]/a/div[2]')
        mylogger.info('明日天气点击成功')
        self.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[1]', '日历_百度搜索')
        self.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[2]', '日历_百度搜索')
        self.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[3]', '生肖查询_百度搜索')
        self.radio_click_pd('//*[@id="calendar"]/div/span[2]/a[1]', '日历_百度搜索')
        self.radio_click_pd('//*[@id="calendar"]/div/span[2]/a[2]', '星座运势_百度搜索')
        self.radio_click('//*[@id="headJoke"]/a/span')
        mylogger.info('顶部游戏推荐栏遍历成功')
        # self.radio_click('//*[@id="header"]/div[1]/div/div[4]/div/div/a/img')
        # mylogger.info('顶部游戏图片遍历成功')
        self.radio_click_pd('//*[@id="eng-logo"]', '360搜索，SO靠谱')
        self.click_by_xpath('//*[@id="g-toggle"]')
        self.inputkeys_by_xpath('//*[@id="search-input"]', '下载器')
        # sleep(3)
        self.radio_click_pd('//*[@id="search-form"]/div[3]/input', '下载器_360搜索')
        mylogger.info("顶部模块测试完成")

    def navigation_moudle(self):
        self.radio_click('//*[@id="menus"]/li[1]/a/span')
        self.radio_click_pd('//*[@id="menus"]/li[2]/a/span', '电视剧')
        self.radio_click_pd('//*[@id="menus"]/li[3]/a/span', '软件下载')
        self.radio_click('//*[@id="menus"]/li[4]/a/span')
        self.radio_click('//*[@id="menus"]/li[5]/a/span')
        self.radio_click('//*[@id="menus"]/li[6]/a/span')
        self.radio_click_pd('//*[@id="menus"]/li[7]/a/span', '桔梗网页游戏')
        self.radio_click_pd('//*[@id="menus"]/li[8]/a/span', '桔梗小游戏')
        self.radio_click('//*[@id="menus"]/li[9]/a/span')
        self.radio_click_pd('//*[@id="menus"]/li[10]/a/span', '携程旅行网官网')
        self.radio_click('//*[@id="menus"]/li[11]/a/span')
        self.radio_click_pd('//*[@id="menus"]/li[11]/a/span', '桔梗益智类小游戏')
        self.radio_click('//*[@id="menus"]/li[1]/a/span')
        mylogger.info("导航模块测试完成")

    def id_site_moudle(self): # 信息流模块
        self.check_click('//*[@id="box-starbar"]/div/a')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[1]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[2]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[3]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[4]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[5]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[6]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[7]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[8]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[9]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[10]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[11]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[12]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[13]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[14]/a[1]')
        self.check_click('//*[@id="site"]/div[1]/ul/li[15]/a[2]/img')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[16]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[17]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[18]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[19]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[20]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[21]/a[1]')
        self.check_click('//*[@id="site"]/div[1]/ul/li[22]/a[2]/img')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[23]/a[1]')
        self.radio_enterkey('//*[@id="site"]/div[1]/ul/li[24]/a[1]')
        mylogger.info('id="site"遍历成功')

    def box_famoussite_moudle(self):
        self.radio_enterkey('//*[@id="box-famoussite"]/div/ul/li/a')
        mylogger.info('id="box-famoussite"遍历成功')
        self.check_click('// *[ @ id = "hlbar"] / span')
        mylogger.info('id = "hlbar"遍历成功')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[1] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[2] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[3] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[4] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[5] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[6] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[7] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[8] / a / span')
        self.radio_click('// *[ @ id = "topzixun-over"] / div / p[9] / a / span')
        mylogger.info('id = topzixun-over遍历成功')

    def id_layout_moudle(self):
        self.check_click('//*[@id="infoflow-list"]/div/div[1]/a/img')
        self.radio_click('//*[@id="topzixun-over"]/div/p[1]/a[@data-id = "10466"]')
        self.radio_click('//*[@id="topzixun-over"]/div/p[2]/a[@data-id = "10467"]')
        self.radio_click('//*[@id="topzixun-over"]/div/p[3]/a[@data-id = "10468"]')
        self.check_click('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div/p[1]/a/span')
        self.check_click('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div[2]/p/a/span')

    def frame_moudle(self):
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[1]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[2]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[3]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[4]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[5]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[6]/a')
        self.switchframe('//*[@id="wrapper"]/div[1]/ul/li[7]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[1]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[2]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[3]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[4]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[5]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[6]/a')
        self.switchframe('//*[@id="wrapper"]/div[2]/ul/li[7]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[1]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[2]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[3]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[4]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[5]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[6]/a')
        self.switchframe('//*[@id="wrapper"]/div[3]/ul/li[7]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[1]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[2]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[3]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[4]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[5]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[6]/a')
        self.switchframe('//*[@id="wrapper"]/div[4]/ul/li[7]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[1]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[2]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[3]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[4]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[5]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[6]/a')
        self.switchframe('//*[@id="wrapper"]/div[5]/ul/li[7]/a')

    def toplist_soft_moudle(self):
        self.check_click('//*[@id="toplist-soft"]/div/div/div[2]/div/p/a')
        self.radio_click('//*[@id="navigate"]/a[1]/span')
        self.radio_click('//*[@id="navigate"]/a[2]/span')
        self.radio_click('//*[@id="navigate"]/a[3]/span')
        self.radio_click('//*[@id="navigate"]/a[4]/span')
        self.radio_click('//*[@id="navigate"]/a[5]/span')
        self.radio_click('//*[@id="navigate"]/a[6]/span')
        self.radio_click('//*[@id="navigate"]/a[7]/span')
        self.radio_click('//*[@id="navigate"]/a[8]/span')
        self.radio_click('//*[@id="navigate"]/a[9]/span')
        self.radio_click('//*[@id="navigate"]/a[10]/span')
        self.radio_click('//*[@id="navigate"]/a[11]/span')
        self.radio_click('//*[@id="navigate"]/a[12]/span')

    def coolsite_moudle(self):
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[1]/span[8]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[2]/span[8]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[3]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[5]/span[8]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[6]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[1]')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[2]')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[3]')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[6]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[7]/span[7]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[2]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[3]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[4]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[5]/a')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[1]')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[2]')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[3]')
        self.radio_click('//*[@id="coolsite-group0"]/div[8]/span[7]/a')
        mylogger.info('id="coolsite-group0"遍历成功')
        self.check_click('//*[@id="coolsite-group1"]/div[1]/a')
        self.check_click('//*[@id="coolsite-group1"]/div/span/a')
        mylogger.info('id="coolsite-group1"遍历成功')
        # self.radio_click('//*[@id="gimgl2"]/a[1]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[2]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[3]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[4]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[5]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[6]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[7]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[8]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[9]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[10]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[11]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[12]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[13]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[14]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[15]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[16]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[17]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[18]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[19]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[20]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[21]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[22]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[23]/img')
        # self.radio_click('//*[@id="gimgl2"]/a[24]/img')
        # mylogger.info('id="gimgl2"遍历成功')
        # self.radio_click('//*[@id="shortvideo_slider1"]/div/div/ul/li[1]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[1]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[2]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[3]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[4]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[5]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[6]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[7]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[8]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[9]/a/img')
        # self.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div/div[10]/a/img')
        # mylogger.info('id="shortvideo_slider2遍历成功')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[1]/a/img')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[2]/a/img')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[3]/a/img')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[4]/a/img')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[5]/a/img')
        # self.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[6]/a/img')
        # mylogger.info('id="hao123-shortvideo"遍历成功')
        self.check_click('//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/ul/li/a')
        mylogger.info('id="slider_597985e4ce882遍历成功')


if __name__ == '__main__':
    dsjmodle = DianShiJu_Moudle(driver = webdriver.Chrome())
    dsjmodle.start_browser()

    #第一页：

    #top_hurdles_moudle(顶部模块)

    # dsjmodle.titpd("桔梗导航")
    # dsjmodle.radio_click_pd('//*[@id="weaoo_container"]/div[1]/div[1]/div[1]/span/a', '围观天气')
    # dsjmodle.radio_click_pd('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[1]', '围观天气')
    # dsjmodle.click_by_xpath('//*[@id="weaoo_container"]/div[1]/div[1]/div[2]/a[2]')
    # dsjmodle.refresh()
    # dsjmodle.radio_click('//*[@id="weaoo_container"]/div[1]/div[2]/div[1]/a/div[2]')
    # mylogger.info('今日天气点击成功')
    # dsjmodle.radio_click('//*[@id="weaoo_container"]/div[1]/div[2]/div[2]/a/div[2]')
    # mylogger.info('明日天气点击成功')
    # dsjmodle.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[1]', '日历_百度搜索')
    # dsjmodle.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[2]', '日历_百度搜索')
    # dsjmodle.radio_click_pd('//*[@id="calendar"]/div/span[1]/a[3]', '生肖查询_百度搜索')
    # dsjmodle.radio_click_pd('//*[@id="calendar"]/div/span[2]/a[1]', '日历_百度搜索')
    # dsjmodle.radio_click_pd('//*[@id="calendar"]/div/span[2]/a[2]', '星座运势_百度搜索')
    # dsjmodle.radio_click('//*[@id="headJoke"]/a/span')
    # mylogger.info('顶部游戏推荐栏遍历成功')
    # dsjmodle.radio_click('//*[@id="header"]/div[1]/div/div[4]/div/div/a/img')
    # mylogger.info('顶部游戏图片遍历成功')
    # dsjmodle.radio_click_pd('//*[@id="eng-logo"]', '360搜索，SO靠谱')
    # dsjmodle.click_by_xpath('//*[@id="g-toggle"]')
    # dsjmodle.inputkeys_by_xpath('//*[@id="search-input"]', '下载器')
    # # sleep(3)
    # dsjmodle.radio_click_pd('//*[@id="search-form"]/div[3]/input', '下载器_360搜索')
    # mylogger.info("顶部模块测试完成")

    # navigation_moudle("导航模块")

    # dsjmodle.radio_click('//*[@id="menus"]/li[1]/a/span')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[2]/a/span', '电视剧')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[3]/a/span', '软件下载')
    # dsjmodle.radio_click('//*[@id="menus"]/li[4]/a/span')
    # dsjmodle.radio_click('//*[@id="menus"]/li[5]/a/span')
    # dsjmodle.radio_click('//*[@id="menus"]/li[6]/a/span')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[7]/a/span', '桔梗网页游戏')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[8]/a/span', '桔梗小游戏')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[9]/a/span', '爱淘宝')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[10]/a/span', '携程旅行网官网')
    # dsjmodle.radio_click('//*[@id="menus"]/li[11]/a/span')
    # dsjmodle.radio_click_pd('//*[@id="menus"]/li[11]/a/span', '桔梗益智类小游戏')
    # mylogger.info("导航模块测试完成")

    # frame_moudle(frame模块)

    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[1]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[2]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[3]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[4]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[5]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[6]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[1]/ul/li[7]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[1]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[2]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[3]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[4]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[5]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[6]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[2]/ul/li[7]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[1]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[2]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[3]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[4]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[5]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[6]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[3]/ul/li[7]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[1]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[2]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[3]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[4]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[5]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[6]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[4]/ul/li[7]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[1]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[2]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[3]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[4]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[5]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[6]/a')
    # dsjmodle.switchframe('//*[@id="wrapper"]/div[5]/ul/li[7]/a')
    # mylogger.info("frame模块测试完成")

   # information_moudle("信息流模块")
   #  dsjmodle.radio_click('//*[@id="layout-side"]/div[1]/div/ul/li[1]/a/img')
   #  dsjmodle.check_click('//*[@id="box-starbar"]/div/a')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[1]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[2]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[3]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[4]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[5]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[6]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[7]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[8]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[9]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[10]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[11]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[12]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[13]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[14]/a[1]')
   #  dsjmodle.check_click('//*[@id="site"]/div[1]/ul/li[15]/a[2]/img')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[16]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[17]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[18]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[19]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[20]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[21]/a[1]')
   #  dsjmodle.check_click('//*[@id="site"]/div[1]/ul/li[22]/a[2]/img')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[23]/a[1]')
   #  dsjmodle.radio_enterkey('//*[@id="site"]/div[1]/ul/li[24]/a[1]')
   #  mylogger.info('id="site"遍历成功')
   #  dsjmodle.radio_enterkey('//*[@id="box-famoussite"]/div/ul/li/a')
   #  mylogger.info('id="box-famoussite"遍历成功')
   #  dsjmodle.check_click('// *[ @ id = "hlbar"] / span')
   #  mylogger.info('id = "hlbar"遍历成功')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[1] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[2] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[3] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[4] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[5] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[6] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[7] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[8] / a / span')
   #  dsjmodle.radio_click('// *[ @ id = "topzixun-over"] / div / p[9] / a / span')
   #  mylogger.info('id = topzixun-over遍历成功')
   #  dsjmodle.check_click('//*[@id="infoflow-list"]/div/div[1]/a/img')
   #  dsjmodle.radio_click('//*[@id="topzixun-over"]/div/p[1]/a[@data-id = "10466"]')
   #  dsjmodle.radio_click('//*[@id="topzixun-over"]/div/p[2]/a[@data-id = "10467"]')
   #  dsjmodle.radio_click('//*[@id="topzixun-over"]/div/p[3]/a[@data-id = "10468"]')
   #  dsjmodle.check_click('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div/p[1]/a/span')
   #  dsjmodle.check_click('//*[@id="layout-side"]/div[3]/div[3]/div/div/div[2]/div[2]/p/a/span')
   #
   #  dsjmodle.check_list_pd('//*[@id="toplist-soft"]/div/div/div[2]/div/p/a',
   #                ['Microsoft Office Visio 2016',
   #                 '极速PDF转Word 免费下载_极速PDF转Word 免费版_极速PDF转Word -桔梗下载站',
   #                 '腾讯QQ 轻聊版',
   #                 '天气网天气预报',
   #                 '花椒直播免费下载_花椒直播免费版_花椒直播-桔梗下载站'
   #                 '微信电脑版',
   #                 '酷狗音乐',
   #                 '爱奇艺PPS影音',
   #                 '万能数据恢复大师',
   #                 '腾讯视频',
   #                 'YY语音（中国最大的视频直播软件）',
   #                 'QQ浏览器免费下载_QQ浏览器免费版_QQ浏览器-桔梗下载站', ])
   #  # dsjmodle.check_list_pd('//*[@id="navigate"]/a/span',
   #  #               ['桔梗电视剧大全 - 更新更全更好看的电视剧网站在线观看 - 2019新电视剧',
   #  #                '桔梗电影大全 - 更新电影_电影天堂_好看的电影排行榜_高清在线观看',
   #  #                '头条新闻_东方新闻',
   #  #                '娱乐新闻_东方资讯网',
   #  #                '军事头条_东方军事网'
   #  #                '在线小游戏,单机小游戏大全-桔梗小游戏',
   #  #                '2019网页游戏大全,更新好玩的网页游戏开服表-桔梗网页游戏',
   #  #                '淘抢购首页- 淘抢购',
   #  #                '爱淘宝-淘宝网购物分享平台',
   #  #                '桔梗综艺大全-最新综艺节目,更全更新好看的综艺节目在线观看',
   #  #                '软件下载中心、最安全的软件资源下载',
   #  #                '宜人贷借款,快捷、简单、无抵押无担保_宜人贷', ])
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[1]/span[8]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[2]/span[8]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[3]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[5]/span[8]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[6]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[1]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[2]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[2]/a[3]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[4]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[6]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[7]/span[7]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[2]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[3]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[4]/a')
   #  dsjmodle.sleep(3)
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[5]/a')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[1]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[2]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[6]/a[3]')
   #  dsjmodle.radio_click('//*[@id="coolsite-group0"]/div[8]/span[7]/a')
   #  mylogger.info('id="coolsite-group0"遍历成功')
    # dsjmodle.check_list_pd('//*[@id="coolsite-group1"]/div[1]/a',
    #               ['软件下载中心、最安全的软件资源下载',
    #                '彩票_福利彩票发行管理中心指定网络信息发布媒体-中彩网',
    #                '考试_桔梗上网导航',
    #                '爱淘宝-淘宝网购物分享平台',
    #                '没有找到站点'
    #                '东方体育新闻_NBA直播吧|足球直播吧|中超直播吧_体育直播吧',
    #                '东方体育新闻_NBA直播吧|足球直播吧|中超直播吧_体育直播吧',
    #                '娱乐新闻_东方资讯网',
    #                '头条新闻_东方新闻',
    #                '在线小游戏,单机小游戏大全-桔梗小游戏',
    #                '桔梗理财 – 专业互联网理财平台',
    #                '桔梗小说网', ])
    # dsjmodle.check_click('//*[@id="coolsite-group1"]/div/span/a')
    # mylogger.info('id="coolsite-group1"遍历成功')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[1]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[2]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[3]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[4]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[5]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[6]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[7]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[8]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[9]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[10]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[11]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[12]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[13]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[14]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[15]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[16]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[17]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[18]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[19]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[20]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[21]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[22]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[23]/img')
    # dsjmodle.radio_click('//*[@id="gimgl2"]/a[24]/img')
    # mylogger.info('id="gimgl2"遍历成功')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider1"]/div/div/ul/li[2]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[1]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[2]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[3]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[4]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[5]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[6]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[7]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[8]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[9]/a/img')
    # dsjmodle.radio_click('//*[@id="shortvideo_slider2"]/div/div/ul/li/div[1]/div[10]/a/img')
    # mylogger.info('id="shortvideo_slider2遍历成功')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[1]/a/img')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[2]/a/img')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[3]/a/img')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[4]/a/img')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[5]/a/img')
    # dsjmodle.radio_click('//*[@id="hao123-shortvideo"]/div[2]/div[2]/div[6]/a/img')
    # mylogger.info('id="hao123-shortvideo"遍历成功')
    # dsjmodle.check_click('//*[@id="slider_597985e4ce882"]/div/div/ul/li/div/ul/li/a')
    # mylogger.info('id="slider_597985e4ce882遍历成功')

    #退出浏览器
    dsjmodle.quit_browser()


