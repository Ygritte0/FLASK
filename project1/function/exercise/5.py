#-*-coding:utf-8-*-
# 定义一个函数，计算数的阶乘
def factorial_of_number(number1):
    n = number1
    total = n
    while n > 2:
        total = total * (n - 1)
        n -= 1

    return total

print(factorial_of_number(7))
