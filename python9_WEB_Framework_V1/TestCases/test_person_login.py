# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 16:53
# @Author  : wangna
# @FileName: test_person_login.py

from TestDatas.login_datas import *
from PageObjects.index_page import IndexPage
from PageObjects.person_login_page import PersonLoginPage
from PageObjects.person_center_page import PersonCenterPage
import pytest
#个人登录
@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.personlogin
class TestPersonLogin:
    def test_personglogin_sucess(self,init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"],person_login_succs["passwd"])
        # 3.登录成功后跳转至个人中心页面
        assert PersonCenterPage(init_indexEnv[0]).get_countname() == person_login_succs["check"]