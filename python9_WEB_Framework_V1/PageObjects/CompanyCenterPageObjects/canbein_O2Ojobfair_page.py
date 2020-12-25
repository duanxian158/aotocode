# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 15:43
# @Author  : wangna
# @FileName: canbein_O2Ojobfair_page.py

from PageLocators.CompanyCenterLocators.canbein_O2Ojobfair_page_locator import CanbeO2OJobfairPageLocator
from Common.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
class CanbeO2OJobFairPage(BasePage,CanbeO2OJobfairPageLocator):
    """
    可入驻O2O招聘会页面操作
    :return
    """
    def __init__(self,driver):
        self.driver=driver
    def click_intoO2Ojobfair(self):
        """
        我要入驻O2O招聘会-通过导入岗位入驻
        :return:
        """
        name = "可入驻O2O招聘会-通过导入岗位入驻"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        # 等待按钮出现
        self.wait_eleVisible(self.into_button, model=name)
        # 点击我要入驻
        self.click_element(self.into_button, model=name)
        self.wait_eleVisible(self.checkjob, model=name)
        # 勾选岗位
        self.click_element(self.checkjob, model=name)
        # 提交
        self.click_element(self.submit_button, model=name)


    def click_intoO2Ojobfair_creatjob(self, gwname, zprs, zplxr, lxphone):
        """
        # 我要入驻O2O招聘会-通过创建岗位入驻
        :param gwname: 岗位名称
        :param zprs: 招聘人数
        :param zplxr: 招聘联系人
        :param lxphone: 联系人电话
        :return:
        """
        name = "我要入驻-创建岗位"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        # 等待按钮出现
        self.wait_eleVisible(self.into_button, model=name)
        # 点击我要入驻
        self.click_element(self.into_button, model=name)
        # 等待创建岗位页面元素
        self.wait_eleVisible(self.creatjobfair_button, model=name)
        # 点击创建创建岗位
        self.click_element(self.creatjobfair_button, model=name)
        # 等待元素//input[@id="zn_sele"]
        self.wait_eleVisible(self.zn_sel,model=name)
        ########输入岗位信息：职能  岗位名称  招聘人数  工作地区  招聘联系人  招聘联系人电话
        self.click_element(self.zn_sel,model=name)
        self.click_element(self.zn_sel_name,model=name)
        self.click_element(self.zn_sel_confirm,model=name)
        self.input_text(self.gwname_input, gwname,model=name)
        self.input_text(self.zprs_input, zprs,model=name)
        self.click_element(self.qydq_sel,model=name)
        self.click_element(self.qydq_sf_sel,model=name)
        self.click_element(self.qydq_cs_sel,model=name)
        self.click_element(self.qydq_sel_confirm,model=name)
        # 向下滚动500个像素
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element(self.zplxr_input))
        # 鼠标悬浮按钮可见
        ActionChains(self.driver).move_to_element(self.get_element(self.zplxr_input)).perform()
        self.input_text(self.zplxr_input, zplxr,model=name)
        self.input_text(self.lxrphone_input, lxphone,model=name)
        self.click_element(self.gwtj_button, model=name)
