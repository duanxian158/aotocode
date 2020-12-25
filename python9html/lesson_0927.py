# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 10:10
# @Author  : wangna
# @FileName: sel.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time

#启动一个与浏览器之间的会话
driver = webdriver.Chrome()
driver.implicitly_wait(10)#隐形等待
driver.get("http://www.baidu.com")
#关闭浏览器会话  多个tab

# 6 xpath
#1.相对定位  1.绝对定位
# //*[@id="s_is_result_css"]
# driver.find_element_by_xpath("//*[@id='s_is_result_css']")
# a = driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_login']")
# print(a.text)//*[@id="kw"]


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
#等待新页面的元素出现，并操作它
xpath = "//ul[@id='js-tab']//h2[contains(text(),'课程')]"
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,xpath)))
driver.find_element_by_xpath(xpath).click()
#关闭当前窗口
driver.close()
time.sleep(5)
#打印当前的窗口句柄
# driver.switch_to.window(cur_handles[-1])
print(driver.window_handles)




# driver.close()