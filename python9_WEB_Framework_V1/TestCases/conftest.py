# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 14:24
# @Author  : wangna
# @FileName: conftest.py
import pytest
import time
from selenium import webdriver
from PageObjects.index_page import IndexPage
from TestDatas.CommonDatas import *
#登录用例的前置条件
#setupt和teardown
@pytest.fixture()
def init_indexEnv():
    #前置
    driver = webdriver.Chrome(chrom_path)
    driver.maximize_window()
    driver.get(web_url)
    indexp = IndexPage(driver)
    yield[driver,indexp]#返回数据  列表类型
    #打开浏览器访问网址
    #后置
    driver.quit()

#setupClasst 和teardownClass
@pytest.fixture(scope="class")
def class_demo():
    print("==========我是class级别的fixture==============")
