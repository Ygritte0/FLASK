#-coding:utf-8--
# n = 100
#
# sum1 = 0
# counter = 1
# while counter <= n:
#     sum1 += counter
#     counter += 1
#
# print("1到 %d 之和为： %d" %(n,sum1))
#
# print('==================')
# var = 1
# while var == 1:
#     var = int(input("输入一个数字："))
#     print("你输入的数字是：", var)
# else:
#     print("Good bye!")

print(">>>>>>>>>>>>>>>>>>>>")

count = 0
while count < 5:
    print(count,"小于5")
    count += 1
else:
    print(count,"大于或等于5")

print("--------------------")

# flag = 1
# while (flag): print('欢迎！')
# print("Good bye!")


# languages = ['C','C++','Perl','Python']
# for x in languages:
#     print(x)
#
#
# print('```````````````````')
#
# sites = ['Baidu','Google','Taobao','Runoob']
# for site in sites:
#     if site == 'Runoob':
#         print("菜鸟教程！")
#         break
#     print('循环数据' + site)
# else:
#     print('没有循环数据！')
# print('完成循环！')
#
#
# print('@@@@@@@@@@@@@@@@@@@@@@@')
#
# for i in range(-10,-100,-30):
#     print(i)


a = ['Google','Baidu','Runoob','Taobao','QQ']
for i in range(len(a)):
    print(i, a[i])


print('===================')

# list(range(5))

for letter in 'Runoob':
    if letter == 'b':
        break
    print('当前字母为：', letter)


var = 10
while var > 0:
    print('当期变量值为：', var)
    var -= 1
    if var == 5:
        break
print("Good bye!")

print("+++++++++++++++++++++++++")

for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母：', letter)


# var = 10
# while var > 0:
#     var -= 1
#     if var == 5:
#         continue
#     print('当前变量值：', var)
# print("Good bye!")


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, '等于', x,'*', n//x)
            break
    else:
        print(n,'是质数')

print('=====================')
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行pass块')
    print('当前字母：', letter)

