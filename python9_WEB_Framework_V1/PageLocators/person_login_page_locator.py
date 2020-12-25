# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 9:27
# @Author  : wangna
# @FileName: person_login_page_locator.py
from selenium.webdriver.common.by import By
#个人登录页面元素
class PersonLoginPageLocator:
    # 元素定位
    user_input = (By.ID, "login-name")  # 用户名输入框 id
    piccode_input = (By.ID, "piccode")  # 图形验证码入框  id
    passwd_input = (By.ID, "login-pwd")  # 密码输入框  id
    login_button = (By.XPATH, "//button[@class='login-butn']")  # 个人登录按钮
    img_code = (By.XPATH, "//img[@class='piccodebutn']")  # 图形验证码
    error_prompt_fromLoginArea = (By.XPATH, "//div[@class='errnotice']/span")  # 手机号码格式有误!  图形验证码不能为空!  密码不能为空!