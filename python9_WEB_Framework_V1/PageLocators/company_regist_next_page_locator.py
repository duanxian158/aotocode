# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:53
# @Author  : wangna
# @FileName: company_regist_next_page_locator.py

from selenium.webdriver.common.by import By
#企业注册2
class CompanyRegistNextPageLocator:
    managename_input = (By.ID,'manageName')#管理员姓名输入框
    manage_idcard_input = (By.ID,'manageIdCrad')#管理员身份证号输入框
    manage_phone_input = (By.ID,'manageIphone')#管理员手机号输入框
    img_code = (By.XPATH,"//img[@class='piccodebutn']")   #图形验证码
    piccode_input = (By.ID, "piccode")  # 图形验证码入框
    phonecode_button = (By.XPATH,'//button[@class="codebutn"]')#发送验证码
    phonecode_input = (By.ID,'code')#验证码输入框
    register_button = (By.XPATH,'//button[@class="register-butn"]')#注册