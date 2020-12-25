#写一个接口类：专门完成接口测试
import requests
import logging
from common import my_logger
class HttpRequest:
    def http_request(self, url, param, method,cookies):
        if method.upper() == 'GET':#防止我们自己输入不分大小写 写错
            try:
                response=requests.get(url, param,cookies=cookies)
            except Exception as e:
                logging.error('GET请求出错了：{0}'.format(e))
                raise e #抛出错误
        elif method.upper() == 'POST':
            try:
                response = requests.post(url, param,cookies=cookies)
            except Exception as e:
                logging.error('POST请求出错了')
                raise e #抛出错误
        else:
            logging.error('输入的请求方法不存在')
        return response#返回结果

#测试代码
if __name__ == '__main__':
    url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
    param = {'ACB501': '15872356845', 'UCC003': 'E10ADC3949BA59ABBE56E057F20F883E'}
    res = HttpRequest().http_request(url,param,'post')
    print('http请求返回的结果是：{0}'.format(res))