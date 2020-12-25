# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 10:30
# @Author  : wangna
# @FileName: person_login_page.py
from Common.imge_code import ImageCode
from Common.base_page import BasePage
from PageLocators.person_login_page_locator import PersonLoginPageLocator
#个人登录
class PersonLoginPage(BasePage,PersonLoginPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #个人登录
    def person_login(self,phone,pwd):
        #输入手机号 图形验证码  密码  登录
        name = "个人登录"
        self.wait_eleVisible(self.user_input,model=name)
        self.input_text(self.user_input,phone,model=name)
        #获取验证码
        imge = ImageCode(self.driver).image_str(self.img_code)
        self.input_text(self.piccode_input,imge,model=name)
        self.input_text(self.passwd_input,pwd,model=name)
        self.click_element(self.login_button,model=name)