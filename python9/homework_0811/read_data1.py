

def read_data1(file):
    file=open(file,'r',encoding='UTF-8')
    test_data=file.readlines()#按行读取数据 每一行作为列表里的一个子元素 返回的是列表
    list_data=[]
    for line_data in test_data:
        split_data=line_data.split(',')
        # split_data=test_data[0].split(',')
        # print('第一行切割后的结果：{0}'.format(split_data))
        dict_data={}
        for item in split_data:
            # print(item.split(':')[0]+'..........'+item.split(':')[1])
            dict_data[item.split(':')[0]]=item.split(':')[1].strip('\n')
            print(dict_data)
        list_data.append(dict_data)

    return list_data

if __name__ == '__main__':
    result=read_data1('test_data2')
    print(result)