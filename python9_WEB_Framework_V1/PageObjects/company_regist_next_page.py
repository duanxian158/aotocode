# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 11:28
# @Author  : wangna
# @FileName: company_regist_next_page.py

from Common.base_page import BasePage
from PageLocators.company_regist_next_page_locator import CompanyRegistNextPageLocator
from Common.imge_code import ImageCode
#企业注册
class CompantyRegistNextPage(BasePage,CompanyRegistNextPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #企业注册
    def click_registnext(self,manaagename,idcard,phone,phonecode):
        name = "企业注册"
        #输入  管理员姓名 管理员身份证号 手机号 图形验证码 短信验证码   注册
        self.wait_eleVisible(self.managename_input,model=name)
        self.input_text(self.managename_input,manaagename,model=name)
        self.input_text(self.manage_idcard_input,idcard,model=name)
        self.input_text(self.manage_phone_input,phone,model=name)
        # 获取验证码
        image = ImageCode(self.driver).image_str(self.img_code)
        # 输入验证码
        self.input_text(self.piccode_input, image, model=name)
        self.click_element(self.phonecode_button,model=name)
        self.input_text(self.phonecode_input,phonecode,model=name)
        self.click_element(self.register_button,model=name)