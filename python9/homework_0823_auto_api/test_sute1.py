
from homework_0823_auto_api.case.test_http_request import TestHttpRequest
import HTMLTestRunnerNew
import unittest
from homework_0823_auto_api.conf import read_path
if __name__ == '__main__':

    suite=unittest.TestSuite()#创建的测试套件
    loader=unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
    with open(read_path.report_path,'wb+') as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(
            file,
            verbosity=2,#默认值可以不写
            title='哈哈测试报告',
            description='homework_0823'
        )
        runner.run(suite)