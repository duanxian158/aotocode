# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 16:05
# @Author  : wangna
# @FileName: unpublish_job_page.py

from Common.base_page import BasePage
from PageLocators.CompanyCenterLocators.unpublish_job_page_locator import UnPublishJobPageLocator

class UnPublishJobPage(BasePage,UnPublishJobPageLocator):
    """
    未发布岗位页面操作
    :return
    """
    #点击创建岗位按钮
    def click_create_job(self):
        """
        点击创建岗位
        :return:
        """
        name = "未发布岗位页面-点击创建岗位"
        self.wait_eleVisible(self.createjob_button,model=name)
        self.click_element(self.createjob_button,model=name)