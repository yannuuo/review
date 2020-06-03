# l1=['小花','小明','花生']
# for name in l1:
#     print(name)
# l2=('苹果','香蕉','橙子')
# for s in l2:
#     print(s)
# l3='d','f','h'
# for x in l3:
#     print(x)
#直接遍历字典 得到是字典的键
# l4={'姓名':'画画','年龄':'19','大小':'大大'}
# a=list(l4.values())  #得到的是字典的值
# # print(a)
# for c in a:
#     print(c)
# a=tuple(range(1,6))
# print(a)
# for i in range(6):
#     print(i)
"""
range(n)默认门生成0到n-1的整数序列,对于这个整数序列我们可以通过list()函数进行转换为列表类型的数据
range(n,m)默认生成n到m-1的整数序列,对于这个整数序列我们通过list()函数进行转换为列表类型的数据
range(n,m,k)相当于其他函数里的for循环,n为初始值,m-1为结束值 k为步长会生成递增或者递减的整数序列
"""
#例子生成100遍hell pyhton
#遍历range
# l1=list(range(100))
# for i in l1:   #l1是个列表,进行遍历
#     print("第{}遍,hello python".format(i+1))
# print(l1)
# l5=[1,2,3,4,5,6]
# for i in l5:
#     print(i)
#遍历字符串
# l6='abcdefghijklmn'
# for i in l6:
#     print(i)
# #遍历列表
# l7=[1,2,3,4,5,6,7]
# for i in l7:
#     print(l7)  #打印7遍列表
#     print(i)
#遍历字典
l4={'姓名':'画画','年龄':'19','大小':'大大'}
#直接遍历,得到的是字典的键
# for i in l4:
#     print(i)
# #遍历字典的值
# for s in l4.values():
#     print(s)
#遍历字典的键值对
for a,v in l4.items():
    print(a)
    print(v)
#元组的拆包
l8=(11,33,44,55,66)
for i in l8:
    print(i)

    #这是增加的一段代码