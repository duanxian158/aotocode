# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 15:33
# @Author  : wangna
# @FileName: unpublish_job_page_locator.py

from selenium.webdriver.common.by import By

class UnPublishJobPageLocator:
    """
    未发布岗位页面元素
    :return
    """
    #创建岗位
    createjob_button = (By.XPATH,'//span[text()="创建岗位"]')