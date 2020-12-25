# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 16:13
# @Author  : wangna
# @FileName: test_person_regist.py
import pytest
from PageObjects.index_page import IndexPage
from PageObjects.person_regist_page import PersonRegistPage
from PageObjects.person_center_page import PersonCenterPage
from TestDatas.personregist_datas import *
from Common.ramdon_fun import RamdonFun
@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.personregist
class TestPersonRegist:
    def test_personregist_sucess(self,init_indexEnv):
        # 1.首页-个人注册
        IndexPage(init_indexEnv[0]).click_personregist()
        # 2.个人注册页面-填写信息-注册
        # 手机号随机获取
        phone = RamdonFun().create_phone()
        PersonRegistPage(init_indexEnv[0]).click_person_regist(phone,personregist_sucess["phonecode"],personregist_sucess["pwd"],personregist_sucess["pwd2"])
        # 3.注册成功-跳转至个人中心页面
        assert PersonCenterPage(init_indexEnv[0]).get_phone() == phone