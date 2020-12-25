
#函数
#type()  print() input() len() str()
#列表  append()  pop()  insert(i,value)
#range() upper()  lower()

#函数的特点：
#1：拿来主义  拿来就可以用
#2：不需要定义 想用就用

#函数的语法：
#def 函数名(参数1,参数2,参数3,...):
    #函数体(你要该函数实现的功能是什么？)

#函数的调用：函数名(参数1,参数2,参数3)

#入门级函数
# def print_msg():
#     print("msg")
#
# print_msg()#调用函数

#加参数的函数 形参--形式参数
# def great_user(name,content):
#     print(name+content)
#
# great_user('橘子','晚上好呀！')#实参
#默认参数必须放在位置参数（形参）的后面
#如果你不传参 那我就取默认值  如果你传参了 选你的值
#函数运行的结果是：函数体的代码执行的结果
#默认参数可以有无数个  无数个  按照语法来就可以了

#动态参数  你想回就加几个
# def add(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)
#
# add(1,2,3)

#关键字参数  **kwargs  key word
# def print_msg(**kwargs):
#         print(kwargs)
# print_msg(x=1,y=2,z='你好')

#return  关键字  返回一个值
# def add_1(a,b):
#     print(a+b)
# def add_2(a,b):
#     return a+b  #返回值
# add_1(5,5)
# a=add_2(6,6)
# print(a)
# print(add_2(5,6))

def add_2(x,y):
    return x+y
def add_1(a):
    b=add_2(a,5) #函数的调用
    return '666' #函数体内 return  后面的代码不执行
    print(a+b)
add_1(5)
