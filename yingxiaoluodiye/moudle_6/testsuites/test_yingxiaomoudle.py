# _*_ coding:utf-8 _*_
import unittest
from selenium import webdriver
from yingxiaoluodiye.moudle_6.pages.homepage import HomePage
from yingxiaoluodiye.moudle_6.common.warning import message

hpage = HomePage(webdriver.Chrome())
class YingXiao_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        hpage.start_browser()
        message("自动化测试开始")

    @classmethod
    def tearDownClass(cls):
        hpage.driver.quit()
        message("自动化测试结束")

    def test_01(self):
        hpage.homepage_test()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
