# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 10:02
# @Author  : wangna
# @FileName: job_ recommen_page_locator.py

from selenium.webdriver.common.by import By
#岗位推荐页面元素
class JobRecommenPageLocator:
    #第一行岗位名称
    onejobname_link = (By.XPATH,'//div[@id="job_box"]/div[1]/div[1]/div[2]//span[@class="job-name ell"]')
