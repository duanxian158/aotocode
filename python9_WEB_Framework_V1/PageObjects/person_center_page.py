# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 16:05
# @Author  : wangna
# @FileName: person_center_page.py
import logging
from PageLocators.person_center_page_locator import PersonCenterPageLocator
from Common.base_page import BasePage
#个人中心页面
class PersonCenterPage(BasePage,PersonCenterPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #获取个人名称
    def get_countname(self):
        name = "获取个人账户名称"
        self.wait_eleVisible(self.person_name,model=name)
        logging.info(self.get_text(self.person_name))
        return self.get_text(self.person_name,model=name)
    #返回个人手机号
    def get_phone(self):
        """
        返回个人账户手机号
        :return:
        """
        name = "获取个人手机号"
        self.wait_eleVisible(self.accout_phone,model=name)
        return self.get_text(self.accout_phone,model=name)

    #点击导航栏-简历管理
    def click_resumemanage(self):
        name = "个人中心页面-点击简历管理"
        self.wait_eleVisible(self.resume_menu,model=name)
        self.click_element(self.resume_menu,model=name)

    #点击导航栏-岗位搜索
    def click_jobsearch(self):
        name = "岗位搜索"
        self.wait_eleVisible(self.jobsearch_menu,model=name)
        self.click_element(self.jobsearch_menu,model=name)

    #点击导航栏-岗位推荐
    def click_jobrecommen(self):
        name = "个人中心页面-岗位搜索"
        self.wait_eleVisible(self.jobrecommend_menu,model=name)
        self.click_element(self.jobrecommend_menu,model=name)