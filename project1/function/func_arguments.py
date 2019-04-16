#-*-coding:utf-8-*-
def power(x):
    return x * x

# print(power(2))


def power(x, n):
    s = 1
    while n > 0:
        n -= 1
        s *= x
    return s

# print(power(25,3))


def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end([1,2,3]))
print(add_end())
print(add_end())

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum

print(calc(1))