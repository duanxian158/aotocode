# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 16:18
# @Author  : wangna
# @FileName: homework_0929_12306_js.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#跳转至12306网站
driver.get("https://www.12306.cn/index/")
#js语句  出发地
js_a = "a= document.getElementById('fromStationText');a.value='北京';"
driver.execute_script(js_a)
#到达地
js_b = "a= document.getElementById('toStationText');a.value='武汉';"
driver.execute_script(js_b)
#出发日期
js_date = "a=document.getElementById('train_date');a.value='2020-11-06'"
driver.execute_script(js_date)
#查询
driver.find_element_by_id("search_one").click()
