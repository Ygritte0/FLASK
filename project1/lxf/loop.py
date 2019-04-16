#-*-coding:utf-8-*-

# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum += n
#     n -= 2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# i = 0
# while i < 3:
#     print('hello',L[i])
# i += 1


# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n += 1
# print("END")


n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)