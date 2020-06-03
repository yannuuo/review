#集合定义：通过{}来表示的
#都变成大写
# a='jjj'
# b=a.upper()
# print(b)
# #字母首字母大写
# b1=a.capitalize()
# print(b1)
# name=" aleX "
# v=name.strip()    #.strip()移nn除指定字符串，空白，/t，/n等转义字符  strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# print(v)
#
# name='abcd'
# x=name[:3]
# print(x)
# s=name[2:4]
# print(s)
# f=name.index("a")
# print(f)


name="aleX"
n=len(name)
idex=0
while idex<n:
    v=name[idex]
    if v=='e':
       print(idex)
       break
    else:
      idex+=1