# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 16:05
# @Author  : wangna
# @FileName: person_regist_page.py
from Common.base_page import BasePage
from PageLocators.person_regist_page_locator import PersonRegistPageLocator
from Common.imge_code import ImageCode
#个人注册
class PersonRegistPage(BasePage,PersonRegistPageLocator):
    def __init__(self,driver):
        self.driver=driver
    #个人注册
    def click_person_regist(self,phone,phonecode,pwd,pwd2):
        name ="个人注册"
        #输入手机号  图形验证码  短信验证码  密码  重复密码 注册
        self.wait_eleVisible(self.phone_input,model=name)
        self.input_text(self.phone_input,phone,model=name)
        # 获取验证码
        image = ImageCode(self.driver).image_str(self.img_code)
        # 输入验证码
        self.input_text(self.piccode_input, image, model=name)
        self.click_element(self.phonecode_button,model=name)
        self.input_text(self.phonecode_input,phonecode,model=name)
        self.input_text(self.passwd_input,pwd,model=name)
        self.input_text(self.passwd2_input,pwd2,model=name)
        self.click_element(self.register_button,model=name)
