# -*- coding: utf-8 -*-
# @Author  : wangna
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
_user = '963907017@qq.com'
_pwd = 'rqvonfzqgvjibdaj'#授权码
_host = 'smtp.qq.com'#设置服务器
now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳
class sendEmail:
    def send_email(self,email_to,filepath):
        #如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg['Subject'] = now+'hh测试报告'
        msg['From'] = _user
        msg['To'] = email_to

        #---这是文字部分---
        part = MIMEText('这是自动化测试结果，请查收！')
        msg.attach(part)

        #---这是附件部分----
        #xlsx类型附件
        part = MIMEText(open(filepath,'rb').read(), 'base64', 'utf-8')
        part["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        part["Content-Disposition"] = 'attachment; filename='+now+'test_report.html'
        msg.attach(part)
        s = smtplib.SMTP_SSL('smtp.qq.com',timeout=30)#连接超时
        s.login(_user,_pwd)
        s.sendmail(_user,email_to,msg.as_string())#发送邮件
        s.close()

if __name__ == '__main__':
    email_to = 'wangna158@dingtalk.com'
    filepath = 'D:/python3.6/code/python9/AUTO_API_TEST_1/test_result/html_report/test_report.html'
    sendEmail().send_email(email_to,filepath)