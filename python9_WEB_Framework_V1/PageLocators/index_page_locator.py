# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 14:29
# @Author  : wangna
# @FileName: index_page_locator.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
class IndexPageLocator:
    #首页
    # 右上角账户名称
    # acount_name = (By.XPATH,"//i[@class='fa fa-user']/following-sibling::span")#用于断言判断
    #//a[@href='/Company/CompanyCenter']
    account_name = (By.XPATH,"//a[@href='/Company/CompanyCenter']")
    #导航栏-招聘会//a[@href='/JobFail/Type']
    menu_jobfair = (By.XPATH,"//a[@href='/JobFail/Type']")

    ##############首页
    #招聘企业登录
    company_login_button = (By.XPATH,'//a[text()="招聘企业登录"]')
    #招聘企业注册
    company_regist_button = (By.XPATH,'//a[text()="招聘企业登录"]/following::a[1]')
    #个人登录
    person_login_button = (By.XPATH,'//a[text()="个人登录"]')
    #个人注册
    person_regist_button = (By.XPATH,'//a[text()="个人登录"]/following::a[1]')