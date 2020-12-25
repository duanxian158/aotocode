
#while 循环 关键字 while
#while 条件表达式：
    #while 代码块

age=18
i=0
while age>=18:
    print('我18岁啦')
    i += 1
    if i==5:
        break

#先判断 后执行代码块，执行完了之后 继续判断 根据判断结果执行
#反复判断
#break 跳出当前循环
#题目：只打印5次
#怎么避免死循环
#1）用变量来控制  2）结合break  和if语句来执行