
#学习一下模块引入
#1.import  from...import
# import class_0807_object.class_0807_1
# #导入 引入 具体到模块名
# class_0807_object.class_0807_1.SuperBoyFriend('王思聪').coding('python')
# #使用引入模块里面的类
# from class_0807_object.class_0807_1 import SuperBoyFriend
# from class_0807_object.class_0807_1 import BoyFriend
# # 多继承
# class BestBoyFriend(SuperBoyFriend,BoyFriend):
#     pass
#继承顺序
# BestBoyFriend('彭于晏').coding('java')
class Mother:
    def __init__(self,name):
        self.name=name
    def cooking(self):
        print('我妈：{0}是中华小当家'.format(self.name))
    def running(self):
        print('我：{0}可以跑3000米'.format(self.name))

class Dad:
    def __init__(self,name):
        self.name=name
    def swiming(self):
        print('我{0}会游泳'.format(self.name))
    def cooking(self,fish):
        print('我只会煮{0}吃'.format(fish))
# 超继承 贪婪继承
class Son(Dad):
    def cooking(self,dish_name,fish):
        super(Son,self).cooking(fish)
        print('我做的{0}非常好吃'.format(dish_name))


t=Son('Summer')
t.cooking('辣椒炒辣椒')

#调试
#1：print 掌握最快
#2：debug 难度最快  但是实用  最快可以发现BUG
#出现error的时候 我需要去调试 报错时候
#你要知道出错的代码在哪一行
#3：logging 日志 手把手带你去写日志类
# 可以打印你的代码的所有的运行情况
#我安排的作业 请你按照类的标准去写？
