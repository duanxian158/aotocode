import unittest
import HTMLTestRunnerNew
from homework_0816.read_data import ReadData
from homework_0816.httprequest import HttpRequest
if __name__ == '__main__':
    url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
    suite=unittest.TestSuite()
    #参数化在这里完成
    test_data=ReadData().readdata()
    # print(test_data)
    #url request_data,method,excepted
    for item in test_data:
        # print(item)

        suite.addTest(HttpRequest('test_login',url,item,'请求成功'))

    with open('test_report.html','wb+') as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(file)
        runner.run(suite)
