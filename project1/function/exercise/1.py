#-*-coding:utf-8-*-


# def max_of_two(x, y):
#     if x > y:
#         print(x)
#         return x
#     else:
#         print(y)
#         return y
#
# a = max_of_two(1, 2)
#
# b = max_of_two(3, 4) + max_of_two(2, 1) + 2
#
#
# def max_of_three(x, y, z):
#     x + y
#
#
#
# # return max_of_two(x, max_of_two(y, z))
#
# def max_of_four(w, x, y, z):
#     return max_of_two(w, max_of_three(x, y, z))
#
# print(max_of_three(1,2,3))


def print_variables(a, b, *args, **kwargs):
    print(args)
    print(kwargs.get('name'))


print({'name':'zm'} == dict(name='zm'))

print_variables(1, 2, [1, 2, 3], 4, name='zm')