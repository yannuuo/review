# print(12,end="\n")
# print(2)
# print('成绩：'"23")
# l='python hello'
# s=l[7:]
# s1=l[2]  #字符串的截取从左边往右是从下标0开始截取的，从右往左截取是从下标-1开始截取
# print(s1)
# print(s)
#逻辑运算 and  or  not(取反)
# print(10<3 and 2>4)
# print(10<3 or 4>3)  #假假为假 一真一假为真

# a=['a','s','g']
# x=2
# print(2  in a)
# print(2 not in a)
#随机数模块 random
# import random
# import decimal
# #指定范围生成一段随机整数（包含边界）
# a=random.randint(1,4)
# print(a)
# #生成0-1的随机小数
# b=random.random()
# print(b)
# s=2.89
# z=0.3
# s1=s-z
# print(s1)
# #解决浮点数精度问题 使用decimal模块进行装换，但是要先将数字转字符穿类型
# s2=decimal.Decimal('2.89')
# z1=decimal.Decimal('0.3')
# print(s2-z1)
#将字符串都变成大写
a='jjj'
b=a.upper()
print(b)
#字符串首字母大写
b1=a.capitalize()
print(b1)



import random
import numpy as np

a = random.randint(10, 20)
res = np.random.randn(5)
ret = random.random()
print("正整数:" + str(a))
print("5个随机小数:" + str(res))
print("0-1随机小数:" + str(ret))

#字符串的拼接
# a='2'
# c='3'
# d=a+','+c
# d1=','.join((a,c))
# print(d1)
# import random
# num=random.randint(10000000,99999999)
# number='130'+str(num)
# print(number)
"""
1、现有字符串    str1 = "PHP is the best programming language in the world! "

      要求一：将给定字符串的PHP替换为Python      

      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
"""
str1 = "PHP is the best programming language in the world! "
str3=str1.replace('PHP','python')
print(str3)
st2=str3.split( )
print(st2)
"""
2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”（要求：使用上课学过的知识点来做） 
"""
time=int(input("请输入1-7之间的数字："))
# l1=["周一",'周二','周三','周四','周五','周六','周日']
# l2=l1[time-1]
# print('今天是{}'.format(l2))
#方法二：
if time==1:
    print("今天是周一")
elif time==2:
    print("今天是周二")
elif time==3:
    print('今天是周三')
elif time==4:
    print('今天是周四')
elif time==5:
    print('今天是周五')
elif time==6:
    print('今天是周六')
elif time==7:
    print('今天是周日')
else:
    print("输入不合法")
