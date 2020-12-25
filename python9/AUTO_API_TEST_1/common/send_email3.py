# -*- coding: utf-8 -*-
# @Author  : wangna
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
_user = '963907017@qq.com'
_pwd = 'rqvonfzqgvjibdaj'#授权码
_host = 'smtp.qq.com'#设置服务器
email_to = 'wangna158@dingtalk.com'
now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳
my_sender = '963907017@qq.com'  # 发件人邮箱账号
my_pass = 'rqvonfzqgvjibdaj'  # 发件人邮箱密码
my_user = 'wangna158@dingtalk.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        #创建一个带附件的实例
        msg = MIMEMultipart()
        msg['Subject'] = now + 'hh测试报告'
        msg['From'] = _user
        msg['To'] = email_to
        #邮件正文
        msg.attach(MIMEText('这是自动化测试报告，请查收！'))

        #附件
        att1 = MIMEText(open('D:/python3.6/code/python9/AUTO_API_TEST_1/test_result/html_report/test_report.html', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att1)


        # msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        # msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        # msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        # msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题
        #
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

# class sendEmail:
    # def send_email(self,email_to,filepath):
    #     #如名字所示Multipart就是分多个部分
    #     msg = MIMEMultipart()
    #     msg['Subject'] = now+'hh测试报告'
    #     msg['From'] = _user
    #     msg['To'] = email_to
    #
    #     #---这是文字部分---
    #     part = MIMEText('这是自动化测试结果，请查收！')
    #     msg.attach(part)
    #
    #     #---这是附件部分----
    #     #xlsx类型附件
    #     part = MIMEApplication(open(filepath,'rb'))
    #     part.add_header('Content-Dispositon','attachment',filename=filepath)
    #     msg.attach(part)
    #     s = smtplib.SMTP_SSL('smtp.qq.com',timeout=30)#连接超时
    #     s.login(_user,_pwd)
    #     s.sendmail(_user,email_to,msg.as_string())#发送邮件
    #     s.close()

# if __name__ == '__main__':
#     email_to = 'wangna158@dingtalk.com'
#     filepath = 'D:/python3.6/code/python9/AUTO_API_TEST_1/test_result/html_report/test_report.html'
#     sendEmail().send_email(email_to,filepath)