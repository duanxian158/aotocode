# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:51
# @Author  : wangna
# @FileName: job_detail_page.py

#个人中心-岗位搜索-岗位详情页面操作
import time
from PageLocators.PersonalCenterLocators.job_detail_page_locator import JobDetailPageLocator
from Common.base_page import BasePage
class JobDetailPage(BasePage,JobDetailPageLocator):
    def __init__(self,drive):
        self.driver = drive
    #申请职位
    def apply_job(self):
        name = "投递岗位"
        self.get_window_handel()
        self.wait_eleVisible(self.applyjob_button,model=name)
        self.click_element(self.applyjob_button,model=name)

    #返回申请成功提示
    def get_noticecontent(self):
        name = "投递岗位成功提示"
        self.wait_eleVisible(self.noticecontent,model=name)
        return self.get_text(self.noticecontent,model=name)

    #收藏职位
    def collect_job(self):
        name = "收藏职位"
        self.get_window_handel()
        self.wait_eleVisible(self.collectjob_button,model=name)
        self.click_element(self.collectjob_button,model=name)