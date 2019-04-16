# -*-coding:utf-8--
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is ", result)
    finally:
        print("executing finally clause")

a = divide(2, 0)
print(a)