# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 10:53
# @Author  : wangna
# @FileName: login_page_locator.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 元素定位
    user_input = (By.ID,"login-name")  # 用户名输入框 id
    piccode_input = (By.ID,"piccode")  # 图形验证码入框  id
    passwd_input = (By.ID,"login-pwd") #密码输入框  id
    login_button = (By.XPATH,"//button[@class='company-butn']")  # 企业登录按钮
    img_code = (By.XPATH,"//img[@class='piccodebutn']")   #图形验证码
    error_prompt_fromLoginArea = (By.XPATH,"//div[@class='errnotice']/span")  #手机号码格式有误!  图形验证码不能为空!  密码不能为空!
