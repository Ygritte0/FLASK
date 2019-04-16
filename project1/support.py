#- coding: utf-8--
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython 路径为：', sys.path, '\n')

# def print_func(par):
#     print("Hello:", par)
#     return



from fibo import fib
print(fib(500))

print("++++++++++++++")

from fibo import fib2
print(fib2(500))


if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')