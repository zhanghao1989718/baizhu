# coding=utf-8
from softjiegeng_firefox.common.log import Logger
from softjiegeng_firefox.pages.homepage import HomePage

mylogger = Logger(logger="桔梗软件站").getlog()


class HomeWork(HomePage):
    def homework(self):
        self.homepage_tuijian()
