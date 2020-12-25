#配置文件
#引用数据文件 绝对路径
#配置文件一般存放：共用的数据 或者经常变化的数据
#.conf .ini  .properties
import configparser#专门处理配置文件
#配置文件：片段 section option 选项 values 值
#打开配置文件
class ReadConfig:
    def read_config(self,file_name,section,option):
        # print(file_name)
        cf=configparser.ConfigParser()#实例
        cf.read(file_name,encoding='UTF-8')
        #获取值：首先找到section 然后找到option
        value=cf.get(section,option)
        return value

        # name_1=cf.get('NAME','s_1')
        # print(type(name_1))

        # mode=cf.get('MODE','mode')
        # print(type(mode))
        #
        # list_1=cf.get('MODE','list')
        # print(type(eval(list_1)))

#所有的数据从配置文件进而面读取出来 都是str类型
#如果要转换格式 请记得用eval()
if __name__ == '__main__':
    value=ReadConfig().read_config('lemon.conf','NAME','S_3')
    print(value)