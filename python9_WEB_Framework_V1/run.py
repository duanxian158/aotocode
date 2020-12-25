# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 10:13
# @Author  : wangna
# @FileName: run.py
# @Software: PyCharm
#unitest 收集测试用例
import pytest
import time

curt_time = time.strftime("%Y%m%d %H%M%S",time.localtime())
pytest.main(["-m","","--reruns","2","--reruns-delay","5","--html=HtmlTestReport/report"+curt_time+".html"])

# pytest.main(["-m","smoke","--reruns","2","--reruns-delay","5","--html=HtmlTestReport/report"+curt_time+".html"])