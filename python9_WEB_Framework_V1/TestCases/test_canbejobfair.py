# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 10:30
# @Author  : wangna
# @FileName: test_canbejobfair.py

#企业入驻网络招聘会
#fixtures函数名称
import pytest
from TestDatas.login_datas import *
from TestDatas.job_datas import *
from PageObjects.company_center_page import CompanyCenterPage
from PageObjects.myjobfair_page import MyJobFairPage
from PageObjects.canbein_jobfair_page import CanbeJobFairPage
from PageObjects.myjobfairdetail_page import MyJobFairDetailPage
from Common.imge_code import ImageCode
from PageObjects.login_page import LoginPage

@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.jobfair
class TestCanbeJobfair():
    #正常场景  入驻招聘会成功

    def test_canbejobfair(self,init_indexEnv):
        #步聚 1.首页-点击招聘企业登录-进入企业登录页面-登录 2.企业中心页面-点击招聘会管理-网络招聘会  3.点击可入驻招聘会  4.我要入驻 5 勾选导入岗位提交
        init_indexEnv[1].click_companylogin()
        LoginPage(init_indexEnv[0]).login(login_succs["username"],  login_succs["passwd"])
        CompanyCenterPage(init_indexEnv[0]).cilick_jobfair()
        MyJobFairPage(init_indexEnv[0]).click_canbejobfair()
        CanbeJobFairPage(init_indexEnv[0]).click_intojobfai()
        #断言
        assert MyJobFairDetailPage(init_indexEnv[0]).get_shzt()=="审核中"
    def test_canbejobfair_creatjob(self,init_indexEnv):
        # 步聚 1.企业登录页面-登录 2.企业中心页面-点击招聘会管理-网络招聘会  3.点击可入驻招聘会  4.我要入驻  5 创建新岗位提交
        init_indexEnv[1].click_companylogin()
        LoginPage(init_indexEnv[0]).login(login_succs["username"], login_succs["passwd"])
        CompanyCenterPage(init_indexEnv[0]).cilick_jobfair()
        MyJobFairPage(init_indexEnv[0]).click_canbejobfair()
        CanbeJobFairPage(init_indexEnv[0]).click_intojobfair_creatjob(job_sucess["gwname"],job_sucess["zprs"],job_sucess["zplxr"],job_sucess["lxrphone"])
        # 断言"
        assert MyJobFairDetailPage(init_indexEnv[0]).get_shzt() == "审核中"


