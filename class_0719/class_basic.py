#规范：1：命名不能以数字开头
#2：数字 字母 下划线组成
#3：一般字母都是小写的
#4：不同的字母之前是用下划线隔开的
#5:模块名 项目名 包名 变量名 都不能使用关键字
#语法：
#变量 x=1 y=5
a=1
print(a)#把内容输出到控制台
#数据类型 整数 浮点数 字符串
#整数 int type(你要判断的值) 获取数据的类型
#a=1
#s='aaa'
#s_2 = '"hello" python'
#f=11.2
#print((type(a),type(s),type(s_2),type(f)))
#print(s_2)
#布尔值 boolean True False
#拼接 字符串之间的拼接
s_1 = 'hello'
s_2 = "python"
a=1
print(s_1+'华华'+'小幸福'+s_2)
#字符串 与整数拼接  1：加逗号  2：转换数据类型
print(s_1,a) #输入2个变量
print(s_1+str(a))
#格式化输出
#{0} 占了一个坑 表示这里要填入一个坑
name='橘子'
name_1="菜菜"
print("pyhton 9 期有一个学生的名字叫做：{0}、{1}".format(name,name_1))
print("pyhton 9 期有一个学生的名字叫做：%s,%s"%(name,name_1))
#%s %d %r %f