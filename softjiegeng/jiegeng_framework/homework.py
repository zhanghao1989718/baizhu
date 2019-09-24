# coding=utf-8
from softjiegeng.common.log import Logger
from softjiegeng.pages.homepage import HomePage

mylogger = Logger(logger="桔梗软件站").getlog()


class HomeWork(HomePage):
    def homework(self):
        self.homepage_tuijian()
