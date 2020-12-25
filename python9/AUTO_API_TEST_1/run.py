import unittest
import HTMLTestRunnerNew
from common import pro_path
from common.send_email import sendEmail
from common.test_http_request import TestHttpRequest

suite = unittest.TestSuite()
#ddt 加载 loader
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

#生成测试报告  HTML
with open(pro_path.test_report_path,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(file,
                                              title='0901python测试报告',
                                              description='微信测试'
                                              )
    runner.run(suite)

#添加发送邮件的请求
sendEmail().send_email('wangna158@dingtalk.com',pro_path.test_report_path)
