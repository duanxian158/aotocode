# -*- coding: utf-8 -*-
# @Time    : 2020/11/7 14:54
# @Author  : wangna
# @FileName: test_login.py
# @Software: PyCharm

#测试用例 = 页面对象当中的页面功能 +测试数据


from PageObjects.login_page import LoginPage
from Common.imge_code import ImageCode
from PageObjects.company_center_page import CompanyCenterPage
import pytest
#引入测试数据
from TestDatas.login_datas import  *

# @pytest.mark.testFail
# def test_failure_case():
#     print("=======我是一定会失败的用例")
#     assert False
# def test_demo():
#     print("我是模块下函数版本的测试用例!!!")

#fixtures函数名称

@pytest.mark.usefixtures("init_indexEnv")
class TestLogin:

    #正常场景-登录成功
    #init_loginEnv接收fixture运行的返回值[diver,loginp]
    @pytest.mark.smoke
    def test_login_success(self,init_indexEnv):
        #前置  -进入招聘企业登录页面
        init_indexEnv[1].click_companylogin()
        # # 登录 -获取验证码
        # image = ImageCode().image_str(init_loginEnv[0])
        LoginPage(init_indexEnv[0]).login(login_succs["username"],login_succs["passwd"])
        # 步骤  断言
        assert CompanyCenterPage(init_indexEnv[0]).get_companyname()==login_succs["check"]

    @pytest.mark.parametrize("data",login_noData)
    def test_login_failed_noUser(self,data,init_indexEnv):
        # 前置  -登录
        # 前置  -进入招聘企业登录页面
        init_indexEnv[1].click_companylogin()
        # 获取验证码
        # image = ImageCode().image_str(init_loginEnv[0])
        LoginPage(init_indexEnv[0]).login(data["usernmae"],data["passwd"])
        # 步骤  断言
        assert LoginPage(init_indexEnv[0]).get_errorMsg_fromLoginArea()==data["check"]

    # def test_login_failed_noPasswd(self):
    #     pass
    # def test_login_fail_wrong_userFormat(self):
    #     pass
    # def test_login_faile_wrongPasswd(self):
    #     pass