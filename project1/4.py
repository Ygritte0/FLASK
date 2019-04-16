#-coding:utf-8--

list1 = ['Rob','Sansa','Arya']
list2 = [1,2,3,4,5]
print("list1[0]:",list1[0])
print("第三个元素为:",list1[2])
list1[2] = 'John'
print("更新后的第三个元素为：",list1[2])
print("原始列表：",list1)
del list1[2]
print("删除第三个元素：",list1)

print("list2[1]:",list2[1])
