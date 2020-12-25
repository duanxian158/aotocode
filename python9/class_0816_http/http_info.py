#请求参数  用户名  密码
#响应头 响应头字段  可以课后去拓展
#响应报文--》响应数据 xml json html 格式？
#<name>'小幸福'</name>-->xml
#{"name":"小幸福"}-->json
#<html> </html>-->html

import requests
url='http://www.baidu.com'
#get请求
# res=requests.get(url)#发起一个http请求
# # print(type(res))
# response=res.text#html xml json 用text去解析
# print(response)
# print('状态码',res.status_code)
#200 404 502 403 401 500 起码了解10个
#200 表示你的请求被服务器接受了 并且服务器返回了结果
# response_2=res.json()#只有当你返回的数据格式是json的 才可以用json

#post 请求
# res=requests.post(url)
# # print(res.text)
# print(res.status_code)

#登录的请求 发起一个有参数的http请求
url='http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
request_data={'ACB501':'18911111111','UCC003':'E10ADC3949BA59ABBE56E057F20F883E'}
login_res=requests.post(url,request_data)
print(login_res.text)#字符串
print(login_res.json()['Message'])#字典
#如果返回的是json格式的数据 推荐用json去解析

#8-16 编写HTTP单元测试类
# 1：根据老师上课讲解的requests完成的get请求和post请求，编写一个http请求类，里面有一个类函数：http.request()
# 可以根据你们指定的方法完成get请求或者是post请求
# 2：请根据你们自己写的http请求类，编写 一个测试类
# 3：请根据你们写的测试类，完成单元测试，生成测试报告

