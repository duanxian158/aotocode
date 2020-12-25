# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 17:43
# @Author  : wangna
# @FileName: lesson_0927_wait.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_login']").click()

#显性等待 =等待弹出框元素可见
locator = "TANGRAM__PSP_11__footerULoginBtn"
#WebDriverWait(driver,10).until(条件)
#等待某一个元素可见
loc = (By.ID,locator)
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))

#操作元素
driver.find_element_by_id(locator).click()

