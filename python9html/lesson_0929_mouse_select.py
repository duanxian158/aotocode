# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 16:59
# @Author  : wangna
# @FileName: lesson_0929_mouse.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)#隐形等待
driver.get("http://www.baidu.com")
#方式一
# driver.find_element_by_id("s-usersetting-top").click()
#方式二  #1.先找到鼠标要操作的元素
ele = driver.find_element_by_id("s-usersetting-top")
#调用鼠标操作方法  最后调用perform()方法去抚摩行鼠标操作
ActionChains(driver).move_to_element(ele).perform()
#弹出框处理 == 非select 元素
#1.等待下拉列表当中的元素出现  2.再去操作
loc = (By.XPATH,"//a[contains(text(),'高级搜索')]")
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))
driver.find_element_by_xpath("//a[contains(text(),'高级搜索')]").click()

#弹出框处理  == select/option这样的元素 使用webdriver Select类来处理
#引入Select类
from selenium.webdriver.support.ui import Select
import time
#1.找到Select元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//select[@name='ft']")))
ele = driver.find_element_by_xpath("//select[@name='ft']")
#2.实例化Select 类
s = Select(ele)
#3.选择一个option值==通过下村
s.select_by_index(3)
time.sleep(2)
#根据value属性来选值
s.select_by_value("all")
time.sleep(2)
#根据文本内容来选值
s.select_by_visible_text("微软 Powerpoint（.ppt）")

#执行js函数

driver.execute_script()

