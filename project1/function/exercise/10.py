#-*-coding:utf-8-*-
# 拿列表里的偶数
def even_list(list1):
    for x in list1:
        if (x % 2 != 0):
            list1.remove(x)
            # list1.index.pop(x)
    return list1

print(even_list([1,2,3,4,5,6,7,8,9]))