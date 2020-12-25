# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:53
# @Author  : wangna
# @FileName: company_regist_page_locator.py

from selenium.webdriver.common.by import By
#企业注册页面
class CompanyRegistPageLocator:
    #代码类型
    codetype_sel = (By.ID,"codeType")
    codetype_sel_confirm = (By.XPATH,'//select[@id="codeType"]/option[2]')#统一信用代码
    #证件号码
    creditcode_input = (By.ID,'creditCode')
    # 企业名称
    companyname_input = (By.ID, 'companyName')
    #地区选择 ssdq
    qydq_sel = (By.ID,'ssdq')  # 请选择
    qydq_cs_sel = (By.XPATH, '//div[@id="CS_Selected"]/ul/li[text()="武汉市"]')  # 选择武汉市
    qydq_sel_confirm = (By.XPATH, '//div[@id="QX_Selected"]/ul/li[text()="武昌区"]')  # 选择武昌区
    #企业账号
    companyno_input = (By.ID,'companyNo')
    #密码
    companypwd_input = (By.ID,'companyPwd')
    companypwd2_input = (By.ID, 'companyPwd2')
    #下一步
    next_button = (By.XPATH,'//button[@class="next-butn"]')


