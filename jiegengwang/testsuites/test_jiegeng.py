# _*_ coding:utf-8 _*_
import unittest
from jiegengwang.jiegeng_framework.jghome import *
from selenium import webdriver
from jiegengwang.common.warning import message

jghome = JgHome(webdriver.Chrome())

class JieGen_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        jghome.start_browser()
        message("https://www.jiegeng.com自动化测试开始")

    @classmethod
    def tearDownClass(cls):
        jghome.driver.quit()
        message("https://www.jiegeng.com自动化测试已结束")

    def test_01(self):
        jghome.top_moudle()

    def test_01_login(self):
        jghome.login_jiegeng("zhanghao", "h502n0e0y7")

    def test_02(self):
        jghome.navigation_moudle()

    def test_03(self):
        jghome.id_site_moudle()

    def test_04(self):
        jghome.dianshiju_moudle()

    def test_05(self):
        jghome.remenyouxi_moudle()

    def test_06(self):
        jghome.box_famoussite_moudle()

    def test_07(self):
        jghome.id_layout_moudle()

    def test_08(self):
        jghome.frame_moudle()

    def test_09(self):
        jghome.toplist_soft_moudle()

    def test_10(self):
        jghome.coolsite_moudle()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
