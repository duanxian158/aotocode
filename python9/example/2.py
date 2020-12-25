
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
# 低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
# #高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# #高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# list_1=[1000000,600000,400000,200000,100000,0]
# list_2=[0.01,0.015,0.03,0.05,0.075,0.1]
# d=int(input('净利润：'))
# sum_1=0
# for item in range(0,6):
#     if d>list_1[item]:
#         sum_1+=(d-list_1[item])*list_2[item]
#         print(float(d-list_1[item])*list_2[item])
#         d=list_1[item]
# print(sum_1)

#Python 练习实例16 输出指定格式的日期
# import datetime
# # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
# print(datetime.date.today())

#Python 练习实例17 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# s=input('输入一个字符串：')
# letters=0
# space=0
# digit=0
# others=0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))

#Python 练习实例20一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
hei=100
tour=[]
height=[]
tim=10
for i in range(1,tim+1):
    tour.append(hei)
    # if i==1:
    #     tour.append(hei)
    # else:
    #     tour.append(2*hei)
    hei/=2
    height.append(hei)

print('第10次落地时，共经过{0}米'.format(sum(tour)))
print('第10次反弹{0}米'.format(height[-1]))


