# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 11:29
# @Author  : wangna
# @FileName: resume_manage_page.py
from selenium.webdriver.common.action_chains import ActionChains
from Common.base_page import BasePage
from PageLocators.resume_manage_page_locator import ResumeManagePageLocator
#简历管理
class ResumeManagePage(BasePage,ResumeManagePageLocator):
    def __init__(self,driver):
        self.driver=driver
    #添加求职意向
    def add_job_intention(self,jobname):
        #职能  岗位名称  择业地区  期望新资  工作性质  保存
        name = "添加求职志愿"
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.addjobintention_button,model=name)
        self.click_element(self.addjobintention_button,model=name)
        #职能
        self.wait_eleVisible(self.edfun_sel,model=name)
        self.click_element(self.edfun_sel,model=name)
        self.wait_eleVisible(self.edfun_sel2,model=name)
        self.click_element(self.edfun_sel2,model=name)
        self.click_element(self.edufn_sel_confirm,model=name)
        #岗位名称
        self.input_text(self.edujobname_input,jobname,model=name)
        #择业地区
        self.click_element(self.edjobarea_sel,model=name)
        self.wait_eleVisible(self.edjobarea_sel2,model=name)
        self.click_element(self.edjobarea_sel2,model=name)
        self.click_element(self.edjobarea_sel3,model=name)
        self.click_element(self.edjobarea_sel_confirm,model=name)
        #期望薪资
        self.click_element(self.edsalary_sel,model=name)
        self.click_element(self.edjobarea_sel_confirm,model=name)
        #工作性质
        self.click_element(self.edworknat_sel,model=name)
        self.click_element(self.edworknat_sel_confirm,model=name)
        #公开状态
        self.click_element(self.state_button,model=name)
        #保存
        self.click_element(self.volunsave_button,model=name)

    #删除求职志愿
    def del_job_initention(self):
        name = "删除求职意向"
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.addjobintention_button,model=name)
        # time.sleep(5)
        # self.driver.execute_script(self.js_intention_del)
        #鼠标悬浮
        self.wait_eleVisible(self.ele_intention,model=name)
        ActionChains(self.driver).move_to_element(self.get_element(self.ele_intention)).perform()
        self.wait_eleVisible(self.edjobintention_del_button,model=name)
        self.click_element(self.edjobintention_del_button,model=name)
        self.wait_eleVisible(self.del_confirm_button,model=name)
        self.click_element(self.del_confirm_button,model=name)

    #获取 保存成功弹窗提示
    def get_save_prompt(self):
        name = "保存或删除成功提示框"
        self.wait_eleVisible(self.save_prompt,model=name)
        return self.get_text(self.save_prompt,model=name)


    #i添加工作经历
    def add_work_exprience(self,unitname,jobname,describe):
        #工作经历  企业名称  岗位名称
        name = "添加工作经历"
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.addworkexprience_button,model=name)
        self.click_element(self.addworkexprience_button,model=name)
        self.wait_eleVisible(self.workdate_sel,model=name)
        self.driver.execute_script(self.js_date)
        self.input_text(self.edunitname_input,unitname,model=name)
        self.input_text(self.edjobname_input,jobname,model=name)
        self.input_text(self.edworkdes_input,describe,model=name)
        self.click_element(self.edworksavae_button,model=name)

    #删除工作经历
    def del_work_exprience(self):
        name = "删除工作经历"
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.addworkexprience_button,model=name)
        #鼠标悬浮 按钮可见
        self.wait_eleVisible(self.ele_work,model=name)
        ActionChains(self.driver).move_to_element(self.get_element(self.ele_work)).perform()
        self.wait_eleVisible(self.work_del_button,model=name)
        self.click_element(self.work_del_button,model=name)
        self.wait_eleVisible(self.del_confirm_button,model=name)
        self.click_element(self.del_confirm_button,model=name)

    #添加项目经历
    def add_project_exprience(self,projectname,projectdes,dutydes):
        name = "添加项目经历"
        print("进入{0}".format(name))
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.addprojectexprience_button,model=name)
        self.click_element(self.addprojectexprience_button,model=name)
        # 向下滚动500个像素
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element(self.edprojectname_input))
        # 鼠标悬浮按钮可见
        ActionChains(self.driver).move_to_element(self.get_element(self.edprojectname_input)).perform()
        self.wait_eleVisible(self.edprojectname_input,model=name)
        self.driver.execute_script(self.js_date_start)
        self.input_text(self.edprojectname_input,projectname,model=name)
        self.input_text(self.edprojectdes_input,projectdes,model=name)
        self.input_text(self.eddutydes_input,dutydes,model=name)
        self.click_element(self.edproctsave_button,model=name)

    #删除项目经历
    def del_project_exprience(self):
        name = "删除项目经历"
        self.wait_eleVisible(self.closewx_button, model=name)
        self.click_element(self.closewx_button, model=name)
        self.wait_eleVisible(self.ele_project,model=name)
        # 向下滚动500个像素
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element(self.ele_project))
        #鼠标悬浮按钮可见
        ActionChains(self.driver).move_to_element(self.get_element(self.ele_project)).perform()
        self.wait_eleVisible(self.project_del_button,model=name)

        self.click_element(self.project_del_button,model=name)
        self.wait_eleVisible(self.project_del_confirm_button,model=name)
        self.click_element(self.project_del_confirm_button,model=name)

