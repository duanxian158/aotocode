from homework_0823.common.do_excel import DoExcel
from homework_0823.case.test_http_request import TestHttpRequest
import HTMLTestRunnerNew
import unittest
from homework_0823.conf import read_path
from homework_0823.common.read_config import ReadConfig
if __name__ == '__main__':
    mode=ReadConfig().read_config(read_path.conf_path,'MODE','mode')
    case_id_list = ReadConfig().read_config(read_path.conf_path, 'MODE', 'case_id_list')
    test_data=DoExcel(read_path.test_data_path,'Sheet2').do_excel(mode,case_id_list)
    suite=unittest.TestSuite()
    # print(test_data)
    for item in test_data:
        # print(item['url'], item['param'], item['excepted'], item['method'])
        # print(item['request_data'])
        # print(item['method'])
        # print(item['excepted'])
        suite.addTest(TestHttpRequest('test_login', item['url'], eval(item['param']), item['method'], item['excepted']))
    with open(read_path.report_path,'wb+') as file:
        runner=HTMLTestRunnerNew.HTMLTestRunner(
            file,
            verbosity=2,#默认值可以不写
            title='哈哈测试报告',
            description='homework_0823'
        )
        runner.run(suite)