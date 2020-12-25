# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 14:43
# @Author  : wangna
# @FileName: login_datas.py
# @Software: PyCharm

#正常场景-- 登录成功的测试数据
#字典
login_succs = {"username":"18800000000",
               "passwd":"123456",
               "check":"武汉时济堂医药有限公司"}
#异常场景--无用户名，无密码，无手机号 不正确
#列表
login_noData = [{"usernmae":"","passwd":"123456","check":"手机号码格式有误!"},
                {"usernmae":"18800000000","passwd":"","check":"密码不能为空!"}]


#个人登录数据
person_login_succs = {"username":"15800000001","passwd":"123456","check":"陈功华"}
