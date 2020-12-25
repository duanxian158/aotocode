# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 16:59
# @Author  : wangna
# @FileName: myjobfairdetail_page_locator.py
from selenium.webdriver.common.by import By

########我的网络招聘会岗位详情
class MyJobFairDetailPageLocator:
    #审核状态
    shzt = (By.XPATH,'//b[@class="fontg"]')