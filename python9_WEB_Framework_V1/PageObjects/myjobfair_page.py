# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 10:14
# @Author  : wangna
# @FileName: myjobfair_page.py
from Common.base_page import BasePage
from PageLocators.myjobfair_page_locator import MyJobFariPageLocator
class MyJobFairPage(MyJobFariPageLocator,BasePage):
    #点击菜单栏-可入驻招聘会
    def __init__(self,driver):
        self.driver=driver
    def click_canbejobfair(self):
        name="点击可入驻招聘会"
        self.click_element(self.canbejobfair_button,model=name)