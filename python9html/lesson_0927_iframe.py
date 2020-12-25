# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 14:20
# @Author  : wangna
# @FileName: lesson_0927-iframe.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)#隐形等待
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
#获取当前窗口
cur_handles = driver.window_handles
#因为click的品质作带来了页面的变化======  一定要等待
driver.find_element_by_xpath("//div[@id='1']/h3/a").click()
#click操作带来了新的窗口==等待新的窗口出现
WebDriverWait(driver,10).until(EC.new_window_is_opened(cur_handles))
#获取所有窗口
cur_handles = driver.window_handles
#获取点击操作之后的窗口
print("获取点击操作之后的窗口：",cur_handles)
#切换到最扣一次新的窗口
driver.switch_to.window(cur_handles[-1])
driver.find_element_by_id("js_login").click()
#等待新的元素出现
# xpath = "//a[@data-type='1']"
WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@data-type='1']")))
driver.find_element_by_xpath("//a[@data-type='1']").click()
# #待待要切换的iframe页面出现 并切换进入iframe
WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
#
# #切换到iframe  -下标/name属性/webelement对象 三种切换方式  //iframe[@name='login_frame_qq']
# # driver.switch_to.frame(4)
# # driver.switch_to.frame("login_frame_qq")
# # driver.switch_to.frame(driver.find_element_by_name("login_frame_qq"))
# #在新的html页面当中，定位元素并操作 switcher_plogin
driver.find_element_by_id("switcher_plogin").click()