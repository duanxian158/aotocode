# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 16:19
# @Author  : wangna
# @FileName: test_invest.py
# @Software: PyCharm
#投标
#正常场景
#前置
#1.用户余额够用：充值一个亿
#2.查看有多少余额，然后吵够200块，我就去充值。如果有就不充值了。
#不走WEB页面，走接口来实现。
#有可投次的标

#步骤
#首页-直接选择第一个标：
#标页面--获取用户可用余额
#标页面--输入金额，进行投资。投资金额：200
#标页页点击投资成功弹出框中的   查看并激活按钮

#验证
#个人页面：获取用户可用余额
#比对：投资金额 == 投资前的余额 - 投资后的余额
#投资记录？？？
#利息是多少？

import unittest
from TestDatas.CommonDatas import *
from PageObjects.login_page import LoginPage
from selenium import webdriver
# class TestInvest(unittest.TestCase):
#     def setUp(self):
#         #打开浏览器，登陆前程贷
#         self.driver = webdriver.Chrome()
#         self.driver.get(web_url)
#         LoginPage(self.driver).login(user,passwd)
#     def tearDown(self):
#         self.driver.quit()
#
#     def test_invest_sucess(self):
#
#         pass
#     def test_invest_fail_no100(self):
#         pass