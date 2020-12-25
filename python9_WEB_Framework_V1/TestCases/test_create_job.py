# -*- coding: utf-8 -*-
# @Time    : 2020/12/18 16:18
# @Author  : wangna
# @FileName: test_create_job.py

import pytest
from TestDatas.login_datas import *
from TestDatas.job_datas import *
from PageObjects.company_center_page import CompanyCenterPage
from PageObjects.CompanyCenterPageObjects.unpublish_job_page import UnPublishJobPage
from PageObjects.CompanyCenterPageObjects.create_job_page import CreateJobPage
from PageObjects.login_page import LoginPage
from Common.ramdon_fun import RamdonFun

@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.createjob
class TestCanbeJobfair():
    #正常场景  入驻招聘会成功

    def test_canbejobfair(self,init_indexEnv):
        #步聚 1.首页-点击招聘企业登录-进入企业登录页面-登录 2.企业中心页面-点击导航栏【岗位管理】  3.未发布岗位页面-【创建岗位】  4.创建岗位页面-填写信息-保存
        # 1.进入企业登录页面-企业登录
        init_indexEnv[1].click_companylogin()
        LoginPage(init_indexEnv[0]).login(login_succs["username"], login_succs["passwd"])
        # 2.在企业中心页面-点击导航栏【岗位管理】
        CompanyCenterPage(init_indexEnv[0]).click_jobmanage()
        # 3.未发布岗位页面-【创建岗位】
        UnPublishJobPage(init_indexEnv[0]).click_create_job()
        # 4.创建岗位页面-填写信息-保存
        num = RamdonFun().ramdom_num(3)
        CreateJobPage(init_indexEnv[0]).create_job_save("{0}{1}".format(job_sucess["gwname"],num),job_sucess["zprs"],job_sucess["dateend"],job_sucess["zplxr"],job_sucess["lxrphone"])
        #断言
        assert CreateJobPage(init_indexEnv[0]).get_noticecontent()=="保存成功"