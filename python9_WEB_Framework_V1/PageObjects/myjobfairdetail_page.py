# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 17:03
# @Author  : wangna
# @FileName: myjobfairdetail_page.py
from PageLocators.myjobfairdetail_page_locator import MyJobFairDetailPageLocator
from Common.base_page import BasePage
class MyJobFairDetailPage(BasePage,MyJobFairDetailPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #获取审核状态
    def get_shzt(self):
        name="获取审核状态"
        self.wait_eleVisible(self.shzt,model=name)
        shzt = self.get_text(self.shzt,model=name)
        return shzt
