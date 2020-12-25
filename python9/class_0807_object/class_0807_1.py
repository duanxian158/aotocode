class BoyFriend:
    #初台化函数里面可以放属性值
    def __init__(self,money,height=170):#出厂设置
        self.money=money
        self.height=height
    #共同的行为
    def cooking(self,language1,languge2): #类函数里面的第一个参数必须是self 未代表任何参数
        self.coding(language1,languge2)
        print('我男朋友会做饭')
    def coding(self,str_1,str_2):
        print('我的男朋友会写{0},{1}代码！超赞的！'.format(str_1,str_2))
    def sport(self,*spt):
        # self.describe()
        sport_item=''
        for item in spt:
            sport_item+=item
            sport_item+='、'
        return ('我男朋友喜欢{0}！'.format(sport_item))
        # print('我的男朋友喜欢{0}'.format(spt))
    def describe(self):
        print('我的男朋友有存款{0},身高是{1}'.format(self.money,self.height))

#特殊的函数：初始化函数
#__init__()#初始化函数 跟普通函数一样
#继承：重写&拓展
class SuperBoyFriend(BoyFriend):
    #重写：1：子类里面的函数名与父类函数名一样  那么就直接覆盖
    #2：重写是针对有需要做修改的父类里面的函数
    def __init__(self,name):
        self.name=name
    def coding(self,str_1):
        print('我的男朋友{0}会写{1}代码！超赞的！'.format(self.name,str_1))
    def fly(self): #拓展：父类里面没有的函数 但是子类有 这个叫拓展
        self.sport('篮球','羽毛球')#这个操作经常用
        self.coding('java')
        print('可以飞到珠穆朗玛峰')
#爸爸的就是我的
#SuperBoyFriend 子类  BoyFriend 父类
#写测试代码

if __name__=='__main__':#函数执行入口
    t=SuperBoyFriend("王思聪")
    t.coding('python')
    print(t.name)
    t.fly()
#只有在执行当前模块的时候main里面的代码才会被执行
#如果在别的页面调用这个模块  代码不会被执行
    # print(t.sport('篮球','羽毛球'))





# t=BoyFriend(200000,185)
# print('存款：{0}，身高：{1}'.format(t.money,t.height))
