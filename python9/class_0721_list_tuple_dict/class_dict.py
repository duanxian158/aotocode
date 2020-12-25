
#字典 dict {}
#1：它的值 也可以是任何数据类型
#2：存储值的格式不一样 key-value 键值对
#3：取值 字典无序 字典名[key值]
#4：key值是唯一的  如果不唯一  前面的值会被覆盖掉
#key
dict_1={'s_1':'sunny','s_2':'紫宸','s_3':'听风','s_4':'one','s_1':'mony'}
#dict_2={2:3} #写法不规范
#print(dict_1['s_1'])
dict_2={'name':'ami','age':'18','heigh':'1.75'}
#字典 可以增删改
#增加  字典名[key] key不存在  如果存在的话 value就会被替换
#dict_2['sex']='girl'
#修改 字典名[key]=new_value  key必须是存在
#dict_2['age']=5
#删除 字典名.pop(key)
#dict_2.pop('age')
print(dict_2)