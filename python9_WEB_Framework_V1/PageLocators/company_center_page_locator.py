# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 11:24
# @Author  : wangna
# @FileName: jobfair_type_page_locator.py

from selenium.webdriver.common.by import By

class CompanyCenterPageLocator:
    """
    #企业中心页面元素
    """
    #企业名称
    company_name = (By.XPATH,'//i[@class="fa fa-user"]/following::span[1]')

    #岗位管理
    jobmanage_menu = (By.XPATH,'//a[text()="岗位管理"]')
    #简历搜索
    resumesearch_menu = (By.XPATH, '//a[text()="简历搜索"]')
    #简历推荐
    resumerecommend_menu = (By.XPATH, '//a[text()="简历推荐"]')
    #我的招聘
    myjob_menu = (By.XPATH, '//a[text()="我的招聘"]')
    #招聘会管理按钮//li[@class="dropdown"]/a
    jobfair_button = (By.XPATH,'//li[@class="dropdown"]/a')
    #网络招聘会按钮//div[@onclick="location.href = '/Jobfail/Index?type=1'"]
    online_jobfair_button = (By.XPATH,'//*[@id="company-dropdown-menu"]/li[1]/a')
    #O2O招聘会按钮
    O2O_jobfair_button = (By.XPATH,'//*[@id="company-dropdown-menu"]/li[2]/a')


