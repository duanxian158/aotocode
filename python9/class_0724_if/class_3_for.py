
#for 循环 关键 90%
#第一个作用：遍历元素
#for item in 数据范围:#str list dict tuple 其它类型的数据范围
    #item是代表数据范围里面每一个元素
# str_1='python9'
# tuple_1=(1,2,[2,5])
# dict_1={'age':'18','sex':'男'}
# print(dict_1.keys())
# print(dict_1.values())
# for item in dict_1.values():
#     print(item)

#range函数 range(m,n,k) 起始值 结束值 步长
#range 函数 生成指定范围的整数序列  数据集全
# a=list(range(1,8,1))#强制换成列表list()
#range(4)#默认从0开始
# a=list(range(6,0,-2))
# print(a)

str_1='python9'
#如果我要用Range 来打印出str_1里面的每一个元素
#我要利用下标打印出str_1里每一个元素
for i in range(7):
    print(str_1[i])