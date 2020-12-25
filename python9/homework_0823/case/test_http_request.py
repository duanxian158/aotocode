#单元测试  写测试用例 对不同的接口写测试用例
import unittest
from homework_0823.common.http_request import HttpRequest
class TestHttpRequest(unittest.TestCase):
    def __init__(self,methodName,url,request_data,method,excepted):
        super(TestHttpRequest,self).__init__(methodName)
        self.url=url
        self.request_data=request_data
        self.method=method
        self.excepted=excepted
    def test_login(self):#正常登录
        # url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
        # request_data = {'ACB501': '18911111111', 'UCC003': 'E10ADC3949BA59ABBE56E057F20F883E'}
        # method='post'
        res=HttpRequest().http_request(self.url,self.request_data,self.method)
        # print(res.text)
        try:
            self.assertEquals(self.excepted,res.json()['Message'])
        except AssertionError as e:
            print('登录请求出错了{0}'.format(e))
            raise e
    #
    # def test_wrong_login(self):#登录失败
    #     url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
    #     request_data = {'ACB501': '18911111133', 'UCC003': 'E10ADC3949BA59ABBE56E057F20F883E'}
    #     method='post'
    #     res=HttpRequest().http_request(url,request_data,method)
    #     try:
    #         self.assertEquals('登录失败',res.json()['Message'])
    #     except AssertionError as e:
    #         print('登录请求出错了{0}'.format(e))
    #         raise e
if __name__ == '__main__':
    TestHttpRequest()