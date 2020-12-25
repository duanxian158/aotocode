
#题目：输出 9*9 乘法口诀表。
for i in range(1,10):

    for j in range(i,10):
        print ('%d*%d=%d'%(i,j,i*j),end=' ')
        j+=1
    i+=1
    print()