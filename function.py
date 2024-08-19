""" 
    实现计算求最大公约数和最小公倍数
"""

# def gcd(x,y):
#     (x,y) = (y,x) if x > y else (x,y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
        
# def lcm(x,y):
#     return (x * y) // gcd(x, y)
    
# print(gcd(12,24))
# print(lcm(12,24))

""" 
    判断是不是回文数
"""

# def is_palindrome(num):
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //=10
#     return total == num

# print(is_palindrome(12314321))



def foo():
    b = 'hello'

    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()