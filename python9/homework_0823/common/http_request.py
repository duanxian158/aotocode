import  requests
#如果要完成不同接口的请求 为了最高的复用性 我们可以封装成函数
#请求地址
#升级成类
#写这个类的目的：完成接口测试
class HttpRequest:
    def http_request(self,url,request_data,method):
        if method.lower()=='get':
            try:
                response=requests.get(url,request_data)
            except Exception as e:
                print('get请求出错了：{0}'.format(e))
                raise e
        elif method.lower()=='post':
            try:
                response=requests.post(url,request_data)
            except Exception as e:
                print('post请求出错了：{0}'.format(e))
                raise e
        else:
            print('method方式不对')
        return response
if __name__ == '__main__':
    url = 'http://47.104.134.50:8554/person/ElectronicCertificates/account/v1.0/ByMobile'
    request_data = {'ACB501': '18911111111', 'UCC003': 'E10ADC3949BA59ABBE56E057F20F883E'}
    # 发起请求 POST
    response = HttpRequest().http_request(url,request_data,'post')
    print(response.text)
    print(response.json()['Message'])
    # 响应数据
    # print(response.text)
    # print(response.json())
#有时间可以去了解下装饰器
# #响应头
# print(response.headers)
# #状态码
# print(response.status_code)