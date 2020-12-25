# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 16:05
# @Author  : wangna
# @FileName: create_job_page.py
import time
from Common.base_page import BasePage
from PageLocators.CompanyCenterLocators.create_job_page_locator import CreateJobPageLocator
from selenium.webdriver.common.action_chains import ActionChains
class CreateJobPage(BasePage,CreateJobPageLocator):
    """
    创建岗位页面操作
    :return
    """
    #创建岗位保存
    def create_job_save(self,gwname, zprs,dateend, zplxr, lxphone):
        """
        创建岗位保存
        :return:
        """
        name = "创建岗位保存"
        self.wait_eleVisible(self.closewx_button,model=name)
        self.click_element(self.closewx_button,model=name)
        ########输入岗位信息：职能  岗位名称  招聘人数  工作地区 岗位有效期 招聘联系人  招聘联系人电话
        self.wait_eleVisible(self.zn_sel,model=name)
        self.click_element(self.zn_sel,model=name)
        self.click_element(self.zn_sel_name, model=name)
        self.click_element(self.zn_sel_confirm, model=name)
        self.input_text(self.gwname_input, gwname, model=name)
        self.input_text(self.zprs_input, zprs, model=name)
        self.click_element(self.qydq_sel, model=name)
        self.click_element(self.qydq_sf_sel, model=name)
        self.click_element(self.qydq_cs_sel, model=name)
        self.click_element(self.qydq_sel_confirm, model=name)
        self.driver.execute_script(self.js_date_start)
        curdate = time.strftime("%Y-%m-%d", time.localtime())
        date_start = 'a.value = "{0}"'.format(curdate)
        self.driver.execute_script(date_start)
        self.driver.execute_script(self.js_date_end)
        date_end = 'a.value = "{0}"'.format(dateend)
        self.driver.execute_script(date_end)
        # 向下滚动500个像素
        self.driver.execute_script('window.scrollBy(0,500)')
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_element(self.zplxr_input))
        # 鼠标悬浮按钮可见
        ActionChains(self.driver).move_to_element(self.get_element(self.zplxr_input)).perform()
        self.input_text(self.zplxr_input, zplxr, model=name)
        self.input_text(self.lxrphone_input, lxphone, model=name)
        self.click_element(self.gwtj_button, model=name)

    #返回保存成功提示
    def get_noticecontent(self):
        """
        返回成功提示
        :return:
        """
        name = "创建岗位-保存成功提示"
        self.wait_eleVisible(self.notice,model=name)
        return self.get_text(self.notice,model=name)
