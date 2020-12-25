# -*- coding: utf-8 -*-
# @Time    : 2020/12/7 17:09
# @Author  : wangna
# @FileName: myjobfair_page_locator.py
from selenium.webdriver.common.by import By
class MyJobFariPageLocator:

    #左边菜单  可入驻招聘会按钮//ul[@id='left_menu']//span[text()='可入驻招聘会']
    canbejobfair_button = (By.XPATH,"//ul[@id='left_menu']//span[text()='可入驻招聘会']")
