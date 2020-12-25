# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 15:43
# @Author  : wangna
# @FileName: dir_config.py
# @Software: PyCharm
import os
#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
#测试数据的路径
testdatas_dir = os.path.join(base_dir,"TestDatas")
#测试用例的路径
testcases_dir = os.path.join(base_dir,"TestCases")
#测试报告的路径
htmlreport_dir = os.path.join(base_dir,"HtmlTestReport")
#日志路径
logs_dir = os.path.join(base_dir,"Logs")
#截图路径
screenshot_dir = os.path.join(base_dir,"ScreenShot")