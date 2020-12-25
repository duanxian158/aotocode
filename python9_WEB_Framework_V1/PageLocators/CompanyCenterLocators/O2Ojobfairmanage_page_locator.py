# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 15:32
# @Author  : wangna
# @FileName: O2Ojobfairmanage_page_locator.py

from selenium.webdriver.common.by import By
class O2OJobFairManagePageLocator:
    """
    O2O招聘会管理页面元素
    :return
    """
    #
    #可入驻招聘会按钮
    canbejobfair_button = (By.XPATH, "//ul[@id='left_menu']//span[text()='可入驻招聘会']")