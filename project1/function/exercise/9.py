#-*-coding:utf-8-*-
# 查看所给参数是否为质数
# def prime_number(number1):
#     if number1%2 = 0 :
#         print("number1 is not a prime number.")
#
#
# print(prime_number(3))


def test_prime(n):
    if n==1:   # 首先要分类，1和2要单独讨论，并且1和2都是质数
        return False
    elif n==2:
        return True
    else:
        for x in range(2,n):  # 当n > 2 时，
            if n % x == 0:
                return False
            return True

print(test_prime(5))