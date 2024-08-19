""" 
    求和1-100
"""

# sum = 0

# for x in range(101):
#     sum += x

# print(sum)


""" 
    求1-100的偶数和
"""

# sum1 = 0

# # for x in range(2,101,2):
# #     sum1 += x

# for x in range(101):
#     if x % 2 ==0:
#         sum1+=x

# print(sum1)


""" 
    game guess number
"""

# import random

# answer = random.randint(1,100)
# counter = 0

# while True:
#     counter += 1
#     number = int(input("please input number"))
    
#     if number < answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你答对了')
#         break
# print('你总共猜了%d次' % counter)


""" 
    99乘法表
"""

# for i in range(1,10):
#     for j in range(1,10):
#         print('%d*%d=%d' % (i,j, i*j), end='\t')
#     print()

from math import sqrt

print(sqrt(10))