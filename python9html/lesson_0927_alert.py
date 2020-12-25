# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 9:46
# @Author  : wangna
# @FileName: lesson_0927_alert.py
# @Software: PyCharm
#先切换
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("file:D:\Python37\code\python9html\//1.html")
#1.触发alert弹出框
driver.find_element_by_id("bb").click()
#2.等待alert弹框出现
WebDriverWait(driver,5).until(EC.alert_is_present())
#3.先切换到alert Alert 类实例化对象
alert = driver.switch_to.alert
#4..操作alert
#accept 表示OK  dismiss 表示no
print(alert.text)
alert.accept()

