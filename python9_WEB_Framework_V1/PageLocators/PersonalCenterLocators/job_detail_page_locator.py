# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 14:42
# @Author  : wangna
# @FileName: job_detail_page_locator.py

#个人中心-搜索岗位-岗位详情页面

from selenium.webdriver.common.by import By

class JobDetailPageLocator:
    #申请职位
    applyjob_button = (By.XPATH,'//div[@id="job-details"]//button[text()="申请职位"]')
    #操作成功
    noticecontent = (By.XPATH,'//div[@class="modal fade in"]/div[1]/div[1]/div[2]/div[1]')
    #确认
    confirm_button = (By.XPATH,'//button[@id="SysOkBtn"]')
    # 收藏职位
    collectjob_button = (By.XPATH, '//div[@id="job-details"]//button[text()="收藏"]')