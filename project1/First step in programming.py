#- coding:utf-8--
# a,b = 0,1
# while b < 10:
#     print(b)
#     a,b = b, a+b
#
#
# print("===============")
#
# var1 = 100
# if var1:
#     print("1-if 表达式条件为True")
#     print(var1)
#
# var2 = 0
# if var2:
#     print("2_if 表达式条件为True")
#     print(var2)
#
# print("Good bye!")
#
# print("++++++++++++++++++")
#
# age = int(input("请输入你家狗狗的年龄："))
# print("")
# if age < 0:
#     print("你是在逗我吧！")
# elif age == 1:
#     print("相当于14岁的人。")
# elif age == 2:
#     print("相当于22岁的人。")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("对应人类年龄：", human)
#
# input("点击enter键退出")


# 猜数字游戏
# number = 7
# guess = 'None'
# print("数字猜谜游戏！")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")


num = int(input("输入一个数字："))
if num%2 == 0:
    if num%3 ==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2，但不能整除3")
else:
    if num%3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")