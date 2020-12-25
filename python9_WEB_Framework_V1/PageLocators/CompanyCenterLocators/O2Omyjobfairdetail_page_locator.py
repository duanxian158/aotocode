# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 15:44
# @Author  : wangna
# @FileName: O2Omyjobfairdetail_page_locator.py

from selenium.webdriver.common.by import By
class O2OMyJobFairDetailPageLocator:
    """
    O2O招聘会-我的招聘会详情页面元素
    :return
    """
    #审核状态
    shzt = (By.XPATH,'//b[@class="fontg"]')