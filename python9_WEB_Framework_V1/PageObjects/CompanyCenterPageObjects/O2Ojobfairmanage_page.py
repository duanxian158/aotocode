# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 15:43
# @Author  : wangna
# @FileName: O2Ojobfairmanage_page.py

from PageLocators.CompanyCenterLocators.O2Ojobfairmanage_page_locator import O2OJobFairManagePageLocator
from Common.base_page import BasePage
class O2OJobFairManagePage(BasePage,O2OJobFairManagePageLocator):
    """
    O2O招聘会管理页面操作
    :return
    """
    def __init__(self,driver):
        self.driver=driver
    def click_canbeO2Ojobfair(self):
        """
        点击可入O2O招聘会
        :return:
        """
        name = "O2O招聘会管理页面-点击可入驻招聘会"
        self.wait_eleVisible(self.canbejobfair_button,model=name)
        self.click_element(self.canbejobfair_button,model=name)
