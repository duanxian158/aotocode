# -*- coding: utf-8 -*-
# @Time    : 2020/12/16 16:23
# @Author  : wangna
# @FileName: test_apply_job.py

import pytest
from TestDatas.login_datas import *
from PageObjects.index_page import IndexPage
from PageObjects.person_login_page import PersonLoginPage
from PageObjects.person_center_page import PersonCenterPage
from PageObjects.PersonalCenterPageObjects.job_detail_page import JobDetailPage
from PageObjects.PersonalCenterPageObjects.job_search_page import JobSearchPage
from PageObjects.PersonalCenterPageObjects.job_recommen_page import JobRecommenPage
@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.applyjob
class TestApplyJob:

    #投递简历
    @pytest.mark.applyjob1
    def test_applyjob_success(self,init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账号密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"],person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-岗位搜索
        PersonCenterPage(init_indexEnv[0]).click_jobsearch()
        # 4.岗位搜索页面-点击申请职位
        JobSearchPage(init_indexEnv[0]).click_aplly_job()
        assert JobSearchPage(init_indexEnv[0]).get_noticecontent() == "申请成功"

    #收藏岗位
    def test_collectjob_succes(self,init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账号密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"],person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-岗位推荐
        PersonCenterPage(init_indexEnv[0]).click_jobrecommen()
        # 4.岗位推荐页面-点击岗位
        JobRecommenPage(init_indexEnv[0]).click_jobname()
        # 5.岗位详情页面-点击收藏，收藏成功
        JobDetailPage(init_indexEnv[0]).collect_job()
        assert JobDetailPage(init_indexEnv[0]).get_noticecontent() == "收藏成功"