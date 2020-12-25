# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 14:32
# @Author  : wangna
# @FileName: index_page.py
# @Software: PyCharm
from Common.base_page import BasePage
from PageLocators.index_page_locator import IndexPageLocator
class IndexPage(IndexPageLocator,BasePage):

    def __init__(self,driver):
        self.driver = driver
    #点击招聘企业登录
    def click_companylogin(self):
        name = "进入招聘企业登录页面"
        self.wait_eleVisible(self.company_login_button,model=name)
        self.click_element(self.company_login_button,model=name)
    #点击企业注册
    def click_companyregist(self):
        name = "企业注册"
        self.wait_eleVisible(self.company_regist_button,model=name)
        self.click_element(self.company_regist_button,model=name)
    #获取右上角账户名称
    def get_nickNmae(self):
        self.wait_eleVisible(self.account_name)#等待元素出现
        return self.get_element(self.account_name).text
    #点击个人注册
    def click_personregist(self):
        name = "个人注册"
        self.wait_eleVisible(self.person_regist_button,model=name)
        self.click_element(self.person_regist_button,model=name)
    #个人登录
    def click_personlogin(self):
        name = "个人登录"
        self.wait_eleVisible(self.person_login_button,model=name)
        self.click_element(self.person_login_button,model=name)

    ###########################
    def click_first_investButton(self):
        pass