# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 9:38
# @Author  : wangna
# @FileName: resume_manage_page_locator.py

from selenium.webdriver.common.by import By
#个人简历管理页面-元素定位

class ResumeManagePageLocator:
    ##################添加求职意向###################################
    # 关闭微信按钮
    closewx_button = (By.XPATH, '//div[@id="close_wx"]')
    addjobintention_button = (By.XPATH,'//a[text()="添加意向"]')
    #职能 岗位名称 择业地区 期望薪资  工作性质
    edfun_sel = (By.XPATH,'//input[@id="ed-function"]')
    edfun_sel2 = (By.ID,'010110')#系统分析员
    edufn_sel_confirm = (By.XPATH,'//input[@class="checkIn btnOn"]')
    #岗位名称
    edujobname_input = (By.ID,'ed-jobName')
    #择业地区
    edjobarea_sel = (By.ID,'ed-jobArea')
    edjobarea_sel2 = (By.XPATH, '//div[@id="CS_Selected"]/ul/li[text()="武汉市"]')  # 选择武汉市
    edjobarea_sel3 = (By.XPATH, '//div[@id="QX_Selected"]/ul/li[text()="武昌区"]')  # 选择武昌区
    #期望薪资
    edsalary_sel = (By.ID,'ed-salary')
    edjobarea_sel_confirm =(By.XPATH,'//select[@id="ed-salary"]/option[4]')
    #工作性质
    edworknat_sel = (By.ID,'ed-workNat')
    edworknat_sel_confirm = (By.XPATH,'//select[@id="ed-workNat"]/option[5]')
    #公开状态
    state_button = (By.XPATH,'//button[@id="close_state"]')
    #求职意向-保存
    volunsave_button = (By.ID,'re-voluntSave')
    #保存成功后提示框
    save_prompt = (By.ID,'SystemNoticeContent')
    #########求职意向删除按钮可见################//div[@class="jobVolunteer"]/div[1]//div[2]
    js_intention_del = 'a = document.getElementsByClassName("col-wb-1 wb_col del-edit")[0];a.style.display="block"'
    ele_intention = (By.XPATH,'//div[@class="jobVolunteer"]/div[1]//div[1]')
    edjobintention_del_button = (By.XPATH,'//div[@class="jobVolunteer"]/div[1]//div[2]')
    #删除确认提示框
    del_confirm_button = (By.ID,'SysOkBtn')

    ####################3添加工作经历##############################
    addworkexprience_button = (By.XPATH, '//a[text()="添加工作"]')
    #工作时间  企业名称  岗位名称 工作描术
    workdate_sel = (By.ID,'ed-workExpTime-strat')
    js_date = 'a = document.getElementById("ed-workExpTime-strat");a.value="2020-11"'
    #企业名称
    edunitname_input = (By.ID,'ed-unitName')
    #岗位名称
    edjobname_input = (By.ID,'ed-job')
    #工作描述
    edworkdes_input = (By.ID,'ed-workDes')
    #工作经历-保存
    edworksavae_button = (By.ID,'re-workExpSave')
    #########工作经历删除
    ########工作经历删除按钮可见
    ele_work = (By.XPATH,'//div[@class="workExp"]/div[1]/div[1]')
    work_del_button = (By.XPATH,'//div[@class="workExp"]/div[1]/div[1]/div[2]/span[1]')

    ##################添加项目经历########################
    addprojectexprience_button = (By.XPATH, '//a[text()="添加经验"]')
    #项目时间
    js_date_start = 'a = document.getElementById("ed-projectTime-strat");a.value="2020-11"'
    #项目名称
    edprojectname_input = (By.ID,'ed-projectName')
    #项目描述
    edprojectdes_input = (By.ID,'ed-projectDes')
    #职责描述
    eddutydes_input = (By.ID,'ed-dutyDes')
    #项目经历-保存
    edproctsave_button = (By.XPATH,'//div[@id="ProjectEditBox"]/ul/li[5]/div/button[1]')
    ##########################删除项目经历
    ele_project = (By.XPATH,'//div[@class="projectExp"]/div[1]/div[1]')
    project_del_button = (By.XPATH,'//div[@class="projectExp"]/div[1]/div[1]/div[2]/span[1]')
    project_del_confirm_button = (By.XPATH,'//div[@id="SystemNotice"]/div[1]/div[1]/div[3]/button[2]')

    ##################添加描述-自我评价
    adddescribe_button = (By.XPATH, '//a[text()="添加描述"]')
    #自我评价
    edselfdes_input = (By.ID,'ed-selfDes')
    #自我评价-保存
    edselfsave_button = (By.ID,'re-selfDesSave')

