
#今天的主题：讲函数  做拓展题
#1:return  关键字
#2：内置函数、函数之间的调用（先定义了才可以调用，参数的传递）
#3：变量的作用域
#4：编写函数的三个步骤

#def 函数名(参数)
    #函数体
#调用：函数名(对应个数的参数)
# def greet_user():
#     print('你好呀！')
# def greet_user(text,time='星期五晚上',name='铁硬'):
# def greet_user(text,name):
#     print(name)
#     # print(time)
#     print(text)
# # greet_user('july','你好棒棒呀')
# # greet_user(text='你好棒棒呀',name='july')
# # greet_user('你好棒棒呀')
# greet_user('你又迟到了呀',name='yeren')
#1：函数可不可以没有参数？当然可以
#2：函数可以有多个参数吗？当然可以
#3：函数的参数  可以都有默认值？当然可以
#4：函数为啥要加参数？提高函数的复用性 功能可定制
#5：位置定义的时候位置参数 形参 调用函数的时候 实参
#6：关于形参的个数：形参有几个，那么你调用的时候就必须传几个 不能多不能少
#7：形参 函数的参数 是按照顺序赋值
#8：但是如果你加了形参的名字 指定变量值 那么顺序就没有关系了
#9：默认参数 它必须放在形参后面
#10：如果有默认参数 你不给默认参数传值 那么函数就取默认值
#如果传值 就取传递的值

#动态参数 * --> 不定长参数 --> 可以输入无数个参数
# def print_msg(*a):
#     print("a的参数值",a)
#     # print("b的参数值：",b)
# # print_msg(1,2,3,4,5)
# t_1=[[1,2,3],[4,5]]
# # d_1={"age":18,"sex":'girl'}
# print_msg(*t_1) #加*号 就相当于脱外套  只能脱一层
#字典是无序的

#关键参数 **kwargs
def print_msg(**a):
    print(a)

d_1={"age":18,"sex":'girl'}
# print(d_1)
print_msg(**d_1)