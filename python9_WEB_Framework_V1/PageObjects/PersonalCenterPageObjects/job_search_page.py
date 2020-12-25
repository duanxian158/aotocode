# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:49
# @Author  : wangna
# @FileName: job_search_page.py

#岗位搜索页面操作
import time
from PageLocators.PersonalCenterLocators.job_search_page_locator import JobSearchPageLocator
from Common.base_page import BasePage
class JobSearchPage(BasePage,JobSearchPageLocator):
    def __init__(self,drive):
        self.driver = drive
    #点击岗位名称
    def click_jobnmae(self):
        name = "个人中心-岗位搜索-点击岗位名称"
        self.wait_eleVisible(self.jobname_link,model=name)
        self.click_element(self.jobname_link,model=name)
        time.sleep(3)

    #申请职位
    def click_aplly_job(self):
        """
        岗位搜索页面-申请职位
        :return:
        """
        name = "岗位搜索-申请职位"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        self.wait_eleVisible(self.applyjob_button,model=name)
        self.click_element(self.applyjob_button,model=name)


    #返回申请成功提示
    def get_noticecontent(self):
        name = "投递岗位成功提示"
        self.wait_eleVisible(self.noticecontent,model=name)
        return self.get_text(self.noticecontent,model=name)
