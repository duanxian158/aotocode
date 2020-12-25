# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 10:19
# @Author  : wangna
# @FileName: canbein_jobfair_page.py
from Common.base_page import BasePage
from PageLocators.canbein_jobfair_page_locator import CanbeJobfairPageLocator
from selenium.webdriver.common.action_chains import ActionChains
#可入驻招聘会页面
class CanbeJobFairPage(BasePage,CanbeJobfairPageLocator):
    def __init__(self,driver):
        self.driver=driver
    def click_intojobfai(self):
        name = "我要入驻-导入岗位列表"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        #等待按钮出现
        self.wait_eleVisible(self.into_button,model=name)
        #点击我要入驻
        self.click_element(self.into_button,model=name)
        self.wait_eleVisible(self.checkjob,model=name)
        #勾选岗位
        self.click_element(self.checkjob,model=name)
        #提交
        self.click_element(self.submit_button,model=name)
    #通过创建岗位入驻
    def click_intojobfair_creatjob(self,gwname,zprs,zplxr,lxphone):
        name = "我要入驻-创建岗位"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        # 等待按钮出现
        self.wait_eleVisible(self.into_button, model=name)
        # 点击我要入驻
        self.click_element(self.into_button, model=name)
        #等待创建岗位页面元素
        self.wait_eleVisible(self.creatjobfair_button, model=name)
        # 点击创建创建岗位
        self.click_element(self.creatjobfair_button, model=name)
        # 等待元素//input[@id="zn_sele"]
        self.wait_eleVisible(self.zn_sel)
        ########输入岗位信息：职能  岗位名称  招聘人数  工作地区  招聘联系人  招聘联系人电话
        self.click_element(self.zn_sel)
        self.click_element(self.zn_sel_name)
        self.click_element(self.zn_sel_confirm)
        self.input_text(self.gwname_input,gwname)
        self.input_text(self.zprs_input,zprs)
        self.click_element(self.qydq_sel)
        self.click_element(self.qydq_sf_sel)
        self.click_element(self.qydq_cs_sel)
        self.click_element(self.qydq_sel_confirm)
        # 向下滚动500个像素
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element(self.zplxr_input))
        # 鼠标悬浮按钮可见
        ActionChains(self.driver).move_to_element(self.get_element(self.zplxr_input)).perform()
        self.input_text(self.zplxr_input,zplxr)
        self.input_text(self.lxrphone_input,lxphone)
        self.click_element(self.gwtj_button, model=name)
