# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 15:33
# @Author  : wangna
# @FileName: create_job_page_locator.py

from selenium.webdriver.common.by import By

class CreateJobPageLocator:
    """
    创建岗位页面元素
    :return
    """
    #关闭微信
    closewx_button = (By.XPATH,'//div[@id="close_wx"]')
    # 职能
    zn_sel = (By.XPATH, '//input[@id="zn_sele"]')  # 请选择
    zn_sel_name = (By.XPATH, '//a[@id="010104"]')  # 算法工程师
    zn_sel_confirm = (By.XPATH, '//input[@class="checkIn btnOn"]')  # 确认选择
    # 岗位名称
    gwname_input = (By.XPATH, '//input[@id="gw_name"]')
    # 招聘人数 //input[@id="zprs"]
    zprs_input = (By.XPATH, '//input[@id="zprs"]')
    # 工作地区 //input[@id="qydq"]
    qydq_sel = (By.XPATH, '//input[@id="qydq"]')  # 请选择
    qydq_sf_sel = (By.XPATH, '//div[@id="SF_Selected"]/ul/li[text()="湖北省"]')  # 选择湖北省
    qydq_cs_sel = (By.XPATH, '//div[@id="CS_Selected"]/ul/li[text()="武汉市"]')  # 选择武汉市
    qydq_sel_confirm = (By.XPATH, '//div[@id="QX_Selected"]/ul/li[text()="武昌区"]')  # 选择武昌区
    #岗位有效期
    js_date_start = 'a = document.getElementById("yxq_ks");'
    js_date_end = 'a = document.getElementById("yxq_js");'
    # 招聘联系人
    zplxr_input = (By.XPATH, '//input[@id="zplxr"]')
    # 招聘联系人电话
    lxrphone_input = (By.XPATH, '//input[@id="lx_phone"]')
    # 提交
    gwtj_button = (By.ID, 'save')
    #保存成功提示
    notice = (By.XPATH,'//div[@id="SystemNoticeContent"]')