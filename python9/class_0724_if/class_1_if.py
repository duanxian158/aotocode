
#if 条件语句 80%
#if else 判断你语句的走向 控制流
#1：最简单的if判断语句：if
#2：复合语句：if...else...
#用缩进来控制 级别
# age=18
# if age>18:
#     print('你成年了！')
# else:
#     print('你未成年')
# print(age)

#if语句：if 后面跟的 比较表达式 比较运算 条件
#if后面的条件语句 运算结果是 布尔值 True 或 False
#if...else else后面不能加任何条件  而且整个if语句里面只能有一个else结尾
#3：if elif else 可以有多个elif,elif后面必须加条件
# score=60
# if score>=60:
#     print('ji ge')
# else:
#     print('bu ji ge')
# if score>=60:
#     print('ji ge11')
# else:
#     print('bu ji ge22')

age=18
sex='girl'
if age>=18:
    if sex=='girl':
        print('shi ge nv hai')
    elif sex=='boy':
        print('shi ge na hai')
elif age<18:
    if sex=='girl':
        print('shi ge nv hai')
    elif sex=='boy':
        print('shi ge na hai')