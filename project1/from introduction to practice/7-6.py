#-*-coding:utf-8-*-
# 用以下方式重新完成7-4和7-5的练习
# 1.在while 循环中使用条件测试来结束循环
# 2.使用变量active 来控制循环结束的时机
# 3.使用break 语句在用户输入‘quit’时退出循环


pizza_elements = ''
active = True
while active:
    print("Please tell the elements of a pizza.")
    print("(Enter 'q' at any time to quit.)")
    p_elements = input("pizza_elements:")
    if p_elements == 'q':
        active = False
    else:
        print("We would like to add " +  ' ' + p_elements + ' '" to our pizza.")