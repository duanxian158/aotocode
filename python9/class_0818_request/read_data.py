class ReadData:
    def read_data(self):
        file=open('test_data','r',encoding='UTF-8')
        result=file.readlines()#按行读取数据 每一行作为列表里的一个子元素 返回的是列表
        # print(result[0])首先处理第一行数据 然后加for循环 处理多行数据
        test_data=[]
        for data_line in result:
            #切割
            result_split=data_line.split(';')#根据封号进行切割
            print(result_split)
            sub_dict={}
            for item in result_split:
                # print('切割前的数据',item)
                # print('切割后的数据',item.split(':',1))
                sub_split=item.split(':',1)#根据冒号切割1次
                sub_dict[sub_split[0]]=sub_split[1].strip('\n')
            test_data.append(sub_dict)#切割完 处理完的数据 放到这里来
        return test_data

if __name__ == '__main__':
    test_data=ReadData().read_data()
    print(test_data)

