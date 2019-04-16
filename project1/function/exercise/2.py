#-*-coding:utf-8-*-
# list1 = [8, 2, 3, 0, 7]

def sum(list):
    n = 0
    sum = 0
    while n < 5:
        sum += list[n]
        n += 1
    return sum

print(sum([8, 2, 3, 0, 7]))

# def list2_sum(a):
#     n = 0
#     while n < 5:
#         print(n)
#         n += 1
#     return n
#
# list2_sum(1)


# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total

# print(sum((8,2,3,0,7)))