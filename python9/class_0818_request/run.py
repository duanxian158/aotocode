import unittest
import HTMLTestRunnerNew
from class_0818_request.test_http_request import TestHttpRequest
from class_0818_request.read_data import ReadData
if __name__ == '__main__':

    suite=unittest.TestSuite()
    #参数化在这里完成
    test_data=ReadData().read_data()
    # print(test_data)
    #url request_data,method,excepted
    for item in test_data:
        # print(item)
        print(item['url'],item['request_data'],item['method'],item['excepted'])
        # print(item['request_data'])
        # print(item['method'])
        # print(item['excepted'])
        suite.addTest(TestHttpRequest('test_login',item['url'],eval(item['request_data']),item['method'],item['excepted']))

    with open('test_report.html','wb+') as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(file)
        runner.run(suite)
