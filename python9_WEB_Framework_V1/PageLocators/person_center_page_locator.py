# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 15:55
# @Author  : wangna
# @FileName: person_center_page_locator.py
from selenium.webdriver.common.by import By
#个人中心页面元素定位
class PersonCenterPageLocator:
    #个人账号名称
    person_name = (By.XPATH,'//div[@id="user-nameA"]')
    #个人手机号
    accout_phone = (By.XPATH,'//span[@id="hname"]')
    #############导航栏菜单
    #简历管理
    resume_menu = (By.XPATH,'//a[text()="简历管理"]')
    #岗位搜索
    jobsearch_menu = (By.XPATH, '//a[text()="岗位搜索"]')
    #岗位推荐
    jobrecommend_menu = (By.XPATH, '//a[text()="岗位推荐"]')
    #我的求职
    myjob_menu = (By.XPATH, '//a[text()="我的求职"]')
    #我的培训
    mytrain_menu = (By.XPATH, '//a[text()="我的培训"]')
    #我的招聘会
    myjobfair_menu = (By.XPATH, '//a[text()="我的招聘会"]')
    #实名认证
    certification_menu = (By.XPATH, '//a[text()="实名认证"]')
    #账户管理
    accountmanage_menu = (By.XPATH, '//a[text()="账户管理"]')
