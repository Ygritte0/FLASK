# -*- coding: utf-8--

f = open("D:/workspace/project1/foo.txt ","rb+")
f.write(b"0123456789abcdef")

a = f.seek(3,0)
print(a)

b = f.read(4)
print(b)
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# str = f.readlines()
# print(str)


# for line in f:

#     print(line, end='')


# num = f.write("Python!")
# print(num)


# value = ('www.runoob.com我', 14)
# s = str(value)
# f.write(s)
#
# d = f.tell()
# print(d)

# with open ('D:/workspace/project1/foo.txt ', 'r') as f:
#     read_data = f.read()
# f.closed
# print(f.closed)

# f.close()
# f.read()


import pickle,pprint


data1 = {'a':[1,2.0,3,4+6j],
         'b':('string',u'Unicode string'),
         'c':None}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open('data1,pkl','wb')
pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)


# pkl_file = open('D:/workspace/project1/data.pkl','w+')
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()