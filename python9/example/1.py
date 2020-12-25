
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=j) and (i!=k) and (j!=k):
#                 print(i,j,k)
#
#Python 练习实例9
#暂停一秒输出。
# import time
# myd={1:'a',2:'b'}
# for key,value in dict.items(myd):
#     print(key,value)
#     time.sleep(1) #暂停1S

# Python 练习实例10  暂停一秒输出，并格式化当前时间。
#Python 练习实例11：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
# 问每个月的兔子总数为多少？
#Python 练习实例12 判断101-200之间有多少个素数，并输出所有素数。
# count=0
# for i in range(101,200):
#     leap = 'true'
#     for j in range(2,i):
#         if i%j==0:
#             leap='false'
#             break
#     if leap=='true':
#         print('素数：%d'%i)
#         # print('%s' % i)
#         count += 1
# print('The total is %d'%count)

#Python 练习实例13打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方
# for i in range(100,1000):
#     h=int(i/100)   #百位
#     t=int(i/10%10)  #十位
#     a=int(i%10)  #个位
#     if i==(a**3+t**3+h**3):
#         print(i)

#Python 练习实例14将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# n=int(input('请输入一个正数：'))
# # n=90
# print ('{0} = '.format(n),end='')
# # if not isinstance(n, int) or n <= 0 :
# #     print ('请输入一个正确的数字 !')
# #     exit(0)
# # elif n in [1] :
# #     print ('{}'.format(n))
# while n not in [1]:
#     for index in range(2,n+1):
#         if int(n%index)==0:
#             n=int(n/index)
#             if n==1:
#                 print(index)
#             else:
#                 print('{0} *'.format(index),end='')
#             break

#Python 练习实例15利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
while True:
    score=int(input('请输入一个分数：'))
    if score>=90:
        print('A')
    elif score in range(60,90):
        print('B')
    else:
        print('C')
    yes_or_no=input('是否要继续？按y继续，按n退出')
    if yes_or_no=='n':
        break
