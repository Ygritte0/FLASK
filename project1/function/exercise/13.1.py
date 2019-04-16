#-*-coding:utf-8-*-
# 思路：
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# 每个列表的第一个和最后一个元素都是1，而其他元素的值都取决于上一行的元素。比如可以归纳出：第n行的索引为m的元素，
# 是由上一行索引为m-1,m 的两个数相加而来
# 因此，先定义一下前后两行的关系
def pascal_triangle_line(n):
    if n == 1 :
        return [1]
    if n == 2 :
        return [1,1]
    line_minus_1 = pascal_triangle_line(n-1)
    line_n = []
    for i in range(n):   # 除了第一个和最后一个元素外的其他元素的定义
        if i in (0,n-1):
            line_n.append(1)
            continue
        line_n.append(line_minus_1[i-1] + line_minus_1[i])
    return line_n

def pascal_triangle(n):
    result = []
    for i in range(1, n+1):  # 范围？
        result.append(pascal_triangle_line(i))
    return result

print(pascal_triangle(7))