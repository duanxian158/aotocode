

class ReadData:
    def read_data(self):
        file=open('test_data','r')
        test_data=file.readlines()#按行读取数据 每一行作为列表里的一个子元素 返回的是列表
        return test_data
# file=open('test_data','r')
# test_data=file.readlines()#按行读取数据 每一行作为列表里的一个子元素 返回的是列表
# print(test_data)
# for item in test_data:
#     print(item)


