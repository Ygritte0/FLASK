#-*-coding:utf-8-*-
def new_list(list1):
    unique_list = set(list1)
    return list(unique_list)

print(new_list([1,2,2,2,3,3,5,5]))