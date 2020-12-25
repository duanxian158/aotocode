
#输入三个整数x,y,z，请把这三个数由小到大输出。
# x=input('输入整数:')
# y=input('输入整数：')
# z=input('输入整数：')
# if x>=y and y>=z:
#     print(z,y,x)
# if x>=y and y<=z and x>=z:
#     print(y,z,x)
# if x<=y and y<=z:
#     print(x,y,z)
# if x<=y and y>=z and x<=z:
#     print(x,z,y)

l=[]
for i in range(4):
    x=input('输入整数：')
    l.append(x)
l.sort()
print(l)
