#-*-coding:utf-8-*-
# 寻找完美数字：该数字的所有因数之和等于这个数
def perfect_number(n):
    sum = 0
    for x in range(1,n):
        if n % x == 0 :
            sum += x
    return sum == n    #

print(perfect_number(49))