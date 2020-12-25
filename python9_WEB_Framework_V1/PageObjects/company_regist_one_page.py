# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:27
# @Author  : wangna
# @FileName: company_regist_page.py

from Common.base_page import BasePage
from PageLocators.company_regist_page_locator import CompanyRegistPageLocator
#企业注册
class CompantyRegistOnePage(BasePage,CompanyRegistPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #企业注册页面-输入信息-点击下一步
    def click_registone(self,creditcode,companyname,companyno,companypwd,companypwd2):
        name = "企业注册-下一步"
        #选择证件类型 输入证件号码，名称 地区 账号  密码  下一点
        self.wait_eleVisible(self.codetype_sel,model=name)#等待元素出现
        self.click_element(self.codetype_sel,model=name)#选择证件类型
        self.click_element(self.codetype_sel_confirm,model=name)
        self.input_text(self.creditcode_input,creditcode,model=name)#输入证件号码
        self.input_text(self.companyname_input,companyname,model=name)#输入企业名称
        self.click_element(self.qydq_sel,model=name)#选择地区
        self.click_element(self.qydq_cs_sel,model=name)
        self.click_element(self.qydq_sel_confirm,model=name)
        self.input_text(self.companyno_input,companyno,model=name)#输入企业账号
        self.input_text(self.companypwd_input,companypwd,model=name)#输入企业密码
        self.input_text(self.companypwd2_input,companypwd2,model=name)
        self.click_element(self.next_button,model=name)#点击下一步