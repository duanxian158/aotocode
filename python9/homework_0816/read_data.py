class ReadData:
    def readdata(self):
        file=open('test_data','r',encoding='UTF-8')
        result=file.readlines()
        # return test_data
        test_data=[]
        # print('文件结果:{0}'.format(result))
        for line_data in result:
            # print('循环读取每行:{0}'.format(line_data))
            split_data=line_data.split(',')
            # print('切割后:{0}'.format(split_data))
            dict_data = {}
            for item in split_data:
                # print(item)
                sub_split = item.split(':', 1)  # 切割
                dict_data[sub_split[0]]=sub_split[1].strip('\n')
            test_data.append(dict_data)
        return test_data

if __name__ == '__main__':
    test=ReadData().readdata()
    print(test)


