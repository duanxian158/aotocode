from class_0821_openpyxl.do_excel import DoExcel
from class_0818_request.test_http_request import TestHttpRequest
import HTMLTestRunnerNew
import unittest
if __name__ == '__main__':
    test_data=DoExcel('python9.xlsx','Sheet2').do_excel()
    suite=unittest.TestSuite()
    # print(test_data)
    for item in test_data:
        print(item['url'], item['param'], item['excepted'], item['method'])
        # print(item['request_data'])
        # print(item['method'])
        # print(item['excepted'])
        suite.addTest(TestHttpRequest('test_login', item['url'], eval(item['param']), item['method'], item['excepted']))
    with open('test_report.html','wb+') as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(file)
        runner.run(suite)