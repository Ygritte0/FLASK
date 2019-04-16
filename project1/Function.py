#-coding:utf-8--
# def hello():
#     print("Hello World!")
#
# hello()
#
#
# def area(width, height):
#     return width * height
#
# def print_welcome(name):
#     print("Welcome", name)
#
# print_welcome("Runoob")
# w = 4
# h = 5
# print("width =", w, "height =", h, "area =", area(w,h))
#
#
#
# def printme(str):
#     print(str)
#     return
#
#
# printme("我是赵梦")
# printme("再次调用函数！")

# def ChangeInt(a):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print(b)
#
# print("++++++++++++++")

# def changeme(mylist):
#     mylist.append([1,2,3,4])
#     print("函数内取值：", mylist)
#     return
#
# mylist = [10,20,30]
# changeme(mylist)
# print("函数外取值：", mylist)
#
# print("===============")
#
# def printifo(name, age=1):
#     print("名字：", name)
#     print("年龄：", age)
#     return
#
# printifo( name = "Judy")
#
#
#
# print('======================')
#
# def printifo(arg1, arg2,*vartuple):
#     print("输出：")
#     print(arg1,arg2)
#     print(vartuple)
#
# printifo(70,88,10,90,30)
#
#
# def printifo(arg1, *vartuple):
#     print("输出：")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
# printifo(70,88,10,90,30)
#
#
# def printifo(arg1, **vardict):
#     print("输出：")
#     print(arg1)
#     print(vardict)
#
# printifo(70,a=4,b=8)
#
# def f(a,b,*,c):
#     return a+b+c
#
# print(f(1,2,c=4))
#
#
#
# sum = lambda arg1,arg2,:arg1 + arg2
# print(sum(1,3))
#
#
#
# print('==============')
#
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("函数内：", total)
#     return total
# total = sum(10,20)
# print("函数外：", total)
#
# print("++++++++++++++++++++++++++")
#
#
# total = 0
# def sum(arg1,arg2):
#     total = arg1 + arg2
#     print("函数内是局部变量：", total)
#
# sum(10,10)
# print("函数外是全局变量：", total)
#
# print("++++++++++++++++++++++++")
#
# num = 1
# def fun1():
#     global num
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)
#
# print("+++++++++++++++++++++")
#
def outer():
    num = 10
    def inner():
        nonlocal  num
        num = 100
        print("inner:",num)
    inner()
    print("outer:",num)
outer()

print("==================")

a = 10
def test(a):
    a += 1
    print(a)
test(a)