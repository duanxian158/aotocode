# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 14:35
# @Author  : wangna
# @FileName: test_company_regist.py

import pytest
from PageObjects.company_regist_one_page import CompantyRegistOnePage
from PageObjects.company_regist_next_page import CompantyRegistNextPage
from PageObjects.company_center_page import CompanyCenterPage
from TestDatas.companyregist_datas import *
from Common.ramdon_fun import RamdonFun

@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.companyregist
class TestCompanyRegist:
    def test_companyregist_sucess(self,init_indexEnv):
        # 1.首页-招聘企业注册
        init_indexEnv[1].click_companyregist()
        #手机号随机获取
        phone = RamdonFun().create_phone()
        # 2.企业注册页面-填写信息-点击下一步
        CompantyRegistOnePage(init_indexEnv[0]).click_registone(companyregist_sucess["codetypeno"],companyregist_sucess["companyname"],companyregist_sucess["companyno"],companyregist_sucess["companypwd"],companyregist_sucess["companypwd2"])
        # 3.下一步页面-填写信息-点击注册
        CompantyRegistNextPage(init_indexEnv[0]).click_registnext(companyregist_sucess["managename"],companyregist_sucess["manageidcard"],phone,companyregist_sucess["phonecode"])
        # 4.注册成功-跳转至企业中心页面
        assert CompanyCenterPage(init_indexEnv[0]).get_companyname()== companyregist_sucess["check"]