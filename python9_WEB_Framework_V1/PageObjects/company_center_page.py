# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 9:42
# @Author  : wangna
# @FileName: company_center_page.py
from PageLocators.company_center_page_locator import CompanyCenterPageLocator
from Common.base_page import BasePage
class CompanyCenterPage(CompanyCenterPageLocator,BasePage):
    def __init__(self,driver):
        self.driver=driver

    #点击岗位管理
    def click_jobmanage(self):
        """
        点击岗位管理
        :return:
        """
        name = "点击岗位管理"
        self.wait_eleVisible(self.jobmanage_menu,model=name)
        self.click_element(self.jobmanage_menu,model=name)

    def cilick_jobfair(self):
        name = "点击网络招聘会"
        self.wait_eleVisible(self.jobfair_button,model=name)
        #点击招聘会管理
        self.click_element(self.jobfair_button,model=name)
        #点击网络招聘会
        self.wait_eleVisible(self.online_jobfair_button,model=name)
        self.click_element(self.online_jobfair_button,model=name)

    def cilick_O2Ojobfair(self):
        """
        点击O2O招聘会
        :return:
        """
        name = "点击O2O招聘会"
        self.wait_eleVisible(self.jobfair_button,model=name)
        #点击招聘会管理
        self.click_element(self.jobfair_button,model=name)
        #点击网络招聘会
        self.wait_eleVisible(self.O2O_jobfair_button,model=name)
        self.click_element(self.O2O_jobfair_button,model=name)
    #获取企业名称
    def get_companyname(self):
        name= "获取企业名称"
        self.wait_eleVisible(self.company_name,model=name)
        return self.get_text(self.company_name,model=name)


