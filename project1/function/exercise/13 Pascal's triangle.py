#-*-coding:utf-8-*-
# def pascal_triangle(list1):
#     list1 = [1]
#     list2 = [1,1]
#     list3 = [1,2,1]
#     list4 = [1,3,3,1]
#     list5 = [1,4,6,4,1]
#     listn[m] = [1,list(n-1)[m-1]+list(n-1)[m],1]

# 标答
# def pascal_triangle(n):
#     trow = [1]
#     y = [0]     # 作用？
#     for x in range(max(n,0)):
#         print(trow)
#         trow = [1+r for l, r in zip(trow+y,trow+y)]  # zip 的用法忘了。。
#     return n>= 1
# pascal_triangle(6)

# answer by xiaozhu
# 分两步走，第一步先定义一下行之间的关系
def pascal_triangle_line(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    line_n_minus_1 = pascal_triangle_line(n - 1)
    line_n = []
    for i in range(n):
        if i in (0, n - 1):  # 此处的(0， n - 1)是一个元组！
            line_n.append(1)
            continue   # 结束当前迭代，并跳到下一次迭代的开头，即跳到29行，该代码块执行两次
        line_n.append(line_n_minus_1[i] + line_n_minus_1[i - 1])
    return line_n

# 第二步，定义三角
def pascal_triangle(n):
    result = []
    for i in range(1, n+1):  # 范围？
        result.append(pascal_triangle_line(i))
    return result

print(pascal_triangle(7))
