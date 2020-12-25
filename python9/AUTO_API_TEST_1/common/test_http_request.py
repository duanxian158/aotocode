import unittest
from common import pro_path
from ddt import ddt,data
import logging
from common import my_logger
from common.do_excel import DoExcel
from common.http_request import HttpRequest

#获取测试数据
test_data = DoExcel(pro_path.test_data_path,'Sheet2').do_excel()
COOKIES = {} #全局变量

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
       self.t = DoExcel(pro_path.test_data_path, 'Sheet2') #创建一个实例

    @data(*test_data)
    def test_api(self,item):
        global COOKIES#声明全局变量，必要的时候去更新从cookie的值
        logging.info('正在执行第{0}条用例：{1}'.format(item['CaseId'],item['Title']))
        logging.info('发起请求的地址是：{0}'.format(item['URL']))
        logging.info('发起请求的参数是：{0}'.format(item['Param']))
        res = HttpRequest().http_request(item["URL"], eval(item["Param"]), item["Method"],cookies=COOKIES)
       #登录请求之后会产生一个cookie
        if res.cookies!={}:#如果cookie不为空  就对全局变量进行修改
            COOKIES = res.cookies
       # 断言
        try:
            self.assertEqual(item['ExpectedResult'],res.json()['Message'])
            TestResult = 'PASS'#存储测试用例的执行结果  通过是PASS  失败是fail
        except Exception as e:
            logging.error('出错了，错误是：{0}'.format(e))
            TestResult = 'FAIL'
            raise e
        finally:
            self.t.write_back(item['CaseId']+1,7,str(res.json()))#因为Excel里面只能支持传递字符串和整数，所以这里要强制转换一下
            self.t.write_back(item['CaseId'] + 1, 8, TestResult)