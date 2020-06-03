"""
字典是可变的数据类型，是以键值对的形式存在的，
字典中的key是唯一不变的，不能重复
key只可能是不可以变的数据类型（建议用字符串）
不可变的数据类型包括：数值（整数，浮点数，布尔值）、元组、字符串
可变的数据类型包括：列表、字典、集合
"""

dic={'姓名':'小米','年龄':18,'身高':198}
#字典的值的读取，通过对应键的去读取对应的值
# x=dic['姓名']
# print(x)
#字典的增删改查的方法
"""
字典的增加和修改
有则改，无则增加
通过键直接赋值，就可以增加元素
"""
# dic['姓名']=22
# dic['体重']=56
# print(dic)
# #一次性增加多个元素,使用update关键字
dic.update({'颜色':'白色','大小':'大'})
# print(dic)
# #删除的方法
# pop方法，使用键进行删除，指定的键值对  返回值为被删除的值
# a=dic.pop("大小")
# print(a)
# print(dic)
#随机删除popitem()
print(dic)
a1=dic.popitem()
print(dic)
print(a1)
a2=dic.popitem()
print(dic)
print(a2)
a3=dic.popitem()
print(dic)
print(a3)
# #删除关键字del (可以删除任何你想想删除的数据)
# del dic['大小']
# # print(dic)
# # # del dic
# # print(dic)
# #查找数据的方法
# #1。通过键去查找对应的数据值
# x=dic['姓名']
# print(x)
# #2.通过get的方法，通过键去查找这个键对应的值，如果没有找到的话，会返回一个none
# x=dic.get('姓名')
# print(x)
# #扩展 dic.get("jdsk",dd) 如果在这个字典里，没有找到就不会返回一个None,会返回一个dd,及可以手动控制找不到元时将会返回的值
# x1=dic.get('kk','jj')  #返回的是dd
# print(x1)
#获取字典里所有的键 keys
# x2=tuple(dic.keys())  #取出的值放到一个元组里
# x3=list(dic.keys())   # 取出的值放到一个列表里
# print(x3)
# #获取字典里所有的值，values
# x4=tuple(dic.values())#取出的值放到一个元组里
# print(x4)
# x5=list(dic.values())# 取出的值放到一个列表里
# print(x5)
#取出所有的键值对 items
# # x6=list(dic.items())[0]#取列表里的第一个值
# x7=list(dic.items())
# # print(x6)
# print(x7)
# # #字典的定义方式扩展
# # #直接定义dic={'姓名':'小米','年龄':18,'身高':198}
# # #使用dict这个内置函数进行定义
# # dic1=dict(name="小明", age=18, gender="男")
# # print(type(dic1))
# # #第三种：使用dict内置函数
# x=[("aa", 11), ("bb", 22), ("cc", 33)]
# dic3=dict(x)  #与items是相反的。list(dic.items())是将字典转换成键值对
# print(dic3)
