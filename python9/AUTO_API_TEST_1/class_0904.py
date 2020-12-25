import requests
login_url = 'http://101.201.144.11:10222/Login/SchoolUserLogin'
login_data = {'pxjgid':'0efb6b58-de90-4eab-b387-74025e35a27f','username':'admin','pwd':'21232F297A57A5A743894A0E4A801FC3'}
signsave_url = 'http://101.201.144.11:10222/SignManage/Save'
signsave_data = {'QZCZXID':'66666','QZRLX':'0','QZRID':'fe2d6522-f237-4cbd-8f78-eacd3d77df9a'}
#登录请求
# response = requests.post(login_url,login_data)
# res = response.json()#获取响应结果
# cookies = response.cookies#获取对应的cookie
# print('登录结果是：{0}'.format(res))
# print('登录成功产生的cookies是{0}'.format(cookies))
# #cookie他是类似于字典格式
# # print('ASP.NET_SessionId：{0}'.format(cookies['ASP.NET_SessionId']))
# res_1 = requests.post(signsave_url,signsave_data,cookies=cookies).json()
# print('提交结果是：{0}'.format(res_1))

#状态处理：每次请求 服务器都要检验你的状态
#cookie  session
#本地cookie session_id
#服务器 session  会话  会话时间
#每次提交请求的时候  会随带cookie  发送至服务器  检查会话是否已过共用
#当你在同一个会话下面  你的可以直接请求

#tooken是什么？ 鉴权  请求参数  header

#手机号码参数化的问题--怎样让手机自动的变化
#1:随机数？  138
#2：时间戳
#3：把数据存在Excel  0550-=》利用到用例 +1-》写回到excel里面
#4：如果你有数据库的操作权限  且手机号未加密
#利用sql查询当前库里面的最大的手机号  在这个基础上+1

