# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 15:48
# @Author  : wangna
# @FileName: logger.py
# @Software: PyCharm
import time
import logging
import logging.handlers
from Common import dir_config
# 控制日志输出格式
fmt = "%(asctime)s-%(levelname)s-%(filename)s %(funcName)s [line:%(lineno)d] %(name)s-日志信息：%(message)s"
# 日期格式
dfmt='%a, %d %b %Y %H:%M:%S'
handler_1 = logging.StreamHandler()#到控制台
curTime = time.strftime("%Y-%m-%d",time.localtime())

handler_2 = logging.FileHandler(dir_config.logs_dir+"/Web_Autotest_"+curTime+".log",encoding="utf-8")

#设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=dfmt,level=logging.INFO,handlers=[handler_1,handler_2])
logging.info("hehehe")