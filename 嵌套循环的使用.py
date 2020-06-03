"""
输入一下图形
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
# i=0
# j=0
# for i in range(1,6):
#     # print(i)
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(  )
"""
打印*
*
**
***
****
*****
******
"""
#代码
# for i in range(2,7):
#     # print(i)
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print( )

"""
打印 *
* * 
* * * 
* * * * 
* * * * * 
* * * * * *
'''
"""
#代码

for i in range(1,7):          #外层循环,遍历行数
    # print(i)
    for j in range(1,i+1):    # 内层循环，根据遍历的行数打印数据（根据行数打印数据，第1行，打印1，第二行，打印1，2 第三行，打印1，2，3,...）
        print("*",end=" ")
    print( )

# i=0
# while i<10:
#     for j in range(1,10):
#         print('i=',i,'j=',j)
#     i+=1
