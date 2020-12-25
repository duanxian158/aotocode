#单元测试  写测试用例 对不同的接口写测试用例
import unittest
from homework_0823_auto_api.common.http_request import HttpRequest
from ddt import ddt,data,unpack
from homework_0823_auto_api.conf import read_path
from homework_0823_auto_api.common.do_excel import DoExcel
from homework_0823_auto_api.common.read_config import ReadConfig
mode=ReadConfig().read_config(read_path.conf_path,'MODE','mode')
case_id_list = ReadConfig().read_config(read_path.conf_path, 'MODE', 'case_id_list')
test_data=DoExcel(read_path.test_data_path,'Sheet2').do_excel(mode,case_id_list)
@ddt
class TestHttpRequest(unittest.TestCase):#创建测试用例
    @data(*test_data)
    def test_login(self,item):#正常登录
        # url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
        # request_data = {'ACB501': '18911111111', 'UCC003': 'E10ADC3949BA59ABBE56E057F20F883E'}
        # method='post'
        res=HttpRequest().http_request(item['url'],eval(item['param']),item['method'])
        # res=HttpRequest().http_request(self.url,self.request_data,self.method)
        # print(res.json('Message'))
        # print(eval(item['excepted']))
        try:
            self.assertEqual(eval(item['excepted'])['Message'],res['Message'])
        except AssertionError as e:
            print('登录请求出错了{0}'.format(e))
            raise e

if __name__ == '__main__':
    TestHttpRequest()