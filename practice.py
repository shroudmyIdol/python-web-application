# """
#  寻找水仙花数
# """

# for x in range(100,1001):
#     low = x % 10
#     mid = x // 10 % 10
#     high = x // 100
#     if x == low ** 3 + mid ** 3 + high ** 3:
#         print(x)


""" 
    百钱百鸡
"""

# for x in range(0,20):
#     for y in range(0,33):
#         z = 100 - x - y
#         if 100 == 5 * x + 3 * y + z / 3:
#             print('公鸡%d, 母鸡%d, 小鸡%d' % (x, y, z))

""" 
    花旗股
"""

# import random

# x = random.randint(1,6)
# y = random.randint(1,6)

# sum = x + y
# print(sum)
# if sum == 7 or sum ==11:
#     print('player win!!!')
# elif sum == 2 or sum ==3 or sum ==12:
#     print('banker win!!!')
# else:
#     while True:
#         x = random.randint(1,6)
#         y = random.randint(1,6)
#         print(x + y)
#         if x + y == 7:
#             print("banker win!!!")
#             break
#         elif x + y == sum:
#             print("player win!!!")
#             break
    
    
"""
    斐波那契数列
"""

# x = 0
# y = 1
# for _ in range(0,20):
#     x, y = y, x + y
#     print(x, end=" ")


""" 
    perfect number 1 ~ 9999
"""

# import math

# for num in range(2, 10000):
#     result = ''
#     sum = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result = result + ' ' + str(factor)
#             sum += factor
#             if factor > 1 and num // factor != factor:
#                 result = result + ' ' +  str(num // factor)
#                 sum += num // factor
#     if sum == num:
#         print('num %d = %s' % (sum, result))

"""
找到1-100内的素数
"""
import math

for num in range(2,100):
    is_Flame = True
    for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            is_Flame = False
            break
    if is_Flame:
        print(num, end=" ")