# _*_ coding:utf-8 _*_
import unittest
from selenium import webdriver
from softjiegeng_firefox.pages.homepage import HomePage
from softjiegeng_firefox.common.warning import message

hpage = HomePage(webdriver.Firefox())
class SoftJieGen_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        hpage.start_browser()
        message("自动化测试开始")

    @classmethod
    def tearDownClass(cls):
        hpage.driver.quit()
        message("自动化测试结束")

    def test_01(self):
        hpage.homepage_tuijian()

    def test_02(self):
        hpage.homepage_xiazai_01()

    def test_03(self):
        hpage.homepage_xiazai_02()

    def test_04(self):
        hpage.homepage_xiazai_03()

    def test_05(self):
        hpage.homepage_xiazai_04()

    def test_06(self):
        hpage.homepage_xiazai_05()

    def test_07(self):
        hpage.homepage_xiazai_06()

    def test_08(self):
        hpage.homepage_xiazai_07()

    def test_09(self):
        hpage.homepage_xiazai_08()

    def test_10(self):
        hpage.homepage_xiazai_09()

    def test_11(self):
        hpage.homepage_xiazai_10()

    def test_12(self):
        hpage.homepage_xiazai_11()

    def test_13(self):
        hpage.homepage_xiazai_12()

    def test_14(self):
        hpage.homepage_xiazai_13()

    def test_15(self):
        hpage.homepage_xiazai_14()

    def test_16(self):
        hpage.homepage_xiazai_15()

    def test_17(self):
        hpage.homepage_xiazai_16()

    def test_18(self):
        hpage.homepage_xiazai_17()

    def test_19(self):
        hpage.homepage_xiazai_18()

    def test_20(self):
        hpage.homepage_xiazai_19()

    def test_21(self):
        hpage.homepage_xiazai_20()

    def test_22(self):
        hpage.homepage_xiazai_21()

    def test_23(self):
        hpage.homepage_xiazai_22()

    def test_24(self):
        hpage.homepage_xiazai_23()

    def test_25(self):
        hpage.homepage_xiazai_24()

    def test_26(self):
        hpage.homepage_xiazai_25()

    def test_27(self):
        hpage.homepage_xiazai_26()

    def test_28(self):
        hpage.homepage_xiazai_27()

    def test_29(self):
        hpage.homepage_xiazai_28()

    def test_30(self):
        hpage.homepage_xiazai_29()

    def test_31(self):
        hpage.homepage_xiazai_30()

    def test_32(self):
        hpage.homepage_xiazai_31()

    def test_33(self):
        hpage.homepage_xiazai_32()

    def test_34(self):
        hpage.homepage_xiazai_33()

    def test_35(self):
        hpage.homepage_xiazai_34()

    def test_36(self):
        hpage.homepage_xiazai_35()

    def test_37(self):
        hpage.homepage_xiazai_36()

    def test_38(self):
        hpage.homepage_xiazai_37()

    def test_39(self):
        hpage.homepage_xiazai_38()

    def test_40(self):
        hpage.homepage_xiazai_39()

    def test_41(self):
        hpage.homepage_xiazai_40()

    def test_42(self):
        hpage.homepage_xiazai_41()

    def test_43(self):
        hpage.homepage_xiazai_42()

    def test_44(self):
        hpage.homepage_xiazai_43()

    def test_45(self):
        hpage.homepage_xiazai_44()

    def test_46(self):
        hpage.homepage_xiazai_45()

    def test_47(self):
        hpage.homepage_xiazai_46()

    def test_48(self):
        hpage.homepage_xiazai_47()

    def test_49(self):
        hpage.homepage_xiazai_48()

    def test_50(self):
        hpage.homepage_xiazai_49()

    def test_51(self):
        hpage.homepage_xiazai_50()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
