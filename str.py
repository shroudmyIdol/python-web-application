# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='\n')
# a=5
# b=10
# print(f'{a} * {b} = {a*b}')


# from sys import getsizeof


# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(getsizeof(f))  # 查看对象占用内存的字节数
# f = (x ** 2 for x in range(1, 1000))
# print(getsizeof(f))
# print(f)
# for val in f:
#     print(val)

def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b, a+b
        yield a
        
def main():
    for val in fib(20):
        print(val)
        
        
if __name__ == '__main__':
    main()