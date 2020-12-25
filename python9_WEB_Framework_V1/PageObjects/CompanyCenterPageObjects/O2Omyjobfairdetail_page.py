# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 15:43
# @Author  : wangna
# @FileName: O2Omyjobfairdetail_page.py

from PageLocators.CompanyCenterLocators.O2Omyjobfairdetail_page_locator import O2OMyJobFairDetailPageLocator
from Common.base_page import BasePage
class O2OMyJobFairDetailPage(BasePage,O2OMyJobFairDetailPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #获取审核状态
    def get_shzt(self):
        """
        O2O招聘会-入驻审核状态
        :return: shzt 审核状态
        """
        name="获取审核状态"
        self.wait_eleVisible(self.shzt,model=name)
        shzt = self.get_text(self.shzt,model=name)
        return shzt