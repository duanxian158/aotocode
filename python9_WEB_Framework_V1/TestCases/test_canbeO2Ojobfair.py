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
from PageObjects.CompanyCenterPageObjects.O2Ojobfairmanage_page import O2OJobFairManagePage
from PageObjects.CompanyCenterPageObjects.canbein_O2Ojobfair_page import CanbeO2OJobFairPage
from PageObjects.CompanyCenterPageObjects.O2Omyjobfairdetail_page import O2OMyJobFairDetailPage
from Common.imge_code import ImageCode
from PageObjects.login_page import LoginPage
from Common.ramdon_fun import RamdonFun
@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.O2Ojobfair
class TestCanbeJobfair():
    #正常场景  入驻招聘会成功

    def test_canbejobfair(self,init_indexEnv):
        #步聚 1.首页-点击招聘企业登录-进入企业登录页面-登录 2.企业中心页面-点击招聘会管理-网络招聘会  3.点击可入驻招聘会  4.我要入驻 5 勾选导入岗位提交
        init_indexEnv[1].click_companylogin()
        LoginPage(init_indexEnv[0]).login(login_succs["username"],  login_succs["passwd"])
        CompanyCenterPage(init_indexEnv[0]).cilick_O2Ojobfair()
        O2OJobFairManagePage(init_indexEnv[0]).click_canbeO2Ojobfair()
        CanbeO2OJobFairPage(init_indexEnv[0]).click_intoO2Ojobfair()
        #断言
        assert O2OMyJobFairDetailPage(init_indexEnv[0]).get_shzt()=="审核中"
    def test_canbejobfair_creatjob(self,init_indexEnv):
        # 步聚 1.企业登录页面-登录 2.企业中心页面-点击招聘会管理-网络招聘会  3.点击可入驻招聘会  4.我要入驻  5 创建新岗位提交
        init_indexEnv[1].click_companylogin()
        LoginPage(init_indexEnv[0]).login(login_succs["username"], login_succs["passwd"])
        CompanyCenterPage(init_indexEnv[0]).cilick_O2Ojobfair()
        O2OJobFairManagePage(init_indexEnv[0]).click_canbeO2Ojobfair()
        num = RamdonFun().ramdom_num(3)
        CanbeO2OJobFairPage(init_indexEnv[0]).click_intoO2Ojobfair_creatjob("{0}{1}".format(job_sucess["gwname"],num),job_sucess["zprs"],job_sucess["zplxr"],job_sucess["lxrphone"])
        # 断言"
        assert O2OMyJobFairDetailPage(init_indexEnv[0]).get_shzt() == "审核中"


