# -*- coding: utf-8--
for x in range(1,11):
    print(repr(x).center(2), repr(x*x).center(3),end=' ')
    print(repr(x*x*x).center(4))


print("+++++++++++++++")
for x in range(1,11):
    print('{0:2d}{1:3d}{2:4d}'.format(x, x*x, x*x*x))

