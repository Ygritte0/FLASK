#-coding: -utf-8--
# a = 8
# b = 1
# print(a+b)


a = 2
b = 2

if (a is b):
    print("1. a 和 b 有相同的标志")
else:
    print("1. a 和 b 没有相同的标志")

if (id(a) == id(b)):
    print("2. a 和 b 有相同的标志")
else:
    print("2. a 和 b 没有相同的标志")

b = 4
if (a is b ):
    print("3.a 和 b 有相同的标志")
else:
    print("3.a 和 b 没有相同的标志")

if (a is not b):
    print("4.a 和 b 没有相同的标志")
else:
    print("4.a 和 b 有相同的标志")