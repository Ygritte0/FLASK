
def list_multiply(list0):
    multiply = 1
    for x in list0:
        multiply *= x
    return multiply

print(list_multiply([8, 2, 3, -1,7]))


# def multiply(list):
#     n = 0
#     multiply = list[0]
#     while n < 5:
#         multiply *= list[n]
#         n += 1
#     return multiply
#
# print(multiply([8, 2, 3, -1, 7]))