# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 10:51
# @Author  : wangna
# @FileName: job_search_page_locator.py
from selenium.webdriver.common.by import By
#个人中心-岗位搜索页面
class JobSearchPageLocator:
    #取行一行岗位元素
    jobname_link = (By.XPATH,'//div[@id="job_box"]/div[1]/div[1]/div[2]/div/span[@class="job-name ell"]')
    #申请职位
    applyjob_button = (By.XPATH,'//div[@id="job_box"]/div[1]//button[1]')
    #申请成功通知
    noticecontent = (By.XPATH,'//div[@id="SystemNoticeContent"]')
    #关闭微信按钮
    closewx_button = (By.XPATH,'//div[@id="close_wx"]')

