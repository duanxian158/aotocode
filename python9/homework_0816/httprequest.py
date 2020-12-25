import requests
import unittest
class HttpRequest(unittest.TestCase):#HTTP请求类
    def __init__(self,methodName,url,request_data,excepted):
        super(HttpRequest, self).__init__(methodName)
        self.url=url
        self.request_data=request_data
        self.excepted=excepted
    def test_login(self):#get请求
        res=requests.post(self.url,self.request_data)
        result=res.json()['Message']#获取响应结果
        try:
            self.assertEquals(self.excepted,result)
        except AssertionError as e:
            print('执行用例的时候出错了，报错是：')
            raise



