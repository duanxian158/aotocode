# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:55
# @Author  : wangna
# @FileName: person_regist_page_locator.py
from selenium.webdriver.common.by import By
#个人注册页面元素
class PersonRegistPageLocator:
    #手机号
    phone_input  = (By.ID,'iphone')
    #图形验证码
    piccode_input = (By.ID, "piccode")  # 图形验证码入框  id
    img_code = (By.XPATH, "//img[@class='piccodebutn']")  # 图形验证码
    phonecode_button = (By.XPATH, '//button[@class="codebutn"]')  # 发送验证码
    phonecode_input = (By.ID, 'code')  # 验证码输入框
    passwd_input = (By.ID, "pwd")  # 密码输入框  id
    passwd2_input = (By.ID, "pwd2")
    register_button = (By.XPATH, "//button[@class='register-butn']")  # 注册

