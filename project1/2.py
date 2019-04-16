# -- coding: utf-8--
# numbers = []
# strings = []
# names = ['John', 'Eric', 'Jessica']
#
# # write your code here
# second_name = 'Green'
# numbers.append(3)
# strings.append('Hello')
# print(numbers)3
# print(strings)
# print(f"The second name on the names list is {second_name}" )
# this code should write out the filled arrays and the second name in the names list (Eric)

# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = odd_numbers + even_numbers
# print(all_numbers)
#
# print([1,2,3] * 3)

# x = object()
# y = object()
#
# x_list = [x] * 10
# y_list = [y] * 10
# big_list = x_list + y_list
#
# print("x_list contains %d object" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))
#
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there ...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")


# name = "John"
# age = 23
# # print("Hello, %s!" % name)
# print("%s is %d years old." % (name, age))

# mylist = [1,2,3]
# print("A list: %s" % mylist)
#
# x = 'a'
# y = 'b'
# print(x)
# print(y)
# print('------------')
#
# print(x,end='')
# print(y,end='')


import sys
print('=======================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv,path
print('++++++++++++++++++++++++++')
print('path:',path)

a = 3
a += 3

