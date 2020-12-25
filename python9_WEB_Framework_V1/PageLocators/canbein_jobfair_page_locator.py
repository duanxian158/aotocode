# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 9:16
# @Author  : wangna
# @FileName: canbein_jobfair_page_locator.py

from selenium.webdriver.common.by import By
#可入驻招聘会页面元素
class CanbeJobfairPageLocator:
    # 关闭微信按钮
    closewx_button = (By.XPATH, '//div[@id="close_wx"]')
    # 我要入驻按钮//*[@id="jobfail"]/div[2]/ul/li[1]/div[2]/a
    into_button = (By.XPATH,'//*[@id="jobfail"]/div[2]/ul/li[1]/div[2]/a')
    #选择岗位窗口   选择check//*[@id="job_tbox"]/dd/div[1]/span[1]
    checkjob = (By.XPATH,'//*[@id="job_tbox"]/dd/div[1]/span[1]')

    #点击提交 //*[@id="FailOkbtn"]
    submit_button = (By.XPATH,'//*[@id="FailOkbtn"]')
    #创建岗位//*[@id="FailCancelBtn"]
    creatjobfair_button = (By.XPATH,'//*[@id="FailCancelBtn"]')
    ###########创建岗位窗口元素
    #职能
    zn_sel = (By.XPATH,'//input[@id="zn_sele"]')#请选择
    zn_sel_name = (By.XPATH,'//a[@id="010108"]')#需求工程师
    zn_sel_confirm = (By.XPATH,'//input[@class="checkIn btnOn"]')#确认选择
    #岗位名称
    gwname_input = (By.XPATH,'//input[@id="gw_name"]')
    #招聘人数 //input[@id="zprs"]
    zprs_input = (By.XPATH,'//input[@id="zprs"]')
    #工作地区 //input[@id="qydq"]
    qydq_sel = (By.XPATH,'//input[@id="qydq"]')#请选择
    qydq_sf_sel = (By.XPATH,'//div[@id="SF_Selected"]/ul/li[text()="湖北省"]')#选择湖北省
    qydq_cs_sel =(By.XPATH,'//div[@id="CS_Selected"]/ul/li[text()="武汉市"]')#选择武汉市
    qydq_sel_confirm = (By.XPATH,'//div[@id="QX_Selected"]/ul/li[text()="武昌区"]')#选择武昌区
    #招聘联系人
    zplxr_input = (By.XPATH,'//input[@id="zplxr"]')
    #招聘联系人电话
    lxrphone_input = (By.XPATH,'//input[@id="lx_phone"]')
    #提交
    gwtj_button = (By.XPATH,'//*[@id="CreJobfferDialog"]/div/div/div[3]/button')
