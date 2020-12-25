# -*- coding: utf-8 -*-
# @Time    : 2020/11/6 17:27
# @Author  : wangna
# @FileName: lesson_1009_file_upload.py
# @Software: PyCharm
#引入pywin32的库
import win32gui
import win32con

def upload_file(file_path):
    #一级窗口
    dialog = win32gui.FindWindow("#32770","打开")
    #二级元素
    comboxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
    #三级元素
    combox = win32gui.FindWindowEx(comboxEx32, 0, 'ComboBox', None)
    #Edit元素
    edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)
    #Button 打开按钮元素
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #Edit当中输入文件完整路径
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)
    #点击打开按钮，提交
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

#webdriver == 登陆客堂派
#访问网址：https://www.ketangpai.com/Courseware/index/couseid/MD
#SLEEP 1到2秒,然后使用upload_file()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)#隐形等待
driver.get("https://www.baidu.com/")
driver.find_element_by_xpath('//form[@id="form"]//span[@class="soutu-btn"]').click()
time.sleep(5)
driver.find_element_by_xpath('//span[@class="upload-text upload-text-new"]').click()
# time.sleep(3)
# file_path = "C:\\2寸.jpg"
# upload_file(file_path)