# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 14:32
# @Author  : wangna
# @FileName: job_ recommen_page.py

#简历推荐页面操作
from PageLocators.PersonalCenterLocators.job_recommen_page_locator import JobRecommenPageLocator
from Common.base_page import BasePage
class JobRecommenPage(BasePage,JobRecommenPageLocator):
    def __init__(self,driver):
        self.driver = driver
    #点击岗位名称
    def click_jobname(self):
        name = "简历推荐页面-点击岗位名称"
        self.wait_eleVisible(self.onejobname_link,model=name)
        self.click_element(self.onejobname_link,model=name)