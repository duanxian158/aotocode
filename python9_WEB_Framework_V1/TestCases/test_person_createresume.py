# -*- coding: utf-8 -*-
# @Time    : 2020/12/11 13:53
# @Author  : wangna
# @FileName: test_person_createresume.py
#创建个人简历
import pytest
from PageObjects.index_page import IndexPage
from PageObjects.person_login_page import PersonLoginPage
from PageObjects.person_center_page import PersonCenterPage
from PageObjects.resume_manage_page import ResumeManagePage
from TestDatas.login_datas import *
from Common.ramdon_fun import RamdonFun
@pytest.mark.usefixtures("init_indexEnv")
@pytest.mark.createresume
class TestPersonCreateresum:
    #添加求职意向
    def test_jobintention_success(self,init_indexEnv):
        #1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"],person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-添加求职意向
        jobname = RamdonFun().ramdom_num(3)
        ResumeManagePage(init_indexEnv[0]).add_job_intention("自动岗位{0}".format(jobname))
        #断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "添加成功！"
    #
    # #删除求职意向
    def test_deljobintention(self,init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"], person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-删除求职意向
        ResumeManagePage(init_indexEnv[0]).del_job_initention()
        # 断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "删除后不可恢复，确认删除吗！"

    #     # 添加工作经历
    #
    def test_workexprience_success(self, init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"], person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-添加求职意向("自动企业{0}".format(num),("自动岗位{0}".format(num)
        num = RamdonFun().ramdom_num(3)
        ResumeManagePage(init_indexEnv[0]).add_work_exprience("自动企业{0}".format(num),"企业岗位{0}".format(num),"{0}能够精通各种计算机前沿理论、具体的软硬件开发技术、大型数据库的知识、项目的整体规划和框架设计、模块式设计和开发技术、数字化建设知识等等。系统分析师具备在一个信息化项目从立项到正式上线整个过程中".format(num))
        # 断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "添加成功！"

    #删除工作经历
    def test_delworkexprience(self,init_indexEnv):
        #1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"], person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-添加求职意向("自动企业{0}".format(num),("自动岗位{0}".format(num)
        ResumeManagePage(init_indexEnv[0]).del_work_exprience()
        # 断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "删除后不可恢复，确认删除吗！"

    #添加项目经历
    @pytest.mark.project
    def test_projectexprience(self,init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"], person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-添加项目("自动企业{0}".format(num),("自动岗位{0}".format(num)
        num = RamdonFun().ramdom_num(3)

        ResumeManagePage(init_indexEnv[0]).add_project_exprience("aoto项目{0}".format(num),"aoto项目描述{0}".format(num),"aoto职责描述{0}".format(num))
        # 断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "添加成功"

    # 删除工作经历
    @pytest.mark.project
    def test_delworkexprience(self, init_indexEnv):
        # 1.首页-个人登录
        IndexPage(init_indexEnv[0]).click_personlogin()
        # 2.登录页面-输入账户密码-登录成功
        PersonLoginPage(init_indexEnv[0]).person_login(person_login_succs["username"], person_login_succs["passwd"])
        # 3.个人中心页面-点击菜单-简历管理
        PersonCenterPage(init_indexEnv[0]).click_resumemanage()
        # 4.简历管理页面-添加求职意向("自动企业{0}".format(num),("自动岗位{0}".format(num)
        ResumeManagePage(init_indexEnv[0]).del_project_exprience()
        # 断言
        assert ResumeManagePage(init_indexEnv[0]).get_save_prompt() == "删除后不可恢复，确认删除吗！"