#-*-coding:utf-8-*-
str ="1234abcd"
def string_reverse(str1):
    rstr1 = ""    # 定义rstr1的类型是字符串，并且是空字符串
    index = len(str1) # 利用长度函数获得字符串的索引
    while index > 0:
        rstr1 += str1[index - 1]  # 获取索引为 index - 1 的元素，即字符串中最后一个元素
        index -= 1  # 直到 index = 0 ,循环体while结束
    return rstr1

print(string_reverse("1234abcd"))