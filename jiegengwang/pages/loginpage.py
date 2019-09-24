# coding=utf-8
from selenium import webdriver
from jiegengwang.common.log import Logger
from jiegengwang.pages.basepage import BasePage

mylogger = Logger(logger="桔梗网登录模块").getlog()
class Login_Jiegeng(BasePage):
    def login_jiegeng(self, username, password):
        self.driver.find_element_by_xpath('//*[@id="login"]/span[1]').click()
        mylogger.info("点击注册按钮")
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/input').send_keys(username)
        mylogger.info("输入用户名：%s" % username)
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/input').send_keys(password)
        mylogger.info("输入密码：%s" % password)
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[4]/input').click()
        self.sleep(2)
        self.driver.switch_to.alert.accept()
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login"]/span[2]').click()
        mylogger.info("点击登录按钮")
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/input').clear()
        mylogger.info("清空用户名栏")
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/input').clear()
        mylogger.info("清空密码栏")
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[2]/input').send_keys(username)
        mylogger.info("输入用户名：%s" % username)
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[3]/input').send_keys(password)
        mylogger.info("输入密码：%s" % password)
        self.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="login_form"]/form/div[4]/input').click()
        mylogger.info("点击登录")
        self.sleep(2)
        self.driver.switch_to.alert.accept()
        mylogger.info("登录成功")


if __name__ == "__main__":
    Ljg = Login_Jiegeng(webdriver.Chrome())
    Ljg.start_browser()
    Ljg.login_jiegeng("zhanghao", "h502n0e0y7")
    Ljg.quit_browser()