# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 15:27
# @Author  : wangna
# @FileName: lesson_0929_js_date.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
import time
driver.implicitly_wait(10)#隐形等待
# driver.maximize_window()
driver.get("https://www.12306.cn/index/")
driver.find_element_by_id('fromStationText').click()
#等待新元素出现
WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//ul[@id='ul_list1']/li[@data='BJP']")))
driver.find_element_by_xpath("//ul[@id='ul_list1']/li[@data='BJP']").click()
driver.find_element_by_id('toStationText').click()
driver.find_element_by_xpath("//ul[@id='ul_list1']/li[@data='WHN']").click()
#js语句
js_pha = "a=document.getElementById('train_date');a.removeAttribute('readOnly');"
#执行js
driver.execute_script(js_pha)
#js语句
js_pha = "a.value='2020-11-05'"
driver.execute_script(js_pha)
# time.sleep(5)
driver.find_element_by_id('search_one').click()
#作业==完成12306查询票的自动化，自己选择起点和终点，时间

