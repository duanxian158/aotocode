
#类  人类  动物类  植物类  妖类
#人以群分  物以类聚
#具有共同的属性   特性这些事物  就划分为类
#谁来定义类  怎么来定义类
#python 类的语法
#关键字 class
#定义一个类：
#class 类名
    #这一类 共同的属性
    #这一类 共同的行为/方法（用函数来表达）---类函数 类方法
#类名的规范：驼峰 首字母大写 见名知意
# BoyFriend
# MyGirl

#单身girl  你理想中的男朋友是怎么样的？
#帅的  高富帅 1.8  有内涵  支持你  幽默
#有钱  阳光  成熟  潜力股  有上进心
#会做饭  会python

#男朋友类
class BoyFriend:
    #共同的属性
    money=10000
    height=180
    #共同的行为
    def cooking(self,language1,languge2): #类函数里面的第一个参数必须是self 未代表任何参数
        self.coding(language1,languge2)
        print('我男朋友会做饭')
    def coding(self,str_1,str_2):
        print('我的男朋友会写{0},{1}代码！超赞的！'.format(str_1,str_2))
    def sport(self,*spt):
        self.describe()
        sport_item=''
        for item in spt:
            sport_item+=item
            sport_item+='、'
        return ('我男朋友喜欢{0}'.format(sport_item))
        # print('我的男朋友喜欢{0}'.format(spt))
    def describe(self):
        print('我的男朋友有存款{0},身高是{1}'.format(self.money,self.height))
#类属性和函数的调用 抽象--具体的对象  实例化
#语法:创建一个实例 类名()
# my_bf=BoyFriend() #对象/实例
# my_bf.money=200000
# my_bf.coding('JAVA','C++')
# my_bf.sport()
# print('身高：{0}'.format(my_bf.money))
# BoyFriend().cooking()
#关于类与实例的特性
#1：类里面的属性和函数 只能是由实例/对象来调用

#类函数的特性
#1：#类函数里面的第一个参数必须是self 未代表任何参数
#1：可以传位置参数吗？可以！！！
#2：可以传多个位置参数吗？可以！！！
#4：可以传默认参数吗？必须可以！！！
#5：位置参数必须是放在默认参数之前！
#5：可以传动态参数，关键字参数吗
# BoyFriend().sport('打篮球','打羽毛球','打乒乓球')
#7:类函数要调用类里面的属性  必须是这样调用 self.属性名
# BoyFriend().describe()
#7:类函数之间可以相互调用吗  必须是这样调用 self.函数名(参数)
c=BoyFriend().sport('打篮球','打羽毛球','打乒乓球')
print(c)
# BoyFriend().cooking('PHP','c#')

#课堂练习：
#请随意发挥 写一个软件测试工程师类
#写好了 发截图到讨论区  或者是py9群里
#时间：15分钟
# class SofewaretTesting:
#     education='大专及以上'
#     age='22岁以上'
#     def skill(self,ski_1):
#         print('技能：会{0}'.format(ski_1),end='')
#     def language(self,language_1):
#         return language_1
# soft_test=SofewaretTesting()
# print('软件测试要求：{0},{1}'.format(soft_test.education,soft_test.age),end='')
# print()
# soft_test.skill('oralce')
# print(soft_test.language(',会python自动化'))



