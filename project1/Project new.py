# mystring = "hello"
# myfloat = 8.0
# myint = 9
#
# if mystring == "hello":
#     print ("string: %s"% mystring)
# if isinstance(myfloat, float) and myfloat == 8.0:
#     print ("myfloat %f" % myfloat)
# if isinstance(myint,int) and myint == 9:
#     print("integer: %d " % myint)


# mylist = []
# mylist.append(1)
# mylist.append(2)
# mylist.append(3)
# # print(mylist[0])
# # print(mylist[1])
# # print(mylist[2])
#
# # print(">" * 50)
#
# for x in mylist:
#     # x = 3
#

mylist = []
x = 0

while x < 10:
   mylist.append(x)
   x += 1
   print(x)
print("**********")
mylist2 = list( range(1,11))
print(mylist2)


print("===========")
mylist4 = []
for i in range(1,11):
    print(i)

print("++++++++")
mylist3 = [i for i in range (1,11)]
mylist3.append(i)
print(i)

##########
numbers = []
strings = []
names = ["John","Eric","Jessica"]
second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

print (numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print("*************")

remainder = 11 % 3
print(remainder)


squared = 8 ** 2
cubed = 2 ** 4
print(squared)
print(cubed)


lotsofhellos = "hello" * 10
print(lotsofhellos)