#-*-coding:utf-8-*-
# height = 1
# weight = 1


a = input('weight: ')
b = input('height: ')
weight = int(a)
height = float(b)

BMI = weight / (height*height)
if BMI < 18.5:
    print("过轻")
elif 18.5<=BMI<25 :
    print('正常')
elif 25<=BMI<28:
    print('过重')
elif 28<=BMI<32:
    print('肥胖')
else:
    print('严重肥胖')



